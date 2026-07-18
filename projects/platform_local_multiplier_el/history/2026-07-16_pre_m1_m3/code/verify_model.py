"""Deterministic checks for the access--capture analytical model.

The script uses only the Python standard library.  It verifies algebra,
comparative statics, threshold formulas, and limiting cases.  It is neither a
calibration nor an empirical exercise.  These computational checks complement,
but do not replace, the analytical proofs in the paper.
"""

from __future__ import annotations

import math
import random


SEED = 20260714
N_DRAWS = 10_000
N_PEAK_DRAWS = 5_000


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(x: float, y: float, rtol: float = 3e-6, atol: float = 3e-9) -> bool:
    return abs(x - y) <= atol + rtol * max(abs(x), abs(y))


def central_difference(function, x: float, h: float) -> float:
    return (function(x + h) - function(x - h)) / (2.0 * h)


def validate_parameters(p: dict[str, float]) -> None:
    require(p["alpha"] > 0.0, "alpha must be positive")
    require(p["beta"] > 0.0, "beta must be positive")
    require(p["alpha"] + p["beta"] < 1.0, "alpha + beta must be below one")
    require(0.0 < p["a"] < 1.0, "a must be interior")
    require(p["eta"] > 1.0, "eta must exceed one")
    require(p["p_a"] > 0.0 and p["bar_p"] > 0.0, "prices must be positive")
    require(p["bar_b"] > 0.0, "base income must be positive")
    require(p["epsilon"] >= 0.0, "epsilon must be nonnegative")
    require(0.0 <= p["rho_a"] <= 1.0, "rho_a must be in [0,1]")
    require(
        0.0 <= p["rho_p_low"] < p["rho_p_high"] <= 1.0,
        "platform-retention endpoints must be ordered in [0,1]",
    )
    require(0.0 <= p["kappa"] <= 1.0, "kappa must be in [0,1]")


def logsumexp2(x: float, y: float) -> float:
    maximum = max(x, y)
    return maximum + math.log(math.exp(x - maximum) + math.exp(y - maximum))


def ces_objects(p: dict[str, float], z: float) -> dict[str, float]:
    log_p_platform = math.log(p["bar_p"]) - z
    log_term_a = math.log(1.0 - p["a"]) + (1.0 - p["eta"]) * math.log(p["p_a"])
    log_term_p = math.log(p["a"]) + (1.0 - p["eta"]) * log_p_platform
    log_q = logsumexp2(log_term_a, log_term_p)
    log_p_m = log_q / (1.0 - p["eta"])
    s = math.exp(log_term_p - log_q)
    return {
        "p_platform": math.exp(log_p_platform),
        "p_m": math.exp(log_p_m),
        "s": s,
        "s_z": (p["eta"] - 1.0) * s * (1.0 - s),
    }


def platform_retention(p: dict[str, float], kappa: float) -> float:
    delta = p["rho_p_high"] - p["rho_p_low"]
    return p["rho_p_low"] + kappa * delta


def equilibrium(
    p: dict[str, float],
    z: float,
    g: float,
    kappa: float | None = None,
) -> dict[str, float]:
    if kappa is None:
        kappa = p["kappa"]
    ces = ces_objects(p, z)
    delta_rho = p["rho_p_high"] - p["rho_p_low"]
    rho_p = platform_retention(p, kappa)
    retention_gap = p["rho_a"] - rho_p
    omega = (1.0 - ces["s"]) * p["rho_a"] + ces["s"] * rho_p
    omega_z = -retention_gap * ces["s_z"]
    omega_kappa = ces["s"] * delta_rho
    base = p["bar_b"] * math.exp(p["epsilon"] * z)
    d = 1.0 - p["beta"] - p["alpha"] * omega
    y = (base + omega * g) / d
    gamma = 1.0 - p["alpha"] - p["beta"]
    utility_constant = (
        p["alpha"] ** p["alpha"]
        * p["beta"] ** p["beta"]
        * gamma ** gamma
    )
    real = utility_constant * y / ces["p_m"] ** p["alpha"]
    return {
        **ces,
        "rho_p": rho_p,
        "delta_rho": delta_rho,
        "retention_gap": retention_gap,
        "omega": omega,
        "omega_z": omega_z,
        "omega_kappa": omega_kappa,
        "base": base,
        "d": d,
        "y": y,
        "real": real,
        "kappa": kappa,
    }


def local_income_multiplier(alpha: float, beta: float, omega: float) -> float:
    return 1.0 / (1.0 - beta - alpha * omega)


def gross_spending_multiplier(alpha: float, beta: float, omega: float) -> float:
    return omega / (1.0 - beta - alpha * omega)


