#!/bin/bash
# commit and push the full run, refresh the store backup
set -e
cd /workspace/lexicon-grok
git add -A && git commit -qm "${1:-Full run: more batches}" || true
git push -q origin grok-lex-pilot grok-lex-pilot:main
tar czf /cursor/stores/store-b70b09de-a0d7-4d1b-a3f4-5cf53c567708/lexicon/lexicon-grok-full.tgz --exclude=.git -C /workspace lexicon-grok
git log --oneline -1
