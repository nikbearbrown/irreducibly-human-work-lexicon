# Replicating the Skills Lexicon drafting analysis

**Summary.** This folder has everything an agent needs to redo the Skills Lexicon entry-drafting analysis on its own, in parallel with other models, so the results can be compared side by side. Pick the way in below that fits what your agent can do, follow [INSTRUCTIONS.md](INSTRUCTIONS.md), and hand in one folder. Never look at another model's drafts, and never push your drafts to this repository.

The analysis: draft one WordNet-style entry for each of 36 lexicon concepts, twice. The grounded run gets the concept's source material (Wikipedia, Wikidata, WordNet, job-posting snippets). The ungrounded run gets the same material with Wikipedia, Wikidata and WordNet removed. Every claim in a draft must say whether a source states it or the model believes it, and the source claims are checked by script.

## Pick your way in

| Your agent can... | Way | What it does |
|---|---|---|
| run code and reach the internet | **A. Full replication** | Builds its own bundles with `scripts/assemble_bundles.py`, then drafts. |
| run code, but not fetch anything | **B. Drafting only** | Drafts from the shared pilot bundles in `bundles/pilot-36.jsonl`. |
| only chat (no code, no fetching) | **C. Hand-out messages** | Gets the 13 messages in `handout/`, one at a time. |

Ways B and C compare drafting alone, because every model gets the same inputs. Way A also tests how bundles get built.

## What's here

| Path | What it is |
|---|---|
| [INSTRUCTIONS.md](INSTRUCTIONS.md) | The task: the 36 concepts, the bundle contract, the posting allow-list, the drafting rules (word for word), the checks, the two runs, and what to hand in. |
| [GENERATION_GUIDE.md](GENERATION_GUIDE.md) | The original spec for the whole pipeline, including the cluster version. |
| `prompts/system.txt`, `prompts/user_template.txt` | The drafting instructions and the per-concept message, exactly as Claude got them. |
| `concepts/` | `pilot-36.tsv` (the comparison set), plus `batch_0002.tsv` to `batch_0005.tsv`, which together cover the rest of the lexicon (3,718 concepts) for a full-lexicon replication. |
| `kaggle-allowlist.tsv` | The only job-posting datasets allowed, with version and licence. |
| `bundles/pilot-36.jsonl` | The pilot's source bundles, built 2026-11-20 (ways B and C). |
| `handout/` | `00-ungrounded.md` (all 36 concepts) and `01-grounded.md` to `12-grounded.md`, each a complete message (way C). |
| `scripts/` | Bundle builder, drafter, checker and comparison tools (below). |
| `run_batch.sh` | Runs one concept list end to end with Claude Code. |
| [DATA-NOTICES.md](DATA-NOTICES.md) | Licences for the source material in `bundles/` and `handout/`. |

## Way A: build your own bundles

You need:

1. This repository at commit `91312fec`, the lexicon every model works from, for example `git worktree add ../lexicon-91312fec 91312fec`.
2. `observations.jsonl`, which lists the posting records that mention each concept. It is on the branch `data/kaggle-occurrence-evidence-20261030`, at `data/source-occurrences/kaggle-publication-2026-10-30/observations.jsonl`.
3. The allow-listed Kaggle datasets at the listed versions, each saved as `KAGGLE_DIR/<owner>/<dataset>/v<version>/dataset.zip`. If you can't get a listed version, say which one you used in RUN.md.
4. Open English WordNet 2025 (`english-wordnet-2025.xml.gz`), and a Python with the `wn` package.

Then:

```bash
LEXICON_REPO=../lexicon-91312fec KAGGLE_DIR=... OBSERVATIONS=... WORDNET_XML=... PYTHON=... \
  STEP=bundles replication/run_batch.sh replication/concepts/pilot-36.tsv work/pilot-36
```

Wikipedia and Wikidata come from their public APIs: Wikipedia at the revision current on 2026-10-01, Wikidata as it is today, with each item's revision id recorded. Responses are cached next to the output, so a rerun fetches nothing twice.

## Drafting (ways A and B)

**With any model:** render the exact messages, then send each one in a fresh conversation:

```bash
python3 replication/scripts/render_prompts.py work/pilot-36/bundles.jsonl prompts-grounded.jsonl
python3 replication/scripts/render_prompts.py work/pilot-36/bundles.jsonl prompts-ungrounded.jsonl --ungrounded
```

Each line holds `system` and `user`. Save each JSON reply on its own line with a `_meta` object (model, run, attempts). Then check the drafts and write them out for a person to read:

```bash
python3 replication/scripts/verify_drafts.py BUNDLES.jsonl drafts-grounded.jsonl report-grounded.jsonl
python3 replication/scripts/verify_drafts.py BUNDLES.jsonl drafts-ungrounded.jsonl report-ungrounded.jsonl --ungrounded
python3 replication/scripts/render_entries.py BUNDLES.jsonl drafts-grounded.jsonl report-grounded.jsonl entries-grounded.md
```

A failed draft gets one retry, sent with its list of errors (INSTRUCTIONS.md, section 6).

**With Claude Code:** `run_batch.sh` drafts with headless `claude -p` on your own Claude plan, not an API key, and does the checking for you. Use `STEP=drafts` to skip the bundle step, `RUN=ungrounded` for the second run, and `WORKERS` (default 2) for parallel calls. For way B, put `bundles/pilot-36.jsonl` in the work folder as `bundles.jsonl` first.

## Way C: hand-out messages

Send `handout/00-ungrounded.md` first, then `01-grounded.md` through `12-grounded.md` in order. Attach each file or paste it in. The ungrounded run goes first so the model hasn't seen any source text when it drafts without it. A fresh chat for each grounded message is best. Each message says what to send back: a file or a `jsonl` block of drafts, plus, after the last message, a short RUN.md note. Save the replies under the names the messages give.

To rebuild the messages from other bundles, run `python3 replication/scripts/make_handout.py BUNDLES.jsonl OUT_DIR`.

## Hand in

Hand in one folder, `lex-pilot-<model>-<YYYYMMDD>`, laid out as INSTRUCTIONS.md section 8 describes. Copy it to the Explorer cluster if you have access, or send it to Bear. Don't push it here. Drafts stay private until every model has handed in.

## Compare (once everyone has handed in)

```bash
python3 replication/scripts/compare_models.py comparison.md lex-pilot-<model-a>-<date> lex-pilot-<model-b>-<date> ...
python3 replication/scripts/collect_flags.py flags.csv WORK_DIR ...
```

`compare_models.py` writes one section per concept (each model's links, definition and relations side by side) and a summary table. `collect_flags.py` gathers every draft's flags into one sheet, sorted by kind.