def capture_drag(p: dict[str, float], z: float, kappa: float) -> float:
    out = equilibrium(p, z, 0.0, kappa)
    return -p["alpha"] * out["omega_z"] / out["d"]


def drag_from_share(p: dict[str, float], kappa: float, s: float) -> float:
    """Evaluate Lambda(s,kappa) directly, independently of the CES z mapping."""
    require(0.0 <= s <= 1.0, "platform share must be in [0,1]")
    delta = p["rho_a"] - platform_retention(p, kappa)
    d_a = 1.0 - p["beta"] - p["alpha"] * p["rho_a"]
    denominator = d_a + p["alpha"] * s * delta
    require(denominator > 0.0, "drag denominator must be positive")
    return (
        p["alpha"]
        * delta
        * (p["eta"] - 1.0)
        * s
        * (1.0 - s)
        / denominator
    )


def drag_share_derivatives(
    p: dict[str, float],
    kappa: float,
    s: float,
) -> tuple[float, float]:
    """Return the analytical first and second s derivatives of Lambda."""
    require(0.0 <= s <= 1.0, "platform share must be in [0,1]")
    delta = p["rho_a"] - platform_retention(p, kappa)
    d_a = 1.0 - p["beta"] - p["alpha"] * p["rho_a"]
    b = p["alpha"] * delta
    h = p["eta"] - 1.0
    denominator = d_a + b * s
    require(denominator > 0.0, "drag derivative denominator must be positive")
    first = (
        b
        * h
        * (d_a * (1.0 - 2.0 * s) - b * s ** 2)
        / denominator ** 2
    )
    second = (
        -2.0
        * b
        * h
        * d_a
        * (d_a + b)
        / denominator ** 3
    )
    return first, second


def intermediate_peak_objects(
    p: dict[str, float],
    kappa: float,
) -> dict[str, float]:
    """Closed-form peak objects for the benchmark Delta(kappa)>0 case."""
    delta_rho = p["rho_p_high"] - p["rho_p_low"]
    delta = p["rho_a"] - platform_retention(p, kappa)
    require(delta > 0.0, "intermediate drag peak requires Delta(kappa) > 0")
    d_a = 1.0 - p["beta"] - p["alpha"] * p["rho_a"]
    b = p["alpha"] * delta
    h = p["eta"] - 1.0
    q = math.sqrt(1.0 + b / d_a)
    s_star = 1.0 / (1.0 + q)
    lambda_max = h * (q - 1.0) / (q + 1.0)
    s_star_kappa = (
        p["alpha"]
        * delta_rho
        / (2.0 * d_a * q * (1.0 + q) ** 2)
    )
    lambda_max_kappa = (
        -h
        * p["alpha"]
        * delta_rho
        / (d_a * q * (1.0 + q) ** 2)
    )
    lambda_s, lambda_ss = drag_share_derivatives(p, kappa, s_star)
    return {
        "delta": delta,
        "d_a": d_a,
        "b": b,
        "q": q,
        "s_star": s_star,
        "lambda_at_star": drag_from_share(p, kappa, s_star),
        "lambda_max": lambda_max,
        "lambda_s": lambda_s,
        "lambda_ss": lambda_ss,
        "s_star_kappa": s_star_kappa,
        "lambda_max_kappa": lambda_max_kappa,
    }


def capacity_threshold(
    p: dict[str, float],
    z: float,
    q: float,
) -> float:
    out = equilibrium(p, z, 0.0, 0.0)
    s = out["s"]
    h = (p["eta"] - 1.0) * (1.0 - s)
    require(q >= 0.0 and h > q, "threshold requires 0 <= q < h(s)")
    d_a = 1.0 - p["beta"] - p["alpha"] * p["rho_a"]
    delta_star = q * d_a / (p["alpha"] * s * (h - q))
    delta_zero = p["rho_a"] - p["rho_p_low"]
    return (delta_zero - delta_star) / (p["rho_p_high"] - p["rho_p_low"])


def random_parameters(rng: random.Random) -> dict[str, float]:
    alpha = rng.uniform(0.04, 0.68)
    beta = rng.uniform(0.02, 0.96 - alpha)
    low = rng.uniform(0.0, 0.8)
    high = rng.uniform(low + 0.01, 1.0)
    return {
        "alpha": alpha,
        "beta": beta,
        "a": rng.uniform(0.03, 0.97),
        "eta": rng.uniform(1.05, 6.0),
        "p_a": rng.uniform(0.6, 2.2),
        "bar_p": rng.uniform(0.6, 2.2),
        "bar_b": rng.uniform(0.2, 6.0),
        "epsilon": rng.uniform(0.0, 0.8),
        "rho_a": rng.uniform(0.0, 1.0),
        "rho_p_low": low,
        "rho_p_high": high,
        "kappa": rng.uniform(0.05, 0.95),
    }


