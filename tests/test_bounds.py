"""Value sanity bounds: unit-error detection from a line's own history, and range guard."""
from engine.harness import bounds


def test_unit_outlier_flagged_against_own_history():
    series = {"1Q24": 1000, "2Q24": 1050, "3Q24": 980, "4Q24": 1_010_000}  # last in R$ '000
    out = bounds.unit_outliers(series)
    assert [o.period for o in out] == ["4Q24"]
    assert out[0].ratio >= bounds.UNIT_RATIO_FLAG


def test_clean_series_has_no_outliers():
    assert bounds.unit_outliers({"1Q24": 100, "2Q24": 110, "3Q24": 95, "4Q24": 105}) == []


def test_too_few_points_returns_empty():
    assert bounds.unit_outliers({"1Q24": 1, "2Q24": 1000}) == []


def test_within_range_guard():
    assert bounds.within(0.10, lo=0.0, hi=1.0)
    assert not bounds.within(1.5, lo=0.0, hi=1.0)
    assert not bounds.within(None, lo=0.0)
