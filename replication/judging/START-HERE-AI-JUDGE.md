# Start here: kickoff messages for AI judges

Open **Codex** or **Claude Code** in a clone of `nikbearbrown/irreducibly-human-work-lexicon`, choose the model, and paste the message for that slot into a **fresh session**. For the next batch, start a new session and paste the same message again: the judge picks the first batch it hasn't finished.

The run is `replication/agreement/pilot-test`: definition pairs (stage P2) for 35 concepts, 144 requests in all.

**Every judge records its exact model version.** Its judge id is `<provider>-<model name>-<version>`, for example `anthropic-claude-fable-5-2`, and its results, branch and commits use that id. A model that cannot state its version must say so (`--version-unknown`). Its results are then **flagged** and kept out of the primary panel until you confirm the version. It is never guessed.

| Slot | Harness and model | Items |
|---|---|---|
| `codex` | Codex | 144 (3 batches) |
| `claude-fable` | Claude Code, Claude Fable | 144 (3 batches) |
| `claude-opus` | Claude Code, Claude Opus | 144 (3 batches) |
| `claude-sonnet` | Claude Code, Claude Sonnet | 13 (1 batch; it drafted the Sonnet edition, so items involving that edition and the reference are excluded) |
| `grok-bot` | Grok | 35 (1 batch; it drafted the Grok editions, so items involving them are excluded) |

## codex

```
You are an AI judge in slot "codex" in a study of how far independent model-written dictionary entries agree in
meaning. In this repository, read replication/judging/AI-JUDGE-INSTRUCTIONS.md and follow it exactly for
RUN_DIR=replication/agreement/pilot-test, slot codex, provider openai, model name codex.
First, state your exact model version as your harness or system information shows it. If you cannot see it,
say so and use --version-unknown. Never guess. Then run the confirm-model step (section 1.1) and use the judge
id it prints (for example openai-codex-X-Y) for your results, your branch judging/<judge id>, and your commit.
Judge the first packet batch in packets/codex/ that has no complete, validated result under your judge id yet, and only that batch. Write the results, run the validator until it passes, commit only
replication/agreement/pilot-test/results/<judge id>/ to judging/<judge id>, and push that branch.
Open only packets/codex/ and your own results/ folder. Do not open requests/, other judges' packets or results,
any other branch, data/lexicon-parallel/ or edition repositories. Do not use the web.
When done, tell me your judge id and version, the batch number, the label counts, and anything unclear.
```

## claude-fable

```
You are an AI judge in slot "claude-fable" in a study of how far independent model-written dictionary entries agree in
meaning. In this repository, read replication/judging/AI-JUDGE-INSTRUCTIONS.md and follow it exactly for
RUN_DIR=replication/agreement/pilot-test, slot claude-fable, provider anthropic, model name claude-fable.
First, state your exact model version as your harness or system information shows it. If you cannot see it,
say so and use --version-unknown. Never guess. Then run the confirm-model step (section 1.1) and use the judge
id it prints (for example anthropic-claude-fable-X-Y) for your results, your branch judging/<judge id>, and your commit.
Judge the first packet batch in packets/claude-fable/ that has no complete, validated result under your judge id yet, and only that batch. Write the results, run the validator until it passes, commit only
replication/agreement/pilot-test/results/<judge id>/ to judging/<judge id>, and push that branch.
Open only packets/claude-fable/ and your own results/ folder. Do not open requests/, other judges' packets or results,
any other branch, data/lexicon-parallel/ or edition repositories. Do not use the web.
When done, tell me your judge id and version, the batch number, the label counts, and anything unclear.
```

## claude-opus

