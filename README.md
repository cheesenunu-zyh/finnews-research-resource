# FinNews Research Resource — Equity Core 0.1

Source-linked company financial states and reproducible evidence-to-factor research.

## Download the real company subset

[Download Equity Core 0.1](finnews-equity-core-v0.1.zip)

156 real company filing events · 13 US equities · 2021–2023 · 1,200 numeric
facts · 156 deterministic states · **36 newly generated real LLM analyses**.
Rules are not relabelled LLM outputs. This new numeric-filing subset is separate
from the private 580-family news study.

The archive contains original SEC source locators, units and periods, frozen
requests and responses, economic states, same-material frozen Qwen vectors,
price-alignment contracts, a standard-library benchmark, licenses and limitations.
It does not require our E: drive, AutoDL, an API key or new model calls.

## Verify and run

```sh
python -I -S verify_release.py finnews-equity-core-v0.1.zip
# Unzip the release into a fresh directory, then:
python -I -S run.py reproduce
python -I -S run.py query --asset AAPL
python -I -S run.py verify
```

Stock-price benchmark reproduction requires an **authorized** historical price
CSV; no raw SIP prices or per-event target labels are redistributed. The release
includes exact trading-calendar, maturity, split-adjustment and right-censoring
requirements and an optional entitled-data adapter. It never fetches sealed
2024–2025 data to fill missing targets.

## Research status

Historical Agent analyses were generated in 2026 and are retrospective, not
contemporaneous 2021–2023 forecasts. Mechanically verified financial comparisons
are distinct from human-reviewed economic explanations. Human interpretation
review remains pending. The small matched benchmark has **not established
independent LLM semantic alpha**; negative baselines are included.

An automated isolated environment reproduced the release. This is not a claim
of independent external human reproduction, a completed forward investment
trial, or validated trading value.

## Scope and licenses

New code/documentation: MIT. Project annotation/arrangement: CC BY 4.0. Numeric
facts themselves are not claimed as our copyright; preserve source attribution.
Issuer narrative, commercial news, private news embeddings, credentials and raw
licensed equity prices are omitted. See `FIELD_RIGHTS.md` and
`DATASET_LICENSE.json` inside the archive. A code license does not relicense
third-party source material.

The immutable archive SHA-256 is:

`64d5c17eec084e1c387d76b022a1f19b9416761f0575517da99acea798ecd864`

[Interactive browser resource](https://finnews-research-open-v1.upbeat-mouse-5935.chatgpt.site/)
provides company inspection. The GitHub mirror is a separate distribution route;
the browser site may reject automated clients through its hosting security layer.

## Quality and benchmark supplement

[Download the quality supplement](QUALITY_SUPPLEMENT_PUBLIC.zip)
includes explicit tasks and field definitions, a source-first review interface
for the 36 filing cases, 288 initially empty human-Gold cells, objective numeric
checks, and an authorized-price CSV validator. Mechanical source checks are not
human semantic judgments. No human Gold has been silently prefilled. The old
40-family commercial-news review is a separate private cohort; its source text
and model explanations are not redistributed.

## Independent download mirror

This public repository is `cheesenunu-zyh/finnews-research-resource`. The root archives preserve the exact
released bytes; `SHA256SUMS` covers both archives. Git commit URLs provide
version-pinned retrieval. This repository is not a DOI or an archival guarantee.