def random_peak_parameters(rng: random.Random) -> dict[str, float]:
    """Draw legal parameters with Delta(kappa)>0 by construction."""
    p = random_parameters(rng)
    low = rng.uniform(0.0, 0.50)
    high = rng.uniform(low + 0.05, 0.85)
    kappa = rng.uniform(0.05, 0.90)
    rho_p = low + kappa * (high - low)
    p.update({
        "rho_p_low": low,
        "rho_p_high": high,
        "kappa": kappa,
        "rho_a": rng.uniform(rho_p + 0.01, 1.0),
    })
    return p


def check_random_draws() -> dict[str, float]:
    rng = random.Random(SEED)
    maxima = {
        "fixed_point": 0.0,
        "z_derivative": 0.0,
        "kappa_derivative": 0.0,
    }
    for draw in range(N_DRAWS):
        p = random_parameters(rng)
        validate_parameters(p)
        # Keep random draws away from machine-precision share corners.  The
        # mathematical z-limits are checked separately below.
        z = rng.uniform(-3.0, 3.0)
        g = rng.uniform(0.0, 5.0)
        out = equilibrium(p, z, g)

        require(0.0 < out["s"] < 1.0, f"share interiority failed at draw {draw}")
        require(0.0 <= out["rho_p"] <= 1.0, f"rho_p bound failed at draw {draw}")
        require(0.0 <= out["omega"] <= 1.0, f"omega bound failed at draw {draw}")
        require(
            out["d"] >= 1.0 - p["alpha"] - p["beta"] > 0.0,
            f"denominator bound failed at draw {draw}",
        )
        require(out["y"] > 0.0 and out["real"] > 0.0, f"positivity failed at draw {draw}")

        rhs = (
            out["base"]
            + p["beta"] * out["y"]
            + out["omega"] * (p["alpha"] * out["y"] + g)
        )
        residual = abs(out["y"] - rhs)
        maxima["fixed_point"] = max(maxima["fixed_point"], residual)
        require(close(out["y"], rhs, rtol=2e-10, atol=2e-10),
                f"fixed-point identity failed at draw {draw}")

        for initial in (0.0, out["y"], 100.0 * out["y"]):
            iterate = initial
            for _ in range(2500):
                updated = (
                    out["base"]
                    + out["omega"] * g
                    + (p["beta"] + p["alpha"] * out["omega"]) * iterate
                )
                if close(updated, iterate, rtol=1e-11, atol=1e-11):
                    iterate = updated
                    break
                iterate = updated
            require(close(iterate, out["y"], rtol=1e-8),
                    f"global fixed-point convergence failed at draw {draw}")

        m_target = rng.uniform(0.1, 5.0)
        m_a = (
            (1.0 - p["a"])
            * (p["p_a"] / out["p_m"]) ** (-p["eta"])
            * m_target
        )
        m_p = (
            p["a"]
            * (out["p_platform"] / out["p_m"]) ** (-p["eta"])
            * m_target
        )
        ces_power = (p["eta"] - 1.0) / p["eta"]
        ces_quantity = (
            (1.0 - p["a"]) ** (1.0 / p["eta"]) * m_a ** ces_power
            + p["a"] ** (1.0 / p["eta"]) * m_p ** ces_power
        ) ** (1.0 / ces_power)
        require(close(ces_quantity, m_target), f"Hicksian quantity failed at draw {draw}")
        require(
            close(
                p["p_a"] * m_a + out["p_platform"] * m_p,
                out["p_m"] * m_target,
            ),
            f"unit expenditure failed at draw {draw}",
        )
        require(
            close(out["p_platform"] * m_p / (out["p_m"] * m_target), out["s"]),
            f"platform expenditure share failed at draw {draw}",
        )

        h_z = 2e-6
        numeric_log_pm = central_difference(
            lambda zz: math.log(equilibrium(p, zz, g)["p_m"]), z, h_z
        )
        numeric_s = central_difference(lambda zz: equilibrium(p, zz, g)["s"], z, h_z)
        numeric_omega_z = central_difference(
            lambda zz: equilibrium(p, zz, g)["omega"], z, h_z
        )
        require(close(numeric_log_pm, -out["s"]), f"price derivative failed at draw {draw}")
        require(close(numeric_s, out["s_z"]), f"share derivative failed at draw {draw}")
        require(close(numeric_omega_z, out["omega_z"]),
                f"omega-z derivative failed at draw {draw}")

        general_log_y_z = (
            (p["epsilon"] * out["base"] + out["omega_z"] * g)
            / (out["base"] + out["omega"] * g)
            + p["alpha"] * out["omega_z"] / out["d"]
        )
        numeric_log_y_z = central_difference(
            lambda zz: math.log(equilibrium(p, zz, g)["y"]), z, h_z
        )
        numeric_log_r_z = central_difference(
            lambda zz: math.log(equilibrium(p, zz, g)["real"]), z, h_z
        )
        maxima["z_derivative"] = max(
            maxima["z_derivative"], abs(numeric_log_y_z - general_log_y_z)
        )
        require(close(numeric_log_y_z, general_log_y_z, rtol=5e-6),
                f"general z derivative failed at draw {draw}")
        require(close(numeric_log_r_z, general_log_y_z + p["alpha"] * out["s"],
                      rtol=5e-6),
                f"real-income z derivative failed at draw {draw}")

        h_k = 2e-6
        numeric_omega_k = central_difference(
            lambda kk: equilibrium(p, z, g, kk)["omega"], out["kappa"], h_k
        )
        general_log_y_k = out["omega_kappa"] * (
            g / (out["base"] + out["omega"] * g) + p["alpha"] / out["d"]
        )
        numeric_log_y_k = central_difference(
            lambda kk: math.log(equilibrium(p, z, g, kk)["y"]), out["kappa"], h_k
        )
        numeric_log_r_k = central_difference(
            lambda kk: math.log(equilibrium(p, z, g, kk)["real"]), out["kappa"], h_k
        )
        maxima["kappa_derivative"] = max(
            maxima["kappa_derivative"], abs(numeric_log_y_k - general_log_y_k)
        )
        require(close(numeric_omega_k, out["omega_kappa"]),
                f"omega-kappa derivative failed at draw {draw}")
        require(close(numeric_log_y_k, general_log_y_k, rtol=5e-6),
                f"income-kappa derivative failed at draw {draw}")
        require(close(numeric_log_r_k, general_log_y_k, rtol=5e-6),
                f"real-income-kappa derivative failed at draw {draw}")
        require(general_log_y_k > 0.0, f"capacity monotonicity failed at draw {draw}")

        multiplier = gross_spending_multiplier(p["alpha"], p["beta"], out["omega"])
        m_b = local_income_multiplier(p["alpha"], p["beta"], out["omega"])
        h_g = 2e-6 * max(1.0, g)
        numeric_y_g = central_difference(
            lambda gg: equilibrium(p, z, gg)["y"], g, h_g
        )
        require(close(numeric_y_g, multiplier),
                f"gross-spending multiplier failed at draw {draw}")
        require(close(multiplier, out["omega"] * m_b),
                f"multiplier decomposition failed at draw {draw}")

        m0_times_omega = out["omega"] / (1.0 - p["alpha"] - p["beta"])
        require(multiplier <= m0_times_omega + 1e-12,
                f"multiplier upper bound failed at draw {draw}")
        if 1e-9 < out["omega"] < 1.0 - 1e-9:
            require(multiplier < m0_times_omega,
                    f"strict multiplier comparison failed at draw {draw}")
            retention_elasticity = (1.0 - p["beta"]) / out["d"]
            require(retention_elasticity > 1.0,
                    f"retention elasticity failed at draw {draw}")
            numeric_log_m_k = central_difference(
                lambda kk: math.log(
                    gross_spending_multiplier(
                        p["alpha"], p["beta"], equilibrium(p, z, g, kk)["omega"]
                    )
                ),
                out["kappa"],
                h_k,
            )
            analytic_log_m_k = (
                (1.0 - p["beta"]) * out["omega_kappa"]
                / (out["omega"] * out["d"])
            )
            require(close(numeric_log_m_k, analytic_log_m_k, rtol=6e-6),
                    f"capacity-multiplier semi-elasticity failed at draw {draw}")

        out_g0 = equilibrium(p, z, 0.0)
        drag = capture_drag(p, z, out["kappa"])
        require(close(
            central_difference(
                lambda zz: math.log(equilibrium(p, zz, 0.0)["y"]), z, h_z
            ),
            p["epsilon"] - drag,
            rtol=5e-6,
        ), f"G=0 nominal decomposition failed at draw {draw}")

        z1 = z + rng.uniform(0.05, 1.0)
        first = equilibrium(p, z, 0.0)
        second = equilibrium(p, z1, 0.0)
        b_ratio = second["base"] / first["base"]
        d_ratio = second["d"] / first["d"]
        p_ratio = second["p_m"] / first["p_m"]
        require(close(second["y"] / first["y"], b_ratio / d_ratio),
                f"finite nominal ratio failed at draw {draw}")
        require(close(
            second["real"] / first["real"],
            b_ratio / (d_ratio * p_ratio ** p["alpha"]),
        ), f"finite real ratio failed at draw {draw}")
        require(
            not (second["y"] > first["y"] and second["real"] < first["real"]),
            f"impossible finite sign pattern at draw {draw}",
        )

        first_g = equilibrium(p, z, g)
        second_g = equilibrium(p, z1, g)
        numerator_ratio = (
            (second_g["base"] + second_g["omega"] * g)
            / (first_g["base"] + first_g["omega"] * g)
        )
        d_ratio_g = second_g["d"] / first_g["d"]
        p_ratio_g = second_g["p_m"] / first_g["p_m"]
        require(close(second_g["y"] / first_g["y"], numerator_ratio / d_ratio_g),
                f"G>0 finite nominal ratio failed at draw {draw}")
        require(close(
            second_g["real"] / first_g["real"],
            numerator_ratio / (d_ratio_g * p_ratio_g ** p["alpha"]),
        ), f"G>0 finite real ratio failed at draw {draw}")

    return maxima


