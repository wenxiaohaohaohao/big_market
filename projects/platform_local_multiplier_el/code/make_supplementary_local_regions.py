"""Create Supplementary Figure S1 for the Economics Letters manuscript.

The figure restores the local marginal sign geometry from the pre-M1--M3
mechanism figure without restoring its superseded local-capacity panel.  It is
explicitly a CES specialization and an analytical illustration, not a
calibration or a finite-change result.

All analytical objects are evaluated with functions imported from
``verify_model.py``.  Outputs are written to the project-local ``figures``
directory as editable SVG/PDF, a 600 dpi PNG preview, and source-data CSV.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from verify_model import (
    ces_share_speed,
    ces_share_speed_prime,
    ces_share_speed_second,
    general_capture_drag,
    general_peak_objects,
    validate_parameters,
)


plt.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
        "svg.fonttype": "none",
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "svg.hashsalt": "platform-local-multiplier-supplement-s1",
        "font.size": 7.2,
        "axes.labelsize": 8.0,
        "axes.titlesize": 8.4,
        "axes.titleweight": "semibold",
        "axes.linewidth": 0.75,
        "axes.spines.right": False,
        "axes.spines.top": False,
        "axes.unicode_minus": False,
        "xtick.labelsize": 6.8,
        "ytick.labelsize": 6.8,
        "xtick.major.width": 0.65,
        "ytick.major.width": 0.65,
        "xtick.major.size": 3.0,
        "ytick.major.size": 3.0,
        "legend.fontsize": 6.5,
        "legend.frameon": False,
    }
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
FIGURE_DIR = PROJECT_ROOT / "figures"
OUTPUT_STEM = FIGURE_DIR / "supplementary_local_marginal_regions"
SOURCE_DATA_PATH = FIGURE_DIR / "supplementary_local_marginal_regions.csv"


# These values reproduce the manuscript's pre-M1--M3 CES illustration.  They
# are deliberately separate from the finite-change illustration in Figure 1,
# whose access elasticity is 0.08 rather than 0.10.
PARAMETERS = {
    "alpha": 0.35,
    "beta": 0.25,
    "a": 0.40,
    "eta": 4.00,
    "p_a": 1.00,
    "bar_p": 1.00,
    "bar_b": 1.00,
    "epsilon": 0.10,
    "rho_a": 0.80,
    "rho_p_low": 0.10,
    "rho_p_high": 0.60,
    "kappa": 0.50,
}
KAPPAS = (0.0, 0.5, 1.0)


def share_speed(s: float) -> float:
    return ces_share_speed(s, PARAMETERS["eta"])


def share_speed_prime(s: float) -> float:
    return ces_share_speed_prime(s, PARAMETERS["eta"])


def share_speed_second(s: float) -> float:
    return ces_share_speed_second(s, PARAMETERS["eta"])


def capture_drag(s: float, kappa: float) -> float:
    return general_capture_drag(PARAMETERS, kappa, s, share_speed)


def peak_objects(kappa: float) -> dict[str, float]:
    return general_peak_objects(
        PARAMETERS,
        kappa,
        share_speed,
        share_speed_prime,
        share_speed_second,
    )


def sign_region(s: float, drag: float) -> str:
    nominal = PARAMETERS["epsilon"] - drag
    real = nominal + PARAMETERS["alpha"] * s
    tolerance = 1e-12
    if nominal > tolerance:
        return "both_rise"
    if real < -tolerance:
        return "both_fall"
    if nominal < -tolerance and real > tolerance:
        return "only_real_income_rises"
    return "boundary"


def validate_contract(s_grid: np.ndarray) -> dict[float, dict[str, float]]:
    """Validate parameters, peaks, identities, and all displayed sign regions."""
    validate_parameters(PARAMETERS)
    if not PARAMETERS["rho_a"] > PARAMETERS["rho_p_high"]:
        raise ValueError("Every displayed capacity requires Delta(kappa) > 0.")

    peaks = {kappa: peak_objects(kappa) for kappa in KAPPAS}
    peak_shares = [peaks[kappa]["s_star"] for kappa in KAPPAS]
    peak_values = [peaks[kappa]["lambda_max"] for kappa in KAPPAS]
    if not 0.0 < peak_shares[0] < peak_shares[1] < peak_shares[2] < 0.5:
        raise ArithmeticError("Capacity must move each CES drag peak toward one-half.")
    if not peak_values[0] > peak_values[1] > peak_values[2] > 0.0:
        raise ArithmeticError("Capacity must strictly lower the CES drag peak.")

    observed_regions: dict[float, set[str]] = {kappa: set() for kappa in KAPPAS}
    for s in s_grid:
        real_boundary = PARAMETERS["epsilon"] + PARAMETERS["alpha"] * float(s)
        for kappa in KAPPAS:
            drag = capture_drag(float(s), kappa)
            nominal = PARAMETERS["epsilon"] - drag
            real = real_boundary - drag
            if not math.isclose(
                real - nominal,
                PARAMETERS["alpha"] * float(s),
                rel_tol=0.0,
                abs_tol=2e-13,
            ):
                raise ArithmeticError("The real-minus-nominal marginal identity failed.")
            observed_regions[kappa].add(sign_region(float(s), drag))

    # Low capacity must display all three regions.  Higher capacities need not
    # enter the joint-loss region, but must display joint gains and the
    # real-income-only region, exactly as in the analytical illustration.
    if not {
        "both_rise",
        "only_real_income_rises",
        "both_fall",
    }.issubset(observed_regions[0.0]):
        raise ArithmeticError("The low-capacity curve must traverse all three regions.")
    for kappa in (0.5, 1.0):
        if not {
            "both_rise",
            "only_real_income_rises",
        }.issubset(observed_regions[kappa]):
            raise ArithmeticError("Higher-capacity curves must traverse both visible regions.")

    return peaks


def write_source_data(
    s_grid: np.ndarray,
    peaks: dict[float, dict[str, float]],
) -> None:
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    fields = [
        "s",
        "epsilon",
        "epsilon_plus_alpha_s",
        "lambda_kappa_0",
        "lambda_kappa_0_5",
        "lambda_kappa_1",
        "dlnY_dz_kappa_0",
        "dlnY_dz_kappa_0_5",
        "dlnY_dz_kappa_1",
        "dlnR_dz_kappa_0",
        "dlnR_dz_kappa_0_5",
        "dlnR_dz_kappa_1",
        "sign_region_kappa_0",
        "sign_region_kappa_0_5",
        "sign_region_kappa_1",
        "peak_s_kappa_0",
        "peak_s_kappa_0_5",
        "peak_s_kappa_1",
        "peak_lambda_kappa_0",
        "peak_lambda_kappa_0_5",
        "peak_lambda_kappa_1",
    ]
    with SOURCE_DATA_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for s_value in s_grid:
            s = float(s_value)
            boundary_nominal = PARAMETERS["epsilon"]
            boundary_real = boundary_nominal + PARAMETERS["alpha"] * s
            drags = {kappa: capture_drag(s, kappa) for kappa in KAPPAS}
            row = {
                "s": f"{s:.10f}",
                "epsilon": f"{boundary_nominal:.10f}",
                "epsilon_plus_alpha_s": f"{boundary_real:.10f}",
            }
            suffixes = {0.0: "0", 0.5: "0_5", 1.0: "1"}
            for kappa, suffix in suffixes.items():
                drag = drags[kappa]
                row[f"lambda_kappa_{suffix}"] = f"{drag:.10f}"
                row[f"dlnY_dz_kappa_{suffix}"] = f"{boundary_nominal - drag:.10f}"
                row[f"dlnR_dz_kappa_{suffix}"] = f"{boundary_real - drag:.10f}"
                row[f"sign_region_kappa_{suffix}"] = sign_region(s, drag)
                row[f"peak_s_kappa_{suffix}"] = f"{peaks[kappa]['s_star']:.10f}"
                row[f"peak_lambda_kappa_{suffix}"] = f"{peaks[kappa]['lambda_max']:.10f}"
            writer.writerow(row)


def make_figure(
    s_grid: np.ndarray,
    peaks: dict[float, dict[str, float]],
) -> None:
    epsilon = PARAMETERS["epsilon"]
    alpha = PARAMETERS["alpha"]
    real_boundary = epsilon + alpha * s_grid
    y_upper = 0.48

    width_mm, height_mm = 160.0, 96.0
    fig, ax = plt.subplots(
        figsize=(width_mm / 25.4, height_mm / 25.4),
        facecolor="white",
    )
    fig.subplots_adjust(left=0.125, right=0.975, bottom=0.165, top=0.845)

    # The three bands classify marginal effects using equations (10)--(11):
    # green: both rise; amber: only real income rises; rose: both fall.
    ax.fill_between(
        s_grid, 0.0, epsilon, color="#DDEBE3", alpha=0.72, linewidth=0.0, zorder=0
    )
    ax.fill_between(
        s_grid, epsilon, real_boundary, color="#F4E8C8", alpha=0.72, linewidth=0.0, zorder=0
    )
    ax.fill_between(
        s_grid, real_boundary, y_upper, color="#F2DDDA", alpha=0.66, linewidth=0.0, zorder=0
    )

    styles = {
        0.0: {"color": "#0072B2", "linestyle": "-", "marker": "o", "label": "κ = 0"},
        0.5: {"color": "#E69F00", "linestyle": "--", "marker": "s", "label": "κ = 0.5"},
        1.0: {"color": "#009E73", "linestyle": "-.", "marker": "D", "label": "κ = 1"},
    }
    for kappa in KAPPAS:
        style = styles[kappa]
        values = np.asarray([capture_drag(float(s), kappa) for s in s_grid])
        ax.plot(
            s_grid,
            values,
            color=style["color"],
            linestyle=style["linestyle"],
            linewidth=1.8,
            label=style["label"],
            zorder=3,
        )
        peak = peaks[kappa]
        ax.plot(
            peak["s_star"],
            peak["lambda_max"],
            marker=style["marker"],
            markersize=4.6,
            markerfacecolor="white",
            markeredgecolor=style["color"],
            markeredgewidth=1.0,
            linestyle="none",
            zorder=5,
        )

    threshold_color = "#444444"
    ax.axhline(
        epsilon,
        color=threshold_color,
        linestyle=(0, (1.5, 1.7)),
        linewidth=1.0,
        zorder=2,
    )
    ax.plot(
        s_grid,
        real_boundary,
        color=threshold_color,
        linestyle=(0, (5.0, 2.4)),
        linewidth=1.0,
        zorder=2,
    )
    ax.text(0.965, epsilon + 0.009, "ε", fontsize=6.8, ha="right", va="bottom")
    boundary_label_x = 0.67
    ax.text(
        boundary_label_x,
        epsilon + alpha * boundary_label_x + 0.012,
        "ε + αs",
        fontsize=6.8,
        ha="left",
        va="bottom",
        rotation=20,
        rotation_mode="anchor",
    )

    # Direct region labels prevent the background colors from being the sole
    # carrier of the outcome classification.
    region_x = 0.76
    label_box = {"facecolor": "white", "edgecolor": "none", "alpha": 0.68, "pad": 0.7}
    ax.text(
        region_x,
        0.035,
        "Both rise",
        color="#3E5F4C",
        fontsize=6.3,
        ha="center",
        va="center",
        bbox=label_box,
    )
    ax.text(
        region_x,
        0.275,
        "Only real income rises",
        color="#6C5A2D",
        fontsize=6.3,
        ha="center",
        va="center",
        bbox=label_box,
    )
    ax.text(
        region_x,
        0.435,
        "Both fall",
        color="#704A47",
        fontsize=6.3,
        ha="center",
        va="center",
        bbox=label_box,
    )

    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, y_upper)
    ax.set_xticks(np.linspace(0.0, 1.0, 6))
    ax.set_yticks(np.arange(0.0, 0.49, 0.10))
    ax.set_xlabel("Platform expenditure share, s")
    ax.set_ylabel(r"Marginal capture drag, $\Lambda_g(s,\kappa)$")
    ax.set_title("Local marginal income regions in the CES specialization", pad=8.5)
    ax.legend(
        title="Local organizational capacity",
        title_fontsize=6.6,
        loc="upper left",
        borderaxespad=0.5,
        handlelength=2.6,
        labelspacing=0.35,
    )

    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    metadata = {
        "Title": "Local marginal income regions in the CES specialization",
        "Author": "Wenxiao Dong and Yaqi Hu",
        "Subject": "Analytical illustration; local marginal effects; not a calibration",
        "Creator": "Python and matplotlib",
    }
    fig.savefig(
        OUTPUT_STEM.with_suffix(".svg"),
        format="svg",
        facecolor="white",
        metadata={"Title": metadata["Title"], "Description": metadata["Subject"]},
    )
    fig.savefig(
        OUTPUT_STEM.with_suffix(".pdf"),
        format="pdf",
        facecolor="white",
        metadata=metadata,
    )
    fig.savefig(
        OUTPUT_STEM.with_suffix(".png"),
        format="png",
        dpi=600,
        facecolor="white",
        metadata={"Title": metadata["Title"]},
    )
    plt.close(fig)


def main() -> None:
    s_grid = np.linspace(0.0, 1.0, 501)
    peaks = validate_contract(s_grid)
    write_source_data(s_grid, peaks)
    make_figure(s_grid, peaks)
    print("PASS: Supplementary Figure S1 marginal-region contract verified")
    for kappa in KAPPAS:
        peak = peaks[kappa]
        print(
            f"  kappa={kappa:.1f}: s_star={peak['s_star']:.6f}, "
            f"Lambda_max={peak['lambda_max']:.6f}"
        )
    print(f"  source rows={len(s_grid)}")
    print(f"Saved Supplementary Figure S1 bundle to: {FIGURE_DIR}")


if __name__ == "__main__":
    main()
