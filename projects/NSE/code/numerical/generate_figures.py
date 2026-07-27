"""Generate the three paper figures and their source-data CSV files."""

from __future__ import annotations

import csv
from dataclasses import replace
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq

from model import (
    Parameters,
    consumer_price_index,
    entry_threshold,
    income_denominator,
    infrastructure_supply,
    local_producer_income,
    nominal_effect,
    nominal_income,
    organization_threshold,
    platform_share,
    producer_choice,
    producer_profit,
    real_effect,
    real_income,
    threshold_rows,
    validate_parameters,
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]
FIGURE_DIR = PROJECT_ROOT / "figures"
SOURCE_DIR = FIGURE_DIR / "source_data"


def configure_style() -> None:
    mpl.rcParams.update(
        {
            "font.family": "serif",
            "font.size": 9.5,
            "axes.labelsize": 10,
            "axes.titlesize": 10.5,
            "legend.fontsize": 8.5,
            "xtick.labelsize": 8.5,
            "ytick.labelsize": 8.5,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": False,
            "figure.dpi": 180,
            "savefig.dpi": 300,
            "lines.antialiased": True,
            "lines.solid_capstyle": "round",
            "lines.solid_joinstyle": "round",
            "path.simplify": False,
        }
    )


def write_rows(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def save_figure(fig: plt.Figure, stem: str) -> None:
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / f"{stem}.pdf", bbox_inches="tight")
    fig.savefig(FIGURE_DIR / f"{stem}.png", bbox_inches="tight")
    plt.close(fig)


def figure_phase_diagram(p: Parameters, z: float = 0.5) -> None:
    costs = np.linspace(0.45, 1.45, 801)
    g_min, g_max = 0.0, 1.20
    entry_line = np.array(
        [entry_threshold(z, replace(p, c=float(c))) for c in costs],
        dtype=float,
    )
    embedded_line = np.array(
        [organization_threshold(z, replace(p, c=float(c))) for c in costs],
        dtype=float,
    )
    if np.any(embedded_line + 1e-10 < entry_line):
        raise RuntimeError("organizational threshold lies below the entry threshold")

    rows: list[dict] = []
    for c, g_entry, g_embedded in zip(costs, entry_line, embedded_line):
        rows.append(
            {
                "z": z,
                "c": float(c),
                "G_E": float(g_entry),
                "G_L": float(g_embedded),
                "platform_interval_width": float(max(0.0, g_embedded - g_entry)),
            }
        )

    write_rows(
        SOURCE_DIR / "figure_1_phase_diagram.csv",
        ["z", "c", "G_E", "G_L", "platform_interval_width"],
        rows,
    )

    fig, ax = plt.subplots(figsize=(6.8, 4.4))
    entry_clip = np.clip(entry_line, g_min, g_max)
    embedded_clip = np.clip(embedded_line, g_min, g_max)
    embedded_clip = np.maximum(entry_clip, embedded_clip)
    palette = {
        "none": "#E8E8E8",
        "platform": "#A9C4DD",
        "local": "#F4C47D",
        "entry_line": "#4D4D4D",
        "local_line": "#9A5B13",
    }
    ax.fill_between(
        costs,
        g_min,
        entry_clip,
        color=palette["none"],
        linewidth=0,
    )
    ax.fill_between(
        costs,
        entry_clip,
        embedded_clip,
        color=palette["platform"],
        linewidth=0,
    )
    ax.fill_between(
        costs,
        embedded_clip,
        g_max,
        color=palette["local"],
        linewidth=0,
    )
    ax.plot(
        costs,
        entry_line,
        color=palette["entry_line"],
        linewidth=1.35,
        linestyle="--",
        label="Actual-entry boundary $G_E$",
    )
    ax.plot(
        costs,
        embedded_line,
        color=palette["local_line"],
        linewidth=1.45,
        label="Local embeddedness $G_L$",
    )
    line_handles = ax.get_lines()
    ax.legend(
        handles=line_handles,
        frameon=False,
        ncol=1,
        loc="lower right",
        columnspacing=1.2,
        handlelength=1.7,
    )
    ax.set_xlabel("Relative production cost, $c$ (lower = stronger LCA)")
    ax.set_ylabel("Shared infrastructure, $G$")
    ax.set_xlim(costs[0], costs[-1])
    ax.set_ylim(g_min, g_max)
    ax.set_title("Actual production and organizational regime")
    ax.grid(axis="y", color="#D9D9D9", linewidth=0.55, alpha=0.65)
    ax.text(
        0.25,
        0.83,
        "Local embedded",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=9,
        color="#6F4513",
    )
    ax.text(
        0.46,
        0.42,
        "External\nplatform",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=8.5,
        color="#365F83",
        rotation=72,
    )
    ax.text(
        0.80,
        0.62,
        "No entry",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=9,
        color="#555555",
    )
    ax.text(
        0.02,
        0.02,
        "Exact analytical boundaries; illustrative parameters; $z=0.5$",
        transform=ax.transAxes,
        fontsize=8,
        color="#444444",
    )
    save_figure(fig, "figure_1_phase_diagram")


