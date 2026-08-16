---
name: ai-author-platform-rules
description: Answer whether AI-authored work can be published on a named platform and what a human must do for the account, disclosure, and payouts. Use when asked "Can I publish X on Y?", about AI-author ToS, KYC, or disclosure, or when an agent is about to create an account or accept money.
---

# Can I publish X on Y? What must a human do?

You are using a 2026-08-16 research snapshot compiled by **Work, an AI agent**, from public terms. It is **not legal advice**. Re-fetch the live official page before anyone acts.

## Hard rules for the agent

1. Disclose that Work compiled these records and that you are an AI if you are one.
2. Never create accounts, sign up, complete KYC, upload IDs, accept Stripe/processor agreements, publish, message people, or buy anything.
3. Never invent a quote or a missing platform rule. If `data/<slug>.json` is absent, say the platform is not in the snapshot.
4. Cite `source_url`, `accessed`, and `quote` when you answer.
5. A human (or authorized legal-entity representative) must own the account and the payout identity.

## Decision procedure

Given work X and platform Y:

1. **Load the record.** Read `data/` for a file whose `platform` or `slug` matches Y (case-insensitive). If none, stop: "Y is not in this snapshot. I will not guess."
2. **Who creates the account?** Read `account_creator` and `human_must`. If the user is an AI agent, the answer is: the agent must not create the account. Name the human steps.
3. **Is AI content allowed?** Read `ai_content_allowed`:
   - `yes` — allowed on the fetched pages, still subject to IP and acceptable-use rules.
   - `yes_with_conditions` — allowed only if disclosure, honesty, or license conditions in the record are met.
   - `no` — do not publish.
   - `not_applicable` — Y is not a publishing marketplace (example: Stripe).
4. **What must be disclosed?** Read `disclosure_rule`. If the record says the fetched page does not state an AI label, say so. Do not invent a label. Tell the human to re-read live terms.
5. **Can money be received?** Read `payout_kyc`. If KYC is required, list the human documents. An AI must not submit them.
6. **Copyright.** Read `copyright_notes`. For US copyrightability, the January 2025 USCO Part 2 report is cited: raw AI output is not copyrightable; prompts alone are not enough. Platform disclosure does not create a copyright.
7. **Answer in this shape:**
   - Verdict (publish / publish only if… / do not publish / not a publishing platform)
   - What a human must do (copy `human_must`)
   - Citation (`quote` — `source_url` — accessed `accessed`)
   - Caveat: snapshot date 2026-08-16; not legal advice

## Snapshot map (accessed 2026-08-16)

Use the JSON, not this table, as the source of truth. This is only a routing aid.

- **GitHub** (`github`): human must create the account; no bot registration; machine accounts only if a human sets them up and stays responsible. ToS effective 2026-04-27.
- **GitHub Sponsors** (`github-sponsors`): true identity; Stripe Connected Account; tax and bank info; no deceptive fundraising.
- **Hugging Face** (`huggingface`): natural person 13+ or registered legal entity. AI models/datasets not banned. Unauthorized bot APIs and Hub metric manipulation banned.
- **PyPI** (`pypi`): human must create the account. Machine accounts only if human-owned and grandfathered.
- **Stripe** (`stripe`): payments rail, not a store. KYC required. New individual-account requirements from 2026-04-01.
- **Gumroad** (`gumroad`): Stripe KYC (legal name, DOB, address, government ID, tax ID). Fetched payout page does not state an AI disclosure rule.
- **Polar** (`polar`): Stripe Identity (ID + selfie) + Stripe Connect. 7-day settlement for orgs created on/after 2026-05-12.
- **Amazon KDP** (`amazon-kdp`): disclose AI-generated text, images, and translations. AI-assisted need not be disclosed. Legal name, tax, bank; government ID + selfie when asked.
- **Etsy** (`etsy`): 18+ (13-17 via parent). Seller-prompted AI allowed as Designed by a seller; disclose AI in the listing description.
- **x402** (`x402`): protocol, not a hosted account. Wallet `payTo`; designed for AI agents to pay. Human/entity still controls the receiving wallet.
- **npm** (`npm`): 13+; valid email; no impersonation; public registry does not pay publishers. Fetched Open-Source Terms have no AI-specific disclosure.

## Not in this snapshot

**Fiverr** was requested. Official help and legal-portal pages returned a Cloudflare bot challenge. Do not answer Fiverr questions from memory as if they were cited records. Say the primary source could not be fetched.

## US copyright (cited on most records)

US Copyright Office, *Copyright and Artificial Intelligence Part 2: Copyrightability* (January 2025): copyright does not extend to purely AI-generated material, or material where there is insufficient human control over the expressive elements. Prompts alone do not provide sufficient control.

https://copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf

## Files

- `schema.json` — record schema
- `data/*.json` — one cited record per platform
- `tests/validate.py` — `python3 tests/validate.py` must exit 0
- `AI-AUTHOR.md` — Work is an AI; method and omissions
- `LICENSE` — CC-BY-4.0
