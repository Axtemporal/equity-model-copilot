---
concept: sum-of-the-parts-octopus
title: Sum-of-the-Parts (the Octopus)
theme: Valuing mature & declining firms
status: draft
---

# Sum-of-the-Parts (the Octopus)

**What it is.** A valuation method for multi-business, multinational firms ("octopuses," whose tentacles each have different risk, growth, and cash-flow profiles): value each business and region separately with its *own* growth, margin, and discount rate, then add the pieces — instead of discounting consolidated cash flows at a single blended rate that silently misprices the mix.

## Core idea

DCF is **additive**: in theory you can value a conglomerate either *consolidated* (weighted-average risk parameters on consolidated cash flows) or *disaggregated* (value each part on its own inputs, then sum), and both should give the same answer. In practice the consolidated route fails for genuinely heterogeneous firms, because the value-weights drift as segments grow at different rates — a blended bottom-up beta computed today is stale next year. Sum-of-the-parts (SOTP) assigns each segment its own [[cost-of-capital]], growth, and margin, discounting risky/emerging-market streams harder than safe/developed ones, then aggregates and runs a fair-value bridge to equity.

SOTP is also the natural tool when you need the value of just *one* part — a division about to be sold, spun off, or split off — which is exactly the situation of divestiture-heavy mature and declining firms.

## Across the life cycle

- **Young / growth:** firms are usually single-business; SOTP rarely applies.
- **Mature:** the peak of conglomeration and multinational sprawl — the home of the octopus. Maturity is where firms diversify across businesses and geographies, so consolidated averaging does the most damage. See [[valuing-mature]].
- **Decline:** SOTP becomes the *break-up* tool — value each separable division, identify a "contaminated" unit dragging the rest, and check whether the sum of parts (net of consolidation benefits lost) beats the going concern. End-game holding companies are valued almost entirely as SOTP of their stakes. See [[valuing-declining-and-distressed]] and [[liquidation-value]].

## Mechanics / formulas

**SOTP procedure.**

```
Firm value = Σ value(business_i, region_i)   # each with its own growth, margin, discount rate
           − capitalized centralized corporate costs
           + cash and non-operating assets
           + fair value of cross-holdings
           − debt (incl. leases as debt)
           − minority interest (at fair, not book, value)
           ± synergy premium / conglomerate discount (judgment)
           → equity value, then adjust for options → value per share
```

**Per-segment discount rate and country risk.** Each tentacle gets its own risk profile. For multinationals, the governing rule is to judge risk by **country of operations, not country of incorporation** — otherwise a developed-market HQ escapes country-risk adjustment while still claiming emerging-market growth, a systematic over-valuation. Keep one currency consistent across each segment's cash flows and discount rate.

**Earnings hygiene.** Divisional earnings are corrupted by two things SOTP must correct: **centralized costs** allocated by arbitrary keys, and **intra-company transactions** priced at non-market transfer prices that shift profit between divisions. Capitalize and subtract genuine corporate overhead; restate transfer-distorted segment results.

**Cross-holdings and minority interest at fair value.** Minority stakes are often lazily carried at book and majority stakes fully consolidated with an outside share booked as minority interest. Restate both to **fair/market value** and value majority holdings separately before adding back.

**SOTP relative valuation.** No single firm is comparable to a unique conglomerate, so either widen the peer set and control for fundamentals, or run SOTP *relative* valuation — pick, per division, the EV multiple with the highest sector-regression R² (EV/EBITDA, EV/Revenues, EV/EBIT, or EV/Capital), value each, sum, then subtract capitalized corporate overhead. EV-family multiples ([[valuation-multiples]]) survive to the divisional level where net income/EPS do not.

## Pitfalls & nuances

- **The averaging argument.** Using consolidated margins, ROC, or beta as if today's mix weights hold forever — the core consolidated-valuation error.
- **Country of incorporation vs. operations.** The recurring multinational mistake; correct it explicitly in each segment's discount rate.
- **Book-value cross-holdings.** Carrying stakes at book understates or overstates equity; restate to fair value.
- **Arbitrary corporate-cost allocation.** Letting unallocated overhead distort divisional profitability before you value each part.
- **Mechanically asserting a break-up gap.** A break-up only creates value when the sum-of-parts gain outweighs lost economies of scale, internal-capital-market access, and synergies — model those costs, don't ignore them.

## Related concepts

- [[valuing-mature]] — the stage where octopuses cluster
- [[valuing-declining-and-distressed]] — SOTP as the break-up / end-game tool
- [[liquidation-value]] — SOTP-by-liquidation as the asset-sale floor
- [[cost-of-capital]] — each segment carries its own, with country risk by operations
- [[valuation-multiples]] — EV-family multiples chosen per division
- [[value-of-cash]] — cash and cross-holdings in the EV→equity bridge
- [[dcf-foundations]] — the additivity that makes SOTP legitimate
- [[fcff]] — the firm-level cash flow valued per segment

## Provenance
- Chapter notes: [[cap_12_valuing_mature]]
- Sources: [The Octopus: Valuing Multi-business, Multi-national Companies (Damodaran, SSRN 1609795)](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/octopus.pdf); [Valuing Mature Businesses (Ch12 slides, CLC companion site)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/CLC.htm); [EV multiples by industry (vebitda.xls)](https://pages.stern.nyu.edu/~adamodar/pc/datasets/vebitda.xls)
- Raw (gitignored): reference/damodaran_clc/text/Ch12.txt
