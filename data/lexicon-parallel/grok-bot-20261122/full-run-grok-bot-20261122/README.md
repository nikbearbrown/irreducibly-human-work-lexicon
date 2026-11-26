# Full run: Grok's independent lexicon drafts (all 3,718 concepts)

Grok Bot's complete parallel run of the Irreducibly Human Work Lexicon replication kit, drafted independently
(no other model's drafts were read). Run date: 2026-11-22 (America/New_York).

- **Input path:** no-source (ungrounded) bundles. No Explorer cluster was available, so each bundle is the
  concept record plus its 30 nearest neighbors at lexicon commit `91312fec`, built by `tools/build_bundles.py`
  with the kit's `assemble_bundles.py` neighbor logic. Sources are empty, all claims are `model_knowledge`,
  links are null. See `RUN.md`.
- **Prompt and schema:** kit prompt gen-v2 and its draft schema.
- **Checker:** kit `scripts/verify_drafts.py --ungrounded`, run on every batch.
- **Result:** 3,718 / 3,718 concepts drafted, 3,718 pass, 0 fail (every pass carries the expected
  "most claims rest on model knowledge" warning).

## Files

| File | What it is |
|---|---|
| `drafts-full.jsonl` | All 3,718 drafts, one JSON object per line |
| `report-full.jsonl` | Checker result per concept |
| `entries-full.md` | Drafts rendered with the kit's `render_entries.py` |
| `batches/b0001.txt`–`b0075.txt` | The compact drafting input, 50 concepts per batch (b0075 has 18) |
| `out/drafts/` | Per-batch compiled drafts and checker reports |
| `out/bundles-full.jsonl` | The ungrounded input bundles |
| `manifest.json` | Progress: done, failed, remaining |
| `tools/` | Bundle builder, batch viewer, compiler, assembler, ship script |

## Conventions and judgment calls

- Names that read as O*NET abilities, skills or knowledge areas carry the flag "The name reads as an O*NET
  ability/skill/knowledge area."
- Obsolete, retired, renamed or superseded products and credentials carry flags (for example "Obsolete.",
  "Retired.", "Replaced by CompTIA Tech+.", "Superseded by DoD 8140.").
- Typo, garbage or wrong variants were dropped (for example "Application Specific Integrated Curcuits",
  "International Computer Drivering License", "Software-Defined Networking Wide Area Network (SD-WAN)",
  "causal inference" on Causal reasoning, "(Programming Language)" suffixes). A bare ambiguous name is
  re-added as a conditioned variant where useful (for example "Apex" in a context about Salesforce).
- Contrast relations are used only for real look-alikes (UIkit vs UIKit, Master of Laws vs Large language
  models, Gulp.js vs Grunt.js).
- Ambiguous records are flagged rather than guessed (Gaelic, HP Brio vs Hyperion Brio, JAFAN).
