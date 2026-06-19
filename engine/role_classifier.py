"""Per-line ROLE tagging (Fase 1, step 1.5): what part a canonical line plays in the model.

Roles route a line to its destination:
  statement-line        -> flows into the 3 statements (the build).
  capital-structure-fact -> valuation inputs (shares, capital structure).
  reported-check        -> reconciled against the model-computed value POST-build; never drives.
  operational-raw       -> waits for Fase 2/3 (no fixed operational schema here).
  contextual-reference  -> unmapped/extra; carried with provenance, never silently dropped.
"""
from __future__ import annotations

from . import canonical_schema as cs

STATEMENT = "statement-line"
CAPITAL_STRUCTURE = "capital-structure-fact"
REPORTED_CHECK = "reported-check"
OPERATIONAL_RAW = "operational-raw"
CONTEXTUAL = "contextual-reference"

# Reported aggregates we INGEST to reconcile post-build (never as drivers). 'EBITDA (as
# disclosed)' is a reported-check even where a sector engine also keys its build off it — that
# is a build-routing fact, kept separate from the intake role.
REPORTED_CHECKS = {
    "(=) EBITDA (as disclosed)",
    "memo: (=) EBITDA (as disclosed)",
    "Net debt",
    "Net debt (reported)",
    "Adjusted EBITDA",
    "(=) EBITDA-AL",
    "EBITDA-AL",
}


def classify(canonical_label: str, sector: str) -> str:
    if canonical_label in cs.STRUCTURAL:
        return CAPITAL_STRUCTURE
    if canonical_label in REPORTED_CHECKS:
        return REPORTED_CHECK
    req = cs.required_labels(sector)
    if canonical_label in req[cs.FINANCIALS]:
        return STATEMENT
    if canonical_label in req[cs.OPERATIONAL]:
        return OPERATIONAL_RAW
    return CONTEXTUAL
