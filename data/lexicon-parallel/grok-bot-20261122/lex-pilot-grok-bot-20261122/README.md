# Grok's independent version: Irreducibly Human Work Lexicon pilot

Grok's own drafts of the 36-concept comparison set in the lexicon's replication kit
(`replication/` in nikbearbrown/irreducibly-human-work-lexicon), made independently so they can be
compared with the other models' versions. No other model's drafts were opened.

## What is here

| File | What it is |
|---|---|
| `drafts-ungrounded.jsonl` | 36 drafts from concept record, neighbors and usage examples only (drafted first). |
| `drafts-grounded.jsonl` | 36 drafts from the full shared bundles (Wikipedia, Wikidata, WordNet added). |
| `report-*.jsonl` | Output of the kit's `verify_drafts.py`: status, errors, warnings per concept. |
| `entries-grounded.md`, `entries-ungrounded.md` | The drafts written out for a person to read (`render_entries.py`). |
| `RUN.md` | Model, prompt version, timing, tools, and every departure from the instructions. |
| `work/` | Working files: the compact views and the batch scripts that produced the drafts. |

## Method

Prompt gen-v2, applied by Grok to each concept: work sense, source links (or abstain), a definition in
my own words, variants, relations from the nine allowed types, a basis on every claim, neighbor target
ids, final check. Way B of the kit: the shared pilot bundles, ungrounded run first and committed before
any source text was opened, then the grounded run. Every claim marked `source` carries a pointer the
kit's checker resolved.

## Coverage and counts

| | Ungrounded | Grounded |
|---|---|---|
| Concepts drafted | 36 / 36 | 36 / 36 |
| Passed `verify_drafts.py` | 36 | 36 (one after its single retry) |
| Claims (definition + variants + relations) | 272 | 321 |
| ...with basis `source` | 23 (usage examples only) | 173 |
| Relations | 133 | 162 |
| ...to proposed new concepts | 42 | 63 |
| Links chosen (WP / WD / WN) | 0 / 0 / 0 | 31 / 30 / 12 of 36 each |
| Reviewer flags | 40 | 51 |

Abstentions in the grounded run were deliberate: Service orientation (the only candidates are the
software paradigm, the kit's known trap), Attention to detail (only a company, album and TV episode),
Mathematics as a skill (the candidates are the field, which belongs to the knowledge record), and the
records with empty bundles (Bachelor's in Nursing, Class B CDL).

## Things a reviewer may want first

- PostgreSQL's existing `broader: SQL` relation reads as "PostgreSQL is a kind of SQL"; the sources call it a relational DBMS.
- Bachelor's in Nursing and Bachelor of Science in Nursing look like duplicates (the BSN article says the degree is also called a Bachelor of Nursing).
- The two Mathematics records (knowledge and skill) cannot be told apart by name.
- CCNA Security has been retired (model knowledge, flagged), and its prerequisite link to CCNP Security is historical.
- Look-alike traps recorded as `contrast`: Java/JavaScript, C/C++/C#, Angular/AngularJS, Swift/SWIFT network, AWS/American Welding Society, NLP/neuro-linguistic programming, Teamwork/Teamwork.com, Service orientation/service-oriented architecture.

Machine-drafted and unreviewed. Nothing here is marked reviewed.
