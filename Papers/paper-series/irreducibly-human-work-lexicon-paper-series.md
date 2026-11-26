# Irreducibly Human Work Lexicon: An Auditable Vocabulary for Matching Skills Across Job Postings and Curricula

*Rough draft, not reviewed.* A paper series modelled on *Five Papers on WordNet*, building on the working manuscript v0.2 in `Papers/` of the repository (cited here as "the manuscript"), which it extends and does not replace. Nik Bear Brown and Humanitarians AI [TODO: confirm authorship]. Drafted 2026-11-26 with Grok Bot.

**Where it stands:** rough manuscript plus this series. The lexicon has 3,754 concepts; none is independently reviewed. Three editions exist for comparison: a checked Grok Bot edition (3,718 concepts, no sources, 3,718/3,718 pass, plus a 36-concept grounded and ungrounded pilot), a Claude Sonnet 5.5 edition (2,895 concepts) and the reference lexicon. Cross-model judging has begun as a pilot; the human evaluation and the held-out matching evaluation the manuscript proposes have not been run.

## Part I. Introduction to the Irreducibly Human Work Lexicon

### I.1 What the lexicon is for

"A job posting that asks for Postgres and a syllabus that names PostgreSQL can refer to the same technology" (the manuscript, abstract). Neither mention shows that a worker uses the tool or that a student is proficient in it. The lexicon's job is narrower and prior: to decide when two names stand for the same concept, when they name related concepts, and what evidence supports each decision, so that postings and curricula can be matched and the matching can be checked by someone other than its author. The name does not imply that the inventory measures which work cannot be automated (the manuscript, §1).

### I.2 Why a WordNet-style relational lexicon

Occupational and skills taxonomies such as O\*NET and ESCO supply reference concepts and structures (the manuscript, §2). What they do not give a matcher is the decision boundary: that *PG* names PostgreSQL only in a database context, that PostgreSQL rolls up to SQL without being a synonym of it, that Java and JavaScript are different things. WordNet's insight was that such boundaries are best expressed as relations between meanings, each with a plain test (Miller et al. 1990/1993). The lexicon applies that idea to the vocabulary of work, and adds what WordNet did not need: evidence attached to each individual claim.

### I.3 The lexical matrix, adapted

Rows are canonical concepts with stable IDs; columns are surface forms. The manuscript's PostgreSQL record shows the adaptation: *Postgres* is a case-insensitive word match, while *PG* is case-sensitive and carries the context condition "database". A form can thus sit in a cell only under a condition, which a printed matrix cannot express. Polysemy appears in the trap set: *Service orientation* is an occupational ability (helping people) in O\*NET and a software-architecture concept on Wikipedia, and the manuscript documents a record whose evidence matched the wrong one.

### I.4 The relations

