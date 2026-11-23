# Measuring semantic agreement between independent model editions of the lexicon

**Status:** proposal, draft 2, revised 2026-11-23 by Grok Bot for Nik Bear Brown. Draft 2 changes three things. Judges now run through the existing Codex and Claude Code subscription plans, so there is no API budget. The judge panel is Codex plus three Claude models, with self-preference controls. And there is a design for human judges, who are interviewed by an agent (section 7). The instructions for judges are in [judging/](judging/README.md): [AI-JUDGE-INSTRUCTIONS.md](judging/AI-JUDGE-INSTRUCTIONS.md) for model judges, [HUMAN-JUDGE-INSTRUCTIONS.md](judging/HUMAN-JUDGE-INSTRUCTIONS.md) for people, and [INTERVIEWER-PROTOCOL.md](judging/INTERVIEWER-PROTOCOL.md) for the agent that runs a person's session. All three share one schema ([judgment.schema.json](judging/judgment.schema.json)) and one validator (`agreement.py validate`). Nothing in this page has been run at full scale yet. `scripts/agreement.py` is a draft skeleton that does the deterministic parts (normalising the editions, coverage, ID and string alignment, the statistics) and writes the judge requests. It does not call a judge model. Judges read request files and write result files (section 9).

**Question.** When several language models draft the same lexicon independently, how far do they agree on what each entry says? We want to know this field by field (sense, definition, links, variants, every relation type, basis, and whether a target is in the lexicon), for each pair of models and across all of them. Wording will always differ, so the method has to measure agreement in meaning, not in words. A panel of language models acts as the judge, human judges validate it, and embedding similarity serves as a cheap baseline.

**Builds on:** `compare_models.py` (a side-by-side view for people to read; it computes no agreement), `verify_drafts.py` (whether pointers are valid), the pilot design in `GENERATION_GUIDE.md` ("relations a reviewer judges unsupported, filled slots that should have been empty, and hypernym and hyponym reversals"), and the reviewer verdicts in `reviews/BRIEF.md` (`supports`, `contradicts`, `unsure`). Those verdicts measure whether a claim is correct. This page measures agreement, and section 11 explains how the two fit together.

---

## 1. The editions as they are today

Both editions pin the roster at commit `91312fec` (3,754 concepts). Copies are on branch `grok-lexicon-parallel-data` under `data/lexicon-parallel/`.

| Edition | Concepts | Schema | Grounding |
|---|---:|---|---|
| `grok-bot-20261122`, pilot | 36 | gen-v2 (kit) | grounded **and** ungrounded |
| `grok-bot-20261122`, full run | 3,718 | gen-v2 (kit) | ungrounded (every claim is `model_knowledge`) |
| `claude-sonnet-5-5` | 2,895 | its own (below) | 120 definitions sourced from O\*NET, 2,775 from `model_knowledge`; every relation and variant is `model_knowledge` |
| reference: the lexicon at `91312fec` | 3,754 | `schemas/entry.schema.json` | 3,552 entries drafted by `claude-sonnet-5-5` on 2026-10-29; the rest imported (O\*NET, jobs.humanitarians.ai) |

**Overlap (computed from the files):** the two editions share **2,895 concepts**, which is every concept in the Sonnet edition. Of these, 2,863 come from Grok's full run and **32 are pilot concepts**. The Sonnet README says the pilot is out of scope, but its `entries.jsonl` does include the 32 pilot concepts that are not credentials. Only the four pilot credentials have no Sonnet counterpart: Bachelor's in Nursing, Bachelor of Science in Nursing, Class B CDL and CCNA Security. The other 859 − 4 = 855 credentials are drafted by Grok alone. For the 32 shared pilot concepts, Grok has two drafts (grounded and ungrounded). The main comparison uses the **ungrounded** one, so that both sides worked from model knowledge, and the grounded one is a secondary contrast (section 8.4).

Profile of the 2,895 shared concepts (exact-ID and normalised-string matching only, before any semantic alignment):

| | Grok | Sonnet | both non-empty | exact match today |
|---|---:|---:|---:|---|
| entries with relations | 1,315 | 203 | 116 | 84 of 1,124 distinct targets (union) by ID |
| relations | 1,856 (855 label-only, 173 of them resolvable by name) | 207 | | |
| entries with variants | 1,330 | 312 | 271 | 210 of 1,882 distinct normalised strings (union) |
| links (Wikipedia, Wikidata, WordNet) | all ABSTAIN or NOT_OFFERED (no-source bundles) | NOT_ELICITED | | |

The two editions differ most in **how much** they say. Sonnet gives relations for 7% of shared concepts and Grok for 45%. Any statistic that does not separate "said something different" from "said nothing" will mostly measure verbosity. The method reports the two apart throughout.

### 1.1 Schema crosswalk (step 0: normalise before comparing)

Every edition is converted by an adapter into one **canonical entry** (`agreement.py`, `load_edition`). Fields an edition never asked for become `NOT_ELICITED`. That is different from `ABSTAIN` (the model was asked and chose null) and from `EMPTY` (asked, and gave an empty list).

| Canonical field | gen-v2 (Grok, kit) | Sonnet edition | Reference lexicon |
|---|---|---|---|
| `sense` | `work_sense` | NOT_ELICITED (its definition serves as the sense proxy, flagged `sense_from_definition`) | NOT_ELICITED (definition serves as proxy) |
| `definition` | `definition.text` | `definition.text` | `definition` |
| `links.{wikipedia,wikidata,wordnet}` | `choice`, or ABSTAIN when null; NOT_OFFERED when the bundle had no candidates | NOT_ELICITED | NOT_ELICITED |
| `variants[].text` | `text` | `label` | `label` |
| `variants[].conditional` | `condition` is not null | `ambiguous == true` | `needs_context` or `match` is not exact |
| `variants[].condition` | `condition` | NOT_ELICITED (true or false only) | `needs_context` |
| `relations[].type_fine` | the nine gen-v2 types | NOT_ELICITED | NOT_ELICITED |
| `relations[].axis` (coarse) | see the type map below | see the type map below | see the type map below |
| `relations[].target_key` | `target_id`, or else `new:<label>` until aligned | `target` (always an ID) | `target` |
| `relations[].proposed_new` | `proposed_new` | false (always an ID) | false |
| `basis` (per claim) | `basis` | `basis` | from `evidence` notes (`general-knowledge` maps to `model_knowledge`) |
| `pointers` | `pointers` | `sources[].identifier` (O\*NET codes) | NOT_ELICITED |
| `flags` | strings | `{type, note}` | n/a |

