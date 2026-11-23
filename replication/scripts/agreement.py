#!/usr/bin/env python3
"""DRAFT skeleton for AGREEMENT-METHOD.md: normalise editions, align, write blinded judge requests, compute stats.

Status: draft (agree-v1-draft). Deterministic parts only; it never calls a model and uses no paid API. Judges
(Codex, Claude Code, or a human interviewed by one of them) read packet files and write result files; see
replication/judging/README.md. One line schema and one validator (`validate`) serve model and human judges alike.

Usage:
  agreement.py run OUT_DIR --edition NAME=SCHEMA:PATH[,PATH...] [--edition ...] [--lexicon LEXICON_REPO] [--seed 7]
     SCHEMA is gen-v2 | sonnet-edition | lexicon. Later paths override earlier ones for the same concept_id.
  agreement.py register OUT_DIR --judge-id ID --type model|human [--name NAME] [--harness codex|claude-code]
                   [--model MODEL] [--drafted EDITION[,EDITION]] [--size 100] [--overlap 0.3] [--pool-size 50]
                   [--trap-share 0.1] [--batch-size 50] [--salt agree-v1]
     model: writes packets/<id>/batch-NNNN.jsonl with every request it may judge (self-exclusion applied)
     human: draws the seeded, stratified sample (30% from the shared overlap pool) into humans/<id>/sample.jsonl
  agreement.py confirm-model OUT_DIR --slot SLOT --provider P --model-name M (--version X.Y | --version-unknown)
                   --model-reported "<string the harness reports>" [--harness-version V]
     (first session of a model judge: prints the versioned judge id, e.g. anthropic-claude-fable-5-2,
      and writes results/<judge_id>/judge.json; an unknown version is FLAGGED, never guessed)
  agreement.py validate OUT_DIR --judge-id VERSIONED_ID   (checks results/<id>/; exit 1 on any error)
  agreement.py stats OUT_DIR --keys PRIVATE/keys/anon.jsonl   (after results/ exist)

Example (today's two editions plus the reference):
  agreement.py run work/agreement/draft \
    --edition grok=gen-v2:GROK/full-run-grok-bot-20261122/drafts-full.jsonl,GROK/lex-pilot-grok-bot-20261122/drafts-ungrounded.jsonl \
    --edition sonnet=sonnet-edition:SONNET/entries.jsonl --lexicon ../lexicon-91312fec
"""
import argparse, glob, hashlib, itertools, json, os, random, re, sys, unicodedata
from collections import Counter, defaultdict

PROMPT_VERSION = "agree-v1-draft"
NOT_ELICITED, ABSTAIN, EMPTY = "NOT_ELICITED", "ABSTAIN", "EMPTY"
AXIS = {"synonym": "EQUIV", "hypernym": "TAX_UP", "broader": "TAX_UP", "hyponym": "TAX_DOWN",
        "holonym": "PART_UP", "part_of": "PART_UP", "meronym": "PART_DOWN", "uses": "ASSOC", "requires": "ASSOC",
        "certifies": "ASSOC", "related": "ASSOC", "contrast": "CONTRAST"}
INVERSE = {"TAX_UP": "TAX_DOWN", "TAX_DOWN": "TAX_UP", "PART_UP": "PART_DOWN", "PART_DOWN": "PART_UP"}
DEF_SCORE = {"EQUIVALENT": 1.0, "A_NARROWER": .75, "B_NARROWER": .75, "OVERLAPPING": .5, "CONFLICTING": 0.0,
             "DIFFERENT_SENSE": 0.0}

def norm(s):
    s = unicodedata.normalize("NFKC", s or "").casefold()
    s = re.sub(r"\((programming )?language\)|\(software\)", "", s)
    return re.sub(r"[^\w+#]", "", s)

# ---------- step 0: adapters to the canonical entry ----------
def canon_genv2(e):
    links = {k: (e["links"][k]["choice"] if e["links"][k]["choice"] is not None else ABSTAIN)
             for k in ("wikipedia", "wikidata", "wordnet")}
    return {"concept_id": e["concept_id"], "sense": e.get("work_sense"), "sense_from_definition": False,
            "definition": e["definition"]["text"], "definition_basis": e["definition"]["basis"],
            "definition_pointers": e["definition"].get("pointers", []), "links": links,
            "variants": [{"text": v["text"], "conditional": v.get("condition") is not None,
                          "condition": v.get("condition"), "basis": v["basis"]} for v in e.get("variants", [])],
            "relations": [{"type_fine": r["type"], "axis": AXIS[r["type"]], "target_id": r.get("target_id"),
                           "target_label": r.get("target_label"), "proposed_new": bool(r.get("proposed_new")),
                           "basis": r["basis"]} for r in e.get("relations", [])],
            "run": (e.get("_meta") or {}).get("run")}

