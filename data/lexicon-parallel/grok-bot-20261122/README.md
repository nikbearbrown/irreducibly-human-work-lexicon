# Grok Bot edition

An unmodified copy of Grok Bot's independent Irreducibly Human Work Lexicon drafts, taken from the private source repository named below. The draft files themselves were not edited for this transfer.

| Field | Value |
|---|---|
| Model | Grok Bot |
| Source repository | [nikbearbrown/irreducibly-human-work-lexicon-grok](https://github.com/nikbearbrown/irreducibly-human-work-lexicon-grok) (private) |
| Commit | [`64aa98f8440710c6543910c70acca37d7b5ffbd2`](https://github.com/nikbearbrown/irreducibly-human-work-lexicon-grok/commit/64aa98f8440710c6543910c70acca37d7b5ffbd2) (`main` and `grok-lex-pilot` were at this same commit) |
| Date | 22 November 2026, 9:03 PM EST (America/New_York); commit timestamp 2026-11-23 02:03:17 UTC |
| Roster pin | Lexicon commit `91312fec957388afe4d1dfbdb4aff2707588b9a1` |
| Prompt / schema | Replication kit prompt gen-v2 and its draft schema |
| Human review | None. Every entry is a machine draft. |

This source repository is private. This copy lives in the public paper repository because the owner asked for the editions to be added here.

## What's in this folder

### Pilot: [`lex-pilot-grok-bot-20261122/`](lex-pilot-grok-bot-20261122/)

36-concept comparison set from the replication kit, drafted independently (no other model's drafts were opened).

| Field | Ungrounded | Grounded |
|---|---:|---:|
| Concepts drafted | 36 / 36 | 36 / 36 |
| Passed `verify_drafts.py` | 36 | 36 (one after a single retry) |
| Method | Concept record, neighbors and usage examples only; drafted and committed before any source text was opened | Full shared bundles (Wikipedia, Wikidata, WordNet added) |

Copied files: `drafts-ungrounded.jsonl`, `drafts-grounded.jsonl`, `report-ungrounded.jsonl`, `report-grounded.jsonl`, `entries-ungrounded.md`, `entries-grounded.md`, `README.md`, `RUN.md`.

Left out: the `work/` directory (compact views, raw batch files, and scripts).

### Full run: [`full-run-grok-bot-20261122/`](full-run-grok-bot-20261122/)

Complete parallel run over the remaining concepts.

| Field | Value |
|---|---|
| Concepts drafted | 3,718 / 3,718 |
| Passed `verify_drafts.py --ungrounded` | 3,718 pass, 0 fail (each pass has the expected "most claims rest on model knowledge" warning) |
| Method | No-source (ungrounded) input path only. Bundles are the concept record plus 30 nearest neighbors; sources are empty; every claim is `model_knowledge`; links are null. |

Copied files: `drafts-full.jsonl`, `report-full.jsonl`, `entries-full.md`, `manifest.json`, `README.md`, `RUN.md`, and `tools/` (bundle builder, compiler, assembler, viewer, ship script).

Left out: `out/bundles-full.jsonl` (input bundles), `out/drafts/` (per-batch intermediates already assembled into `drafts-full.jsonl`), `batches/*.txt` (compact drafting input), empty `views/`, and `out/build.log`. Those remain in the source repository.

No copied file is over 50 MB.
