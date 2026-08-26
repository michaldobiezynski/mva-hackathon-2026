#!/usr/bin/env python3
"""Query Open Targets for the druggability of a gene, to establish whether
direct pharmacological targeting exists before proposing indirect strategies.

An empty result is informative: it is the evidence that a candidate list has to
be built from abundance, stability or lesion-class rescue rather than from
direct inhibition.

    python3 eval/target_druggability.py ENSG00000156970    # BUB1B
"""
import argparse
import json
import sys
import urllib.request

API = "https://api.platform.opentargets.org/api/v4/graphql"

QUERY = """
{
  target(ensemblId: "%s") {
    approvedSymbol
    drugAndClinicalCandidates {
      count
      rows {
        maxClinicalStage
        drug { name drugType mechanismsOfAction { rows { mechanismOfAction actionType } } }
      }
    }
    tractability { label modality value }
    chemicalProbes { id isHighQuality mechanismOfAction }
  }
}
"""


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("ensembl_id", help="Ensembl gene id, e.g. ENSG00000156970")
    p.add_argument("--json-out", help="write the raw response to this path")
    args = p.parse_args()

    req = urllib.request.Request(
        API,
        data=json.dumps({"query": QUERY % args.ensembl_id}).encode(),
        headers={"Content-Type": "application/json"},
    )
    payload = json.load(urllib.request.urlopen(req, timeout=60))
    if "errors" in payload:
        print(json.dumps(payload["errors"], indent=2), file=sys.stderr)
        return 1
    if args.json_out:
        with open(args.json_out, "w") as f:
            json.dump(payload, f, indent=2)

    target = payload["data"]["target"]
    candidates = target.get("drugAndClinicalCandidates") or {}
    print(f"{target['approvedSymbol']}: {candidates.get('count', 0)} drug/clinical candidate(s)")
    for row in candidates.get("rows") or []:
        moa = [m["mechanismOfAction"] for m in ((row["drug"].get("mechanismsOfAction") or {}).get("rows") or [])]
        print(f"  - {row['drug']['name']} ({row['drug']['drugType']}), "
              f"max stage {row['maxClinicalStage']}: {'; '.join(moa[:2])}")

    tractable = [(t["modality"], t["label"]) for t in target.get("tractability") or [] if t["value"]]
    print(f"tractability buckets met: {tractable or 'none'}")

    probes = target.get("chemicalProbes") or []
    print(f"chemical probes: {len(probes)} "
          f"({sum(1 for x in probes if x.get('isHighQuality'))} high quality)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