| Relation | Test the drafter must pass with the real names filled in | WordNet analogue |
|---|---|---|
| synonym | the target can replace the concept in a source excerpt without changing the concept | membership in one synset |
| hypernym | "[concept] is a kind of [target]" is true | hypernymy (@) |
| hyponym | "[target] is a kind of [concept]" is true | hyponymy (~) |
| meronym | the concept includes the target as a component by definition | part meronymy (%p) |
| holonym | the concept is a component of the target by definition | part holonymy (#p) |
| uses | the concept is characteristically associated with the target tool, material or substance | none (new) |
| requires | an explicit conceptual prerequisite supported by a source | none; compare verb entailment |
| certifies | the concept is a credential and attests to the target | none (new) |
| contrast | the target is often confused with the concept but differs from it, including look-alike names | none; replaces antonymy |

Antonyms and pertainyms are not recorded. Every relation also carries a `basis` (`source`, with pointers, or `model_knowledge`, with none) and a target that is either a seed ID or marked `proposed_new`.

This is the one lexicon that uses **certifies**: a credential attests to a skill or knowledge area. In the Grok Bot full run, the relations are hypernym (716 edges), contrast (701), certifies (347), uses (253), holonym (147), hyponym (109), meronym (21), synonym (18) and requires (12) [counted from `drafts-full.jsonl` on 2026-11-26]. Separately, the reference lexicon's relations can carry `rolls_up`, an explicit decision that an occurrence of one concept counts toward another (PostgreSQL toward SQL); the manuscript stresses that roll-up is not synonymy.

### I.5 Built with AI: what changes and what does not

Most of the reference lexicon's entries were drafted by a model (3,552 of 3,754 by Claude Sonnet 5.5 on 2026-10-29; the rest imported from O\*NET and jobs.humanitarians.ai). The manuscript's audit found that 1,455 of 17,229 assertion fields (8.45%) had qualifying source backing and that no entry was independently reviewed. This series adds what has happened since: independent model editions drafted blind from the replication kit, and a method for measuring how far they agree in meaning before people review them.

## Part II. The vocabulary by category

The manuscript counts five broad classes at its audit pin (`3cd82a45`): 1,988 skills (of which 723 have the narrower developed-skill kind; the rest are technologies, methods, standards and so on), 550 knowledge concepts, 67 abilities, 290 languages and 859 credentials. The kinds of the 3,718 concepts in the Grok Bot full run, read from the entry files on main, are: credential 855, skill 716, knowledge 547, tool 497, method 216, platform 216, human language 157, library 129, standard 115, programming language 102, framework 83, ability 65, markup language 10, modelling language 7, style language 3. The five papers below follow the broad classes, as the WordNet series followed parts of speech.

### II.1 Skills, tools and methods

The broad skill class is the largest and least uniform. Developed skills (*Battle management*) sit beside tools, platforms, libraries, frameworks, standards and programming languages. The hypernym carries the taxonomy, and `uses` links technologies: *CoffeeScript* is drafted as a kind of programming language that uses JavaScript and contrasts with TypeScript. Contrast is as frequent as the hypernym in this edition, and not all of it is useful: *Battle management* contrasted with *Talent management* records a shared word, not a real risk of confusion. That is the kind of edge the agreement study and human review are meant to find.

### II.2 Knowledge

Knowledge areas (*Real estate*) are broad and overlap. Hyponyms and holonyms matter here: *Real estate contracts* is drafted as a hyponym of *Real estate*, and *Real estate owned* as a contrast. Many knowledge records mirror O\*NET knowledge areas, which raises the question of whether a generic record named like an O\*NET area is the O\*NET concept or something broader.

### II.3 Abilities

Abilities are few (65 in the full run) and come from O\*NET. Their structure is mostly contrast between near neighbours: *Oral Comprehension* contrasts with *Oral Expression* and *Written Comprehension*. These are the closest analogue in the lexicon to WordNet's adjective clusters, where meaning is defined by position among neighbours rather than by a hypernym.

### II.4 Languages

Human languages and computer languages share a class. Human languages are organised by family (*Nepali* is drafted as a kind of Indo-Aryan language, contrasting with *Bengali*). Computer languages bring the hardest look-alike problems in the lexicon: Java and JavaScript; C, C++ and C#; R, Go and C as short names; Angular and AngularJS; Swift. These make up most of the agreement study's trap set.

### II.5 Credentials

Credentials are the only class with the `certifies` relation. *Series 7 General Securities Representative* certifies securities sales, is a kind of securities licence, and contrasts with the Series 6 and Series 79 licences. The class matters for the agreement study because the Claude Sonnet 5.5 edition did not cover credentials: 855 credential records have only the Grok Bot draft, so their agreement cannot be measured until another edition covers them.

## Part III. Design and implementation

### III.1 Seed list and manifest

The roster is the lexicon itself at commit `91312fec` (3,754 concepts): 36 pilot concepts in `replication/concepts/pilot-36.tsv` and 3,718 in `batch_0002.tsv` to `batch_0005.tsv`. Unlike the other four lexicons, there is no `source-manifest.json` hash for the roster. [TODO: the parallel-edition prompt uses a SHA-256 computed over the four batch files joined (369d34c9…); commit a manifest.]

### III.2 Evidence bundles

The kit supports two input paths. Way A builds bundles from a Wikipedia dump, Kaggle copies of postings, `observations.jsonl` and the Wikipedia and Wikidata APIs. The Grok Bot pilot drafted the 36 concepts both grounded and ungrounded. The full run used **no-source bundles**: concept record, existing variants and relations, and 30 neighbours from the kit's `neighbors()`, with `examples`, `wikipedia`, `wikidata` and `wordnet` empty, so every claim is `model_knowledge`. RUN.md gives the reasons: grounded drafting would have meant reading about 140 MB of source text, and the allow-listed Kaggle datasets need a login the box did not have. The bundles showed the lexicon's existing variants and relations but not its definitions.

### III.3 Drafting prompt and kit

Prompt gen-v2 in `replication/prompts/`. The kit (`replication/INSTRUCTIONS.md`, `GENERATION_GUIDE.md`) is the original from which the other four lexicons' kits were adapted.

### III.4 Flags

Free-text flags; 314 records in the full run carry at least one [counted from `drafts-full.jsonl`]. The kit's flag collection is `scripts/collect_flags.py`.

### III.5 Checking

`verify_drafts.py --ungrounded` on each batch; 3,718 of 3,718 pass, each with the warning "most claims rest on model knowledge", as expected for an ungrounded run.

### III.6 Provenance

Hand-in folders `lex-pilot-grok-bot-20261122` and `full-run-grok-bot-20261122`, each with RUN.md; batch sources in `batches/`. Copies of both editions are on the branch `grok-lexicon-parallel-data` under `data/lexicon-parallel/`.

### III.7 The Grok Bot edition: what was done and how it deviated

Started on 2026-11-22 at about 8:15 PM EST, after Professor Bear asked for "a complete parallel run". Grok Bot read compact views of 50 bundles at a time and wrote one line per concept (work sense, definition, relations, extras), which a script compiled into gen-v2 JSON. No fresh context per concept; no other model's drafts opened; no web search. A target in the lexicon but outside a bundle's 30 neighbours was recorded as `proposed_new` with a note naming the lexicon ID.

### III.8 Parallel editions and agreement

This is the lexicon where the agreement method was designed (`AGREEMENT-METHOD.md` on `grok-agreement-method`, now at commit `78f889a2`, with one generic judge prompt, versioned judge IDs and self-exclusion through `drafters.tsv`). First deterministic numbers, on exact matching only (a lower bound on agreement in meaning):

| Pair | Shared | Relation F1, target | Variant F1, exact | Conditional flag agrees |
|---|---:|---|---|---|
| Grok × Sonnet | 2,895 | 0.055 [0.044, 0.066] | 0.111 [0.098, 0.125] | 0.85 (n = 222) |
| Grok × reference | 3,754 | 0.107 [0.095, 0.119] | 0.963 [0.956, 0.970] | 0.98 (n = 2,851) |
| Sonnet × reference | 2,895 | 0.066 [0.046, 0.088] | 0.106 [0.093, 0.119] | 0.99 (n = 206) |

The high Grok × reference variant figure is the copy-through effect: the bundles showed the lexicon's existing variants. The editions differ most in how much they say: Sonnet gives relations for 7% of shared concepts and Grok for 45%. In the first judge pilot, Fable 5.2 found 43 of 50 items equivalent and Muse Spark 1.3 39 of 50; on the 14 items both judged they agreed on 12. Two batches per judge remain (50 and 44).

### III.9 Human in the loop

The repository's policy: only reviewed entries should feed published estimates of skill mentions (the manuscript, §6), and an entry is `reviewed` only with a named reviewer, qualifying backing and no unresolved contradiction (§3.2).

## Part IV. Evaluation (to do): what humans do after the AI comparison

### IV.1 Status

The AI comparison is in its pilot. No human judging, claim verification or held-out evaluation has been run.

### IV.2 Prerequisites on the AI side

Finish the remaining judge batches; rewrite the family-balancing section for an open panel and code the family-weighted label, leave-one-judge-out and the self-preference probe; run the leak check; recompute `stats`. See [HUMAN-EVALUATION-TODO.md](HUMAN-EVALUATION-TODO.md), Part 1.

### IV.3 Human steps in order

The steps below are the same for every lexicon and are written out once, with owners and checkboxes, in [HUMAN-EVALUATION-TODO.md](HUMAN-EVALUATION-TODO.md). They run **after** the AI side has produced its blinded, pairwise comparison of the independent editions. Every step is a human step. None has started.

| # | Human step | What it produces | Gate before the next step | Owner | Status |
|---|---|---|---|---|---|
| H1 | Settle the open decisions (IV.6): judge invitations, `drafters.tsv` rows, trap list, worked examples, weights, acceptance threshold | a committed decision record | Bear signs off | Bear | not started |
| H2 | Recruit and register human judges (`agreement.py register`) | registry rows, seeded samples | at least 2 judges for the pilot; about 10 for full scale | Bear | not started |
| H3 | Pilot: Bear and at least one other judge label the whole pilot pool; tune the rubric on the development half only; freeze the prompts (`agree-v1`) and tag the analysis plan | adjudicated pilot labels, frozen rubric | rubric frozen and tagged | Bear + 1 judge | not started |
| H4 | Human–human overlap pool: about 30% of each judge's items come from a shared pool of about 50, each item judged by at least 2 people | the **human ceiling** (Krippendorff's α, pairwise κ, before adjudication) | ceiling reported per field | human judges | not started |
| H5 | Calibrate the AI judges against people: judge–human κ per field, for the panel, for the outside-family judge alone and for each judge | acceptance per field | κ ≥ 0.6 **and** no more than 0.1 below human–human; otherwise revise the rubric on the development split only and redraw the validation sample | Bear | not started |
| H6 | Targeted review queues (IV.4): disagreements, `FAMILY_SPLIT`, low agreement, flagged records, redirects, Wikidata errors, consensus gaps | a human label for each queued item | every queued item labelled or marked `UNSURE` with a note | human judges | not started |
| H7 | Random audit of agreed items: a seeded sample of items every model agreed on | the false-agreement rate | reported with an interval | human judges | not started |
| H8 | Adjudicate: majority of human judges, ties to Bear, judges' own words kept in `notes` | one adjudicated label per reviewed item | no open ties | Bear | not started |
| H9 | Verify claims (correctness, not agreement): for every claim kept, a reviewer opens the cited source and marks `supports`, `contradicts` or `unsure`; claims with only `model_knowledge` basis are sourced or withheld | per-claim decisions | no kept claim without a named check | reviewers | not started |
| H10 | Domain-safety review against the lexicon's rule (IV.4) | a pass or a list of removals | zero open safety items | Bear or a named domain reviewer | not started |
| H11 | Scope, duplicate and redirect decisions, with a crosswalk to the original seed IDs | decision list and crosswalk | every flagged seed decided | Bear | not started |
| H12 | Accept or reject merged entries into the reviewed edition (`lexicon/entries.jsonl`), with per-claim decisions, contributing run IDs and a named reviewer | the first reviewed entries | each accepted entry has a named reviewer and no unresolved contradiction | Bear | not started |
| H13 | Held-out task and coverage evaluations (IV.5) | task scores with intervals | analysis plan fixed before annotation | Bear + raters | not started |
| H14 | Write up: human ceiling, judge–human agreement, false-agreement rate, safety outcome, accepted-entry counts | the evaluation section of this paper | Bear approves | Bear | not started |

