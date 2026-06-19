"""Verification harness for the generated Excel models (foundation item 1).

openpyxl writes formulas but never computes them, so the engine delivers a model
"blind". This package recalculates the workbook with a real calculator and then
asserts the model's integrity invariants (balance check ~0, statements tie, no
error cells, every formula resolved), turning the fidelity promise into a test.

Public API:
    verify_model(path) -> Report
"""
from __future__ import annotations

import openpyxl

from .invariants import INVARIANTS
from .recalc import RecalcError, recalc, recalc_workbook
from .report import CellRef, InvariantResult, Report, Severity

__all__ = [
    "verify_model",
    "Report",
    "InvariantResult",
    "Severity",
    "CellRef",
    "RecalcError",
    "recalc",
    "recalc_workbook",
]


def verify_model(path: str, *, backend: str = "formulas") -> Report:
    """Recalculate `path` with `backend` and run every registered invariant."""
    orig = openpyxl.load_workbook(path)  # formulas (data_only=False)
    calc, _out = recalc_workbook(path, backend=backend)
    report = Report(model_path=path, backend_used=backend)
    for check in INVARIANTS:
        report.results.append(check(orig, calc))
    return report