def check_intermediate_penetration_peak() -> dict[str, float]:
    """Numerically audit the closed-form peak for Delta(kappa)>0.

    The strict-concavity check evaluates the analytical second derivative on
    the full closed share interval.  Finite differences are used separately
    for the two kappa derivatives requested by the comparative statics.
    """
    rng = random.Random(SEED + 104729)
    maxima = {
        "foc": 0.0,
        "closed_form": 0.0,
        "ces_mapping": 0.0,
        "s_kappa_derivative": 0.0,
        "lambda_kappa_derivative": 0.0,
    }
    largest_lambda_ss = -math.inf
    smallest_half_gap = math.inf

    for draw in range(N_PEAK_DRAWS):
        p = random_peak_parameters(rng)
        validate_parameters(p)
        kappa = p["kappa"]
        peak = intermediate_peak_objects(p, kappa)

        require(0.0 < peak["s_star"] < 0.5,
                f"intermediate peak location failed at draw {draw}")
        require(peak["lambda_at_star"] > 0.0,
                f"positive peak value failed at draw {draw}")
        require(peak["s_star_kappa"] > 0.0,
                f"peak-location capacity sign failed at draw {draw}")
        require(peak["lambda_max_kappa"] < 0.0,
                f"peak-value capacity sign failed at draw {draw}")
        maxima["foc"] = max(maxima["foc"], abs(peak["lambda_s"]))
        require(abs(peak["lambda_s"]) < 2e-12,
                f"analytical peak FOC failed at draw {draw}")
        maxima["closed_form"] = max(
            maxima["closed_form"],
            abs(peak["lambda_at_star"] - peak["lambda_max"]),
        )
        require(close(
            peak["lambda_at_star"], peak["lambda_max"],
            rtol=2e-10, atol=2e-12,
        ), f"closed-form peak value failed at draw {draw}")

        # The formula for Lambda_ss is strictly negative for every s in [0,1]
        # when Delta(kappa)>0.  A grid evaluates the full interval, including
        # its endpoints, while the sign follows from the analytical formula.
        for index in range(101):
            s = index / 100.0
            _, lambda_ss = drag_share_derivatives(p, kappa, s)
            largest_lambda_ss = max(largest_lambda_ss, lambda_ss)
            require(lambda_ss < 0.0,
                    f"global strict concavity failed at draw {draw}, s={s}")
            require(
                peak["lambda_at_star"] >= drag_from_share(p, kappa, s) - 2e-12,
                f"global peak dominance failed at draw {draw}, s={s}",
            )
        left_slope, _ = drag_share_derivatives(
            p, kappa, 0.5 * peak["s_star"]
        )
        right_slope, _ = drag_share_derivatives(
            p, kappa, 0.5 * (1.0 + peak["s_star"])
        )
        require(left_slope > 0.0 > right_slope,
                f"unique peak slope pattern failed at draw {draw}")
        smallest_half_gap = min(smallest_half_gap, 0.5 - peak["s_star"])

        # Map the closed-form share back into z and recover the same drag from
        # the complete CES equilibrium, not only from the share representation.
        logit_s = math.log(peak["s_star"] / (1.0 - peak["s_star"]))
        logit_a = math.log(p["a"] / (1.0 - p["a"]))
        z_star = (
            math.log(p["bar_p"] / p["p_a"])
            + (logit_s - logit_a) / (p["eta"] - 1.0)
        )
        ces_gap = abs(capture_drag(p, z_star, kappa) - peak["lambda_max"])
        maxima["ces_mapping"] = max(maxima["ces_mapping"], ces_gap)
        require(ces_gap < 2e-11,
                f"CES peak mapping failed at draw {draw}")

        delta_rho = p["rho_p_high"] - p["rho_p_low"]
        h_kappa = min(
            2e-6,
            0.10 * kappa,
            0.10 * (1.0 - kappa),
            0.10 * peak["delta"] / delta_rho,
        )
        require(h_kappa > 0.0, f"invalid kappa step at draw {draw}")
        numeric_s_kappa = central_difference(
            lambda kk: intermediate_peak_objects(p, kk)["s_star"],
            kappa,
            h_kappa,
        )
        numeric_lambda_kappa = central_difference(
            lambda kk: intermediate_peak_objects(p, kk)["lambda_max"],
            kappa,
            h_kappa,
        )
        maxima["s_kappa_derivative"] = max(
            maxima["s_kappa_derivative"],
            abs(numeric_s_kappa - peak["s_star_kappa"]),
        )
        maxima["lambda_kappa_derivative"] = max(
            maxima["lambda_kappa_derivative"],
            abs(numeric_lambda_kappa - peak["lambda_max_kappa"]),
        )
        require(close(
            numeric_s_kappa, peak["s_star_kappa"], rtol=1e-5, atol=2e-8,
        ), f"peak-location kappa derivative failed at draw {draw}")
        require(close(
            numeric_lambda_kappa,
            peak["lambda_max_kappa"],
            rtol=1e-5,
            atol=2e-8,
        ), f"peak-value kappa derivative failed at draw {draw}")

    require(largest_lambda_ss < 0.0, "strict-concavity sign check failed")
    require(smallest_half_gap > 0.0, "peak must remain strictly below one half")

    # Delta(kappa) -> 0+: the unique interior peak approaches one half and its
    # height approaches zero.  At Delta=0, Lambda is identically zero, so no
    # unique peak exists and the Delta>0 helper must reject the case.
    boundary = {
        "alpha": 0.30,
        "beta": 0.20,
        "a": 0.40,
        "eta": 3.50,
        "p_a": 1.00,
        "bar_p": 1.00,
        "bar_b": 1.00,
        "epsilon": 0.10,
        "rho_a": 0.50,
        "rho_p_low": 0.20,
        "rho_p_high": 0.80,
        "kappa": 0.50,
    }
    validate_parameters(boundary)
    for index in range(101):
        s = index / 100.0
        first, second = drag_share_derivatives(boundary, 0.50, s)
        require(close(drag_from_share(boundary, 0.50, s), 0.0, atol=1e-14),
                "Delta=0 must imply Lambda identically zero")
        require(close(first, 0.0, atol=1e-14),
                "Delta=0 first share derivative must be zero")
        require(close(second, 0.0, atol=1e-14),
                "Delta=0 second share derivative must be zero")
    rejected_zero = False
    try:
        intermediate_peak_objects(boundary, 0.50)
    except AssertionError:
        rejected_zero = True
    require(rejected_zero, "Delta=0 must not be assigned a unique drag peak")

    previous_distance = math.inf
    previous_height = math.inf
    for gap in (1e-2, 1e-4, 1e-6):
        near_zero = dict(boundary, rho_a=0.50 + gap)
        peak = intermediate_peak_objects(near_zero, 0.50)
        distance = 0.5 - peak["s_star"]
        height = peak["lambda_max"]
        require(0.0 < distance < previous_distance,
                "Delta-to-zero peak location limit failed")
        require(0.0 < height < previous_height,
                "Delta-to-zero peak-height limit failed")
        previous_distance = distance
        previous_height = height
    require(previous_distance < 1e-6 and previous_height < 1e-6,
            "Delta-to-zero boundary is not numerically close enough")

    reverse = dict(boundary, rho_a=0.45)
    validate_parameters(reverse)
    require(all(
        drag_from_share(reverse, 0.50, index / 100.0) < 0.0
        for index in range(1, 100)
    ), "Delta<0 should produce a negative capture term in the interior")
    rejected_reverse = False
    try:
        intermediate_peak_objects(reverse, 0.50)
    except AssertionError:
        rejected_reverse = True
    require(rejected_reverse, "Delta<0 must not use the drag-peak proposition")

    return {
        **maxima,
        "largest_lambda_ss": largest_lambda_ss,
        "smallest_half_gap": smallest_half_gap,
    }


