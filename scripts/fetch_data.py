#!/usr/bin/env python3
"""Download gated dataset files into ~/mva-data/ (NEVER into this repo).

Requires granted access to SageBio/mva-hackathon-2026-data and a logged-in
HF token (hf auth login). Start with --list; download VCF + phenotype files
before any FASTQ (the full set is ~85 GB).

    python3 scripts/fetch_data.py --list
    python3 scripts/fetch_data.py <filename> [<filename> ...]
"""
import argparse
import sys
from pathlib import Path

REPO_ID = "SageBio/mva-hackathon-2026-data"
DATA_DIR = Path.home() / "mva-data"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("filenames", nargs="*", help="repo filenames to download")
    parser.add_argument("--list", action="store_true", help="list files and sizes, download nothing")
    args = parser.parse_args()

    from huggingface_hub import HfApi, hf_hub_download

    if args.list or not args.filenames:
        api = HfApi()
        info = api.dataset_info(REPO_ID, files_metadata=True)
        total = 0
        for f in sorted(info.siblings, key=lambda s: s.rfilename):
            size = f.size or 0
            total += size
            print(f"{size / 1e9:9.2f} GB  {f.rfilename}")
        print(f"\n{total / 1e9:.1f} GB total. Download with: python3 scripts/fetch_data.py <filename>")
        return 0

    DATA_DIR.mkdir(exist_ok=True)
    for name in args.filenames:
        path = hf_hub_download(
            repo_id=REPO_ID, filename=name, repo_type="dataset", local_dir=DATA_DIR
        )
        print(f"Downloaded: {path}")
    print(f"\nReminder: {DATA_DIR} is outside the repo on purpose. Log the environment in DATA-GOVERNANCE.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
