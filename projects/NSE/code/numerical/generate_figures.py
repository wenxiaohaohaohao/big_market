"""Generate the three paper figures and their source-data CSV files."""

from __future__ import annotations

import csv
from dataclasses import replace
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import BoundaryNorm, ListedColormap

from model import (
    Parameters,
    consumer_price_index,
    entry_threshold,
    infrastructure_supply,
    local_producer_income,
    nominal_effect,
    nominal_income,
    organization_threshold,
    platform_share,
    producer_choice,
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
            "figure.dpi": 180,
            "savefig.dpi": 300,
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
    costs = np.linspace(0.45, 1.45, 241)
    infrastructure = np.linspace(0.0, 1.20, 241)
    regime = np.zeros((len(infrastructure), len(costs)), dtype=int)
    rows: list[dict] = []
    code = {"0": 0, "P": 1, "L": 2}

    for i, g in enumerate(infrastructure):
        for j, c in enumerate(costs):
            pc = replace(p, c=float(c))
            choice = producer_choice(z, float(g), pc)
            regime[i, j] = code[choice]
            rows.append(
                {
                    "z": z,
                    "c": float(c),
                    "G": float(g),
                    "regime": choice,
                }
            )

    write_rows(
        SOURCE_DIR / "figure_1_phase_diagram.csv",
        ["z", "c", "G", "regime"],
        rows,
    )

    fig, ax = plt.subplots(figsize=(6.4, 4.3))
    cmap = ListedColormap(["#d9d9d9", "#4c78a8", "#f2a541"])
    norm = BoundaryNorm([-0.5, 0.5, 1.5, 2.5], cmap.N)
    # Rasterizing only the dense regime layer prevents vector-PDF hairline
    # seams while keeping axes, labels, and threshold lines as vector objects.
    mesh = ax.pcolormesh(
        costs,
        infrastructure,
        regime,
        cmap=cmap,
        norm=norm,
        shading="auto",
        rasterized=True,
    )
    cbar = fig.colorbar(mesh, ax=ax, ticks=[0, 1, 2], pad=0.02)
    cbar.ax.set_yticklabels(["No entry", "External platform", "Local embedded"])
    entry_line = np.array(
        [entry_threshold(z, replace(p, c=float(c))) for c in costs],
        dtype=float,
    )
    embedded_line = np.array(
        [organization_threshold(z, replace(p, c=float(c))) for c in costs],
        dtype=float,
    )
    ax.plot(costs, entry_line, color="#555555", linewidth=1.0, linestyle="--")
    ax.plot(costs, embedded_line, color="#8c5d19", linewidth=1.0)
    ax.set_xlabel("Relative production cost, $c$ (lower = stronger LCA)")
    ax.set_ylabel("Shared infrastructure, $G$")
    ax.set_ylim(infrastructure[0], infrastructure[-1])
    ax.set_title("Industry realization and organizational regime")
    ax.text(
        0.02,
        0.02,
        "Illustrative parameters; $z=0.5$",
        transform=ax.transAxes,
        fontsize=8,
        color="#444444",
    )
    save_figure(fig, "figure_1_phase_diagram")


def figure_thresholds(p: Parameters, z: float = 0.5) -> None:
    costs = np.linspace(0.82, 1.02, 121)
    rows = threshold_rows(costs, z, p)
    write_rows(
        SOURCE_DIR / "figure_2_thresholds.csv",
        ["c", "G_E", "G_L", "G_R", "G_Y"],
        rows,
    )

    fig, ax = plt.subplots(figsize=(6.4, 4.3))
    c = np.array([row["c"] for row in rows])
    styles = {
        "G_E": ("#666666", "--", "Entry $G_E$"),
        "G_L": ("#f2a541", "-", "Embedding $G_L$"),
        "G_R": ("#54a24b", "-.", "Real income $G_R$"),
        "G_Y": ("#b279a2", "-", "Nominal income $G_Y$"),
    }
    for key, (color, linestyle, label) in styles.items():
        values = np.array([row[key] for row in rows], dtype=float)
        ax.plot(c, values, color=color, linestyle=linestyle, linewidth=2.0, label=label)

    ax.set_xlabel("Relative production cost, $c$ (lower = stronger LCA)")
    ax.set_ylabel("Infrastructure threshold")
    ax.set_ylim(0.0, 2.60)
    ax.set_title("LCA-conditioned development thresholds")
    ax.legend(frameon=False, ncol=3)
    ax.text(
        0.02,
        0.02,
        "Illustrative parameters; $z=0.5$",
        transform=ax.transAxes,
        fontsize=8,
        color="#444444",
    )
    save_figure(fig, "figure_2_thresholds")


def figure_reform_paths(p: Parameters) -> None:
    z_grid = np.linspace(0.0, 1.2, 161)
    participation = [0.05, 0.50, 0.99]
    colors = ["#4c78a8", "#f2a541", "#54a24b"]
    rows: list[dict] = []

    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.5))
    common_shares = [platform_share(float(z), p) for z in z_grid]
    axes[0].plot(z_grid, common_shares, color="#333333", linewidth=2.2)
    for vartheta, color in zip(participation, colors):
        g = infrastructure_supply(vartheta, p)
        nominal_effects = []
        real_effects = []
        nominal_levels = []
        real_levels = []
        nominal_base = nominal_income(float(z_grid[0]), g, p)
        real_base = real_income(float(z_grid[0]), g, p)
        for z in z_grid:
            s = platform_share(float(z), p)
            y_effect = nominal_effect(float(z), g, p)
            r_effect = real_effect(float(z), g, p)
            nominal_effects.append(y_effect)
            real_effects.append(r_effect)
            nominal_levels.append(nominal_income(float(z), g, p) / nominal_base)
            real_levels.append(real_income(float(z), g, p) / real_base)
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
                    "nominal_income_index": nominal_levels[-1],
                    "real_income_index": real_levels[-1],
                    "consumer_price_index": consumer_price_index(float(z), p),
                    "regime": producer_choice(float(z), g, p),
                }
            )

        label = rf"$\vartheta={vartheta:.2f}$, $G={g:.2f}$"
        axes[1].plot(z_grid, nominal_levels, color=color, linewidth=2, label=label)
        axes[2].plot(z_grid, real_levels, color=color, linewidth=2, label=label)

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

    axes[0].set_title("Consumer access")
    axes[0].set_ylabel("Platform expenditure share")
    axes[1].set_title("Nominal local income")
    axes[1].set_ylabel(r"$Y(z)/Y(0)$")
    axes[2].set_title("Consumption-equivalent income")
    axes[2].set_ylabel(r"$R(z)/R(0)$")
    for ax in axes:
        ax.set_xlabel("Platform integration, $z$")
    axes[1].axhline(1.0, color="#999999", linewidth=0.8, linestyle=":")
    axes[2].axhline(1.0, color="#999999", linewidth=0.8, linestyle=":")
    axes[1].legend(frameon=False, fontsize=7.5)
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