def figure_thresholds(p: Parameters, z: float = 0.5) -> None:
    costs = np.linspace(0.82, 1.02, 401)
    rows = threshold_rows(costs, z, p)
    write_rows(
        SOURCE_DIR / "figure_2_thresholds.csv",
        ["c", "G_E", "G_L", "G_R", "G_Y"],
        rows,
    )

    fig, axes = plt.subplots(1, 2, figsize=(9.4, 4.0), sharey=True)
    c = np.array([row["c"] for row in rows])
    values = {
        key: np.array([row[key] for row in rows], dtype=float)
        for key in ("G_E", "G_L", "G_R", "G_Y")
    }
    baseline_idx = int(np.argmin(np.abs(c - p.c)))

    structural_styles = {
        "G_E": ("#4D4D4D", "--", "Actual entry $G_E$"),
        "G_L": ("#D68A20", "-", "Embeddedness $G_L$"),
    }
    for key, (color, linestyle, label) in structural_styles.items():
        axes[0].plot(
            c,
            values[key],
            color=color,
            linestyle=linestyle,
            linewidth=1.9,
            label=label,
        )
        axes[0].scatter(
            [c[baseline_idx]],
            [values[key][baseline_idx]],
            s=25,
            facecolor="white",
            edgecolor=color,
            linewidth=1.1,
            zorder=4,
        )
    axes[0].fill_between(
        c,
        values["G_E"],
        values["G_L"],
        color="#A9C4DD",
        alpha=0.32,
        linewidth=0,
        label="Platform-dependent interval",
    )

    income_styles = {
        "G_R": ("#3F7C78", "--", "Real income $G_R$"),
        "G_Y": ("#9A5F8A", "-", "Nominal income $G_Y$"),
    }
    for key, (color, linestyle, label) in income_styles.items():
        axes[1].plot(
            c,
            values[key],
            color=color,
            linestyle=linestyle,
            linewidth=1.9,
            label=label,
        )
        axes[1].scatter(
            [c[baseline_idx]],
            [values[key][baseline_idx]],
            s=25,
            facecolor="white",
            edgecolor=color,
            linewidth=1.1,
            zorder=4,
        )
    axes[1].fill_between(
        c,
        values["G_R"],
        values["G_Y"],
        color="#C7AFCA",
        alpha=0.30,
        linewidth=0,
        label="Real gain before nominal gain",
    )

    titles = [
        "(a) Production and organization",
        "(b) Local-income effects",
    ]
    for ax, title in zip(axes, titles):
        ax.set_xlabel("Relative production cost, $c$\n(lower = stronger LCA)")
        ax.set_xlim(c[0], c[-1])
        ax.set_ylim(0.0, 2.60)
        ax.set_title(title)
        ax.axvline(p.c, color="#9A9A9A", linewidth=0.8, linestyle=":")
        ax.grid(axis="y", color="#D9D9D9", linewidth=0.55, alpha=0.65)
        ax.legend(frameon=False, loc="upper left")
    axes[0].set_ylabel("Infrastructure threshold")
    fig.suptitle("LCA-conditioned infrastructure thresholds", y=1.01, fontsize=11)
    save_figure(fig, "figure_2_thresholds")


