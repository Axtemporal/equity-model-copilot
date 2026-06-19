"""Reverse DCF consistency (requires a recalc backend)."""
import pytest

from engine.reverse_dcf import (
    extract_dcf_inputs,
    implied_fcff_scale,
    implied_g,
    implied_wacc,
    value_per_share,
)


@pytest.mark.recalc
def test_reverse_dcf_inverts_to_base(require_recalc, synth_inputs, tmp_path):
    from engine import build_model

    out = str(tmp_path / "model.xlsx")
    build_model.main(synth_inputs, out)
    inp = extract_dcf_inputs(out)

    # the Python DCF reproduces the Valuation tab's implied price
    assert inp.fcff, "no FCFF stream extracted"
    assert abs(value_per_share(inp, inp.wacc, inp.g) - inp.price) < 1e-3

    # inverting at the model's own price returns the base assumptions
    assert abs(implied_wacc(inp, inp.price) - inp.wacc) < 1e-4
    assert abs(implied_g(inp, inp.price) - inp.g) < 1e-4
    assert abs(implied_fcff_scale(inp, inp.price) - 1.0) < 1e-3

    # monotonicity: a lower price implies a higher discount rate
    assert implied_wacc(inp, inp.price * 0.8) > inp.wacc
