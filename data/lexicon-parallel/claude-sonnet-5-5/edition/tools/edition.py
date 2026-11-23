#!/usr/bin/env python3
"""Skills Lexicon edition tooling (Claude Sonnet 5.5 edition).

Subcommands
  build      parse drafts/*.txt (+ O*NET-sourced elements) -> entries.jsonl, inventory.jsonl, coverage.json, manifest.json
  show       print the next pending inventory rows (n|kind|label) to draft
  validate   independent validation of every output file (use --full for the final all-2,895 gate)
  markdown   write entries.md from entries.jsonl
  find       grep inventory labels (case-insensitive substring)

Draft line format (drafts/*.txt), one concept per block:
  <n>|<exact canonical label>|<definition text>
  +v|<variant label>                      optional, repeatable
  +r|<broader|part_of|related|contrast>|<target label or #n>     optional, repeatable
  +f|<flag type>|<note>                   optional, repeatable
Lines starting with # and blank lines are ignored. <n> is the 1-based row number in inventory.jsonl;
the label must match inventory exactly, which guards against ID drift.

Run with: python3 -I tools/edition.py <subcommand>
"""
import json
import os
import re
import sys
import glob
import collections
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODEL_LABEL = "Claude Sonnet 5.5"
MODEL_ID = "claude-sonnet-5-5"
SLUG = "skills-lexicon-claude-sonnet-5-5"
PINNED = "91312fec957388afe4d1dfbdb4aff2707588b9a1"
SOURCE_REPO = "https://github.com/nikbearbrown/skills-lexicon"
EXPECTED = {"skill": 1988, "ability": 67, "knowledge": 550, "language": 290}
EXPECTED_TOTAL = 2895
REL_TYPES = {"broader", "part_of", "related", "contrast"}
FLAG_TYPES = {"classification_dispute", "sense_note", "ambiguous_label", "low_confidence", "scope_note"}
BASES = {"source", "model_knowledge"}
KIND_TO_CLASS = {"ability": "ability", "knowledge": "knowledge", "human-language": "language", "programming-language": "language",
                 "markup-language": "language", "style-language": "language", "modeling-language": "language",
                 "skill": "skill", "method": "skill", "standard": "skill", "tool": "skill", "platform": "skill",
                 "library": "skill", "framework": "skill", "work-activity": "skill"}
ONET_FILE_URL = {"abilities/onet-abilities.json": f"{SOURCE_REPO}/blob/{PINNED}/abilities/onet-abilities.json",
                 "onet-skills/onet-skills.json": f"{SOURCE_REPO}/blob/{PINNED}/onet-skills/onet-skills.json",
                 "onet-knowledge/onet-knowledge.json": f"{SOURCE_REPO}/blob/{PINNED}/onet-knowledge/onet-knowledge.json"}

P_INV = ROOT / "inventory.jsonl"
P_ENT = ROOT / "entries.jsonl"
P_COV = ROOT / "coverage.json"
P_MAN = ROOT / "manifest.json"
P_ONET = ROOT / "data" / "onet-30.2-elements.json"
P_OOS = ROOT / "data" / "out-of-scope-credential-ids.txt"
P_MD = ROOT / "entries.md"
DRAFTS = ROOT / "drafts"


def read_jsonl(p):
    out = []
    with open(p, encoding="utf-8") as fh:
        for i, line in enumerate(fh, 1):
            if line.strip():
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError as e:
                    raise SystemExit(f"{p}:{i}: invalid JSON: {e}")
    return out


def write_jsonl(p, rows):
    tmp = str(p) + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    os.replace(tmp, p)


def write_json(p, obj):
    tmp = str(p) + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    os.replace(tmp, p)


def onet_source_record(el):
    return {"source": "O*NET", "version": "30.2", "identifier": el["element_id"],
            "permalink": ONET_FILE_URL[el["source_file"]], "license": "CC BY 4.0",
            "attribution": "O*NET 30.2 database, U.S. Department of Labor, Employment and Training Administration (USDOL/ETA), "
                           "CC BY 4.0; selected and reformatted; USDOL/ETA has not approved, endorsed or tested the changes. "
                           "O*NET(R) is a trademark of USDOL/ETA."}


