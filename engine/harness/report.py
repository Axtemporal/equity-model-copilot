"""Verification harness — result types.

A `Report` is the outcome of verifying one generated model: a list of
`InvariantResult`s, each carrying the failing cells (with period label and the
numeric error) so a failure points straight at the broken column.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Severity(str, Enum):
    FAIL = "FAIL"   # a hard integrity guarantee — a failure means the model is wrong
    WARN = "WARN"   # suspicious but not necessarily an engine error (e.g. odd input)
    INFO = "INFO"


@dataclass
class CellRef:
    """A located value, optionally with the expectation it violated."""
    sheet: str
    a1: str
    period: str | None = None
    expected: float | None = None
    actual: object = None
    abs_error: float | None = None

    def __str__(self) -> str:
        loc = f"{self.sheet}!{self.a1}"
        if self.period:
            loc += f" ({self.period})"
        if self.expected is not None:
            return f"{loc} = {self.actual!r}, expected {self.expected} (abs_err={self.abs_error:.4g})"
        return f"{loc} = {self.actual!r}"


@dataclass
class InvariantResult:
    name: str
    severity: Severity
    passed: bool
    message: str
    failing_cells: list[CellRef] = field(default_factory=list)


@dataclass
class Report:
    model_path: str
    backend_used: str
    results: list[InvariantResult] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        """True iff no FAIL-severity invariant failed."""
        return all(r.passed for r in self.results if r.severity is Severity.FAIL)

    def __bool__(self) -> bool:
        return self.ok

    def failures(self) -> list[InvariantResult]:
        return [r for r in self.results if not r.passed and r.severity is Severity.FAIL]

    def warnings(self) -> list[InvariantResult]:
        return [r for r in self.results if not r.passed and r.severity is Severity.WARN]

    def summary(self) -> str:
        hard = [r for r in self.results if r.severity is Severity.FAIL]
        n_pass = sum(1 for r in hard if r.passed)
        status = "PASS" if self.ok else "FAIL"
        warns = len(self.warnings())
        tail = f" ({warns} warning{'s' if warns != 1 else ''})" if warns else ""
        return f"{status}: {n_pass}/{len(hard)} hard invariants passed{tail}"
