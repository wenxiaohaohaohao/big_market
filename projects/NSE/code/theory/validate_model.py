"""Analytical-identity and finite-difference checks for the NSE model."""

from __future__ import annotations

import math
import sys
from dataclasses import replace
from pathlib import Path

import numpy as np

NUMERICAL_DIR = Path(__file__).resolve().parents[1] / "numerical"
sys.path.insert(0, str(NUMERICAL_DIR))

from model import (  # noqa: E402
    Parameters,
    capture_drag,
    consumer_price_index,
    entry_threshold,
    financing_wedge,
    infrastructure_supply,
    local_producer_income,
    nominal_effect,
    nominal_income,
    nominal_income_threshold,
    organization_threshold,
    platform_intermediate_condition,
    platform_share,
    platform_share_derivative,
    producer_choice,
    producer_access_elasticity,
    producer_profit,
    producer_retention,
    raw_local_entry_threshold,
    raw_organization_switch_threshold,
    raw_platform_entry_threshold,
    real_effect,
    real_income,
    real_income_threshold,
    validate_parameters,
)


def assert_close(actual: float, expected: float, tolerance: float, label: str) -> None:
    if not math.isfinite(actual) or abs(actual - expected) > tolerance:
        raise AssertionError(f"{label}: actual={actual}, expected={expected}, tol={tolerance}")


def central_difference(function, x: float, h: float = 1e-6) -> float:
    return (function(x + h) - function(x - h)) / (2.0 * h)