def canon_sonnet(e):
    return {"concept_id": e["concept_id"], "sense": e["definition"]["text"], "sense_from_definition": True,
            "definition": e["definition"]["text"], "definition_basis": e["definition"]["basis"],
            "definition_pointers": [s.get("identifier") for s in e["definition"].get("sources", [])],
            "links": {k: NOT_ELICITED for k in ("wikipedia", "wikidata", "wordnet")},
            "variants": [{"text": v["label"], "conditional": bool(v.get("ambiguous")), "condition": NOT_ELICITED,
                          "basis": v.get("basis")} for v in e.get("variants", [])],
            "relations": [{"type_fine": NOT_ELICITED, "axis": AXIS[r["type"]], "target_id": r["target"],
                           "target_label": r.get("target_label"), "proposed_new": False, "basis": r.get("basis")}
                          for r in e.get("relations", [])], "run": "edition"}

def canon_lexicon(e):
    return {"concept_id": e["id"], "sense": e.get("definition"), "sense_from_definition": True,
            "definition": e.get("definition"), "definition_basis": None, "definition_pointers": [],
            "links": {k: NOT_ELICITED for k in ("wikipedia", "wikidata", "wordnet")},
            "variants": [{"text": v["label"], "conditional": bool(v.get("needs_context")),
                          "condition": v.get("needs_context") or None, "basis": None} for v in e.get("variants", [])],
            "relations": [{"type_fine": NOT_ELICITED, "axis": AXIS.get(r["type"], "ASSOC"), "target_id": r.get("target"),
                           "target_label": r.get("target_name"), "proposed_new": False, "basis": None}
                          for r in e.get("relations", [])], "run": "reference"}

ADAPTERS = {"gen-v2": canon_genv2, "sonnet-edition": canon_sonnet}

def load_edition(spec):
    name, rest = spec.split("=", 1)
    schema, paths = rest.split(":", 1)
    out = {}
    for p in paths.split(","):
        for line in open(p):
            if line.strip():
                c = ADAPTERS[schema](json.loads(line)); out[c["concept_id"]] = c
    return name, out

def load_lexicon(repo):
    lex = {}
    for f in glob.glob(os.path.join(repo, "entries", "*.json")):
        d = json.load(open(f)); lex[d["id"]] = d
    return lex

# ---------- step 1: deterministic alignment ----------
def name_index(lex):
    idx = defaultdict(set)
    for i, d in lex.items():
        idx[norm(d["preferred_name"])].add(i)
        for v in d.get("variants", []):
            idx[norm(v["label"])].add(i)
    return idx

def resolve_targets(ed, idx):
    """Pass 2: resolve label-only targets to a lexicon id when exactly one concept has that name."""
    n = 0
    for c in ed.values():
        for r in c["relations"]:
            if not r["target_id"]:
                hits = idx.get(norm(r["target_label"]), set())
                if len(hits) == 1:
                    r["target_id"], r["resolved_by"] = next(iter(hits)), "name"; n += 1
            else:
                r.setdefault("resolved_by", "id")
    return n

def edge_set(c, level):
    s = set()
    for r in c["relations"]:
        key = r["target_id"] or "unresolved:" + norm(r["target_label"])
        if level == "target": s.add(key)
        elif level == "axis": s.add((r["axis"], key))
        else: s.add((r["type_fine"], key))
    return s

# ---------- statistics ----------
def f1(a, b):
    if not a and not b: return None
    return 2 * len(a & b) / (len(a) + len(b))

def kripp_alpha_nominal(units):
    """units: list of lists of values (one per rater that rated the unit; missing omitted)."""
    o = Counter(); n = 0
    for vals in units:
        m = len(vals)
        if m < 2: continue
        for a, b in itertools.permutations(range(m), 2):
            o[(vals[a], vals[b])] += 1 / (m - 1)
        n += m
    if n == 0: return None
    nc = Counter()
    for (a, _), w in o.items(): nc[a] += w
    do = sum(w for (a, b), w in o.items() if a != b) / n
    de = sum(nc[a] * nc[b] for a in nc for b in nc if a != b) / (n * (n - 1))
    return None if de == 0 else 1 - do / de

