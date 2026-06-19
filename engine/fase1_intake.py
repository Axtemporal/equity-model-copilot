"""Fase 1 intake orchestrator (steps 1.2-1.10) — the deterministic spine Claude Code drives.

Pure-Python pipeline; the AI/conversation handles ONLY the residual + the gap/currency
judgments, consuming this output:
  flatten -> detect + coverage-gate sector -> resolve labels (3-pass) -> classify roles ->
  content sufficiency -> Manifest.

The input may be one messy tab mixing statements, capital-structure facts and reported
aggregates, so flatten operates on a FLAT line list across all sheets, not a fixed layout.
Writing the canonical adjusted-input .xlsx and the AI residual/currency steps plug on top of
the Manifest this produces. Run as: python -m engine.fase1_intake <input.xlsx>
"""
from __future__ import annotations

import re

import openpyxl
from openpyxl.utils import get_column_letter

from . import canonical_schema as cs
from . import label_resolver as lr
from . import role_classifier as rc
from . import sector_coverage as scov
from .fase1_manifest import (
    CONTEXTUAL, MAPPED, SLOT_ABSENT, SLOT_MAPPED, LineRecord, Manifest, SlotCoverage,
)
from .harness.invariants import FIRST_COL, HDR, LABEL_COL
from .harness.validator import detect_sector
from .template_loader import identify_company

_QUARTER_RE = re.compile(r"^[1-4]Q\d{2}$")
_YEAR_RE = re.compile(r"^\d{4}$")
_SKIP_SHEETS = ("assumptions", "readme", "premises")


def _is_period(value) -> bool:
    text = str(value).strip() if value is not None else ""
    return bool(_QUARTER_RE.match(text) or _YEAR_RE.match(text))


def _find_header_row(ws) -> int:
    """The row with the most period-like header cells (falls back to the template's row 5)."""
    best_row, best_n = HDR, 0
    for row in range(1, min(ws.max_row, 40) + 1):
        n = sum(1 for col in range(1, ws.max_column + 1) if _is_period(ws.cell(row, col).value))
        if n > best_n:
            best_row, best_n = row, n
    return best_row


def flatten(wb) -> list[LineRecord]:
    """Collapse the workbook (any layout) into a flat list of labeled line records."""
    records: list[LineRecord] = []
    for sheet in wb.sheetnames:
        if sheet.strip().lower().startswith(_SKIP_SHEETS):
            continue
        ws = wb[sheet]
        hdr = _find_header_row(ws)
        period_cols = [(c, str(ws.cell(hdr, c).value).strip())
                       for c in range(1, ws.max_column + 1) if _is_period(ws.cell(hdr, c).value)]
        first_pc = min((c for c, _ in period_cols), default=FIRST_COL)
        label_col = LABEL_COL if LABEL_COL < first_pc else 1
        unit_col = label_col + 1 if (label_col + 1) < first_pc else None
        for row in range(hdr + 1, ws.max_row + 1):
            label = ws.cell(row, label_col).value
            if not isinstance(label, str) or not label.strip():
                continue
            values = {pl: ws.cell(row, c).value
                      for c, pl in period_cols if ws.cell(row, c).value is not None}
            unit = ws.cell(row, unit_col).value if unit_col else None
            records.append(LineRecord(
                raw_label=label.strip(),
                sheet=sheet,
                cell=f"{sheet}!{get_column_letter(label_col)}{row}",
                unit=unit.strip() if isinstance(unit, str) else None,
                values=values,
            ))
    return records


def analyze(input_path: str, sector: str | None = None) -> Manifest:
    """Run the deterministic Fase 1 spine and return the Manifest (raises if sector is blocked)."""
    wb = openpyxl.load_workbook(input_path, data_only=True)
    fin = wb["Input Financials"] if "Input Financials" in wb.sheetnames else None
    company = identify_company(fin) if fin is not None else "Unknown"

    sector = sector or detect_sector(wb)
    if sector:
        scov.assert_supported(sector)            # coverage gate (raises SectorCoverageError)

    records = flatten(wb)

    if sector:
        matches: dict[str, lr.Match] = {}
        for m in lr.resolve([r.raw_label for r in records], sector):
            matches.setdefault(m.raw, m)         # first occurrence wins (label dedupe parity)
        for rec in records:
            m = matches.get(rec.raw_label)
            if m and m.canonical:
                rec.canonical, rec.method, rec.confidence = m.canonical, m.method, m.score
                rec.role = rc.classify(m.canonical, sector)
                rec.disposition = MAPPED
                rec.provenance = f"{m.method} match"
            else:
                rec.role = rc.CONTEXTUAL
                rec.disposition = CONTEXTUAL

    coverage: list[SlotCoverage] = []
    if sector:
        mapped_canonical = {r.canonical for r in records if r.disposition == MAPPED}
        for sheet, labels in cs.required_labels(sector).items():
            for slot in labels:
                status = SLOT_MAPPED if slot in mapped_canonical else SLOT_ABSENT
                coverage.append(SlotCoverage(slot, sheet, status))

    residual = [r.raw_label for r in records if r.canonical is None]
    return Manifest(company=company, sector=sector, lines=records,
                    coverage=coverage, residual=residual)


def _report(manifest: Manifest) -> str:
    mapped = sum(1 for line in manifest.lines if line.disposition == MAPPED)
    out = [
        f"Fase 1 intake — {manifest.company} [{manifest.sector or 'sector?'}]",
        f"  lines: {len(manifest.lines)} ({mapped} mapped, {len(manifest.residual)} residual)",
        f"  content sufficient: {manifest.content_sufficient}",
    ]
    if manifest.missing_required:
        out.append("  MISSING required slots:")
        for cov in manifest.missing_required:
            out.append(f"    - [{cov.sheet}] {cov.slot}")
    if manifest.residual:
        out.append("  residual (for the AI semantic pass / your review):")
        for raw in manifest.residual[:20]:
            out.append(f"    - {raw}")
    return "\n".join(out)


if __name__ == "__main__":
    import sys

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass

    if len(sys.argv) < 2:
        print("usage: python -m engine.fase1_intake <input.xlsx> [sector]")
        sys.exit(2)
    sec = sys.argv[2] if len(sys.argv) > 2 else None
    try:
        manifest = analyze(sys.argv[1], sec)
    except scov.SectorCoverageError as exc:
        print("BLOCKED:", exc)
        sys.exit(3)
    print(_report(manifest))
