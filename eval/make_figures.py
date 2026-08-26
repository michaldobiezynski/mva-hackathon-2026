#!/usr/bin/env python3
"""Generate the report figures.

    .venv/bin/python eval/make_figures.py

Writes PNG (for embedding) and PDF (vector, for print) into track2/figures/.
Figure 1 is drawn from UniProt O60566 feature coordinates; figure 2 reads
eval/mosaicism_scan.tsv, which is the same table the report cites.
"""
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "track2" / "figures"

INK = "#1a1a1a"
MUTED = "#6b6b6b"
NULL_ALLELE = "#b23a48"      # allele A, truncating
MISSENSE = "#2e5e8c"          # allele B, missense
DOMAIN_N = "#c9d6df"
DOMAIN_KINASE = "#a8bfae"
KARD = "#e8c07d"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"],
    "axes.edgecolor": MUTED,
    "text.color": INK,
    "axes.labelcolor": INK,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
})


def save(fig, stem):
    OUT.mkdir(parents=True, exist_ok=True)
    for ext in ("png", "pdf"):
        fig.savefig(OUT / f"{stem}.{ext}", dpi=200, bbox_inches="tight",
                    facecolor="white")
    plt.close(fig)
    print(f"wrote {stem}.png / .pdf")


def figure1_domains():
    """Reference BubR1 architecture, then what each allele actually yields."""
    fig, ax = plt.subplots(figsize=(11.5, 4.6))
    L = 1050
    bar_h = 0.13

    def domain_track(y, upto=L, faded=False, show_labels=True):
        """Draw the protein backbone and its domains up to residue `upto`."""
        alpha = 0.28 if faded else 1.0
        ax.add_patch(Rectangle((0, y), min(upto, L), bar_h, facecolor="#ececec",
                               edgecolor=MUTED, linewidth=0.6, alpha=alpha))
        for start_r, end_r, colour, label in [
            (62, 226, DOMAIN_N, "BUB1 N-terminal"),
            (660, 686, KARD, "KARD"),
            (766, 1050, DOMAIN_KINASE, "pseudokinase domain"),
        ]:
            if start_r >= upto:
                continue
            e = min(end_r, upto)
            ax.add_patch(Rectangle((start_r, y), e - start_r, bar_h, facecolor=colour,
                                   edgecolor=MUTED, linewidth=0.7, alpha=alpha))
            if show_labels and e - start_r > 60:
                ax.text((start_r + e) / 2, y + bar_h / 2, label, ha="center",
                        va="center", fontsize=8, color=INK)

    # --- Reference protein ---
    y_ref = 0.74
    domain_track(y_ref)
    ax.text(-30, y_ref + bar_h / 2, "reference", ha="right", va="center",
            fontsize=9, color=INK, fontweight="bold")
    ax.annotate("K668 acetylation (SIRT2 target)\nS670 / S676 phosphorylation",
                xy=(673, y_ref + bar_h), xytext=(560, y_ref + 0.20),
                fontsize=7.6, color=INK, ha="center",
                arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.8))

    # --- Allele A ---
    y_a = 0.44
    domain_track(y_a, upto=737, show_labels=False)
    ax.add_patch(Rectangle((737, y_a), L - 737, bar_h, facecolor="none",
                           edgecolor="#cccccc", linewidth=0.6, hatch="////"))
    ax.plot([737, 737], [y_a - 0.03, y_a + bar_h + 0.03], color=NULL_ALLELE, linewidth=2)
    ax.text(-30, y_a + bar_h / 2, "allele A", ha="right", va="center",
            fontsize=9, color=NULL_ALLELE, fontweight="bold")
    ax.text(752, y_a + bar_h / 2, "p.Leu737Ter  ·  premature TGA stop  ·  NMD expected  ·  no functional product",
            ha="left", va="center", fontsize=8, color=NULL_ALLELE)

    # --- Allele B ---
    y_b = 0.20
    domain_track(y_b, show_labels=False)
    ax.plot([1002, 1002], [y_b - 0.03, y_b + bar_h + 0.03], color=MISSENSE, linewidth=2)
    ax.plot(1002, y_b + bar_h + 0.045, marker="v", color=MISSENSE, markersize=7)
    ax.text(-30, y_b + bar_h / 2, "allele B", ha="right", va="center",
            fontsize=9, color=MISSENSE, fontweight="bold")
    ax.text(985, y_b - 0.055,
            "p.Asn1002Lys  ·  full-length product  ·  AlphaMissense 0.92 (pathogenic)",
            ha="right", va="center", fontsize=8, color=MISSENSE)

    for pos in (0, 250, 500, 750, 1000):
        ax.plot([pos, pos], [0.045, 0.065], color=MUTED, linewidth=0.7)
        ax.text(pos, 0.005, str(pos), ha="center", fontsize=7, color=MUTED)
    ax.text(L / 2, -0.055, "residue", ha="center", fontsize=8, color=MUTED)

    ax.set_xlim(-210, L + 40)
    ax.set_ylim(-0.10, 1.02)
    ax.axis("off")
    ax.set_title("The two alleles fail differently, which is what creates two separate therapeutic openings",
                 fontsize=11.5, color=INK, pad=10, loc="left")
    save(fig, "fig1_domain_architecture")


