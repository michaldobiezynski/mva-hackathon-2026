#!/usr/bin/env python3
"""Characterise a residue's structural environment in an AlphaFold model.

This is not a ddG calculation. It reports three things that bear on whether a
substitution is likely to destabilise a fold or to alter a surface interaction:
model confidence (pLDDT) at the site, burial (heavy-atom neighbour count within
10 A of CB, expressed as a percentile against the whole chain), and the nearest
annotated functional residues.

    .venv/bin/python eval/structural_context.py <model.pdb> 1002 737
"""
import argparse
import sys
from collections import defaultdict

import numpy as np

# UniProt O60566 features worth measuring distance to
LANDMARKS = {
    772: "ATP-binding region start", 780: "ATP-binding region end",
    795: "binding site", 882: "active-site residue (proton acceptor)",
    668: "K668 acetylation (SIRT2)", 670: "S670 phospho (CDK1)",
    676: "S676 phospho (PLK1)", 1008: "T1008 phospho (PLK1)",
}


def parse_pdb(path):
    coords, plddt, resname = defaultdict(list), {}, {}
    with open(path) as f:
        for line in f:
            if not line.startswith("ATOM"):
                continue
            element = line[76:78].strip()
            if element == "H":
                continue
            resi = int(line[22:26])
            xyz = (float(line[30:38]), float(line[38:46]), float(line[46:54]))
            coords[resi].append((line[12:16].strip(), xyz))
            plddt[resi] = float(line[60:66])
            resname[resi] = line[17:20].strip()
    return coords, plddt, resname


def reference_atom(atoms):
    """CB where present (CA for glycine), else the first atom."""
    by_name = dict(atoms)
    for name in ("CB", "CA"):
        if name in by_name:
            return by_name[name]
    return atoms[0][1]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pdb")
    ap.add_argument("residues", nargs="+", type=int)
    ap.add_argument("--radius", type=float, default=10.0)
    args = ap.parse_args()

    coords, plddt, resname = parse_pdb(args.pdb)
    if not coords:
        print("no ATOM records parsed", file=sys.stderr)
        return 1

    all_xyz = np.array([xyz for atoms in coords.values() for _, xyz in atoms])
    refs = {r: np.array(reference_atom(a)) for r, a in coords.items()}

    neighbours = {}
    for r, ref in refs.items():
        d = np.linalg.norm(all_xyz - ref, axis=1)
        neighbours[r] = int((d < args.radius).sum()) - len(coords[r])

    counts = np.array(sorted(neighbours.values()))
    print(f"chain: {len(coords)} residues; neighbour counts within {args.radius:.0f} A "
          f"(median {int(np.median(counts))}, IQR {int(np.percentile(counts,25))}-{int(np.percentile(counts,75))})\n")

    for r in args.residues:
        if r not in coords:
            print(f"residue {r}: not in model"); continue
        n = neighbours[r]
        pct = float((counts < n).sum()) / len(counts) * 100
        burial = "buried" if pct >= 66 else ("intermediate" if pct >= 33 else "exposed")
        print(f"residue {r} ({resname[r]}):")
        print(f"  pLDDT               {plddt[r]:.1f}  "
              f"({'high confidence' if plddt[r] >= 70 else 'LOW confidence - interpret with care'})")
        print(f"  neighbour count     {n}  ({pct:.0f}th percentile of chain) -> {burial}")
        near = sorted(((np.linalg.norm(refs[r] - refs[l]), l, label)
                       for l, label in LANDMARKS.items() if l in refs))[:3]
        for dist, l, label in near:
            print(f"  {dist:6.1f} A to {l:>4}  {label}")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
