"""Numerical and algebraic checks for the Stage-2 seller-entry candidates.

This script is an internal theorem-feasibility check.  It does not compile or
modify the formal paper.  It uses only the Python standard library and a fixed
random seed so that every audit is reproducible.
"""

from __future__ import annotations

import math
import random


SEED = 20260714
TOL = 5.0e-8


def central_difference(function, point, step=1.0e-6):
    return (function(point + step) - function(point - step)) / (2.0 * step)


def platform_share(z, a, eta, p_a, p_bar):
    p_p = p_bar * math.exp(-z)
    numerator = a * p_p ** (1.0 - eta)
    denominator = (1.0 - a) * p_a ** (1.0 - eta) + numerator
    return numerator / denominator


def continuous_objects(z, parameters):
    (
        alpha,
        beta,
        rho_a,
        tau,
        mu,
        fixed_cost,
        outside_weight,
        base_income,
        e_bar,
        epsilon,
        a,
        eta,
        p_a,
        p_bar,
    ) = parameters

    s = platform_share(z, a, eta, p_a, p_bar)
    external_orders = e_bar * math.exp(epsilon * z)
    d0 = 1.0 - beta - alpha * rho_a * (1.0 - s)
    d1 = d0 - alpha * s * (1.0 - tau)
    access = external_orders + alpha * s * base_income / d0
    cutoff = fixed_cost * outside_weight / (mu * (1.0 - tau))

    if access <= cutoff:
        income = base_income / d0
        seller_mass = 0.0
        active = False
    else:
        income = (
            base_income
            + (1.0 - tau) * external_orders
            - fixed_cost * outside_weight / mu
        ) / d1
        seller_mass = (
            mu
            * (1.0 - tau)
            * d0
            * (access - cutoff)
            / (fixed_cost * d1)
        )
        active = True

    order_pool = external_orders + alpha * s * income
    routed_local = 0.0 if seller_mass == 0.0 else seller_mass / (
        seller_mass + outside_weight
    )
    income_rhs = (
        base_income
        + beta * income
        + rho_a * (1.0 - s) * alpha * income
        + (1.0 - tau) * routed_local * order_pool
    )
    profit = (
        mu * (1.0 - tau) * order_pool / (seller_mass + outside_weight)
        - fixed_cost
    )

    return {
        "s": s,
        "e": external_orders,
        "d0": d0,
        "d1": d1,
        "access": access,
        "cutoff": cutoff,
        "income": income,
        "seller_mass": seller_mass,
        "active": active,
        "order_pool": order_pool,
        "income_rhs": income_rhs,
        "profit": profit,
    }


def check_continuous_candidate(rng, draws=20_000):
    maximum_residual = 0.0
    maximum_derivative_error = 0.0
    active_count = 0

    for _ in range(draws):
        alpha = rng.uniform(0.15, 0.65)
        beta = rng.uniform(0.05, 0.9 - alpha)
        rho_a = rng.uniform(0.05, 1.0)
        tau = rng.uniform(0.01, 0.65)
        mu = rng.uniform(0.05, 0.8)
        fixed_cost = rng.uniform(0.05, 4.0)
        outside_weight = rng.uniform(0.1, 4.0)
        base_income = rng.uniform(0.5, 8.0)
        e_bar = rng.uniform(0.01, 3.0)
        epsilon = rng.uniform(0.02, 0.6)
        a = rng.uniform(0.1, 0.9)
        eta = rng.uniform(1.05, 6.0)
        p_a = rng.uniform(0.5, 2.0)
        p_bar = rng.uniform(0.5, 2.0)
        z = rng.uniform(-2.0, 2.0)
        parameters = (
            alpha,
            beta,
            rho_a,
            tau,
            mu,
            fixed_cost,
            outside_weight,
            base_income,
            e_bar,
            epsilon,
            a,
            eta,
            p_a,
            p_bar,
        )

        objects = continuous_objects(z, parameters)
        assert 0.0 < objects["s"] < 1.0
        assert objects["d0"] > 0.0
        assert objects["d1"] > 0.0
        assert objects["income"] > 0.0
        assert objects["seller_mass"] >= 0.0

        income_residual = abs(objects["income"] - objects["income_rhs"])
        maximum_residual = max(maximum_residual, income_residual)

        if objects["active"]:
            active_count += 1
            maximum_residual = max(maximum_residual, abs(objects["profit"]))
        else:
            assert objects["profit"] <= 1.0e-10

        # Check the derivative only away from the activation kink.
        if abs(objects["access"] - objects["cutoff"]) > 2.0e-3:
            numeric = central_difference(
                lambda value: continuous_objects(value, parameters)["income"], z
            )
            s = objects["s"]
            s_z = (eta - 1.0) * s * (1.0 - s)
            if not objects["active"]:
                analytic = -(
                    alpha
                    * rho_a
                    * s_z
                    * objects["income"]
                    / objects["d0"]
                )
            else:
                numerator = (
                    base_income
                    + (1.0 - tau) * objects["e"]
                    - fixed_cost * outside_weight / mu
                )
                analytic = (
                    (1.0 - tau)
                    * epsilon
                    * objects["e"]
                    * objects["d1"]
                    + alpha
                    * ((1.0 - tau) - rho_a)
                    * s_z
                    * numerator
                ) / objects["d1"] ** 2
            maximum_derivative_error = max(
                maximum_derivative_error, abs(numeric - analytic)
            )

    assert maximum_residual < TOL
    assert maximum_derivative_error < TOL
    assert active_count > 0
    return {
        "draws": draws,
        "active": active_count,
        "max_residual": maximum_residual,
        "max_derivative_error": maximum_derivative_error,
    }