**Relation type map.** Agreement is measured on a **coarse axis** that every schema can express, and on the fine type only between editions that both use gen-v2.

| Coarse axis | gen-v2 types | Sonnet / reference types |
|---|---|---|
| `EQUIV` | synonym | (none) |
| `TAX_UP` (concept is a kind of target) | hypernym | broader |
| `TAX_DOWN` (target is a kind of concept) | hyponym | (none) |
| `PART_UP` (concept is part of target) | holonym | part_of |
| `PART_DOWN` (target is part of concept) | meronym | (none) |
| `ASSOC` (associated, not taxonomic) | uses, requires, certifies | related |
| `CONTRAST` | contrast | contrast |

Direction is normalised: a relation `TAX_DOWN(A→B)` is also stored as `TAX_UP(B→A)` when B is a lexicon concept, so that A's hyponym and B's hypernym count as the same edge in the **graph-level** analysis (section 6.3). A pair with opposite directions (A says B is broader, B says B is narrower) is labelled a **reversal**, the error the generation guide asks us to count.

Sonnet's `related` is wider than any single gen-v2 type. A gen-v2 `uses` or `requires` matched with a Sonnet `related` on the same target therefore counts as a coarse-axis agreement and as a fine-type `COMPATIBLE`, never `EQUIVALENT`.

### 1.2 First deterministic numbers (exact matching only; a lower bound on semantic agreement)

From `scripts/agreement.py run` on the two editions plus the reference, with intervals from 300 bootstrap resamples:

| Pair | Shared | Relation F1, target (macro) | Relation F1, target + axis | Variant F1, exact normalised | Conditional flag agrees |
|---|---:|---|---|---|---|
| Grok × Sonnet | 2,895 | 0.055 [0.044, 0.066] | 0.033 [0.024, 0.042] | 0.111 [0.098, 0.125] | 0.85 (n = 222) |
| Grok × reference | 3,754 | 0.107 [0.095, 0.119] | 0.066 [0.056, 0.075] | **0.963** [0.956, 0.970] | 0.98 (n = 2,851) |
| Sonnet × reference | 2,895 | 0.066 [0.046, 0.088] | 0.053 [0.035, 0.072] | 0.106 [0.093, 0.119] | 0.99 (n = 206) |

Two lessons for the method: (1) on exact matching, agreement is very low, so semantic alignment (section 3) is where the analysis has to happen; (2) Grok's variants almost reproduce the reference's, because the bundle showed the lexicon's existing variants. That is the copy-through effect (section 6.6) and must be removed before agreement on variants is interpreted.

---

## 2. What gets compared: units and levels

| Level | Unit | Value each edition gives | Comparison |
|---|---|---|---|
| L0 coverage | concept | drafted or not, with a pass or fail status | deterministic |
| L1 sense | concept | sense statement (work_sense, or the definition as proxy) | LLM: sense clustering |
| L2 definition | concept × model pair | definition text | LLM: pairwise label |
| L3 links | concept × source | ID, ABSTAIN, NOT_OFFERED or NOT_ELICITED | deterministic, with LLM only to tell "different but compatible" from "conflicting" |
| L4 variants | concept | set of strings, each conditional or not, with a condition | align (strings, then LLM), set F1, then condition label |
| L5 relations | concept × axis (and × fine type) | set of targets | align (ID, string, LLM), set F1, type label on matched targets |
| L6 basis and pointers | aligned claim | source or model_knowledge; pointer list | deterministic |
| L7 target status | aligned relation target | in the lexicon (ID) or proposed_new | deterministic |
| L8 entry | concept × model pair | all of the above | composite score |

---

## 3. Alignment: match items across models before judging

Alignment comes first. If items are not matched, a judge asked whether "two relation lists agree" will reward lists that look similar, not lists that say the same thing.

**3.1 Sense gate (L1).** For each concept, the judge sees the concept's name and kind plus every edition's sense statement, anonymised and shuffled. It groups them into **sense clusters**: same referent in the world of work, or different referent (prompt P1). A model whose sense falls outside the majority cluster is marked `cross_sense` for that concept. Its other fields are still compared but reported **separately**, because disagreement about relations is then a consequence of having picked a different sense (Service orientation in the software sense versus the customer sense, for example). This is also the main result for the trap concepts.

**3.2 Relation targets (L5).** These are aligned in three passes, each logged with the pass that produced the match:

1. **By ID.** `target_id` or `target` equal. Exact, no judge needed.
2. **By name.** A proposed_new label is normalised (NFKC, case-folded, punctuation and spacing removed, a trailing "(programming language)" style qualifier dropped) and matched to a lexicon `preferred_name` or variant label at `91312fec`. If exactly one concept matches, the label resolves to that ID (`resolved_by=name`). If several match, it stays unresolved.
3. **By meaning.** Within one concept, take every target still unresolved, plus the other editions' targets on the same coarse axis family. The judge clusters them into "same concept" groups (prompt P3). A group containing a lexicon ID takes that ID. Otherwise it gets a synthetic key `new:<concept_id>:<k>`. Grouping across axes is allowed, so that "uses Linux" and "requires Linux" align on target and then disagree on type.

**3.3 Variants (L4).** First an exact match after normalisation. The rest go to the judge clustering prompt (P3), with the rule that a variant matches only if it names the same concept (so "Go" and "Golang" match, but "PG" and "PostgreSQL Global Development Group" do not).

**3.4 Links (L3).** Links are matched on canonical identity, not on raw strings. A Wikipedia revision ID is resolved to its page ID and title after redirects, using the model's own bundle, because models that built their own bundles (way A) have different revisions of the same page. Wikidata uses the QID. WordNet uses the OEWN 2025 synset ID.

All alignments are saved (`alignment/*.jsonl`, section 10) **before** any agreement label is assigned. 10% of the meaning-based alignments go into the human validation sample (section 9).

---

## 4. The LLM judge

### 4.1 Labels for each field

**Definitions and sense statements (pairwise, P2).** One label, with sub-fields:

