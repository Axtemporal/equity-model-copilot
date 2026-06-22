# AI-Assisted Financial Modeling System

A modeling copilot for Brazilian equities: turns the analyst's manual inputs into standardized Excel models (three-statement IFRS + sector-specific operational modeling), with the AI proposing assumptions line by line for user approval.

## Reference documents (read before any work)

1. `docs/project_specification.md`: spec v0.2 with all closed decisions
2. `docs/calibration_and_knowledge_notes.md`: conventions extracted from reference market models and from a licensed training library (per-line method cards)

## Closed decisions (do not reopen unless the user asks)

- Hybrid architecture: Python engine in this repo + AI (Claude) as the reasoning layer. **The user interface is Claude Code itself (the user's terminal / PowerShell); there is no GUI** (decision of June 18, 2026 — see the build-phase decisions below). Claude Code orchestrates and drives the engine as a toolkit/CLI; the engine no longer calls Claude.
- MVP: historicals + projections. DCF in v2
- Pilots: Prio (Oil & Gas) and 3tentos (agricultural inputs)
- Data entry 100% manual by the user; sector data (ANP etc.) delivered ready-to-use by the user
- Operational structure self-adapts to the granularity each company discloses (core differentiator)
- Quarterly + annual with interleaved columns: 1Q22, 2Q22, 3Q22, 4Q22, 2022, 1Q23... (the year closes the block)
- History: 10 years or since the IPO
- Line labels in English, each company's reporting currency
- History in the model tabs always linked by formula to the input tab, never typed
- The 3 statements automatically interlinked (NI → RE, schedules as roll-forwards, CF as a reconciliation, cash/revolver as plugs, balance check in every column)
- The AI proposes each assumption with method, source, date and rationale; the user approves; logged in the Assumptions tab + a cell comment

## Spreadsheet conventions (mandatory)

- Blue = hardcode/input, black = formula, green = link between tabs, red = external link
- Sign convention 1: revenues positive, expenses negative, labels prefixed (=) (-) (+)
- No constants embedded in formulas; every assumption in its own cell
- No nested IFs (use MIN/MAX/flags), no named ranges, no macros, no hidden rows
- No circularity in the MVP: interest on the opening debt balance
- Aesthetics and clarity: follow Model A in `Example models/` (local archive, not under version control); avoid the style of Model D (dense, hard to audit)

## Compliance (non-negotiable)

- Every estimate labeled with method and source, never presented as reported data
- No investment recommendations, no target price in the MVP
- Public sources only
- `Example models/` and `Knowledge Base/` are proprietary, copyright-protected materials: keep them in `.gitignore`, never copy their literal content into public code or docs

## Decisions closed on June 10, 2026 (second round)

- Projection horizon: quarterly through the end of next year, annual through year 10
- Pilot order: Prio first, then 3tentos
- Base/bull/bear scenarios: v2

## Decisions closed on June 10, 2026 (third round, "resolve all open points")

- Valuation tab in the final model: DCF (FCFF), WACC with assumptions and sources, multiples, target price (analytical output with a disclaimer, never a recommendation), bull/base/bear scenarios, summary of financial/operational data and assumptions
- Scenarios: three complete assumption sets in the Premises tab with a toggle in Valuation; the AI proposes bull/bear as justified deviations from base
- IFRS 16: report EBITDA and EBITDA-AL; in the EV→equity bridge, leases count as debt; FCFF deducts lease payments (consistent with telecom guidance)
- Quarterly updates: approved assumptions are the source of truth; when regenerating the model with new input, the engine reapplies everything with Approved status from the Assumptions log (merged by line+period); seeds only for lines without a decision
- JCP (interest on equity) / effective tax rate: dedicated method card (taxation and distributions in Brazil)

## Build backlog (order for the next Claude Code session)

1. Refactor the engine to declarative sector templates (YAML in /templates); O&G and telecom become data, not code
2. Revolver + dynamic debt (simple cash sweep, interest on the opening balance, no circularity)
3. Dynamic working capital (DSO/DPO/turnover as assumptions)
4. New inputs: shares outstanding (telecom has it; add to O&G), EV→equity bridge components
5. Persistence of approved assumptions on re-build (read the Assumptions log)
6. Full Valuation tab (DCF, WACC, multiples, scenarios, WACC×g sensitivity). Cost of debt (Kd) linked to the debt section: the debt schedule's weighted average cost (tranches, indexes, spreads) feeds the WACC by formula, never a standalone typed assumption
7. Run a complete assumption session (every line) in the rich format: history + alternatives with pros/cons + reasoning, never a bare question
8. Multi-company structure (decision of June 10, 2026): /coverage folder with one folder per sector (a _sector.md file: theses, drivers and shared assumptions with source/date, e.g. Brent, FX, sector growth) and a subfolder per company (inputs, models, Assumptions log). An analyst_profile.md file at the root records how the user works (assumption style, conservatism, preferred formats), updated at the end of each session with approval. New Claude Code conversation per company; this CLAUDE.md instructs reading the profile + _sector.md + the company log when opening a session. Sessions must flag divergences between companies in the same sector (coverage consistency)
9. Per-sector LLM wiki (decision of June 10, 2026; Andrej Karpathy's three-folder "llm-wiki" pattern): beyond the input tabs, each sector in /coverage gets a knowledge base in 3 layers — `sources/` (immutable raw material: releases, transcripts, sector reports; the AI reads but never edits; gitignored for copyright reasons), `wiki/` (AI-distilled markdown articles, one concept per file, with cross-links, provenance pointing to the source and an `index.md` entry point; git-versioned) and schema (wiki maintenance rules in this CLAUDE.md). The assumption session consults the wiki before proposing — grounding proposals in verifiable sources instead of model memory, mitigating source hallucination. Extends item 8's `_sector.md` (which becomes the wiki's executive summary)

## Status (June 2026) — what is already built

- **Oil & Gas engine: dynamic schedules done** — backlog items 2 (revolver + dynamic debt), 3 (dynamic working capital) and 5 (assumption persistence on rebuild) are implemented in `engine/build_model.py`, plus IFRS-16 leases (RoU + lease-liability roll-forwards) and ARO. Interest on the opening balance, no circularity.
- **Verification harness** (`engine/harness/`): recalculates the generated workbook (`formulas` backend) and asserts the invariants (balance check = 0 every column, ties, no error cells). Run end-to-end with `python -m engine.harness.pipeline <input> <output>`.
- **Interface = Claude Code (June 18, 2026)**: the Streamlit app (`app/assumption_session.py`) was **removed**. The line-by-line assumption session now runs as a conversation in Claude Code, which drives the engine as a toolkit. The four-agent panel and resumable-session concepts survive but are being redesigned for the engine-CLI + Claude Code format; the old Python→Claude bridge (`engine/advisor.py`, `engine/panel.py`) is orphaned, pending that redesign. **Guardrails (method+source gate, sanity bounds, harness, YAML log + cell comments) must be enforced by the engine as invariants**, not left to the conversation.
- **Knowledge base started** (backlog item 9): `knowledge/damodaran_corporate_life_cycle/` and `knowledge/sector_modeling_rules/` (per-sector).
- **Adaptive operational layer + single base template (June 17, 2026)** — backlog item 1 reframed: no per-sector YAML (`oil_and_gas.yaml` deleted); `templates/base.yaml` is the only template; sector knowledge lives in `knowledge/sector_modeling_rules/<sector>.md` cards. `engine/template_loader.py` identifies company/sector + introspects the operational tab + locates the card. The engine builds the operational section from introspection: O&G keeps its bottom-up volume×price build; any other sector gets a generic top-down build (revenue growth × margin + disclosed drivers). Verified (pytest 17/17; generic path balances 0). **Caveat:** the *financial* input schema is still per-engine (telecom uses different labels + `build_model_telecom.py`) — a single adaptive engine still needs the financial template generalized.
- **Valuation tab done (item 6, June 17, 2026)** — `add_valuation_tab` in `build_model.py`: FCFF DCF, WACC with **Kd read from the debt schedule by formula**, Gordon terminal value, EV→equity bridge (leases as debt, IFRS-16), implied value/share, EV/EBITDA + P/E multiples, bull/base/bear scenarios, WACC×g sensitivity grid. Reads the statements only (balance check unaffected). Scenarios are valuation-parameter variations (WACC/g); full operational-premise scenario sets remain a follow-up.
- **Reverse DCF / break-even done** — `engine/reverse_dcf.py`: reads the FCFF stream + bridge off the recalculated Valuation tab and back-solves the WACC, terminal g, and uniform FCFF haircut the screen price implies. CLI: `python -m engine.reverse_dcf <model.xlsx> <price>`.
- **Session grounded in the method card (Stage 3) done** — `engine/sector_knowledge.py` detects the sector from the input and extracts the card excerpt relevant to the premise; injected into the panel/advisor prompts so proposals are grounded in `knowledge/sector_modeling_rules/` and cite it, not model memory.
- **Damodaran line-linking adjustments done (June 17, 2026)** — three changes from `knowledge/damodaran_corporate_life_cycle/application_to_copilot.md` that tie previously-independent lines together, in `build_model.py` (+ `reverse_dcf.py` kept in sync): (1) **sales-to-capital capex** in the generic top-down build — `capex = D&A + Δrevenue ÷ sales-to-capital` premise (replaces the flat capex seed), so PP&E/invested capital grows in step with revenue and FCFF reinvestment is consistent; O&G's bottom-up per-field capex is intentionally untouched. (2) **Reinvestment-consistent terminal value** — the Gordon TV is rebuilt from terminal NOPAT × (1 − g÷ROIC) via a new "Terminal ROIC" assumption, not by growing the last explicit FCFF; scenarios/sensitivity use the same terminal. (3) **ROIC vs. WACC value-creation block** on the Valuation tab (per-year ROIC, invested capital from BS, ROIC−WACC spread) — the headline test for O&G "bad-business" growth. Verified: pytest 22/22; generic path balances 6/6 with no warnings. The wider life-cycle classifier (stage read + cyclical guard) remains unwired — a separate follow-up.
- **Sector-agnostic intake + build (June 21, 2026)** — Fase 1 intake redesigned as a sector-agnostic pipeline (flatten → tolerant period grid → bilingual match → data-driven detection → coverage gate → base+delta schema → role tag → rollup → sufficiency → write the canonical adjusted input → `assert_fase1_pass` gate), with compliance guardrails as engine invariants. No sector is hardcoded: the sector set is disk-driven (`canonical_schema.known_sectors()`), detection matches `signals:` declared in each `templates/sectors/<slug>.delta.yaml`, and the builder is found by convention (`build_model_<slug>.py` if present, else the default engine). The shared statement reads are **None-safe**, so a non-O&G input builds AND balances through the generic top-down path (`tests/test_generic_build.py`). **Telecom was removed** (never a pilot). Authoring guide: `knowledge/sector_modeling_rules/_sector_page_guide.md`.
- **Pending:** per-sector dedicated builders (`build_model_<slug>.py`) where the generic path is too coarse; per-sector operational granularity (Fase 2/3); full three-scenario premise sets in the model (not just valuation-level); the rollup checksum-vs-reported-subtotal.

## Decisions closed in the build phase (June 2026)

- **Interface = Claude Code (decided June 18, 2026).** The Streamlit prototype + Agent SDK bridge (Python calling Claude) hit its limits (the Streamlit rerun model fights a stateful, latency-heavy approval workflow). The architecture inverted: **Claude Code orchestrates and drives the Python engine as a toolkit/CLI**, instead of Python calling Claude. The engine exposes a clean CLI (runnable bare in PowerShell) and Claude Code is the reasoning driver. This resolves the earlier open "Phase B bridge (Agent SDK vs MCP)" decision: neither — the bridge is Claude Code. `app/` and the `streamlit`/`claude-agent-sdk` dependencies were removed.
- **LangChain / LangGraph: evaluated and discarded.** Keep a plain Python engine driven by Claude Code. The valuable patterns (structured output, adversarial panel, markdown logs) were harvested without the framework. Revisit LangGraph only if a hosted autonomous service is ever needed.

## Open decisions (ask the user when relevant)

- Python package name
- Reporting currency of each pilot (confirm with the first input)

## Stack

Python (pandas, numpy, openpyxl with real formulas), declarative sector templates (YAML/JSON), engine tests. Target repo structure: `/engine`, `/templates`, `/inputs`, `/models` (.xlsx outputs), `/knowledge` (method cards), `/reference` (gitignored).
