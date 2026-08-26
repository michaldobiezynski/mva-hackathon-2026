# Data governance

This hackathon uses real genomic and clinical data from a living child, shared by their family under WCG IRB protocol #20252010. The obligations below are from the Official Rules and are not optional.

## Storage

- All dataset files (~85 GB: FASTQ, VCF/BAM/CRAM, HPO phenotype terms) live in **`~/mva-data/`, outside this repository**, and are never committed, even temporarily. `.gitignore` and `scripts/selfcheck.py` both enforce this, but the primary control is habit: nothing from `~/mva-data/` gets copied into the repo tree.
- Derived files that embed individual-level data (filtered VCFs, per-variant tables carrying the child's genotypes) count as data and also stay in `~/mva-data/`. Committed outputs may reference only the small number of candidate variants being proposed, which become public in the submission anyway.
- No cloud copies unless needed; if any are made, list them below so deletion is complete.

| Environment holding data | Created | Deleted |
| --- | --- | --- |
| ~/mva-data/ (local) | | |

## Hard rules

- **No resharing** of the data through any channel, to anyone.
- **No recontact**: never attempt to contact the data subject, their family, or MVA Society contacts.
- **No re-identification**: public outputs must not include information that could re-identify the child or family beyond what the family has already made public themselves.
- Suspected unauthorised disclosure must be reported to Sage Bionetworks' Privacy and Compliance Office via Sage's Help Center.

## Deletion protocol (deadline-critical)

Hackathon closes 24/10/2026. **All data must be deleted from every environment within 30 days of close, i.e. by 23/11/2026**, including local machines, cloud instances, notebooks, private repos and any intermediate or derived datasets. Then email **RarediseaserealkidMVAhackathon2026@synapse.org** to confirm deletion; the organisers chase non-responders.

- [ ] Delete `~/mva-data/` (and any environments listed in the table above)
- [ ] Search for stray copies (`mdfind`, Downloads, scratch dirs, Trash)
- [ ] Send confirmation email
- [ ] Record the date here: deleted on ____

## Publication and embargo

- Embargo runs from hackathon close until the organisers post their summary report or preprint: no peer-reviewed manuscript submissions using the dataset during it.
- Code, models and derived outputs may be shared publicly at any time; conference abstracts/posters need prior written approval.
- Any publication or public communication must include the required acknowledgement (in README.md) and cite the dataset per the Synapse page.
- Submissions are CC BY 4.0 and may be rerun by the organisers; my name is shared in the open-access attribution.
