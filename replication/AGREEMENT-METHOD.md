# Measuring semantic agreement between independent model editions of the lexicon

**Status:** proposal, draft 1, written 2026-11-23 by Grok Bot for Nik Bear Brown. Nothing in this page has been run at full scale yet. `scripts/agreement.py` is a draft skeleton that does the deterministic parts (normalising the editions, coverage, ID and string alignment, the statistics) and writes the judge requests. It does not call a judge model yet.

**Question.** When several language models draft the same lexicon independently, how far do they agree on what each entry says? We want to know this field by field (sense, definition, links, variants, every relation type, basis, and whether a target is in the lexicon), for each pair of models and across all of them. Wording will always differ, so the method has to measure agreement in meaning, not in words. A language model acts as the judge, a panel of humans validates it, and embedding similarity serves as a cheap baseline.

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

**P5, variant condition** and **P6, link compatibility** follow the same pattern, with the labels in 4.1.

Output is validated against a JSON schema (`schemas/agreement-judgment.schema.json`, to be added in stage 1). An invalid reply gets **one** retry with the validation error, the same rule as the kit's drafting retry. If it fails again, the item is recorded as `JUDGE_FAILED` and kept in the denominators as missing.

### 4.3 Blinding and order

- Model names, `draft_set`, `_meta`, edition folder names and `flags` are removed. Model-identifying words in the text ("Grok", "Claude", "as an AI") are masked. Every item is shown in the same neutral format, for example `Definition A: ...`.
- A and B are assigned at random for each call. In the pilot, and for a 10% sample at full scale, each pair is judged **in both orders**. The **position-flip rate** is reported, and `A_NARROWER` turning into `B_NARROWER` under the swap counts as consistent.
- In P1 and P3, items are shuffled with a seed saved in the record.
- The key that maps anonymous item IDs to models is written to a separate `keys/` file that the judge never sees.

### 4.4 Choosing the judge and checking its consistency

- **Rule:** a judge never judges a pair that includes its own model family. Families under test now are xAI (Grok) and Anthropic (Claude). Later editions will add others.
- **Recommended: a panel of three** judges from families outside the editions being compared, including **one open-weights model** with pinned weights, so the full analysis can be rerun exactly. The panel label is the majority. If all three differ, the item is `NO_MAJORITY` and goes to a human. Panel agreement is reported (section 7.4).
- If an N-th edition comes from a judge's family, that judge is left out of every pair touching that edition, and the remaining two decide (with a tie going to a human).
- **Self-consistency:** each judge runs R = 3 times in the pilot (temperature 0.7, different order seeds), and R = 1 at full scale plus R = 3 on a 10% stratified sample. Test-retest is reported as Krippendorff's α across runs.
- Every model version, date, temperature, seed and prompt hash is pinned in each record, so drift in a hosted model can be detected.

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

### 7.1 The human sample

A **stratified sample, separate for each field type**, annotated independently by two people with expertise in the field (for example Bear and one trained research assistant). They are blind to model identity and to the judge's labels, and use the same rubric and the same anonymised rendering the judge saw.

| Stratum | Pilot | Full scale |
|---|---:|---:|
| definition pairs | all: 32 shared pilot concepts × (Grok ungrounded × Sonnet, Grok grounded × Sonnet, Grok grounded × ungrounded) = 96 | **300** |
| sense clusters | all | 150 |
| meaning-based alignments (targets and variants) | all | 200 groups |
| relation type labels (P4) | all | 200 |
| link disagreements (P6) | all | 100 (or all, if fewer) |

**Why 300 definition pairs:** to estimate judge–human Cohen's κ near 0.7 on five categories with a 95% interval half-width of about ±0.07, about 250–300 items are needed. To estimate a proportion near 0.8 to ±0.05, 246 are needed. Sampling is **stratified by judge label**, with at least 30 each of CONFLICTING and DIFFERENT_SENSE, which are rare but matter most. It is also stratified by broad class and by schema pair. Estimates are reweighted to the population with inverse sampling weights. Smaller fields use about 150–200 items, which gives about ±0.08–0.10.

**Effort:** about 1.5 minutes per definition pair and 2 to 3 minutes per alignment group. That comes to roughly **20 hours per annotator** at full scale and about 3 hours for the pilot.