| Label | Meaning | Score |
|---|---|---:|
| `EQUIVALENT` | Same sense, same genus, same essential differentia. A recruiter would accept the same postings under either. | 1.00 |
| `NARROWER` or `BROADER` | Same sense, but one scope strictly contains the other (A is narrower than B, or broader). | 0.75 |
| `OVERLAPPING` | Same sense, different emphasis. Neither contains the other and nothing contradicts. | 0.50 |
| `CONFLICTING` | Same sense, but at least one factual claim contradicts (genus, issuer, what it is a kind of, scope). | 0.00 |
| `DIFFERENT_SENSE` | Different referents. | 0.00 |
| `ONE_SIDE_ONLY` | Computed, never judged: one edition has no value. | not scored, counted |
| `UNSURE` | Any stage, model or human: the judge cannot tell. | missing (the rate is reported for each judge) |

Sub-fields: `same_sense` (bool), `genus_a`, `genus_b` (a few words each), `conflicts` (a list of claim pairs), `confidence` (1–5), and `rationale` (40 words at most, quoting the short spans it relied on).

**Variants: conditions (P5).** For each aligned variant pair: `BOTH_UNCONDITIONAL`, `SAME_CONDITION`, `COMPATIBLE_CONDITION`, `CONFLICTING_CONDITION`, or `CONDITIONAL_VS_NOT`. The last is assigned deterministically whenever one side has a condition and the other does not.

**Relations: type of an aligned target (P4).** `SAME_TYPE`, `COMPATIBLE_TYPE` (for example uses and requires, meronym and uses, or Sonnet `related` with any ASSOC type), `REVERSED` (hypernym against hyponym, or holonym against meronym), and `CONFLICTING_TYPE` (for example hypernym against contrast, or synonym against contrast). The judge sees both relation statements spelled out as sentences, using the system prompt's own tests ("[concept] is a kind of [target]").

**Links (L3), deterministic:** `SAME`, `BOTH_ABSTAIN`, `ABSTAIN_VS_LINK`, `DIFFERENT`. Only `DIFFERENT` goes to the judge (P6), which labels it `COMPATIBLE` (for example a product versus its software family in Wikidata, or a page that redirects) or `CONFLICTING` (a different referent).

### 4.2 Prompts

Each prompt has a version (`agree-v1`) and its SHA-256 is saved in every judgment record. The texts are below. The renderer is `agreement.py prompts`.

**System (all judge calls):**

```
You compare entries from a dictionary of work concepts (skills, tools, knowledge areas, abilities,
languages, credentials) as they appear in job postings and course syllabi. Several anonymous drafters
wrote entries for the same concept independently. You judge whether they MEAN the same thing, not
whether they use the same words. Wording, length, order and style do not matter. A longer or more
fluent text is not better. Do not decide which drafter is right; decide only how their meanings relate.
Use only the texts shown and general knowledge of the concept. Return only the JSON object asked for.
```

**P1, sense clustering (one call per concept):**

```
Concept: "{preferred_name}" (kind: {kind}; broad class: {broad_class})
Lexicon neighbours, for orientation only: {up to 10 neighbour names}

Each drafter states the sense of this concept as used in work:
{for each item, in random order: [S1] text, [S2] text, ...}

Group the statements so that two statements share a group if and only if they refer to the same thing a
job posting could ask for (same referent), even if one is broader or narrower. Different referents (for
example a programming paradigm versus a customer-service attitude) go in different groups.
Return: {"groups": [["S1","S3"],["S2"]], "majority_reading": "<10 words>", "ambiguous_name": true|false,
         "note": "<=30 words"}
```

**P2, definition pair (one call per concept per pair; A and B are assigned at random):**

```
Concept: "{preferred_name}" (kind: {kind})
Definition A: {text_a}
Definition B: {text_b}

Choose exactly one label:
EQUIVALENT: same sense, same kind of thing, same essential features; either could replace the other.
A_NARROWER: same sense, A's scope is strictly inside B's.   B_NARROWER: the reverse.
OVERLAPPING: same sense, different emphasis, neither contains the other, nothing contradicts.
CONFLICTING: same sense, but some factual claim in one contradicts the other (what it is a kind of,
             who issues it, what it covers, what it is used for).
DIFFERENT_SENSE: they describe different things.
UNSURE: you cannot tell (counted as missing; do not use it to avoid hard items).
Return: {"label": "...", "same_sense": true|false, "genus_a": "...", "genus_b": "...",
         "conflicts": [{"a": "<span>", "b": "<span>"}], "confidence": 1-5, "rationale": "<=40 words"}
```

**P3, set alignment (variants, or relation targets; one call per concept and field, only for items left unaligned after the deterministic passes):**

```
Concept: "{preferred_name}" (kind: {kind})
Below are {variant names | relation targets} proposed by anonymous drafters, in random order, each
with an item id. {for targets: each line shows the target name and, if given, its lexicon id}
{I1 ...} {I2 ...} ...

Group items that name the SAME concept. {Variants: a variant matches only if, in a job posting, it
would name this same concept.} {Targets: ignore the relation type; group by what the target is.}
Do not group a thing with a broader or narrower thing (Java is not Java EE; SQL is not PostgreSQL).
Return: {"groups": [["I1","I4"],["I2"],["I3"]], "notes": {"I3": "<=20 words if unsure"}}
```

**P4, relation type for an aligned target:** both statements are shown as sentences from the gen-v2 tests, for example "A says: PostgreSQL is a kind of SQL. B says: PostgreSQL uses SQL." The output is `{"label": SAME_TYPE|COMPATIBLE_TYPE|REVERSED|CONFLICTING_TYPE, "confidence", "rationale"}`.

**P4 to P6** (relation type, variant condition, link compatibility) follow the same pattern, with the labels in 4.1. Their exact texts are in `judging/prompts/P4.txt` to `P6.txt`. The draft script generates only P2 requests so far.

Output is validated against a JSON schema (`schemas/agreement-judgment.schema.json`, to be added in stage 1). An invalid reply gets **one** retry with the validation error, the same rule as the kit's drafting retry. If it fails again, the item is recorded as `JUDGE_FAILED` and kept in the denominators as missing.

### 4.3 Blinding and order

