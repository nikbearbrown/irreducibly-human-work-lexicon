# Parallel lexicon editions

Independent, machine-drafted editions of the Irreducibly Human Work Lexicon, kept here as parallel evaluations so they can be compared side by side. Each subfolder is one model's edition. This layout follows the earlier `grok-lexicon-parallel-data` branch.

- **Unreviewed.** Every entry is a machine draft. None has been checked by a person.
- **Not for drafters.** If you are drafting an edition with the [replication kit](../../replication/README.md), do not open this folder until your edition is frozen. The kit's blindness rule covers every edition here.
- **Unedited copies.** Files inside an edition folder are copied unchanged from the edition's private repository (`nikbearbrown/irreducibly-human-work-lexicon-grok`, commit `64aa98f8440710c6543910c70acca37d7b5ffbd2`). Paths inside `RUN.md` and the tools refer to the drafter's own machine.

## Editions

| Folder | Model as recorded | Run mode | Date | Lexicon roster commit | Concepts | Input | Checker (`verify_drafts.py`) |
|---|---|---|---|---|---|---|---|
| [`grok-bot-20261122/lex-pilot-grok-bot-20261122/`](grok-bot-20261122/lex-pilot-grok-bot-20261122/) | Grok Bot (exact version not exposed) | Batched in one session (batches of 3–10), not a fresh context per concept; disclosed in its `RUN.md` | 2026-11-22 (EST) | `91312fec957388afe4d1dfbdb4aff2707588b9a1` (kit files at `9eba1b7d`), prompt gen-v2 | 36 / 36 pilot concepts, twice | Way B: the shared pilot bundles; ungrounded first, then grounded | 36/36 ungrounded, 36/36 grounded (one after its single retry) |
| [`grok-bot-20261122/full-run-grok-bot-20261122/`](grok-bot-20261122/full-run-grok-bot-20261122/) | Grok Bot (exact version not exposed) | Batched in one session (75 batches of 50), not a fresh context per concept; disclosed in its `RUN.md` | 2026-11-22 (EST) | `91312fec957388afe4d1dfbdb4aff2707588b9a1`, prompt gen-v2 | 3,718 / 3,718 (the roster minus the pilot) | No-source bundles (concept record plus 30 neighbors); every claim `model_knowledge` | 3,718/3,718 pass with `--ungrounded`, 0 fail |

## `grok-bot-20261122/`: files

| File | What it is |
|---|---|
| `README.md` | The edition repository's top-level README |
| `full-run-grok-bot-20261122/README.md`, `RUN.md` | What the full run is, how it was made, conventions and judgment calls |
| `full-run-grok-bot-20261122/drafts-full.jsonl` | All 3,718 drafts |
| `full-run-grok-bot-20261122/report-full.jsonl` | Checker result per concept |
| `full-run-grok-bot-20261122/entries-full.md` | Drafts rendered with the kit's `render_entries.py` |
| `full-run-grok-bot-20261122/manifest.json` | Progress record |
| `full-run-grok-bot-20261122/batches/b0001.txt`–`b0075.txt` | The drafter's compact per-batch drafting lines |
| `full-run-grok-bot-20261122/out/bundles-full.jsonl` | The input bundles (7.1 MB): concept record and neighbor names only. The `examples`, `wikipedia`, `wikidata` and `wordnet` fields are empty in all 3,718, so they hold no job-posting text and no personal data |
| `full-run-grok-bot-20261122/tools/` | Bundle builder, viewer, compiler, assembler, ship script |
| `lex-pilot-grok-bot-20261122/README.md`, `RUN.md` | Pilot description, counts, method and deviations |
| `lex-pilot-grok-bot-20261122/drafts-*.jsonl`, `report-*.jsonl`, `entries-*.md` | Pilot drafts, checker reports and rendered entries, grounded and ungrounded |

## Left out, and why

- **Pilot `work/` folder.** `work/view-ungrounded.txt` reproduces the pilot bundles' usage examples, which are job-posting snippets from Kaggle datasets. The folder is also excluded by this repository's `.gitignore`. The pilot drafts keep only `ex:` row pointers to those datasets, not the snippet text.
- **Pilot bundles.** The pilot was drafted from the shared bundles in `replication/bundles/`, so no separate bundle file exists in the edition.
- **`full-run-grok-bot-20261122/out/drafts/` and `out/build.log`.** Per-batch copies of the same drafts and reports that are assembled in `drafts-full.jsonl` and `report-full.jsonl`.
- **Claude Sonnet 5.5 edition.** It is not in this branch. A copy is on the separate `grok-lexicon-parallel-data` branch; whether it belongs here is the project owner's call.
- No keys, secrets or judging anonymisation files are included.

More editions can be added as sibling folders, with a row in the table above.