```
You are an AI judge in slot "claude-opus" in a study of how far independent model-written dictionary entries agree in
meaning. In this repository, read replication/judging/AI-JUDGE-INSTRUCTIONS.md and follow it exactly for
RUN_DIR=replication/agreement/pilot-test, slot claude-opus, provider anthropic, model name claude-opus.
First, state your exact model version as your harness or system information shows it. If you cannot see it,
say so and use --version-unknown. Never guess. Then run the confirm-model step (section 1.1) and use the judge
id it prints (for example anthropic-claude-opus-X-Y) for your results, your branch judging/<judge id>, and your commit.
Judge the first packet batch in packets/claude-opus/ that has no complete, validated result under your judge id yet, and only that batch. Write the results, run the validator until it passes, commit only
replication/agreement/pilot-test/results/<judge id>/ to judging/<judge id>, and push that branch.
Open only packets/claude-opus/ and your own results/ folder. Do not open requests/, other judges' packets or results,
any other branch, data/lexicon-parallel/ or edition repositories. Do not use the web.
When done, tell me your judge id and version, the batch number, the label counts, and anything unclear.
```

## claude-sonnet

```
You are an AI judge in slot "claude-sonnet" in a study of how far independent model-written dictionary entries agree in
meaning. In this repository, read replication/judging/AI-JUDGE-INSTRUCTIONS.md and follow it exactly for
RUN_DIR=replication/agreement/pilot-test, slot claude-sonnet, provider anthropic, model name claude-sonnet.
First, state your exact model version as your harness or system information shows it. If you cannot see it,
say so and use --version-unknown. Never guess. Then run the confirm-model step (section 1.1) and use the judge
id it prints (for example anthropic-claude-sonnet-X-Y) for your results, your branch judging/<judge id>, and your commit.
Your packets already exclude items involving your own edition(s). Judge packets/claude-sonnet/batch-0001.jsonl (13 items). Write the results, run the validator until it passes, commit only
replication/agreement/pilot-test/results/<judge id>/ to judging/<judge id>, and push that branch.
Open only packets/claude-sonnet/ and your own results/ folder. Do not open requests/, other judges' packets or results,
any other branch, data/lexicon-parallel/ or edition repositories. Do not use the web.
When done, tell me your judge id and version, the batch number, the label counts, and anything unclear.
```

## grok-bot

```
You are an AI judge in slot "grok-bot" in a study of how far independent model-written dictionary entries agree in
meaning. In this repository, read replication/judging/AI-JUDGE-INSTRUCTIONS.md and follow it exactly for
RUN_DIR=replication/agreement/pilot-test, slot grok-bot, provider xai, model name grok.
First, state your exact model version as your harness or system information shows it. If you cannot see it,
say so and use --version-unknown. Never guess. Then run the confirm-model step (section 1.1) and use the judge
id it prints (for example xai-grok-X-Y) for your results, your branch judging/<judge id>, and your commit.
Your packets already exclude items involving your own edition(s). Judge packets/grok-bot/batch-0001.jsonl (35 items). Write the results, run the validator until it passes, commit only
replication/agreement/pilot-test/results/<judge id>/ to judging/<judge id>, and push that branch.
Open only packets/grok-bot/ and your own results/ folder. Do not open requests/, other judges' packets or results,
any other branch, data/lexicon-parallel/ or edition repositories. Do not use the web.
When done, tell me your judge id and version, the batch number, the label counts, and anything unclear.
```

## For the operator

- A flagged judge (`...-version-unknown`) can be confirmed later: once you know the version, rerun `confirm-model` with `--version`, which creates the versioned id. Then rewrite the result files under that id and validate them. Or leave it flagged. `stats` marks it either way.
- The key that unblinds A and B is **not** in this repository. Scoring needs it: `agreement.py stats replication/agreement/pilot-test --keys <private>/pilot-test/keys/anon.jsonl`.
- Each judge pushes its own `judging/<judge id>` branch and touches only `results/<judge id>/`, so branches never conflict. Two versions of the same model in one slot get two judge ids, and both are kept.
- To rebuild this run, use `replication/agreement/pilot-test/README.md`.
