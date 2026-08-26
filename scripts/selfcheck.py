#!/usr/bin/env python3
"""Repo hygiene gate for the MVA hackathon kit.

Two silent catastrophes are gated hard, always:
  1. Patient data in the repo tree (governance breach; repo must go public).
  2. Secrets in the repo tree.
Substance gaps ([[FILL markers in public-facing docs) are warnings normally,
failures with --strict (use before flipping the repo public / submitting).

    python3 scripts/selfcheck.py [--strict]
"""
import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "README.md",
    "DATA-GOVERNANCE.md",
    "eval/evaluation.py",
    "eval/local_scorer.py",
    "command-centre/SUBMISSION-LEDGER.md",
]

PUBLIC_DOCS = ["README.md", "track1/report", "track2/report"]

# Genomic / sequencing data must never be in the tree, whatever the extension case.
DATA_SUFFIX_RE = re.compile(
    r"\.(vcf|vcf\.gz|vcf\.bgz|fastq|fastq\.gz|fq|fq\.gz|bam|cram|crai|bai|gvcf|gvcf\.gz)$",
    re.IGNORECASE,
)
MAX_FILE_MB = 25  # nothing in a no-data repo should be near this

SECRET_PATTERNS = [
    (re.compile(r"AKIA[0-9A-Z]{16}"), "AWS access key"),
    (re.compile(r"\bsk-[A-Za-z0-9_-]{20,}"), "API secret key (sk-...)"),
    (re.compile(r"ghp_[A-Za-z0-9]{36}"), "GitHub token"),
    (re.compile(r"hf_[A-Za-z0-9]{30,}"), "Hugging Face token"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "private key block"),
]

SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__"}


def iter_files():
    for path in REPO_ROOT.rglob("*"):
        if path.is_file() and not any(part in SKIP_DIRS for part in path.parts):
            yield path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    failures, warnings = [], []

    def substance(msg):
        (failures if args.strict else warnings).append(msg)

    for rel in REQUIRED_FILES:
        if not (REPO_ROOT / rel).exists():
            failures.append(f"missing required file: {rel}")

    for path in iter_files():
        rel = path.relative_to(REPO_ROOT)
        if DATA_SUFFIX_RE.search(path.name):
            failures.append(f"GENOMIC DATA FILE in repo tree: {rel} (belongs in ~/mva-data/)")
        elif path.stat().st_size > MAX_FILE_MB * 1024 * 1024:
            failures.append(f"oversized file ({path.stat().st_size // (1024*1024)} MB): {rel}")
        else:
            try:
                text = path.read_text(errors="ignore")
            except OSError:
                continue
            for pattern, label in SECRET_PATTERNS:
                if pattern.search(text):
                    failures.append(f"possible secret ({label}) in {rel}")

    for entry in PUBLIC_DOCS:
        base = REPO_ROOT / entry
        docs = [base] if base.is_file() else list(base.glob("*.md")) if base.is_dir() else []
        for doc in docs:
            count = doc.read_text().count("[[FILL")
            if count:
                substance(f"{doc.relative_to(REPO_ROOT)}: {count} unfilled [[FILL marker(s)")

    for msg in warnings:
        print(f"WARN  {msg}")
    for msg in failures:
        print(f"FAIL  {msg}")
    mode = "strict" if args.strict else "normal"
    print(f"\nselfcheck ({mode}): {len(failures)} failure(s), {len(warnings)} warning(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
