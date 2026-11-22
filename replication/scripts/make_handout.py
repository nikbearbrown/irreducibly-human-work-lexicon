#!/usr/bin/env python3
"""Hand-out messages for a model that drafts from pasted or attached files only (no web, no fetching).

Usage: python3 pilot/make_handout.py BUNDLES.jsonl OUT_DIR [--max-chars 150000]

Writes one self-contained message per chunk: the pilot's drafting instructions (system.txt, word for word)
and each concept's material rendered exactly as Claude received it (user_template.txt). The ungrounded run
comes first, as 00-ungrounded.md, so the model has seen no sources when it drafts without them; then
01-grounded.md, 02-grounded.md and so on. Bundles are inputs only: nothing here comes from any model's drafts.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE, os.path.dirname(HERE)]  # generate_drafts.py sits beside this script or one folder up
from generate_drafts import fill  # same rendering as Claude's own calls


def prompt_file(name):
    """prompts/ next to the scripts folder (replication kit), else the folder above (lex/)."""
    for d in (os.path.join(os.path.dirname(HERE), "prompts"), os.path.dirname(HERE)):
        if os.path.exists(os.path.join(d, name)):
            return os.path.join(d, name)
    raise SystemExit(f"can't find {name}")


SYSTEM = open(prompt_file("system.txt")).read().strip()
TEMPLATE = open(prompt_file("user_template.txt")).read()

HEADER = """# Skills Lexicon pilot, {label}: message {num} of {chunks} (chunk {chunk}, {n} concepts)

Everything you need is in this message. Don't fetch, search or look anything up. Draft only from what is here and what you already know.

**Independence.** Several models are drafting these same 36 entries separately so Nik Bear Brown can compare them. Don't read, search for or ask for any other model's drafts, including Claude's. The material below is source material only (the lexicon's record, candidate neighbors, posting snippets{sources}); it holds no one's drafts.

**How to work.** Treat each concept on its own, as if you had never seen the others: don't carry a decision, a wording or a relation from one concept to the next. {run_note}

**Instructions for every concept** (use them exactly as written):

~~~~text
{system}
~~~~

**Before you answer**, check every draft against this list and fix what fails (one pass of fixes, no more):

- `links.wikipedia`, `links.wikidata` and `links.wordnet` each have a `choice`, and each is null or one of that concept's candidates below.
- The definition, each variant and each relation has `basis` `source` or `model_knowledge`, and every `source` claim has at least one pointer.
- Every pointer resolves in the material below: `wd:` names the linked item or one of its ancestors and the statement or alias is really there; `wn:` names the linked synset and the lemma or relation is really there; `wp:` names the linked article's revision id and quotes at most 20 words that appear word for word; `ex:` names an example below.
- Only the nine relation types. A `target_id` must be one of that concept's neighbors.
- `certifies` only when the concept's `kind` is `credential`.
- The definition shares no run of 9 or more consecutive words with any Wikipedia text below.

**What to send back.** One JSON object per concept, one per line, in the order below, each with one extra field:
`"_meta": {{"model": "<your model and version>", "run": "{run}", "chunk": "{chunk}", "attempts": 1}}`.
If you can make files, send a file named `drafts-{run}-{chunk}.jsonl`. Otherwise send one code block marked `jsonl` holding the {n} lines and nothing else. A script will check them afterwards.{last}

---
"""

RUN_NOTE = {
    "ungrounded": "This is the **ungrounded** run: the Wikipedia, Wikidata and WordNet lists are empty on purpose.",
    "grounded": "This is the **grounded** run: each concept comes with its candidate Wikipedia articles, Wikidata items and WordNet senses.",
}

LAST = """

**This is the last chunk.** After the drafts, add a short note headed `RUN.md` with: your model and version and any reasoning or effort setting; when you started chunk 00 and finished this one (date and time, with time zone); and anything you did differently from these instructions, with the reason."""


def render(b):
    return fill(TEMPLATE, b)


def chunks_of(bundles, max_chars):
    out, cur, size = [], [], 0
    for b in bundles:
        n = len(render(b))
        if cur and size + n > max_chars:
            out.append(cur)
            cur, size = [], 0
        cur.append(b)
        size += n
    if cur:
        out.append(cur)
    return out


def write(path, label, run, chunk, chunks, group, last):
    parts = [HEADER.format(label=label, chunk=chunk, num=int(chunk) + 1, chunks=chunks, n=len(group), run=run,
                           sources="" if run == "ungrounded" else ", Wikipedia, Wikidata and WordNet candidates",
                           run_note=RUN_NOTE[run], system=SYSTEM, last=LAST if last else "")]
    for i, b in enumerate(group, 1):
        c = b["concept"]
        parts.append(f"## Concept {i} of {len(group)}: {c['preferred_name']} (`{b['concept_id']}`)\n\n"
                     f"~~~~text\n{render(b).strip()}\n~~~~\n")
    text = "\n".join(parts)
    assert "~~~~" not in "".join(render(b) for b in group), "fence clash"
    open(path, "w").write(text)
    return len(text)


def main():
    src, out_dir = sys.argv[1], sys.argv[2]
    max_chars = int(sys.argv[sys.argv.index("--max-chars") + 1]) if "--max-chars" in sys.argv else 150000
    bundles = [json.loads(l) for l in open(src) if l.strip()]
    os.makedirs(out_dir, exist_ok=True)
    bare = [dict(b, wikipedia=[], wikidata=[], wordnet=[]) for b in bundles]
    grounded = chunks_of(bundles, max_chars)
    ungrounded = chunks_of(bare, max_chars)
    total = len(ungrounded) + len(grounded)
    files, k = [], 0
    for group in ungrounded:
        name = f"{k:02d}-ungrounded.md"
        files.append((name, write(os.path.join(out_dir, name), "ungrounded run", "ungrounded",
                                  f"{k:02d}", total, group, False), len(group)))
        k += 1
    for j, group in enumerate(grounded):
        name = f"{k:02d}-grounded.md"
        files.append((name, write(os.path.join(out_dir, name), "grounded run", "grounded",
                                  f"{k:02d}", total, group, j == len(grounded) - 1), len(group)))
        k += 1
    for name, size, n in files:
        print(f"{name}: {n} concepts, {size:,} characters")


if __name__ == "__main__":
    main()
