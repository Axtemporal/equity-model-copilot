---
concept: cfem-royalty
title: CFEM — Financial Compensation for Mineral Exploitation
theme: brazil-specific
applies_to: [metals_mining]
confidence: verified
status: draft
---

# CFEM — Financial Compensation for Mineral Exploitation

**What it is.** **CFEM** (*Compensação Financeira pela Exploração de Recursos Minerais*)
is the Brazilian mining royalty — a constitutionally-mandated compensation levied by
mineral on **gross sale revenue minus the taxes on its commercialization** (iron ore at
3.5%) — that must be modeled **between gross and net revenue**, not as flat operating
expense, because it scales directly with price and volume.

## Core idea

CFEM is a government take on mineral extraction, established by **Art. 20, §1º of Brazil's
1988 Constitution** and owed to states, municipalities and federal entities for the
economic use of mineral resources. Because it moves with realized price and volume, it
behaves like a **revenue-linked royalty, not a fixed cost** — so it belongs in the
**gross-to-net revenue bridge**, alongside the cost-curve economics ([[c1-aisc-mining]]).

Rates vary by mineral, and the model should treat the rate as an **input keyed to the
mineral** so it adapts to the issuer's commodity mix.

## Applies to sectors

- **Metals & mining** — directly; a Brazilian miner's revenue bridge.
- Conceptually parallel to O&G **government take** (royalties + special participation),
  which sits between gross revenue and netback in that sector ([[reserve-based-nav]]).

## Mechanics / formulas

- **Calculation base (sales):** `gross sale revenue − taxes levied on commercialization`
  (a net-of-commercialization-taxes base) — it sits in the gross-to-net bridge. ✅
- **CFEM = rate(mineral) × base.** ✅
- **Rates by mineral** ✅ (with a statutory **maximum cap of 4%**):
  - **Iron ore (ferro): 3.5%**
  - Bauxite / manganese / niobium / rock salt: 3%
  - Diamond / other: 2%
  - Gold: 1.5%
  - Construction aggregates / ornamental rocks: 1%

## Modeling implications

- Model CFEM as a **revenue-linked royalty line** (rate × base, by mineral) in the
  gross-to-net bridge — never as a flat opex %.
- Use the **net-of-commercialization-taxes** base, consistent with the ANM definition.
- Keep the rate as a **per-mineral input** so the engine adapts to the issuer's commodity
  mix (a multi-mineral miner like Vale carries different rates per stream).

## Pitfalls & nuances

- **Do NOT model CFEM as flat opex** — it scales with price and volume; it is a
  revenue-linked royalty in the gross-to-net bridge.
- **Do NOT use a single blended rate** for a multi-mineral miner — rate is per-mineral
  (iron ore 3.5% differs from copper/gold/bauxite).
- Nuance: the **exact post-2018-reform base wording** (whether transport/insurance are
  deductible) and the ANM's discretion to reduce rates for low-performing deposits were
  *abstention-killed on the session limit (not refuted)* — the ANM FAQ base definition
  (gross revenue minus commercialization taxes) is the 3-0 verified anchor; finer base
  mechanics are a round-4 confirm.

## Related concepts

- [[c1-aisc-mining]] — the cost stack CFEM sits beside
- [[reserve-based-nav]] — the gross-to-net bridge in the mining NAV; O&G government-take parallel
- [[jorc-resources-and-reserves]] — the reserve base being exploited

## Provenance
- Method cards: [[metals_mining]]
- Sources: [ANM-CFEM — ANM FAQ, Compensação Financeira pela Exploração Mineral (gov.br)](https://www.gov.br/anm/pt-br/acesso-a-informacao/perguntas-frequentes/contribuicao-financeira-pela-exploracao-mineral-2013-cfem) (constitutional basis Art. 20 §1º; rates by mineral incl. iron ore 3.5% + 4% cap; base = gross sale revenue minus commercialization taxes — all 3-0)
- Confidence: ✅ verified (round 3, 3-0 on constitutional basis, iron-ore 3.5% + rate table + 4% cap, and the calculation base)
