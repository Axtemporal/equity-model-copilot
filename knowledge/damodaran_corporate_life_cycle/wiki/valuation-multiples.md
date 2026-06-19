---
concept: valuation-multiples
title: Valuation Multiples
theme: Valuation foundations
status: draft
---

# Valuation Multiples

**What it is.** A valuation multiple prices an asset by scaling its market value to an observable metric (earnings, book value, sales, EBITDA) and comparing that ratio to a peer group — the engine of relative valuation, or *pricing*; every multiple is a disguised DCF, an implicit function of the same growth, risk and cash-flow drivers, so using one soundly means knowing which fundamental drives it and controlling for differences across firms.

## Core idea

Relative valuation gives up on estimating intrinsic worth and instead trusts the market to price comparable assets right *on average*. It is popular because it is fast, makes fewer explicit assumptions, and stays close to market prices — and dangerous for exactly those reasons: the same ease lets analysts ignore risk, growth and cash-flow quality, import the market's mispricing, and manipulate the answer through biased multiple or peer choices. This is the *pricing* side of [[intrinsic-vs-relative-valuation]]; the discipline that tames it is the four-step process below.

The deep point is that **every multiple is derived from a DCF model**. Divide a stable-growth valuation by the relevant denominator and the multiple falls out as a function of growth, risk, payout and — for some — a quality variable. The dominant fundamental is the multiple's **companion variable**: the one input that most explains why one firm's multiple differs from another's.

## The four-step discipline

1. **Define it consistently and uniformly.** The numerator is either an *equity* value (price, market cap) or a *firm* value (enterprise value = equity + debt − cash); the denominator must match. Equity numerator → equity denominator (EPS, net income, book equity); firm numerator → firm denominator (revenues, EBIT, EBITDA, book capital). A consistent multiple matches levels (PE, EV/EBITDA); an inconsistent one (price/EBITDA — equity over firm) mis-ranks levered vs unlevered firms. Measure it *uniformly*: same trailing/forward convention, same accounting standards across the peer group.
2. **Make a timing choice.** Current (most recent annual), trailing (last four quarters), or forward (next year's expected) figure.
3. **Choose the peer group.** Narrow vs broad sector, similar size, same region or global. A true comparable is any firm with similar cash flows, growth and risk — *not* necessarily the same industry.
4. **Tell a story / control for differences.** Adjust for **risk** (higher risk → lower multiple), **growth** (higher growth → higher multiple) and **quality of growth** (higher ROC/ROE → higher multiple), via subjective adjustment, modified multiples (PEG), or sector regressions.

## The main multiples and their drivers

| Multiple | Level | Stable-growth form | Companion variable / key drivers |
|---|---|---|---|
| **PE** (price / earnings) | Equity | `Payout × (1+g) / (k_e − g)` | **Growth** (companion); risk, payout |
| **P/B (PBV)** (price / book equity) | Equity | `ROE × Payout × (1+g) / (k_e − g)` | **ROE** (companion); growth, risk, payout |
| **P/S (PS)** (price / sales) | Equity | `Net margin × Payout × (1+g) / (k_e − g)` | **Net margin** (companion); growth, risk, payout |
| **EV/EBITDA** (and EV/EBIT) | Firm | from `1/(WACC − g)`, adjusted for tax & reinvestment | Reinvestment rate, ROC, tax, growth, risk |
| **EV/FCFF** | Firm | `1 / (WACC − g)` | WACC, g |
| **EV/Sales** | Firm | analogous to PS at the firm level | Operating margin, reinvestment, growth, risk |

**PE variants:** current (most-recent EPS), trailing (last four quarters), forward (next year's expected). In a rising-earnings environment forward < trailing < current, so the variant chosen reveals the analyst's bias. The **PEG ratio** (PE ÷ expected growth) is a modified multiple that controls for the growth companion, but assumes a linear PE-growth relationship and equal risk across firms.

## Across the life cycle

The pricing metric rotates with age, tracking whatever the market currently fixates on (see [[pricing-game-vs-value-game]]):

- **Start-up:** EV/TAM, EV/users, EV/subscribers — there are no earnings, often no revenue (see [[value-per-user]], [[valuing-young-and-startups]]).
- **Young / high growth:** EV/forward sales, EV/Sales — revenue exists, margins don't yet.
- **Mature growth:** PEG, forward PE — earnings growth becomes the focus.
- **Mature stable:** PE, EV/EBITDA — earnings stability dominates (see [[valuing-mature]]).
- **Decline:** PE, EV/liquidation value, sometimes book value (see [[valuing-declining-and-distressed]], [[liquidation-value]]).

## Pitfalls & nuances

- **Consistency failure** — price/EBITDA and other equity-over-firm (or firm-over-equity) ratios are not interpretable across firms with different leverage.
- **Distribution blindness.** Multiples are bounded below at zero but unbounded above, so distributions are right-skewed; the **median** and percentiles (10/25/75/90) define "cheap" and "expensive" *relative to the market* — absolute thresholds are meaningless without the distribution.
- **Selection bias.** Negative-earnings firms drop out of PE samples, biasing the average **upward**; fixes are an aggregate PE (Σ market cap ÷ Σ net income) or the **earnings yield** (E/P), which is computable for loss-makers.
- **"Cheap" usually deserves it.** Low multiples typically reflect weak growth, high risk, or poor ROC — not hidden bargains. Book-value metrics in particular are overrated: sub-book stocks usually have low ROE or sit in declining, capital-heavy sectors.
- **Compliance:** a multiples-based target price is a *pricing* estimate with a disclaimer, never a recommendation.

## Related concepts

- [[intrinsic-vs-relative-valuation]] — multiples are the pricing game, distinct from DCF value
- [[pricing-game-vs-value-game]] — how the metric rotates by stage
- [[dcf-foundations]] — every multiple is a disguised DCF
- [[roic-and-excess-returns]] — ROE/ROC is the quality driver behind PBV and EV/EBITDA
- [[value-per-user]] — the pricing scalar when there are no earnings
- [[terminal-value]] — the `1/(r − g)` core inside firm multiples
- [[valuing-mature]] — where PE / EV/EBITDA dominate

## Provenance
- Chapter notes: [[cap_09_valuation_101]]
- Sources: local papers multiples.pdf ("Relative Valuation / Pricing First Principles"), valuesurvey.pdf; [January 2019 Data Update 9: The Pricing Game](https://aswathdamodaran.blogspot.com/2019/02/january-2019-data-update-9-pricing-game.html); Damodaran tool eqmult.xls ([pages.stern.nyu.edu](https://pages.stern.nyu.edu/~adamodar/pc/eqmult.xls))
- Raw (gitignored): reference/damodaran_clc/text/Ch9.txt, reference/damodaran_clc/text/multiples.txt
