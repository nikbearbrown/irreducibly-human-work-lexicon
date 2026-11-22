#!/usr/bin/env python3
"""Collect every draft's flags into one CSV, sorted into rough kinds by keyword, for a reviewer.

Usage: python3 collect_flags.py OUT.csv WORK_DIR [WORK_DIR ...]
Reads WORK_DIR/drafts.jsonl (a batch folder) or every WORK_DIR/drafts-*.jsonl (a hand-in folder), and
WORK_DIR/bundles.jsonl for concept names when it is there. The kinds are a keyword sort, not a judgement:
read the flag itself before acting on it.
"""
import csv
import glob
import json
import os
import re
import sys

KINDS = [
    ("record_fix", r"(existing|record|lexicon'?s?)\b.{0,160}(misspel|typo|scrap|error|inaccura|wrong|incorrect|"
                   r"should (be|say|read)|remov|retyp|mislabel|broad_class|kind ?=|kind is|footnote|outdated|"
                   r"present tense|not a |doesn't mention|does not mention|rewrites?)"),
    ("status_change", r"retired|deprecated|phased out|discontinued|offline|renamed|rebrand|superseded|successor|"
                      r"legacy|end of life|end-of-life|no longer"),
    ("ambiguity", r"ambiguous|ambiguity|collision|keyword|may mean|false (match|positive)|matching risk|"
                  r"also (the name|means|refers)"),
    ("possible_duplicate", r"overlap|duplicat|merge|same concept|near-?duplicate|already (in|exists)"),
    ("no_sources", r"no (usage )?examples|no source|no sources|no wikipedia|no reference|were not provided|"
                   r"was not provided|weren't provided"),
    ("left_out", r"left out|omitted|dropped|not included|leaving out|did not add|didn't add"),
]


def kind(text):
    for name, pattern in KINDS:
        if re.search(pattern, text, re.I | re.S):
            return name
    return "other"


def main(out, *dirs):
    rows = []
    for d in dirs:
        names = {}
        if os.path.exists(f"{d}/bundles.jsonl"):
            for line in open(f"{d}/bundles.jsonl"):
                b = json.loads(line)
                names[b["concept_id"]] = b["concept"].get("preferred_name", "")
        folder = d.rstrip("/").split("/")[-1]
        files = [f"{d}/drafts.jsonl"] if os.path.exists(f"{d}/drafts.jsonl") else sorted(glob.glob(f"{d}/drafts-*.jsonl"))
        for path in files:
            run = os.path.basename(path)[len("drafts-"):-len(".jsonl")] if "drafts-" in path else ""
            for line in open(path):
                if not line.strip():
                    continue
                x = json.loads(line)
                for i, f in enumerate(x.get("flags", []), 1):
                    rows.append({"batch": f"{folder}/{run}" if run else folder, "concept_id": x["concept_id"],
                                 "name": names.get(x["concept_id"], ""), "flag_no": i, "kind": kind(f), "flag": f})
    order = [k for k, _ in KINDS] + ["other"]
    rows.sort(key=lambda r: (order.index(r["kind"]), r["batch"], r["name"].lower()))
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["kind", "batch", "concept_id", "name", "flag_no", "flag"])
        w.writeheader()
        w.writerows(rows)
    counts = {k: sum(r["kind"] == k for r in rows) for k in order}
    print(len(rows), "flags;", counts)


if __name__ == "__main__":
    main(*sys.argv[1:])