def fleiss_kappa(units):
    units = [u for u in units if len(u) == len(units[0])] if units else []
    if not units or len(units[0]) < 2: return None
    m = len(units[0]); cats = sorted({v for u in units for v in u}, key=str)
    p_j = {c: sum(u.count(c) for u in units) / (len(units) * m) for c in cats}
    P_i = [(sum(u.count(c) ** 2 for c in cats) - m) / (m * (m - 1)) for u in units]
    Pbar, Pe = sum(P_i) / len(P_i), sum(v * v for v in p_j.values())
    return None if Pe == 1 else (Pbar - Pe) / (1 - Pe)

def gwet_ac1_two(pairs):
    if not pairs: return None
    cats = sorted({x for p in pairs for x in p}, key=str); q = len(cats)
    if q < 2: return None
    pa = sum(a == b for a, b in pairs) / len(pairs)
    pi = {c: sum((a == c) + (b == c) for a, b in pairs) / (2 * len(pairs)) for c in cats}
    pe = sum(p * (1 - p) for p in pi.values()) / (q - 1)
    return (pa - pe) / (1 - pe)

def bootstrap(concepts, stat, reps=2000, seed=7):
    """Resample concepts with replacement; stat(list_of_concepts) -> float or None."""
    rng = random.Random(seed); est = stat(concepts); vals = []
    for _ in range(reps):
        v = stat([rng.choice(concepts) for _ in concepts])
        if v is not None: vals.append(v)
    vals.sort()
    if est is None or not vals: return est, None, None
    return est, vals[int(.025 * len(vals))], vals[int(.975 * len(vals)) - 1]

# ---------- step 2: blinded judge requests (stubs; no model is called) ----------
PROMPTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "judging", "prompts")
SYSTEM = open(os.path.join(PROMPTS, "system.txt")).read().strip() if os.path.exists(os.path.join(PROMPTS, "system.txt")) else ""
LABELS = {"P1": None, "P2": set(DEF_SCORE), "P3": None,
          "P4": {"SAME_TYPE", "COMPATIBLE_TYPE", "REVERSED", "CONFLICTING_TYPE"},
          "P5": {"SAME_CONDITION", "COMPATIBLE_CONDITION", "CONFLICTING_CONDITION"},
          "P6": {"COMPATIBLE", "CONFLICTING"}}
# trap concepts (INSTRUCTIONS.md section 2): look-alikes, short names, Service orientation, near-duplicates
TRAP_IDS = {"ls6hrpynv0", "h60l8olauw", "a0h79b66kq", "qb4qnsutxp", "dbxqhrpv38", "fcadn3ihwg", "mnlgauzi32",
            "p1pplzvq0f", "oeixkjthc3", "n29960itit", "thsmk1q1kl", "n7a094bha6", "c4tp7yji9k", "so9zp6tzyh", "v2tu54uao9"}

def broad_class(kind):
    if kind in ("credential", "ability", "knowledge"): return kind
    return "language" if (kind or "").endswith("language") else "skill"

MASK = re.compile(r"\b(grok|xai|claude|anthropic|sonnet|opus|gpt|openai|codex|muse|gemini|as an ai)\b", re.I)

P2_TEMPLATE = open(os.path.join(PROMPTS, "P2.txt")).read().strip() if os.path.exists(os.path.join(PROMPTS, "P2.txt")) else ""

def p2_request(cid, lexe, ea, eb, a_text, b_text, rng):
    """Render prompts/P2.txt exactly; A/B order is random and recorded only in the private key."""
    order = [ea, eb]; rng.shuffle(order)
    texts = {ea: a_text, eb: b_text}
    user = (P2_TEMPLATE.replace("{preferred_name}", lexe["preferred_name"]).replace("{kind}", lexe["kind"])
            .replace("{text_a}", MASK.sub("[model]", texts[order[0]])).replace("{text_b}", MASK.sub("[model]", texts[order[1]])))
    return order, user

