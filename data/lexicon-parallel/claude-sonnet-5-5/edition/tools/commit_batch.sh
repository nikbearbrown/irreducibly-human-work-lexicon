#!/bin/bash
# usage: tools/commit_batch.sh "<batch label>"   -- build, validate, commit, push, then print drafted/pending
set -e
cd "$(dirname "$0")/.."
python3 -I tools/edition.py build
python3 -I tools/edition.py validate
python3 -I - <<'PY'
import json
c = json.load(open("coverage.json"))
print("progress:", c["drafted"], "drafted /", c["pending"], "pending")
PY
D=$(python3 -I -c "import json;c=json.load(open('coverage.json'));print(c['drafted'])")
git add -A
git commit -q -F - <<MSG
$1

$D of 2,895 drafted; validation passes.

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
MSG
git push -q origin main
git log --oneline | head -1
