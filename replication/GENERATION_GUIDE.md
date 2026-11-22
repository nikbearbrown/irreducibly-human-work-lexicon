# Irreducibly Human Work Lexicon: Source-Grounded Entry Generation

This pipeline drafts WordNet-style entries for lexicon concepts from Wikipedia, Wikidata, WordNet, and your own posting and syllabus examples. Large source data stays on the cluster. Each batch pulls a small bundle down, generates and verifies drafts locally, and pushes the results back.

Everything this produces is machine-drafted. The verifier checks that every cited pointer exists and says what the draft claims. It does not check that the claim is right. A real pointer can still support a wrong-sense claim, which is the Service Orientation failure. Passing the verifier makes a draft reviewable, not reviewed.

## How the pieces fit

For each batch:

1. A list of concept IDs and names goes up to the cluster.
2. A cluster job pulls Wikipedia and Wikidata candidates for those concepts into a small bundle.
3. The bundle comes down. Locally, it gets the lexicon record, nearby concepts, usage examples, and WordNet senses added.
4. The model drafts one JSON entry per concept.
5. The verifier checks every pointer. Failed drafts get one retry with the verifier's errors as feedback. Drafts that still fail are kept and marked for review.
6. Entries are rendered as markdown for human reading. A random sample is set aside for review, a manifest records versions, and everything goes back to the cluster.

## Part 1: The generation prompt

The scripts read these from `prompts/system.txt` and `prompts/user_template.txt`. Change `PROMPT_VERSION` whenever you edit either file; the manifest also records a hash of both.

System prompt. It still calls the project Skills Lexicon, its name when the pilot ran; keep that wording, so every model's drafts come from the same prompt:

```text
You draft entries for Skills Lexicon, an open vocabulary of skills, knowledge areas, abilities, languages, and credentials used to match job postings with course syllabi. You receive one concept and a bundle of source material. You return one JSON object.

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

User message template (the generator fills the placeholders from each bundle):

```text
Concept record:
{concept_json}

lexicon_neighbors (existing concepts you may use as relation targets):
{neighbors_json}

Usage examples from postings and syllabi:
{examples_json}

Wikipedia candidates (each with revision_id and plain text):
{wikipedia_json}

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
{wikidata_json}

WordNet senses for the concept's name and variants:
{wordnet_json}

