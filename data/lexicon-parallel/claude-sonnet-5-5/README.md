# Claude Sonnet 5.5 edition

An unmodified copy of Claude Sonnet 5.5's independent Skills Lexicon / Irreducibly Human Work Lexicon edition, taken from the private source repository named below. The edition files themselves were not edited for this transfer. They live under [`edition/`](edition/), which is a verbatim copy of that repository (except `.git`).

| Field | Value |
|---|---|
| Model | Claude Sonnet 5.5 (model ID `claude-sonnet-5-5`; the edition's `RUN.md` notes that the model-picker label was pending confirmation) |
| Source repository | [nikbearbrown/skills-lexicon-claude-sonnet-5-5](https://github.com/nikbearbrown/skills-lexicon-claude-sonnet-5-5) (private) |
| Commit | [`9df2a7d7116da2e2955c6eb12f327f336ff56e94`](https://github.com/nikbearbrown/skills-lexicon-claude-sonnet-5-5/commit/9df2a7d7116da2e2955c6eb12f327f336ff56e94) (`main`) |
| Date | 21 November 2026, 4:58 PM EST (America/New_York); commit timestamp 2026-11-21 16:58:18 -0500 |
| Roster pin | `nikbearbrown/skills-lexicon` (now this paper repository) at `91312fec957388afe4d1dfbdb4aff2707588b9a1` |
| Method | Independent edition schema, not the replication-kit draft schema. Inventory taken from roster IDs, labels, kinds, classes and O\*NET identifiers only (source definitions were not read). 120 O\*NET 30.2 element definitions were copied verbatim (`basis: source`). The other 2,775 definitions were written from model knowledge in 13 compact draft batches and expanded by `tools/edition.py`. |
| Scope | 2,895 in-scope concepts drafted (1,988 skills, 67 abilities, 550 knowledge, 290 languages). 859 credential concepts and the 36-concept pilot were out of scope. |
| Grounded / ungrounded | Mixed: 120 sourced (O\*NET), 2,775 model knowledge |
| Checks | `python3 -I tools/edition.py validate --full` reported 0 warnings. This is the edition's own validator, not the kit's `verify_drafts.py`. |
| Human review | None. Every entry is a machine draft. |

This source repository is private. This copy lives in the public paper repository because the owner asked for the editions to be added here.

## What's in `edition/`

| File or folder | What it is |
|---|---|
| `edition/entries.jsonl` | One drafted entry per in-scope concept |
| `edition/inventory.jsonl` | Roster inventory used for the run |
| `edition/coverage.json`, `edition/manifest.json` | Counts, model label, pin, progress |
| `edition/entries.md` | Readable rendering of every entry |
| `edition/README.md`, `edition/RUN.md` | Edition documentation and run notes |
| `edition/THIRD-PARTY-NOTICES.md` | O\*NET 30.2 attribution (CC BY 4.0) |
| `edition/drafts/` | Compact draft batches that the build expands |
| `edition/data/` | Extracted O\*NET 30.2 elements, roster metadata, out-of-scope credential IDs |
| `edition/tools/` | `edition.py` and `build_inventory.py` |

No file was left out of the source repository except `.git`. No copied file is over 50 MB.