- Model names, `draft_set`, `_meta`, edition folder names and `flags` are removed. Model-identifying words in the text ("Grok", "Claude", "as an AI") are masked. Every item is shown in the same neutral format, for example `Definition A: ...`.
- A and B are assigned at random for each call. In the pilot, and for a 10% sample at full scale, each pair is judged **in both orders**. The **position-flip rate** is reported, and `A_NARROWER` turning into `B_NARROWER` under the swap counts as consistent.
- In P1 and P3, items are shuffled with a seed saved in the record.
- The key that maps anonymous item IDs to models is written to a separate `keys/` file that the judge never sees. A request file never contains an edition name.
- **Style normalisation before judging.** Every text is first put into the common canonical format of section 1.1. A deterministic normaliser then (a) unifies quotes, dashes, spacing and the final full stop, (b) maps British spellings to American with a fixed word list, (c) removes stock openings ("In job postings, ...", "Refers to ...") from a fixed list, and (d) shows variants and relation targets as bare names in a fixed order. The normaliser never changes content words. Its rules are versioned along with the prompts.
- **Leak check.** On 100 pilot pairs, each judge is asked which of the two texts a Claude model wrote. If any judge does better than chance (a binomial test, p < 0.05), the blinding leaks style. The normaliser is then tightened and the check repeated. The accuracy is reported either way.

### 4.4 The judge panel, self-preference, and consistency

**Panel.** Four model judges, each run through a subscription plan Bear already has, in an agent harness. No paid API is used.

| Judge id | Harness and plan | Family | Also a drafter? |
|---|---|---|---|
| `codex` | Codex (OpenAI), Bear's US$200-a-month plan | OpenAI | no |
| `claude-fable` | Claude Code, Claude Fable | Anthropic | no (same family as a drafter) |
| `claude-sonnet` | Claude Code, Claude Sonnet | Anthropic | **yes**, if it is Sonnet 5.5 (the `claude-sonnet-5-5` edition, and most of `reference`) |
| `claude-opus` | Claude Code, Claude Opus | Anthropic | no (same family as a drafter) |
| `grok-bot` (optional) | Grok | xAI | **yes** (the `grok` edition) |

**Self-exclusion: drafters never judge their own edition.** The rule works item by item. A model that drafted an edition is never shown any item whose hidden key includes that edition, and `agreement.py register --drafted` enforces this when it writes the judge's packets. Concretely:

- **Grok** drafted `grok`, so it never judges an item involving Grok's edition. Today that leaves it only Sonnet × reference items (2,895 of 9,544 definition requests), and in future, pairs of other editions. If Bear prefers the stricter reading ("a drafter never judges at all"), Grok simply isn't registered (decision 1 in section 12).
- **Claude Sonnet 5.5**, if the panel's Sonnet is that same model, is excluded from items involving `claude-sonnet-5-5` or `reference`. On items about other editions, it judges normally.
- **Fable and Opus** drafted nothing, so they judge everything. Because they share a family with a drafter, they are checked for self-preference below.
- **Any future edition:** its model registers with `--drafted <edition>`, and the same rule applies.
- **Self-judgment probe:** to measure self-preference directly, a drafter can additionally be run on its own edition's items under a separate judge id (for example `claude-sonnet-selfprobe`). Probe labels are compared with the panel's and **never** enter the panel label.

**Aggregating the panel.** Three of the four judges are Anthropic models, so a simple majority would let one family decide. The **primary label is balanced by family**: the Claude label is the majority of the three Claude judges (or their median for the ordinal definition score); the Codex label stands alone; and the panel score is the mean of the two family scores. For nominal labels, the panel label is the one the two families agree on, and items where they disagree go to `FAMILY_SPLIT` (counted, and oversampled for humans). The **full four-judge majority** is reported next to the primary label.

**Self-preference controls:**

1. **Blinding and style normalisation** (section 4.3), with the leak check.
2. **Codex-only results** next to every panel result. Codex is the only judge outside the family of any drafter, so it is the cleanest reading.
3. **Self-preference check (difference in differences).** Each Claude judge j (Fable and Opus on every item; Sonnet through its self-judgment probe) gets a score for leniency toward the Sonnet edition, relative to Codex:
   Δ_j = [mean score_j − mean score_codex] on pairs **involving** the Sonnet edition − [the same difference] on pairs **not involving** Sonnet or the reference (which Sonnet mostly wrote).
   Today the non-Sonnet pairs are Grok grounded × Grok ungrounded in the pilot, plus any later editions. Δ_j gets a bootstrap interval. If the interval excludes 0, judge j shows self-preference (or, from the Codex side, lack of it). For the same check on alignments (P3), the outcome is the rate at which a judge merges a Sonnet target with another edition's target. For relation types (P4), it is the rate of `SAME_TYPE` when one side is Sonnet. When the correctness review (section 11.1) is added, the same check uses "supports" on Sonnet claims, where self-preference matters most.
4. **Leave one judge out.** Every main table (T3, T5) is recomputed once without each judge in turn (and without Grok, if Grok judged). A conclusion is reported as robust only if it holds every time.
5. **Agreement between judges, by family** (section 7.4). If Claude judges agree with each other much more than with Codex, the gap is reported. That gap is a family effect, not evidence that the Claude judges are right.

**Self-consistency.** Agent harnesses do not expose temperature or seeds, so repeat runs vary through order and session instead. Each judge runs R = 3 times in the pilot, each time in a fresh session with a different shuffle seed and the other A/B order. At full scale, R = 1, plus R = 3 on a 10% stratified sample. Test-retest is reported as Krippendorff's α across runs.

**Pinning.** Each batch records the harness and its version, the model as the harness reports it, the reasoning-effort setting, the plan, and the start and end time with zone (section 9.4). A batch whose reported model differs from the manifest is rejected and rerun.

---

## 5. A cheap baseline next to the judge

For every definition pair and sense pair:

1. **Embedding cosine**, from one pinned open sentence-embedding model chosen from a family outside the editions. It runs on CPU in minutes for about 6k texts.
2. **Lexical baselines:** token Jaccard and ROUGE-L.

They are reported in three ways: (a) Spearman correlation with the judge's ordinal score; (b) ROC-AUC for predicting the human label "same meaning" (EQUIVALENT, NARROWER or BROADER) on the validation sample; (c) a deliberately adversarial comparison on the look-alike pairs (Java against JavaScript, Angular against AngularJS, C against C++ and C#), where high cosine with the judge saying `DIFFERENT_SENSE` shows why a judge is needed. If the baseline matches the judge as well as two humans match each other, the paper can say so and recommend the cheap method.

---

## 6. Statistics

Every interval below is a **95% bootstrap interval from 2,000 resamples of concepts** (10,000 in the pilot), because fields within one concept are correlated. Where judge runs repeat, a second level of the bootstrap draws one judge run per item, so judge noise is included. Intervals are percentile intervals, or BCa when the statistic is skewed.

