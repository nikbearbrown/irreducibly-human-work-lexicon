#!/usr/bin/env python3
"""Turn Grok's compact draft lines into gen-v2 JSON drafts, check them with the kit, update the manifest.

Line format (one concept per line, fields split by ' | '):
  concept_id | work sense | definition | relations | extras
relations: items split by ';', each  T:Target name[~note]  with T in
  s synonym, h hypernym, o hyponym, m meronym, l holonym, u uses, q requires, c certifies, x contrast
extras: items split by ';':  v:text[~condition]  adds a variant,  -v:label  drops a record variant,  f:text  adds a flag
Every claim is basis model_knowledge (no-source run). Record variants are kept as variants unless dropped.
Usage: python3 compile.py BATCH_NAME [--attempt N]
"""
import json, os, re, subprocess, sys, collections, glob
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KIT = "/workspace/ihwl/replication/scripts"
LEX = "/workspace/ihwl-91312fec/entries"
T = dict(s="synonym", h="hypernym", o="hyponym", m="meronym", l="holonym", u="uses", q="requires", c="certifies", x="contrast")
MK = "model_knowledge"
NOLINK = "No candidates were provided in this bundle (no-source run), so I abstain."

def load_bundles():
    return {b["concept_id"]: b for b in map(json.loads, open(os.path.join(HERE, "out", "bundles-full.jsonl")))}

_lex = None
def lex_names():
    global _lex
    if _lex is None:
        _lex = collections.defaultdict(list)
        for f in glob.glob(os.path.join(LEX, "*.json")):
            e = json.load(open(f))
            for n in [e["preferred_name"]] + [v["label"] for v in e.get("variants", [])]:
                _lex[n.lower()].append(e["id"])
    return _lex

def cond_of(v):
    nc = v.get("needs_context")
    return ("in a context about " + " or ".join(nc)) if nc else None

def build(line, B, attempt):
    parts = [p.strip() for p in re.split(r"\s*\|\s*", line)]
    while len(parts) < 5: parts.append("")
    cid, sense, defn, rels, extras = parts[:5]
    if re.match(r"-?v:|f:", rels): rels, extras = "", (rels + "; " + extras).strip("; ")
    b = B[cid]
    nb = {n["name"].lower(): n["id"] for n in b["neighbors"]}
    drop, addv, flags = set(), [], []
    for x in [x.strip() for x in re.split(r";\s*(?=-?v:|f:)", extras) if x.strip()]:
        if x.startswith("-v:"): drop.add(x[3:].strip().lower())
        elif x.startswith("v:"):
            t, _, c = x[2:].partition("~"); addv.append({"text": t.strip(), "condition": c.strip() or None, "basis": MK, "pointers": []})
        elif x.startswith("f:"): flags.append(x[2:].strip())
        else: flags.append(x)
    variants = [{"text": v["label"], "condition": cond_of(v), "basis": MK, "pointers": []}
                for v in b["concept"]["variants"] if v["label"].lower() not in drop] + addv
    relations = []
    for r in [r.strip() for r in re.split(r";\s*(?=[shomluqcx]:)", rels) if r.strip()]:
        k, _, rest = r.partition(":")
        name, _, note = rest.partition("~")
        name, note = name.strip(), note.strip() or None
        tid = nb.get(name.lower())
        if tid is None and lex_names().get(name.lower()):
            ids = [i for i in lex_names()[name.lower()] if i != cid]
            if ids:
                extra = f"The lexicon has this concept ({', '.join(ids)}) but it is not among this bundle's neighbors."
                note = f"{note} {extra}" if note else extra
        relations.append({"type": T[k.strip()], "target_label": name, "target_id": tid, "proposed_new": tid is None,
                          "basis": MK, "pointers": [], "note": note})
    return {"concept_id": cid, "work_sense": sense,
            "links": {s: {"choice": None, "reason": NOLINK} for s in ("wikipedia", "wikidata", "wordnet")},
            "definition": {"text": defn, "basis": MK, "pointers": []},
            "variants": variants, "relations": relations, "flags": flags,
            "_meta": {"model": "grok-bot", "run": "ungrounded", "attempts": attempt, "prompt_version": "gen-v2",
                      "input": "no-source bundle (full run)", "unresolved_errors": []}}

def main():
    name = sys.argv[1]
    attempt = int(sys.argv[sys.argv.index("--attempt") + 1]) if "--attempt" in sys.argv else 1
    B = load_bundles()
    lines = [l.rstrip("\n") for l in open(os.path.join(HERE, "batches", name + ".txt")) if l.strip() and not l.startswith("#")]
    drafts = [build(l, B, attempt) for l in lines]
    os.makedirs(os.path.join(HERE, "out", "drafts"), exist_ok=True)
    dpath = os.path.join(HERE, "out", "drafts", name + ".jsonl")
    with open(dpath, "w") as f:
        for d in drafts: f.write(json.dumps(d, ensure_ascii=False) + "\n")
    bpath = os.path.join(HERE, "out", "drafts", name + ".bundles.jsonl")
    with open(bpath, "w") as f:
        for d in drafts: f.write(json.dumps(B[d["concept_id"]], ensure_ascii=False) + "\n")
    rpath = os.path.join(HERE, "out", "drafts", name + ".report.jsonl")
    subprocess.run([sys.executable, os.path.join(KIT, "verify_drafts.py"), bpath, dpath, rpath, "--ungrounded"], check=True)
    os.remove(bpath)
    bad = [r for r in map(json.loads, open(rpath)) if r["status"] != "pass"]
    for r in bad: print("FAIL", r["concept_id"], r["errors"])
    update_manifest(B)

def update_manifest(B):
    status = {}
    for rp in sorted(glob.glob(os.path.join(HERE, "out", "drafts", "*.report.jsonl"))):
        for r in map(json.loads, open(rp)):
            status[r["concept_id"]] = r["status"]
    order = list(B)
    done = [c for c in order if status.get(c) == "pass"]
    failed = [c for c in order if status.get(c) == "fail"]
    remaining = [c for c in order if c not in status]
    json.dump({"total": len(order), "done": len(done), "failed": failed, "remaining_count": len(remaining),
               "next_concept_id": remaining[0] if remaining else None, "next_index": order.index(remaining[0]) if remaining else None},
              open(os.path.join(HERE, "manifest.json"), "w"), indent=1)
    print(f"manifest: {len(done)} pass, {len(failed)} fail, {len(remaining)} remaining of {len(order)}")

if __name__ == "__main__":
    main()