### 7.2 What gets reported

- **Human–human** κ and α before adjudication. This is the **ceiling** for the judge.
- **Judge–human**, measured against the adjudicated label: κ (weighted κ for the ordinal definition scale), a confusion matrix, and precision and recall for "same meaning" and for "conflicting".
- **Acceptance rule, fixed before the full run:** the judge panel is accepted for a field if judge–human κ ≥ 0.6 **and** is no more than 0.1 below human–human. Otherwise the rubric is revised, but **only on the pilot development split**, and the validation sample is drawn fresh after the rubric is frozen.

### 7.3 Consistency within one judge

Test-retest α across R runs, and the position-flip rate (section 4.3).

### 7.4 Agreement between judges

Pairwise κ and Fleiss' κ across the three-judge panel; the `NO_MAJORITY` rate; and whether any judge leans systematically toward one edition, compared using the anonymisation key after judging.

---

## 8. Plan in stages (pilot first)

1. **Stage 0: freeze and normalise.** Record the commit SHA of each edition, run the adapters, and produce the coverage tables, the crosswalk audit and the deterministic alignments (ID and name). No model calls. *(The skeleton script does this now.)*
2. **Stage 1: pilot.** The 32 shared pilot concepts, plus the reference, plus Grok grounded against Grok ungrounded. Judge panel with R = 3, both orders. Full human annotation. Tune the rubric on half the concepts (development) and test it on the other half.
3. **Stage 2: freeze.** Prompt version `agree-v1` is locked. The analysis plan (this page, with its weights and acceptance rule) is committed with a tag **before** the full run.
4. **Stage 3: full scale.** The 2,895 shared concepts, plus 855 Grok-only credentials (coverage and reference comparison only). R = 1 plus a 10% sample at R = 3. Draw the human validation sample.
5. **Stage 4: as more editions arrive.** When another model hands in an edition, it gets an adapter; only the new pairs are judged; and α and Fleiss' κ are recomputed. Pairwise calls grow as N(N − 1)/2, while the clustering calls (P1, P3) stay at one per concept.
6. **Stage 5: paper.** Tables and figures (section 10.2).

### 8.4 Grounded against ungrounded

For the pilot, there are two contrasts: (a) **within a model**, Grok grounded against Grok ungrounded, which shows how much the sources change the entry; and (b) **across models**, whether cross-model agreement is higher when both are grounded. (b) needs a second gen-v2 grounded pilot edition. That is the main reason to have other models run the kit as it is.

---

## 9. Cost and compute

Per concept with N editions: P1 once, P2 N(N − 1)/2 times, P3 at most twice (variants, targets), P4 once per concept with type disagreements (batched), P6 rarely. Call it about **3 + N(N − 1)/2 calls**, with about 1.5k tokens in and 0.3k out each.

| Scope | Editions | Calls per judge run | Tokens per judge run (in / out) | Panel of 3, plus repeats |
|---|---:|---:|---|---|
| Pilot, 32 concepts | 2 + reference + grounded | about 32 × 9 ≈ 290; × 2 orders × R 3 ≈ 1.7k | about 2.6M / 0.5M | about 5k calls, about 8M / 1.5M tokens |
| Full, 2,895 concepts, today | 2 (+ reference = 3) | about 2,895 × 6 ≈ 17k | about 26M / 5M | × 3 judges × 1.1 ≈ 57k calls, about 86M / 17M tokens |
| Full, 3,754 concepts, N = 5 | 5 | about 3,754 × 13 ≈ 49k | about 73M / 15M | about 160k calls, about 240M / 48M tokens |

Cost scales as (input tokens × input price) + (output tokens × output price). For illustration, at US$3 per million input tokens and US$15 per million output tokens, the full run today costs about **US$500** for the panel, and the five-edition case about **US$1,450**. Batch APIs usually halve this. Running the open-weights judge locally costs nothing per call but takes GPU time: roughly one day on a single 80 GB GPU for the 3,754-concept, five-edition case at an 8B–70B model size. The embedding baseline and all the statistics run on CPU in minutes. The human annotation in 7.1 is the scarce resource.

---

## 10. Outputs