### 6.1 Agreement for each field and each pair of models (works with N = 2)

For each field f and pair (m, n) over the concepts both drafted:

- **Mean agreement score** (scores from 4.1). In addition, `P(same meaning)` = the share of pairs labelled EQUIVALENT, NARROWER or BROADER, and the full label distribution.
- **Both present, one only, neither**, given as counts and shares before any agreement is computed, so that coverage and verbosity are kept separate from meaning.
- **Links:** exact agreement, plus Cohen's κ on the three-way {link, abstain, not offered} value. Where both editions link, the same-target rate is also given. (Not available for Grok against Sonnet: Sonnet did not elicit links.)
- **Basis:** for aligned claims, agreement and κ. When an edition's basis has no variance (Grok full run: all `model_knowledge`), κ is undefined. The prevalence is reported instead, with no κ.
- **Target status:** for aligned targets, the agreement on in-lexicon versus proposed_new.

### 6.2 Agreement across many models (for N ≥ 3; computed for N = 2 as well)

- **Krippendorff's α** is the main coefficient because it handles missing data (Sonnet has no credentials) and any number of raters. Here the models are the raters.
  - *Nominal α* on: link choice; the sense-cluster ID from P1 (the arbitrary cluster label for each concept is a valid nominal value, since α uses only agreement within a unit); presence or absence of each candidate relation target, over a **fixed frame** for each concept: the kit's 30 bundle neighbours plus every aligned proposed_new cluster (one unit per concept × frame member; value = the coarse axis or NONE). The frame must not be built from the union of what the editions said. A union frame guarantees that at least one rater says something for every unit, which pushes α below zero (the draft script shows this: α = −0.21 on a union frame); the coarse axis of each aligned target; and the conditional flag of each aligned variant.
  - *A semantic α* for definitions: α = 1 − D_o / D_e. Here D_o is the mean pairwise distance within a concept, with distance = 1 − score from 4.1. D_e is estimated by having the judge label a random sample of 500 **cross-concept** pairs (same kind, different concept). Without that estimate, α cannot be computed for free text.
- **Fleiss' κ**, only on the complete subset where every model drafted every unit, as a familiar comparison.
- **Gwet's AC1** next to κ and α whenever a category is very common (abstentions, "no relation"), because κ falls sharply when one category dominates even if raw agreement is high.

### 6.3 Relation and variant sets

For each concept and pair, after alignment:

- **Set F1** = 2|A∩B| / (|A| + |B|) and **Jaccard**, at three levels of strictness: (i) same target, any type; (ii) same target and same coarse axis, direction normalised; (iii) same target and same fine type (gen-v2 against gen-v2 only). For level (iii), `COMPATIBLE_TYPE` counts as a half match and is reported separately.
- **Directional coverage:** the share of m's edges that n also gives, and the reverse. With Sonnet's sparse relations, this asymmetry is the main finding, so it is reported alongside F1.
- **Empty sets:** F1(∅, ∅) is undefined. "Both empty" is reported as its own agreement rate, and F1 is averaged only over concepts where at least one edition gives relations. A sensitivity version with F1(∅, ∅) = 1 is reported too.
- Both a **macro** average (mean over concepts) and a **micro** average (pooled edges) are given, for each axis and for each fine type: synonym, hypernym, hyponym, meronym, holonym, uses, requires, certifies and contrast.
- **Reversal rate:** the share of aligned taxonomic or part-whole edges with opposite directions.
- **Graph level:** the edges are combined into one directed graph per edition. The analysis reports how often the editions share edges, the agreement on each concept's TAX_UP parent, and the cycles each edition creates.
- **Consensus gaps:** proposed_new targets that two or more editions independently propose and that align to the same cluster. These are candidates for new lexicon concepts, and the list is a useful result in its own right.

### 6.4 One score per entry

For each concept and pair: S = Σ_f w_f · a_f / Σ_f w_f, summed only over fields **both** editions elicited. Each a_f is in [0, 1].

| Field | a_f | Default weight |
|---|---|---:|
| sense | 1 if same cluster, else 0 | 0.20 |
| definition | score from 4.1 | 0.25 |
| relations | F1 at level (ii); "both empty" = 1 | 0.25 |
| variants | F1 after alignment; "both empty" = 1 | 0.10 |
| links | mean over the three sources of exact or compatible agreement | 0.15 |
| basis and target status | agreement on aligned claims | 0.05 |

A **hard gate** applies: if the sense clusters differ, S = 0 (the ungated version is reported too). S is also reported with **equal weights** and for each field left out in turn. The paper should show that no conclusion depends on the weights. For N > 2, the entry score is the mean of S over pairs, and the unanimity rate is the share of concepts where every pair has S ≥ 0.75.

### 6.5 Breakdowns

Every statistic in 6.1 to 6.4 is broken down by: **kind** (15), **broad class** (skill, ability, knowledge, language, credential), **grounded versus ungrounded** (pilot only), **trap set** versus the rest, **schema pair** (gen-v2 against gen-v2, or gen-v2 against another), and **how often the concept appears in postings** (tertiles of `observations.jsonl` counts, if available).

The trap set: Java and JavaScript; C, C++ and C#; Angular and AngularJS; Swift; R, Go and C (short names); Service orientation; the two nursing degrees; and the two Mathematics records. Differences between breakdown cells use a paired bootstrap, with Holm correction within each table. A mixed-effects logistic model, `agree ~ pair + broad_class + grounded + (1 | concept)`, is an optional robustness check.

### 6.6 The existing lexicon as a reference

The lexicon at `91312fec` is treated as an **additional edition**, not as the right answer. 95% of its entries were drafted by `claude-sonnet-5-5`, so Sonnet against the reference partly measures Sonnet agreeing with itself. The analysis reports (a) each edition's agreement with the reference, (b) agreement between editions **when both depart from the reference**, and (c) the **copy-through rate**: the share of each edition's variants and relations that already appear in the reference. The kit's bundles showed the drafter the lexicon's existing record, so (c) measures anchoring directly.

---

## 7. Is the judge right? Validation

### 7.1 Human judges: who judges what