def _regime_transition_events(
    g: float,
    p: Parameters,
    z_min: float = 0.0,
    z_max: float = 1.2,
) -> list[tuple[float, str, str]]:
    """Locate exact entry and organization switches for a fixed G.

    The dense grid only brackets events. Brent's method then solves the
    relevant profit equality, so plotted jumps are not tied to grid spacing.
    """

    scan = np.linspace(z_min, z_max, 2401)
    modes = [producer_choice(float(z), g, p) for z in scan]
    events: list[tuple[float, str, str]] = []
    for idx in range(1, len(scan)):
        left_mode, right_mode = modes[idx - 1], modes[idx]
        if left_mode == right_mode:
            continue

        if left_mode == "0":
            gap = lambda z: producer_profit(right_mode, float(z), g, p)
        elif right_mode == "0":
            gap = lambda z: producer_profit(left_mode, float(z), g, p)
        else:
            gap = lambda z: (
                producer_profit(right_mode, float(z), g, p)
                - producer_profit(left_mode, float(z), g, p)
            )

        left_z, right_z = float(scan[idx - 1]), float(scan[idx])
        root = float(brentq(gap, left_z, right_z, xtol=1e-13, rtol=1e-13))
        if events and abs(root - events[-1][0]) < 1e-10:
            continue
        events.append((root, left_mode, right_mode))
    return events


def _income_for_mode(
    mode: str,
    z: float,
    g: float,
    p: Parameters,
    *,
    real: bool,
) -> float:
    autonomous = p.b0 + local_producer_income(mode, z, g, p)
    value = autonomous / income_denominator(z, p)
    if real:
        value /= consumer_price_index(z, p) ** p.alpha_m
    return value


def _plot_event_aware_income(
    ax: plt.Axes,
    g: float,
    p: Parameters,
    color: str,
    linestyle: str,
    label: str,
    *,
    real: bool,
    event_rows: list[dict],
    vartheta: float,
) -> None:
    z_min, z_max = 0.0, 1.2
    events = _regime_transition_events(g, p, z_min, z_max)
    base = real_income(z_min, g, p) if real else nominal_income(z_min, g, p)
    boundaries = [z_min, *[event[0] for event in events], z_max]

    for idx in range(len(boundaries) - 1):
        left, right = boundaries[idx], boundaries[idx + 1]
        midpoint = 0.5 * (left + right)
        mode = producer_choice(midpoint, g, p)
        segment = np.linspace(left, right, 121)
        values = np.array(
            [
                _income_for_mode(mode, float(z), g, p, real=real) / base
                for z in segment
            ]
        )
        ax.plot(
            segment,
            values,
            color=color,
            linestyle=linestyle,
            linewidth=1.9,
            label=label if idx == 0 else None,
            zorder=3,
        )

    for event_z, left_mode, right_mode in events:
        left_value = (
            _income_for_mode(left_mode, event_z, g, p, real=real) / base
        )
        right_value = (
            _income_for_mode(right_mode, event_z, g, p, real=real) / base
        )
        ax.vlines(
            event_z,
            left_value,
            right_value,
            color=color,
            linewidth=1.15,
            alpha=0.85,
            zorder=4,
        )
        ax.scatter(
            [event_z],
            [left_value],
            s=20,
            facecolor="white",
            edgecolor=color,
            linewidth=1.0,
            zorder=5,
        )
        ax.scatter(
            [event_z],
            [right_value],
            s=20,
            facecolor=color,
            edgecolor=color,
            linewidth=0.8,
            zorder=5,
        )
        if not real:
            event_rows.append(
                {
                    "vartheta": vartheta,
                    "G": g,
                    "z": event_z,
                    "from_regime": left_mode,
                    "to_regime": right_mode,
                    "nominal_left_index": left_value,
                    "nominal_right_index": right_value,
                    "real_left_index": (
                        _income_for_mode(
                            left_mode, event_z, g, p, real=True
                        )
                        / real_income(z_min, g, p)
                    ),
                    "real_right_index": (
                        _income_for_mode(
                            right_mode, event_z, g, p, real=True
                        )
                        / real_income(z_min, g, p)
                    ),
                }
            )


