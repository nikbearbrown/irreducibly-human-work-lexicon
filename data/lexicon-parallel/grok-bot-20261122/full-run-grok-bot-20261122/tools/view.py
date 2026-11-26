#!/usr/bin/env python3
"""Print a compact view of bundles START..END (0-based, end exclusive): name, kind, variants, record relations, top neighbors."""
import json, sys, os
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s, e, k = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]) if len(sys.argv) > 3 else 8
for i, l in enumerate(open(os.path.join(HERE, "out", "bundles-full.jsonl"))):
    if i < s: continue
    if i >= e: break
    b = json.loads(l); c = b["concept"]
    v = "|".join(x["label"] + (f"[{','.join(x['needs_context'])}]" if x.get("needs_context") else "") for x in c["variants"])
    r = ",".join(f"{x['type']}>{x['target_name']}" for x in c["relations"])
    print(f"{c['id']} {c['preferred_name']} ({c['kind']}) v:{v} r:{r} N:{"; ".join(n["name"][:40] for n in b["neighbors"][:k])}")