def discrete_equilibrium_objects(parameters, entry_rate):
    beta, chi, ell, kappa, theta, f_low, f_high, external, base = parameters
    seller_retention = theta * (1.0 - kappa - ell)
    d0 = 1.0 - beta - chi * ell
    c = chi * seller_retention
    q_scale = (1.0 - beta) * external + chi * base
    income = (base + (ell + seller_retention * entry_rate) * external) / (
        d0 - c * entry_rate
    )
    market = external + chi * income
    seller_payoff = seller_retention * market
    if seller_payoff <= f_low:
        best_response = 0.0
    elif seller_payoff >= f_high:
        best_response = 1.0
    else:
        best_response = (seller_payoff - f_low) / (f_high - f_low)
    return income, market, seller_payoff, best_response, d0, c, q_scale


def check_discrete_candidate(rng, draws=100_000):
    overlap_count = 0
    maximum_fixed_point_residual = 0.0
    maximum_conservation_residual = 0.0

    for _ in range(draws):
        beta = rng.uniform(0.0, 0.7)
        chi = rng.uniform(0.02, 0.95 - beta)
        ell = rng.uniform(0.0, 0.7)
        kappa = rng.uniform(0.0, 0.9 - ell)
        theta = rng.uniform(0.05, 1.0)
        f_low = rng.uniform(0.02, 2.0)
        f_high = f_low + rng.uniform(0.02, 2.0)
        external = rng.uniform(0.0, 3.0)
        base = rng.uniform(0.02, 3.0)
        parameters = (
            beta,
            chi,
            ell,
            kappa,
            theta,
            f_low,
            f_high,
            external,
            base,
        )
        u = theta * (1.0 - kappa - ell)
        d0 = 1.0 - beta - chi * ell
        c = chi * u
        assert d0 - c > 0.0
        scale = u * ((1.0 - beta) * external + chi * base)
        m0 = f_low * d0
        m1 = f_high * (d0 - c)

        if m1 < scale < m0:
            overlap_count += 1
            delta_f = f_high - f_low
            discriminant = (
                (delta_f * d0 - c * f_low) ** 2
                + 4.0 * c * delta_f * (m0 - scale)
            )
            root = (
                delta_f * d0
                - c * f_low
                + math.sqrt(discriminant)
            ) / (2.0 * c * delta_f)
            assert 0.0 < root < 1.0
            income, market, payoff, best_response, *_ = discrete_equilibrium_objects(
                parameters, root
            )
            maximum_fixed_point_residual = max(
                maximum_fixed_point_residual, abs(root - best_response)
            )

            local_income = beta * income + (ell + u * root) * market
            external_income = (1.0 - beta - chi) * income + (
                1.0 - ell - u * root
            ) * market
            maximum_conservation_residual = max(
                maximum_conservation_residual,
                abs(local_income + external_income - (income + external)),
            )
            assert abs(payoff - (f_low + delta_f * root)) < TOL

    assert overlap_count > 0
    assert maximum_fixed_point_residual < TOL
    assert maximum_conservation_residual < TOL
    return {
        "draws": draws,
        "overlap": overlap_count,
        "max_fixed_point_residual": maximum_fixed_point_residual,
        "max_conservation_residual": maximum_conservation_residual,
    }


