#!/usr/bin/env python3
"""Summarise a ThermoMPNN site-saturation scan for one variant of interest.

The scan itself is produced by ThermoMPNN (Dieckhaus et al., PNAS 2024); see
REPRODUCE-DDG.md for the exact commands. This script reads the resulting CSV
and does three things the raw numbers do not: it establishes the sign
convention empirically, places the variant against the distribution of all
substitutions in the domain, and shows the full substitution profile at the
site.

    .venv/bin/python eval/ddg_analysis.py --residue 1002 --mutation K
"""
import argparse
import sys
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parent.parent
DEFAULT_CSV = REPO / "eval" / "ddg_ssm_kinase_domain.csv"
DOMAIN_START = 766  # scan was run on the extracted pseudokinase domain


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--csv", default=str(DEFAULT_CSV))
    ap.add_argument("--residue", type=int, required=True, help="residue number in full-length numbering")
    ap.add_argument("--mutation", required=True, help="single-letter substituted residue")
    ap.add_argument("--domain-start", type=int, default=DOMAIN_START)
    args = ap.parse_args()

    df = pd.read_csv(args.csv)
    df["residue"] = df.position + args.domain_start

    # Sign convention, established from the data rather than assumed: identity
    # substitutions must score zero, and prolines should sit on the
    # destabilising side of the overall mean.
    identity = df[df.wildtype == df.mutation].ddG_pred
    pro = df[df.mutation == "P"].ddG_pred
    destabilising_is_positive = pro.mean() > df.ddG_pred.mean()
    print(f"scan: {len(df)} substitutions across {df.residue.nunique()} residues")
    print(f"  identity substitutions mean {identity.mean():+.3f} (expected 0)")
    print(f"  X->Pro mean {pro.mean():+.3f} vs overall mean {df.ddG_pred.mean():+.3f}")
    print(f"  => {'positive' if destabilising_is_positive else 'negative'} values are destabilising\n")

    row = df[(df.residue == args.residue) & (df.mutation == args.mutation)]
    if row.empty:
        print(f"{args.residue}{args.mutation} not present in scan "
              f"(domain covers {df.residue.min()}-{df.residue.max()})", file=sys.stderr)
        return 1

    value = float(row.ddG_pred.iloc[0])
    wt = row.wildtype.iloc[0]
    pct = (df.ddG_pred < value).mean() * 100 if destabilising_is_positive else (df.ddG_pred > value).mean() * 100
    print(f"{wt}{args.residue}{args.mutation}: ddG = {value:+.3f} kcal/mol "
          f"({pct:.0f}th percentile of all substitutions in this domain)")

    site = df[df.residue == args.residue].sort_values("ddG_pred", ascending=not destabilising_is_positive)
    site_mean = site.ddG_pred.mean()
    per_site = df.groupby("residue").ddG_pred.mean()
    site_pct = (per_site < site_mean).mean() * 100 if destabilising_is_positive else (per_site > site_mean).mean() * 100
    print(f"site mean {site_mean:+.3f} ({site_pct:.0f}th percentile of {len(per_site)} sites): "
          f"this position is {'more' if site_pct > 50 else 'less'} substitution-sensitive than average\n")

    rank = list(site.mutation).index(args.mutation) + 1
    print(f"substitution profile at {wt}{args.residue} "
          f"(most destabilising first; observed variant ranks {rank} of {len(site)}):")
    for _, r in site.iterrows():
        mark = "   <-- observed" if r.mutation == args.mutation else ""
        print(f"  {wt}{args.residue}{r.mutation}  {r.ddG_pred:+.3f}{mark}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
