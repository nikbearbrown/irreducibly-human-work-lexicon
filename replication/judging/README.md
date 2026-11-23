# Judging: how models and people judge agreement between lexicon editions

This folder supports the agreement study in [../AGREEMENT-METHOD.md](../AGREEMENT-METHOD.md). Several language models each drafted their own edition of the Irreducibly Human Work Lexicon. Judges compare two editions' entries for the same concept and say how far they **mean** the same thing.

| You are | Read |
|---|---|
| A **person** asked to judge (about 100 items, a few hours) | [HUMAN-JUDGE-INSTRUCTIONS.md](HUMAN-JUDGE-INSTRUCTIONS.md) |
| An **operator** starting an AI judge | [START-HERE-AI-JUDGE.md](START-HERE-AI-JUDGE.md): one kickoff message per judge, for the `pilot-test` run |
| An **AI judge** (Codex; Claude Fable, Sonnet or Opus; Grok; or a future model) | [AI-JUDGE-INSTRUCTIONS.md](AI-JUDGE-INSTRUCTIONS.md) |
| An **AI agent running a person's session** (the person said "I'm a human judge") | [INTERVIEWER-PROTOCOL.md](INTERVIEWER-PROTOCOL.md) |

All three use **one output schema** ([judgment.schema.json](judgment.schema.json)) and **one validator**:

```bash
python3 replication/scripts/agreement.py validate RUN_DIR --judge-id YOUR_JUDGE_ID
```

## The pieces

| Path | What it is |
|---|---|
| `prompts/system.txt`, `prompts/P1.txt` … `prompts/P6.txt` | The exact judge prompts (AGREEMENT-METHOD.md 4.2). Every request already carries its rendered `system` and `user` text. |
| `judgment.schema.json` | The one result-line schema, for models and people alike |
| `RUN_DIR/requests/<stage>/batch-NNNN.jsonl` | Every blinded request (written by `agreement.py run`) |
| `<PRIVATE>/keys/anon.jsonl` | Which edition is A and which is B. **Never committed here** (it is gitignored and kept privately by the operator). Only `stats` and registering new model judges need it. |
| `RUN_DIR/judges.json` | Registered **slots** (and human judges): type, harness, editions drafted, seed |
| `RUN_DIR/results/<judge id>/judge.json` | A model judge's identity: provider, model name, **exact version** (required, or flagged as unknown), and the model string as the harness reports it. The judge id is `<provider>-<model name>-<version>`, for example `anthropic-claude-fable-5-2`. |
| `RUN_DIR/packets/<slot>/batch-NNNN.jsonl` | An AI judge's work, by slot, with self-exclusion already applied |
| `RUN_DIR/humans/<judge_id>/sample.jsonl`, `progress.json` | A person's seeded sample and where they stopped |
| `RUN_DIR/results/<judge_id>/...` | What a judge hands in |

`RUN_DIR` is the run folder Bear names. The first one is `replication/agreement/pilot-test`. Results are committed on a branch `judging/<judge id>` and pushed. Nothing is ever pushed to `main`, and nothing is force-pushed.

## Rules everyone follows

- **Blind.** Never open the keys, `data/lexicon-parallel/` or the `grok-lexicon-parallel-data` branch, any edition repository, or another judge's `results/`. Judge only what the packet or sample shows.
- **Self-exclusion.** A model never judges an item that involves an edition it drafted. Registration enforces this (AI-JUDGE-INSTRUCTIONS.md, section 2).
- **Independence.** Judge each item on its own. Don't compare your answers with anyone else's.
- **Meaning, not wording.** Two texts agree if they say the same thing, however differently they say it.