def figure_reform_paths(p: Parameters) -> None:
    z_grid = np.linspace(0.0, 1.2, 321)
    participation = [0.05, 0.50, 0.99]
    colors = ["#4C78A8", "#D68A20", "#8B6F9E"]
    linestyles = ["-", "--", "-."]
    rows: list[dict] = []
    event_rows: list[dict] = []

    fig, axes = plt.subplots(1, 3, figsize=(11.0, 3.7))
    common_shares = [platform_share(float(z), p) for z in z_grid]
    axes[0].plot(z_grid, common_shares, color="#333333", linewidth=2.2)
    for vartheta, color, linestyle in zip(participation, colors, linestyles):
        g = infrastructure_supply(vartheta, p)
        nominal_base = nominal_income(float(z_grid[0]), g, p)
        real_base = real_income(float(z_grid[0]), g, p)
        for z in z_grid:
            s = platform_share(float(z), p)
            y_effect = nominal_effect(float(z), g, p)
            r_effect = real_effect(float(z), g, p)
            nominal_level = nominal_income(float(z), g, p) / nominal_base
            real_level = real_income(float(z), g, p) / real_base
            rows.append(
                {
                    "vartheta": vartheta,
                    "G": g,
                    "z": float(z),
                    "platform_share": s,
                    "nominal_income_effect": y_effect,
                    "real_income_effect": r_effect,
                    "nominal_income": nominal_income(float(z), g, p),
                    "real_income": real_income(float(z), g, p),
                    "nominal_income_index": nominal_level,
                    "real_income_index": real_level,
                    "consumer_price_index": consumer_price_index(float(z), p),
                    "regime": producer_choice(float(z), g, p),
                }
            )

        label = rf"$\vartheta={vartheta:.2f}$, $G={g:.2f}$"
        _plot_event_aware_income(
            axes[1],
            g,
            p,
            color,
            linestyle,
            label,
            real=False,
            event_rows=event_rows,
            vartheta=vartheta,
        )
        _plot_event_aware_income(
            axes[2],
            g,
            p,
            color,
            linestyle,
            label,
            real=True,
            event_rows=event_rows,
            vartheta=vartheta,
        )

    write_rows(
        SOURCE_DIR / "figure_3_reform_paths.csv",
        [
            "vartheta",
            "G",
            "z",
            "platform_share",
            "nominal_income_effect",
            "real_income_effect",
            "nominal_income",
            "real_income",
            "nominal_income_index",
            "real_income_index",
            "consumer_price_index",
            "regime",
        ],
        rows,
    )
    write_rows(
        SOURCE_DIR / "figure_3_transition_events.csv",
        [
            "vartheta",
            "G",
            "z",
            "from_regime",
            "to_regime",
            "nominal_left_index",
            "nominal_right_index",
            "real_left_index",
            "real_right_index",
        ],
        event_rows,
    )

    axes[0].set_title("(a) Consumer access")
    axes[0].set_ylabel("Platform expenditure share")
    axes[1].set_title("(b) Nominal local income")
    axes[1].set_ylabel(r"$Y(z)/Y(0)$")
    axes[2].set_title("(c) Consumption-equivalent income")
    axes[2].set_ylabel(r"$R(z)/R(0)$")
    for ax in axes:
        ax.set_xlabel("Platform integration, $z$")
        ax.grid(axis="y", color="#D9D9D9", linewidth=0.55, alpha=0.65)
    axes[1].axhline(1.0, color="#999999", linewidth=0.8, linestyle=":")
    axes[2].axhline(1.0, color="#999999", linewidth=0.8, linestyle=":")
    axes[1].legend(frameon=False, fontsize=7.5, loc="upper left")
    fig.text(
        0.995,
        0.01,
        "Open/filled markers and vertical segments denote exact equilibrium switches.",
        ha="right",
        va="bottom",
        fontsize=7.5,
        color="#555555",
    )
    save_figure(fig, "figure_3_reform_paths")


