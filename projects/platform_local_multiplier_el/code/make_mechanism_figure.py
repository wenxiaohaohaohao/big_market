"""Create Figure 1 for the M1--M3 Economics Letters manuscript.

Panel A illustrates the general single-peak theorem with two symmetric,
strictly concave share-speed laws. Panel B plots the finite income ratios and
the ordered organizational-capacity thresholds. All analytical objects are
imported from ``verify_model.py`` so the figure and verification contract use
one implementation. Parameters are illustrative, not calibrated.
"""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from verify_model import (
    ces_share_speed,
    ces_share_speed_prime,
    ces_share_speed_second,
    classify_finite_capacity_thresholds,
    finite_capacity_objects,
    general_capture_drag,
    general_peak_objects,
    sine_share_speed,
    sine_share_speed_prime,
    sine_share_speed_second,
    validate_parameters,
)


plt.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
        "svg.fonttype": "none",
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "svg.hashsalt": "platform-local-multiplier-m1-m3",
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
        "legend.fontsize": 6.3,
        "legend.frameon": False,
    }
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
FIGURE_DIR = PROJECT_ROOT / "figures"
OUTPUT_STEM = FIGURE_DIR / "mechanism_figure"


# One parameterization supports both panels. It is an illustration, not a
# calibration. Panel B uses the nested CES demand path to map z into (P_M, s).
PARAMETERS = {
    "alpha": 0.35,
    "beta": 0.25,
    "a": 0.40,
    "eta": 4.00,
    "p_a": 1.00,
    "bar_p": 1.00,
    "bar_b": 1.00,
    "epsilon": 0.08,
    "rho_a": 0.80,
    "rho_p_low": 0.10,
    "rho_p_high": 0.60,
    "kappa": 0.50,
}
Z0 = -0.75
Z1 = -0.30
KAPPA_LOW = 0.20
KAPPA_HIGH = 0.80
SINE_SCALE = (PARAMETERS["eta"] - 1.0) / 4.0


def share_speed_laws():
    """Return two symmetric, strictly concave speed laws and derivatives."""
    return (
        {
            "key": "ces",
            "label": "CES",
            "color": "#356C9A",
            "marker": "o",
            "speed": lambda s: ces_share_speed(s, PARAMETERS["eta"]),
            "prime": lambda s: ces_share_speed_prime(s, PARAMETERS["eta"]),
            "second": lambda s: ces_share_speed_second(s, PARAMETERS["eta"]),
        },
        {
            "key": "sine",
            "label": "Sine",
            "color": "#B66A3C",
            "marker": "s",
            "speed": lambda s: sine_share_speed(s, SINE_SCALE),
            "prime": lambda s: sine_share_speed_prime(s, SINE_SCALE),
            "second": lambda s: sine_share_speed_second(s, SINE_SCALE),
        },
    )


def validate_contract() -> dict[str, float | str | None]:
    """Validate the theorem conditions and every plotted crossing."""
    validate_parameters(PARAMETERS)
    thresholds = classify_finite_capacity_thresholds(PARAMETERS, Z0, Z1)
    if thresholds["classification"] != "double_threshold":
        raise ValueError("Panel B requires the finite endpoint-crossing condition.")
    kappa_r = float(thresholds["kappa_r"])
    kappa_y = float(thresholds["kappa_y"])
    if not 0.0 < kappa_r < kappa_y < 1.0:
        raise ArithmeticError("Finite thresholds must satisfy 0 < kappa_R^F < kappa_Y^F < 1.")

    for law in share_speed_laws():
        low = general_peak_objects(
            PARAMETERS,
            KAPPA_LOW,
            law["speed"],
            law["prime"],
            law["second"],
        )
        high = general_peak_objects(
            PARAMETERS,
            KAPPA_HIGH,
            law["speed"],
            law["prime"],
            law["second"],
        )
        if not 0.0 < low["s_star"] < high["s_star"] < 0.5:
            raise ArithmeticError("Symmetric speeds must peak below one-half and shift right.")
        if not low["lambda_max"] > high["lambda_max"] > 0.0:
            raise ArithmeticError("Higher capacity must lower the peak capture drag.")

    for kappa, expected in (
        (0.5 * kappa_r, (-1, -1)),
        (0.5 * (kappa_r + kappa_y), (-1, 1)),
        (0.5 * (kappa_y + 1.0), (1, 1)),
    ):
        objects = finite_capacity_objects(PARAMETERS, Z0, Z1, kappa)
        signs = (
            1 if objects["y_ratio"] > 1.0 else -1,
            1 if objects["r_ratio"] > 1.0 else -1,
        )
        if signs != expected:
            raise ArithmeticError("Panel B sign regions do not match Proposition 1.")
    return thresholds


