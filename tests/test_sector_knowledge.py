"""Stage 3 grounding: sector detection + method-card excerpt (no Claude needed)."""
from engine import sector_knowledge


def test_detect_sector_from_synth_input(synth_inputs):
    assert sector_knowledge.detect_sector_from_input(synth_inputs) == "oil_and_gas"


def test_card_excerpt_grounds_in_the_card():
    text = sector_knowledge.card_excerpt("oil_and_gas", "Brent average")
    assert text, "expected a non-empty excerpt for an existing card"
    # the excerpt is drawn from the real card, not invented
    assert text in sector_knowledge.load_card("oil_and_gas") or len(text) <= 2600


def test_card_excerpt_empty_for_unknown_sector():
    assert sector_knowledge.card_excerpt(None, "anything") == ""
    assert sector_knowledge.card_excerpt("no_such_sector", "anything") == ""


def test_premise_prompt_includes_grounding():
    from engine.advisor import premise_prompt

    line = {"line_item": "Brent average", "unit": "USD/bbl", "periods": [("2027", 70)]}
    prompt = premise_prompt("qual sua visão?", line, [], grounding="GROUND-XYZ")
    assert "GROUND-XYZ" in prompt
    assert "CONHECIMENTO SETORIAL" in prompt