def run(args):
    """Public files (requests/) go in OUT; everything that names an edition (keys, canonical drafts, coverage,
    deterministic tables) goes in --private-dir, which must NOT be committed to a public repo."""
    priv = args.private_dir or args.out
    for d in ("requests/P2", "results", "packets", "humans"):
        os.makedirs(os.path.join(args.out, d), exist_ok=True)
    for d in ("canonical", "keys", "tables"):
        os.makedirs(os.path.join(priv, d), exist_ok=True)
    secret = os.urandom(16).hex()  # request ids are keyed by this secret so they cannot be brute-forced to editions
    open(os.path.join(priv, "keys", "request-id-secret.txt"), "w").write(secret + "\n")
    only = set(l.split()[0] for l in open(args.concepts) if l.strip() and not l.startswith("#")) if args.concepts else None
    lex = load_lexicon(args.lexicon) if args.lexicon else {}
    eds = dict(load_edition(s) for s in args.edition)
    if lex and args.with_reference:
        eds["reference"] = {i: canon_lexicon(d) for i, d in lex.items()}
    idx = name_index(lex) if lex else {}
    names = list(eds)
    for n, ed in eds.items():
        k = resolve_targets(ed, idx) if idx else 0
        with open(os.path.join(priv, "canonical", f"{n}.jsonl"), "w") as f:
            for c in ed.values(): f.write(json.dumps(c) + "\n")
        print(f"{n}: {len(ed)} concepts; {k} label-only targets resolved by name")
    allc = sorted(set(lex) | set().union(*[set(e) for e in eds.values()]))
    # coverage
    with open(os.path.join(priv, "coverage.csv"), "w") as f:
        f.write("concept_id,kind," + ",".join(names) + "\n")
        for c in allc:
            f.write(f"{c},{lex.get(c, {}).get('kind', '')}," + ",".join("1" if c in eds[n] else "0" for n in names) + "\n")
    rows = ["| pair | shared | both have relations | rel F1 target (macro) | rel F1 axis | both have variants | variant F1 (exact norm) | conditional-flag agreement |",
            "|---|---:|---:|---|---|---:|---|---|"]
    rng = random.Random(args.seed); req, keys = [], []
    for a, b in itertools.combinations(names, 2):
        shared = sorted(set(eds[a]) & set(eds[b]))
        if only is not None: shared = [c for c in shared if c in only]
        def relf(level):
            def s(cs):
                v = [f1(edge_set(eds[a][c], level), edge_set(eds[b][c], level)) for c in cs]
                v = [x for x in v if x is not None]; return sum(v) / len(v) if v else None
            return s
        def varf(cs):
            v = [f1({norm(x["text"]) for x in eds[a][c]["variants"]}, {norm(x["text"]) for x in eds[b][c]["variants"]}) for c in cs]
            v = [x for x in v if x is not None]; return sum(v) / len(v) if v else None
        cond = []
        for c in shared:
            vb = {norm(x["text"]): x["conditional"] for x in eds[b][c]["variants"]}
            cond += [(x["conditional"], vb[norm(x["text"])]) for x in eds[a][c]["variants"] if norm(x["text"]) in vb]
        fmt = lambda t: "n/a" if t[0] is None else f"{t[0]:.3f} [{t[1]:.3f}, {t[2]:.3f}]"
        both_rel = sum(1 for c in shared if eds[a][c]["relations"] and eds[b][c]["relations"])
        both_var = sum(1 for c in shared if eds[a][c]["variants"] and eds[b][c]["variants"])
        ca = sum(x == y for x, y in cond) / len(cond) if cond else None
        rows.append(f"| {a} × {b} | {len(shared)} | {both_rel} | {fmt(bootstrap(shared, relf('target'), args.reps))} | "
                    f"{fmt(bootstrap(shared, relf('axis'), args.reps))} | {both_var} | {fmt(bootstrap(shared, varf, args.reps))} | "
                    f"{'n/a' if ca is None else f'{ca:.3f} (n={len(cond)}, AC1={gwet_ac1_two(cond)})'} |")
        for c in shared:
            if c not in lex: continue
            order, user = p2_request(c, lex[c], a, b, eds[a][c]["definition"], eds[b][c]["definition"], rng)
            rid = "r-" + hashlib.sha256(f"{secret}|P2|{c}|{a}|{b}".encode()).hexdigest()[:12]
            req.append({"request_id": rid, "stage": "P2", "concept_id": c, "field": "definition",
                        "kind": lex[c]["kind"], "broad_class": broad_class(lex[c]["kind"]), "trap": c in TRAP_IDS,
                        "prompt_version": PROMPT_VERSION, "prompt_sha256": hashlib.sha256((SYSTEM + user).encode()).hexdigest(),
                        "system": SYSTEM, "user": user})
            keys.append({"request_id": rid, "A": order[0], "B": order[1]})
    # multi-rater: presence/absence of each target (axis-level), nominal alpha across all editions
    units = []
    for c in allc:
        have = [n for n in names if c in eds[n]]
        if len(have) < 2: continue
        tgts = set().union(*[edge_set(eds[n][c], "target") for n in have])
        for t in tgts:
            units.append([next((r["axis"] for r in eds[n][c]["relations"] if (r["target_id"] or "unresolved:" + norm(r["target_label"])) == t), "NONE") for n in have])
    rows += ["", f"UNION-FRAME (biased low, see AGREEMENT-METHOD.md 6.2; replace with the fixed neighbour frame) Krippendorff nominal alpha, {len(units)} units: "
             f"{kripp_alpha_nominal(units)}", f"Fleiss kappa on the same units (complete only): {fleiss_kappa(units)}"]
    open(os.path.join(priv, "tables", "deterministic.md"), "w").write("\n".join(rows) + "\n")
    rng.shuffle(req)  # so batch position reveals nothing about which editions are paired
    for b in range(0, len(req), args.batch_size):
        with open(os.path.join(args.out, "requests", "P2", f"batch-{b // args.batch_size + 1:04d}.jsonl"), "w") as f:
            for r in req[b:b + args.batch_size]: f.write(json.dumps(r) + "\n")
    with open(os.path.join(priv, "keys", "anon.jsonl"), "w") as f:
        for k in keys: f.write(json.dumps(k) + "\n")
    print("\n".join(rows)); print(f"wrote {len(req)} P2 requests (blinded); PRIVATE key in {priv}/keys/anon.jsonl")

