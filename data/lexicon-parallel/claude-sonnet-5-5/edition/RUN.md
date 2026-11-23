# RUN.md: Claude Sonnet 5.5 edition

**Status: COMPLETE.** All 2,895 in-scope IDs have a distinct machine-drafted entry. Live counts are in `coverage.json`; every number below was computed from the files in this repository.

## Identity

| Field | Value |
|---|---|
| Authoring model | **Claude Sonnet 5.5** (`claude-sonnet-5-5`) |
| How the label was obtained | The session's system information names the model "Sonnet 5.5" with ID `claude-sonnet-5-5`, and the commit attribution line reads "Claude Sonnet 5.5". The model picker itself was not visible to the run, so the label is **pending the user's confirmation**. If the picker shows something else, every file here needs the same relabel. |
| Model changes during run | None observed |
| Harness | Claude desktop app, Code tab (Claude Code / Claude Agent SDK), macOS |
| Drafting delegated to another model or subagent | No. Every definition was written by this model in this session; no subagent or workflow was started. |
| Other models' work consulted | No. No other edition, draft, repository or Explorer folder was read, searched for or requested. |
| Run date | 2026-11-21, America/New_York (roster clone about 16:23, final validation about 16:57 EST) |

## Source and scope

- Roster: `https://github.com/nikbearbrown/skills-lexicon`, pinned at `91312fec957388afe4d1dfbdb4aff2707588b9a1` (2026-11-20 22:04:52 -0500, "Add Skills Lexicon research manuscript draft"). `origin/main` was at this same commit when cloned, so the pin and main did not differ; the roster was not changed afterwards.
- Recount from the pinned commit (3,754 entry files): skills 1,988, abilities 67, knowledge 550, languages 290 = **2,895 in scope**; 859 credentials out of scope. This matches the figures in the request. The 36-concept pilot is not part of the roster counts.
- Class comes from the source's `top_class` rule applied to `kind` (`credential` excluded; language kinds are `human-language` 158, `programming-language` 112, `markup-language` 10, `modeling-language` 7, `style-language` 3).
- One label occurs twice, "Mathematics" (a skill and a knowledge area). They stay separate by ID and each carries an `ambiguous_label` flag.

## Methods

1. Cloned the source into `input/skills-lexicon-source` (outside this repository) and checked out the pinned commit detached.
2. Read the README, CONTRIBUTING, `docs/ENTRY-FORMAT.md`, `docs/CLASSES.md`, `docs/SOURCES.md`, `skills/draft-entry/SKILL.md` and `THIRD-PARTY-NOTICES.md`.
3. `tools/build_inventory.py` read only `id`, `preferred_name`, `kind` and `identifiers` from each source entry. It does not read the source `definition`, `description`, `evidence`, `notes` or any model-review data, and none of those were opened by hand. Inventory order: abilities, languages, knowledge, then skills grouped by kind, each alphabetical.
4. **Sourced definitions (120).** Entries carrying an `onet-element` identifier (52 abilities, 35 skills, 33 knowledge areas) use O*NET 30.2's own definition text (CC BY 4.0) from the raw O*NET data files in the source checkout, with element ID, version, permalink to the file at the pinned commit, and license recorded. These are the only entries with `basis: source`.
5. **Drafted definitions (2,775).** Written from model knowledge in 13 compact batch files (`drafts/batch-001.txt` to `batch-013.txt`) and expanded by `tools/edition.py build`. Each draft line carries the concept's row number and exact canonical label, and the build refuses a line whose label does not match the inventory, so a drafting slip cannot attach text to the wrong ID. Definitions are one or two plain sentences in the work or learning sense; products and tools say what someone does with them.
6. Worked in batches; each completed batch was built, validated and committed (13 batch commits plus final packaging).
7. Variants and relations were added only where confident, always `model_knowledge`, always with canonical target IDs. Four variants shared by two concepts (API, NLP) are marked `ambiguous: true`.

## Results (from `coverage.json` and the files)

| Measure | Count |
|---|---:|
| In-scope IDs / entries / distinct definition texts | 2,895 / 2,895 / 2,895 |
| Drafted / pending | 2,895 / 0 |
| Skills / abilities / knowledge / languages | 1,988 / 67 / 550 / 290 |
| Definition basis `model_knowledge` / `source` | 2,775 / 120 |
| Entries with variants (variant records) | 312 (324) |
| Entries with relations (relation records) | 203 (207) |
| Entries with flags (flag records) | 80 (80) |
| Flag types | classification_dispute 20, sense_note 34, low_confidence 14, ambiguous_label 11, scope_note 1 |
| Out-of-scope credential IDs found in entries | 0 |

## Checks

`python3 -I tools/edition.py validate --full` independently verifies: every JSON/JSONL file parses; exactly one entry per roster ID; no entry ID outside the roster and none from the credential list; entry name, kind and class equal the inventory; model label and draft set on every entry; machine-drafted and not human-reviewed; definition basis, source records (source, version, identifier, permalink, license) and O*NET text equality against `data/onet-30.2-elements.json`; relation types, canonical target IDs, target labels, no self-relations and no `broader`/`part_of` cycles; flag shape; no two concepts sharing identical definition text; no shared variant unless marked ambiguous; `coverage.json` equal to counts recomputed from the files. `--full` also requires 2,895 entries, 0 pending and the expected per-class counts. It passes with 0 warnings.

A second check that does not import the tool re-derived the roster directly from the pinned source checkout and confirmed: 2,895 in-scope roster IDs equal the 2,895 entry IDs, 0 label/kind/class mismatches, 0 credential IDs, 0 invalid relation targets. The three O*NET source files resolve at the pinned commit through the GitHub contents API (blob SHAs `9aaeb51e`, `44bb9174`, `b12e1909`).

## Limits and review gaps

- Definitions are machine drafts from model knowledge, not human-reviewed and not checked against an outside source, except the 120 O*NET entries. Facts about vendors, versions, dates and product status for tools, platforms and legacy products can be stale or wrong and need review. The 14 `low_confidence` entries are the ones where identification itself is uncertain.
- The 15 non-O*NET abilities are dispositions or work styles more than abilities; each carries a `classification_dispute` flag. 20 `classification_dispute` flags in total mark entries I think belong in a different kind (standards or regulations filed as knowledge, product features, documents).
- O*NET text was copied from the source repository's data files, not re-fetched from onetcenter.org. The pointers resolve, but the text was not compared against a fresh O*NET download.
- Open English WordNet 2025 was not used: it is not in the local environment and downloading it was not authorized. No WordNet-sourced claim is made; human-language definitions are model knowledge, not sourced.
- Variants and relations are sparse by design and rest on model knowledge only. Absence of a variant or relation is not evidence that none exists.
- Job examples were not included (optional for this construction).
- The model-picker label is unconfirmed (see Identity).

## Delivery

- Private GitHub repository: `nikbearbrown/skills-lexicon-claude-sonnet-5-5` (private, created under the user's account; the source repository was never pushed to).
- Explorer cluster copy: see the final report for the verified status; if it says not verified, only the GitHub checkpoint exists.
