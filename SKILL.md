---
name: ai-author-platform-rules
description: Check a named platform's rules for publishing AI-authored work, including disclosure and payout requirements.
---

# AI-author platform rules

Answer the requested publishing-policy question with current official evidence and clearly identified gaps. This skill performs research; account creation, publishing, messaging, purchases and payout actions are outside this workflow.

## Find the applicable evidence

Read only the matching `data/<slug>.json` record. The dataset began on 2026-08-16; each record's `accessed` date is authoritative for that snapshot. Preserve the original [AI-AUTHOR.md](AI-AUTHOR.md) and license attribution.

Check the live official terms or help page before presenting a current verdict. A missing record is a research gap, not a prohibition: look up the official source when the request requires it. If it cannot be retrieved, identify what could not be verified and distinguish a dated snapshot answer from a current answer. Never invent a quote, platform rule or permission.

Read [references/SNAPSHOT.md](references/SNAPSHOT.md) only for historical coverage, omitted sources or the snapshot's copyright background. Use [schema.json](schema.json) when interpreting or updating the record format. Do not copy the snapshot summaries into current policy claims without verification.

## Answer and finish

Give the supported verdict, relevant account/disclosure/payout conditions, the steps reserved for a human or authorized entity representative, and citations with source and access dates. Distinguish source statements from interpretation. A missing AI-disclosure statement is not proof that no disclosure is required.

Keep KYC, identity documents, acceptance of agreements and authoritative account/payout decisions with the responsible human. A policy-research answer does not authorize external action. If a separate action is requested, use its applicable workflow, platform rules and existing authorization.

Completion means the question is answered from identified evidence, or the exact unresolved source gap and its effect on the verdict are stated. Do not stop solely because the local snapshot lacks the platform. Validate `data/` with `python3 tests/validate.py` only when records or their schema change; passing that check establishes data shape, not current policy accuracy.