def figure2_mosaicism():
    """Per-chromosome depth ratio and heterozygous allele-balance dispersion."""
    rows = list(csv.DictReader(open(REPO / "eval" / "mosaicism_scan.tsv"), delimiter="\t"))
    chroms = [r["chrom"] for r in rows]
    ratios = [float(r["dp_ratio"]) for r in rows]
    sds = [float(r["sd_ab"]) for r in rows]
    x = range(len(chroms))

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 5.2), sharex=True,
                                   gridspec_kw={"hspace": 0.18})

    colours = [MISSENSE if c not in ("X",) else NULL_ALLELE for c in chroms]
    ax1.bar(x, ratios, color=colours, width=0.68)
    ax1.axhline(1.0, color=MUTED, linewidth=0.8, linestyle="--")
    ax1.set_ylim(0, 1.62)
    ax1.set_ylabel("median depth\n(ratio to genome)", fontsize=9)
    ax1.annotate("chrX at half depth: male proband, and a built-in control for the panel below",
                 xy=(len(chroms) - 1, 0.56), xytext=(0.4, 1.44),
                 fontsize=7.8, color=NULL_ALLELE, ha="left", va="center",
                 arrowprops=dict(arrowstyle="->", color=NULL_ALLELE, linewidth=0.8,
                                 connectionstyle="arc3,rad=-0.25"))
    ax1.set_yticks([0.0, 0.25, 0.5, 0.75, 1.0, 1.25])
    ax1.set_title("No dominant clonal aneuploidy in bulk WGS: depth is flat across autosomes",
                  fontsize=11, color=INK, loc="left", pad=8)

    ax2.bar(x, sds, color=colours, width=0.68)
    ax2.axhline(sum(sds[:18]) / 18, color=MUTED, linewidth=0.8, linestyle="--")
    ax2.set_ylabel("het allele balance\n(std. dev.)", fontsize=9)
    ax2.set_xticks(list(x))
    ax2.set_xticklabels(chroms, fontsize=8)
    ax2.set_xlabel("chromosome", fontsize=9)
    ax2.set_ylim(0, max(sds) * 1.45)
    ax2.text(0.4, max(sds) * 1.34,
             "chr20-22 show wider dispersion, but chrX matches them and its 'hets' are\n"
             "necessarily artefactual, so mapping bias is the parsimonious explanation",
             fontsize=7.8, color=MUTED, ha="left", va="top")
    ax2.text(0.4, sum(sds[:18]) / 18 + 0.003, "autosomal mean",
             fontsize=7, color=MUTED, ha="left", va="bottom")

    for ax in (ax1, ax2):
        ax.spines[["top", "right"]].set_visible(False)
    save(fig, "fig2_mosaicism_scan")


def figure3_ddg():
    """Where N1002K sits in the domain-wide ddG distribution."""
    import pandas as pd
    df = pd.read_csv(REPO / "eval" / "ddg_ssm_kinase_domain.csv")
    df["residue"] = df.position + 766
    df = df[df.wildtype != df.mutation]          # drop identity substitutions
    variant = float(df[(df.residue == 1002) & (df.mutation == "K")].ddG_pred.iloc[0])
    site = df[df.residue == 1002].ddG_pred

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 3.9),
                                   gridspec_kw={"width_ratios": [2.1, 1], "wspace": 0.28})

    ax1.hist(df.ddG_pred, bins=60, color="#c9d6df", edgecolor="white", linewidth=0.4)
    ax1.axvline(variant, color=MISSENSE, linewidth=2)
    ax1.axvline(df.ddG_pred.mean(), color=MUTED, linewidth=1, linestyle="--")
    ymax = ax1.get_ylim()[1]
    ax1.text(variant + 0.08, ymax * 0.92, f"p.Asn1002Lys\n{variant:+.2f} kcal/mol\n75th percentile",
             fontsize=8.5, color=MISSENSE, va="top")
    ax1.text(df.ddG_pred.mean() - 0.1, ymax * 0.5, "domain mean\n+0.87", fontsize=7.5,
             color=MUTED, ha="right", va="center")
    ax1.set_xlabel("predicted ΔΔG (kcal/mol); positive = destabilising", fontsize=9)
    ax1.set_ylabel("substitutions", fontsize=9)
    ax1.set_title(f"All {len(df):,} substitutions in the pseudokinase domain",
                  fontsize=10, color=INK, loc="left")

    order = site.sort_values()
    colours = [MISSENSE if abs(v - variant) < 1e-9 else "#c9d6df" for v in order]
    ax2.barh(range(len(order)), order.values, color=colours, height=0.72)
    labels = df[df.residue == 1002].set_index("ddG_pred").mutation.to_dict()
    ax2.set_yticks(range(len(order)))
    ax2.set_yticklabels([labels[v] for v in order.values], fontsize=7)
    ax2.set_xlabel("ΔΔG (kcal/mol)", fontsize=9)
    ax2.set_title("Every substitution at residue 1002", fontsize=10, color=INK, loc="left")
    ax2.text(variant + 0.05, list(order.values).index(variant), " observed",
             fontsize=7.5, color=MISSENSE, va="center")

    for ax in (ax1, ax2):
        ax.spines[["top", "right"]].set_visible(False)
    save(fig, "fig3_ddg_distribution")


if __name__ == "__main__":
    figure1_domains()
    figure2_mosaicism()
    figure3_ddg()
