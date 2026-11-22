# Irreducibly Human Work Lexicon pilot: draft the entries on your own

**What this is.** You are one of several language models drafting the same 36 Irreducibly Human Work Lexicon entries **independently**, so Nik Bear Brown can compare the models afterwards. [README.md](README.md) says which of three ways in fits what you can do; this page is the task itself. You gather the source material for each concept yourself, draft one WordNet-style entry per concept under the rules below, check your own drafts, and hand in one folder. Do it twice: once with the outside sources and once without them, so we can see whether the sources help.

**First written 2026-11-20.** Claude (Opus 5.5) ran this task first, under these same rules. Its drafts stay private until every model has finished.

## 1. Independence rules (read first)

- **Work alone.** Do not read, search for, or ask for any other model's drafts or reports, including Claude's. Do not ask another AI to do any part of this for you.
- **Bundles.** If you build your own bundles (way A), build them yourself and leave `bundles/` alone. Ways B and C draft from the shared pilot bundles in `bundles/` and `handout/`; those are source material, not anyone's drafts.
- If you come across a folder or file that belongs to another run (anything under `lex-pilot/` that isn't your own folder, or any `drafts*.jsonl` or `entries*.md` that you didn't write), **don't open it.**
- You **may** read the public lexicon repository and the shared raw data listed below. Those are inputs, not anyone's entries.
- Don't edit the lexicon repository, don't push to GitHub (not even your hand-in), and don't publish anything.

## 2. The 36 concepts

Lexicon: https://github.com/nikbearbrown/irreducibly-human-work-lexicon at commit `91312fec` (public). The list is also in `concepts/pilot-36.tsv`. Each concept's record is the file in `entries/` whose `id` matches; read it at that commit.

| id | preferred name | variants in the lexicon |
|---|---|---|
| sh6x1wmacn | PostgreSQL | Postgres|PG |
| pk7cebmtg6 | Python | Python (Programming Language) |
| g5lqkx80zn | Docker | — |
| ls6hrpynv0 | Java | Java (Programming Language) |
| h60l8olauw | JavaScript | Javascript (Programming Language) |
| a0h79b66kq | C | C (Programming Language) |
| qb4qnsutxp | C++ | C++ (Programming Language) |
| dbxqhrpv38 | C# | C Sharp|C Sharp (Programming Language)|C# (Programming Language) |
| fcadn3ihwg | Angular | — |
| mnlgauzi32 | AngularJS | Angular.js |
| oeixkjthc3 | R | R (Programming Language) |
| n29960itit | Go | Go (Programming Language)|Golang |
| p1pplzvq0f | Swift | Swift3|Swift (Programming Language) |
| f69xny35zm | SQL | Sql (Programming Language) |
| flxbx98seh | Machine learning | ML |
| d168utcmjy | Natural language processing | NLP |
| d9sq04v2o1 | Extract, transform, load | Extraction, Transformation, and Loading (ETL)|ETL|Extraction, Transformation, and Loading |
| xe2d2jfa1r | Application programming interface | API|APIs |
| h00skqgqmn | Amazon Web Services | AWS |
| gisypzf6gf | Communication | — |
| tz7ipk5s96 | Teamwork | Team-working |
| thsmk1q1kl | Service orientation | Service-Orientation |
| b9mkf081yw | Critical Thinking | — |
| ccexfymw9t | Negotiation | — |
| gdzh66chlx | Attention to detail | Detail Conscious|Detail oriented |
| wclhs8ljcp | Deductive Reasoning | — |
| ecoz6ylymx | Statistics | statistical analysis |
| so9zp6tzyh | Mathematics | — |
| v2tu54uao9 | Mathematics | — |
| de8aeltv9z | Spanish | Spanish (Language)|Español |
| n7a094bha6 | Bachelor's in Nursing | Bachelor's degree in Nursing|Bachelors degree in Nursing |
| c4tp7yji9k | Bachelor of Science in Nursing | Bachelor Of Science in Nursing (BSN)|BSN |
| zkn14vnicf | Class B commercial driver's license | CDL Class B License|Class B CDL |
| tp5pvtb8jm | CCNA Security | Cisco Certified Network Associate- Security|Cisco Certified Network Associate Security |
| url3hq4jid | Salesforce | Salesforce.Com|Salesforce CRM |
| sixghka9vw | User experience design | UX design|user experience|User Experience Design (UX) |