def parse_drafts(inv, errors):
    """Return {n: {"label","definition","variants":[],"relations":[(type,target_spec)],"flags":[(type,note)]}}"""
    drafted = {}
    for path in sorted(DRAFTS.glob("*.txt")):
        cur = None
        for ln, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            line = raw.rstrip("\n")
            where = f"{path.name}:{ln}"
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if line.startswith("+"):
                if cur is None:
                    errors.append(f"{where}: modifier line before any entry")
                    continue
                parts = line[1:].split("|", 2)
                tag = parts[0]
                if tag in ("v", "va") and len(parts) >= 2:
                    cur["variants"].append(("|".join(parts[1:]).strip(), tag == "va"))
                elif tag == "r" and len(parts) == 3:
                    cur["relations"].append((parts[1].strip(), parts[2].strip(), where))
                elif tag == "f" and len(parts) == 3:
                    cur["flags"].append((parts[1].strip(), parts[2].strip()))
                else:
                    errors.append(f"{where}: malformed modifier {line[:60]!r}")
                continue
            m = re.match(r"^(\d+)\|", line)
            if not m:
                errors.append(f"{where}: line does not start with '<n>|': {line[:60]!r}")
                cur = None
                continue
            n = int(m.group(1))
            rest = line[m.end():]
            if n < 1 or n > len(inv):
                errors.append(f"{where}: n={n} is outside the inventory")
                cur = None
                continue
            rec = inv[n - 1]
            label = rec["preferred_name"]
            if not rest.startswith(label + "|"):
                errors.append(f"{where}: n={n} label mismatch: inventory has {label!r}, draft starts {rest[:40]!r}")
                cur = None
                continue
            definition = rest[len(label) + 1:].strip()
            if n in drafted:
                errors.append(f"{where}: n={n} ({label}) drafted more than once")
                cur = None
                continue
            cur = {"label": label, "definition": definition, "variants": [], "relations": [], "flags": [], "where": where}
            drafted[n] = cur
    return drafted