def check_ces_business_stealing(rng, draws=100_000):
    """Verify that standard symmetric CES dilution kills the complementarity.

    If each local seller's relative order density is h(n)=1/(n+nu), its
    business-stealing elasticity is n/(n+nu).  Strategic complementarity would
    require this elasticity to be smaller than chi*u*n*h(n)/d0, which reduces
    to d0 < chi*u.  Feasible expenditure shares imply the opposite strict
    inequality: d0-chi*u >= 1-beta-chi > 0.
    """

    smallest_gap = math.inf
    largest_payoff_derivative = -math.inf
    for _ in range(draws):
        beta = rng.uniform(0.0, 0.7)
        chi = rng.uniform(0.01, 0.99 - beta)
        ell = rng.uniform(0.0, 0.8)
        kappa = rng.uniform(0.0, 0.95 - ell)
        theta = rng.uniform(0.01, 1.0)
        u = theta * (1.0 - kappa - ell)
        d0 = 1.0 - beta - chi * ell
        nu = rng.uniform(0.05, 10.0)
        n = rng.uniform(1.0e-5, 1.0)
        h = 1.0 / (n + nu)
        elasticity = n / (n + nu)
        feedback_bound = chi * u * n * h / d0
        gap = elasticity - feedback_bound
        smallest_gap = min(smallest_gap, gap)
        assert d0 - chi * u >= 1.0 - beta - chi - 1.0e-14
        assert gap > 0.0

        # Sign of d log(per-seller payoff)/dn under the generalized model.
        log_derivative_numerator = chi * u * n * h - elasticity * d0
        largest_payoff_derivative = max(
            largest_payoff_derivative, log_derivative_numerator
        )
        assert log_derivative_numerator < 0.0

    return {
        "draws": draws,
        "min_elasticity_gap": smallest_gap,
        "max_log_derivative_numerator": largest_payoff_derivative,
    }


def rent_receipt_objects(local_share, parameters):
    (
        alpha,
        beta,
        rho_a,
        tau,
        mu,
        fixed_cost,
        outside_weight,
        base_income,
        external_orders,
        platform_share_value,
    ) = parameters
    phi = alpha * platform_share_value
    c0 = beta + alpha * rho_a * (1.0 - platform_share_value)
    d_bar = 1.0 - c0
    d0 = d_bar - local_share * tau * phi
    d1 = d0 - (1.0 - tau) * phi
    q_e = fixed_cost * outside_weight / (mu * (1.0 - tau))
    q0 = external_orders + phi * base_income / d0

    if q0 <= q_e:
        income = base_income / d0
        seller_mass = 0.0
        active = False
    else:
        income = (
            base_income + (1.0 - tau) * (external_orders - q_e)
        ) / d1
        order_pool = external_orders + phi * income
        seller_mass = (
            mu * (1.0 - tau) * (order_pool - q_e) / fixed_cost
        )
        active = True

    order_pool = external_orders + phi * income
    theta = 0.0 if seller_mass == 0.0 else seller_mass / (
        seller_mass + outside_weight
    )
    income_rhs = (
        base_income
        + c0 * income
        + local_share * tau * phi * income
        + (1.0 - tau) * theta * order_pool
    )
    profit = (
        mu
        * (1.0 - tau)
        * order_pool
        / (seller_mass + outside_weight)
        - fixed_cost
    )
    return {
        "phi": phi,
        "c0": c0,
        "d_bar": d_bar,
        "d0": d0,
        "d1": d1,
        "q_e": q_e,
        "q0": q0,
        "income": income,
        "seller_mass": seller_mass,
        "active": active,
        "order_pool": order_pool,
        "theta": theta,
        "income_rhs": income_rhs,
        "profit": profit,
    }


