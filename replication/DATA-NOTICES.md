# Data in this folder

The scripts and pages here are under the repository's MIT licence. `bundles/` and `handout/` also hold source material from other projects, under the terms below. Because they include adapted Wikipedia text, **`bundles/` and `handout/` are distributed under CC BY-SA 4.0**.

| Material | Where | Source and licence |
|---|---|---|
| Wikipedia article text | `wikipedia` in each bundle; the grounded hand-out messages | English Wikipedia, the revision current on 2026-10-01 for each article. Markup was stripped and the text cut at about 3,000 words. Authors: Wikipedia contributors; each article's history is at `https://en.wikipedia.org/w/index.php?oldid=<revision_id>`. [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). |
| Wikidata items | `wikidata` in each bundle | Wikidata, fetched from the public API on 2026-11-20; each item carries its revision id. [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). |
| WordNet senses | `wordnet` in each bundle | [Open English WordNet](https://github.com/globalwordnet/english-wordnet) 2025, under its own licence, CC BY 4.0. |
| Job-posting snippets | `examples` in each bundle | Kaggle datasets on the allow-list (`kaggle-allowlist.tsv`), under the licence each publisher declared. In the pilot bundles: 57 snippets CC0, 44 MIT, 24 Apache 2.0, 13 CC BY 4.0. Each snippet id names its dataset, version, file and record. |
| Lexicon records | `concept` and `neighbors` | This repository at commit `91312fec`; O*NET material as described in the top-level `THIRD-PARTY-NOTICES.md`. |

No other Kaggle dataset was used. The allow-list leaves out every dataset whose licence is non-commercial, share-alike, GPL or unclear.