# ---------- judges: registration, sampling, validation (one schema for model and human judges) ----------
def jload(path):
    return [json.loads(l) for l in open(path) if l.strip()] if os.path.exists(path) else []

def all_requests(out):
    return [r for f in sorted(glob.glob(os.path.join(out, "requests", "*", "batch-*.jsonl"))) for r in jload(f)]

def judges_file(out):
    p = os.path.join(out, "judges.json")
    return p, (json.load(open(p)) if os.path.exists(p) else {})

def stratified(items, n, rng, trap_share):
    """Proportional allocation over field x broad_class (>=1 per non-empty cell), trap quota first."""
    if n <= 0 or not items: return []
    pick = []
    traps = [r for r in items if r.get("trap")]
    rng.shuffle(traps); pick += traps[:min(len(traps), max(1, round(n * trap_share)) if traps else 0)]
    rest = [r for r in items if r not in pick]
    cells = defaultdict(list)
    for r in rest: cells[(r["field"], r.get("broad_class"))].append(r)
    need = n - len(pick)
    for k in sorted(cells, key=str):
        rng.shuffle(cells[k])
        pick += cells[k][:max(1, round(need * len(cells[k]) / len(rest)))]
    rng.shuffle(pick)
    return pick[:n]

def register(args):
    out = args.out; reqs = all_requests(out)
    kp = args.keys or os.path.join(out, "keys", "anon.jsonl")
    keys = {k["request_id"]: k for k in jload(kp)}
    if args.type == "model" and args.drafted and not keys:
        sys.exit(f"self-exclusion needs the private key file; pass --keys (looked for {kp})")
    jp, judges = judges_file(out)
    if args.judge_id in judges and not args.force: sys.exit(f"{args.judge_id} is already registered (use --force to redraw)")
    drafted = set(filter(None, (args.drafted or "").split(",")))
    seed = int(hashlib.sha256(f"{args.salt}|{args.judge_id}".encode()).hexdigest()[:8], 16)
    judges[args.judge_id] = {"type": args.type, "name": args.name, "harness": args.harness, "model": args.model or None,
                             "drafted": sorted(drafted), "seed": seed, "salt": args.salt, "size": args.size,
                             "overlap": args.overlap, "pool_size": args.pool_size, "trap_share": args.trap_share}
    if args.type == "model":
        # self-exclusion: never a request whose hidden key contains an edition this model drafted
        ok = [r for r in reqs if not drafted & {keys.get(r["request_id"], {}).get("A"), keys.get(r["request_id"], {}).get("B")}]
        random.Random(seed).shuffle(ok)  # each judge sees its own seeded order
        d = os.path.join(out, "packets", args.judge_id); os.makedirs(d, exist_ok=True)
        for old in glob.glob(os.path.join(d, "batch-*.jsonl")): os.remove(old)
        for b in range(0, len(ok), args.batch_size):
            with open(os.path.join(d, f"batch-{b // args.batch_size + 1:04d}.jsonl"), "w") as f:
                for r in ok[b:b + args.batch_size]:
                    f.write(json.dumps({k: r[k] for k in ("request_id", "stage", "concept_id", "prompt_version", "prompt_sha256", "system", "user")}) + "\n")
        print(f"{args.judge_id}: {len(ok)} of {len(reqs)} requests eligible after self-exclusion ({sorted(drafted) or 'none'}); "
              f"{-(-len(ok) // args.batch_size)} batches in packets/{args.judge_id}/")
    else:
        hd = os.path.join(out, "humans"); os.makedirs(hd, exist_ok=True)
        pool_path = os.path.join(hd, "overlap-pool.jsonl")
        pool = jload(pool_path)
        if not pool:
            prng = random.Random(f"{args.salt}|pool")
            pool = [{"request_id": r["request_id"], "times_assigned": 0} for r in stratified(reqs, args.pool_size, prng, args.trap_share)]
        rng = random.Random(seed)
        n_over = round(args.size * args.overlap)
        order = sorted(pool, key=lambda x: (x["times_assigned"], rng.random()))[:n_over]
        for x in order: x["times_assigned"] += 1
        with open(pool_path, "w") as f:
            for x in pool: f.write(json.dumps(x) + "\n")
        taken = {x["request_id"] for x in pool}
        for f in glob.glob(os.path.join(hd, "*", "sample.jsonl")):
            taken |= {x["request_id"] for x in jload(f)}
        uniq = stratified([r for r in reqs if r["request_id"] not in taken], args.size - len(order), rng, args.trap_share)
        byid = {r["request_id"]: r for r in reqs}
        sample = [dict(byid[x["request_id"]], overlap=True) for x in order] + [dict(r, overlap=False) for r in uniq]
        rng.shuffle(sample)
        d = os.path.join(hd, args.judge_id); os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "sample.jsonl"), "w") as f:
            for i, r in enumerate(sample): f.write(json.dumps({"position": i + 1, **{k: r[k] for k in ("request_id", "stage", "concept_id", "user", "overlap")}}) + "\n")
        json.dump({"next_position": 1, "done": 0, "total": len(sample)}, open(os.path.join(d, "progress.json"), "w"))
        with open(os.path.join(hd, "registry.jsonl"), "a") as f:
            f.write(json.dumps({"judge_id": args.judge_id, "name": args.name, "seed": seed, "size": len(sample),
                                "overlap_items": len(order), "unique_items": len(uniq)}) + "\n")
        print(f"{args.judge_id}: {len(sample)} items ({len(order)} overlap, {len(uniq)} unique) in humans/{args.judge_id}/sample.jsonl")
    json.dump(judges, open(jp, "w"), indent=1)

