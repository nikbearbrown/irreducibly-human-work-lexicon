#!/usr/bin/env python3
"""Concatenate batch drafts and reports into drafts-full.jsonl / report-full.jsonl, in bundle order, and render entries-full.md."""
import glob, json, os, subprocess, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = [json.loads(l) for l in open(os.path.join(HERE, "out", "bundles-full.jsonl"))]
D, R = {}, {}
for p in sorted(glob.glob(os.path.join(HERE, "out", "drafts", "b*.jsonl"))):
    if p.endswith(".report.jsonl"): continue
    for d in map(json.loads, open(p)): D[d["concept_id"]] = d
    for r in map(json.loads, open(p.replace(".jsonl", ".report.jsonl"))): R[r["concept_id"]] = r
order = [b["concept_id"] for b in B if b["concept_id"] in D]
with open(os.path.join(HERE, "drafts-full.jsonl"), "w") as f:
    for c in order: f.write(json.dumps(D[c], ensure_ascii=False) + "\n")
with open(os.path.join(HERE, "report-full.jsonl"), "w") as f:
    for c in order: f.write(json.dumps(R[c], ensure_ascii=False) + "\n")
bp = os.path.join(HERE, "out", "bundles-done.tmp.jsonl")
with open(bp, "w") as f:
    for b in B:
        if b["concept_id"] in D: f.write(json.dumps(b, ensure_ascii=False) + "\n")
subprocess.run([sys.executable, "/workspace/ihwl/replication/scripts/render_entries.py", bp,
                os.path.join(HERE, "drafts-full.jsonl"), os.path.join(HERE, "report-full.jsonl"),
                os.path.join(HERE, "entries-full.md")], check=True)
os.remove(bp)
print(len(order), "drafts assembled;", sum(R[c]["status"] == "pass" for c in order), "pass")
