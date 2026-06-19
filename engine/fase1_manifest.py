"""Fase 1 mapping manifest — the audited record of how a raw input became a canonical one.

Every flattened input line reaches exactly one terminal disposition; the manifest carries that,
the resolution method + confidence + provenance, the per-slot content-sufficiency matrix, and
the currency/staleness block. Written to disk (models/<company>/fase1_manifest.yaml) so the
Fase 1 PASS is read from artifacts, never from conversation memory.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field

import yaml

# line dispositions (every flattened line ends in exactly one)
MAPPED = "mapped"
DECLARED_ZERO = "declared_zero"
CONTEXTUAL = "contextual"
ESCALATED = "escalated"
DROPPED = "dropped"
PENDING = "pending"

# required-slot content-sufficiency statuses
SLOT_MAPPED = "mapped"
SLOT_DECLARED_ZERO = "declared_zero"
SLOT_ABSENT = "absent"


@dataclass
class LineRecord:
    raw_label: str
    sheet: str
    cell: str | None = None
    unit: str | None = None
    values: dict = field(default_factory=dict)      # period -> value
    canonical: str | None = None
    method: str = "unresolved"                       # exact|alias|fuzzy|ai|unresolved
    confidence: float = 0.0
    role: str | None = None
    disposition: str = PENDING
    provenance: str = ""


@dataclass
class SlotCoverage:
    slot: str
    sheet: str
    status: str                                       # mapped|declared_zero|absent


@dataclass
class Manifest:
    company: str
    sector: str | None
    lines: list = field(default_factory=list)         # list[LineRecord]
    coverage: list = field(default_factory=list)      # list[SlotCoverage]
    residual: list = field(default_factory=list)      # raw labels no pass resolved
    currency: dict = field(default_factory=dict)      # filled by step 1.8b (staleness)

    @property
    def missing_required(self) -> list:
        return [c for c in self.coverage if c.status == SLOT_ABSENT]

    @property
    def content_sufficient(self) -> bool:
        return not self.missing_required

    def to_dict(self) -> dict:
        return {
            "company": self.company,
            "sector": self.sector,
            "content_sufficient": self.content_sufficient,
            "missing_required": [c.slot for c in self.missing_required],
            "lines": [asdict(line) for line in self.lines],
            "coverage": [asdict(c) for c in self.coverage],
            "residual": list(self.residual),
            "currency": dict(self.currency),
        }

    def save(self, path: str) -> str:
        with open(path, "w", encoding="utf-8") as handle:
            yaml.safe_dump(self.to_dict(), handle, allow_unicode=True, sort_keys=False)
        return path
