# AI-Assisted Financial Modeling System

A modeling copilot for Brazilian equities: turns the analyst's manual inputs into standardized Excel models (three-statement IFRS + sector-specific operational modeling), with the AI proposing assumptions line by line for user approval.

## Reference documents (read before any work)

1. `docs/project_specification.md`: spec v0.2 with all closed decisions
2. `docs/calibration_and_knowledge_notes.md`: conventions extracted from reference market models and from a licensed training library (per-line method cards)

## Closed decisions (do not reopen unless the user asks)

- Hybrid architecture: Python engine in this repo, AI (Claude) as the reasoning layer, web interface (Phase B) later
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
6. Full Valuation tab (DCF, WACC, multiples, scenarios, WACC×g sensitivity)
7. Run a complete assumption session (every line) in the rich format: history + alternatives with pros/cons + reasoning, never a bare question
8. Multi-company structure (decision of June 10, 2026): /coverage folder with one folder per sector (a _sector.md file: theses, drivers and shared assumptions with source/date, e.g. Brent, FX, sector growth) and a subfolder per company (inputs, models, Assumptions log). An analyst_profile.md file at the root records how the user works (assumption style, conservatism, preferred formats), updated at the end of each session with approval. New Claude Code conversation per company; this CLAUDE.md instructs reading the profile + _sector.md + the company log when opening a session. Sessions must flag divergences between companies in the same sector (coverage consistency)

## Open decisions (ask the user when relevant)

- Phase B technical bridge (Claude Agent SDK vs. MCP server), decide after a prototype
- Python package name
- Reporting currency of each pilot (confirm with the first input)

## Stack

Python (pandas, numpy, openpyxl with real formulas), declarative sector templates (YAML/JSON), engine tests. Target repo structure: `/engine`, `/templates`, `/inputs`, `/models` (.xlsx outputs), `/knowledge` (method cards), `/reference` (gitignored).