def write_source_data(
    s_grid: np.ndarray,
    kappa_grid: np.ndarray,
    thresholds: dict[str, float | str | None],
) -> None:
    """Write source-data tables for both analytical panels."""
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    laws = share_speed_laws()

    peak_map: dict[tuple[str, float], dict[str, float]] = {}
    for law in laws:
        for kappa in (KAPPA_LOW, KAPPA_HIGH):
            peak_map[(law["key"], kappa)] = general_peak_objects(
                PARAMETERS,
                kappa,
                law["speed"],
                law["prime"],
                law["second"],
            )

    panel_a_path = FIGURE_DIR / "mechanism_figure_panel_a.csv"
    panel_a_fields = [
        "s",
        "lambda_ces_kappa_low",
        "lambda_ces_kappa_high",
        "lambda_sine_kappa_low",
        "lambda_sine_kappa_high",
        "kappa_low",
        "kappa_high",
        "ces_peak_s_low",
        "ces_peak_s_high",
        "sine_peak_s_low",
        "sine_peak_s_high",
        "ces_peak_lambda_low",
        "ces_peak_lambda_high",
        "sine_peak_lambda_low",
        "sine_peak_lambda_high",
    ]
    with panel_a_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=panel_a_fields)
        writer.writeheader()
        for s in s_grid:
            row = {
                "s": f"{s:.10f}",
                "kappa_low": f"{KAPPA_LOW:.10f}",
                "kappa_high": f"{KAPPA_HIGH:.10f}",
            }
            for law in laws:
                row[f"lambda_{law['key']}_kappa_low"] = f"{general_capture_drag(PARAMETERS, KAPPA_LOW, float(s), law['speed']):.10f}"
                row[f"lambda_{law['key']}_kappa_high"] = f"{general_capture_drag(PARAMETERS, KAPPA_HIGH, float(s), law['speed']):.10f}"
                for suffix, kappa in (("low", KAPPA_LOW), ("high", KAPPA_HIGH)):
                    peak = peak_map[(law["key"], kappa)]
                    row[f"{law['key']}_peak_s_{suffix}"] = f"{peak['s_star']:.10f}"
                    row[f"{law['key']}_peak_lambda_{suffix}"] = f"{peak['lambda_max']:.10f}"
            writer.writerow(row)

    kappa_r = float(thresholds["kappa_r"])
    kappa_y = float(thresholds["kappa_y"])
    panel_b_path = FIGURE_DIR / "mechanism_figure_panel_b.csv"
    panel_b_fields = [
        "kappa",
        "log_y_ratio",
        "log_r_ratio",
        "d_ratio",
        "b_ratio",
        "p_ratio",
        "kappa_R_F",
        "kappa_Y_F",
        "z0",
        "z1",
    ]
    with panel_b_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=panel_b_fields)
        writer.writeheader()
        for kappa in kappa_grid:
            objects = finite_capacity_objects(PARAMETERS, Z0, Z1, float(kappa))
            writer.writerow(
                {
                    "kappa": f"{kappa:.10f}",
                    "log_y_ratio": f"{np.log(objects['y_ratio']):.10f}",
                    "log_r_ratio": f"{np.log(objects['r_ratio']):.10f}",
                    "d_ratio": f"{objects['d_ratio']:.10f}",
                    "b_ratio": f"{objects['b_ratio']:.10f}",
                    "p_ratio": f"{objects['p_ratio']:.10f}",
                    "kappa_R_F": f"{kappa_r:.10f}",
                    "kappa_Y_F": f"{kappa_y:.10f}",
                    "z0": f"{Z0:.10f}",
                    "z1": f"{Z1:.10f}",
                }
            )


