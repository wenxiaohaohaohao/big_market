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
    income_denominator,
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
    if income_denominator(z, p) < 1.0 - p.alpha_m - p.beta - 1e-14:
        raise AssertionError("income denominator must follow from expenditure-share restrictions")
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
    assert_close(gr, entry_threshold(z, p), 1e-12, "event-exact real threshold")
    access_elasticity = producer_access_elasticity(0.0, p)
    if access_elasticity <= capture_drag(z, p):
        raise AssertionError("baseline high-G endpoint must support a nominal threshold")
    if access_elasticity + p.alpha_m * platform_share(z, p) <= capture_drag(z, p):
        raise AssertionError("baseline high-G endpoint must support a real threshold")
    if abs(gy - gx) < 1e-4:
        raise AssertionError("baseline nominal threshold should not coincide with organization switching")

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
    low_fixed_cost = replace(p, big_f=0.05, market0=0.50)
    if platform_intermediate_condition(low_fixed_cost):
        raise AssertionError("low local fixed cost should eliminate the platform-intermediate condition")
    low_gl0 = max(0.0, raw_local_entry_threshold(z, low_fixed_cost))
    assert_close(
        organization_threshold(z, low_fixed_cost),
        low_gl0,
        1e-12,
        "direct-local organization threshold",
    )
    if any(producer_choice(z, float(g), low_fixed_cost) == "P" for g in np.linspace(0.0, 1.5, 301)):
        raise AssertionError("platform mode should be absent when the local mode enters directly")

    # The baseline excludes access-infrastructure complementarity. A positive
    # extension term raises the z elasticity more at higher infrastructure.
    no_complementarity = replace(p, chi_extension=0.0)
    for g in (0.0, 0.4, 1.0):
        assert_close(
            producer_access_elasticity(g, no_complementarity),
            (p.sigma - 1.0) * p.psi,
            1e-14,
            "baseline producer-access elasticity",
        )
    positive_complementarity = replace(p, chi_extension=0.20)
    if producer_access_elasticity(1.0, positive_complementarity) <= producer_access_elasticity(
        0.0, positive_complementarity
    ):
        raise AssertionError("positive complementarity must raise the z elasticity with G")

    # A narrow external-channel restriction can favor localization only by
    # worsening platform entry and consumer access. It is not the general NSE
    # concept of protecting a nonviable sector.
    restricted = replace(p, d_p=0.50, consumer_platform_wedge=1.10)
    if raw_platform_entry_threshold(z, restricted) <= gp:
        raise AssertionError("the restriction must raise the platform entry threshold")
    if raw_organization_switch_threshold(z, restricted) >= gx:
        raise AssertionError("the restriction must lower the local-organization switch threshold")
    baseline_policy_g = 0.80
    facilitated_g = 1.15
    if producer_choice(z, baseline_policy_g, p) != "P":
        raise AssertionError("policy baseline must remain platform dependent")
    if producer_choice(z, facilitated_g, p) != "L":
        raise AssertionError("facilitation must attain local embeddedness")
    if producer_choice(z, baseline_policy_g, restricted) != "L":
        raise AssertionError("restriction comparison must attain the same local organization")
    if consumer_price_index(z, restricted) <= consumer_price_index(z, p):
        raise AssertionError("the restriction must worsen consumer access")
    if platform_share(z, restricted) >= platform_share(z, p):
        raise AssertionError("the restriction must reduce the consumer platform share")
    for mode in ("P", "L"):
        if producer_profit(mode, z, facilitated_g, p) <= producer_profit(
            mode, z, baseline_policy_g, p
        ):
            raise AssertionError("facilitation must raise producer profit in both modes")
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

    # Minimum state-enabled infrastructure additions inherit the structural
    # threshold ordering without importing a separate financing model.
    initial_g = 0.18
    facilitating_targets = {
        "E": entry_threshold(z, p),
        "L": organization_threshold(z, p),
        "R": gr,
        "Y": gy,
    }
    facilitating_increments = {
        name: max(0.0, target - initial_g)
        for name, target in facilitating_targets.items()
    }
    if not (
        facilitating_increments["E"]
        <= facilitating_increments["R"]
        <= facilitating_increments["Y"]
        <= facilitating_increments["L"]
    ):
        raise AssertionError(
            f"unexpected facilitating-increment ordering: {facilitating_increments}"
        )
    stronger_lca = replace(p, c=0.80)
    stronger_targets = {
        "E": entry_threshold(z, stronger_lca),
        "L": organization_threshold(z, stronger_lca),
        "R": real_income_threshold(z, stronger_lca),
        "Y": nominal_income_threshold(z, stronger_lca),
    }
    for name, target in stronger_targets.items():
        stronger_increment = max(0.0, target - initial_g)
        if stronger_increment > facilitating_increments[name] + 1e-10:
            raise AssertionError(
                f"stronger LCA raises the facilitating requirement for {name}"
            )

    print("All analytical, boundary, and finite-difference checks passed.")
    print(f"GP={gp:.6f}, GL0={gl0:.6f}, GX={gx:.6f}")
    print(f"GR={gr:.6f}, GY={gy:.6f}")
    print(
        f"Minimum facilitating additions from G0={initial_g:.2f}:",
        ", ".join(
            f"I_{name}={value:.4f}"
            for name, value in facilitating_increments.items()
        ),
    )


if __name__ == "__main__":
    main()
