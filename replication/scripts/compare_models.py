#!/usr/bin/env python3
"""Side-by-side comparison of several models' pilot folders, once every model has handed in.

Usage: python3 compare_models.py OUT.md FOLDER [FOLDER ...]

Each FOLDER is one model's hand-in (lex-pilot-<model>-<date>/ with bundles.jsonl, drafts-grounded.jsonl,
report-grounded.jsonl). Links are shown with the titles from that model's own bundle, since each model
gathered its own sources. Writes one section per concept, then a summary table.
"""
import json
import os
import sys


def load(path):
    if not os.path.exists(path):
        return {}
    return {json.loads(l)["concept_id"]: json.loads(l) for l in open(path) if l.strip()}


def link_label(kind, choice, b):
    if choice is None:
        return "abstained"
    if kind == "wikipedia":
        hit = next((w["title"] for w in b.get("wikipedia", []) if str(w["revision_id"]) == str(choice)), None)
    elif kind == "wikidata":
        hit = next((f"{i['qid']} {i['label']}" for i in b.get("wikidata", []) if i["qid"] == choice), None)
    else:
        hit = next((f"{s['synset']} {', '.join(s['lemmas'][:2])}" for s in b.get("wordnet", []) if s["synset"] == choice), None)
    return hit or f"{choice} (not in its bundle)"


def main(out, *folders):
    runs = []
    for f in folders:
        name = os.path.basename(os.path.normpath(f))
        runs.append((name, load(os.path.join(f, "bundles.jsonl")), load(os.path.join(f, "drafts-grounded.jsonl")),
                     load(os.path.join(f, "report-grounded.jsonl"))))
    ids = list(dict.fromkeys(cid for _, b, _, _ in runs for cid in b))
    lines, summary = ["# Model comparison: grounded drafts", ""], []
    for cid in ids:
        name = next((b[cid]["concept"]["preferred_name"] for _, b, _, _ in runs if cid in b), cid)
        lines += [f"## {name} ({cid})", ""]
        for model, b, d, r in runs:
            e, bb = d.get(cid), b.get(cid, {})
            if not e:
                lines += [f"**{model}:** no draft", ""]
                continue
            links = e.get("links", {})
            rels = "; ".join(f"{x.get('type')} → {x.get('target_label')}" for x in e.get("relations", [])) or "none"
            lines += [f"**{model}** ({r.get(cid, {}).get('status', '?')})", "",
                      f"- Definition: {e.get('definition', {}).get('text', '')}",
                      "- Links: " + "; ".join(f"{k} = {link_label(k, links.get(k, {}).get('choice'), bb)}"
                                             for k in ("wikipedia", "wikidata", "wordnet")),
                      f"- Variants: {', '.join(v.get('text', '') for v in e.get('variants', [])) or 'none'}",
                      f"- Relations: {rels}",
                      f"- Flags: {len(e.get('flags', []))}", ""]
            summary.append((model, cid, len(e.get("relations", [])), r.get(cid, {}).get("status")))
    lines += ["## Summary", "", "| model | drafts | passed checks | relations per draft |", "|---|---:|---:|---:|"]
    for model, _, d, r in runs:
        n = len(d)
        lines.append(f"| {model} | {n} | {sum(x.get('status') == 'pass' for x in r.values())} | "
                     f"{(sum(len(e.get('relations', [])) for e in d.values()) / n if n else 0):.1f} |")
    open(out, "w").write("\n".join(lines) + "\n")
    print(f"wrote {out}: {len(ids)} concepts, {len(runs)} models")


if __name__ == "__main__":
    main(*sys.argv[1:])