def main() -> None:
    p = Parameters()
    validate_parameters(p)
    z = 0.5

    # Consumer-side analytical derivatives.
    ds_numeric = central_difference(lambda zz: platform_share(zz, p), z)
    assert_close(ds_numeric, platform_share_derivative(z, p), 2e-8, "platform share derivative")
    dlogp_numeric = central_difference(lambda zz: math.log(consumer_price_index(zz, p)), z)
    assert_close(dlogp_numeric, -platform_share(z, p), 2e-8, "consumer price derivative")

    # Profit thresholds and complete organizational classification.
    gp = raw_platform_entry_threshold(z, p)
    gl0 = raw_local_entry_threshold(z, p)
    gx = raw_organization_switch_threshold(z, p)
    assert platform_intermediate_condition(p), "baseline must contain a platform-intermediate regime"
    if not gp < gl0 < gx:
        raise AssertionError(f"threshold ordering failed: GP={gp}, GL0={gl0}, GX={gx}")
    assert_close(producer_profit("P", z, gp, p), 0.0, 1e-10, "platform zero profit")
    assert_close(producer_profit("L", z, gl0, p), 0.0, 1e-10, "local zero profit")
    assert_close(
        producer_profit("L", z, gx, p) - producer_profit("P", z, gx, p),
        0.0,
        1e-10,
        "organization indifference",
    )
    expected_modes = [
        (max(0.0, gp - 0.03), "0" if gp > 0.03 else "P"),
        (0.5 * (max(0.0, gp) + gx), "P"),
        (gx + 0.05, "L"),
    ]
    for g, expected in expected_modes:
        actual = producer_choice(z, g, p)
        if actual != expected:
            raise AssertionError(f"regime classification at G={g}: {actual} != {expected}")

    # Stronger LCA (lower c) lowers entry and embedding thresholds.
    costs = np.linspace(0.55, 1.25, 25)
    entry = np.array([entry_threshold(z, replace(p, c=float(c))) for c in costs])
    organization = np.array([organization_threshold(z, replace(p, c=float(c))) for c in costs])
    raw_organization = np.array(
        [raw_organization_switch_threshold(z, replace(p, c=float(c))) for c in costs]
    )
    if np.any(np.diff(entry) < -1e-10):
        raise AssertionError("entry threshold is not weakly increasing in relative production cost")
    if np.any(np.diff(organization) < -1e-10):
        raise AssertionError("clipped organization threshold is not weakly increasing in relative cost")
    if np.any(np.diff(raw_organization) <= 0.0):
        raise AssertionError("raw organization threshold is not strictly increasing in relative cost")

    # Formula-based income effects match finite differences away from discrete cutoffs.
    for g in (0.10, 0.40, 0.80):
        if min(abs(g - gp), abs(g - gl0), abs(g - gx)) < 0.02:
            continue
        dlogy_numeric = central_difference(lambda zz: math.log(nominal_income(zz, g, p)), z)
        dlogr_numeric = central_difference(lambda zz: math.log(real_income(zz, g, p)), z)
        assert_close(dlogy_numeric, nominal_effect(z, g, p), 2e-7, f"nominal effect G={g}")
        assert_close(dlogr_numeric, real_effect(z, g, p), 2e-7, f"real effect G={g}")

    gr = real_income_threshold(z, p)
    gy = nominal_income_threshold(z, p)
    if not 0.0 < gr < gy < 1.5:
        raise AssertionError(f"baseline income thresholds are not ordered and interior: GR={gr}, GY={gy}")
    if abs(gr - gx) < 1e-4 or abs(gy - gx) < 1e-4:
        raise AssertionError("baseline income thresholds should not coincide with organization switching")

    # The capture drag vanishes when both consumer channels have the same local content.
    no_gap = replace(p, ell_p=p.ell_a)
    assert_close(capture_drag(z, no_gap), 0.0, 1e-14, "capture-gap closure")
    reverse_gap = replace(p, ell_p=min(1.0, p.ell_a + 0.10))
    if capture_drag(z, reverse_gap) >= 0.0:
        raise AssertionError("capture drag must reverse sign when the platform channel retains more")

    # Partial localization raises platform retention and local platform income.
    partial_local = replace(p, platform_localization=0.50)
    full_local = replace(p, platform_localization=1.00)
    if not (
        producer_retention("P", p)
        < producer_retention("P", partial_local)
        < producer_retention("P", full_local)
    ):
        raise AssertionError("platform retention must rise with service localization")
    if not (
        local_producer_income("P", z, 0.40, p)
        < local_producer_income("P", z, 0.40, partial_local)
        < local_producer_income("P", z, 0.40, full_local)
    ):
        raise AssertionError("platform local income must rise with service localization")

    # The platform-intermediate regime is conditional, not universal.
    low_fixed_cost = replace(p, big_f=0.05)
    if platform_intermediate_condition(low_fixed_cost):
        raise AssertionError("low local fixed cost should eliminate the platform-intermediate condition")
    if any(producer_choice(z, float(g), low_fixed_cost) == "P" for g in np.linspace(0.0, 1.5, 301)):
        raise AssertionError("platform mode should be absent when the local mode enters directly")

    # Removing access-infrastructure complementarity removes the G term from the z elasticity.
    no_complementarity = replace(p, chi=0.0)
    for g in (0.0, 0.4, 1.0):
        assert_close(
            producer_access_elasticity(g, no_complementarity),
            p.epsilon,
            1e-14,
            "access-infrastructure complementarity closure",
        )

    # Protection can favor localization only by worsening platform entry conditions.
    protected = replace(p, d_p=0.55)
    if raw_platform_entry_threshold(z, protected) <= gp:
        raise AssertionError("protection must raise the platform entry threshold")
    if raw_organization_switch_threshold(z, protected) >= gx:
        raise AssertionError("protection must lower the local-organization switch threshold")

    # Global income effects are nondecreasing in G, and real thresholds never exceed nominal ones.
    for zz in (0.20, 0.50, 0.80):
        for cost in (0.65, 0.80, 1.00):
            pc = replace(p, c=cost)
            grid = np.linspace(0.0, 2.0, 4001)
            ny = np.array([nominal_effect(zz, float(g), pc) for g in grid])
            nr = np.array([real_effect(zz, float(g), pc) for g in grid])
            if np.any(np.diff(ny) < -1e-9) or np.any(np.diff(nr) < -1e-9):
                raise AssertionError(f"income effects fall with G at z={zz}, c={cost}")
            gr_grid = real_income_threshold(zz, pc)
            gy_grid = nominal_income_threshold(zz, pc)
            if math.isfinite(gr_grid) and math.isfinite(gy_grid) and gr_grid > gy_grid + 1e-8:
                raise AssertionError(f"real threshold exceeds nominal threshold at z={zz}, c={cost}")

    # State participation raises infrastructure.
    participation = np.linspace(0.0, 1.0, 51)
    supplies = np.array([infrastructure_supply(float(v), p) for v in participation])
    if np.any(np.diff(supplies) <= 0.0):
        raise AssertionError("infrastructure supply must rise with state participation")
    for vartheta in (0.1, 0.5, 0.9):
        g = infrastructure_supply(vartheta, p)
        lhs = p.infrastructure_revenue_scale / (1.0 + g)
        rhs = financing_wedge(vartheta, p) * g
        assert_close(lhs, rhs, 1e-12, f"infrastructure FOC at participation={vartheta}")

    print("All analytical, boundary, and finite-difference checks passed.")
    print(f"GP={gp:.6f}, GL0={gl0:.6f}, GX={gx:.6f}")
    print(f"GR={gr:.6f}, GY={gy:.6f}")
    print(
        "State supply:",
        ", ".join(
            f"G({v:.1f})={infrastructure_supply(v, p):.4f}" for v in (0.1, 0.5, 0.9)
        ),
    )


if __name__ == "__main__":
    main()
