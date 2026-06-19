# Concept registry (canonical slugs)

The single source of truth for wiki article slugs. Every `wiki/<slug>.md` and
every `[[slug]]` cross-link MUST use a slug from this table. 46 concepts in 8
themes. "Sources" = the primary chapter note(s) to distil from; articles may also
draw on the synthesis notes [[00_framework_lifecycle]] / [[application_to_copilot]].

## Theme 1 — Lifecycle foundations
| slug | title | scope | primary sources |
|---|---|---|---|
| `corporate-lifecycle` | The Corporate Life Cycle | HUB: the six financial stages, the one idea, revenue-leads-earnings-lags; gateway to the whole wiki | cap_01, cap_02, 00_framework |
| `transition-gates` | Transition Gates | the gates between stages (lightbulb, product test, bar mitzvah, scaling, midlife, end game) + the events (VC/IPO/SEO/LBO/activism) that move firms across them | cap_04, cap_02 |
| `lifecycle-determinants` | Determinants of the Life-Cycle Curve | length, height, steepness, flatness and what drives each | cap_03 |
| `compressed-lifecycle-tech` | The Compressed (Tech) Life Cycle | "aging in dog years": steep rise, brief plateau, abrupt decline, near-zero salvage | cap_03, cap_15 |
| `measuring-lifecycle-stage` | Measuring a Firm's Stage | the classifier: age vs sector vs operating metrics, growth×margin 2×2, Mauboussin cash-flow signs, decline diagnostic | cap_03, cap_14, cap_02 |
| `moat` | Economic Moat | competitive advantage as the driver of the maturity plateau and the margin/ROIC fade | cap_03, cap_12 |

## Theme 2 — Corporate finance: investing & cost of capital
| slug | title | scope | primary sources |
|---|---|---|---|
| `corporate-finance-first-principles` | Corporate Finance First Principles | the three decisions (invest/finance/return) serving one objective; emphasis rotates by stage | cap_05, cap_01 |
| `hurdle-rate-and-investment-decision` | The Investment Decision & Hurdle Rate | invest only above the risk-adjusted hurdle rate; NPV/IRR; the dominant decision when young | cap_06, cap_05 |
| `cost-of-capital` | Cost of Capital (WACC) | building Ke and Kd into a blended, sourced, dynamic WACC; how it fades with maturity | cap_06 |
| `roic-and-excess-returns` | ROIC & Excess Returns | ROIC vs cost of capital, EVA/excess return, why growth only creates value at a positive spread | cap_06 |
| `real-options` | Real Options | optionality (delay/expand/abandon) as a value layer; promise and peril | cap_06, cap_13 |

## Theme 3 — Corporate finance: financing & cash return
| slug | title | scope | primary sources |
|---|---|---|---|
| `capital-structure-tradeoff` | The Debt–Equity Trade-off | tax shield + discipline vs bankruptcy + agency costs; the illusory vs real trade-off | cap_07 |
| `cost-of-debt-and-synthetic-rating` | Cost of Debt & Synthetic Ratings | Kd from coverage→rating→spread; the synthetic-rating loop feeding WACC | cap_07 |
| `debt-capacity-by-stage` | Debt Capacity Across the Life Cycle | optimal leverage, debt capacity rising to a mature peak then winding down; the matching principle | cap_07 |
| `cash-return-dividends-buybacks` | Cash Return: Dividends vs Buybacks | the cash-return decision, dividend stickiness, buyback flexibility, value-equivalence in form | cap_08 |
| `fcfe` | Free Cash Flow to Equity (FCFE) | FCFE as "potential dividends"; its sign across the life cycle | cap_08, cap_05 |
| `value-of-cash` | The Value of Cash | when cash trades at a discount; trapped cash as a liability in declining firms | cap_08 |

## Theme 4 — Valuation foundations
| slug | title | scope | primary sources |
|---|---|---|---|
| `intrinsic-vs-relative-valuation` | Intrinsic vs Relative Valuation (Value vs Price) | the value game vs the pricing game; two different processes/questions | cap_09 |
| `dcf-foundations` | DCF Foundations | the four inputs (cash flows, growth, risk, terminal value); equity vs firm DCF | cap_09 |
| `fcff` | Free Cash Flow to Firm (FCFF) | the firm-level cash flow discounted at WACC; FCFF vs FCFE | cap_09 |
| `terminal-value` | Terminal Value | the perpetuity, the r−g engine, why it dominates for growth firms, negative-g for decline | cap_09, cap_11 |
| `valuation-multiples` | Valuation Multiples | PE, EV/EBITDA, P/B, P/S, EV/Sales and the value drivers behind each; companion variables | cap_09 |
| `narrative-to-numbers` | Narrative to Numbers | value = story + numbers; tying every assumption to a story and back | cap_09, cap_10 |
| `uncertainty-in-valuation` | Handling Uncertainty | ranges, scenarios, simulation; estimation vs economic uncertainty; not false precision | cap_05, cap_09, cap_10 |