Agreement between models is not evidence that an entry is right. Steps H9 to H12 exist because two models can agree on the same mistake.

### IV.4 What humans review in this lexicon

Editions available today: **three**, on a roster of 3,754 concepts pinned at `91312fec`: Grok Bot (a 36-concept pilot, grounded and ungrounded, and a 3,718-concept full run, ungrounded); Claude Sonnet 5.5 (2,895 concepts, its own schema); and the reference lexicon (3,754 entries, 3,552 drafted by Claude Sonnet 5.5, the rest imported). They share 2,895 concepts. This is the only lexicon where the AI comparison has started: two model judges have labelled pilot batches (Fable 5.2: 43 of 50 items `EQUIVALENT`; Muse Spark 1.3: 39 of 50; on the 14 items both judged they agreed on 12), with two batches each still pending.

| Queue | Source | Size | What the human decides |
|---|---|---:|---|
| Definition pairs not `EQUIVALENT` | judge results | [TODO: after the remaining batches] | the label; whether the disagreement is about meaning or verbosity |
| `FAMILY_SPLIT` and `cross_sense` | panel aggregation, sense gate | [TODO] | which sense; which label |
| Trap set | `TRAP_IDS` | the look-alikes: Java and JavaScript; C, C++ and C#; Angular and AngularJS; Swift; R, Go and C; Service orientation; the two nursing degrees; the two Mathematics records | sense and contrast |
| Credentials with one edition only | coverage | 855 (Grok only) | reviewed against sources, or held until a second edition covers credentials |
| Copy-through | variants already in the reference | Grok × reference variant F1 0.963 | discount; review variants only where an edition departs from the reference |
| Known wrong-sense evidence | manuscript §4 | Service orientation | confirm the definition, withdraw the software-architecture description |
| Grok records with flags | `drafts-full.jsonl` | 314 [counted on 2026-11-26] | read |
| Relation sets | set F1 after alignment | [TODO] | spurious `contrast` edges (for example *Battle management* contrasted with *Talent management*) and reversed hypernyms |