def check_capacity_thresholds() -> None:
    p = {
        "alpha": 0.30,
        "beta": 0.20,
        "a": 0.40,
        "eta": 5.0,
        "p_a": 1.0,
        "bar_p": 1.0,
        "bar_b": 1.0,
        "epsilon": 0.05,
        "rho_a": 0.90,
        "rho_p_low": 0.05,
        "rho_p_high": 0.95,
        "kappa": 0.50,
    }
    validate_parameters(p)
    z = 0.0
    out = equilibrium(p, z, 0.0)
    q_y = p["epsilon"]
    q_r = p["epsilon"] + p["alpha"] * out["s"]
    lambda_low = capture_drag(p, z, 0.0)
    lambda_high = capture_drag(p, z, 1.0)
    require(lambda_low > q_r > q_y > lambda_high,
            "fixture does not satisfy both endpoint-crossing conditions")

    kappa_r = capacity_threshold(p, z, q_r)
    kappa_y = capacity_threshold(p, z, q_y)
    require(0.0 < kappa_r < kappa_y < 1.0, "capacity-threshold ordering failed")
    require(close(capture_drag(p, z, kappa_r), q_r),
            "real-income threshold identity failed")
    require(close(capture_drag(p, z, kappa_y), q_y),
            "nominal-income threshold identity failed")

    for kappa, expected in (
        (0.5 * kappa_r, (-1, -1)),
        (0.5 * (kappa_r + kappa_y), (-1, 1)),
        (0.5 * (kappa_y + 1.0), (1, 1)),
    ):
        drag = capture_drag(p, z, kappa)
        nominal = p["epsilon"] - drag
        real = nominal + p["alpha"] * out["s"]
        signs = (1 if nominal > 0.0 else -1, 1 if real > 0.0 else -1)
        require(signs == expected, f"capacity sign region failed at kappa={kappa}")

    kappa = 0.43
    eq = equilibrium(p, z, 0.0, kappa)
    d_a = 1.0 - p["beta"] - p["alpha"] * p["rho_a"]
    analytic = (
        -p["alpha"]
        * (p["rho_p_high"] - p["rho_p_low"])
        * (p["eta"] - 1.0)
        * eq["s"]
        * (1.0 - eq["s"])
        * d_a
        / eq["d"] ** 2
    )
    numeric = central_difference(lambda kk: capture_drag(p, z, kk), kappa, 2e-6)
    require(close(numeric, analytic, rtol=5e-6),
            "capture-drag capacity derivative failed")
    require(analytic < 0.0, "capture drag must decrease in capacity")

    h = (p["eta"] - 1.0) * (1.0 - out["s"])
    require(h > q_r, "valid threshold must satisfy h(s) > q")