## Theme 5 — Valuing young & high-growth firms
| slug | title | scope | primary sources |
|---|---|---|---|
| `valuing-young-and-startups` | Valuing Young & Start-up Firms | top-down TAM→share→target margin→sales-to-capital→failure-adjusted DCF | cap_10 |
| `failure-probability` | Failure / Survival Probability | explicit p(failure), runway from cash burn, the survival-weighted value blend | cap_10 |
| `value-per-user` | Valuing Users, Subscribers & Customers | value = PV(existing users) + PV(new users) − corporate drag; CAC/churn | cap_15, cap_10 |
| `valuing-high-growth` | Valuing High-Growth Firms | growth fade, margin convergence, year-specific WACC, reinvestment via sales-to-capital | cap_11 |
| `big-market-delusion` | The Big Market Delusion | the trap of summing implausible market shares in a large TAM | cap_11 |

## Theme 6 — Valuing mature & declining firms
| slug | title | scope | primary sources |
|---|---|---|---|
| `valuing-mature` | Valuing Mature Firms | near-term cash flows dominate; status-quo vs restructured; EV/EBITDA emphasis | cap_12 |
| `value-of-control` | The Value of Control | P(change) × (optimal − status-quo value); the four restructuring levers | cap_12 |
| `sum-of-the-parts-octopus` | Sum-of-the-Parts (the Octopus) | valuing multi-business / multinational firms by segment; per-segment country risk | cap_12 |
| `valuing-declining-and-distressed` | Valuing Declining & Distressed Firms | negative growth, negative reinvestment, the going-concern × distress blend | cap_13 |
| `distress-probability` | Distress / Default Probability | cumulative distress odds from ratings / bond price / probit; distress-sale value | cap_13 |
| `equity-as-option` | Distressed Equity as an Option | equity as a call on firm assets (S, K=debt, t, σ) so DCF doesn't wrongly zero it | cap_13 |
| `liquidation-value` | Liquidation Value | the asset-sale floor; when shrinking/selling beats operating | cap_13 |

## Theme 7 — Investing across the life cycle
| slug | title | scope | primary sources |
|---|---|---|---|
| `investment-philosophies` | Investment Philosophies | value/growth/trading/arbitrage/indexing mapped to market-efficiency views and stages | cap_14 |
| `value-investing` | Value Investing | screeners, contrarians, buy-and-hold; the "lost decade"; Graham/Buffett tradition | cap_16 |
| `growth-investing` | Growth Investing | betting on the future; Peter Lynch; investing in youth | cap_15 |
| `activist-investing` | Activist Investing | unlocking trapped value in mature/declining firms; raises P(control) | cap_16, cap_17 |
| `private-equity-and-lbo` | Private Equity & LBOs | the three separable bets (leverage/tax, control/operating, going-private) | cap_17 |
| `pricing-game-vs-value-game` | The Pricing Game vs the Value Game | momentum/multiples vs intrinsic value; why both coexist; the trader–investor mix by stage | cap_14, cap_09 |

## Theme 8 — Managing across the life cycle
| slug | title | scope | primary sources |
|---|---|---|---|
| `managing-across-lifecycle` | Managing Across the Life Cycle | the CEO archetypes (Visionary→Liquidator) and the stage-fit / mismatch problem | cap_18 |
| `corporate-governance-lifecycle` | Corporate Governance & the Life Cycle | governance as the power to change management; dual-class entrenchment; how it shifts with age | cap_18 |
| `fighting-aging` | Fighting Aging | acceptance → renewal (facelift test) → revamp → rebirth; why most rejuvenation fails | cap_19 |
| `acting-your-age-serenity` | Acting Your Age (Serenity) | the book's spine: align policy with stage; denial→acceptance→reinvention; mismatched policy destroys value | cap_20, cap_05 |

---
**Total: 46 concepts.** A QA pass (W3) verifies every slug here has a `wiki/<slug>.md`,
every `[[slug]]` resolves, and no article is an orphan.
