# RUN.md: lex-pilot-grok-bot-20261122

- **Model:** Grok Bot (the Grok agent in Professor Bear's Grok Bot workspace). No separate reasoning or effort setting is exposed; drafting was done by the agent itself, not through an API.
- **Prompt version:** gen-v2 (replication/INSTRUCTIONS.md section 5, as of lexicon commit `9eba1b7d`, 2026-11-22).
- **Way in:** B (drafting only), from the shared pilot bundles `replication/bundles/pilot-36.jsonl` (built 2026-11-20). `bundles.jsonl` is therefore left out of this folder.
- **Lexicon commit:** concept records as carried in the shared bundles (built from `91312fec`); kit files read at `9eba1b7d`.
- **Started:** 2026-11-22 18:19 EST (23:19 UTC). **Finished:** 2026-11-22 18:31 EST (23:31 UTC), approximately.

## Order of work

1. **Ungrounded run first.** Before opening any Wikipedia, Wikidata or WordNet text, I drafted all 36 entries from the concept record, the neighbors and the usage examples only. That run was committed on its own (first commit in this folder's history) before any source text was opened.
2. **Grounded run second**, from the full bundles.
3. Both runs checked with the kit's `scripts/verify_drafts.py`; grounded entries written out with `scripts/render_entries.py` (ungrounded also rendered, for convenience).

## Tools and data

- Kit scripts used unchanged: `verify_drafts.py`, `render_entries.py`.
- To read the bundles I printed a compact view of each one (Wikipedia: title, revision id and the first few hundred characters; Wikidata: candidate items with labels, descriptions, aliases and claims, plus ancestor labels; WordNet: synsets, lemmas, glosses and relation targets). When a claim needed more of an article, I searched that article's text in the bundle (for example the CCNA Security section of the Cisco certifications article). I did not read every article in full.
- Drafts were written by hand as small Python files (`work/src/`), one batch of concepts per file, using a tiny helper (`work/src/dsl.py`) that emits exactly the section 5 JSON shape.
- **Neighbors:** the bundles' own `neighbors` lists (way B); I did not choose them.
- No web or X search, no other model's drafts, no other AI.

## Differences from the page, with reasons

- **One session, not one fresh conversation per concept.** I drafted concepts in batches of three to ten within one session, so a concept's draft could be influenced by earlier drafts (for example, the same "Programming language" proposed hypernym appears across languages). The grounded run was drafted after the ungrounded run in the same session, so the grounded drafts are not blind to my own ungrounded drafts; they were re-drafted from the sources, not copied, but readers should treat the two runs as one drafter's work.
- **Retry:** one grounded draft (Extract, transform, load) failed the first check (a Wikipedia quote over 20 words) and was retried once with the quote shortened. Every other draft passed on the first attempt.
- **Post-check cosmetic edit:** I removed a leading "when" / "only when" / "only" from a few variant conditions, because `render_entries.py` already prefixes "only when". Both runs were re-verified afterwards (36/36 each). The `work/src/` scripts hold the pre-edit text.
- **Times** above are approximate; the box clock was read at start and end.

## What I could not get

- Explorer cluster access (not available from this box), so no way-A bundles and no copy to `/projects/aiskunks/skills-lexicon-work/lex-pilot/`.
