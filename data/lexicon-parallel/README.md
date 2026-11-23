# Parallel lexicon constructions

Independent machine-drafted editions of the Irreducibly Human Work Lexicon, copied here so they can be compared side by side. Each folder is one model's edition. The files inside an edition are an unmodified copy of that edition's outputs (drafts, checker reports, rendered entries, and run notes). Nothing in those copies was edited for this transfer.

**These copies make previously private drafts public.** This repository (`nikbearbrown/irreducibly-human-work-lexicon`) is public. The source edition repositories are private. They were added here at the repository owner's request. Every entry remains a machine draft; none is human-reviewed.

The kit in [`replication/`](../../replication/README.md) asked models not to push drafts here until every model had handed in. Other models may still be running. Treat this folder as a snapshot of the editions found on 23 November 2026, not as a complete comparison set.

## Editions in this folder

| Edition folder | Model | Source repository | Visibility | Commit | Date (America/New_York) | Method | Concepts | Grounded / ungrounded | Schema |
|---|---|---|---|---|---|---|---:|---|---|
| [grok-bot-20261122/](grok-bot-20261122/) (pilot) | Grok Bot | [nikbearbrown/irreducibly-human-work-lexicon-grok](https://github.com/nikbearbrown/irreducibly-human-work-lexicon-grok) | Private | [`64aa98f8440710c6543910c70acca37d7b5ffbd2`](https://github.com/nikbearbrown/irreducibly-human-work-lexicon-grok/commit/64aa98f8440710c6543910c70acca37d7b5ffbd2) | 22 Nov 2026, 9:03 PM EST | Replication kit, prompt gen-v2, way B: ungrounded first, then grounded | 36 / 36 | Both: ungrounded, then grounded | Kit draft schema |
| [grok-bot-20261122/](grok-bot-20261122/) (full run) | Grok Bot | same repo, same commit | Private | same | 22 Nov 2026, 9:03 PM EST | Replication kit, prompt gen-v2, no-source (ungrounded) bundles only | 3,718 / 3,718 | Ungrounded | Kit draft schema |
| [claude-sonnet-5-5/](claude-sonnet-5-5/) | Claude Sonnet 5.5 (`claude-sonnet-5-5`) | [nikbearbrown/skills-lexicon-claude-sonnet-5-5](https://github.com/nikbearbrown/skills-lexicon-claude-sonnet-5-5) | Private | [`9df2a7d7116da2e2955c6eb12f327f336ff56e94`](https://github.com/nikbearbrown/skills-lexicon-claude-sonnet-5-5/commit/9df2a7d7116da2e2955c6eb12f327f336ff56e94) | 21 Nov 2026, 4:58 PM EST | Independent edition schema; 120 O\*NET 30.2 definitions copied verbatim; remaining definitions from model knowledge. Credentials and the 36-concept pilot were out of scope. | 2,895 / 2,895 in-scope (859 credentials excluded) | Mixed: 120 sourced (O\*NET), 2,775 model knowledge | Edition's own schema (see `edition/README.md`) |

Both editions pin the lexicon roster at commit `91312fec957388afe4d1dfbdb4aff2707588b9a1`. Grok's full run covers 3,718 concepts (the roster minus the 36-concept pilot). Claude covers 2,895 concepts (the roster minus 859 credentials and the pilot). The two sets overlap, but they are not the same slice and they do not use the same entry schema, so they should not be line-compared as if they were kit-for-kit.

Grok's 36-concept pilot and 3,718-concept full run both passed the kit checker (`verify_drafts.py`): 36/36 ungrounded, 36/36 grounded, 3,718/3,718 ungrounded. Claude's edition is validated by its own `tools/edition.py validate --full`, not by the kit checker.

## What was not copied, and why

- **Working files and bundles.** Grok's `work/` folders, per-batch `out/drafts/`, `out/bundles-full.jsonl` (the ungrounded input bundles), `batches/*.txt` compact drafting inputs, and an empty `views/` directory were left in the source repository. They are working files, not the handed-in drafts.
- **No file in this copy is over 50 MB**, so none was compressed or stored with Git LFS. The largest file is Grok's `drafts-full.jsonl` (3.72 MiB).

## Looked for and not included

These are not parallel constructions of the lexicon (independent model drafts of entries) and were not copied here:

- No other edition repositories turned up in a search of all 756 repositories under `nikbearbrown` for names or descriptions containing `lexicon`, `skills-lexicon`, or `lex-pilot`. There is no Codex, Muse, Gemini, or GPT draft-edition repository.
- No `lex-pilot-*` folder exists on any branch of this repository.
- `review/codex-1` is an independent Codex 1 *review* corpus under `reviews/codex-1`, not a draft edition.
- `review/muse-spark-1.3-p001` holds Muse Spark 1.3 review answers to existing packets, not a draft edition.
- `audit/gpt-6-skill-p001-p005-20261029` holds GPT-6 audit packets, not a draft edition.
- `nikbearbrown/irreducibly-human-facets` is a different replication kit (coding job-posting lines against seven facets).

If another model's `lex-pilot-*` hand-in arrives later, it can be added as a sibling folder in this directory.