Draft the entry for this concept. Return the JSON object only.
```

## Part 2: What each bundle contains

Each line of a bundle file is one concept. The verifier checks pointers against exactly this content, so anything the model should be able to cite must be in the bundle.

| Field | Built where | Contents |
|---|---|---|
| `concept_id` | local | The lexicon ID; also the join key for every file |
| `concept` | local | The record at the pinned commit: `id`, `preferred_name`, `kind`, `broad_class`, `variants`, existing relations |
| `neighbors` | local | 20 to 30 nearby lexicon concepts (`id`, `name`) by name or embedding similarity, plus concepts already related to this one |
| `examples` | local | Up to 5 posting snippets from the ledger and 3 syllabus observations, each with a stable `id`, a `source` label, and about 300 characters of `text` around the mention |
| `wordnet` | local | Senses for the preferred name and each variant from a pinned Open English WordNet release: `synset`, `lemmas`, `gloss`, `examples`, and `relations` keyed by the pointer relation names |
| `wikipedia` | cluster | Up to 3 candidate articles found by title and redirect match on the name and variants: `title`, `revision_id`, and plain `text` (lead section plus the first few thousand words, markup stripped) |
| `wikidata` | cluster | Up to 3 candidate items matched by English label, alias, or Wikipedia sitelink: `qid`, `label`, `description`, `aliases`, and `claims` limited to P31, P279, P361, P527, P460, and P1889 (QID values only); plus ancestors up to two levels through P31 and P279, each with `ancestor_of` set to its candidate |

The six Wikidata properties are instance of, subclass of, part of, has part, said to be the same as, and different from. The last one is a ready-made source of contrast candidates.

## Part 3: Cluster setup and the two data-specific scripts

Two scripts depend on how your data is laid out and aren't written yet: `extract_batch.sbatch` on the cluster and `assemble_bundles.py` locally. Their contracts follow. Run heavy cluster work as Slurm jobs, not on login nodes.

### One-time cluster preparation

Wikipedia: if the dump is the multistream XML version, it ships with an index file mapping titles to byte offsets, so you can seek straight to a page instead of decompressing the whole file. Build a redirect map once as well, since many skill names are redirects ("UX design" to the main article). Keep the revision ID from each page's revision element; it's what pointers cite. If the dump on the cluster is already processed (Parquet or JSONL), build a title index once instead.

Wikidata: the full JSON dump has one entity per line, so a streaming filter works without loading it. One Slurm job, two passes. The first pass keeps items whose English label or alias matches any lexicon name or variant, or whose English Wikipedia sitelink matches a candidate title. The second pass collects their P31 and P279 ancestors to two levels. Write the result as compact JSONL. Rerun it only when many new concepts enter the lexicon.

### Contract for `extract_batch.sbatch`

Input: a batch file with one concept per line (`concept_id`, tab, `preferred_name`, tab, variants separated by `|`) and an output directory. Output: `cluster_bundle.jsonl` in that directory, one line per concept, with `concept_id`, `wikipedia`, and `wikidata` as described in Part 2. A concept with no candidates gets empty lists, not a missing line.

### Contract for `assemble_bundles.py`

Input: the cluster bundle and the lexicon repository path. Output: `bundles.jsonl` with all seven fields from Part 2. It reads the concept record and neighbors from the lexicon at the current commit, pulls examples from the ledger and syllabus observation table, and adds WordNet senses through the `wn` package. The `wn` package names part relations `mero_part`, `holo_part`, `mero_member`, and `holo_member`; map them to `part_meronym`, `part_holonym`, `member_meronym`, and `member_holonym` so they match the pointer format.

## Part 4: Running a batch

### One-time local setup

1. Install the Python packages.

```bash
pip install anthropic wn
```

2. Download a pinned WordNet release. Use the newest OEWN edition the `wn` package offers if it's newer than this one, and set `OEWN_VERSION` to match.

```bash
python3 -c "import wn; wn.download('oewn:2024')"
```

3. Edit this block once with your values, then paste it into each new terminal session. It assumes `ANTHROPIC_API_KEY` is already set.

```bash
export CLUSTER_HOST="YOUR_USERNAME@YOUR_CLUSTER_LOGIN_HOST"
export CLUSTER_DIR="/path/on/cluster/irreducibly-human-work-lexicon"
export LOCAL_DIR="$HOME/irreducibly-human-work-lexicon-drafts"
export LEXICON_REPO="$HOME/path/to/irreducibly-human-work-lexicon"
export LEXICON_MODEL="MODEL_ID_YOU_CHOOSE"
export PROMPT_VERSION="gen-v1"
export WIKIPEDIA_DUMP="enwiki-YYYYMMDD"
export WIKIDATA_DUMP="wikidata-YYYYMMDD"
export OEWN_VERSION="oewn:2024"
```

Local layout: the four Python scripts and `assemble_bundles.py` sit in `$LOCAL_DIR`, the prompts in `$LOCAL_DIR/prompts/`, batch lists in `$LOCAL_DIR/batches/`, and each batch's working files in `$LOCAL_DIR/work/BATCH/`.

### Per batch

1. Set the batch name. Every later command uses it, so they paste unchanged.

```bash
export BATCH="batch_0001"
```

2. Push the batch list to the cluster.

```bash
rsync -av "$LOCAL_DIR/batches/$BATCH.tsv" "$CLUSTER_HOST:$CLUSTER_DIR/batches/"
```

3. Run the extraction job and wait for it to finish.

```bash
ssh "$CLUSTER_HOST" "cd $CLUSTER_DIR && sbatch --wait extract_batch.sbatch batches/$BATCH.tsv out/$BATCH"
```

4. Pull the cluster bundle down.

```bash
mkdir -p "$LOCAL_DIR/work/$BATCH" && rsync -av "$CLUSTER_HOST:$CLUSTER_DIR/out/$BATCH/cluster_bundle.jsonl" "$LOCAL_DIR/work/$BATCH/"
```

5. Add the local fields.

```bash
cd "$LOCAL_DIR" && python3 assemble_bundles.py "work/$BATCH/cluster_bundle.jsonl" "$LEXICON_REPO" "work/$BATCH/bundles.jsonl"
```

6. Generate drafts. If it's interrupted, rerun the same command; it skips concepts already drafted.

```bash
cd "$LOCAL_DIR" && python3 generate_drafts.py prompts/system.txt prompts/user_template.txt "work/$BATCH/bundles.jsonl" "work/$BATCH/drafts.jsonl"
```

7. Verify every draft.

```bash
cd "$LOCAL_DIR" && python3 verify_drafts.py "work/$BATCH/bundles.jsonl" "work/$BATCH/drafts.jsonl" "work/$BATCH/report.jsonl"
```

8. Render the drafts as markdown for review.

```bash
cd "$LOCAL_DIR" && python3 render_entries.py "work/$BATCH/bundles.jsonl" "work/$BATCH/drafts.jsonl" "work/$BATCH/report.jsonl" "work/$BATCH/entries.md"
```

9. Draw a reproducible random sample of 10 passing drafts for human review.

```bash
cd "$LOCAL_DIR" && python3 -c "import json,random,sys; rows=[l for l in open(sys.argv[1]) if json.loads(l)['status']=='pass']; random.seed(sys.argv[2]); sys.stdout.write(''.join(random.sample(rows, min(10, len(rows)))))" "work/$BATCH/report.jsonl" "$BATCH" > "work/$BATCH/review_sample.jsonl"
```

10. Write the batch manifest.

```bash
cd "$LOCAL_DIR" && python3 write_manifest.py "$BATCH" "work/$BATCH/report.jsonl" prompts/system.txt prompts/user_template.txt "$LEXICON_REPO" "work/$BATCH/manifest.json"
```

11. Push the batch results back to the cluster.

```bash
rsync -av "$LOCAL_DIR/work/$BATCH/" "$CLUSTER_HOST:$CLUSTER_DIR/drafts/$BATCH/"
```

## Part 5: Before the full run

Run a pilot of about 50 concepts first, chosen so you already know the right answers. Include easy technologies, abbreviations with several senses, soft skills, credentials, and look-alike pairs such as Java and JavaScript. Then generate the same 50 with empty Wikipedia, Wikidata, and WordNet fields. Compare the two runs on three counts: relations a reviewer judges unsupported, filled slots that should have been empty, and hypernym and hyponym reversals. If the grounded run isn't clearly better, fix the prompt or the bundles before spending money on 3,754 concepts. That comparison is also a small, clean result for the paper.

## Notes

- **Retry policy:** one retry, with the verifier's errors as feedback. More retries mostly teach the model to satisfy the verifier rather than the sources. Drafts that still fail are kept with their errors in `_meta.unresolved_errors`.
- **Verifier scope:** it confirms pointers exist and match, catches near-copies of Wikipedia text (nine or more consecutive words), rejects targets outside the neighbor list, and blocks `certifies` on non-credentials. It can't judge whether the model chose the right sense. The random review sample is what measures that.
- **Nothing merges automatically.** Drafts enter the lexicon's candidate queue as machine-drafted claims. Under your backing rule, a verified `source` pointer to Wikidata or WordNet can count as a source match. A `model_knowledge` claim cannot.
- **Licensing:** Wikipedia quotes in pointers are CC BY-SA. If the lexicon's definitions will carry a different license, store pointers in a separate evidence layer licensed to match Wikipedia.
- **Cost:** expect one to two model calls per concept. The Claude API's batch processing option is worth checking for a run this size; see https://docs.claude.com/en/api/overview.
