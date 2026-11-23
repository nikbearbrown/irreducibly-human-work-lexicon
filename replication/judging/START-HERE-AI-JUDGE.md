# Start here: one prompt for any AI judge

Paste the prompt below, **unchanged**, into a fresh session of any model: in an agent harness opened in a clone of `nikbearbrown/irreducibly-human-work-lexicon`, or in a plain chat. The model works out its own provider, model name and exact version. A script then decides which items it may judge (self-exclusion from [drafters.tsv](drafters.tsv)) and builds its packets. Paste the same prompt again in a new session for each later batch: the model resumes where it left off.

## The prompt (for every model)

```
You are an AI judge in a study of how far independent, model-written dictionary entries for work concepts
agree in meaning. Do not use the web.

1. Identify yourself from your harness or system information, not from memory: your provider (the company),
   your model name (without provider or version), your exact version, and the model string exactly as shown.
   If you cannot see an exact version, say so plainly; you will use --version-unknown. Never guess a version.

2. If you cannot run shell commands in this repository, reply only with:
   NO SHELL
   provider: ...
   model name: ...
   version: ... (or: unknown)
   model string: ...
   and wait. The operator will paste your items.

3. Otherwise, in this repository, read replication/judging/AI-JUDGE-INSTRUCTIONS.md and follow it exactly with
   RUN_DIR=replication/agreement/pilot-test, starting from origin/grok-agreement-method: compute your judge id,
   switch to the branch judging/<your judge id>, and run the join command (it decides which items you get and
   resumes if you already joined). Judge only the next batch it names, write your results, run the validator
   until it passes, commit only your own results/ and packets/ folders, and push your judging/<judge id> branch.
   Open only your own packets/ and results/ folders.

4. When done, report your judge id, provider, model name and version, any flags join printed, the batch
   number, your label counts, and anything in the instructions that was unclear.
```

## Chat-only models (no shell)

If the model replied `NO SHELL`, the operator runs the commands from a clone of the repository, on the branch `judging/<judge id>`:

1. **Join for it**, using what the model stated:
   `python3 replication/scripts/agreement.py join replication/agreement/pilot-test --provider P --model-name M --version V --model-reported "<its model string>" --harness chat`
   (`--version-unknown` instead of `--version V` if it couldn't see its version). Note the judge id it prints.
2. **Export one paste block:**
   `python3 replication/scripts/agreement.py export-packet replication/agreement/pilot-test --judge-id <judge id> --write packet.txt`
3. **Paste** all of `packet.txt` into the same chat. The model replies with one `jsonl` block, one line per item.
4. **Import:** save the whole reply as `reply.txt` and run
   `python3 replication/scripts/agreement.py import replication/agreement/pilot-test --judge-id <judge id> --reply reply.txt`.
   It validates the reply and stores it as `results/<judge id>/batch-NNNN.jsonl`. If anything is missing or invalid, it stores nothing and says what to fix.
5. **Commit and push** `results/<judge id>/` and `packets/<judge id>/` to `judging/<judge id>` (AI-JUDGE-INSTRUCTIONS.md, section 7). For the next batch, repeat steps 2 to 5.

## What each judge gets in `pilot-test`

144 definition pairs over 35 concepts (stage P2), in batches of 50:

| Judge | Items |
|---|---|
| any model that drafted no edition (it may still be flagged `same_family_as_drafter`) | 144 (3 batches) |
| Claude Sonnet 5.5 (drafted the Sonnet edition and most of the reference lexicon) | 13 (1 batch) |
| any Grok (drafted the Grok editions) | 35 (1 batch) |
| a model whose version is unknown but whose provider and model match a drafter | the drafter's share, **flagged** |

## For the operator

- To add a new drafter, add a row to [drafters.tsv](drafters.tsv) **before** that model joins.
- Flags printed by `join` are kept in `results/<judge id>/judge.json`. `stats` reports `version_unknown` judges separately.
- The key that unblinds A and B is **not** in this repository. Scoring needs it: `agreement.py stats replication/agreement/pilot-test --keys <private>/pilot-test/keys/anon.jsonl`.
- `requests/exclusions.json` lists, for each edition under an obfuscated token, which requests involve it, so that `join` can exclude drafters without the key. It is obfuscation, not secrecy: a judge that read it together with `drafters.tsv` and the script could learn which items involve which edition. Judges are told not to open it.
- Each judge pushes its own `judging/<judge id>` branch and touches only its own folders, so branches never conflict.
