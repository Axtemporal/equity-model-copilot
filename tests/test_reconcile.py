"""Reconciliation gate: the deterministic compare_series core (reported vs computed)."""
from engine.harness.reconcile import compare_series


def test_flags_period_beyond_tolerance():
    reported = {"2023": 1000, "2024": 1100}
    computed = {"2023": 1000, "2024": 1300}
    gaps = compare_series(reported, computed, rel_tol=0.01)
    assert [g[0] for g in gaps] == ["2024"]
    assert gaps[0] == ("2024", 1100.0, 1300.0)


def test_within_tolerance_no_gap():
    assert compare_series({"2023": 1000}, {"2023": 1005}, rel_tol=0.01) == []


def test_ignores_nonnumeric_and_missing():
    assert compare_series({"2023": None, "2024": "x", "2025": 5}, {"2023": 1, "2024": 2}) == []
