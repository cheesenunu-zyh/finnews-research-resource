# Field-by-field public scope and source rights

Checked 2026-10-20. This release uses SEC as-filed numeric iXBRL elements and our
own normalized fact arrangement. It does not claim all issuer-submitted filings
are government-authored works or that payment for an API grants news rights.

| Field | Release decision | Basis |
|---|---|---|
| Current/prior financial numeric facts, periods, XBRL concept, unit, IDs | PUBLIC | Non-expressive facts; direct SEC original locator |
| Our normalized comparisons/schema/annotations | PUBLIC CC BY4.0 | New project contributions; facts themselves not monopolized |
| New LLM explanation using only the above numeric facts | PUBLIC, AI-generated, human review pending | No protected narrative in input; provider output rights do not validate truth |
| Issuer narrative, exhibit prose and logos | OMITTED | No blanket issuer-text redistribution claim |
| Old580 news originals/short quotes | RESTRICTED | FNSPID's dataset license cannot prove every publisher's downstream rights |
| Old580 open Agent explanations / embeddings | RESTRICTED | No inference that removal of quote solves derivative/contract scope |
| Old580 closed enum lineage | RESTRICTED | Non-expressive does not establish provider contract permission; omitted from ZIP |
| SIP prices and derived per-event labels | BYO / PRIVATE | Research entitlement is not public data redistribution authorization |
| Our benchmark software and safe aggregate diagnostics | PUBLIC | No row-level licensed prices/targets bundled |

Primary sources consulted:

- US Copyright Office, facts not protected, expression may be protected:
  https://www.copyright.gov/what-is-copyright/
- SEC privacy/security policy, Website Dissemination; this release still omits
  company narrative and never uses SEC logos or implies SEC endorsement:
  https://www.sec.gov/about/privacy-information
- SEC EDGAR XBRL data API:
  https://www.sec.gov/edgar/sec-api-documentation
- FNSPID original license is CC BY-NC4.0; it only covers rights licensors hold,
  not an independently verified publisher sublicense:
  https://github.com/Zdong104/FNSPID_Financial_News_Dataset/blob/main/LICENSE
- Alpaca Terms and Conditions: Content includes third-party news and market data:
  https://files.alpaca.markets/disclosures/library/TermsAndConditions.pdf
- DeepSeek output terms/accuracy responsibility:
  https://cdn.deepseek.com/policies/en-US/deepseek-open-platform-terms-of-service.html

The old580 field-level policy is applied to every event and every field class in
OLD_580_FIELD_RIGHTS.csv (4,060 rows). This is a deterministic release-policy
review, not a claim that a lawyer or human expert manually audited every field.
