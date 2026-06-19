---
concept: equity-as-option
title: Distressed Equity as an Option
theme: Valuing mature & declining firms
status: draft
---

# Distressed Equity as an Option

**What it is.** The recognition that, with limited liability, the equity of a heavily indebted firm is a **call option on the firm's assets** — struck at the face value of debt, expiring when the debt comes due — so equity retains value even when the firm "owes more than it owns"; it is an analytical overlay that stops a pure DCF from wrongly zeroing distressed equity, never a recommendation.

## Core idea

For a money-losing, heavily indebted firm, a going-concern DCF can produce a near-zero or negative equity value. But equity holders have **limited liability**: they keep the residual if asset value exceeds debt and walk away (losing only their stake) if it does not. That payoff — `V − D if V > D, else 0` — is exactly the payoff of a **call option** on the firm's asset value with a strike equal to the face value of debt. So even when firm value sits *below* the face value of debt, the equity option retains value from two sources: the **time premium** (the time until the debt matures, during which assets might recover above the debt) and the chance assets rise above the debt face before maturity — exactly as a deep-out-of-the-money traded option commands a positive price.

This is the late-life member of the [[real-options]] family and the reason stock in effectively-bankrupt firms still trades at a positive price.

## Mechanics / formulas

Map the firm onto the Black–Scholes inputs:

| Option input | Firm-valuation analogue |
|---|---|
| Underlying asset value S | Value of the firm's assets |
| Strike price K | **Face value of outstanding debt** |
| Time to expiry t | Life / face-value-weighted duration of the debt |
| Variance σ² | Variance in firm value |
| Riskless rate r | Treasury rate matching the option life |

Equity = `S·N(d₁) − K·e^(−rt)·N(d₂)`; the debt is then `S − equity`.

**Worked example.** S = $100M, σ = 40% (σ² = 0.16), K = $80M zero-coupon debt, t = 10y, r = 10% → d₁ = 1.5994, d₂ = 0.3345 → equity ≈ **$75.94M**; debt = 100 − 75.94 = $24.06M; implied debt rate = `(80/24.06)^(1/10) − 1 = 12.77%`. **Troubled case:** drop S to $50M (firm owes more than it owns) → equity *still* ≈ **$30.44M** (d₁ = 1.0515, d₂ = −0.2135).

**Estimating the inputs.** Estimate firm value and its variance by cumulating the market values of debt + equity (or value the assets via FCFF/WACC); estimate firm-value variance from `σ²_firm = w_e²σ_e² + w_d²σ_d² + 2·w_e·w_d·ρ_ed·σ_e·σ_d` (use similarly-rated bonds, or the industry average, where debt isn't traded); for the option life use the face-value-weighted debt duration.

**Risk is the equity holder's friend.** Because option value rises with the volatility of the underlying, *more uncertainty in firm value raises equity value* in a distressed firm — the opposite of the healthy-firm intuition. This also explains the **debt–equity agency conflict**: equity (the option holder) prefers more risk while lenders prefer less, and the conflict worsens (risk-shifting / asset-substitution) as operations deteriorate and leverage rises.

## Across the life cycle

- **Young firms:** equity already behaves option-like (limited liability over an uncertain future), but the framing is usually a survival-weighted DCF — see [[failure-probability]].
- **Mature firms:** firm value comfortably exceeds debt, the option is deep in-the-money, and the option lens adds little over a straight DCF.
- **Decline / distress (this concept):** the only place the overlay materially changes the answer — when the face value of debt approaches or exceeds firm value and a DCF would otherwise zero out equity.

## Pitfalls & nuances

- **It is an analytical estimate, not advice.** Surface it with a disclaimer; it does not say to buy distressed equity.
- **Hard-to-estimate inputs.** Firm-value variance and debt duration are noisy; treat point estimates with humility (general [[real-options]] caveats apply).
- **Don't generalize "risk helps value."** It is specific to the option holder in a distressed firm; in ordinary cash-flow valuation, more risk lowers value.
- **Renegotiation re-cuts the split.** Distressed-debt restructurings can re-divide the debt / equity-option / common-stock claims "overnight," so the static option split is a snapshot.
- **Double-counting with the distress blend.** The option overlay and the going-concern × distress blend ([[valuing-declining-and-distressed]]) are alternative lenses on the same problem — apply one coherently, don't stack them naïvely.

## Related concepts

- [[real-options]] — equity-as-call is the late-life member of the option family
- [[valuing-declining-and-distressed]] — the parent valuation this overlay corrects
- [[distress-probability]] — the alternative probability-weighted lens on the same firm
- [[liquidation-value]] — the asset value S that strikes against the debt face
- [[capital-structure-tradeoff]] — the agency conflict the option lens explains
- [[cost-of-debt-and-synthetic-rating]] — debt value as the complement of the equity option
- [[fcff]] — one way to estimate the underlying firm-asset value
- [[uncertainty-in-valuation]] — the volatility input that gives the option value

## Provenance
- Chapter notes: [[cap_13_valuing_declining]]
- Sources: [Valuing Equity in Firms in Distress (Damodaran, eqnotes/distress.pdf)](https://pages.stern.nyu.edu/~adamodar/pdfiles/eqnotes/distress.pdf); [Valuing Distressed and Declining Companies (Damodaran, NewDistress.pdf)](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/NewDistress.pdf); [Valuing Declining and Distressed Companies (SSRN 1428022)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1428022)
- Raw (gitignored): reference/damodaran_clc/text/Ch13.txt