def check_rent_receipt_candidate(rng, draws=50_000):
    maximum_residual = 0.0
    maximum_derivative_error = 0.0
    maximum_mass_derivative_error = 0.0
    maximum_threshold_continuity_error = 0.0
    maximum_ledger_residual = 0.0
    maximum_fixed_cost_residual = 0.0
    maximum_branch_identity_residual = 0.0
    maximum_no_respending_mass_change = 0.0
    interior_thresholds = 0
    active_count = 0

    for _ in range(draws):
        alpha = rng.uniform(0.15, 0.70)
        beta = rng.uniform(0.02, 0.95 - alpha)
        rho_a = rng.uniform(0.05, 1.0)
        tau = rng.uniform(0.03, 0.70)
        mu = rng.uniform(0.05, 0.90)
        fixed_cost = rng.uniform(0.02, 3.0)
        outside_weight = rng.uniform(0.05, 4.0)
        base_income = rng.uniform(0.2, 8.0)
        external_orders = rng.uniform(0.0, 4.0)
        s = rng.uniform(0.05, 0.95)
        local_share = rng.uniform(0.0, 1.0)
        parameters = (
            alpha,
            beta,
            rho_a,
            tau,
            mu,
            fixed_cost,
            outside_weight,
            base_income,
            external_orders,
            s,
        )
        objects = rent_receipt_objects(local_share, parameters)
        assert objects["d0"] > 0.0
        assert objects["d1"] > 0.0
        assert objects["income"] > 0.0
        assert objects["seller_mass"] >= 0.0
        maximum_residual = max(
            maximum_residual,
            abs(objects["income"] - objects["income_rhs"]),
        )

        # Complete local-plus-external receipt ledger.
        local_receipts = (
            objects["c0"] * objects["income"]
            + local_share * tau * objects["phi"] * objects["income"]
            + (1.0 - tau) * objects["theta"] * objects["order_pool"]
        )
        external_receipts = (
            (1.0 - alpha - beta) * objects["income"]
            + alpha
            * (1.0 - s)
            * (1.0 - rho_a)
            * objects["income"]
            + (1.0 - local_share)
            * tau
            * objects["phi"]
            * objects["income"]
            + (1.0 - tau)
            * (1.0 - objects["theta"])
            * objects["phi"]
            * objects["income"]
            + tau * external_orders
            + (1.0 - tau)
            * (1.0 - objects["theta"])
            * external_orders
        )
        maximum_ledger_residual = max(
            maximum_ledger_residual,
            abs(
                local_receipts
                + external_receipts
                - (objects["income"] + external_orders)
            ),
        )

        # The two branch formulas must imply the same active-set sign.
        y1_candidate = (
            base_income
            + (1.0 - tau) * (external_orders - objects["q_e"])
        ) / objects["d1"]
        q1_candidate = external_orders + objects["phi"] * y1_candidate
        branch_identity_residual = abs(
            (q1_candidate - objects["q_e"])
            - objects["d0"]
            / objects["d1"]
            * (objects["q0"] - objects["q_e"])
        )
        maximum_branch_identity_residual = max(
            maximum_branch_identity_residual, branch_identity_residual
        )

        if objects["active"]:
            active_count += 1
            maximum_residual = max(maximum_residual, abs(objects["profit"]))
            seller_payout = (
                (1.0 - tau) * objects["theta"] * objects["order_pool"]
            )
            fixed_input_income = objects["seller_mass"] * fixed_cost
            maximum_fixed_cost_residual = max(
                maximum_fixed_cost_residual,
                abs(fixed_input_income - mu * seller_payout),
                abs(
                    fixed_input_income
                    + (1.0 - mu) * seller_payout
                    - seller_payout
                ),
            )
        else:
            assert objects["profit"] <= 1.0e-10

        if abs(objects["q0"] - objects["q_e"]) > 2.0e-3:
            numeric = central_difference(
                lambda value: rent_receipt_objects(value, parameters)["income"],
                local_share,
            )
            denominator = objects["d1"] if objects["active"] else objects["d0"]
            analytic = (
                tau
                * objects["phi"]
                * objects["income"]
                / denominator
            )
            maximum_derivative_error = max(
                maximum_derivative_error, abs(numeric - analytic)
            )
            if (
                objects["active"]
                and 1.0e-5 < local_share < 1.0 - 1.0e-5
            ):
                numeric_mass = central_difference(
                    lambda value: rent_receipt_objects(value, parameters)[
                        "seller_mass"
                    ],
                    local_share,
                )
                analytic_mass = (
                    mu
                    * (1.0 - tau)
                    * objects["phi"]
                    * analytic
                    / fixed_cost
                )
                maximum_mass_derivative_error = max(
                    maximum_mass_derivative_error,
                    abs(numeric_mass - analytic_mass)
                    / max(1.0, abs(numeric_mass), abs(analytic_mass)),
                )

        # Closed-form receipt-location threshold and its one-sided kink.
        if objects["q_e"] > external_orders:
            lambda_star = (
                objects["d_bar"]
                - objects["phi"]
                * base_income
                / (objects["q_e"] - external_orders)
            ) / (tau * objects["phi"])
            if 0.0 < lambda_star < 1.0:
                interior_thresholds += 1
                d0_star = objects["d_bar"] - lambda_star * tau * objects["phi"]
                d1_star = d0_star - (1.0 - tau) * objects["phi"]
                y0_star = base_income / d0_star
                y1_star = (
                    base_income
                    + (1.0 - tau) * (external_orders - objects["q_e"])
                ) / d1_star
                maximum_threshold_continuity_error = max(
                    maximum_threshold_continuity_error, abs(y0_star - y1_star)
                )
                left_slope = tau * objects["phi"] * y0_star / d0_star
                right_slope = tau * objects["phi"] * y1_star / d1_star
                assert right_slope > left_slope > 0.0
                right_mass_slope = (
                    mu
                    * (1.0 - tau)
                    * tau
                    * objects["phi"] ** 2
                    * y1_star
                    / (fixed_cost * d1_star)
                )
                assert right_mass_slope > 0.0

            q0_at_zero = rent_receipt_objects(0.0, parameters)["q0"]
            q0_at_one = rent_receipt_objects(1.0, parameters)["q0"]
            threshold_condition = q0_at_zero < objects["q_e"] < q0_at_one
            closed_form_condition = 0.0 < lambda_star < 1.0
            assert threshold_condition == closed_form_condition

        # With seller mass fixed, localization has a smaller smooth effect.
        if objects["active"] and objects["theta"] < 1.0:
            fixed_denominator = 1.0 - objects["c0"] - objects["phi"] * (
                local_share * tau + (1.0 - tau) * objects["theta"]
            )
            fixed_mass_effect = (
                tau
                * objects["phi"]
                * objects["income"]
                / fixed_denominator
            )
            endogenous_effect = (
                tau
                * objects["phi"]
                * objects["income"]
                / objects["d1"]
            )
            assert endogenous_effect > fixed_mass_effect > 0.0

        # Freeze resident platform orders: seller entry cannot depend on where
        # the buyer-side commission is received.
        fixed_resident_orders = objects["phi"] * base_income
        q_hat = external_orders + fixed_resident_orders
        n_hat_at_zero = max(
            mu * (1.0 - tau) * q_hat / fixed_cost - outside_weight, 0.0
        )
        n_hat_at_one = max(
            mu * (1.0 - tau) * q_hat / fixed_cost - outside_weight, 0.0
        )
        maximum_no_respending_mass_change = max(
            maximum_no_respending_mass_change,
            abs(n_hat_at_one - n_hat_at_zero),
        )

    assert active_count > 0
    assert interior_thresholds > 0
    assert maximum_residual < TOL
    assert maximum_derivative_error < TOL
    assert maximum_mass_derivative_error < TOL
    assert maximum_threshold_continuity_error < TOL
    assert maximum_ledger_residual < TOL
    assert maximum_fixed_cost_residual < TOL
    assert maximum_branch_identity_residual < TOL
    assert maximum_no_respending_mass_change == 0.0
    return {
        "draws": draws,
        "active": active_count,
        "interior_thresholds": interior_thresholds,
        "max_residual": maximum_residual,
        "max_derivative_error": maximum_derivative_error,
        "max_mass_derivative_relative_error": maximum_mass_derivative_error,
        "max_threshold_continuity_error": maximum_threshold_continuity_error,
        "max_ledger_residual": maximum_ledger_residual,
        "max_fixed_cost_residual": maximum_fixed_cost_residual,
        "max_branch_identity_residual": maximum_branch_identity_residual,
        "max_no_respending_mass_change": maximum_no_respending_mass_change,
    }


