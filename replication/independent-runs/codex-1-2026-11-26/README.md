# Codex 1: independent lexicon construction

**In progress:** 50 of 3,718 non-pilot concepts drafted as of November 26, 2026. All 50 pass structural checks. The definitions are model-generated, ungrounded, and not independently fact-checked. No separate judge was used.

This run is independent of the other model editions: no other edition or its review was used for drafting. It reused the pinned canonical concept metadata as seeds. One chat retained context across five batches of ten, so this is **not** a fresh-context replication. Nothing here is part of the canonical lexicon under `entries/`.

- [Run record](RUN.md): pinned inputs, protocol deviations, source limitations, and progress.
- [Readable drafts](entries-ungrounded.md) and [machine-readable drafts](drafts-ungrounded.jsonl).
- [Structural verification report](report-ungrounded.jsonl), [input bundles](bundles.jsonl), and [full concept queue](queue.tsv).
- Numbered JSONL files preserve each batch's bundles, rendered prompts, outputs, and reports. The rendered prompts document the intended prompt fields; they are not separate model API transcripts.
- [Resume instructions and scripts](support/README.md).

If you are drafting a separate blind edition, do not use these outputs. Work from the pinned [replication kit](https://github.com/nikbearbrown/irreducibly-human-work-lexicon/tree/9e6fb2b4f125b22c45bc4d0ccd074e1c3189cfcf/replication) until your own handoff is complete.