def cmd_build():
    errors = []
    inv = read_jsonl(P_INV)
    onet = json.loads(P_ONET.read_text(encoding="utf-8"))
    el_by_code = {e["element_id"]: e for e in onet["elements"]}
    by_label = collections.defaultdict(list)
    for r in inv:
        by_label[r["preferred_name"].casefold()].append(r["n"])
    drafted = parse_drafts(inv, errors)

    entries = {}
    onet_used = set()
    for r in inv:
        n = r["n"]
        codes = [i["code"] for i in r.get("identifiers", []) if i.get("scheme") == "onet-element"]
        if codes:
            el = el_by_code.get(codes[0])
            if el is None:
                errors.append(f"n={n} {r['preferred_name']}: O*NET element {codes[0]} not in data file")
                continue
            if n in drafted:
                errors.append(f"n={n} {r['preferred_name']}: has an O*NET element; remove the manual draft ({drafted[n]['where']})")
                continue
            onet_used.add(codes[0])
            entries[n] = {"definition": {"text": el["definition"], "basis": "source", "sources": [onet_source_record(el)]},
                          "variants": [], "relations": [], "flags": []}
    if len(onet_used) != 120:
        errors.append(f"expected 120 O*NET elements matched to inventory, got {len(onet_used)}")

    def resolve(spec, where):
        if spec.startswith("#"):
            try:
                k = int(spec[1:])
                return inv[k - 1] if 1 <= k <= len(inv) else None
            except ValueError:
                return None
        hits = by_label.get(spec.casefold(), [])
        if len(hits) == 1:
            return inv[hits[0] - 1]
        errors.append(f"{where}: relation target {spec!r} " + ("matches several concepts; use #n" if hits else "is not in the roster"))
        return None

    for n, d in drafted.items():
        r = inv[n - 1]
        rels, seen_rel = [], set()
        for typ, spec, where in d["relations"]:
            if typ not in REL_TYPES:
                errors.append(f"{where}: relation type {typ!r} not allowed")
                continue
            t = resolve(spec, where)
            if t is None:
                continue
            if t["concept_id"] == r["concept_id"]:
                errors.append(f"{where}: self relation on {r['preferred_name']}")
                continue
            if (typ, t["concept_id"]) in seen_rel:
                continue
            seen_rel.add((typ, t["concept_id"]))
            rels.append({"type": typ, "target": t["concept_id"], "target_label": t["preferred_name"], "basis": "model_knowledge"})
        variants, seen_v = [], set()
        for v, amb in d["variants"]:
            if v.casefold() == r["preferred_name"].casefold() or v.casefold() in seen_v or not v:
                continue
            seen_v.add(v.casefold())
            rec_v = {"label": v, "basis": "model_knowledge"}
            if amb:
                rec_v["ambiguous"] = True
            variants.append(rec_v)
        flags = []
        for typ, note in d["flags"]:
            if typ not in FLAG_TYPES:
                errors.append(f"{d['where']}: flag type {typ!r} not allowed")
                continue
            flags.append({"type": typ, "note": note})
        if len(d["definition"]) < 20 or "\n" in d["definition"]:
            errors.append(f"{d['where']}: definition too short or multi-line for {r['preferred_name']}")
        entries[n] = {"definition": {"text": d["definition"], "basis": "model_knowledge", "sources": []},
                      "variants": variants, "relations": rels, "flags": flags}

    if errors:
        print(f"BUILD FAILED with {len(errors)} error(s); nothing written:")
        for e in errors[:80]:
            print("  -", e)
        if len(errors) > 80:
            print(f"  ... and {len(errors) - 80} more")
        sys.exit(1)

    out, new_inv = [], []
    for r in inv:
        n = r["n"]
        rec = {k: v for k, v in r.items() if k != "status"}
        if n in entries:
            e = entries[n]
            dup = [inv[m - 1] for m in by_label[r["preferred_name"].casefold()] if m != n]
            for o in dup:
                e["flags"].append({"type": "ambiguous_label", "note":
                    f"Another in-scope concept shares this label ({o['kind']}, id {o['concept_id']}); kept separate by ID."})
            out.append({"concept_id": r["concept_id"], "preferred_name": r["preferred_name"], "kind": r["kind"], "class": r["class"],
                        "draft_set": SLUG, "model": MODEL_LABEL, "status": "machine-drafted", "human_reviewed": False,
                        "definition": e["definition"], "variants": e["variants"], "relations": e["relations"], "flags": e["flags"]})
            rec["status"] = "drafted"
        else:
            rec["status"] = "pending"
        new_inv.append(rec)
    write_jsonl(P_ENT, out)
    write_jsonl(P_INV, new_inv)
    cov = coverage(new_inv, out)
    write_json(P_COV, cov)
    old = json.loads(P_MAN.read_text()) if P_MAN.exists() else {}
    write_json(P_MAN, {
        "edition": SLUG, "model_label": MODEL_LABEL, "model_id": MODEL_ID, "authoring_model_changed_during_run": False,
        "draft_set": SLUG, "entry_status": "machine-drafted (not human-reviewed)",
        "source_repo": SOURCE_REPO, "pinned_commit": PINNED,
        "scope": {"total": EXPECTED_TOTAL, "per_class": EXPECTED,
                  "excluded": ["859 credentials", "36-concept pilot"]},
        "created": old.get("created", "2026-11-21"),
        "progress": {"total": cov["total"], "drafted": cov["drafted"], "pending": cov["pending"]},
        "files": ["README.md", "RUN.md", "manifest.json", "inventory.jsonl", "entries.jsonl", "coverage.json", "entries.md",
                  "THIRD-PARTY-NOTICES.md", "data/onet-30.2-elements.json", "data/roster-meta.json",
                  "data/out-of-scope-credential-ids.txt", "drafts/", "tools/"]})
    print(f"built: {cov['drafted']} drafted, {cov['pending']} pending of {cov['total']} "
          f"({len(drafted)} hand-drafted + {len(onet_used)} O*NET-sourced)")


def coverage(inv, ents):
    drafted_ids = {e["concept_id"] for e in ents}
    per_class, per_kind = {}, {}
    for r in inv:
        d = r["concept_id"] in drafted_ids
        for key, bucket in ((r["class"], per_class), (r["kind"], per_kind)):
            b = bucket.setdefault(key, {"total": 0, "drafted": 0, "pending": 0})
            b["total"] += 1
            b["drafted" if d else "pending"] += 1
    basis = collections.Counter(e["definition"]["basis"] for e in ents)
    return {"edition": SLUG, "model_label": MODEL_LABEL, "pinned_commit": PINNED,
            "total": len(inv), "drafted": len(ents), "pending": len(inv) - len(ents),
            "per_class": per_class, "per_kind": per_kind,
            "definition_basis": dict(basis),
            "entries_with_variants": sum(1 for e in ents if e["variants"]),
            "entries_with_relations": sum(1 for e in ents if e["relations"]),
            "entries_with_flags": sum(1 for e in ents if e["flags"]),
            "variant_records": sum(len(e["variants"]) for e in ents),
            "relation_records": sum(len(e["relations"]) for e in ents),
            "flag_records": sum(len(e["flags"]) for e in ents)}