def check_phase_reversal_without_respender_feedback():
    """Exhibit phase reversal in a first-round accounting counterfactual.

    This is a deliberate falsification check: the original continuous model's
    sign reversal is not, by itself, evidence that local respending is needed.
    """

    alpha = 0.40
    rho_a = 0.80
    tau = 0.10
    base_income = 1.0
    s_z = 0.20
    external_order_growth = 0.05
    no_entry_slope = -alpha * rho_a * s_z * base_income
    active_slope = (
        (1.0 - tau) * external_order_growth
        + alpha * ((1.0 - tau) - rho_a) * s_z * base_income
    )
    assert no_entry_slope < 0.0 < active_slope
    return {
        "no_entry_slope": no_entry_slope,
        "active_slope": active_slope,
    }


def main():
    rng = random.Random(SEED)
    continuous = check_continuous_candidate(rng)
    discrete = check_discrete_candidate(rng)
    ces = check_ces_business_stealing(rng)
    rent_receipt = check_rent_receipt_candidate(rng)
    phase_reversal_counterexample = check_phase_reversal_without_respender_feedback()

    print("seller-entry candidate verification: PASS")
    print(f"seed: {SEED}")
    print(f"continuous: {continuous}")
    print(f"discrete: {discrete}")
    print(f"CES business stealing: {ces}")
    print(f"rent receipt x entry: {rent_receipt}")
    print(
        "phase reversal without respending feedback: "
        f"{phase_reversal_counterexample}"
    )


if __name__ == "__main__":
    main()