def slug(*parts):
    return re.sub(r"[^a-z0-9]+", "-", "-".join(p for p in parts if p).lower()).strip("-")

def confirm_model(args):
    """First session of a model judge: record provider, model name and the exact model VERSION (required).
    The versioned judge id is <provider>-<model name>-<version>, for example anthropic-claude-fable-5-2.
    A model that cannot state its version passes --version-unknown: the id ends in -version-unknown and the
    judge is FLAGGED (its results are reported separately and never enter the primary panel label).
    Writes results/<judge_id>/judge.json only (the judge's own folder), so parallel judge branches never conflict."""
    _, judges = judges_file(args.out); slot = judges.get(args.slot)
    if not slot or slot["type"] != "model": sys.exit(f"{args.slot} is not a registered model-judge slot in judges.json")
    if bool(args.version) == bool(args.version_unknown):
        sys.exit("give exactly one of --version X.Y (as your harness or system information states it) or --version-unknown")
    version = args.version.strip() if args.version else None
    jid = slug(args.provider, args.model_name, version or "version-unknown")
    d = os.path.join(args.out, "results", jid); os.makedirs(d, exist_ok=True)
    p = os.path.join(d, "judge.json")
    import datetime
    rec = {"judge_id": jid, "slot": args.slot, "provider": args.provider, "model_name": args.model_name,
           "model_version": version, "version_status": "stated" if version else "unknown",
           "flags": [] if version else ["version_unknown"], "model_reported": args.model_reported,
           "harness": args.harness or slot.get("harness"), "harness_version": args.harness_version,
           "effort": args.effort, "plan": args.plan,
           "confirmed_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds")}
    if os.path.exists(p):
        old = json.load(open(p))
        same = all(old.get(k) == rec[k] for k in ("slot", "provider", "model_name", "model_version", "model_reported"))
        if not same and not args.force:
            sys.exit(f"{p} already records a different model or version; stop and tell the operator")
        if same: rec["confirmed_at"] = old["confirmed_at"]
    json.dump(rec, open(p, "w"), indent=1)
    print(f"judge id: {jid}" + ("   ** FLAGGED: version unknown **" if not version else ""))
    print(f"recorded in {p}; work on branch judging/{jid}; packets in packets/{args.slot}/")

