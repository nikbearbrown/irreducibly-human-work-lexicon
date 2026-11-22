#!/usr/bin/env python3
"""Render verified drafts as WordNet-style markdown for human review.

Usage: python3 render_entries.py BUNDLES.jsonl DRAFTS.jsonl REPORT.jsonl ENTRIES.md
"""
import json
import sys

from verify_drafts import is_credential, load_jsonl

SECTIONS = [("synonym", "Synonymy"), ("hypernym", "Hypernymy"), ("hyponym", "Hyponymy"),
            ("meronym", "Meronymy"), ("holonym", "Part Holonyms"), ("uses", "Uses"),
            ("requires", "Requires"), ("certifies", "Certifies"), ("contrast", "Contrast")]


def tag(c):
    return "source" if c.get("basis") == "source" else "model knowledge, unsourced"


def render(b, d, r):
    name = b["concept"].get("preferred_name", d["concept_id"])
    lines = [f"## {name}", "", f"*{d['concept_id']} | verifier: {r['status']}*", ""]
    if r["errors"]:
        lines += ["**Verifier errors:**", ""] + [f"- {e}" for e in r["errors"]] + [""]
    if d.get("definition"):
        lines += [f"**{name} (n.):** {d['definition'].get('text', '')} *({tag(d['definition'])})*", ""]
    lines += ["**Variants:**", ""]
    lines += [f"- {v['text']}" + (f" (only when {v['condition']})" if v.get("condition") else "")
              + f" *({tag(v)})*" for v in d.get("variants", [])] or ["- None"]
    lines.append("")
    for key, title in SECTIONS:
        if key == "certifies" and not is_credential(b["concept"]):
            continue
        rels = [x for x in d.get("relations", []) if x.get("type") == key]
        lines += [f"**{title}:**", ""]
        lines += [f"- {x['target_label']}" + (" (proposed new concept)" if x.get("proposed_new") else "")
                  + (f": {x['note']}" if x.get("note") else "") + f" *({tag(x)})*" for x in rels] or ["- None"]
        lines.append("")
    links = d.get("links", {})
    lines += ["**Source links:**", ""]
    for s in ("wikipedia", "wikidata", "wordnet"):
        l = links.get(s, {})
        lines.append(f"- {s}: {l.get('choice') or 'abstained'} ({l.get('reason', 'no reason given')})")
    if d.get("flags"):
        lines += ["", "**Flags for reviewer:**", ""] + [f"- {f}" for f in d["flags"]]
    return "\n".join(lines) + "\n\n---\n"


def main(bundle_path, draft_path, report_path, out_path):
    bundles, drafts, reports = (load_jsonl(p) for p in (bundle_path, draft_path, report_path))
    with open(out_path, "w") as out:
        out.write("# Draft entries (machine-drafted, unreviewed)\n\n")
        for cid, d in drafts.items():
            out.write(render(bundles[cid], d, reports[cid]))


if __name__ == "__main__":
    main(*sys.argv[1:5])
