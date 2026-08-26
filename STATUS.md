# Status - MVA Hackathon 2026

**Phase: setup.** Submissions close 24/10/2026 23:59 UTC. Data deletion deadline 23/11/2026.

## Next actions

1. Read `~/mva-data/Challenge_Clinical_Phenotype_1.docx` (the HPO phenotype description) and extract the term list.
2. Literature pass on Mosaic Variegated Aneuploidy genetics (known genes, inheritance patterns) before touching the VCF.
3. VCF sanity pass: reference build check (GRCh38 expected), variant count, sample fields, then first-pass Track 1 pipeline per `command-centre/STRATEGY.md`.

Dataset access: **ACCEPTED** (confirmed 26/08 in HF settings/gated-repos; account already held access, no new form needed). **Full corpus downloaded** to `~/mva-data/` on 26/08 (~79 GiB: 8 WGS FASTQ lane pairs + `WGS_EX2312012_HGWCNDSX7.vcf.gz` + .tbi + phenotype docx + README; verified against the repo tree, download exit 0). The FASTQs are the deletion-obligation bulk; the analysis starts from the VCF.

## Submission budget

Track 1: **6/6 remaining**. Track 2: **1/1 remaining**. Ledger: `command-centre/SUBMISSION-LEDGER.md`.

## Decisions log

| Date | Decision | Why |
| --- | --- | --- |
| 26/08 | Kit scaffolded; challenge Space source read in full (about/rules/faq/tracks/evaluation) | Gradio app is JS-rendered; the Space repo is the readable source of truth |
| 26/08 | Vendored the Space's `evaluation.py` for offline scoring | Protects the 6-submission budget; CC BY 4.0 permits it with attribution |

## Session log

| Date | What happened |
| --- | --- |
| 26/08 | Kit scaffolded from challenge source; local scorer verified against the official template CSV |
| 26/08 | Dataset access confirmed ACCEPTED; VCF working set downloaded to ~/mva-data/ (logged in DATA-GOVERNANCE.md) |