**No file upload.** A human judges by talking to Claude Code or Codex opened in this repository. The agent acts as an interviewer, following [judging/INTERVIEWER-PROTOCOL.md](judging/INTERVIEWER-PROTOCOL.md) (AGENT-AS-INTERVIEWER). The person reads [judging/HUMAN-JUDGE-INSTRUCTIONS.md](judging/HUMAN-JUDGE-INSTRUCTIONS.md). It registers the judge, draws their sample, and shows the blinded items one at a time. It maps the judge's free-form comments to the fixed label set, reads the label back for the judge to confirm, and keeps the judge's own words verbatim in `notes`. It writes `results/<judge_id>/` in the same schema as the model judges, runs the validator, and commits under the judge's name. A judge can pause and resume at any point. The interviewing agent records labels only; it never suggests one before the judge has spoken. Its mapping is checked because every label is read back and confirmed.

**Sampling (seeded, drawn fresh for each judge at registration):**

- **Size:** about **100 items** per judge by default, or **50** if the judge prefers.
- **Strata:** field (sense, definition, alignment, relation type, link) × broad class (skill, ability, knowledge, language, credential), allocated in proportion to the request pool with at least one item per non-empty cell. Kinds are spread within each cell. **Trap concepts** are always included, at a quota of at least 10% of each sample.
- **Overlap:** about **30%** of each judge's items come from a **shared overlap pool**, assigned least-judged-first, so every overlap item gets **at least 2** human judges once enough people have registered (with a pool of 50 and 30 overlap items each, from the fourth judge on). The other **70%** are **unique** to that judge and never given to another.
- **Scale:** with 10 judges at 100 items each, that is about 1,000 human judgments. With an overlap pool of 50 items, each pool item gets about 6 judges, and there are about 700 + 50 = **750 unique items**. Pool size, sample size, overlap share and the trap quota are all settings (`agreement.py register --size --overlap --pool-size --trap-share`).
- **Reproducibility:** the judge's seed is derived from the run salt and the judge id, and recorded in the registry, so anyone can redraw the same sample.
- **Optional rare-label boost:** if model judgments already exist when a judge registers, CONFLICTING, DIFFERENT_SENSE and FAMILY_SPLIT items can be oversampled. Sampling weights are recorded, and estimates are reweighted to the population with inverse weights.

**Why this design:**

- *Judge–human agreement* needs many distinct items more than repeated ones. The 70% unique share gives about 700 items, which estimates judge–human κ to about ±0.05 overall and to about ±0.08–0.10 per field.
- *Human–human agreement* is the ceiling the judge is held to (section 7.2). The overlap pool gives every pool item several human ratings. Krippendorff's α handles that incomplete, unbalanced design directly. A pool of 50 items × about 6 raters estimates human α to about ±0.1. A larger pool (for example 100 items at about 3 raters each) narrows that interval at the cost of fewer unique items, and the setting makes the trade explicit.
- A fresh seeded sample for each judge spreads human attention across the lexicon instead of concentrating it on one fixed set. It also keeps any single judge's tastes from defining the gold standard.
- Stratification guarantees that every field and every broad class is validated, including small ones (abilities, languages), and the trap quota guarantees that the hardest cases get human eyes.
- Humans see the same blinded, style-normalised rendering as the model judges, so differences come from the judging, not from what was shown.

**Effort:** 100 items at about 1.5 to 3 minutes each is roughly **3 to 5 hours per judge**, which can be split across sessions with pause and resume.

**Pilot:** the 32 shared pilot concepts form their own pool. Bear plus at least one other judge label all of it (96 definition pairs plus the other fields). That pilot work tunes the rubric before the seeded samples above are drawn for the full run.

### 7.2 What gets reported

- **Human–human** α (and pairwise κ) on the overlap pool, before adjudication. This is the **ceiling** for the judge. Adjudication of overlap items uses the majority of the human judges, and ties go to Bear.
- **Judge–human** on every human-judged item, measured against the adjudicated label where there is one and against the single human label otherwise. This is reported for the primary panel, for Codex alone, and for each judge: κ (weighted κ for the ordinal definition scale), a confusion matrix, and precision and recall for "same meaning" and for "conflicting".
- **Acceptance rule, fixed before the full run:** the judge panel is accepted for a field if judge–human κ ≥ 0.6 **and** is no more than 0.1 below human–human. Otherwise the rubric is revised, but **only on the pilot development split**, and the validation sample is drawn fresh after the rubric is frozen.

### 7.3 Consistency within one judge

Test-retest α across R runs, and the position-flip rate (section 4.3).

### 7.4 Agreement between judges

Pairwise κ for every pair of judges, and Fleiss' κ across the four; agreement within the Claude family against agreement between Codex and the Claude judges; the `FAMILY_SPLIT` rate; and the self-preference check of section 4.4.

---

## 8. Plan in stages (pilot first)

1. **Stage 0: freeze and normalise.** Record the commit SHA of each edition, run the adapters, and produce the coverage tables, the crosswalk audit and the deterministic alignments (ID and name). No model calls. *(The skeleton script does this now.)*
2. **Stage 1: pilot.** The 32 shared pilot concepts, plus the reference, plus Grok grounded against Grok ungrounded. Model judge panel (section 4.4) with R = 3, both orders, and the leak check. Full human annotation. Tune the rubric on half the concepts (development) and test it on the other half.
3. **Stage 2: freeze.** Prompt version `agree-v1` is locked. The analysis plan (this page, with its weights and acceptance rule) is committed with a tag **before** the full run.
4. **Stage 3: full scale.** The 2,895 shared concepts, plus 855 Grok-only credentials (coverage and reference comparison only). R = 1 plus a 10% sample at R = 3. Human judges register and are interviewed (section 7.1).
5. **Stage 4: as more editions arrive.** When another model hands in an edition, it gets an adapter; only the new pairs are judged; and α and Fleiss' κ are recomputed. Pairwise calls grow as N(N − 1)/2, while the clustering calls (P1, P3) stay at one per concept.
6. **Stage 5: paper.** Tables and figures (section 10.2).

### 8.4 Grounded against ungrounded

For the pilot, there are two contrasts: (a) **within a model**, Grok grounded against Grok ungrounded, which shows how much the sources change the entry; and (b) **across models**, whether cross-model agreement is higher when both are grounded. (b) needs a second gen-v2 grounded pilot edition. That is the main reason to have other models run the kit as it is.

---

## 9. Run plan (subscription agents, no API)

There is **no dollar budget**. All judging runs through the plans Bear already has: Codex (OpenAI, US$200 a month) and Claude Code (Fable, Sonnet, Opus). The plans are flat-rate, so the limits are the plans' usage windows and wall-clock time. Nothing is billed per token.

