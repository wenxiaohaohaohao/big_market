"""Core functions for the NSE illustrative numerical exercises.

The module implements the exact equations stated in the paper. Continuous
thresholds are bracketed on a bounded grid and then solved with SciPy's Brent
method; discrete organization switches remain explicit. All parameters are
illustrative and normalized.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from math import exp, log, sqrt
from typing import Iterable

import numpy as np
from scipy.optimize import brentq


@dataclass(frozen=True)
class Parameters:
    # Household and consumer-channel block
    alpha_m: float = 0.35
    beta: float = 0.30
    eta: float = 6.0
    a_platform: float = 0.40
    p_a: float = 1.0
    p_p_bar: float = 1.20
    consumer_platform_wedge: float = 1.0
    ell_a: float = 0.70
    ell_p: float = 0.10

    # Producer block
    sigma: float = 4.0
    b0: float = 1.0
    market0: float = 5.0
    psi: float = 0.19
    gamma: float = 0.10
    # Optional extension: platform access and public infrastructure can have
    # increasing differences. The paper's baseline sets this term to zero.
    chi_extension: float = 0.0
    c: float = 0.90
    d_p: float = 0.40
    d_l: float = 0.10
    f: float = 0.34
    big_f: float = 0.53
    platform_localization: float = 0.0

    # Enabling-state block
    kappa_private: float = 4.0
    kappa_government: float = 0.30
    infrastructure_revenue_scale: float = 0.80


def validate_parameters(p: Parameters) -> None:
    if not 0.0 < p.alpha_m < 1.0:
        raise ValueError("alpha_m must lie in (0,1)")
    if not 0.0 <= p.beta < 1.0 or p.alpha_m + p.beta >= 1.0:
        raise ValueError("alpha_m + beta must be less than one")
    if p.eta <= 1.0 or p.sigma <= 1.0:
        raise ValueError("eta and sigma must exceed one")
    if not 0.0 < p.a_platform < 1.0:
        raise ValueError("a_platform must lie in (0,1)")
    if p.consumer_platform_wedge <= 0.0:
        raise ValueError("consumer_platform_wedge must be positive")
    if not 0.0 <= p.ell_a <= 1.0 or not 0.0 <= p.ell_p <= 1.0:
        raise ValueError("local income contents must lie in [0,1]")
    if p.d_l >= p.d_p or p.d_l < 0.0:
        raise ValueError("the local mode requires 0 <= d_l < d_p")
    if min(p.c, p.f, p.big_f, p.market0, p.b0) <= 0.0:
        raise ValueError("cost, fixed-cost, market, and background-income terms must be positive")
    if min(p.psi, p.gamma, p.chi_extension) < 0.0:
        raise ValueError("producer-access cost effects must be nonnegative")
    if not 0.0 <= p.platform_localization <= 1.0:
        raise ValueError("platform_localization must lie in [0,1]")
    if not 0.0 < p.kappa_government < p.kappa_private:
        raise ValueError("government financing wedge must be below the private wedge")


def markup(p: Parameters) -> float:
    return p.sigma / (p.sigma - 1.0)


def operating_profit_coefficient(p: Parameters) -> float:
    mu = markup(p)
    return mu ** (1.0 - p.sigma) / p.sigma


def platform_price(z: float, p: Parameters) -> float:
    return p.consumer_platform_wedge * p.p_p_bar * exp(-z)


def platform_share(z: float, p: Parameters) -> float:
    pp = platform_price(z, p)
    numerator = p.a_platform * pp ** (1.0 - p.eta)
    denominator = (1.0 - p.a_platform) * p.p_a ** (1.0 - p.eta) + numerator
    return numerator / denominator


def platform_share_derivative(z: float, p: Parameters) -> float:
    s = platform_share(z, p)
    return (p.eta - 1.0) * s * (1.0 - s)


def consumer_price_index(z: float, p: Parameters) -> float:
    pp = platform_price(z, p)
    inside = (
        (1.0 - p.a_platform) * p.p_a ** (1.0 - p.eta)
        + p.a_platform * pp ** (1.0 - p.eta)
    )
    return inside ** (1.0 / (1.0 - p.eta))


def consumer_retention(z: float, p: Parameters) -> float:
    s = platform_share(z, p)
    return (1.0 - s) * p.ell_a + s * p.ell_p


def income_denominator(z: float, p: Parameters) -> float:
    return 1.0 - p.beta - p.alpha_m * consumer_retention(z, p)


def capture_drag(z: float, p: Parameters) -> float:
    return (
        p.alpha_m
        * (p.ell_a - p.ell_p)
        * platform_share_derivative(z, p)
        / income_denominator(z, p)
    )


def producer_market_access(z: float, g: float, p: Parameters) -> float:
    exponent = (p.sigma - 1.0) * (
        p.psi * z + p.gamma * g + p.chi_extension * z * g
    )
    return p.market0 * exp(exponent)


def producer_access_elasticity(g: float, p: Parameters) -> float:
    return (p.sigma - 1.0) * (p.psi + p.chi_extension * g)


def marginal_cost(mode: str, p: Parameters) -> float:
    if mode == "P":
        return p.c + p.d_p
    if mode == "L":
        return p.c + p.d_l
    raise ValueError(f"unknown producer mode: {mode}")


def fixed_cost(mode: str, p: Parameters) -> float:
    if mode == "P":
        return p.f
    if mode == "L":
        return p.f + p.big_f
    raise ValueError(f"unknown producer mode: {mode}")


def producer_revenue(mode: str, z: float, g: float, p: Parameters) -> float:
    mu = markup(p)
    market = producer_market_access(z, g, p)
    return market * mu ** (1.0 - p.sigma) * marginal_cost(mode, p) ** (1.0 - p.sigma)


def producer_profit(mode: str, z: float, g: float, p: Parameters) -> float:
    return producer_revenue(mode, z, g, p) / p.sigma - fixed_cost(mode, p)


def producer_choice(z: float, g: float, p: Parameters) -> str:
    profits = {"0": 0.0, "P": producer_profit("P", z, g, p), "L": producer_profit("L", z, g, p)}
    # At exact ties, select the mode with greater local embeddedness.
    return max(("0", "P", "L"), key=lambda mode: (profits[mode], {"0": 0, "P": 1, "L": 2}[mode]))


def producer_retention(mode: str, p: Parameters) -> float:
    if mode == "0":
        return 0.0
    if mode == "L":
        return 1.0
    mu = markup(p)
    external_share = (1.0 - p.platform_localization) * p.d_p / (mu * (p.c + p.d_p))
    return 1.0 - external_share


def local_producer_income(mode: str, z: float, g: float, p: Parameters) -> float:
    if mode == "0":
        return 0.0
    return producer_retention(mode, p) * producer_revenue(mode, z, g, p)


def nominal_income(z: float, g: float, p: Parameters) -> float:
    mode = producer_choice(z, g, p)
    autonomous = p.b0 + local_producer_income(mode, z, g, p)
    return autonomous / income_denominator(z, p)


def real_income(z: float, g: float, p: Parameters) -> float:
    return nominal_income(z, g, p) / consumer_price_index(z, p) ** p.alpha_m


def industry_income_share(z: float, g: float, p: Parameters) -> float:
    mode = producer_choice(z, g, p)
    bj = local_producer_income(mode, z, g, p)
    return bj / (p.b0 + bj)


def nominal_effect(z: float, g: float, p: Parameters) -> float:
    zeta = industry_income_share(z, g, p)
    return zeta * producer_access_elasticity(g, p) - capture_drag(z, p)


def real_effect(z: float, g: float, p: Parameters) -> float:
    return nominal_effect(z, g, p) + p.alpha_m * platform_share(z, p)


def _raw_mode_threshold(mode: str, z: float, p: Parameters) -> float:
    omega = (p.sigma - 1.0) * (p.gamma + p.chi_extension * z)
    if omega <= 0.0:
        return np.inf
    coefficient = operating_profit_coefficient(p)
    numerator = log(
        fixed_cost(mode, p)
        / (
            coefficient
            * p.market0
            * exp((p.sigma - 1.0) * p.psi * z)
            * marginal_cost(mode, p) ** (1.0 - p.sigma)
        )
    )
    return numerator / omega


def raw_platform_entry_threshold(z: float, p: Parameters) -> float:
    return _raw_mode_threshold("P", z, p)


def raw_local_entry_threshold(z: float, p: Parameters) -> float:
    return _raw_mode_threshold("L", z, p)


def raw_organization_switch_threshold(z: float, p: Parameters) -> float:
    omega = (p.sigma - 1.0) * (p.gamma + p.chi_extension * z)
    if omega <= 0.0:
        return np.inf
    coefficient = operating_profit_coefficient(p)
    delta_b = marginal_cost("L", p) ** (1.0 - p.sigma) - marginal_cost("P", p) ** (
        1.0 - p.sigma
    )
    numerator = log(
        p.big_f
        / (
            coefficient
            * p.market0
            * exp((p.sigma - 1.0) * p.psi * z)
            * delta_b
        )
    )
    return numerator / omega


def entry_threshold(z: float, p: Parameters) -> float:
    return max(0.0, min(raw_platform_entry_threshold(z, p), raw_local_entry_threshold(z, p)))


def organization_threshold(z: float, p: Parameters) -> float:
    if platform_intermediate_condition(p):
        raw = raw_organization_switch_threshold(z, p)
    else:
        # When the platform-dependent interval is absent, the local mode
        # becomes the equilibrium organization at its own zero-profit point.
        raw = raw_local_entry_threshold(z, p)
    return max(0.0, raw)


def platform_intermediate_condition(p: Parameters) -> bool:
    coefficient = operating_profit_coefficient(p)
    b_p = coefficient * marginal_cost("P", p) ** (1.0 - p.sigma)
    b_l = coefficient * marginal_cost("L", p) ** (1.0 - p.sigma)
    f_bar = p.f * (b_l - b_p) / b_p
    return p.big_f > f_bar


def _minimal_effect_threshold(
    effect,
    z: float,
    p: Parameters,
    lower: float = 0.0,
    upper: float = 2.5,
    grid_size: int = 5001,
) -> float:
    del grid_size  # retained for API compatibility; thresholds are event-exact.
    if effect(z, lower, p) >= 0.0:
        return float(lower)

    structural_events = sorted(
        {
            float(lower),
            float(upper),
            *[
                float(value)
                for value in (entry_threshold(z, p), organization_threshold(z, p))
                if np.isfinite(value) and lower < value < upper
            ],
        }
    )

    for idx in range(len(structural_events) - 1):
        left = structural_events[idx]
        right = structural_events[idx + 1]
        interval_scale = max(1.0, abs(left), abs(right))
        event_epsilon = min(1e-9 * interval_scale, 0.01 * (right - left))
        probe_left = left if idx == 0 else left + event_epsilon
        probe_right = (
            right
            if idx == len(structural_events) - 2
            else right - event_epsilon
        )
        value_left = effect(z, probe_left, p)
        value_right = effect(z, probe_right, p)

        # If a discrete entry or organization switch makes the effect
        # nonnegative immediately to its right, the economic threshold is the
        # exact structural event, not the next point on an arbitrary grid.
        if value_left >= 0.0:
            return float(left)

        if value_right >= 0.0:
            return float(
                brentq(
                    lambda g: effect(z, float(g), p),
                    probe_left,
                    probe_right,
                    xtol=1e-12,
                    rtol=1e-12,
                )
            )

    return np.nan


def nominal_income_threshold(z: float, p: Parameters) -> float:
    return _minimal_effect_threshold(nominal_effect, z, p)


def real_income_threshold(z: float, p: Parameters) -> float:
    return _minimal_effect_threshold(real_effect, z, p)


def financing_wedge(vartheta: float, p: Parameters) -> float:
    if not 0.0 <= vartheta <= 1.0:
        raise ValueError("government participation must lie in [0,1]")
    return p.kappa_private - (p.kappa_private - p.kappa_government) * vartheta


def infrastructure_supply(vartheta: float, p: Parameters) -> float:
    """Unique solution to a/(1+G) = kappa(vartheta) G.

    Infrastructure revenue is a*log(1+G), and the real construction cost is
    G^2/2 multiplied by the financing wedge.
    """

    wedge = financing_wedge(vartheta, p)
    ratio = p.infrastructure_revenue_scale / wedge
    return 0.5 * (-1.0 + sqrt(1.0 + 4.0 * ratio))


def participation_threshold(target_g: float, p: Parameters) -> float:
    """Minimum state participation required to supply target_g.

    Returns zero if private provision already crosses the threshold and NaN
    if even full participation cannot cross it.
    """

    lower_supply = infrastructure_supply(0.0, p)
    upper_supply = infrastructure_supply(1.0, p)
    if target_g <= lower_supply:
        return 0.0
    if target_g > upper_supply:
        return np.nan
    return float(
        brentq(
            lambda vartheta: infrastructure_supply(float(vartheta), p) - target_g,
            0.0,
            1.0,
            xtol=1e-12,
            rtol=1e-12,
        )
    )


def with_cost(p: Parameters, c: float) -> Parameters:
    return replace(p, c=float(c))


def threshold_rows(
    costs: Iterable[float], z: float, p: Parameters
) -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for c in costs:
        pc = with_cost(p, c)
        rows.append(
            {
                "c": float(c),
                "G_E": entry_threshold(z, pc),
                "G_L": organization_threshold(z, pc),
                "G_R": real_income_threshold(z, pc),
                "G_Y": nominal_income_threshold(z, pc),
            }
        )
    return rows
