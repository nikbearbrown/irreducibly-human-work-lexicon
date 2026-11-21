# Codex 1 independent Skills Lexicon run

Canonical input: nikbearbrown/skills-lexicon main, revision
`91312fec957388afe4d1dfbdb4aff2707588b9a1`. This is an independent comparison draft in its own repository folder,
not a canonical import. 2,895 concepts in the four named classes are in scope;
859 credential IDs are inventoried separately. Other branch and model outputs
are excluded. Canonical label, kind hint, stable ID, and O*NET code if any are
the only per-concept fields extracted into the drafting prompts.

- `inventory.json`: stable input IDs, including credentials outside the listed scope.
- `batches/` and `drafts/`: independent model inputs and outputs. No aliases or
  relationships are asserted in this pass. Unresolved definitions are null, not fabricated.
- `entries/`: one JSON packet per in-scope concept.
- `entries.csv`: spreadsheet view. See `SUMMARY.md` for counts.
- `entries.json` and `verification.json`: assembled checkpoint and coverage.
- `review-queue.json`: unresolved senses, repeated definitions, and other flags.
- `review/`: public source checks; even a source-supported draft is not human-reviewed.

`python3 -I inventory.py` regenerates the immutable inventory and packets.
`python3 -I language_sources.py` regenerates conservative catalog identity links.
`python3 -I assemble.py` validates and assembles the actual saved draft batches.
`--require-complete` rejects missing or unresolved entries or a missing official O*NET
reference. That check alone does not prove that the drafted definitions are correct.

### Source verification

[O*NET Content Model Reference](https://www.onetcenter.org/dictionary/30.2/text/content_model_reference.html), release 30.2, U.S. Department of Labor,
Employment and Training Administration, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). 120 exact name/code/kind
joins use the source definition verbatim, independently compared to the official
release file. The selection is reformatted, not endorsed by USDOL/ETA. These
records are source definitions, not model-authored definitions.

[Glottolog 5.3 CLDF](https://github.com/glottolog/glottolog-cldf/releases/tag/v5.3), Hammarström, Forkel, Haspelmath and Bank (2026), Max Planck Institute for Evolutionary Anthropology, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Versioned source links and
hashes are in `sources/human-language-links.json`. A unique exact language
label match adds catalog identity evidence only. It does not verify a draft's
geography, example, or semantics. Family/dialect collisions are candidates,
not asserted synonyms. Raw upstream data are kept in `sources/` for replay.

Every assembled packet includes `entry_text` for reading. Its kind separates a
draft/source definition, a suggested source-based definition awaiting scope
review, and disambiguation text. This does not silently convert unresolved
concepts into verified definitions. `--require-coverage` checks for every
expected packet, while `--require-complete` additionally rejects unresolved
drafts. Exact matches to O*NET Work Styles on inherited ability labels are
classification review flags, not automatic changes.