### 9.1 Requests and results are files, so any agent can do the work

- `agreement.py run` writes `requests/<stage>/batch-NNNN.jsonl`. Each batch holds 50 requests, and each line has `request_id`, `system`, `user` and `prompt_sha256`, with no edition names. A batch is the unit of work.
- `agreement.py register` gives each model judge its own copy, `packets/<judge_id>/batch-NNNN.jsonl`, with self-exclusion already applied (section 4.4).
- A judge session gets one instruction ([judging/AI-JUDGE-INSTRUCTIONS.md](judging/AI-JUDGE-INSTRUCTIONS.md)): read its packet batch; answer each line independently, following its own system and user text; write one JSON line per request to `results/<judge_id>/<stage>/batch-NNNN.jsonl`; then run `agreement.py validate`.
- **One fresh session per batch.** No context carries between batches, which keeps judgments independent and stops the drift that builds up in long sessions. Within a batch, the session must not compare lines with each other.
- Headless invocation, for example `codex exec -m <model> "<batch-judge prompt> requests/P2/batch-0007.jsonl"` or `claude -p --model <model> "<...>"`, the same way `run_batch.sh` already drives `claude -p`. Interactive sessions work too: the prompt is the same either way.
- `manifest.json` lists every batch × judge × run with a status (`todo`, `done`, `invalid`, `rerun`). A runner picks the next `todo`, so a stopped run resumes where it left off. Invalid replies get one retry (section 4.2).

### 9.2 Request and session counts (rough)

About 3 + N(N − 1)/2 requests per concept, where N counts editions plus the reference, plus order swaps and repeats.

| Scope | Requests per judge | Batches (= sessions) per judge, at 50 per batch | Four judges |
|---|---:|---:|---:|
| Pilot, 32 concepts (Grok ungrounded, Grok grounded, Sonnet, reference; both orders; R = 3) | about 1,500 | about 30 | about 120 sessions |
| Full, 2,895 shared concepts today (Grok, Sonnet, reference; R = 1 plus 10% at R = 3) | about 21,000 | about 420 | about 1,700 sessions |
| Full, 3,754 concepts, 5 editions | about 55,000 | about 1,100 | about 4,400 sessions |

Batches of 100 halve the session counts if a harness handles them reliably. The pilot shows which size works.

### 9.3 Rate limits

- Subscription plans meter usage in rolling windows (for example over a few hours, plus a weekly cap). The current limits are whatever the plan shows at the time; this page does not assume a number. The runner runs a small number of parallel sessions per plan (for example 2 to 4). When a session hits a limit, it marks the batch `todo` again and waits for the window to reset.
- Codex and Claude Code have separate limits, so the four judges can run at the same time. The three Claude judges share one plan's limits, so the Claude side is the slower one. It is scheduled round-robin across Fable, Sonnet and Opus, so that no judge finishes far ahead of the others and model updates hit all three at about the same point.
- At a rough 5 to 10 minutes per 50-request batch, the full run today is about 35 to 70 hours of session time per judge. Spread across usage windows, that is one to three weeks of calendar time. The pilot fits in a day or two.
- Usage spent on judging competes with Bear's other work on the same plans. The runner has a quiet-hours setting, and full-scale stages are scheduled for when the plans are otherwise idle.

### 9.4 Pinning and recording the model

- Each judge's model is set explicitly at launch (`-m` / `--model`) and never left to a default. At the start of each batch, the session writes a header line to its result file: `{"_batch": "...", "judge_id": "...", "harness": "codex|claude-code", "harness_version": "<codex --version | claude --version>", "model_reported": "<the model id the harness reports>", "effort": "<reasoning effort, if set>", "plan": "...", "started_at": "...-05:00"}`. It writes `finished_at` at the end.
- `validate` rejects a batch whose `model_reported` differs from the judge's entry in `judges.json`. If a provider changes the model behind a name partway through, the batches before and after are given different `judge_version` values and tested for a shift (on the repeated 10% sample).
- Because the model behind a hosted name can change, exact reruns are not guaranteed. Every request, result line and raw reply hash is committed, so the analysis itself can always be recomputed.

The embedding baseline and all the statistics run on CPU in minutes. The human interviews in 7.1 take the most time.

---

## 10. Outputs

### 10.1 Files (under `agreement/<run>/`, committed on a branch)

- `canonical/<edition>.jsonl`: one canonical entry per concept (section 1.1), with `edition`, `edition_sha`, `schema`, `run`.
- `coverage.csv`: concept_id, kind, broad_class, and one column per edition (`drafted`, `missing`, `out_of_scope`).
- `alignment/{targets,variants}.jsonl`: `{concept_id, field, cluster_key, members: [{edition, item_index, text, target_id}], resolved_by: id|name|judge|human, judgment_id}`.
- `keys/anon.jsonl`: `{request_id, A, B}`, plus `keys/request-id-secret.txt` (request ids are keyed with a secret, so nobody can recompute them from concept and edition names). These go in `--private-dir` and are **never committed** to the public repo. `stats` and `register` take `--keys PATH`. `canonical/`, `tables/` and `coverage.csv` are private too, because they name editions.
- `requests/<stage>/batch-NNNN.jsonl`: `{request_id, stage: P1..P6, concept_id, field, kind, broad_class, trap, prompt_version, prompt_sha256, order_seed, system, user}`. Only `system` and `user` are shown to a judge.
- `judges.json`: the panel (id, type `model` or `human`, harness, pinned model, family, drafter flag).
- `humans/registry.jsonl`, `humans/overlap-pool.jsonl`, `humans/<judge_id>/sample.jsonl`, `humans/<judge_id>/progress.json`: registration, the seeded sample and the resume point.
- `results/<judge_id>/<stage>/batch-NNNN.jsonl` for model judges, or `results/<judge_id>/judgments.jsonl` for humans. **The same line schema for both**, one line per judgment:

