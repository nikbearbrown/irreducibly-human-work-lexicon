#!/usr/bin/env python3
"""DRAFT skeleton for AGREEMENT-METHOD.md: normalise editions, align, write blinded judge requests, compute stats.

Status: draft (agree-v1-draft). Deterministic parts only; it never calls a model. Judge replies are read back
from judgments/*.jsonl written by whatever harness runs the requests.

Usage:
  agreement.py run OUT_DIR --edition NAME=SCHEMA:PATH[,PATH...] [--edition ...] [--lexicon LEXICON_REPO] [--seed 7]
     SCHEMA is gen-v2 | sonnet-edition | lexicon. Later paths override earlier ones for the same concept_id.
  agreement.py stats OUT_DIR        (after judgments/ exists; folds judge labels into the tables)

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
SYSTEM = open(os.path.join(os.path.dirname(__file__), "..", "AGREEMENT-METHOD.md")).read().split(
    "**System (all judge calls):**", 1)[1].split("```")[1].strip() if os.path.exists(
    os.path.join(os.path.dirname(__file__), "..", "AGREEMENT-METHOD.md")) else ""
MASK = re.compile(r"\b(grok|xai|claude|anthropic|sonnet|opus|gpt|openai|codex|muse|gemini|as an ai)\b", re.I)

def p2_request(cid, lexe, ea, eb, a_text, b_text, rng):
    order = [ea, eb]; rng.shuffle(order)
    texts = {ea: a_text, eb: b_text}
    user = (f'Concept: "{lexe["preferred_name"]}" (kind: {lexe["kind"]})\n'
            f"Definition A: {MASK.sub('[model]', texts[order[0]])}\nDefinition B: {MASK.sub('[model]', texts[order[1]])}\n\n"
            "Choose exactly one label: EQUIVALENT, A_NARROWER, B_NARROWER, OVERLAPPING, CONFLICTING, DIFFERENT_SENSE "
            "(definitions in AGREEMENT-METHOD.md 4.2, P2).\nReturn: {\"label\": \"...\", \"same_sense\": true|false, "
            "\"genus_a\": \"...\", \"genus_b\": \"...\", \"conflicts\": [], \"confidence\": 1-5, \"rationale\": \"<=40 words\"}")
    return order, user

def run(args):
    os.makedirs(args.out, exist_ok=True)
    for d in ("canonical", "requests", "keys", "results", "judgments"):
        os.makedirs(os.path.join(args.out, d), exist_ok=True)
    lex = load_lexicon(args.lexicon) if args.lexicon else {}
    eds = dict(load_edition(s) for s in args.edition)
    if lex and args.with_reference:
        eds["reference"] = {i: canon_lexicon(d) for i, d in lex.items()}
    idx = name_index(lex) if lex else {}
    names = list(eds)
    for n, ed in eds.items():
        k = resolve_targets(ed, idx) if idx else 0
        with open(os.path.join(args.out, "canonical", f"{n}.jsonl"), "w") as f:
            for c in ed.values(): f.write(json.dumps(c) + "\n")
        print(f"{n}: {len(ed)} concepts; {k} label-only targets resolved by name")
    allc = sorted(set(lex) | set().union(*[set(e) for e in eds.values()]))
    # coverage
    with open(os.path.join(args.out, "coverage.csv"), "w") as f:
        f.write("concept_id,kind," + ",".join(names) + "\n")
        for c in allc:
            f.write(f"{c},{lex.get(c, {}).get('kind', '')}," + ",".join("1" if c in eds[n] else "0" for n in names) + "\n")
    rows = ["| pair | shared | both have relations | rel F1 target (macro) | rel F1 axis | both have variants | variant F1 (exact norm) | conditional-flag agreement |",
            "|---|---:|---:|---|---|---:|---|---|"]
    rng = random.Random(args.seed); req, keys = [], []
    for a, b in itertools.combinations(names, 2):
        shared = sorted(set(eds[a]) & set(eds[b]))
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
                    f"{'n/a' if ca is None else f'{ca:.3f} (n={len(cond)}, AC1={gwet_ac1_two(cond):.3f})'} |")
        for c in shared:
            if c not in lex: continue
            order, user = p2_request(c, lex[c], a, b, eds[a][c]["definition"], eds[b][c]["definition"], rng)
            rid = "r-" + hashlib.sha256(f"P2|{c}|{a}|{b}".encode()).hexdigest()[:12]
            req.append({"request_id": rid, "stage": "P2", "concept_id": c, "field": "definition",
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
    open(os.path.join(args.out, "results", "deterministic.md"), "w").write("\n".join(rows) + "\n")
    with open(os.path.join(args.out, "requests", "P2.jsonl"), "w") as f:
        for r in req: f.write(json.dumps(r) + "\n")
    with open(os.path.join(args.out, "keys", "anon.jsonl"), "w") as f:
        for k in keys: f.write(json.dumps(k) + "\n")
    print("\n".join(rows)); print(f"wrote {len(req)} P2 requests (blinded; key in keys/anon.jsonl)")

def stats(args):
    """Fold judge labels (judgments/P2.jsonl: request_id, label, judge.model, run_index) into definition agreement."""
    keys = {json.loads(l)["request_id"]: json.loads(l) for l in open(os.path.join(args.out, "keys", "anon.jsonl"))}
    path = os.path.join(args.out, "judgments", "P2.jsonl")
    if not os.path.exists(path): sys.exit("no judgments/P2.jsonl yet: run the requests through the judge panel first")
    by_pair = defaultdict(list)
    for l in open(path):
        j = json.loads(l); k = keys[j["request_id"]]
        by_pair[tuple(sorted((k["A"], k["B"])))].append((j["concept_id"], DEF_SCORE.get(j["label"]), j["label"]))
    for pair, xs in by_pair.items():
        cs = sorted({c for c, _, _ in xs}); sc = defaultdict(list)
        for c, s, _ in xs:
            if s is not None: sc[c].append(s)
        st = lambda cc: (lambda v: sum(v) / len(v) if v else None)([sum(sc[c]) / len(sc[c]) for c in cc if sc[c]])
        print(pair, "mean definition score", bootstrap(cs, st, args.reps), Counter(l for _, _, l in xs).most_common())

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="cmd", required=True)
    r = sp.add_parser("run"); r.add_argument("out"); r.add_argument("--edition", action="append", required=True)
    r.add_argument("--lexicon"); r.add_argument("--with-reference", action="store_true")
    r.add_argument("--seed", type=int, default=7); r.add_argument("--reps", type=int, default=2000)
    s = sp.add_parser("stats"); s.add_argument("out"); s.add_argument("--reps", type=int, default=2000)
    a = ap.parse_args(); run(a) if a.cmd == "run" else stats(a)
