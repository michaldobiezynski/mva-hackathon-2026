#!/usr/bin/env python3
"""Check that the numbers written in the reports match the committed analyses.

Across four review rounds the recurring defect was never the code or the data:
it was prose quoting an earlier version of a number the analysis had since
changed. This recomputes the load-bearing figures from the committed artefacts
and fails if a report does not contain them.

    .venv/bin/python scripts/check_report_numbers.py

Requires pandas and numpy (the repo venv), because it recomputes rather than
trusting cached text.

Limitation: this checks that each computed figure APPEARS somewhere, not that it
appears in the right sentence. A bare number can in principle match an unrelated
occurrence, so treat a pass as "no figure has silently drifted", not as proof that
every claim is correctly worded.
"""
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

REPO = Path(__file__).resolve().parent.parent
REPORTS = [
    REPO / "track2" / "report" / "michaldobiezynski_track2_report.md",
    REPO / "track1" / "report" / "michaldobiezynski_track1_report.md",
    REPO / "REPRODUCE-DDG.md",
]
DOMAIN = (766, 1050)


def ordinal(n: int) -> str:
    """1st, 2nd, 3rd, 4th ... including the 11-13 exceptions."""
    if 11 <= n % 100 <= 13:
        return f"{n}th"
    return f"{n}{ {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th') }".replace(" ", "")


def ddg_facts():
    df = pd.read_csv(REPO / "eval" / "ddg_ssm_kinase_domain.csv")
    df["residue"] = df.position + DOMAIN[0]
    real = df[df.wildtype != df.mutation]
    variant = float(real[(real.residue == 1002) & (real.mutation == "K")].ddG_pred.iloc[0])
    site = real[real.residue == 1002]
    per_site = real.groupby("residue").ddG_pred.mean()
    return {
        "ΔΔG of N1002K": f"{variant:+.2f}".replace("+", "+"),
        "count of real substitutions": f"{len(real):,}",
        "number of sites": str(real.residue.nunique()),
        "variant percentile": ordinal(round((real.ddG_pred < variant).mean() * 100)),
        "site mean ΔΔG": f"{site.ddG_pred.mean():+.2f}",
        "domain mean ΔΔG": f"{real.ddG_pred.mean():+.2f}",
        "share destabilising": f"{(real.ddG_pred > 0).mean() * 100:.1f}%",
        "site percentile": ordinal(round((per_site < site.ddG_pred.mean()).mean() * 100)),
    }


def burial_facts(pdb: Path):
    """Recompute neighbour counts and the intra/extra split for both residues."""
    coords, plddt = {}, {}
    for line in pdb.read_text().splitlines():
        if not line.startswith("ATOM") or line[76:78].strip() == "H":
            continue
        r = int(line[22:26])
        coords.setdefault(r, []).append(
            (line[12:16].strip(), (float(line[30:38]), float(line[38:46]), float(line[46:54]))))
        plddt[r] = float(line[60:66])

    def ref(r):
        named = dict(coords[r])
        for name in ("CB", "CA"):
            if name in named:
                return np.array(named[name])
        return np.array(coords[r][0][1])

    all_xyz = np.array([xyz for atoms in coords.values() for _, xyz in atoms])
    facts = {}
    for target in (1002, 737):
        t = ref(target)
        total = int((np.linalg.norm(all_xyz - t, axis=1) < 10).sum()) - len(coords[target])
        intra = sum(1 for r, atoms in coords.items() if DOMAIN[0] <= r <= DOMAIN[1] and r != target
                    for _, xyz in atoms if np.linalg.norm(np.array(xyz) - t) < 10)
        facts[f"residue {target} neighbour count"] = str(total)
        facts[f"residue {target} intra-domain"] = str(intra)
        if target == 737:
            facts["residue 737 extra-domain"] = str(total - intra)
    facts["Asn1002 pLDDT"] = f"{plddt[1002]:.1f}"
    return facts


def mosaicism_facts():
    df = pd.read_csv(REPO / "eval" / "mosaicism_scan.tsv", sep="\t")
    x = df[df.chrom == "X"].dp_ratio.iloc[0]
    return {"chrX depth ratio": f"{x:.2f}"}


def main() -> int:
    pdb = REPO / "eval" / "bubr1_kinase_domain.pdb"
    facts = dict(ddg_facts())
    facts.update(mosaicism_facts())
    # The committed domain PDB cannot give whole-chain burial; use the cached
    # full-model output instead, which the reproduction doc tells judges to
    # regenerate. Skip rather than assert if the full model is absent locally.
    full = REPO / "eval" / "structural_context_output.txt"
    if full.exists():
        text = full.read_text()
        for label, pattern in [
            ("residue 1002 neighbour count", r"residue 1002 \(ASN\):.*?neighbour count\s+(\d+)"),
            ("residue 737 neighbour count", r"residue 737 \(LEU\):.*?neighbour count\s+(\d+)"),
            ("residue 1002 intra-domain", r"residue 1002 \(ASN\):.*?intra-domain \(766-1050\) (\d+)"),
            ("residue 737 intra-domain", r"residue 737 \(LEU\):.*?intra-domain \(766-1050\) (\d+)"),
            ("residue 737 extra-domain", r"residue 737 \(LEU\):.*?extra-domain (\d+)"),
        ]:
            m = re.search(pattern, text, re.S)
            if m:
                facts[label] = m.group(1)

    corpus = {p: p.read_text() for p in REPORTS if p.exists()}
    failures = []
    print(f"checking {len(facts)} computed figures against {len(corpus)} documents\n")
    for label, value in sorted(facts.items()):
        pattern = re.compile(r"(?<![\w.])" + re.escape(value) + r"(?![\w.])")
        where = [p.name for p, text in corpus.items() if pattern.search(text)]
        if where:
            print(f"  OK    {label:34s} {value:>9s}  found in {', '.join(where)}")
        else:
            print(f"  ABSENT {label:33s} {value:>9s}  in no document")
            failures.append((label, value))

    print(f"\n{len(failures)} computed figure(s) absent from every document")
    if failures:
        print("A figure absent everywhere is usually prose that drifted from the analysis, "
              "or a value the reports deliberately do not quote. Check each before submitting.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