```json
{"judgment_id": "j-000123", "request_id": "r-000123", "stage": "P2", "concept_id": "sh6x1wmacn",
 "field": "definition",
 "judge": {"id": "codex", "type": "model", "harness": "codex", "model_reported": "...", "judge_version": 1},
 "run_index": 0, "order_seed": 11, "prompt_version": "agree-v1", "prompt_sha256": "...",
 "label": "A_NARROWER",
 "fields": {"same_sense": true, "genus_a": "...", "genus_b": "...", "conflicts": [], "confidence": 4,
            "rationale": "..."},
 "notes": null, "confirmed": null,
 "valid": true, "attempts": 1, "raw_sha256": "...", "created_at": "2026-12-01T10:00:00-05:00"}
```

  A human line has `judge.type = "human"`, `judge.name`, the judge's words verbatim in `notes`, and `confirmed: true` once the judge has accepted the read-back label. The model-only fields (`raw_sha256`, `attempts`) are null for humans. The pairing of A and B with editions lives only in `keys/`, and the statistics step joins it in.
- `adjudicated.jsonl`: the resolved labels for overlap items.
- `tables/*.csv`: one file per table below, each with its bootstrap intervals.

### 10.2 Tables and figures for the paper

| # | Table |
|---|---|
| T1 | Coverage by edition × broad class × kind, with the intersection |
| T2 | Schema crosswalk: which fields each edition elicits |
| T3 | Agreement per field: pairwise score, P(same meaning), α, Fleiss' κ, AC1, with 95% intervals |
| T4 | Model × model matrix, one per field |
| T5 | Relation set F1 at three levels of strictness, per axis and per fine type; directional coverage; reversal rate |
| T6 | Breakdowns by broad class and kind |
| T7 | Pilot: grounded against ungrounded |
| T8 | Trap concepts, case by case |
| T9 | Judge validation: human–human, judge–human, confusion matrices |
| T10 | Judge test-retest, position flips, agreement between judges |
| T11 | Embedding and lexical baselines compared with the judge and with humans |
| T12 | Consensus gaps: proposed_new targets proposed by two or more editions |

| # | Figure |
|---|---|
| F1 | UpSet plot of coverage |
| F2 | Heatmaps of model × field agreement |
| F3 | Definition labels per pair (stacked bars) |
| F4 | Forest plot of agreement by kind |
| F5 | Embedding cosine by human label (box plots) |
| F6 | Distribution of the entry score, gated and ungated |
| F7 | Confusion of relation types on aligned targets (Sankey or matrix) |

---

## 11. Threats to validity

1. **Agreement is not correctness.** Two models can agree on the same wrong claim, especially from shared pretraining (Wikipedia, O\*NET). This analysis is therefore paired with the correctness verdicts in `reviews/BRIEF.md` on the same human sample, and the paper reports "agree and correct", "agree and wrong" and "disagree" separately.
2. **A shared anchor.** Both drafting routes could see the lexicon's existing record (the kit's bundles include it), and most of that record was written by Sonnet. This inflates agreement. Mitigation: the copy-through rate and agreement conditional on departing from the reference (section 6.6).
3. **Model is confounded with schema and prompt.** Grok used the kit (gen-v2) and Sonnet used its own schema and instructions. A difference between them is therefore model **plus** procedure. The coarse-axis comparison reduces this but does not remove it. The fix is for each model to also run the kit as it is (stage 4).
4. **Differences in procedure.** Grok drafted every concept in one session rather than a fresh chat per concept (recorded in its RUN.md). The Sonnet model label is still awaiting the user's confirmation (its RUN.md). Both are recorded as edition covariates.
5. **Judge bias:** self-preference, because three judges are Anthropic models and one of them may be the same model as a drafter (handled by blinding, style normalisation, the leak check, Codex-only results, family-balanced aggregation, the difference-in-differences check and leave-one-judge-out; section 4.4); family-level shared blind spots, which balancing by family reduces but cannot remove with only two families; favouring longer or more fluent text, position bias (both orders tested), and leniency (labelling things OVERLAPPING too readily). Measured in 7.2 to 7.4.
6. **Alignment errors propagate.** An over-eager merge in P3 inflates set F1. Mitigation: deterministic passes first, a conservative prompt ("not broader or narrower"), and human checks on 10% of the meaning-based alignments.
7. **Ambiguity in the labels and the rubric.** NARROWER against OVERLAPPING is a fuzzy line. The human–human ceiling measures how fuzzy, and a sensitivity analysis merges them.
8. **Prevalence and sparsity.** Mostly empty fields (Sonnet's relations) give paradoxical κ values. Presence, AC1 and conditional agreement are reported separately (section 6.1).
9. **Concepts are not independent.** Look-alike and near-duplicate concepts are related, and bootstrap resampling by concept understates the uncertainty for them. A sensitivity check resamples families of related concepts (clusters of trap concepts).
10. **Coverage is selected.** The overlap excludes credentials, so the result is not about the whole lexicon. Credential agreement must wait for a second edition that covers credentials.
11. **Blinding by instruction.** Packets and requests are public files in this repo. A judge that compared its packet with another judge's (for example `grok-bot`'s, which holds only Sonnet × reference items) could infer which editions are paired. Judges are told to open only their own folders, and the leak check (4.3) would catch systematic unblinding. A stricter setup would hand each judge its packet privately.
11. **Drift and reproducibility.** Hosted judge models change. Subscription harnesses report a model name but may change what sits behind it. Batches are pinned and stamped (section 9.4), shifts are tested on the repeated sample, and every request and reply is committed.
12. **Many comparisons.** There are many fields × breakdowns × pairs. A short list of primary outcomes is fixed in advance (T3 per field and T5 at level (ii)), and everything else is exploratory with Holm correction.

---

## 12. Decisions for Bear

1. **The exact model ids** for `codex`, `claude-fable`, `claude-sonnet` and `claude-opus`, and whether `claude-sonnet` is the same Sonnet 5.5 that drafted (if it is, the self-preference check matters most). Also: does Grok judge items that don't involve its own edition (the default here), or not judge at all?
2. **Human judges:** who the roughly 10 are, and the settings (default: 100 items, 30% overlap, a pool of 50, a 10% trap quota; full pilot pool labelled by Bear and at least one other judge).
3. **Weights and the hard gate** for the entry score, and the acceptance threshold (κ ≥ 0.6 and within 0.1 of human–human).
4. **Whether to ask the Sonnet run (and future models) to also run the kit's gen-v2**, so the comparison is not confounded with schema. Without this, links, work sense, conditions and fine relation types are compared for Grok alone.
5. **Whether the reference lexicon counts as an edition** in α (default: reported separately, not counted).
6. **Scheduling:** how much of each plan's usage judging may take, and the quiet hours (section 9.3).
7. **Batch size** (50 or 100 requests per session), settled in the pilot.