def cmd_show(args):
    start = int(args[0]) if args else 1
    count = int(args[1]) if len(args) > 1 else 100
    inv = read_jsonl(P_INV)
    shown = 0
    for r in inv:
        if r["n"] >= start and r["status"] == "pending":
            print(f"{r['n']}|{r['kind']}|{r['preferred_name']}")
            shown += 1
            if shown >= count:
                break
    pend = sum(1 for r in inv if r["status"] == "pending")
    print(f"# shown {shown}; pending overall {pend}", file=sys.stderr)


def cmd_find(args):
    q = " ".join(args).casefold()
    for r in read_jsonl(P_INV):
        if q in r["preferred_name"].casefold():
            print(f"{r['n']}|{r['kind']}|{r['preferred_name']}|{r['status']}")


def cmd_validate(args):
    full = "--full" in args
    errs, warns = [], []
    # 1. every JSON / JSONL file parses
    for p in list(ROOT.rglob("*.json")) + list(ROOT.rglob("*.jsonl")):
        if ".git" in p.parts:
            continue
        try:
            if p.suffix == ".jsonl":
                read_jsonl(p)
            else:
                json.loads(p.read_text(encoding="utf-8"))
        except (SystemExit, json.JSONDecodeError) as e:
            errs.append(f"{p.relative_to(ROOT)}: not valid JSON ({e})")
    if errs:
        report(errs, warns)
    inv, ents = read_jsonl(P_INV), read_jsonl(P_ENT)
    cov = json.loads(P_COV.read_text(encoding="utf-8"))
    onet = {e["element_id"]: e for e in json.loads(P_ONET.read_text(encoding="utf-8"))["elements"]}
    oos = set(P_OOS.read_text().split())
    # 2. roster / inventory integrity
    ids = [r["concept_id"] for r in inv]
    if len(ids) != len(set(ids)):
        errs.append("inventory has duplicate concept_id values")
    if [r["n"] for r in inv] != list(range(1, len(inv) + 1)):
        errs.append("inventory n values are not 1..N in order")
    inv_by_id = {r["concept_id"]: r for r in inv}
    if len(oos) != 859:
        errs.append(f"out-of-scope credential list has {len(oos)} ids, expected 859")
    if oos & set(ids):
        errs.append(f"{len(oos & set(ids))} out-of-scope credential ids appear in the inventory")
    for r in inv:
        if r["class"] not in EXPECTED or KIND_TO_CLASS.get(r["kind"]) != r["class"]:
            errs.append(f"inventory {r['concept_id']}: class/kind inconsistent ({r['class']}/{r['kind']})")
        if r["status"] not in ("drafted", "pending"):
            errs.append(f"inventory {r['concept_id']}: bad status {r['status']}")
    class_counts = collections.Counter(r["class"] for r in inv)
    if dict(class_counts) != EXPECTED or len(inv) != EXPECTED_TOTAL:
        errs.append(f"inventory counts {dict(class_counts)} total {len(inv)} differ from expected {EXPECTED} / {EXPECTED_TOTAL}")
    # 3. entries
    eids = [e["concept_id"] for e in ents]
    if len(eids) != len(set(eids)):
        dups = [k for k, v in collections.Counter(eids).items() if v > 1]
        errs.append(f"entries.jsonl has {len(dups)} concept_id(s) with more than one entry, e.g. {dups[:3]}")
    out_scope_ent = [i for i in eids if i not in inv_by_id]
    if out_scope_ent:
        errs.append(f"{len(out_scope_ent)} entries have ids outside the roster, e.g. {out_scope_ent[:3]}; {len(set(out_scope_ent) & oos)} are credentials")
    drafted_inv = {r["concept_id"] for r in inv if r["status"] == "drafted"}
    if drafted_inv != set(eids):
        errs.append(f"inventory 'drafted' ({len(drafted_inv)}) and entries ({len(set(eids))}) disagree: "
                    f"{len(drafted_inv - set(eids))} drafted w/o entry, {len(set(eids) - drafted_inv)} entries not marked drafted")
    req = ["concept_id", "preferred_name", "kind", "class", "draft_set", "model", "status", "human_reviewed",
           "definition", "variants", "relations", "flags"]
    seen_text = collections.defaultdict(list)
    variant_owner = collections.defaultdict(set)
    graph = collections.defaultdict(set)
    for e in ents:
        cid = e.get("concept_id")
        for k in req:
            if k not in e:
                errs.append(f"{cid}: missing field {k}")
        r = inv_by_id.get(cid)
        if not r:
            continue
        for k in ("preferred_name", "kind", "class"):
            if e.get(k) != r[k]:
                errs.append(f"{cid}: {k} {e.get(k)!r} differs from inventory {r[k]!r}")
        if e.get("model") != MODEL_LABEL or e.get("draft_set") != SLUG:
            errs.append(f"{cid}: model/draft_set not '{MODEL_LABEL}' / '{SLUG}'")
        if e.get("status") != "machine-drafted" or e.get("human_reviewed") is not False:
            errs.append(f"{cid}: must be machine-drafted and human_reviewed false")
        d = e.get("definition", {})
        txt = d.get("text")
        if not isinstance(txt, str) or not (20 <= len(txt) <= 700) or "\n" in txt:
            errs.append(f"{cid} {e.get('preferred_name')}: definition text missing/too short/too long/multi-line")
        else:
            seen_text[txt.casefold()].append(cid)
        if d.get("basis") not in BASES:
            errs.append(f"{cid}: definition basis {d.get('basis')!r} not in {sorted(BASES)}")
        srcs = d.get("sources")
        if not isinstance(srcs, list):
            errs.append(f"{cid}: definition.sources must be a list")
            srcs = []
        if d.get("basis") == "source" and not srcs:
            errs.append(f"{cid}: basis 'source' but no sources")
        if d.get("basis") == "model_knowledge" and srcs:
            errs.append(f"{cid}: basis 'model_knowledge' must not list sources")
        for s in srcs:
            for k in ("source", "version", "identifier", "permalink", "license"):
                if not s.get(k):
                    errs.append(f"{cid}: source record missing {k}")
            if s.get("source") == "O*NET":
                el = onet.get(s.get("identifier"))
                if el is None:
                    errs.append(f"{cid}: O*NET identifier {s.get('identifier')} not in the O*NET data file")
                elif el["definition"] != txt:
                    errs.append(f"{cid}: definition text differs from O*NET {s['identifier']}")
                elif not any(i.get("code") == s["identifier"] for i in r.get("identifiers", [])):
                    errs.append(f"{cid}: O*NET identifier {s['identifier']} is not this concept's canonical identifier")
                if s.get("version") != "30.2":
                    errs.append(f"{cid}: O*NET version must be 30.2")
            elif s.get("source", "").startswith("Open English WordNet") and s.get("version") != "oewn:2025":
                errs.append(f"{cid}: WordNet source must use version 'oewn:2025'")
        for v in e.get("variants", []):
            if not isinstance(v.get("label"), str) or not v["label"].strip() or v.get("basis") not in BASES:
                errs.append(f"{cid}: malformed variant {v}")
            else:
                if "ambiguous" in v and v["ambiguous"] is not True:
                    errs.append(f"{cid}: variant ambiguous must be true when present")
                variant_owner[v["label"].casefold()].add((cid, bool(v.get("ambiguous"))))
        seen_pairs = set()
        for rel in e.get("relations", []):
            t = rel.get("target")
            if rel.get("type") not in REL_TYPES:
                errs.append(f"{cid}: relation type {rel.get('type')!r} invalid")
            if t not in inv_by_id:
                errs.append(f"{cid}: relation target {t!r} not in roster")
                continue
            if t == cid:
                errs.append(f"{cid}: self relation")
            if rel.get("target_label") != inv_by_id[t]["preferred_name"]:
                errs.append(f"{cid}: relation target_label mismatch for {t}")
            if rel.get("basis") not in BASES:
                errs.append(f"{cid}: relation basis invalid")
            if (rel["type"], t) in seen_pairs:
                errs.append(f"{cid}: duplicate relation {rel['type']} -> {t}")
            seen_pairs.add((rel["type"], t))
            if rel["type"] in ("broader", "part_of"):
                graph[cid].add(t)
        for f in e.get("flags", []):
            if f.get("type") not in FLAG_TYPES or not f.get("note"):
                errs.append(f"{cid}: malformed flag {f}")
    for txt, who in seen_text.items():
        if len(who) > 1:
            errs.append(f"identical definition text on {len(who)} concepts: {who[:4]}")
    # cycles in broader/part_of
    state = {}

    def dfs(u, path):
        state[u] = 1
        for w in graph.get(u, ()):
            if state.get(w) == 1:
                errs.append(f"broader/part_of cycle through {u} -> {w}")
            elif w not in state:
                dfs(w, path + [w])
        state[u] = 2
    for u in list(graph):
        if u not in state:
            dfs(u, [u])
    shared_ambiguous = 0
    for lab, owners in variant_owner.items():
        if len({o for o, _ in owners}) > 1:
            if all(a for _, a in owners):
                shared_ambiguous += 1
            else:
                errs.append(f"variant {lab!r} is attached to {len({o for o, _ in owners})} concepts and not marked ambiguous on all of them")
    # 4. coverage.json must equal counts recomputed from files
    recomputed = coverage(inv, ents)
    if cov != recomputed:
        errs.append("coverage.json does not match counts recomputed from inventory.jsonl/entries.jsonl (run build)")
    # 5. final gate
    if full:
        if len(ents) != EXPECTED_TOTAL or recomputed["pending"] != 0:
            errs.append(f"--full: {len(ents)} entries / {recomputed['pending']} pending; need {EXPECTED_TOTAL} / 0")
        for k, v in EXPECTED.items():
            if recomputed["per_class"].get(k, {}).get("drafted") != v:
                errs.append(f"--full: class {k} drafted {recomputed['per_class'].get(k, {}).get('drafted')} != {v}")
    report(errs, warns, extra=f"entries={len(ents)} inventory={len(inv)} drafted={recomputed['drafted']} pending={recomputed['pending']} "
                              f"unique_definitions={len(seen_text)} per_class_drafted="
                              f"{ {k: v['drafted'] for k, v in recomputed['per_class'].items()} }")


