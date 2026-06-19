"""Canonical financial schema — the single source of truth for sector slugs and the
input line labels the engine consumes.

The Fase 1 layered minimum (see flow_sistema_e_progresso.md §Fase 1):
  - UNIVERSAL_BASE_FINANCIAL: the three-statement line labels shared *verbatim* by every
    sector engine. Kept DRY here so the validator, the build engines and the future label
    resolver agree, instead of duplicating string literals — the very duplication that bred
    the 'oil_and_gas' vs 'oil_gas' slug bug and the validator/engine label-set gap.
  - per-sector DELTA: the extra (and divergent-spelling) labels a sector needs, declared as
    machine-readable YAML in templates/sectors/<slug>.delta.yaml. The method card links to
    it; the schema is never duplicated in card prose.

`required_labels(sector)` -> {sheet: [labels]} = base + delta: the labels that sector's
engine hard-reads, so "the validator passes" means "the engine will not KeyError on a label".

Import the slug constants (OIL_AND_GAS, TELECOM) — never write the string literal again.
"""
from __future__ import annotations

import re
import unicodedata
from functools import lru_cache
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SECTOR_DELTA_DIR = ROOT / "templates" / "sectors"

# ─── canonical sector slugs (one family — the single source of truth for the slug) ──────
OIL_AND_GAS = "oil_and_gas"
TELECOM = "telecom"
SECTORS = (OIL_AND_GAS, TELECOM)

FINANCIALS = "Input Financials"
OPERATIONAL = "Input Operational"

# ─── universal base: shared verbatim by every sector engine (all on Input Financials) ───
INCOME_STATEMENT_BASE = [
    "(=) Net revenue",
    "(=) EBIT",
    "(=) EBT",
    "(-) Income taxes",
    "(=) Net income",
]
BALANCE_SHEET_BASE = [
    "Cash and equivalents",
    "Short-term investments",
    "Trade receivables",
    "Inventories",
    "Other current assets",
    "PP&E",
    "Intangible assets and goodwill",
    "Right-of-use assets",
    "Deferred tax assets",
    "Other non-current assets",
    "Trade payables",
    "Other current liabilities",
    "Loans and financing (current)",
    "Loans and financing (non-current)",
    "Lease liabilities (current)",
    "Lease liabilities (non-current)",
    "Deferred tax liabilities",
    "Other non-current liabilities",
    "Share capital and reserves",
    "Retained earnings (accumulated)",
]
UNIVERSAL_BASE_FINANCIAL = INCOME_STATEMENT_BASE + BALANCE_SHEET_BASE

# Structural facts (not statement lines). Part of the Fase 1 minimum but NOT yet hard-required
# by the validator: the engine still hardcodes shares (build_model.py) instead of reading this
# line. Promoting it to a read input is the integration step that makes per-share value real.
STRUCTURAL = ["memo: Shares outstanding (EOP)"]


@lru_cache(maxsize=16)
def load_delta(sector: str) -> dict:
    """templates/sectors/<sector>.delta.yaml -> {'Input Financials': [...], 'Input Operational': [...]}.

    Returns {} when the file is absent (a sector with a card but no machine schema yet).
    """
    path = SECTOR_DELTA_DIR / f"{sector}.delta.yaml"
    if not path.exists():
        return {}
    with open(path, encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    return data.get("required", {}) or {}


def has_delta(sector: str) -> bool:
    return (SECTOR_DELTA_DIR / f"{sector}.delta.yaml").exists()


def required_labels(sector: str) -> dict[str, list[str]]:
    """{sheet: [labels]} the sector's engine hard-reads = universal base + sector delta.

    The universal base is shared verbatim; the delta carries sector-specific lines AND the
    divergent-spelling ones (e.g. O&G '(+/-) Financial result' vs telecom
    '(+/-) Net financial result'). A sector with no delta yields base-only.
    """
    delta = load_delta(sector)
    fin = list(UNIVERSAL_BASE_FINANCIAL) + list(delta.get(FINANCIALS, []) or [])
    op = list(delta.get(OPERATIONAL, []) or [])
    return {FINANCIALS: fin, OPERATIONAL: op}


def known_sectors() -> tuple[str, ...]:
    """Sectors that have a declared delta (i.e. a machine-readable Fase 1 intake schema)."""
    if not SECTOR_DELTA_DIR.exists():
        return ()
    return tuple(sorted(
        p.name[: -len(".delta.yaml")] for p in SECTOR_DELTA_DIR.glob("*.delta.yaml")
    ))


_SIGN_PREFIX_RE = re.compile(r"^\(\s*[=+\-/ ]+\s*\)\s*")  # (=) (-) (+) (+/-)
_MEMO_PREFIX_RE = re.compile(r"^memo\s*:\s*")
_NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")


def normalize(label: str) -> str:
    """Canonical normal form for label matching — the SINGLE normalizer the resolver, the
    alias dictionary and the exact pass all share.

    Casefolds, strips accents, drops a leading sign prefix ('(=)', '(-)', '(+/-)') and a
    'memo:' prefix, and collapses punctuation/whitespace. So '(=) Net revenue', 'Net Revenue'
    and 'Receita líquida' compare on equal footing where they should.
    """
    if not label:
        return ""
    text = unicodedata.normalize("NFKD", str(label))
    text = "".join(ch for ch in text if not unicodedata.combining(ch))  # strip accents
    text = text.casefold().strip()
    text = _SIGN_PREFIX_RE.sub("", text)
    text = _MEMO_PREFIX_RE.sub("", text)
    text = _NON_ALNUM_RE.sub(" ", text)
    return text.strip()
