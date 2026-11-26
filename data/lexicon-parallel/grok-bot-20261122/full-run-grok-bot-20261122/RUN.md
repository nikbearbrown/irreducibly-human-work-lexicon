# RUN.md: Grok full parallel run (all 3,718 non-pilot concepts)

Professor Bear (2026-11-22): "keep on doing it until you've done all of the entries. You're doing a complete parallel run."
The 36 pilot concepts are in `../lex-pilot-grok-bot-20261122/` (grounded and ungrounded). This folder covers the other
3,718 concepts in `replication/concepts/batch_0002.tsv` to `batch_0005.tsv`, in that order.

- **Model:** Grok Bot. **Prompt version:** gen-v2. **Started:** 2026-11-22, about 8:15 PM EST.
- **Independence:** no other model's drafts opened; no other AI used; no web or X search.

## Input path chosen, and why

**No-source bundles (the kit's ungrounded run), all claims `model_knowledge`.**

- The kit's way A needs the Explorer cluster (Wikipedia dump, Kaggle copies, `observations.jsonl` on a data branch)
  and the public Wikipedia and Wikidata APIs. Building Wikipedia/Wikidata/WordNet bundles for 3,718 concepts is
  scriptable, but grounded drafting means reading each concept's sources (about 38 KB per concept in the pilot,
  roughly 140 MB of text in total), far beyond what one drafter can read in this run. A half-read bundle would invite
  pointers that do not say what is claimed, which the rules call an error.
- Usage examples need the allow-listed Kaggle datasets, which need a Kaggle login this box does not have.
- So every bundle here has the kit's contract with `examples`, `wikipedia`, `wikidata` and `wordnet` empty, which is
  exactly the input of the pilot's ungrounded run. Grounded drafts for these concepts remain possible later from
  bundles built with `replication/scripts/assemble_bundles.py`.

## How the bundles were built (reproducible)

`tools/build_bundles.py` reads the lexicon at commit `91312fec` (the kit's reference commit) and, for each concept,
writes the concept record (id, preferred name, kind, broad class, variants, existing relations) and 30 neighbors from
the kit's own `neighbors()` in `replication/scripts/assemble_bundles.py`, called with no source text. Output:
`out/bundles-full.jsonl` (3,718 lines). The lexicon's own definitions are not put in the bundles (as in the pilot's
contract), and I did not read them.

## How drafting works

- I read a compact view of 50 bundles at a time (`tools/view.py`: name, kind, variants, existing relations, top 4 to 8 neighbors),
  then write one line per concept in `batches/bNNNN.txt`: work sense | definition | relations | extras.
- `tools/compile.py` turns each line into the gen-v2 JSON object: links all null (abstain, no candidates), every
  claim `model_knowledge` with no pointers, the record's variants kept (their `needs_context` becomes the condition)
  unless I drop or qualify them, and relation targets resolved to neighbor ids by exact name.
- A target that exists in the lexicon but is not among the bundle's 30 neighbors gets `target_id` null and
  `proposed_new` true, as prompt step 7 requires, with a note naming the lexicon id, so a reviewer can link it.
  (The kit's neighbor list is name-similarity only when there are no sources, so many true targets fall outside it.)
- Each batch is checked with the kit's `verify_drafts.py --ungrounded`; reports in `out/drafts/*.report.jsonl`.
  A failed draft gets one retry (`compile.py NAME --attempt 2`).
- Judgment calls: I add `contrast` only for names a matcher or reader could really confuse, not for every
  name-similar neighbor; generic records named like O*NET areas (for example "Production and Processing") are
  drafted in that sense and flagged.

## Progress

**Complete (2026-11-22, EST):** all 75 batches compiled; 3,718 / 3,718 concepts pass the kit checker,
0 fail. `drafts-full.jsonl`, `report-full.jsonl` and `entries-full.md` are assembled.

See `manifest.json` (done, failed, remaining, next concept id and index). Batches are numbered in bundle order,
50 concepts each: batch `bNNNN` covers bundle lines `(NNNN-1)*50` to `NNNN*50 - 1`.

## How to resume

1. `python3 tools/view.py START END 5` with START = `next_index` from `manifest.json`, END = START + 50.
2. Write the next `batches/bNNNN.txt` in the line format in `tools/compile.py`.
3. `python3 tools/compile.py bNNNN`, fix any failure once with `--attempt 2`, commit, push to the private repo.
4. When all are done: `python3 tools/assemble.py` concatenates `out/drafts/*.jsonl` into `drafts-full.jsonl` and
   `report-full.jsonl`, and renders `entries-full.md` with the kit's `render_entries.py`.