def make_figure(thresholds: dict[str, float | str | None]) -> None:
    """Draw and export the two-panel analytical figure."""
    s_grid = np.linspace(0.0, 1.0, 501)
    kappa_grid = np.linspace(0.0, 1.0, 501)
    write_source_data(s_grid, kappa_grid, thresholds)
    laws = share_speed_laws()
    kappa_r = float(thresholds["kappa_r"])
    kappa_y = float(thresholds["kappa_y"])

    width_mm, height_mm = 183.0, 84.0
    fig, (ax_a, ax_b) = plt.subplots(
        1,
        2,
        figsize=(width_mm / 25.4, height_mm / 25.4),
        facecolor="white",
    )
    fig.subplots_adjust(left=0.080, right=0.985, bottom=0.190, top=0.815, wspace=0.31)

    # Panel A: two demand-induced share speeds, each at low and high capacity.
    line_styles = {
        KAPPA_LOW: ("-", 1.75, 1.0),
        KAPPA_HIGH: ("--", 1.45, 0.90),
    }
    all_values = []
    for law in laws:
        for kappa in (KAPPA_LOW, KAPPA_HIGH):
            values = np.array(
                [
                    general_capture_drag(PARAMETERS, kappa, float(s), law["speed"])
                    for s in s_grid
                ]
            )
            all_values.append(values)
            linestyle, linewidth, alpha = line_styles[kappa]
            ax_a.plot(
                s_grid,
                values,
                color=law["color"],
                linestyle=linestyle,
                linewidth=linewidth,
                alpha=alpha,
                label=f"{law['label']}, κ = {kappa:.1f}",
                zorder=3,
            )
            peak = general_peak_objects(
                PARAMETERS,
                kappa,
                law["speed"],
                law["prime"],
                law["second"],
            )
            ax_a.plot(
                peak["s_star"],
                peak["lambda_max"],
                marker=law["marker"],
                markersize=3.9,
                markerfacecolor="white",
                markeredgecolor=law["color"],
                markeredgewidth=0.9,
                linestyle="none",
                zorder=5,
            )
    y_max_a = max(float(np.max(values)) for values in all_values) * 1.18
    ax_a.axvline(0.5, color="#777777", linestyle=(0, (2.0, 2.2)), linewidth=0.8)
    ax_a.text(0.512, y_max_a * 0.035, "s = 1/2", color="#666666", fontsize=6.2,
              rotation=90, ha="left", va="bottom")
    ax_a.set_xlim(0.0, 1.0)
    ax_a.set_ylim(0.0, y_max_a)
    ax_a.set_xticks(np.linspace(0.0, 1.0, 6))
    ax_a.set_xlabel("Platform expenditure share, s")
    ax_a.set_ylabel(r"Marginal capture drag, $\Lambda_g(s,\kappa)$")
    ax_a.set_title("The single peak is not CES-specific", pad=7.5)
    ax_a.legend(loc="upper right", ncol=2, columnspacing=0.9, handlelength=2.3,
                borderaxespad=0.35, labelspacing=0.30, frameon=True,
                facecolor="white", framealpha=0.90, edgecolor="none")

    # Panel B: finite log-income ratios and their ordered capacity thresholds.
    log_y = []
    log_r = []
    for kappa in kappa_grid:
        objects = finite_capacity_objects(PARAMETERS, Z0, Z1, float(kappa))
        log_y.append(np.log(objects["y_ratio"]))
        log_r.append(np.log(objects["r_ratio"]))
    log_y = np.asarray(log_y)
    log_r = np.asarray(log_r)
    y_min = min(float(log_y.min()), float(log_r.min()))
    y_max = max(float(log_y.max()), float(log_r.max()))
    padding = 0.18 * (y_max - y_min)
    y_lower, y_upper = y_min - padding, y_max + 1.45 * padding

    regions = (
        (0.0, kappa_r, "#F2DDDA", "Both fall"),
        (kappa_r, kappa_y, "#F4E8C8", "Only real\nincome rises"),
        (kappa_y, 1.0, "#DDEBE3", "Both rise"),
    )
    for left, right, color, label in regions:
        ax_b.axvspan(left, right, facecolor=color, alpha=0.72, linewidth=0.0, zorder=0)
        ax_b.text((left + right) / 2.0, y_upper - 0.08 * (y_upper - y_lower), label,
                  fontsize=6.0, color="#444444", ha="center", va="top", linespacing=0.95)
    ax_b.axhline(0.0, color="#555555", linewidth=0.8, zorder=1)
    ax_b.plot(kappa_grid, log_y, color="#356C9A", linewidth=1.8, zorder=3)
    ax_b.plot(kappa_grid, log_r, color="#B66A3C", linewidth=1.8, linestyle="--", zorder=3)
    for threshold, label, color, marker in (
        (kappa_r, rf"$\kappa_R^F={kappa_r:.2f}$", "#B66A3C", "o"),
        (kappa_y, rf"$\kappa_Y^F={kappa_y:.2f}$", "#356C9A", "s"),
    ):
        ax_b.axvline(threshold, color="#555555", linestyle=(0, (2.0, 2.0)), linewidth=0.8)
        ax_b.plot(threshold, 0.0, marker=marker, markersize=4.0, markerfacecolor="white",
                  markeredgecolor=color, markeredgewidth=1.0, linestyle="none", zorder=5)
        ax_b.text(threshold + 0.012, y_lower + 0.035 * (y_upper - y_lower), label,
                  fontsize=5.9, color="#444444", rotation=90, ha="left", va="bottom")
    ax_b.set_xlim(0.0, 1.0)
    ax_b.set_ylim(y_lower, y_upper)
    ax_b.set_xticks(np.linspace(0.0, 1.0, 6))
    direct_x = 0.98
    ax_b.text(
        direct_x,
        float(np.interp(direct_x, kappa_grid, log_r)) - 0.015 * (y_upper - y_lower),
        "Consumption-equivalent real income",
        color="#8E4E2C",
        fontsize=6.0,
        ha="right",
        va="top",
    )
    ax_b.text(
        direct_x,
        float(np.interp(direct_x, kappa_grid, log_y)) - 0.015 * (y_upper - y_lower),
        "Nominal local income",
        color="#285779",
        fontsize=6.0,
        ha="right",
        va="top",
    )
    ax_b.set_xlabel(r"Local organizational capacity, $\kappa$")
    ax_b.set_ylabel("Finite log income change")
    ax_b.set_title("Capacity orders the finite income crossings", pad=7.5)

    ax_a.text(-0.16, 1.12, "a", transform=ax_a.transAxes, fontsize=9.0, fontweight="bold")
    ax_b.text(-0.16, 1.12, "b", transform=ax_b.transAxes, fontsize=9.0, fontweight="bold")

    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    metadata = {
        "Title": "General capture-drag peak and finite capacity thresholds",
        "Author": "Wenxiao Dong and Yaqi Hu",
        "Subject": "Analytical illustration; not a calibration",
        "Creator": "Python and matplotlib",
    }
    fig.savefig(OUTPUT_STEM.with_suffix(".svg"), format="svg", facecolor="white",
                metadata={"Title": metadata["Title"], "Description": metadata["Subject"]})
    fig.savefig(OUTPUT_STEM.with_suffix(".pdf"), format="pdf", facecolor="white",
                metadata=metadata)
    fig.savefig(OUTPUT_STEM.with_suffix(".png"), format="png", dpi=600,
                facecolor="white", metadata={"Title": metadata["Title"]})
    plt.close(fig)


def main() -> None:
    thresholds = validate_contract()
    make_figure(thresholds)
    print("PASS: general share-speed peaks and finite capacity crossings verified")
    print(f"  kappa_R^F = {float(thresholds['kappa_r']):.6f}")
    print(f"  kappa_Y^F = {float(thresholds['kappa_y']):.6f}")
    for law in share_speed_laws():
        for kappa in (KAPPA_LOW, KAPPA_HIGH):
            peak = general_peak_objects(
                PARAMETERS, kappa, law["speed"], law["prime"], law["second"]
            )
            print(
                f"  {law['label']}, kappa={kappa:.1f}: "
                f"s*={peak['s_star']:.6f}, Lambda_max={peak['lambda_max']:.6f}"
            )
    print(f"Saved figure bundle and source data to: {FIGURE_DIR}")


if __name__ == "__main__":
    main()
