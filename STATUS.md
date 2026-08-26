# Status - MVA Hackathon 2026

**Phase: setup.** Submissions close 24/10/2026 23:59 UTC. Data deletion deadline 23/11/2026.

## Headline finding (26/08, first triage pass)

**BUB1B compound-het candidate identified.** Het `15:40209701 T>G` = stop-gain p.Leu737*, ClinVar Pathogenic/Likely pathogenic, gnomAD 3.3e-5, rs759242053 (46x, GQ99, PASS) + het `15:40220612 T>G` = novel missense p.Asn1002Lys, absent from gnomAD (28x, GQ99, PASS). Fallback second allele: het `15:40216470 A>G` (novel, unresolved consequence). Phenotype fit: rhabdomyosarcoma marks the BUB1B (MVA1) subtype specifically. Draft ranking in `track1/predictions/michaldobiezynski_bub1b-region-triage-draft.csv` scores 100/100 against the primary hypothesis offline. Evidence trail: `~/mva-data/derived/` (phenotype text, HPO terms, region variants, annotations).

**Gotcha for submission**: the challenge VCF is GRCh38 with NON-chr contig names (`15`, not `chr15`); predictions must convert to chr-prefixed.

## Next actions (verification before any submission - 6-slot budget untouched)

1. Verify p.Leu737* directly on ClinVar and p.Asn1002Lys consequence via VEP (Ensembl REST was down 26/08; MyVariant.info used, must cross-check).
2. Genome-wide unbiased sweep (rare + damaging + biallelic patterns beyond the 4 known genes) so the ranking isn't gene-prior circular.
3. Phase caveat: trans configuration unproven (single sample, ~11 kb apart); note in report, consider FASTQ-level read-backed phasing as a long shot.
4. Then: finalise EPCR ranking, ledger entry, first real submission (also validates mechanics).

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