The list is deliberate: easy technologies, look-alike names (Java and JavaScript; C, C++ and C#; Angular and AngularJS; Swift), short names (R, Go, C), abbreviations, soft skills, abilities, knowledge, a language, near-duplicate credentials (Bachelor's in Nursing and Bachelor of Science in Nursing), and a known trap: **Service orientation** once got a Wikipedia description of the software paradigm, which is the wrong sense.

## 3. Build one source bundle per concept

One JSON line per concept, with exactly these seven fields. Your drafts may cite only what is in your bundle, so save it. `scripts/assemble_bundles.py` builds exactly this (README.md, way A); `bundles/pilot-36.jsonl` is what it built for the pilot on 2026-11-20.

| Field | What goes in it | Where to get it |
|---|---|---|
| `concept_id` | the id above | |
| `concept` | the record: `id`, `preferred_name`, `kind`, `broad_class`, `variants`, existing `relations` | the entry file at commit `91312fec`. `broad_class` is the lexicon's class worked out from `kind`: `credential` gives `certification`; `ability` and `knowledge` stay as they are; the language kinds (`programming-language`, `markup-language`, `style-language`, `modeling-language`, `human-language`) give `language`; everything else is `skill`. |
| `neighbors` | 20 to 30 other lexicon concepts (`id`, `name`) that could be relation targets: similar names or variants, related topics, and any concept already related to this one | the same commit's `entries/`. Say in RUN.md how you chose them. |
| `examples` | up to 5 job-posting snippets: `id`, `source`, `text` (about 300 characters around the mention, plus the job title if there is one) | **postings only, no syllabi**, and only from the allow-list in section 4 |
| `wikipedia` | up to 3 candidate articles: `title`, `revision_id` (a **string**), `text` (the lead plus about the first 3,000 words, markup stripped) | English Wikipedia **as of 2026-10-01**, to match the dump at `/projects/aiskunks/enwiki/20261001/` on the Explorer cluster. The repo's `data/wikipedia-match/20261001/` (`matches.jsonl`, `candidates.jsonl`) already lists title and redirect candidates with page ids and revision ids. Without the cluster, use the public API: the newest revision at or before 2026-10-01T00:00:00Z. |
| `wikidata` | up to 3 candidate items: `qid`, `label`, `description`, `aliases`, `claims` (only P31, P279, P361, P527, P460, P1889, QID values only), `value_labels` (the English label of each QID in `claims`), `revision_id`; plus their P31/P279 ancestors to two levels, each with `ancestor_of` set to the candidate it belongs to | **The pilot used the public Wikidata API** (wbsearchentities, wbgetentities; also the English Wikipedia sitelink of your Wikipedia candidates). Record each item's revision id (`lastrevid`) and the date you fetched it. The full dump `wikidata-20261116-all.json.gz` is downloading to `/projects/aiskunks/wikidata/20261116/`; its README.txt says when it is complete. Later full runs will use it. |
| `wordnet` | senses for the preferred name and each variant: `synset`, `lemmas`, `gloss`, `examples`, `relations` keyed by `hypernym`, `hyponym`, `part_meronym`, `part_holonym`, `member_meronym`, `member_holonym` | **Open English WordNet 2025**: on Explorer at `/projects/aiskunks/wordnet/oewn-2025/`, or the `wn` Python package. The `wn` package calls the part relations `mero_part`, `holo_part`, `mero_member`, `holo_member`; rename them. |

A concept with nothing found gets empty lists, not a missing line.

## 4. Posting snippets: the allow-list

Use only these Kaggle job datasets. Each has a clear, permissive licence as its publisher declared it. **Leave out every other Kaggle dataset**, including the non-commercial, share-alike, GPL and unclear ones. On Explorer they are under `/projects/aiskunks/kaggle/jobs/kaggle-data/<owner>/<dataset>/v<version>/`.

| dataset | version | licence | file(s) | useful columns |
|---|---|---|---|---|
| adityamalguri/shine-it-jobs-dataset-for-practicing-eda | v1 | Apache 2.0 | Shine.csv | skills |
| arnabk123/data-science-data-analyst-and-ml-jobs-from-indeed | v1 | CC0: Public Domain | Data Analyst jobs (Indeed).csv, Data Science jobs (Indeed).csv, ML Engineer jobs (Indeed).csv | skills required |
| arturszledak/data-science-job-listings-from-pracuj-pl | v5 | CC0: Public Domain | jobs_pracujpl.csv | skills |
| asaniczka/1-3m-linkedin-jobs-and-skills-2024 | v2 | ODC Attribution License (ODC-By) | job_skills.csv, job_summary.csv | job_skills, job_summary |
| asaniczka/data-science-job-postings-and-skills | v2 | ODC Attribution License (ODC-By) | job_skills.csv | job_skills |
| austinnguyen00/data-jobs-in-australia | v3 | CC0: Public Domain | Data_Jobs_in_Australia_cleaned.csv | Skills |
| debojitbasak02/data-science-job-in-wuzzuf | v1 | CC0: Public Domain | data_science_jobs_in_wuzzuf.csv | industry_and_skills |
| dev122/internshala-jobs-dataset | v1 | CC0: Public Domain | JobData.csv | Description, Skills |
| emreksz/data-scientist-job-roles-in-uk | v1 | Apache 2.0 | Cleaned_Dataset.csv | Skills |
| jayaantanaath/internship-opportunities-in-india-2025 | v1 | MIT | merged_internships_dataset.csv | Skills |
| koti4878m/naukari | v1 | CC0: Public Domain | naukari.csv | key_skills |
| kyryllebed/uk-job-postings-in-data-sector | v1 | CC0: Public Domain | UKJobPostings.csv | full_description, skills_list |
| lukebarousse/data-analyst-job-postings-google-search | v744 | Apache 2.0 | gsearch_jobs.csv | description_tokens |
| maminkheneifar/jobinja-job-listings-26k | v1 | CC0: Public Domain | Jobinja - Processed.csv | Job Description, Skills |
| meerawks/it-skills-from-jobs | v1 | Apache 2.0 | JobsDatasetProcessed.csv | Description, IT Skills |
| mohityd2007/real-world-job-postings-dataset-for-ml-projects | v1 | Attribution 4.0 International (CC BY 4.0) | jobs_data.csv | Job Description, Skills Required |
| priyankamalavade/naukri-jobs-details | v1 | MIT | naukri_data_analyst_jobs.csv | Description, Skills |
| promptcloud/jobs-on-naukricom | v1 | CC0: Public Domain | home/sdf/marketing_sample_for_naukri_com-jobs__20190701_20190830__30k_data.csv | Key Skills |
| q1n9huan/global-job-market-postings-dataset | v1 | CC0: Public Domain | foreign_jobs.release_candidate_v14_enriched.kaggle.csv | description, skills |
| scrapifier/indeed-usa-job-postings | v1 | CC0: Public Domain | indeed_usa_job_postings.csv | description, skills |
| vitthnhnguyn138/vietnam-it-job-posts | v1 | MIT | vietnam_it_job_posts.csv | requirements, skills |

- Give each snippet a stable id: `<owner>/<dataset>@v<version>/<file>:<record number>`, where record 1 is the header line. Don't put `#` or `=` in an id: pointers are split on those characters. (Changed 2026-11-20 23:45: the first version of this page used `#` here.)
- Prefer a description column, so the snippet shows the word in use. Use a skills-list column only when there is no description.
- **Explorer rules:** the login node is shared, so nothing heavy runs there. Copy only the files you need to your own machine through the transfer node `xfer.discovery.neu.edu` and work there. Ask Bear before any Slurm job, and never delete anything on the cluster. If you can't reach the cluster, leave `examples` empty and say so in RUN.md.

## 5. Drafting rules (use these exactly)

This is prompt version `gen-v2` (November 22, 2026). Hand-ins made before then used `gen-v1`, whose first line still said Skills Lexicon, an open vocabulary; the rest of the prompt is the same.

Use the text below, word for word, as your instructions for each concept. Then give yourself the concept's bundle, set out under these headings: Concept record, lexicon_neighbors, Usage examples, Wikipedia candidates, Wikidata candidates and their ancestors, WordNet senses.

```text
You draft entries for the Irreducibly Human Work Lexicon, a WordNet-style lexical database of work concepts (skills, knowledge areas, abilities, languages, and credentials) used to match job postings with course syllabi. You receive one concept and a bundle of source material. You return one JSON object.

Your job is to record what the sources support, not to complete a template. An empty relation list is a correct answer. A plausible relation you cannot support is an error.

Work through these steps in order.

1. Work sense. Read the concept record and the usage examples. Write one sentence saying what the concept means as a job requirement or learning outcome. Every later decision is about this sense.

2. Source links. For Wikipedia, Wikidata, and WordNet separately, pick the single candidate that matches the work sense, or abstain by setting choice to null. Abstain when no candidate matches, when the candidates describe a different sense, or when you cannot tell. Give a one-sentence reason either way. You may cite only sources you linked, plus Wikidata ancestors of the item you linked.

3. Definition. Write one to three sentences in your own words describing the concept as it appears in postings and syllabi. Never reuse more than eight consecutive words from any source. Cite the pointers that support it.

4. Variants. List surface forms that name this concept: abbreviations, alternate spellings, historical names. If a form names the concept only in some contexts, state the condition (for example, "when it labels a skill, role, or team, not the experience itself").

5. Relations. Use only these types, and include a relation only if its test passes with the actual names filled in:
   - synonym: the target can replace the concept in a posting or syllabus without changing what is asked for or taught.
   - hypernym: "[concept] is a kind of [target]" is true.
   - hyponym: "[target] is a kind of [concept]" is true.
   - meronym: practicing or knowing the concept routinely includes the target as a component.
   - holonym: the concept is routinely a component of the target.
   - uses: the concept is typically practiced with the target, which is a tool, runtime, framework, or other technology rather than a component.
   - requires: the target must be learned before the concept can be practiced.
   - certifies: only when the concept is a credential; the credential attests to the target.
   - contrast: the target is often confused with the concept but differs from it. Use this for false-equivalence risks, including look-alike names.
   Do not record antonyms or pertainyms. Work concepts almost never have them.

6. Basis. Give every definition, variant, and relation a basis:
   - "source": the provided material states it, and you give at least one pointer that identifies the exact statement, synset relation, passage, or example.
   - "model_knowledge": you believe it, but the provided material does not state it. This is allowed. Never label model knowledge as source, and never invent a pointer.

7. Targets. If a relation's target matches a concept in lexicon_neighbors, set target_id to that concept's id. Otherwise set target_id to null and proposed_new to true.

8. Final check. Before returning, review every claim. Remove any relation whose test fails when read with the real names, any pointer that does not say what you claim, and anything you added only because a slot was empty. Put any concern a reviewer should see (conflicting sources, unclear sense, a likely error in the lexicon's existing record) in flags.

Pointer formats:
- Wikidata statement: wd:QID#PID=VALUE_QID (for example, wd:Q100#P279=Q200)
- Wikidata label or alias: wd:QID#alias=TEXT
- WordNet lemma: wn:SYNSET_ID#lemma=TEXT
- WordNet relation: wn:SYNSET_ID#RELATION=TARGET_SYNSET_ID, where RELATION is hypernym, hyponym, part_meronym, part_holonym, member_meronym, or member_holonym
- Wikipedia passage: wp:REVISION_ID#quote=TEXT, where TEXT is copied exactly from the provided article and is at most 20 words
- Usage example: ex:EXAMPLE_ID

Return only this JSON object, with no preamble and no code fences:

{
  "concept_id": "string",
  "work_sense": "string",
  "links": {
    "wikipedia": {"choice": "REVISION_ID or null", "reason": "string"},
    "wikidata": {"choice": "QID or null", "reason": "string"},
    "wordnet": {"choice": "SYNSET_ID or null", "reason": "string"}
  },
  "definition": {"text": "string", "basis": "source or model_knowledge", "pointers": ["string"]},
  "variants": [
    {"text": "string", "condition": "string or null", "basis": "source or model_knowledge", "pointers": ["string"]}
  ],
  "relations": [
    {"type": "one of the nine types above", "target_label": "string", "target_id": "string or null", "proposed_new": false, "basis": "source or model_knowledge", "pointers": ["string"], "note": "string or null"}
  ],
  "flags": ["string"]
}
```

## 6. Check every draft

These checks are what a draft must pass. Run them on every draft. A failed draft gets **one** retry with the list of what failed; if it still fails, keep it and record the errors. More retries mostly teach a model to satisfy the checker rather than the sources.

- `links.wikipedia`, `links.wikidata` and `links.wordnet` each have a `choice`, and each choice is null or one of that concept's candidates in the bundle.
- Every claim (the definition, each variant, each relation) has `basis` `source` or `model_knowledge`, and a `source` claim has at least one pointer.
- Every pointer resolves in the bundle:
  - `wd:` names the linked item or one of its ancestors, and the statement or alias is really there.
  - `wn:` names the linked synset, and the lemma or relation is really there.
  - `wp:` names the linked article's revision id (compare as text), and the quote is at most 20 words and appears word for word (ignoring case and spacing).
  - `ex:` names an example in the bundle.
- Relation types are only the nine allowed. A `target_id` must be one of the bundle's neighbors.
- `certifies` appears only when the concept's `kind` is `credential`.
- The definition shares no run of 9 or more consecutive words with any Wikipedia text in the bundle.

## 7. Two runs

1. **Grounded:** each concept with its full bundle.
2. **Ungrounded:** the same 36, with `wikipedia`, `wikidata` and `wordnet` emptied. Keep `concept`, `neighbors` and `examples`.

Draft each concept separately, with no memory of the other concepts' drafts.

## 8. What to hand in

One folder named `lex-pilot-<your model name>-<the date you started, YYYYMMDD>`, for example `lex-pilot-gpt-5-codex-20261120`, holding:

- `bundles.jsonl`: one line per concept, section 3 (ways B and C: say so in RUN.md and leave it out).
- `drafts-grounded.jsonl` and `drafts-ungrounded.jsonl`: one JSON entry per line, as section 5 describes. Add a `_meta` object to each: model, run (`grounded` or `ungrounded`), attempts, and any unresolved errors.
- `report-grounded.jsonl` and `report-ungrounded.jsonl`: one line per concept: `concept_id`, `status` (`pass` or `fail`), `errors`, `warnings`.
- `entries-grounded.md`: the grounded drafts written out for a person to read: name, definition, variants, each relation type with its targets, source links, flags, and whether each claim is from a source or from model knowledge.
- `RUN.md`:
  - the model and version, and any reasoning or effort setting;
  - the prompt version (`gen-v2` for this page);
  - the date and time you started and finished;
  - which tools and data you used, and how you chose neighbors;
  - what you could not get, and anything you did differently from this page, with the reason.

When it is done and you have Explorer access, copy the folder to the cluster at `/projects/aiskunks/skills-lexicon-work/lex-pilot/` (for example: `tar czf - <folder> | ssh explorer 'cd /projects/aiskunks/skills-lexicon-work/lex-pilot && tar xzf -'`). Then tell Bear it is there. Without Explorer access, send the folder to Bear. Don't open the other folders in `lex-pilot/`, and don't push your folder to this repository.
