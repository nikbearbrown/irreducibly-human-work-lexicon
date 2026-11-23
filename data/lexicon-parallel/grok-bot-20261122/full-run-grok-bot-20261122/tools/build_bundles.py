#!/usr/bin/env python3
"""Build no-source bundles for every concept in the kit's lists (all but pilot-36), reproducibly.

Same contract as replication/INSTRUCTIONS.md section 3, with examples, wikipedia, wikidata and wordnet left
empty (the kit's ungrounded run). Concept records and neighbors come from the lexicon at commit 91312fec,
using the kit's own neighbors() from replication/scripts/assemble_bundles.py with no source text.

Usage: python3 build_bundles.py LEXICON_AT_91312fec KIT_SCRIPTS_DIR CONCEPTS_DIR OUT.jsonl
"""
import collections, glob, json, os, sys
from multiprocessing import Pool
repo, kit, cdir, out = sys.argv[1:5]
sys.path.insert(0, kit)
import assemble_bundles as AB

entries = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(repo, "entries", "*.json")))]
by_id = {e["id"]: e for e in entries}
by_name = collections.defaultdict(list)
for e in entries:
    for f in [e["preferred_name"]] + [v["label"] for v in e.get("variants", [])]:
        by_name[f.lower()].append(e["id"])
ids = []
for f in ["batch_0002.tsv", "batch_0003.tsv", "batch_0004.tsv", "batch_0005.tsv"]:
    ids += [l.split("\t")[0] for l in open(os.path.join(cdir, f)) if l.strip()]

def one(cid):
    e = by_id[cid]
    concept = {"id": cid, "preferred_name": e["preferred_name"], "kind": e["kind"],
               "broad_class": AB.broad_class(e["kind"]),
               "variants": [{k: v[k] for k in ("label", "needs_context", "ambiguous") if k in v} for v in e.get("variants", [])],
               "relations": [{"type": r["type"], "target": r["target"],
                              "target_name": by_id.get(r["target"], {}).get("preferred_name")} for r in e.get("relations", [])]}
    return {"concept_id": cid, "concept": concept, "neighbors": AB.neighbors(e, entries, by_id, by_name, [], ""),
            "examples": [], "wikipedia": [], "wikidata": [], "wordnet": []}

if __name__ == "__main__":
    with Pool(8) as p, open(out, "w") as o:
        for i, b in enumerate(p.imap(one, ids, chunksize=8)):
            o.write(json.dumps(b, ensure_ascii=False) + "\n")
            if i % 250 == 0: print(i, flush=True)
    print("done", len(ids))
