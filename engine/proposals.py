"""Structured capture of an assumption proposal.

A proposal is what the AI puts forward for one premise line: per-period values, the method, the
source (with date), a rationale, and optional alternatives. It is a typed object the UI renders
(instead of prose) and that a connected Claude can emit directly via tool-use —
ASSUMPTION_PROPOSAL_TOOL is the JSON Schema to register as an Anthropic tool, force with
tool_choice, then validate the result with proposal_from_toolcall. This is the structured-output
technique harvested from the TradingAgents study, without a framework dependency.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field


@dataclass
class Alternative:
    label: str
    values: dict = field(default_factory=dict)
    note: str = ""


@dataclass
class AssumptionProposal:
    line_item: str
    values: dict = field(default_factory=dict)        # period label -> number
    method: str = ""
    source: str = ""
    source_date: str = ""
    rationale: str = ""
    unit: str = ""
    alternatives: list = field(default_factory=list)  # list[Alternative]

    def to_dict(self) -> dict:
        return asdict(self)


# JSON Schema for Anthropic tool-use — a connected Claude emits a proposal by calling this tool.
ASSUMPTION_PROPOSAL_TOOL = {
    "name": "propose_assumption",
    "description": "Emit one auditable assumption proposal for a model premise line.",
    "input_schema": {
        "type": "object",
        "properties": {
            "line_item": {"type": "string", "description": "the Premises line this is for"},
            "values": {
                "type": "object",
                "description": "map of period label (e.g. '2029') to the proposed number",
                "additionalProperties": {"type": "number"},
            },
            "method": {"type": "string", "description": "calculation method, e.g. 'forward curve + consensus'"},
            "source": {"type": "string", "description": "public source"},
            "source_date": {"type": "string", "description": "source date, YYYY-MM"},
            "rationale": {"type": "string", "description": "why this premise, versus the alternatives"},
            "alternatives": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "label": {"type": "string"},
                        "values": {"type": "object", "additionalProperties": {"type": "number"}},
                        "note": {"type": "string"},
                    },
                    "required": ["label"],
                },
            },
        },
        "required": ["line_item", "values", "method", "source", "rationale"],
    },
}


def proposal_from_seed(line: dict) -> AssumptionProposal:
    """Build an offline proposal from a Premises line's seed values."""
    values = {p: v for p, v in line["periods"] if isinstance(v, (int, float))}
    return AssumptionProposal(
        line_item=line["line_item"],
        values=values,
        unit=line.get("unit") or "",
        method="",
        rationale="Valor inicial a partir do último histórico reportado (ainda sem decisão). "
                  "Converse no chat para ajustar — ex.: \"declínio de 1,5% ao ano\" ou "
                  "\"60% da produção do Bravo\" — e confirme.",
    )


def proposal_from_toolcall(payload: dict) -> AssumptionProposal:
    """Validate an Anthropic tool-use result into an AssumptionProposal (the future Claude bridge)."""
    alternatives = [Alternative(**a) for a in (payload.get("alternatives") or [])]
    return AssumptionProposal(
        line_item=payload["line_item"],
        values={str(k): v for k, v in (payload.get("values") or {}).items()},
        method=payload.get("method", ""),
        source=payload.get("source", ""),
        source_date=payload.get("source_date", ""),
        rationale=payload.get("rationale", ""),
        alternatives=alternatives,
    )


def proposal_to_assumption(proposal: AssumptionProposal, *, status: str | None = None):
    """Convert a proposal into a log Assumption (engine.assumptions.Assumption)."""
    from .assumptions import Assumption, AssumptionStatus

    return Assumption(
        line_item=proposal.line_item,
        values=dict(proposal.values),
        method=proposal.method,
        source=proposal.source,
        source_date=proposal.source_date,
        rationale=proposal.rationale,
        status=status or AssumptionStatus.PROPOSED.value,
    )
