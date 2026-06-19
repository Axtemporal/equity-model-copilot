---
concept: spe-prms-reserve-categories
title: SPE-PRMS — Reserve Categories (1P/2P/3P)
theme: accounting-standard
applies_to: [oil_and_gas]
confidence: verified
status: draft
---

# SPE-PRMS — Reserve Categories (1P/2P/3P)

**What it is.** The Petroleum Resources Management System (SPE-PRMS) is the industry
framework that classifies an oil & gas company's barrels by commercial maturity and
confidence — **1P (Proved), 2P (Proved + Probable), 3P (Proved + Probable + Possible)**
— and separates commercially recoverable **Reserves** from not-yet-commercial
**Resources**, giving the upstream constraint that bounds every E&P production schedule.

## Core idea

An E&P company is worth the barrels it can **commercially produce**, so the valuation
cannot float on a free "price × volume" — it is bounded by how many barrels are
certified, and at what confidence. PRMS provides that certification vocabulary:

- **1P / Proved** — high confidence (≥90% probability the actual recovery equals or
  exceeds the estimate).
- **2P / Proved + Probable** — the **best-estimate base case** (~50% probability). This
  is the **standard anchor for NAV/DCF**.
- **3P / Proved + Probable + Possible** — the upside case (~10% probability).

Categories are additive only **within committed / in-development projects**; PRMS
explicitly warns against naively summing categories of different risk when aggregating a
portfolio probabilistically.

## Applies to sectors

- **Oil & Gas (E&P)** — directly. Build the model on the **2P reserve case** with 1P as
  the downside band and 3P as the upside, never on a perpetual growth rate. See
  [[reserve-based-nav]] and [[uop-depletion]].
- The logic runs closely parallel to mining's [[jorc-resources-and-reserves]] — same
  reserves-vs-resources discipline, different code.

## Mechanics / formulas

- `2P = Proved + Probable` is the base-case recoverable volume that caps cumulative
  production.
- **Reserves vs Resources:** Reserves are commercially recoverable **with a firm
  development intent** (typically within ~5 years). **Contingent Resources** are
  discovered but not yet commercial; **Prospective Resources** are undiscovered. PRMS
  gives risking mechanics — chance of development `Pd`, chance of discovery `Pg` — to
  risk or exclude these from a base-case reserve NAV.
- **SEC reserves differ:** the SEC recognizes **proved (1P) only**, priced at a trailing
  12-month average — a conservative subset. Do not equate SEC "proved" with the analyst
  2P base case.

## Modeling implications

- The reserve base is the **upstream constraint**: a reserve roll-forward (opening −
  production ± revisions ± acquisitions = closing) feeds the production schedule, which
  can never exceed recoverable reserves.
- The same reserve base drives **depletion** ([[uop-depletion]]) and the **terminal
  value** (field exhaustion + ARO, not a Gordon-growth tail).
- Pick **one base (2P)** and present 1P/3P as the band; never mix definitions within one
  case.

## Pitfalls & nuances

- **Do NOT model perpetual production growth** — barrels are finite; production declines
  against the certified reserve case.
- **Do NOT mix reserve definitions** — SEC proved (1P) ≠ analyst 2P base case ≠ 3P
  upside.
- **Do NOT count contingent/prospective resources in the base case unrisked.**
- **REFUTED — do NOT encode:** PRMS as "two independent axes with Reserves a strict
  subset of Resources, every barrel tagged on both dimensions." This failed verification;
  use the simple 1P/2P/3P + Reserves-vs-Resources framing above.

## Related concepts

- [[reserve-based-nav]] — valuing the reserve-bounded production profile
- [[uop-depletion]] — the reserve base also drives DD&A
- [[ifrs-6-ee-capitalization]] — how pre-reserve exploration cost is capitalized
- [[ev-2p-reserves]] — the reserve-based valuation multiple
- [[jorc-resources-and-reserves]] — the mining parallel

## Provenance
- Method cards: [[oil_and_gas]]
- Sources: [SPE-PRMS-2007 — Petroleum Resources Management System, Guide for Non-Technical Users (SPE, 2007)](https://www.spe.org/industry/docs/PRMS-Guide-for-Non-Technical-Users-2007.pdf); multiple: [CFI-EV2P — EV/2P ratio](https://corporatefinanceinstitute.com/resources/valuation/ev-2p-ratio)
- Confidence: ✅ verified (3-0)
