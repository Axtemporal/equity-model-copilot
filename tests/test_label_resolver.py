"""3-pass label resolver: exact, alias (bilingual), fuzzy (typo), and residual routing."""
from engine import canonical_schema as cs
from engine import label_resolver as lr


def _one(raw, sector=cs.OIL_AND_GAS):
    return lr.resolve([raw], sector)[0]


def test_exact_pass_ignores_sign_prefix_and_case():
    m = _one("Net Revenue")  # raw without the '(=)' prefix, different case
    assert m.canonical == "(=) Net revenue"
    assert m.method == lr.EXACT
    assert m.sheet == cs.FINANCIALS


def test_alias_pass_resolves_portuguese():
    m = _one("Receita líquida")
    assert m.canonical == "(=) Net revenue"
    assert m.method == lr.ALIAS


def test_fuzzy_pass_catches_typo():
    m = _one("Net reveneu")  # transposed typo
    assert m.canonical == "(=) Net revenue"
    assert m.method == lr.FUZZY
    assert m.score >= lr.FUZZY_CUTOFF


def test_unrelated_label_is_residual():
    m = _one("Quantum flux capacitance")
    assert m.canonical is None and m.method == lr.UNRESOLVED


def test_residual_collects_only_unresolved():
    matches = lr.resolve(["Net revenue", "Receita líquida", "totally unknown line"], cs.OIL_AND_GAS)
    assert lr.residual(matches) == ["totally unknown line"]


def test_telecom_alias_for_disclosed_ebitda():
    m = _one("EBITDA", sector=cs.TELECOM)
    assert m.canonical == "(=) EBITDA (as disclosed)"
    assert m.method == lr.ALIAS
