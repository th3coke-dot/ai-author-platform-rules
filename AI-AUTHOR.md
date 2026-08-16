# AI-AUTHOR

**Work is an AI agent.** This dataset, schema, tests, skill, and documentation were compiled by Work on **2026-08-16** from publicly posted terms, help articles, and government reports. No human lawyer reviewed the compilation before it was written to disk.

## What Work did

- Fetched official pages with a read-only HTTP client.
- Copied short **verbatim excerpts** into each record's `quote` (and `additional_sources[].quote`).
- Summarized nearby rules into `account_creator`, `ai_content_allowed`, `disclosure_rule`, `payout_kyc`, `copyright_notes`, and `human_must`.
- Set every `accessed` date to **2026-08-16**.
- Omitted any platform whose official page could not be fetched. Work did not invent quotes.

## What Work did not do

- Did not create accounts, sign up, publish, message anyone, or buy anything.
- Did not complete KYC, upload identity documents, or accept payment-processor agreements.
- Did not contact the platforms or their payment partners.
- Did not use SolvoOps, PartnerForge, or Scope2Plan.
- Did not give legal advice. Summaries are research notes, not counsel.

## Attribution of quotes

Every `data/*.json` record names the page the quote came from:

| Field | Meaning |
| --- | --- |
| `source_url` | Official page the primary `quote` was copied from |
| `accessed` | Date that page was fetched (2026-08-16) |
| `quote` | Short verbatim excerpt from that page |
| `additional_sources[]` | Extra official pages, each with its own URL, date, and quote |

US copyright notes that mention the January 2025 Part 2 report quote:

- https://copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf

Platform terms remain the property of their publishers. Quotes are used here for identification and commentary. This compilation is released under **CC-BY-4.0** (see `LICENSE`). That license covers Work's arrangement and summaries, not the underlying platform terms.

## Platforms omitted

**Fiverr** was on the target list. Official help and legal-portal pages returned a Cloudflare bot challenge and could not be read. Work omitted Fiverr rather than fabricate a quote.

## How a human should treat this file

A human — not Work — must own any account and any payout identity. Re-fetch the live terms before acting. If a quote and the live page disagree, the live page wins.
