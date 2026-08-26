#!/usr/bin/env python3
"""Offline Track 1 submission checker.

Runs the challenge's own vendored parser and scorer (eval/evaluation.py) so a
CSV is validated, and score-tested against ground-truth hypotheses, BEFORE one
of the 6 real submissions is spent. The real answer key is private; hypothesis
files answer "if the truth were X, what would this CSV score?".

    python3 eval/local_scorer.py track1/predictions/foo.csv
    python3 eval/local_scorer.py track1/predictions/foo.csv --truth eval/hypotheses/
    python3 eval/local_scorer.py track1/predictions/foo.csv --truth eval/hypotheses/demo.json

Hypothesis JSON mirrors the Space's groundtruth formats:
    {"PROBAND01": [["chr1", 100000, "A", "T"], ["chr1", 200000, "G", "C"]]}
or  {"PROBAND01": {"primary_variants": [{"chrom": ..., "pos": ..., "ref": ..., "alt": ...}]}}
Keys starting with "_" are ignored (usable for comments).
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from evaluation import load_submission, score_proband


def load_truth(path: Path) -> dict[str, frozenset]:
    raw = json.loads(path.read_text())
    result = {}
    for pid, entry in raw.items():
        if pid.startswith("_"):
            continue
        if isinstance(entry, list):
            result[pid] = frozenset(tuple(v) for v in entry)
        else:
            result[pid] = frozenset(
                (v["chrom"], v["pos"], v["ref"], v["alt"])
                for v in entry.get("primary_variants", [])
            )
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", help="predictions CSV in the official Track 1 format")
    parser.add_argument("--truth", help="hypothesis JSON file, or a directory of them")
    args = parser.parse_args()

    try:
        submissions = load_submission(args.csv)
    except Exception as e:
        print(f"REJECTED by the challenge parser: {e}", file=sys.stderr)
        return 1
    if not submissions:
        print("REJECTED: no valid rows found.", file=sys.stderr)
        return 1

    for pid, rows in submissions.items():
        print(f"\nProband {pid}: {len(rows)} row(s), parsed and ranked by EPCR desc")
        for row in rows:
            variants = " + ".join(f"{c}:{p} {r}>{a}" for c, p, r, a in sorted(row.variants))
            pair = "pair" if len(row.variants) == 2 else "single"
            print(f"  rank {row.rank:2d}  epcr {row.epcr:.3f}  [{pair}] [{row.finding_type}]  {variants}")

    if not args.truth:
        print("\nFormat OK. No --truth given, so no scoring performed.")
        return 0

    truth_path = Path(args.truth)
    truth_files = sorted(truth_path.glob("*.json")) if truth_path.is_dir() else [truth_path]
    if not truth_files:
        print(f"No hypothesis JSON files found at {truth_path}", file=sys.stderr)
        return 1

    for tf in truth_files:
        gt = load_truth(tf)
        print(f"\n--- Hypothesis: {tf.name}")
        for pid, rows in submissions.items():
            if pid not in gt:
                print(f"  {pid}: not present in this hypothesis, skipped")
                continue
            r = score_proband(pid, rows, gt[pid])
            match = (
                f"FULL match at rank {r.full_match_rank}"
                if r.full_match_rank is not None
                else (
                    f"PARTIAL match (one of two) at rank {r.partial_match_rank}"
                    if r.partial_match_rank is not None
                    else "NO match"
                )
            )
            print(f"  {pid}: rank points {r.rank_points:.1f}/100  f-max {r.f_max:.3f} "
                  f"(threshold {r.f_max_threshold})  {match}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