def judge_record(out, jid):
    p = os.path.join(out, "results", jid, "judge.json")
    return json.load(open(p)) if os.path.exists(p) else None

REQUIRED = ("judgment_id", "request_id", "stage", "concept_id", "judge", "run_index", "prompt_version", "label",
            "fields", "notes", "confirmed", "created_at")
WHO = ("provider", "model_name", "model_version", "model_reported")

def validate(args):
    out, jid = args.out, args.judge_id
    _, judges = judges_file(out)
    rec = judge_record(out, jid)
    if jid in judges and judges[jid]["type"] == "human":
        me, kind = judges[jid], "human"
        allowed = {r["request_id"] for r in jload(os.path.join(out, "humans", jid, "sample.jsonl"))}
        pkdir = None
    elif rec:
        me, kind = judges.get(rec["slot"]), "model"
        if not me: sys.exit(f"{jid}: slot {rec['slot']!r} is not in judges.json")
        pkdir = os.path.join(out, "packets", rec["slot"])
        allowed = {r["request_id"] for f in glob.glob(os.path.join(pkdir, "*.jsonl")) for r in jload(f)}
    elif jid in judges:
        sys.exit(f"{jid} is a slot: run `agreement.py confirm-model {out} --slot {jid} --provider ... --model-name ... "
                 f"--version X.Y|--version-unknown --model-reported ...` and validate with the judge id it prints")
    else:
        sys.exit(f"{jid} is not registered (no results/{jid}/judge.json and no human registration)")
    errs, warns, seen, n = [], [], set(), 0
    if kind == "model":
        if rec.get("version_status") == "unknown" or not rec.get("model_version"):
            warns.append(f"FLAGGED: {jid} did not state a model version; its results are reported separately and kept out of the primary panel")
        if not jid.endswith(slug(rec.get("model_version") or "version-unknown")):
            errs.append(f"judge id {jid} does not end with its version {rec.get('model_version')!r}")
    for f in sorted(glob.glob(os.path.join(out, "results", jid, "**", "*.jsonl"), recursive=True)):
        for ln, line in enumerate(open(f), 1):
            if not line.strip(): continue
            try: j = json.loads(line)
            except ValueError: errs.append(f"{f}:{ln} not JSON"); continue
            if "_batch" in j:
                if kind == "model":
                    bad = [k for k in WHO if j.get(k) != rec.get(k)]
                    if j.get("judge_id") != jid: bad.append("judge_id")
                    if bad: errs.append(f"{f}:{ln} header {bad} differ from results/{jid}/judge.json")
                continue
            n += 1
            miss = [k for k in REQUIRED if k not in j]
            if miss: errs.append(f"{f}:{ln} missing {miss}"); continue
            if j["request_id"] not in allowed: errs.append(f"{f}:{ln} {j['request_id']} was not assigned to {jid}")
            key = (j["request_id"], j["run_index"])
            if key in seen: errs.append(f"{f}:{ln} duplicate {key}")
            seen.add(key)
            labels = LABELS.get(j["stage"])
            if labels and j["label"] not in labels | {"UNSURE"}: errs.append(f"{f}:{ln} label {j['label']!r} not allowed for {j['stage']}")
            if j["judge"].get("id") != jid: errs.append(f"{f}:{ln} judge.id {j['judge'].get('id')!r} != {jid}")
            if kind == "model":
                if "model_version" not in j["judge"]: errs.append(f"{f}:{ln} judge.model_version is required (null only if unknown)")
                bad = [k for k in WHO if j["judge"].get(k) != rec.get(k)]
                if bad: errs.append(f"{f}:{ln} judge {bad} differ from results/{jid}/judge.json")
            if kind == "human" and j["confirmed"] is not True: errs.append(f"{f}:{ln} human label not confirmed by the judge")
    if kind == "model":  # a handed-in batch must answer every request in the packet of the same name
        for f in sorted(glob.glob(os.path.join(out, "results", jid, "*", "batch-*.jsonl"))):
            pk = os.path.join(pkdir, os.path.basename(f))
            want_ids = {r["request_id"] for r in jload(pk)}
            got = {j["request_id"] for j in jload(f) if "_batch" not in j and "request_id" in j}
            if not os.path.exists(pk): errs.append(f"{f}: no packet {pk}")
            elif want_ids - got: errs.append(f"{f}: incomplete, {len(want_ids - got)} of {len(want_ids)} requests unanswered")
            hdr = [j for j in jload(f) if "_batch" in j]
            if not any("finished_at" in h for h in hdr): errs.append(f"{f}: no closing header line with finished_at")
    for w in warns: print("WARNING", w)
    for e in errs[:50]: print("ERROR", e)
    print(f"{jid}: {n} judgments, {len(errs)} errors, {len(warns)} flags"); sys.exit(1 if errs else 0)

