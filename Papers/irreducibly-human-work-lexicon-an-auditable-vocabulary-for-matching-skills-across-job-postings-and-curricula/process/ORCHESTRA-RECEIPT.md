# Paper Orchestra draft-stage receipt

- Target snapshot: `nikbearbrown/irreducibly-human-work-lexicon@3cd82a454877e83d3f7eb989136de1d234e9944e`. `git archive`, `python3 -I tools/lexicon.py validate`, and `python3 -I scripts/summary_stats.py` verified the audited counts. These are artifact counts, not benchmark results.
- Tool source: local Google Research PaperOrchestra commit `d9bae99`. Executed the real `OutlineAgent.run` and `SectionWritingAgent.run` with explicit no-network operator adapters, using Codex-written responses to the generated requests. This is an adapted two-stage draft run, **not** a full stock CLI run. Neither adapter imported a provider SDK or sent any data out; requests and figures were handled locally.
- Provenance: `inputs/{idea_sparse,experimental_log}.md` were staged from the pinned evidence. `outline-request.json` records the upstream outline agent's formatted five-part prompt. `outline.json` is the upstream outline stage's output. `citation_map.json` contains a manually assembled and checked citation map, not the output of the upstream literature agent. `sections-request.json` records the upstream section agent's prompt, system instruction, figure paths, and chosen adapter.
- `manuscript-v0.2-pre-critique.md` is the section-writer response in its editable form. A local Pandoc conversion created the equivalent LaTeX response; the upstream LaTeX parser and section agent emitted `raw_draft_paper.tex`. A local `pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error` check produced a four-page PDF with both figures.
- Upstream automated literature search, plotting, and content refinement were **not** invoked. The figures were independently generated and supplied to the writer. Separate Critique review and author approval follow, and were not faked or included in the upstream run.
- A future stock run would require an approved Gemini/Vertex writer because the first stage directly calls Gemini; external literature also needs separately approved API/network access. Provider and Scholar secrets should be supplied only to an isolated, reviewed run. Upstream Scholar code logs its API key during import, so remove that behavior before any credentialed execution. Disable generating executable plot code unless specifically needed and isolated. Compile without shell escape and use a fresh output directory.

| Artifact | SHA-256 |
|---|---|
| `outline.json` | `9ed6243bdb191e39dfbe108191508467a7f5ddebcfe52b4fda4cd493a51db89e` |
| `manuscript-v0.2-pre-critique.md` | `15c5be91688d61859152954b09966b8f3fc14fe5acb4679edaaf9134b06e33b8` |
| `raw_draft_paper.tex` | `c10fc1505d312602bc8d83fe55a471e0a68dfc49ed412fe2583b03e8e9e2980c` |

This public package includes the sanitized inputs, outline, independent review, and archived pre-Critique Markdown. Run logs and intermediate LaTeX request files are not required to reproduce the inventory. The archived Markdown points to the current figure assets; the independent review describes the original rendering.