**Privacy review (H10).** IHWL has no hazard rule like the medical lexicons. Its rule is privacy and attribution: no identifiable postings or personal data, O*NET and Wikipedia material kept under their licences, and no claim that the inventory measures which work cannot be automated (manuscript §1).

### IV.5 Held-out task and coverage evaluations

These are the manuscript's proposed evaluations (§5), unchanged:

- **Matching: when does context help?** Held-out, reusable job and course excerpts; two raters masked to system output mark spans, concepts, unresolved ambiguity and out-of-inventory status; an exact-form baseline against context-aware matching; span-plus-ID precision and recall, ID accuracy given a gold span, correct abstention, error against linked fraction, document-family clustered intervals.
- **Review: when does provenance help?** A counterbalanced reviewer exercise with and without the field-level trail, measuring agreement with adjudicated dispositions, time per item and recall for claims needing correction.
- **Coverage.** Against ESCO skills and O*NET (abilities, skills, knowledge), reported by broad class. Status: not designed.

### IV.6 Open decisions

- The seven "Decisions for Bear" in `AGREEMENT-METHOD.md` §12 (grok-agreement-method, 78f889a2): invitations and `drafters.tsv`; human judges; weights and threshold; whether Sonnet and later models also run gen-v2; whether the reference counts as an edition in α; scheduling; batch size.
- The family-balancing section still assumes the earlier fixed panel (three Claude judges plus Codex) and must be rewritten now that any model can join; the family-weighted panel label, leave-one-judge-out and the self-preference test are not yet in the code.
- Whether the remaining judge batches (50 and 44) finish before rescoring.

