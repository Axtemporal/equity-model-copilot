# Note schema — Sector modeling rules (method cards)

This file defines the **mandatory structure** every sector method card
(`<sector>.md`) must follow, so the cards are homogeneous, machine-navigable, and
safe to feed into the assumption layer. It is a maintenance contract, not content.

## Purpose

One card per sector capturing the rules a model must follow **beyond** the generic
three-statement + projection + DCF framework — the industry-native drivers,
mandatory KPIs/disclosures, peculiar accounting treatments, how the operational
structure must adapt, and the common modeling pitfalls. These cards extend the
per-line method library in [`docs/calibration_and_knowledge_notes.md`](../../docs/calibration_and_knowledge_notes.md)
with sector overlays.

## Conventions

- **Language:** English (technical valuation/accounting terms kept market-standard;
  Brazilian-specific terms — CFEM, JCP, sinistralidade, ANS — kept in Portuguese
  with a gloss).
- **Distillation, not copying:** paraphrase in our own words. Numbers/examples may
  be cited as facts with provenance, but never paste source prose verbatim. The
  proprietary `Example models/` and `Knowledge Base/` archives must never be quoted.
- **Provenance is mandatory and confidence is explicit.** Every load-bearing claim
  carries a `> source:` callout pointing to an entry in [`_sources.md`](_sources.md),
  and a confidence tag. Three tiers:
  - ✅ **Verified** — confirmed by the deep-research adversarial pass (vote ≥ 2-0)
    against a primary or strong secondary source.
  - 🟡 **Seed** — single-source or unverified-but-reputable; usable as a starting
    point, confirm before hardcoding.
  - ⚠️ **To verify** — industry-standard practitioner knowledge included for
    completeness but NOT yet sourced in this research. Never present as verified,
    never attach a fabricated citation. These mark the round-2 research agenda.
- **Method, not numbers.** Encode the *method* (e.g. "spread per route × utilization"),
  not the point-in-time figures (a bank's 2025 WACC, a spot price). Specific numbers
  appear only as dated illustrations with provenance, flagged as time-sensitive.
- **Cross-links:** link sibling cards with `[[sector_slug]]` and the cross-cutting
  accounting note with `[[_accounting_ifrs_overlays]]` where one exists.
- **No investment advice:** describe methods and KPIs; never turn them into a
  recommendation or target price. (Project compliance rule.)

## Required sections (in order)

```markdown
---
sector: <human name>
slug: <file_slug>
pilots_examples: <BR/global tickers this applies to>
coverage: <verified | partial | seed-only>
key_standards: <SPE-PRMS, IFRS 6, IAS 41, IFRS 15, ...>
status: draft
---

# <Sector> — sector method card

## 1. Core thesis
One paragraph: how this sector breaks the generic "revenue = price × volume"
frame and what the single most important sector-specific idea is.

## 2. Operational drivers (the revenue/COGS build)
The driver tree that replaces the generic line. State the identity(ies)
explicitly (e.g. Revenue = capacity × utilization × (price − feedstock cost)).
Tag each driver with confidence + source.

## 3. Mandatory KPIs & regulatory disclosures
The metrics the market and regulators expect, defined and with how they are
computed. Brazilian regulator specifics (ANP, ANS, CVM, ANEEL...) noted.

## 4. Peculiar accounting / normative rules
The accounting treatments that differ from the generic model (capitalization,
depletion, revenue recognition, fair value, contra-revenue...). Cite the
standard. Note IFRS vs US-GAAP divergence where relevant.

## 5. Model structure adaptation
How the engine's tabs/templates must adapt — granularity (per asset / per BU /
per product family), extra schedules, the self-adapting-granularity differential.

## 6. Modeling pitfalls
Concrete mistakes to avoid, including any claims that were REFUTED in research
(state them explicitly as "do NOT encode").

## 7. Confidence & open questions
What is verified vs. seed vs. to-verify, and the specific round-2 research agenda
for this sector.
```

## Length
No artificial cap, but these are operational cards, not essays — aim for tight,
actionable bullets over prose. Completeness on the verified parts; honesty about
the gaps.