def check_finite_regions() -> None:
    alpha = 0.35
    d_ratio = 1.18
    p_ratio = 0.86
    lower = d_ratio * p_ratio ** alpha
    candidates = {
        "joint_gain": d_ratio * 1.05,
        "split": 0.5 * (lower + d_ratio),
        "joint_loss": lower * 0.95,
    }
    expected = {
        "joint_gain": (True, True),
        "split": (False, True),
        "joint_loss": (False, False),
    }
    for name, b_ratio in candidates.items():
        signs = (b_ratio / d_ratio > 1.0, b_ratio / lower > 1.0)
        require(signs == expected[name], f"finite {name} region failed")
    require(close(d_ratio / d_ratio, 1.0) and d_ratio / lower > 1.0,
            "upper equality boundary failed")
    require(lower / d_ratio < 1.0 and close(lower / lower, 1.0),
            "lower equality boundary failed")


def check_boundaries() -> None:
    p = {
        "alpha": 0.35,
        "beta": 0.25,
        "a": 0.40,
        "eta": 2.40,
        "p_a": 1.20,
        "bar_p": 1.10,
        "bar_b": 2.00,
        "epsilon": 0.20,
        "rho_a": 0.60,
        "rho_p_low": 0.20,
        "rho_p_high": 0.80,
        "kappa": 2.0 / 3.0,
    }
    z = 0.30
    equal = equilibrium(p, z, 0.0)
    require(close(equal["rho_p"], p["rho_a"]), "equal-retention fixture failed")
    require(close(equal["omega_z"], 0.0), "equal-retention z effect failed")

    reverse = equilibrium(p, z, 0.0, 1.0)
    reverse_later = equilibrium(p, z + 0.1, 0.0, 1.0)
    require(reverse["omega_z"] > 0.0, "reverse-retention derivative failed")
    require(reverse_later["y"] > reverse["y"] and reverse_later["real"] > reverse["real"],
            "reverse-retention income effect failed")

    p_zero = dict(p, rho_a=0.0, rho_p_low=0.0, rho_p_high=0.4)
    zero = equilibrium(p_zero, z, 1.0, 0.0)
    require(close(zero["omega"], 0.0), "zero-retention value failed")
    require(close(zero["y"], zero["base"] / (1.0 - p_zero["beta"])),
            "zero-retention income failed")
    require(close(gross_spending_multiplier(
        p_zero["alpha"], p_zero["beta"], zero["omega"]
    ), 0.0), "zero-retention multiplier failed")

    p_one = dict(p, rho_a=1.0, rho_p_low=0.5, rho_p_high=1.0)
    one = equilibrium(p_one, z, 1.0, 1.0)
    require(close(one["omega"], 1.0), "full-retention value failed")
    require(close(
        gross_spending_multiplier(p_one["alpha"], p_one["beta"], one["omega"]),
        1.0 / (1.0 - p_one["alpha"] - p_one["beta"]),
    ), "full-retention multiplier failed")

    p_eta = dict(p, eta=1.000001)
    eta_limit = equilibrium(p_eta, z, 0.0)
    p_platform = p_eta["bar_p"] * math.exp(-z)
    geometric_price = p_eta["p_a"] ** (1.0 - p_eta["a"]) * p_platform ** p_eta["a"]
    require(close(eta_limit["p_m"], geometric_price, rtol=3e-6),
            "Cobb-Douglas price limit failed")
    require(close(eta_limit["s"], p_eta["a"], rtol=3e-6),
            "Cobb-Douglas share limit failed")

    p_cheaper = dict(p, eta=80.0, p_a=1.0, bar_p=0.7)
    p_dearer = dict(p, eta=80.0, p_a=1.0, bar_p=1.3)
    p_equal = dict(p, eta=80.0, p_a=1.0, bar_p=1.0)
    require(equilibrium(p_cheaper, 0.0, 0.0)["s"] > 1.0 - 1e-10,
            "perfect-substitutes cheaper-platform limit failed")
    require(equilibrium(p_dearer, 0.0, 0.0)["s"] < 1e-8,
            "perfect-substitutes dearer-platform limit failed")
    require(close(equilibrium(p_equal, 0.0, 0.0)["s"], p_equal["a"]),
            "perfect-substitutes tie selection failed")

    p_limits = dict(p, eta=2.0)
    require(equilibrium(p_limits, -40.0, 0.0)["s"] < 1e-15,
            "lower share limit failed")
    require(1.0 - equilibrium(p_limits, 40.0, 0.0)["s"] < 1e-15,
            "upper share limit failed")

    p_alpha = dict(p, alpha=1e-10)
    alpha_limit = equilibrium(p_alpha, z, 0.0)
    require(close(alpha_limit["d"], 1.0 - p_alpha["beta"], rtol=1e-9),
            "alpha limit failed")

    p_beta = dict(p, beta=0.0)
    beta_limit = equilibrium(p_beta, z, 0.0)
    require(close(
        gross_spending_multiplier(p_beta["alpha"], 0.0, beta_limit["omega"]),
        beta_limit["omega"] / (1.0 - p_beta["alpha"] * beta_limit["omega"]),
    ), "beta boundary failed")

    p_epsilon = dict(p, epsilon=0.0)
    epsilon_out = equilibrium(p_epsilon, z, 0.0, 0.2)
    numeric = central_difference(
        lambda zz: math.log(equilibrium(p_epsilon, zz, 0.0, 0.2)["y"]), z, 2e-6
    )
    require(close(numeric, p_epsilon["alpha"] * epsilon_out["omega_z"] / epsilon_out["d"]),
            "zero-access-response boundary failed")

    p_near = {
        "alpha": 0.4995,
        "beta": 0.4994,
        "a": 0.5,
        "eta": 2.0,
        "p_a": 1.0,
        "bar_p": 1.0,
        "bar_b": 1.0,
        "epsilon": 0.0,
        "rho_a": 1.0,
        "rho_p_low": 0.5,
        "rho_p_high": 1.0,
        "kappa": 1.0,
    }
    near = equilibrium(p_near, 0.0, 0.0)
    require(near["d"] > 0.0 and close(near["d"], 0.0011, rtol=1e-10),
            "near-stability-boundary case failed")


def main() -> None:
    maxima = check_random_draws()
    peak = check_intermediate_penetration_peak()
    check_capacity_thresholds()
    check_finite_regions()
    check_boundaries()
    print(
        "PASS: "
        f"{N_DRAWS} deterministic random equilibria, capacity thresholds, "
        f"finite regions, and boundary cases (seed={SEED})."
    )
    print(
        "Maximum absolute residuals: "
        f"fixed point={maxima['fixed_point']:.3e}, "
        f"z derivative={maxima['z_derivative']:.3e}, "
        f"kappa derivative={maxima['kappa_derivative']:.3e}."
    )
    print(
        "Peak checks (computational verification, not a proof): "
        f"{N_PEAK_DRAWS} Delta(kappa)>0 draws; "
        f"FOC={peak['foc']:.3e}, "
        f"closed-form value={peak['closed_form']:.3e}, "
        f"CES mapping={peak['ces_mapping']:.3e}, "
        f"ds*/dkappa={peak['s_kappa_derivative']:.3e}, "
        f"dLambda_max/dkappa={peak['lambda_kappa_derivative']:.3e}; "
        "Delta-to-zero and Delta<0 boundary classifications passed."
    )


if __name__ == "__main__":
    main()
