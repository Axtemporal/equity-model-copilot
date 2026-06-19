"""Sector coverage gate — tiers from disk, and the block-with-available-list behavior."""
import pytest

from engine import canonical_schema as cs
from engine import sector_coverage as sc


def test_pilots_are_full_tier():
    assert sc.coverage(cs.OIL_AND_GAS).tier == sc.TIER_FULL
    assert sc.coverage(cs.TELECOM).tier == sc.TIER_FULL


def test_card_without_delta_is_partial():
    # agri_inputs has a method card but no delta YAML and no dedicated builder.
    cov = sc.coverage("agri_inputs")
    assert cov.has_card and not cov.has_delta
    assert cov.tier == sc.TIER_PARTIAL


def test_unknown_sector_is_blocked():
    cov = sc.coverage("aerospace_defense")
    assert cov.tier == sc.TIER_NONE
    assert cov.blocked


def test_assert_supported_passes_for_pilot():
    assert sc.assert_supported(cs.OIL_AND_GAS).tier == sc.TIER_FULL


def test_assert_supported_blocks_and_lists_available():
    with pytest.raises(sc.SectorCoverageError) as exc:
        sc.assert_supported("aerospace_defense")
    assert cs.OIL_AND_GAS in exc.value.full
    assert cs.TELECOM in exc.value.full
    assert "agri_inputs" in exc.value.partial


def test_by_tier_lists_pilots_as_full():
    tiers = sc.by_tier()
    assert cs.OIL_AND_GAS in tiers[sc.TIER_FULL]
    assert cs.TELECOM in tiers[sc.TIER_FULL]
