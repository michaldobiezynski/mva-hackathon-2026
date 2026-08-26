#!/usr/bin/env python3
"""Derive the identity of the premature stop codon created by a coding variant.

The stop codon's identity determines readthrough amenability (UGA > UAG > UAA),
so it is a therapeutic determinant, not just an annotation detail. For
NM_001211.6:c.2210T>G p.Leu737Ter this resolves unambiguously to TGA (UGA).

    python3 eval/stop_codon_identity.py 2210 T G 737 Leu
"""
import argparse
import sys

CODONS = {
    "Leu": {"TTA", "TTG", "CTT", "CTC", "CTA", "CTG"},
    "Ser": {"TCT", "TCC", "TCA", "TCG", "AGT", "AGC"},
    "Arg": {"CGT", "CGC", "CGA", "CGG", "AGA", "AGG"},
    "Gly": {"GGT", "GGC", "GGA", "GGG"},
    "Trp": {"TGG"},
    "Gln": {"CAA", "CAG"},
    "Glu": {"GAA", "GAG"},
    "Lys": {"AAA", "AAG"},
    "Tyr": {"TAT", "TAC"},
    "Cys": {"TGT", "TGC"},
}
STOPS = {"TAA", "TAG", "TGA"}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("cds_pos", type=int, help="1-based CDS position of the substitution")
    p.add_argument("ref", help="reference base")
    p.add_argument("alt", help="alternate base")
    p.add_argument("codon_num", type=int, help="1-based codon number of the affected residue")
    p.add_argument("residue", help="reference amino acid three-letter code, e.g. Leu")
    args = p.parse_args()

    if args.residue not in CODONS:
        print(f"No codon table entry for {args.residue}", file=sys.stderr)
        return 1

    start = (args.codon_num - 1) * 3 + 1
    offset = args.cds_pos - start
    if not 0 <= offset <= 2:
        print(f"c.{args.cds_pos} does not fall within codon {args.codon_num} "
              f"(c.{start}-{start + 2})", file=sys.stderr)
        return 1

    print(f"codon {args.codon_num} spans c.{start}-{start + 2}; "
          f"substitution at codon position {offset + 1}")
    solutions = []
    for codon in sorted(CODONS[args.residue]):
        if codon[offset] != args.ref.upper():
            continue
        mutated = codon[:offset] + args.alt.upper() + codon[offset + 1:]
        verdict = f"STOP {mutated}" if mutated in STOPS else f"{mutated} (not a stop)"
        print(f"  {codon} -> {verdict}")
        if mutated in STOPS:
            solutions.append((codon, mutated))

    if len(solutions) == 1:
        ref_codon, stop = solutions[0]
        print(f"\nUnambiguous: reference codon {ref_codon}, premature stop {stop} "
              f"({stop.replace('T', 'U')} in mRNA)")
        return 0
    print(f"\n{len(solutions)} codon(s) yield a stop; identity not determined by the "
          f"substitution alone (check the reference sequence)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
