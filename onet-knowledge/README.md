# O*NET knowledge

## Executive summary

**What it is.** O*NET's 33 knowledge areas, with their definitions, and O*NET's ratings of how much of each one every occupation calls for, on the 0 to 7 level scale: 894 occupations × 33 areas = **29,502 rows**. It is the knowledge counterpart of `abilities/` and `onet-skills/`, built the same way.

**In the lexicon.** Every area here is an entry in `entries/`, kind `knowledge`, with its O*NET element id as an identifier and `matched_source` evidence naming O*NET. 32 are new entries, `proposed`, with O*NET's definition. One, Mathematics, matched the existing `mathematics` entry, which kept its drafted definition and gained the identifier and the evidence.

**Release: O\*NET 30.2**, the release the abilities cite. O*NET 31.0 has the same 33 areas, element ids and definitions (checked 2026-11-13).

**Read it correctly.** Each rating describes what an *occupation* demands, not what a person knows. Unlike abilities and skills, most knowledge ratings come from job holders, not analysts (see below).

**Licence.** O*NET data is CC BY 4.0. These files are modified (selected and reformatted). See [Attribution](#attribution).

## Files

| File | Rows | What it holds |
|---|---|---|
| `onet-knowledge.json` | 33 | Element id, name, definition, and category: the O*NET group (Business and Management, Manufacturing and Production, Engineering and Technology, Mathematics and Science, Health Services, Arts and Humanities, Law and Public Safety, Communications). Education and Training and Transportation sit directly under Knowledge, so their category is null. `subcategory` is null for all 33. |
| `onet-knowledge-ratings-all-occupations.csv` | 29,502 | Level (`LV`) ratings, 894 occupations × 33 areas, the same 15 columns as `abilities/onet-ability-ratings-all-occupations.csv`. Occupation titles: join `soc_code` to `abilities/onet-occupations.csv`. |

The columns are described in [`abilities/README.md`](../abilities/README.md#columns). Differences from that file: values are written as O*NET writes them (`6.50`, not `6.500`); `category` is O*NET's own group name; and the raters are different:

- `domain_source`: `Incumbent` (job holders) in 22,044 rows, `Occupational Expert` in 6,930, `Analyst - Transition` in 528. Abilities and skills are rated by analysts.
- `n` varies by occupation (most often 20 to 22 raters), where abilities and skills always have 8.
- `recommend_suppress` is `true` in 4,860 rows, `false` in 17,679, and `n/a` in 6,963. `n/a` is O*NET's own value and is kept as written.
- `not_relevant` is `true` in 6,037 rows. Values run 0.0 to 6.96; rating dates 12/2004 to 08/2025.

The importance (`IM`) rows are in O*NET's `Knowledge.txt` and are not copied here, as for abilities.

## The 33 areas

| Group | Areas |
|---|---|
| Business and Management | Administration and Management, Administrative, Economics and Accounting, Sales and Marketing, Customer and Personal Service, Personnel and Human Resources |
| Manufacturing and Production | Production and Processing, Food Production |
| Engineering and Technology | Computers and Electronics, Engineering and Technology, Design, Building and Construction, Mechanical |
| Mathematics and Science | Mathematics, Physics, Chemistry, Biology, Psychology, Sociology and Anthropology, Geography |
| Health Services | Medicine and Dentistry, Therapy and Counseling |
| Arts and Humanities | English Language, Foreign Language, Fine Arts, History and Archeology, Philosophy and Theology |
| Law and Public Safety | Public Safety and Security, Law and Government |
| Communications | Telecommunications, Communications and Media |
| (directly under Knowledge) | Education and Training, Transportation |

## Found while importing

- **Mathematics is both a knowledge area and a skill in O*NET.** See `onet-skills/README.md`. Both entries are named Mathematics and marked `name_ambiguous`.
- **English Language and Foreign Language are knowledge here, not languages.** O*NET means knowledge of the structure and content of a language. The lexicon's `English` entry (a human language) is a different concept and is not linked to it.
- **Bare names match a lot of text.** Design, Mechanical, Administrative and Transportation are matched as whole words, so "mechanical engineer" and "administrative assistant" resolve to these areas. The entries are `proposed`, so they feed no published counts; whoever reviews them should decide whether each needs a context rule.
- **Many areas were missing.** Before this import the lexicon had no entry for Physics, Chemistry, Biology, Psychology, Law and Government or 26 of the other areas; it had degrees in some of them (PhD in Physics) as credentials. No `attests` link from those degrees to these areas was added (open item 5 in `docs/CLASSES.md`).

## Where it came from

`Content Model Reference.txt` (SHA-256 `909f6ce0b4376227945dcc98101da909a0b516c9354afdc1a0a5143c5bffe810`) and `Knowledge.txt` (SHA-256 `d9601dd763d5b3b203dd8827a3c2bd6c1b3d6155c1674168f0ef30b0e005cf07`) from `db_30_2_text.zip` (SHA-256 `b5479271931796b838f7173dc0f673a9ec961b7833ac87168fd11e92e7453741`, the archive `abilities/README.md` cites), copied from `/projects/aiskunks/onet/30.2/` on the cluster on 2026-11-13. Written by `python3 -I scripts/import_onet_skills_knowledge.py extract <db_30_2_text>` and turned into entries by `... entries` (run `2026-11-13-onet-skills-knowledge-import`). Every CSV row was read back and compared with `Knowledge.txt`: 29,502 of 29,502 equal on every field.

| File | SHA-256 |
|---|---|
| `onet-knowledge.json` | `cbb3de362bf0d9d081cc541bef2bffec266f87c6f6713e4b2545047aa2123036` |
| `onet-knowledge-ratings-all-occupations.csv` | `54688c5c7ab810f7862806f42bd4418d962d0a272b7e66fade3169817d792daf` |

## Attribution

This folder includes information from the O\*NET 30.2 Database by the U.S. Department of Labor, Employment and Training Administration (USDOL/ETA). Used under the CC BY 4.0 license. O\*NET® is a trademark of USDOL/ETA. Humanitarians AI has modified all or some of this information: it selected the level ratings, reformatted the data from tab-separated text to CSV and JSON, and added O*NET's group names to each row. USDOL/ETA has not approved, endorsed, or tested these modifications.

- O*NET database releases: https://www.onetcenter.org/db_releases.html
- Licence guidance and attribution wording: https://www.onetcenter.org/license_db.html
- Creative Commons Attribution 4.0 International: https://creativecommons.org/licenses/by/4.0/
