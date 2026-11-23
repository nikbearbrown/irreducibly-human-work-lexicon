# Start here: kickoff messages for AI judges

Open **Codex** or **Claude Code** in a clone of `nikbearbrown/irreducibly-human-work-lexicon`, choose the model, and paste the message for that judge into a **fresh session**. For the next batch, start a new session and paste the same message again: the judge picks the first batch it hasn't finished.

The run is `replication/agreement/pilot-test`: definition pairs (stage P2) for 35 concepts, 144 requests in all.

| Judge id | Harness and model | Items |
|---|---|---|
| `codex` | Codex | 144 (3 batches) |
| `claude-fable` | Claude Code, Claude Fable | 144 (3 batches) |
| `claude-opus` | Claude Code, Claude Opus | 144 (3 batches) |
| `claude-sonnet` | Claude Code, Claude Sonnet | 13 (1 batch; it drafted the Sonnet edition, so it is excluded from items involving that edition and the reference) |
| `grok-bot` | Grok | 35 (1 batch; it drafted the Grok editions, so it is excluded from items involving them) |

## codex

```
You are AI judge "codex" in a study of how far independent model-written dictionary entries agree in meaning.
In this repository, run `git fetch origin && git switch -c judging/codex origin/grok-agreement-method`
(or `git switch judging/codex` if it exists). Then read replication/judging/AI-JUDGE-INSTRUCTIONS.md and follow
it exactly for RUN_DIR=replication/agreement/pilot-test with judge id codex. If results/codex/judge.json does not
exist yet, first record your model with the confirm-model command (section 1.1). Judge the first packet batch in
packets/codex/ that has no complete, validated result yet, and only that batch. Write the results, run the
validator until it passes, commit only replication/agreement/pilot-test/results/codex/ to judging/codex, and
push that branch. Open only your own packets/ and results/ folders. Do not open requests/, other judges' packets, any other branch, data/lexicon-parallel/, edition repositories or other judges'
results. Do not use the web. When done, tell me the batch number, the label counts, and anything unclear.
```

## claude-fable

```
You are AI judge "claude-fable" in a study of how far independent model-written dictionary entries agree in meaning.
In this repository, run `git fetch origin && git switch -c judging/claude-fable origin/grok-agreement-method`
(or `git switch judging/claude-fable` if it exists). Then read replication/judging/AI-JUDGE-INSTRUCTIONS.md and
follow it exactly for RUN_DIR=replication/agreement/pilot-test with judge id claude-fable. If
results/claude-fable/judge.json does not exist yet, first record your model with the confirm-model command
(section 1.1). Judge the first packet batch in packets/claude-fable/ that has no complete, validated result yet,
and only that batch. Write the results, run the validator until it passes, commit only
replication/agreement/pilot-test/results/claude-fable/ to judging/claude-fable, and push that branch. Open only your own
packets/ and results/ folders. Do not open requests/, other judges' packets, any other branch, data/lexicon-parallel/, edition repositories or other judges' results. Do not use the web.
When done, tell me the batch number, the label counts, and anything unclear.
```

## claude-opus

```
You are AI judge "claude-opus" in a study of how far independent model-written dictionary entries agree in meaning.
In this repository, run `git fetch origin && git switch -c judging/claude-opus origin/grok-agreement-method`
(or `git switch judging/claude-opus` if it exists). Then read replication/judging/AI-JUDGE-INSTRUCTIONS.md and
follow it exactly for RUN_DIR=replication/agreement/pilot-test with judge id claude-opus. If
results/claude-opus/judge.json does not exist yet, first record your model with the confirm-model command
(section 1.1). Judge the first packet batch in packets/claude-opus/ that has no complete, validated result yet,
and only that batch. Write the results, run the validator until it passes, commit only
replication/agreement/pilot-test/results/claude-opus/ to judging/claude-opus, and push that branch. Open only your own
packets/ and results/ folders. Do not open requests/, other judges' packets, any other branch, data/lexicon-parallel/, edition repositories or other judges' results. Do not use the web.
When done, tell me the batch number, the label counts, and anything unclear.
```

## claude-sonnet

```
You are AI judge "claude-sonnet" in a study of how far independent model-written dictionary entries agree in meaning.
In this repository, run `git fetch origin && git switch -c judging/claude-sonnet origin/grok-agreement-method`
(or `git switch judging/claude-sonnet` if it exists). Then read replication/judging/AI-JUDGE-INSTRUCTIONS.md and
follow it exactly for RUN_DIR=replication/agreement/pilot-test with judge id claude-sonnet. If
results/claude-sonnet/judge.json does not exist yet, first record your model with the confirm-model command
(section 1.1). Your packets already exclude items that involve your own model's edition. Judge
packets/claude-sonnet/batch-0001.jsonl (13 items). Write the results, run the validator until it passes, commit
only replication/agreement/pilot-test/results/claude-sonnet/ to judging/claude-sonnet, and push that branch. Open only your own
packets/ and results/ folders. Do not open requests/, other judges' packets, any other branch, data/lexicon-parallel/, edition repositories or other judges' results. Do not use the
web. When done, tell me the label counts and anything unclear.
```

## grok-bot

```
You are AI judge "grok-bot" in a study of how far independent model-written dictionary entries agree in meaning.
In this repository, run `git fetch origin && git switch -c judging/grok-bot origin/grok-agreement-method`
(or `git switch judging/grok-bot` if it exists). Then read replication/judging/AI-JUDGE-INSTRUCTIONS.md and follow
it exactly for RUN_DIR=replication/agreement/pilot-test with judge id grok-bot. If results/grok-bot/judge.json
does not exist yet, first record your model with the confirm-model command (section 1.1). Your packets already
exclude items that involve your own editions. Judge packets/grok-bot/batch-0001.jsonl (35 items). Write the
results, run the validator until it passes, commit only replication/agreement/pilot-test/results/grok-bot/ to
judging/grok-bot, and push that branch. Open only your own packets/ and results/ folders. Do not open requests/, other judges' packets, any other branch, data/lexicon-parallel/, edition
repositories or other judges' results. Do not use the web. When done, tell me the label counts and anything unclear.
```

## For the operator

- The key that unblinds A and B is **not** in this repository. Bear's private copy lives outside it. Scoring needs it: `agreement.py stats replication/agreement/pilot-test --keys <private>/pilot-test/keys/anon.jsonl`.
- Each judge pushes its own `judging/<id>` branch. The branches touch only `results/<id>/`, so they never conflict.
- To rebuild this run, use `replication/agreement/pilot-test/README.md`.
