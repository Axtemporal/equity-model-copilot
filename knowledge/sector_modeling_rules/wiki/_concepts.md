# Concept registry (canonical slugs)

The single source of truth for sector-wiki article slugs. Every `wiki/<slug>.md`
and every `[[slug]]` cross-link MUST use a slug from this table. 25 concepts in 4
themes. "Cards" = the per-sector method card(s) the concept overlays; "Conf." =
current confidence tier (✅ verified / 🟡 seed / ⚠️ to-verify).

## Theme 1 — Accounting standards (cross-sector overlays)
| slug | title | scope | cards | conf. |
|---|---|---|---|---|
| `ias-41-biological-assets` | IAS 41 — Biological Assets at Fair Value | FVLCTS measurement, changes through P&L, consumable vs bearer split | agriculture, agri_inputs, pulp_paper | ✅ |
| `ias-41-bearer-plants` | IAS 41 — Bearer Plant Amendment | June 2014 amendment: bearer plants → IAS 16; produce stays IAS 41; why row crops & pulp eucalyptus are NOT bearer plants | agriculture, pulp_paper | ✅ |
| `spe-prms-reserve-categories` | SPE-PRMS — Reserve Categories (1P/2P/3P) | proved/probable/possible, Reserves vs Resources, 2P as the NAV/DCF anchor | oil_and_gas | ✅ |
| `jorc-resources-and-reserves` | JORC / CRIRSCO — Resources vs Reserves | resource/reserve categories, conversion mapping, Modifying Factors, Inferred exclusion | metals_mining | ✅ |
| `ifrs-6-ee-capitalization` | IFRS 6 — Exploration & Evaluation Capitalization | the E&E accounting-policy exemption; successful-efforts vs full-cost read per issuer | oil_and_gas, metals_mining | ✅ |
| `ifrs-15-performance-obligations` | IFRS 15 — Over-time vs Point-in-time Recognition | five-step model; service obligations over time vs goods at a point; contra-revenue | education, tech_saas, auto | ✅ |
| `ias-2-inventory-costing` | IAS 2 — Inventory Costing | FIFO / weighted-average only (LIFO banned); weighted-avg cost-flow lag; LCNRV as a separate mechanism | fuel_distribution | ✅ |
| `ias-38-rd-capitalization` | IAS 38 vs ASC 730 — R&D / Software Capitalization | IFRS develop-capitalize-if-six-criteria vs US-GAAP expense-as-incurred; read the issuer's framework | tech_saas, auto | ✅ |
| `ifrs-16-leases` | IFRS 16 — Leases, EBITDA-AL & the EV Bridge | RoU + lease liability; EBITDA vs EBITDA-AL; leases as debt in the bridge; FCFF deducts lease payments | (all) | 🟡 |

## Theme 2 — Operational driver patterns (replacing generic price × volume)
| slug | title | scope | cards | conf. |
|---|---|---|---|---|
| `spread-based-revenue` | Spread-Based Revenue Modeling | margin = product price − feedstock cost, per route; capacity × utilization; for processors not price-takers on output alone | petrochemicals, fuel_distribution | ✅ |
| `reserve-based-nav` | Reserve-Based NAV / DCF | production bounded by the certified reserve curve; SOTP per field/asset vs consolidated FCFF; the NAV-vs-DCF default question | oil_and_gas, metals_mining | 🟡 |
| `uop-depletion` | Units-of-Production Depletion | depletion/DD&A as a function of production over reserves, not straight-line; reserve basis is a policy choice; ARO interaction | oil_and_gas, metals_mining | ✅ |
| `inventory-effect-fuel` | The Inventory Effect (cost-flow lag) | weighted-average COGS lagging spot → holding gains/losses; recurring vs reported margin; import-parity driver | fuel_distribution | ✅ |
| `arr-roll-forward` | ARR / MRR Roll-Forward | recurring-revenue corkscrew: opening + new + expansion − contraction − churn; revenue derives from the ARR base | tech_saas | 🟡 |
| `biological-assets-in-model` | Modeling IAS 41 Fair-Value Swings | separating the fair-value re-measurement line from cash operating results; hectares × yield underneath | agriculture, pulp_paper | ✅ |
| `mid-cycle-normalization` | Mid-Cycle / Normalized Earnings | cyclical valuation on normalized mid-cycle margins/spreads in a separate block, not a spot snapshot | petrochemicals, steel, metals_mining | ✅ |

## Theme 3 — Sector KPIs & disclosures
| slug | title | scope | cards | conf. |
|---|---|---|---|---|
| `ev-2p-reserves` | EV/2P Reserve Multiple | enterprise value per barrel of 2P reserves; a reserve-based cross-check | oil_and_gas | 🟡 |
| `ebitda-al-ifrs16` | EBITDA-AL (after-lease EBITDA) | the IFRS-16-adjusted profitability metric; why it matters for lease-heavy sectors | (all) | 🟡 |
| `saas-unit-economics` | SaaS Unit Economics | NRR, gross/logo churn, CAC, LTV, LTV/CAC, CAC payback, Rule of 40, cohort retention | tech_saas | ⚠️ |
| `c1-aisc-mining` | C1 Cash Cost & AISC | mining cost stack: C1 cash cost, all-in sustaining cost, position on the global cost curve, grade/teor; + provisional pricing | metals_mining | 🟡 |
| `mlr-sinistralidade` | MLR / Sinistralidade | medical loss ratio as the core margin driver for health plans; the Brazilian analogue and ANS context | healthcare | 🟡 |
| `r-per-m3-fuel` | R$/m³ — Fuel Distribution Profitability | profitability measured per cubic metre, not % of (pass-through) revenue; recurring margin | fuel_distribution | ✅ |

## Theme 4 — Brazil-specific rules
| slug | title | scope | cards | conf. |
|---|---|---|---|---|
| `jcp-effective-tax` | JCP & Effective Tax Rate (Brazil) | juros sobre capital próprio as a tax-deductible distribution; effect on the effective tax rate; method card called for in the spec | (all BR) | ⚠️ |
| `cfem-royalty` | CFEM — Financial Compensation for Mineral Exploitation | the Brazilian mining royalty by mineral (iron ore 3.5%); base = gross revenue − commercialization taxes; gross-to-net bridge | metals_mining | ✅ |
| `fies-prouni-mechanics` | FIES & PROUNI — Education Financing | the public student-financing programmes and how they drive intake, ticket and receivables for BR education | education | ⚠️ |

## Notes
- A slug tagged ⚠️ may not have an article yet, or may have a skeleton article that
  states the gap honestly. The `index.md` status column tracks which are written.
- When a future research round upgrades a claim, update the article's frontmatter
  `confidence:`, the inline tag, and this table together.
- New concepts get a row here FIRST, then an article. Never orphan a `[[slug]]`.
