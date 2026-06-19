"""Role classifier: each canonical line routed to its destination role."""
from engine import canonical_schema as cs
from engine import role_classifier as rc


def test_statement_line():
    assert rc.classify("(=) Net revenue", cs.OIL_AND_GAS) == rc.STATEMENT
    assert rc.classify("PP&E", cs.OIL_AND_GAS) == rc.STATEMENT


def test_disclosed_ebitda_is_reported_check_even_for_telecom():
    # telecom keys its build off it, but the INTAKE role is reported-check
    assert rc.classify("(=) EBITDA (as disclosed)", cs.TELECOM) == rc.REPORTED_CHECK


def test_operational_raw():
    assert rc.classify("Brent average", cs.OIL_AND_GAS) == rc.OPERATIONAL_RAW
    assert rc.classify("Total lines", cs.TELECOM) == rc.OPERATIONAL_RAW


def test_capital_structure_fact():
    assert rc.classify("memo: Shares outstanding (EOP)", cs.OIL_AND_GAS) == rc.CAPITAL_STRUCTURE


def test_unknown_is_contextual():
    assert rc.classify("Some bespoke footnote line", cs.OIL_AND_GAS) == rc.CONTEXTUAL