def stats(args):
    """Fold every judge's results (results/<judge_id>/...) into definition agreement, per judge and per edition pair."""
    keys = {k["request_id"]: k for k in jload(args.keys or os.path.join(args.out, "keys", "anon.jsonl"))}
    if not keys: sys.exit("stats needs the PRIVATE key file: pass --keys PATH/anon.jsonl")
    files = glob.glob(os.path.join(args.out, "results", "*", "**", "*.jsonl"), recursive=True)
    if not files: sys.exit("no results/ yet: judges have not handed in")
    by = defaultdict(list)
    for f in files:
        for j in jload(f):
            if "_batch" in j or j.get("stage") != "P2" or j["request_id"] not in keys: continue
            k = keys[j["request_id"]]
            by[(j["judge"]["id"], tuple(sorted((k["A"], k["B"]))))].append((j["concept_id"], DEF_SCORE.get(j["label"]), j["label"]))
    for (judge, pair), xs in sorted(by.items()):
        cs = sorted({c for c, _, _ in xs}); sc = defaultdict(list)
        for c, s, _ in xs:
            if s is not None: sc[c].append(s)
        st = lambda cc: (lambda v: sum(v) / len(v) if v else None)([sum(sc[c]) / len(sc[c]) for c in cc if sc[c]])
        rec = judge_record(args.out, judge) or {}
        flag = " [FLAGGED: version unknown; not in primary panel]" if "version_unknown" in rec.get("flags", []) else ""
        print(judge + flag, pair, "mean definition score", bootstrap(cs, st, args.reps), Counter(l for _, _, l in xs).most_common())
    # TODO(draft): family-balanced panel label, Codex-only, leave-one-judge-out, self-preference DiD (AGREEMENT-METHOD.md 4.4)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="cmd", required=True)
    r = sp.add_parser("run"); r.add_argument("out"); r.add_argument("--edition", action="append", required=True)
    r.add_argument("--lexicon"); r.add_argument("--with-reference", action="store_true")
    r.add_argument("--seed", type=int, default=7); r.add_argument("--reps", type=int, default=2000)
    r.add_argument("--batch-size", type=int, default=50); r.add_argument("--concepts", help="file of concept ids to keep")
    r.add_argument("--private-dir", help="where keys, canonical drafts and tables go (keep out of public repos)")
    g = sp.add_parser("register"); g.add_argument("out"); g.add_argument("--judge-id", required=True)
    g.add_argument("--type", choices=("model", "human"), required=True); g.add_argument("--name")
    g.add_argument("--harness"); g.add_argument("--model"); g.add_argument("--drafted")
    g.add_argument("--size", type=int, default=100); g.add_argument("--overlap", type=float, default=0.3)
    g.add_argument("--pool-size", type=int, default=50); g.add_argument("--trap-share", type=float, default=0.1)
    g.add_argument("--batch-size", type=int, default=50); g.add_argument("--salt", default="agree-v1")
    g.add_argument("--force", action="store_true"); g.add_argument("--keys", help="private keys/anon.jsonl")
    c = sp.add_parser("confirm-model"); c.add_argument("out"); c.add_argument("--slot", required=True)
    c.add_argument("--provider", required=True, help="openai | anthropic | xai | ...")
    c.add_argument("--model-name", required=True, help='for example "claude-fable" or "codex"')
    c.add_argument("--version", help='exact model version, for example "5.2"'); c.add_argument("--version-unknown", action="store_true")
    c.add_argument("--model-reported", required=True, help="the model string exactly as the harness reports it")
    c.add_argument("--harness"); c.add_argument("--harness-version")
    c.add_argument("--effort"); c.add_argument("--plan"); c.add_argument("--force", action="store_true")
    v = sp.add_parser("validate"); v.add_argument("out"); v.add_argument("--judge-id", required=True)
    s = sp.add_parser("stats"); s.add_argument("out"); s.add_argument("--reps", type=int, default=2000)
    s.add_argument("--keys", help="private keys/anon.jsonl")
    a = ap.parse_args()
    {"run": run, "register": register, "confirm-model": confirm_model, "validate": validate, "stats": stats}[a.cmd](a)
