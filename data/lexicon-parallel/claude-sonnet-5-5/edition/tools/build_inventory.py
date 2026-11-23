#!/usr/bin/env python3 -I
"""Build inventory.jsonl from the pinned source checkout.

Reads ONLY structural fields from each source entry (id, preferred_name, kind, identifiers).
It never reads or copies the source `definition`, `description`, `evidence` or any other prose.
Usage: build_inventory.py <source_checkout> <out_inventory.jsonl> <out_roster_meta.json>
"""
import json, sys, glob, os, collections, subprocess

src, out_inv, out_meta = sys.argv[1:4]
LANGUAGE_KINDS = {"programming-language", "markup-language", "style-language", "modeling-language", "human-language"}

def top_class(kind):  # mirrors tools/lexicon.py top_class in the source
    return ("ability" if kind == "ability" else "knowledge" if kind == "knowledge" else "certification" if kind == "credential"
            else "language" if kind in LANGUAGE_KINDS else "skill")

CLASS_ORDER = {"ability": 0, "language": 1, "knowledge": 2, "skill": 3}
KIND_ORDER = ["ability", "human-language", "programming-language", "markup-language", "style-language", "modeling-language",
              "knowledge", "skill", "method", "standard", "tool", "platform", "library", "framework", "work-activity"]

rows, all_counts, out_of_scope, oos_ids = [], collections.Counter(), collections.Counter(), []
for f in glob.glob(os.path.join(src, "entries", "*.json")):
    e = json.load(open(f, encoding="utf-8"))
    kind, cls = e["kind"], top_class(e["kind"])
    all_counts[cls] += 1
    if cls == "certification":
        out_of_scope[cls] += 1
        oos_ids.append(e["id"])
        continue
    idents = [{"scheme": i.get("scheme"), "code": i.get("code")} for i in e.get("identifiers", [])]
    rows.append({"concept_id": e["id"], "preferred_name": e["preferred_name"], "kind": kind, "class": cls,
                 "source_key": e.get("key"), "identifiers": idents})

rows.sort(key=lambda r: (CLASS_ORDER[r["class"]], KIND_ORDER.index(r["kind"]) if r["kind"] in KIND_ORDER else 99,
                         r["preferred_name"].casefold(), r["concept_id"]))
with open(out_inv, "w", encoding="utf-8") as fh:
    for n, r in enumerate(rows, 1):
        rec = {"n": n, **{k: r[k] for k in ("concept_id", "preferred_name", "kind", "class")}, "status": "pending"}
        if r["identifiers"]:
            rec["identifiers"] = r["identifiers"]
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

open(os.path.join(os.path.dirname(out_meta), "out-of-scope-credential-ids.txt"), "w").write("\n".join(sorted(oos_ids)) + "\n")
commit = subprocess.run(["git", "-C", src, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
meta = {"source_repo": "https://github.com/nikbearbrown/skills-lexicon", "pinned_commit": commit,
        "source_entry_files": sum(all_counts.values()), "all_classes_in_source": dict(all_counts),
        "out_of_scope_counts": dict(out_of_scope),
        "in_scope_total": len(rows),
        "in_scope_by_class": dict(collections.Counter(r["class"] for r in rows)),
        "in_scope_by_kind": dict(collections.Counter(r["kind"] for r in rows)),
        "duplicate_labels_casefold": sorted([k for k, v in collections.Counter(r["preferred_name"].casefold() for r in rows).items() if v > 1])}
json.dump(meta, open(out_meta, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(json.dumps(meta, indent=2, ensure_ascii=False))
