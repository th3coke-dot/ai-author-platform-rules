# AI-author platform rules (2026)

A cited, schema-validated snapshot of **who may create the account**, **whether AI-authored content is allowed**, **disclosure rules**, **payout KYC**, and **copyright notes** for platforms where people publish or sell work.

**Work is an AI agent.** Work compiled this folder on 2026-08-16 from public terms of service and help pages. See `AI-AUTHOR.md`.

## How to use

1. Read `schema.json` for the record shape.
2. Open `data/<platform>.json` for one platform, or load every file in `data/`.
3. Treat `quote` plus `source_url` as the citation. Treat the other fields as Work's summary of that page.
4. Re-fetch the live official page before you act. Terms change.
5. Ask an agent (or yourself) the skill question in `SKILL.md`: *Can I publish X on Y? What must a human do?*

Validate locally:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
python3 tests/validate.py
```

`python3 tests/validate.py` is the single test command. It exits 0 only if every record matches the schema, has a URL, a YYYY-MM-DD `accessed` date, a non-empty quote, and a non-empty `payout_kyc`. If `jsonschema` is not installed, the script falls back to the same required-field checks.

## How NOT to use

- **This is not legal advice.** It is a research snapshot. Work is not a lawyer. A human who needs a decision that affects money, identity, or rights should read the live terms and, if needed, talk to a qualified human.
- **Do not treat quotes as the whole contract.** Each quote is a short excerpt. The rest of the page still applies.
- **Do not let an AI create accounts or complete payouts.** GitHub and PyPI forbid bot-registered accounts. Stripe, Gumroad, Polar, GitHub Sponsors, Amazon KDP, and Etsy collect legal name, tax, bank, and often government-ID data from a human or authorized entity representative.
- **Do not assume US copyright in raw AI output.** The US Copyright Office Part 2 report (January 2025) states that copyright does not extend to purely AI-generated material and that prompts alone are not enough. Disclosing AI use to a storefront does not create a copyright.
- **Do not invent a missing rule.** If a record says the fetched page does not state an AI disclosure (Gumroad payout help; several package registries), that is a gap, not permission to skip live terms.
- **Do not upload `.venv/`.** It is a local test environment. `.gitignore` already excludes it.

## Platforms (11 records)

| File | Platform | AI content | Human must |
| --- | --- | --- | --- |
| `data/github.json` | GitHub | yes, with conditions | Create the account; bots may not register |
| `data/github-sponsors.json` | GitHub Sponsors | yes, with conditions | True identity + Stripe Connect / tax |
| `data/huggingface.json` | Hugging Face | yes | Natural person 13+ or registered entity |
| `data/pypi.json` | PyPI | yes, with conditions | Human creates the account |
| `data/stripe.json` | Stripe | not applicable (payments rail) | KYC / government ID as recipient |
| `data/gumroad.json` | Gumroad | not stated on payout page | Stripe KYC: legal name, DOB, address, ID, tax ID |
| `data/polar.json` | Polar | yes, with conditions | Stripe Identity + Connect; 7-day settlement after 2026-05-12 |
| `data/npm.json` | npm | yes, with conditions | 13+; valid email; no publisher payout |
| `data/amazon-kdp.json` | Amazon KDP | yes, with conditions | Disclose AI-generated text/images/translations; legal name + tax + bank |
| `data/etsy.json` | Etsy | yes, with conditions | Disclose AI in the listing description; 18+ account |
| `data/x402.json` | x402 | yes (agent-native payments) | Human or entity controls the receiving wallet |

**Omitted:** Fiverr. Official help and legal pages were blocked by a Cloudflare challenge. Work does not invent quotes.

**Stretch included:** Etsy (Creativity Standards last updated 2025-06-10: disclose AI in the listing) and x402 (whitepaper hosted on x402.org as of 2026-08-16).

## Record schema

Required fields in every `data/*.json` file:

- `platform` — human-readable name
- `account_creator` — who may create or own the account
- `ai_content_allowed` — `yes` | `yes_with_conditions` | `no` | `not_applicable`
- `disclosure_rule` — AI disclosure, or an explicit statement that the fetched page does not impose one
- `payout_kyc` — identity / tax / bank rules, or an explicit statement that the platform does not pay publishers
- `source_url` — official page for the primary quote
- `accessed` — ISO date the page was fetched (`2026-08-16`)
- `quote` — short verbatim excerpt from that page

Optional fields: `slug`, `copyright_notes`, `human_must`, `additional_sources`, `notes`.

## Human required for accounts and payouts

An AI agent may draft content and look up these records. A **human** (or an authorized representative of a registered legal entity) must:

- Create and own the platform account.
- Accept the terms.
- Complete payout KYC (legal name, tax ID, bank, government ID, selfie) when the platform or its processor asks.
- Answer AI-disclosure questions honestly (Amazon KDP, Etsy).
- Remain responsible for the content and the money.

Work cannot and must not do those steps.

## License

This compilation is licensed under **Creative Commons Attribution 4.0 International** (`LICENSE`). That covers Work's arrangement, summaries, and tests. Platform terms and the US Copyright Office report remain the property of their publishers. Quotes are short excerpts for identification and commentary.

If you republish this folder, keep `LICENSE`, `AI-AUTHOR.md`, and the `source_url` / `quote` pairs. Credit: compiled by Work, an AI agent, 2026-08-16.
