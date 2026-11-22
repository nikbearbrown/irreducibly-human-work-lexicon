#!/usr/bin/env python3
"""The exact messages Claude drafted from, one concept per line, for drafting with any model.

Usage: python3 scripts/render_prompts.py BUNDLES.jsonl OUT.jsonl [--ungrounded]

Each line is {"concept_id", "system", "user"}: send `system` as the system prompt and `user` as the
message, one concept per fresh conversation. Save each JSON reply on its own line with a `_meta` object
(model, run, attempts), then check the file with verify_drafts.py.
--ungrounded empties wikipedia, wikidata and wordnet first, as the pilot's comparison run did.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE]
from generate_drafts import fill  # the same rendering Claude's calls used
from verify_drafts import ungrounded

PROMPTS = os.path.join(os.path.dirname(HERE), "prompts")


def main():
    src, out = sys.argv[1], sys.argv[2]
    bare = "--ungrounded" in sys.argv[3:]
    system = open(os.path.join(PROMPTS, "system.txt")).read().strip()
    template = open(os.path.join(PROMPTS, "user_template.txt")).read()
    n = 0
    with open(out, "w") as f:
        for line in open(src):
            if not line.strip():
                continue
            b = json.loads(line)
            if bare:
                b = ungrounded(b)
            f.write(json.dumps({"concept_id": b["concept_id"], "system": system, "user": fill(template, b)},
                               ensure_ascii=False) + "\n")
            n += 1
    print(f"{n} prompts written to {out}")


if __name__ == "__main__":
    main()
