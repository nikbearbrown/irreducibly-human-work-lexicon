#!/bin/bash
# One batch, end to end: bundles, drafts (Claude Code, headless, on your own plan), checks, readable entries, manifest.
# Usage: replication/run_batch.sh CONCEPTS.tsv WORK_DIR
#   CONCEPTS.tsv   a file from replication/concepts/ (pilot-36.tsv for the pilot)
#   WORK_DIR       where bundles.jsonl, drafts.jsonl, report.jsonl, entries.md and manifest.json go
# Needed for the bundle step (README.md, way A):
#   KAGGLE_DIR     <owner>/<dataset>/v<version>/dataset.zip for each allow-listed dataset
#   OBSERVATIONS   observations.jsonl from the data/kaggle-occurrence-evidence-20261030 branch
#   WORDNET_XML    english-wordnet-2025.xml.gz (Open English WordNet 2025)
# Optional:
#   LEXICON_REPO   a checkout of this repo at commit 91312fec (default: the checkout this script is in)
#   PYTHON         a Python with the `wn` package (default: python3)
#   STEP           bundles | drafts | all (default all)
#   RUN            grounded | ungrounded (default grounded; ungrounded empties wikipedia, wikidata, wordnet)
#   WITH_RECORD=1  also give the drafter the entry's own definition and identifiers (the gen-v1+record bundles)
#   WORKERS        parallel drafting calls (default 2)
# Drafting with another model instead of Claude Code: STEP=bundles, then scripts/render_prompts.py (README.md).
set -u
K=$(cd "$(dirname "$0")" && pwd)
CONCEPTS=$1
W=$2
REPO=${LEXICON_REPO:-$(cd "$K/.." && pwd)}
PY=${PYTHON:-python3}
RUN=${RUN:-grounded}
FLAG=""; [ "$RUN" = ungrounded ] && FLAG="--ungrounded"
export LEXICON_MODEL=${LEXICON_MODEL:-claude-opus-5-5} LEXICON_EFFORT=${LEXICON_EFFORT:-high}
export PROMPT_VERSION=${PROMPT_VERSION:-gen-v1${WITH_RECORD:++record}}
export WIKIPEDIA_DUMP=enwiki-20261001 WIKIDATA_DUMP=${WIKIDATA_DUMP:-"public API, live"} OEWN_VERSION=oewn:2025
mkdir -p "$W"
if [ "${STEP:-all}" != drafts ]; then
  echo "== bundles $(date)"
  "$PY" -I "$K/scripts/assemble_bundles.py" "$CONCEPTS" "$REPO" "$W/bundles.jsonl" \
    --kaggle "$KAGGLE_DIR" --allowlist "$K/kaggle-allowlist.tsv" --observations "$OBSERVATIONS" \
    --wordnet "$WORDNET_XML" ${WITH_RECORD:+--with-record} || exit 1
fi
[ "${STEP:-all}" = bundles ] && exit 0
echo "== drafts ($RUN) $(date)"
python3 "$K/scripts/generate_drafts.py" "$K/prompts/system.txt" "$K/prompts/user_template.txt" \
  "$W/bundles.jsonl" "$W/drafts-$RUN.jsonl" $FLAG --workers "${WORKERS:-2}"
code=$?
python3 "$K/scripts/verify_drafts.py" "$W/bundles.jsonl" "$W/drafts-$RUN.jsonl" "$W/report-$RUN.jsonl" $FLAG
python3 "$K/scripts/render_entries.py" "$W/bundles.jsonl" "$W/drafts-$RUN.jsonl" "$W/report-$RUN.jsonl" "$W/entries-$RUN.md"
python3 "$K/scripts/write_manifest.py" "$(basename "$CONCEPTS" .tsv)" "$W/report-$RUN.jsonl" \
  "$K/prompts/system.txt" "$K/prompts/user_template.txt" "$REPO" "$W/manifest-$RUN.json" > /dev/null
[ $code -eq 3 ] && { echo "== stopped at the usage limit $(date)"; exit 3; }
echo "== done $(date)"
