#!/usr/bin/env python3
"""Write a provenance manifest for one batch.

Usage: python3 write_manifest.py BATCH REPORT.jsonl SYSTEM_PROMPT.txt USER_TEMPLATE.txt LEXICON_REPO MANIFEST.json
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys


def main(batch, report, system, template, repo, out):
    rows = [json.loads(line) for line in open(report) if line.strip()]
    prompt_hash = hashlib.sha256((open(system).read() + open(template).read()).encode()).hexdigest()
    git = subprocess.run(["git", "-C", repo, "rev-parse", "--verify", "HEAD"],
                         capture_output=True, text=True)
    commit = git.stdout.strip() if git.returncode == 0 else "unknown"
    manifest = {
        "batch": batch,
        "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "lexicon_commit": commit,
        "model": os.environ.get("LEXICON_MODEL"),
        "prompt_version": os.environ.get("PROMPT_VERSION"),
        "prompt_sha256": prompt_hash,
        "sources": {
            "wikipedia_dump": os.environ.get("WIKIPEDIA_DUMP"),
            "wikidata_dump": os.environ.get("WIKIDATA_DUMP"),
            "wordnet": os.environ.get("OEWN_VERSION"),
        },
        "concepts": len(rows),
        "passed_verifier": sum(r["status"] == "pass" for r in rows),
    }
    with open(out, "w") as f:
        json.dump(manifest, f, indent=2)
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main(*sys.argv[1:7])