### 10.1 Files (under `work/agreement/<run>/`)

- `canonical/<edition>.jsonl`: one canonical entry per concept (section 1.1), with `edition`, `edition_sha`, `schema`, `run`.
- `coverage.csv`: concept_id, kind, broad_class, and one column per edition (`drafted`, `missing`, `out_of_scope`).
- `alignment/{targets,variants}.jsonl`: `{concept_id, field, cluster_key, members: [{edition, item_index, text, target_id}], resolved_by: id|name|judge|human, judgment_id}`.
- `keys/anon.jsonl`: `{request_id, item_id, edition}`. Never shown to the judge.
- `requests/<stage>.jsonl`: `{request_id, stage: P1..P6, concept_id, field, prompt_version, prompt_sha256, order_seed, system, user}`.
- `judgments/<stage>.jsonl`, one line per judge reply:

```json
{"judgment_id": "j-000123", "request_id": "r-000123", "stage": "P2", "concept_id": "sh6x1wmacn",
 "field": "definition", "pair": ["e1", "e2"], "order": ["e2", "e1"],
 "judge": {"model": "...", "version": "...", "family": "...", "temperature": 0.7, "seed": 11},
 "run_index": 0, "prompt_version": "agree-v1", "prompt_sha256": "...",
 "label": "A_NARROWER", "label_canonical": "NARROWER:e2<e1",
 "fields": {"same_sense": true, "genus_a": "...", "genus_b": "...", "conflicts": [], "confidence": 4,
            "rationale": "..."},
 "valid": true, "attempts": 1, "tokens_in": 1430, "tokens_out": 210, "raw_sha256": "...",
 "created_at": "2026-12-01T10:00:00-05:00"}
```

- `human/annotations.jsonl`: the same shape, with `annotator`, plus `adjudicated.jsonl`.
- `results/*.csv`: one file per table below, each with its bootstrap intervals.

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
5. **Judge bias:** preferring its own family (handled by the family-exclusion rule), favouring longer or more fluent text, position bias (both orders tested), and leniency (labelling things OVERLAPPING too readily). Measured in 7.2 to 7.4.
6. **Alignment errors propagate.** An over-eager merge in P3 inflates set F1. Mitigation: deterministic passes first, a conservative prompt ("not broader or narrower"), and human checks on 10% of the meaning-based alignments.
7. **Ambiguity in the labels and the rubric.** NARROWER against OVERLAPPING is a fuzzy line. The human–human ceiling measures how fuzzy, and a sensitivity analysis merges them.
8. **Prevalence and sparsity.** Mostly empty fields (Sonnet's relations) give paradoxical κ values. Presence, AC1 and conditional agreement are reported separately (section 6.1).
9. **Concepts are not independent.** Look-alike and near-duplicate concepts are related, and bootstrap resampling by concept understates the uncertainty for them. A sensitivity check resamples families of related concepts (clusters of trap concepts).
10. **Coverage is selected.** The overlap excludes credentials, so the result is not about the whole lexicon. Credential agreement must wait for a second edition that covers credentials.
11. **Drift and reproducibility.** Hosted judge models change. Versions are pinned, the open-weights judge serves as a reproducible anchor, and every request is saved with its raw reply hash.
12. **Many comparisons.** There are many fields × breakdowns × pairs. A short list of primary outcomes is fixed in advance (T3 per field and T5 at level (ii)), and everything else is exploratory with Holm correction.

---

## 12. Decisions for Bear

1. **Judge models:** which three families, and which open-weights model, given that xAI and Anthropic are under test.
2. **Human annotators** and the sample sizes (default: 300 definition pairs; 150–200 for the other fields; full annotation for the pilot).
3. **Weights and the hard gate** for the entry score, and the acceptance threshold (κ ≥ 0.6 and within 0.1 of human–human).
4. **Whether to ask the Sonnet run (and future models) to also run the kit's gen-v2**, so the comparison is not confounded with schema. Without this, links, work sense, conditions and fine relation types are compared for Grok alone.
5. **Whether the reference lexicon counts as an edition** in α (default: reported separately, not counted).
6. **Budget** for hosted judges (about US$500 today, about US$1,450 for five editions at the illustrative prices).