def mechanism_closures(p: Parameters, z: float = 0.5) -> None:
    scenarios = {
        "baseline": p,
        "no_consumer_capture_gap": replace(p, ell_p=p.ell_a),
        "reverse_consumer_capture_gap": replace(p, ell_p=min(1.0, p.ell_a + 0.10)),
        "producer_payments_localized": replace(p, platform_localization=1.0),
        "positive_access_infrastructure_complementarity": replace(
            p, chi_extension=0.20
        ),
        "partial_platform_localization": replace(p, platform_localization=0.5),
    }
    rows: list[dict] = []
    for name, ps in scenarios.items():
        for g in np.linspace(0.0, 1.2, 121):
            rows.append(
                {
                    "scenario": name,
                    "z": z,
                    "G": float(g),
                    "nominal_effect": nominal_effect(z, float(g), ps),
                    "real_effect": real_effect(z, float(g), ps),
                    "nominal_income": nominal_income(z, float(g), ps),
                    "real_income": real_income(z, float(g), ps),
                    "regime": producer_choice(z, float(g), ps),
                }
            )
    write_rows(
        SOURCE_DIR / "appendix_mechanism_closures.csv",
        [
            "scenario",
            "z",
            "G",
            "nominal_effect",
            "real_effect",
            "nominal_income",
            "real_income",
            "regime",
        ],
        rows,
    )


def channel_restriction_comparison(p: Parameters, z: float = 0.5) -> None:
    """Compare facilitation and an external-channel restriction.

    The restriction is a deliberately narrow policy example. It is not the
    general NSE concept of protecting a comparative-advantage-defying sector.
    """

    scenarios = [
        ("baseline", replace(p), 0.80),
        ("facilitation", replace(p), 1.15),
        (
            "external_channel_restriction",
            replace(p, d_p=0.50, consumer_platform_wedge=1.10),
            0.80,
        ),
    ]
    rows: list[dict] = []
    expected_modes = {
        "baseline": "P",
        "facilitation": "L",
        "external_channel_restriction": "L",
    }
    for name, ps, g in scenarios:
        mode = producer_choice(z, g, ps)
        if mode != expected_modes[name]:
            raise RuntimeError(
                f"policy design no longer matches the intended regime: {name}={mode}"
            )
        rows.append(
            {
                "scenario": name,
                "z": z,
                "G": g,
                "d_P": ps.d_p,
                "consumer_platform_wedge": ps.consumer_platform_wedge,
                "regime": mode,
                "platform_share": platform_share(z, ps),
                "consumer_price_index": consumer_price_index(z, ps),
                "producer_entry_threshold_G_E": entry_threshold(z, ps),
                "local_producer_income": local_producer_income(mode, z, g, ps),
                "nominal_local_income": nominal_income(z, g, ps),
                "consumption_equivalent_income": real_income(z, g, ps),
            }
        )

    write_rows(
        SOURCE_DIR / "appendix_channel_restriction.csv",
        [
            "scenario",
            "z",
            "G",
            "d_P",
            "consumer_platform_wedge",
            "regime",
            "platform_share",
            "consumer_price_index",
            "producer_entry_threshold_G_E",
            "local_producer_income",
            "nominal_local_income",
            "consumption_equivalent_income",
        ],
        rows,
    )


def main() -> None:
    p = Parameters()
    validate_parameters(p)
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    configure_style()
    figure_phase_diagram(p)
    figure_thresholds(p)
    figure_reform_paths(p)
    mechanism_closures(p)
    channel_restriction_comparison(p)
    print(f"Figures written to {FIGURE_DIR}")
    print(f"Source data written to {SOURCE_DIR}")


if __name__ == "__main__":
    main()