def report(errs, warns, extra=""):
    for w in warns[:20]:
        print("WARN:", w)
    if len(warns) > 20:
        print(f"WARN: ... {len(warns) - 20} more warnings")
    if errs:
        print(f"VALIDATION FAILED: {len(errs)} error(s)")
        for e in errs[:60]:
            print("  -", e)
        if len(errs) > 60:
            print(f"  ... and {len(errs) - 60} more")
        sys.exit(1)
    print("VALIDATION OK;", extra, f"(warnings: {len(warns)})")
    if "--" not in sys.argv:
        pass


def cmd_markdown():
    ents = read_jsonl(P_ENT)
    cov = json.loads(P_COV.read_text(encoding="utf-8"))
    lines = [f"# Skills Lexicon: {MODEL_LABEL} edition", "",
             f"Machine drafts by **{MODEL_LABEL}** (`{MODEL_ID}`) for the roster pinned at "
             f"[`{PINNED[:7]}`]({SOURCE_REPO}/commit/{PINNED}). Not human-reviewed. "
             f"{cov['drafted']} of {cov['total']} concepts drafted ({cov['pending']} pending).", "",
             "| Class | Drafted | Total |", "|---|---:|---:|"]
    for c in ("skill", "ability", "knowledge", "language"):
        v = cov["per_class"].get(c, {"drafted": 0, "total": 0})
        lines.append(f"| {c} | {v['drafted']} | {v['total']} |")
    lines += ["", "Each entry shows its kind, concept ID, definition, basis, and any variants, relations and flags. "
              "`basis: model_knowledge` means no permitted source was matched to the exact claim.", ""]
    cur_class = cur_kind = None
    for e in ents:
        if e["class"] != cur_class:
            cur_class, cur_kind = e["class"], None
            lines += [f"## {cur_class.capitalize()}", ""]
        if e["kind"] != cur_kind:
            cur_kind = e["kind"]
            lines += [f"### Kind: {cur_kind}", ""]
        d = e["definition"]
        b = "O*NET 30.2 " + d["sources"][0]["identifier"] if d["basis"] == "source" else "model knowledge"
        lines.append(f"**{e['preferred_name']}** (`{e['concept_id']}`, {e['kind']}; basis: {b})  ")
        lines.append(d["text"])
        extra = []
        if e["variants"]:
            extra.append("Variants: " + "; ".join(v["label"] for v in e["variants"]))
        if e["relations"]:
            extra.append("Relations: " + "; ".join(f"{r['type']} → {r['target_label']} (`{r['target']}`)" for r in e["relations"]))
        if e["flags"]:
            extra.append("Flags: " + "; ".join(f"{f['type']}: {f['note']}" for f in e["flags"]))
        if extra:
            lines.append("")
            lines.append("<br>".join(extra))
        lines.append("")
    P_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote entries.md ({len(ents)} entries)")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "build":
        cmd_build()
    elif cmd == "show":
        cmd_show(sys.argv[2:])
    elif cmd == "find":
        cmd_find(sys.argv[2:])
    elif cmd == "validate":
        cmd_validate(sys.argv[2:])
    elif cmd == "markdown":
        cmd_markdown()
    else:
        print(__doc__)
        sys.exit(2)
