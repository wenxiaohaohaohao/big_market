"""Create the analytical mechanism figure for the EL manuscript.

The figure illustrates two exact comparative-static results from the model:

1. Greater local organizational capacity lowers the peak capture drag and
   moves its maximizing platform share toward one half.
2. At a fixed platform share, organizational capacity moves the marginal
   effects of integration through the two sign thresholds.

Outputs are written to the project-local ``figures`` directory.  The SVG and
PDF retain editable text; the PNG is a high-resolution preview.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


# Publication typography and editable-vector settings.
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial", "DejaVu Sans", "Liberation Sans"]
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["ps.fonttype"] = 42
plt.rcParams["svg.hashsalt"] = "platform-local-multiplier-mechanism"
plt.rcParams["font.size"] = 7.2
plt.rcParams["axes.labelsize"] = 8.0
plt.rcParams["axes.titlesize"] = 8.3
plt.rcParams["axes.titleweight"] = "semibold"
plt.rcParams["axes.linewidth"] = 0.75
plt.rcParams["xtick.labelsize"] = 6.8
plt.rcParams["ytick.labelsize"] = 6.8
plt.rcParams["xtick.major.width"] = 0.65
plt.rcParams["ytick.major.width"] = 0.65
plt.rcParams["xtick.major.size"] = 3.0
plt.rcParams["ytick.major.size"] = 3.0
plt.rcParams["legend.fontsize"] = 6.7
plt.rcParams["legend.frameon"] = False
plt.rcParams["axes.spines.right"] = False
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.unicode_minus"] = False


PROJECT_ROOT = Path(__file__).resolve().parents[1]
FIGURE_DIR = PROJECT_ROOT / "figures"
OUTPUT_STEM = FIGURE_DIR / "mechanism_figure"


# Baseline parameters.  They are illustrative, not calibrated.
ALPHA = 0.35
BETA = 0.25
ETA = 4.0
RHO_A = 0.80
RHO_P_LOW = 0.10
RHO_P_HIGH = 0.60
EPSILON = 0.10
S_BAR = 0.25

DELTA_RHO = RHO_P_HIGH - RHO_P_LOW
D_A = 1.0 - BETA - ALPHA * RHO_A
Q = ETA - 1.0


def rho_platform(kappa: float | np.ndarray) -> float | np.ndarray:
    """Platform-channel local retention at organizational capacity kappa."""

    return RHO_P_LOW + DELTA_RHO * kappa


def retention_gap(kappa: float | np.ndarray) -> float | np.ndarray:
    """Traditional-minus-platform local retention gap."""

    return RHO_A - rho_platform(kappa)


def denominator(s: float | np.ndarray, kappa: float | np.ndarray) -> float | np.ndarray:
    """Positive local-income fixed-point denominator."""

    return D_A + ALPHA * s * retention_gap(kappa)


def capture_drag(s: float | np.ndarray, kappa: float | np.ndarray) -> float | np.ndarray:
    """Marginal local-capture drag Lambda(s, kappa)."""

    gap = retention_gap(kappa)
    return ALPHA * Q * gap * s * (1.0 - s) / denominator(s, kappa)


def peak_share(kappa: float) -> float:
    """Unique maximizer of capture drag, valid when the retention gap is positive."""

    gap = float(retention_gap(kappa))
    if gap <= 0.0:
        raise ValueError("The peak-share formula requires rho_A > rho_P(kappa).")
    return 1.0 / (1.0 + math.sqrt(1.0 + ALPHA * gap / D_A))


def peak_drag(kappa: float) -> float:
    """Capture drag evaluated at its unique maximizing share."""

    s_peak = peak_share(kappa)
    return float(capture_drag(s_peak, kappa))


def capacity_threshold(target: float, s_fixed: float) -> float:
    """Solve Lambda(s_fixed, kappa) = target for the unique capacity threshold."""

    h = Q * (1.0 - s_fixed)
    if not 0.0 <= target < h:
        raise ValueError("An interior analytical threshold requires 0 <= target < q(1-s).")
    gap_star = target * D_A / (ALPHA * s_fixed * (h - target))
    return (RHO_A - RHO_P_LOW - gap_star) / DELTA_RHO


def validate_contract() -> tuple[float, float]:
    """Validate the parameter domain and the endpoint-crossing figure contract."""

    if not (ALPHA > 0.0 and BETA > 0.0 and ALPHA + BETA < 1.0):
        raise ValueError("Require alpha,beta > 0 and alpha + beta < 1.")
    if not (ETA > 1.0 and 0.0 < S_BAR < 1.0):
        raise ValueError("Require eta > 1 and an interior fixed platform share.")
    if not (0.0 <= RHO_P_LOW < RHO_P_HIGH <= 1.0):
        raise ValueError("Platform retention endpoints must lie in [0,1] and be ordered.")
    if not (0.0 <= RHO_A <= 1.0 and RHO_A > RHO_P_HIGH):
        raise ValueError("All Panel A curves require rho_A > rho_P(kappa) for kappa in [0,1].")
    if D_A <= 0.0:
        raise ValueError("The fixed-point denominator component d_A must be positive.")

    lambda_low_capacity = float(capture_drag(S_BAR, 0.0))
    lambda_high_capacity = float(capture_drag(S_BAR, 1.0))
    nominal_target = EPSILON
    real_target = EPSILON + ALPHA * S_BAR

    crossing = (
        lambda_low_capacity
        > real_target
        > nominal_target
        > lambda_high_capacity
    )
    if not crossing:
        raise ValueError(
            "Panel B requires Lambda(sbar,0) > epsilon + alpha*sbar "
            "> epsilon > Lambda(sbar,1)."
        )

    kappa_real = capacity_threshold(real_target, S_BAR)
    kappa_nominal = capacity_threshold(nominal_target, S_BAR)
    if not (0.0 < kappa_real < kappa_nominal < 1.0):
        raise ValueError("Thresholds must satisfy 0 < kappa_R* < kappa_Y* < 1.")

    # Direct residual checks protect the plotted threshold locations.
    if not math.isclose(
        float(capture_drag(S_BAR, kappa_real)), real_target, rel_tol=0.0, abs_tol=1e-12
    ):
        raise ArithmeticError("Real-income capacity threshold failed its defining equation.")
    if not math.isclose(
        float(capture_drag(S_BAR, kappa_nominal)), nominal_target, rel_tol=0.0, abs_tol=1e-12
    ):
        raise ArithmeticError("Nominal-income capacity threshold failed its defining equation.")

    peak_shares = [peak_share(kappa) for kappa in (0.0, 0.5, 1.0)]
    peak_values = [peak_drag(kappa) for kappa in (0.0, 0.5, 1.0)]
    if not (0.0 < peak_shares[0] < peak_shares[1] < peak_shares[2] < 0.5):
        raise ArithmeticError("Higher capacity must move the unique drag peak toward one half.")
    if not (peak_values[0] > peak_values[1] > peak_values[2] > 0.0):
        raise ArithmeticError("Higher capacity must strictly lower peak capture drag.")

    # Check the three sign regions at interior representative capacities.
    region_midpoints = (
        0.5 * kappa_real,
        0.5 * (kappa_real + kappa_nominal),
        0.5 * (kappa_nominal + 1.0),
    )
    signs = []
    for kappa in region_midpoints:
        drag = float(capture_drag(S_BAR, kappa))
        signs.append((EPSILON - drag, EPSILON + ALPHA * S_BAR - drag))
    if not (signs[0][0] < 0.0 and signs[0][1] < 0.0):
        raise ArithmeticError("The low-capacity region must lower both income measures.")
    if not (signs[1][0] < 0.0 < signs[1][1]):
        raise ArithmeticError("The intermediate region must raise only real income.")
    if not (0.0 < signs[2][0] < signs[2][1]):
        raise ArithmeticError("The high-capacity region must raise both income measures.")

    return kappa_real, kappa_nominal


def write_source_data(
    s_grid: np.ndarray,
    kappa_grid: np.ndarray,
    kappas_panel_a: tuple[float, ...],
    kappa_real: float,
    kappa_nominal: float,
) -> None:
    """Write clean source-data tables for both analytical panels."""

    FIGURE_DIR.mkdir(parents=True, exist_ok=True)

    panel_a_path = FIGURE_DIR / "mechanism_figure_panel_a.csv"
    panel_a_fields = [
        "s",
        "lambda_kappa_0",
        "lambda_kappa_0_5",
        "lambda_kappa_1",
        "epsilon",
        "epsilon_plus_alpha_s",
        "s_dagger_kappa_0",
        "s_dagger_kappa_0_5",
        "s_dagger_kappa_1",
        "lambda_max_kappa_0",
        "lambda_max_kappa_0_5",
        "lambda_max_kappa_1",
    ]
    peaks = [peak_share(kappa) for kappa in kappas_panel_a]
    peak_values = [peak_drag(kappa) for kappa in kappas_panel_a]
    with panel_a_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=panel_a_fields)
        writer.writeheader()
        for index, s_value in enumerate(s_grid):
            writer.writerow(
                {
                    "s": f"{s_value:.10f}",
                    "lambda_kappa_0": f"{capture_drag(s_value, kappas_panel_a[0]):.10f}",
                    "lambda_kappa_0_5": f"{capture_drag(s_value, kappas_panel_a[1]):.10f}",
                    "lambda_kappa_1": f"{capture_drag(s_value, kappas_panel_a[2]):.10f}",
                    "epsilon": f"{EPSILON:.10f}",
                    "epsilon_plus_alpha_s": f"{EPSILON + ALPHA * s_value:.10f}",
                    "s_dagger_kappa_0": f"{peaks[0]:.10f}",
                    "s_dagger_kappa_0_5": f"{peaks[1]:.10f}",
                    "s_dagger_kappa_1": f"{peaks[2]:.10f}",
                    "lambda_max_kappa_0": f"{peak_values[0]:.10f}",
                    "lambda_max_kappa_0_5": f"{peak_values[1]:.10f}",
                    "lambda_max_kappa_1": f"{peak_values[2]:.10f}",
                }
            )

    panel_b_path = FIGURE_DIR / "mechanism_figure_panel_b.csv"
    panel_b_fields = [
        "kappa",
        "lambda_at_sbar",
        "dlnY_dz",
        "dlnR_dz",
        "sbar",
        "kappa_R_star",
        "kappa_Y_star",
    ]
    lambda_b = capture_drag(S_BAR, kappa_grid)
    nominal_effect = EPSILON - lambda_b
    real_effect = EPSILON + ALPHA * S_BAR - lambda_b
    with panel_b_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=panel_b_fields)
        writer.writeheader()
        for values in zip(kappa_grid, lambda_b, nominal_effect, real_effect):
            kappa_value, lambda_value, nominal_value, real_value = values
            writer.writerow(
                {
                    "kappa": f"{kappa_value:.10f}",
                    "lambda_at_sbar": f"{lambda_value:.10f}",
                    "dlnY_dz": f"{nominal_value:.10f}",
                    "dlnR_dz": f"{real_value:.10f}",
                    "sbar": f"{S_BAR:.10f}",
                    "kappa_R_star": f"{kappa_real:.10f}",
                    "kappa_Y_star": f"{kappa_nominal:.10f}",
                }
            )


def make_figure(kappa_real: float, kappa_nominal: float) -> None:
    """Draw and export the two-panel mechanism figure."""

    s_grid = np.linspace(0.0, 1.0, 501)
    kappa_grid = np.linspace(0.0, 1.0, 501)
    kappas_panel_a = (0.0, 0.5, 1.0)

    write_source_data(
        s_grid=s_grid,
        kappa_grid=kappa_grid,
        kappas_panel_a=kappas_panel_a,
        kappa_real=kappa_real,
        kappa_nominal=kappa_nominal,
    )

    # Okabe-Ito colors plus line styles and markers make the curves print-safe.
    capacity_styles = (
        {"color": "#0072B2", "linestyle": "-", "marker": "o", "label": "κ = 0"},
        {"color": "#E69F00", "linestyle": "--", "marker": "s", "label": "κ = 0.5"},
        {"color": "#009E73", "linestyle": "-.", "marker": "D", "label": "κ = 1"},
    )
    nominal_color = "#0072B2"
    real_color = "#D55E00"
    threshold_color = "#3F3F3F"

    width_mm = 183.0
    height_mm = 84.0
    fig, (ax_a, ax_b) = plt.subplots(
        1,
        2,
        figsize=(width_mm / 25.4, height_mm / 25.4),
        facecolor="white",
    )
    fig.subplots_adjust(left=0.085, right=0.985, bottom=0.185, top=0.80, wspace=0.32)

    # Panel A: capacity changes both the height and location of peak drag.
    y_max_a = 0.48
    ax_a.fill_between(
        s_grid, 0.0, EPSILON, color="#E9F3ED", alpha=0.65, linewidth=0.0, zorder=0
    )
    ax_a.fill_between(
        s_grid,
        EPSILON,
        EPSILON + ALPHA * s_grid,
        color="#F8F0D9",
        alpha=0.60,
        linewidth=0.0,
        zorder=0,
    )
    ax_a.fill_between(
        s_grid,
        EPSILON + ALPHA * s_grid,
        y_max_a,
        color="#F7E8E6",
        alpha=0.55,
        linewidth=0.0,
        zorder=0,
    )

    for kappa, style in zip(kappas_panel_a, capacity_styles):
        lambda_curve = capture_drag(s_grid, kappa)
        ax_a.plot(
            s_grid,
            lambda_curve,
            color=style["color"],
            linestyle=style["linestyle"],
            linewidth=1.65,
            label=style["label"],
            zorder=3,
        )
        s_peak = peak_share(kappa)
        lambda_peak = peak_drag(kappa)
        ax_a.plot(
            s_peak,
            lambda_peak,
            marker=style["marker"],
            markersize=4.3,
            markerfacecolor="white",
            markeredgecolor=style["color"],
            markeredgewidth=1.0,
            linestyle="none",
            zorder=5,
        )
        offset_x = {0.0: -17, 0.5: -2, 1.0: 12}[kappa]
        ax_a.annotate(
            "s†",
            xy=(s_peak, lambda_peak),
            xytext=(offset_x, 7),
            textcoords="offset points",
            color=style["color"],
            fontsize=6.2,
            ha="center",
            va="bottom",
        )

    ax_a.axhline(
        EPSILON,
        color=threshold_color,
        linestyle=(0, (1.5, 1.7)),
        linewidth=1.0,
        zorder=2,
    )
    ax_a.plot(
        s_grid,
        EPSILON + ALPHA * s_grid,
        color=threshold_color,
        linestyle=(0, (5.0, 2.4)),
        linewidth=1.0,
        zorder=2,
    )
    ax_a.text(0.965, EPSILON + 0.008, "ε", fontsize=6.6, ha="right", va="bottom")
    label_x = 0.72
    ax_a.text(
        label_x,
        EPSILON + ALPHA * label_x + 0.012,
        "ε + αs",
        fontsize=6.6,
        ha="left",
        va="bottom",
        rotation=21,
        rotation_mode="anchor",
    )
    ax_a.set_xlim(0.0, 1.0)
    ax_a.set_ylim(0.0, y_max_a)
    ax_a.set_xticks(np.linspace(0.0, 1.0, 6))
    ax_a.set_yticks(np.arange(0.0, 0.49, 0.10))
    ax_a.set_xlabel("Platform expenditure share, s")
    ax_a.set_ylabel("Capture drag, Λ(s, κ)")
    ax_a.set_title("Capacity lowers drag and shifts its peak toward s = 1/2", pad=8.0)
    ax_a.legend(
        title="Organizational capacity",
        title_fontsize=6.7,
        loc="upper left",
        borderaxespad=0.45,
        handlelength=2.4,
        labelspacing=0.35,
    )

    # Panel B: fixed-share marginal effects and their two capacity thresholds.
    lambda_b = capture_drag(S_BAR, kappa_grid)
    nominal_effect = EPSILON - lambda_b
    real_effect = EPSILON + ALPHA * S_BAR - lambda_b
    y_min_b, y_max_b = -0.19, 0.14

    region_specs = (
        (0.0, kappa_real, "#F3DEDB", "////", "Both\nfall"),
        (kappa_real, kappa_nominal, "#F4E9C8", "....", "Only real\nincome rises"),
        (kappa_nominal, 1.0, "#DDEDE4", "", "Both\nrise"),
    )
    for left, right, color, hatch, label in region_specs:
        ax_b.axvspan(
            left,
            right,
            facecolor=color,
            alpha=0.58,
            hatch=hatch,
            edgecolor="#B5B5B5" if hatch else "none",
            linewidth=0.0,
            zorder=0,
        )
        ax_b.text(
            (left + right) / 2.0,
            0.128,
            label,
            fontsize=6.0,
            color="#444444",
            ha="center",
            va="top",
            linespacing=0.95,
        )

    ax_b.axhline(0.0, color="#4C4C4C", linewidth=0.8, zorder=1)
    ax_b.plot(
        kappa_grid,
        nominal_effect,
        color=nominal_color,
        linestyle="-",
        linewidth=1.8,
        zorder=3,
    )
    ax_b.plot(
        kappa_grid,
        real_effect,
        color=real_color,
        linestyle="--",
        linewidth=1.8,
        zorder=3,
    )

    for threshold, label, color, marker in (
        (kappa_real, f"κR* = {kappa_real:.2f}", real_color, "o"),
        (kappa_nominal, f"κY* = {kappa_nominal:.2f}", nominal_color, "s"),
    ):
        ax_b.axvline(
            threshold,
            color=threshold_color,
            linestyle=(0, (2.0, 2.0)),
            linewidth=0.85,
            zorder=2,
        )
        ax_b.plot(
            threshold,
            0.0,
            marker=marker,
            markersize=4.0,
            markerfacecolor="white",
            markeredgecolor=color,
            markeredgewidth=1.0,
            linestyle="none",
            zorder=5,
        )
        ax_b.text(
            threshold + 0.012,
            y_min_b + 0.008,
            label,
            fontsize=5.9,
            color=threshold_color,
            rotation=90,
            ha="left",
            va="bottom",
        )

    # Label the curves before the narrow high-capacity region so that the
    # region annotation remains legible at final journal width.
    label_x_b = 0.78
    ax_b.text(
        label_x_b,
        float(np.interp(label_x_b, kappa_grid, real_effect)) + 0.006,
        "Real income",
        color=real_color,
        fontsize=6.5,
        fontweight="semibold",
        ha="right",
        va="bottom",
        bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.78, "pad": 0.6},
    )
    ax_b.text(
        label_x_b,
        float(np.interp(label_x_b, kappa_grid, nominal_effect)) - 0.006,
        "Nominal income",
        color=nominal_color,
        fontsize=6.5,
        fontweight="semibold",
        ha="right",
        va="top",
        bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.78, "pad": 0.6},
    )
    ax_b.set_xlim(0.0, 1.0)
    ax_b.set_ylim(y_min_b, y_max_b)
    ax_b.set_xticks(np.linspace(0.0, 1.0, 6))
    ax_b.set_yticks(np.arange(-0.15, 0.11, 0.05))
    ax_b.set_xlabel("Local organizational capacity, κ")
    ax_b.set_ylabel("Marginal effect of integration")
    ax_b.set_title(f"Capacity changes integration effects (s = {S_BAR:.2f})", pad=8.0)

    # Panel letters are outside the axes but remain inside the fixed-size canvas.
    ax_a.text(-0.17, 1.13, "a", transform=ax_a.transAxes, fontsize=9.0, fontweight="bold")
    ax_b.text(-0.17, 1.13, "b", transform=ax_b.transAxes, fontsize=9.0, fontweight="bold")

    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT_STEM.with_suffix(".svg"),
        format="svg",
        facecolor="white",
        metadata={
            "Title": "Organizational capacity, capture drag, and local integration effects",
            "Description": "Analytical illustration using the manuscript's closed-form model.",
        },
    )
    fig.savefig(
        OUTPUT_STEM.with_suffix(".pdf"),
        format="pdf",
        facecolor="white",
        metadata={
            "Title": "Organizational capacity, capture drag, and local integration effects",
            "Subject": "Analytical mechanism figure",
            "Creator": "Python and matplotlib",
        },
    )
    fig.savefig(
        OUTPUT_STEM.with_suffix(".png"),
        format="png",
        dpi=400,
        facecolor="white",
        metadata={"Title": "Organizational capacity and local integration effects"},
    )
    plt.close(fig)


def main() -> None:
    kappa_real, kappa_nominal = validate_contract()
    make_figure(kappa_real=kappa_real, kappa_nominal=kappa_nominal)

    print("PASS: endpoint crossing and analytical thresholds verified")
    print(f"  Lambda(sbar, kappa=0) = {capture_drag(S_BAR, 0.0):.6f}")
    print(f"  epsilon + alpha*sbar = {EPSILON + ALPHA * S_BAR:.6f}")
    print(f"  epsilon              = {EPSILON:.6f}")
    print(f"  Lambda(sbar, kappa=1) = {capture_drag(S_BAR, 1.0):.6f}")
    print(f"  kappa_R* = {kappa_real:.6f}")
    print(f"  kappa_Y* = {kappa_nominal:.6f}")
    for kappa in (0.0, 0.5, 1.0):
        print(
            f"  kappa={kappa:.1f}: s_dagger={peak_share(kappa):.6f}, "
            f"Lambda_max={peak_drag(kappa):.6f}"
        )
    print(f"Saved figure bundle to: {FIGURE_DIR}")


if __name__ == "__main__":
    main()
