"""Structured proposal capture: seed proposal, tool schema, tool-call validation, conversion."""
from engine.proposals import (
    ASSUMPTION_PROPOSAL_TOOL,
    proposal_from_seed,
    proposal_from_toolcall,
    proposal_to_assumption,
)


def test_proposal_from_seed_drops_blanks():
    line = {"line_item": "Brent average", "unit": "USD/bbl",
            "periods": [("2028", 80), ("2029", 80), ("2030", None)]}
    proposal = proposal_from_seed(line)
    assert proposal.line_item == "Brent average"
    assert proposal.values == {"2028": 80, "2029": 80}
    assert proposal.unit == "USD/bbl"


def test_tool_schema_is_well_formed():
    schema = ASSUMPTION_PROPOSAL_TOOL
    assert schema["name"] == "propose_assumption"
    props = schema["input_schema"]["properties"]
    assert {"line_item", "values", "method", "rationale"} <= set(props)
    assert set(schema["input_schema"]["required"]) == {"line_item", "values", "method", "rationale"}


def test_toolcall_validates_and_converts():
    payload = {"line_item": "Brent average", "values": {"2029": 70},
               "method": "forward curve", "source": "EIA STEO", "rationale": "mean reversion"}
    proposal = proposal_from_toolcall(payload)
    assert proposal.values == {"2029": 70}
    assumption = proposal_to_assumption(proposal, status="Aprovada")
    assert assumption.line_item == "Brent average"
    assert assumption.status == "Aprovada"
    assert assumption.values["2029"] == 70