### IV.7 Resources, owners and status

About 10 human judges at about 100 items each (3 to 5 hours per judge); the pilot pool of 32 shared concepts (96 definition pairs plus other fields), labelled by Bear and at least one other judge; two masked raters for the matching evaluation; reviewers for the provenance study. Tools: `agreement.py register`, `validate`, `stats`; `HUMAN-JUDGE-INSTRUCTIONS.md`; `INTERVIEWER-PROTOCOL.md`. Owner: Bear unless delegated. Status: not started.

## Part V. Limitations

The manuscript's limitations stand: the inventories and drafting methods are not a probability sample of work; source links give traceability, not correctness. To them this series adds: the Grok Bot full run is ungrounded; the Sonnet edition uses its own schema, so links, work senses, conditions and fine relation types can be compared for Grok alone; credentials have one edition; and the reference lexicon was mostly drafted by the same model as one edition, so Sonnet × reference partly measures Sonnet agreeing with itself.

## Appendix A. File formats

**Roster**: `replication/concepts/*.tsv`, one concept per line: ID, preferred name, variants separated by `|`. **Entries** in the reference lexicon: `entries/<slug>.json` with `id`, `preferred_name`, `kind`, `definition`, `variants`, `relations`, `status`, `provenance`, `evidence` (see `docs/ENTRY-FORMAT.md` and `schemas/`).

**Evidence bundle** (`bundles.jsonl`, one JSON object per seed, exactly seven top-level fields):

| Field | Content |
|---|---|
| `concept_id` | the seed ID, unchanged |
| `concept` | `id`, `preferred_name`, `kind` and `broad_class` (`unclassified` until supported), `variants` and `relations` (start empty) |
| `neighbors` | candidate relation targets, taken only from the seed list, each `{id, name}` |
| `examples` | optional public terminology excerpts `{id, source URL, text}` |
| `wikipedia` | up to three `{title, revision_id, text}`; the revision is pinned |
| `wikidata` | candidate items `{qid, label, aliases, claims, revision_id}` and ancestors marked `ancestor_of` |
| `wordnet` | matching senses `{synset, lemmas, gloss, relations}` |

**Draft** (`drafts.jsonl`, one JSON object per seed, prompt gen-v2):

