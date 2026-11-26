# Paper drafts: Irreducibly Human Work Lexicon: An Auditable Vocabulary for Matching Skills Across Job Postings and Curricula

**Rough drafts, not reviewed.** Written with Grok Bot on 2026-11-26 for Nik Bear Brown. No claim here has been checked by a reviewer, and no evaluation described here has been run.

**Where it stands:** Rough manuscript plus this series. No entry is independently reviewed. A checked Grok Bot edition (3,718/3,718 pass, no sources) sits alongside the Claude Sonnet 5.5 edition and the reference lexicon; the cross-model judge pilot is under way; the human evaluation and the held-out matching evaluation have not been run.

This folder sits beside the existing manuscript, [../irreducibly-human-work-lexicon-an-auditable-vocabulary-for-matching-skills-across-job-postings-and-curricula/](../irreducibly-human-work-lexicon-an-auditable-vocabulary-for-matching-skills-across-job-postings-and-curricula/README.md), which it builds on and does not replace. The manuscript stays the paper of record; the series adds the WordNet-style structure, the AI build process and the evaluation to-do.

> **Drafting an independent edition?** Don't read this folder. The papers quote examples from the Grok Bot edition, so reading them would break the blind protocol in the [replication kit](../../replication/README.md).

The drafts are modelled on the WordNet series (Miller et al., *Five Papers on WordNet*, 1990, revised 1993): an introduction, one paper per part of the vocabulary, a design and implementation paper, and appendices. Two things are added: the design paper documents an AI build (independent model editions, checking, provenance, the agreement method), and the evaluation is written as a to-do of what people must do after the AI comparison of the editions.

| File | What it is |
|---|---|
| [irreducibly-human-work-lexicon-paper-series.md](irreducibly-human-work-lexicon-paper-series.md) | this lexicon's paper series (Parts I to V and appendices) |
| [HUMAN-EVALUATION-TODO.md](HUMAN-EVALUATION-TODO.md) | the ordered human evaluation steps, shared across the five lexicons, plus this lexicon's queues, safety rule, held-out tasks and open decisions |
| [building-wordnet-style-lexica-with-ai.md](building-wordnet-style-lexica-with-ai.md) | the shared methods paper, *Building WordNet-style lexica with AI: process and provenance*, identical in all five lexicon repositories |
| [TEMPLATE.md](TEMPLATE.md) | the section template every series follows, identical in all five repositories |
| `*.docx` | Word copies, generated from the .md files |
| [tools/build_docx.py](tools/build_docx.py) | regenerates the .docx files |

## How to edit

1. Edit the `.md` files; they are the source. Don't edit the `.docx` files, which are overwritten.
2. Regenerate the Word copies: `pip install python-docx`, then from this folder run `python3 tools/build_docx.py` (or name the files to rebuild).
3. Keep the *Rough draft, not reviewed* line at the top until a reviewer has checked the paper.
4. Keep the headings in TEMPLATE.md order, so the five series stay parallel. If you change the shared methods paper, TEMPLATE.md or the shared part of the to-do, make the same change in the other four repositories.
5. Use only numbers you can trace to this repository, a run's RUN.md or report, or the agreement-method documents. Mark anything unknown `[TODO: …]` and any uncertain reference `[verify]`.
