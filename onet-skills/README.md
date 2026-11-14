# O*NET skills

## Executive summary

**What it is.** O*NET's 35 skills, with their definitions, and O*NET's ratings of how much of each skill every occupation calls for, on the 0 to 7 level scale: 894 occupations × 35 skills = **31,290 rows**. It is the skills counterpart of `abilities/`, built the same way, and `onet-knowledge/` does the same for the 33 knowledge areas.

**In the lexicon.** Every skill here is an entry in `entries/`, kind `skill`, with its O*NET element id as an identifier and `matched_source` evidence naming O*NET. 34 are new entries, `proposed`, with O*NET's definition. One, Service Orientation, matched an existing entry (`service-orientation`), which kept its drafted definition and gained the identifier and the evidence.

**Release: O\*NET 30.2**, the release the abilities cite. O*NET 31.0 splits these 35 into Essential Skills (the 10 Basic Skills) and Transferable Skills (the 25 Cross-Functional Skills), with the same element ids and the same definitions (checked 2026-11-13).

**Read it correctly.** Each rating describes what an *occupation* demands, not what a person can do, and not an AI replacement probability.

**Licence.** O*NET data is CC BY 4.0. These files are modified (selected and reformatted). See [Attribution](#attribution).

## Files

| File | Rows | What it holds |
|---|---|---|
| `onet-skills.json` | 35 | Element id, name, definition, category (Basic Skills or Cross-Functional Skills) and subcategory (Content, Process, Social Skills, Complex Problem Solving Skills, Technical Skills, Systems Skills, Resource Management Skills). |
| `onet-skill-ratings-all-occupations.csv` | 31,290 | Level (`LV`) ratings, 894 occupations × 35 skills, the same 15 columns as `abilities/onet-ability-ratings-all-occupations.csv`. Occupation titles: join `soc_code` to `abilities/onet-occupations.csv`. |

The columns are described in [`abilities/README.md`](../abilities/README.md#columns). Two differences from that file: values are written as O*NET writes them (`4.62`, not `4.620`), and `category` and `subcategory` are O*NET's own group names, taken from `Content Model Reference.txt`.

Observed in this file: values 0.0 to 6.0; `n` is 8 and `domain_source` is `Analyst` in every row; `recommend_suppress` is `true` in 147 rows; `not_relevant` is `true` in 3,383; rating dates 06/2010 to 08/2025. The importance (`IM`) rows are in O*NET's `Skills.txt` and are not copied here, as for abilities.

## The 35 skills

| Group | Skills |
|---|---|
| Basic Skills, Content | Reading Comprehension, Active Listening, Writing, Speaking, Mathematics, Science |
| Basic Skills, Process | Critical Thinking, Active Learning, Learning Strategies, Monitoring |
| Cross-Functional, Social | Social Perceptiveness, Coordination, Persuasion, Negotiation, Instructing, Service Orientation |
| Cross-Functional, Complex Problem Solving | Complex Problem Solving |
| Cross-Functional, Technical | Operations Analysis, Technology Design, Equipment Selection, Installation, Programming, Operations Monitoring, Operation and Control, Equipment Maintenance, Troubleshooting, Repairing, Quality Control Analysis |
| Cross-Functional, Systems | Judgment and Decision Making, Systems Analysis, Systems Evaluation |
| Cross-Functional, Resource Management | Time Management, Management of Financial Resources, Management of Material Resources, Management of Personnel Resources |

## Found while importing

- **Mathematics is both a skill and a knowledge area in O*NET** (2.A.1.e and 2.C.4.a). The skill is a new entry, `mathematics-skill`; the knowledge area matched the existing `mathematics`. Both are named Mathematics and both are marked `name_ambiguous`.
- **`service-orientation` has a wrong-subject description.** Its definition and O*NET's are about helping people; its description, adapted from the Wikipedia article "Service-orientation", is about a software design paradigm. Nothing was removed; a person should decide.
- **Bare names match a lot of text.** Writing, Speaking, Science, Monitoring, Coordination, Installation, Programming and Repairing are matched as whole words, so "installation" in "installation of the HVAC unit" and "monitoring" in "monitoring software" both resolve to these skills. The entries are `proposed`, so they feed no published counts; whoever reviews them should decide whether each needs a context rule. No variants were added: O*NET lists none, and a variant needs a source.
- **No relations were added.** O*NET does not link a skill to the abilities or knowledge it draws on, and the lexicon adds a relation only with a source. Narrower entries that already exist (Price negotiation, Copier troubleshooting, Technical writing) are not linked to these.

## Where it came from

`Content Model Reference.txt` (SHA-256 `909f6ce0b4376227945dcc98101da909a0b516c9354afdc1a0a5143c5bffe810`) and `Skills.txt` (SHA-256 `d6832c9c195742524a9e48598d962140aaa499c2f78046d4be3af0b69f2686be`) from `db_30_2_text.zip` (SHA-256 `b5479271931796b838f7173dc0f673a9ec961b7833ac87168fd11e92e7453741`, the archive `abilities/README.md` cites), copied from `/projects/aiskunks/onet/30.2/` on the cluster on 2026-11-13. Written by `python3 -I scripts/import_onet_skills_knowledge.py extract <db_30_2_text>` and turned into entries by `... entries` (run `2026-11-13-onet-skills-knowledge-import`). Every CSV row was read back and compared with `Skills.txt`: 31,290 of 31,290 equal on every field.

| File | SHA-256 |
|---|---|
| `onet-skills.json` | `5d3acd84d74772969ad16505ab1f0b12adb7ba2ff4a4d457840406bd1ec21e89` |
| `onet-skill-ratings-all-occupations.csv` | `5b06981f2077fe1c2fcd033ce19941b14e52847cbdeebe8aa52dc735c9d68383` |

## Attribution

This folder includes information from the O\*NET 30.2 Database by the U.S. Department of Labor, Employment and Training Administration (USDOL/ETA). Used under the CC BY 4.0 license. O\*NET® is a trademark of USDOL/ETA. Humanitarians AI has modified all or some of this information: it selected the level ratings, reformatted the data from tab-separated text to CSV and JSON, and added O*NET's group names to each row. USDOL/ETA has not approved, endorsed, or tested these modifications.

- O*NET database releases: https://www.onetcenter.org/db_releases.html
- Licence guidance and attribution wording: https://www.onetcenter.org/license_db.html
- Creative Commons Attribution 4.0 International: https://creativecommons.org/licenses/by/4.0/