| Field | Content |
|---|---|
| `concept_id` | the seed ID |
| `work_sense` | one sentence fixing the sense every later decision is about (the name is kept from the first lexicon for schema compatibility) |
| `links.{wikipedia,wikidata,wordnet}` | `{choice, reason}`; `choice` is a revision ID, QID or synset ID, or `null` to abstain |
| `definition` | `{text, basis, pointers}`; one to three sentences, never more than eight consecutive words from a source |
| `variants[]` | `{text, condition, basis, pointers}`; `condition` says when the form names the concept |
| `relations[]` | `{type, target_label, target_id, proposed_new, basis, pointers, note}` |
| `flags[]` | strings, each a prefix and a reason (Appendix B) |
| `_meta` | added after drafting: model and version (or `unknown`), run mode, attempt count, and for retries the errors that triggered them |

**Pointer forms:** `wd:QID#PID=VALUE_QID`, `wd:QID#alias=TEXT`, `wn:SYNSET#lemma=TEXT`, `wn:SYNSET#RELATION=TARGET`, `wp:REVISION_ID#quote=TEXT` (at most 20 words, copied exactly), `ex:EXAMPLE_ID`.

**Check report** (`report.jsonl`): one line per seed, `{concept_id, status: pass|fail, errors[], warnings[]}`.

**RUN.md:** dates, seed commit and hash, model and settings, tools, evidence sources, deviations, coverage totals, retries and unresolved failures.

## Appendix B. Flags

The Grok Bot editions use free-text flags. The repository's review flags are documented in `docs/REVIEW-FLAGS.md`.

## Appendix C. Scripts

| Script | What it does |
|---|---|
| `tools/lexicon.py validate` | structural validation of the lexicon |
| `scripts/summary_stats.py` | the inventory recount used by the manuscript |
| `replication/scripts/assemble_bundles.py` | builds evidence bundles (way A) and neighbours |
| `replication/scripts/render_prompts.py`, `generate_drafts.py` | render prompts and drive drafting |
| `replication/scripts/verify_drafts.py` | pointer and format checks (`--ungrounded` for no-source runs) |
| `replication/scripts/compare_models.py` | side-by-side view for people; computes no agreement |
| `replication/scripts/collect_flags.py` | gathers flags for review |
| `replication/scripts/agreement.py` | the agreement kit: run, join, register, export-packet, import, validate, stats |

## References

- Miller, G. A., Beckwith, R., Fellbaum, C., Gross, D., and Miller, K. J. 1990. Introduction to WordNet: An on-line lexical database. *International Journal of Lexicography* 3(4): 235–244. Revised in *Five Papers on WordNet*, CSL Report 43, Princeton University, 1990, revised 1993.
- Miller, G. A. 1990. Nouns in WordNet: A lexical inheritance system. *International Journal of Lexicography* 3(4): 245–264.
- Gross, D., and Miller, K. J. 1990. Adjectives in WordNet. *International Journal of Lexicography* 3(4): 265–277. Revised as Fellbaum, Gross and Miller in *Five Papers on WordNet*, 1993.
- Fellbaum, C. 1990. English verbs as a semantic net. *International Journal of Lexicography* 3(4): 278–301.
- Beckwith, R., Miller, G. A., and Tengi, R. 1993. Design and implementation of the WordNet lexical database and searching software. In *Five Papers on WordNet*.
- Miller, G. A. 1995. WordNet: A lexical database for English. *Communications of the ACM* 38(11): 39–41.
- Fellbaum, C., ed. 1998. *WordNet: An Electronic Lexical Database*. MIT Press.
- Vrandečić, D., and Krötzsch, M. 2014. Wikidata: A free collaborative knowledgebase. *Communications of the ACM* 57(10): 78–85.
- Krippendorff, K. 2018. *Content Analysis: An Introduction to Its Methodology*, 4th ed. SAGE.
- Fleiss, J. L. 1971. Measuring nominal scale agreement among many raters. *Psychological Bulletin* 76(5): 378–382.
- Shared methods paper: *Building WordNet-style lexica with AI: process and provenance* (`building-wordnet-style-lexica-with-ai.md` in this folder).
- The manuscript's references, unchanged: O\*NET 30.2; ESCO; Zhang et al. 2022 (SkillSpan); Zhang, van der Goot and Plank 2024; De Santo et al. 2026 (SkiLLens); PROV-O (2013); SKOS (2009); SSSOM.
