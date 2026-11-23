# Skills Lexicon: Claude Sonnet 5.5 edition

An independent, machine-drafted edition of 2,895 Skills Lexicon definitions written by **Claude Sonnet 5.5** (model ID `claude-sonnet-5-5`), so entries can be compared with other models' editions **by concept ID**. Repository slug: `skills-lexicon-claude-sonnet-5-5`.

**Every entry is a machine draft. None has been human-reviewed.**

## Scope

The roster is [nikbearbrown/skills-lexicon](https://github.com/nikbearbrown/skills-lexicon) pinned at commit `91312fec957388afe4d1dfbdb4aff2707588b9a1`. Counts below are recounted from that commit, not from the README.

| Class | Concepts | Kinds inside the class |
|---|---:|---|
| Skills | 1,988 | skill 723, tool 498, platform 219, method 219, library 129, standard 115, framework 85 |
| Abilities | 67 | ability 67 |
| Knowledge areas | 550 | knowledge 550 |
| Languages | 290 | human-language 158, programming-language 112, markup-language 10, modeling-language 7, style-language 3 |
| **Total** | **2,895** | |

Out of scope: the 859 credential concepts (their IDs are listed in `data/out-of-scope-credential-ids.txt` so the validator can prove none is drafted) and the old 36-concept pilot. One label, "Mathematics", appears twice (a skill and a knowledge area) and the two stay separate by ID.

## Files

| File | What it is |
|---|---|
| `inventory.jsonl` | One record per in-scope ID: `n`, `concept_id`, canonical `preferred_name`, `kind`, `class`, `status` (`drafted` or `pending`), O*NET `identifiers` where the roster has them |
| `entries.jsonl` | One entry per ID (see schema) |
| `coverage.json` | Total, drafted, pending, per-class and per-kind counts, basis counts |
| `entries.md` | Readable version of every entry |
| `manifest.json` | Model label and ID, pinned commit, scope, progress |
| `RUN.md` | Methods, dates, checks and limits of this run |
| `THIRD-PARTY-NOTICES.md` | O*NET 30.2 attribution (CC BY 4.0) |
| `data/` | Extracted O*NET 30.2 elements, roster metadata, out-of-scope credential IDs |
| `drafts/` | Compact hand-written draft batches that `tools/edition.py build` expands into `entries.jsonl` |
| `tools/` | `edition.py` (build, validate, show, markdown) and `build_inventory.py` |

## Entry schema

```json
{
  "concept_id": "canonical roster ID",
  "preferred_name": "canonical label from the roster",
  "kind": "canonical kind from the roster",
  "class": "skill | ability | knowledge | language (canonical, preserved for comparison)",
  "draft_set": "skills-lexicon-claude-sonnet-5-5",
  "model": "Claude Sonnet 5.5",
  "status": "machine-drafted",
  "human_reviewed": false,
  "definition": {
    "text": "one or two plain sentences in the work or learning sense",
    "basis": "model_knowledge | source",
    "sources": [{"source": "", "version": "", "identifier": "", "permalink": "", "license": "", "attribution": ""}]
  },
  "variants": [{"label": "", "basis": "model_knowledge", "ambiguous": true}],
  "relations": [{"type": "broader | part_of | related | contrast", "target": "canonical ID", "target_label": "", "basis": "model_knowledge"}],
  "flags": [{"type": "classification_dispute | sense_note | ambiguous_label | low_confidence | scope_note", "note": ""}]
}
```

## Conventions

- **Basis.** `source` is used only where a permitted source supports the exact claim: the 120 O*NET 30.2 elements (52 abilities, 35 skills, 33 knowledge areas) carry O*NET's own definition text verbatim, with element ID, version, permalink and license. Everything else is `model_knowledge` with an empty `sources` list. No WordNet, Wikipedia or ESCO text is used.
- **Distinguishing the classes.** An *ability* is an enduring attribute; a *skill* is a developed capacity (tools, platforms, libraries, frameworks and methods are written as what a person does with them); *knowledge* is an organized body of facts and principles; a *language* names a communication system whose use is graded by proficiency.
- **Variants and relations** are added only where I was confident from model knowledge, use canonical target IDs, and are marked `model_knowledge`. Roster candidates and legacy tags were not treated as evidence. Empty lists are normal. The optional `ambiguous: true` on a variant means the same abbreviation also belongs to another concept (API, NLP).
- **Status.** Complete: 2,895 of 2,895 drafted (2,775 `model_knowledge`, 120 O*NET `source`). Exact counts and the checks run are in `coverage.json` and `RUN.md`.
- **Flags** record a disputed classification, a label with more than one sense, a scope note, or low confidence. A `low_confidence` flag means the definition is deliberately minimal.
- Source definitions, source descriptions and prior model drafts in the roster repository were not read or used. Only IDs, labels, kinds, classes and O*NET identifiers were taken from it, plus the raw O*NET 30.2 data files.

## Reproduce

```bash
python3 -I tools/edition.py build          # drafts/*.txt + O*NET -> entries.jsonl, inventory.jsonl, coverage.json, manifest.json
python3 -I tools/edition.py validate --full
python3 -I tools/edition.py markdown       # entries.md
```

Licence: original material here is offered under the same MIT terms as the source repository; O*NET-derived text is CC BY 4.0 (see `THIRD-PARTY-NOTICES.md`).
