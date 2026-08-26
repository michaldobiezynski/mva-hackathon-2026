# Status - MVA Hackathon 2026

**Phase: setup.** Submissions close 24/10/2026 23:59 UTC. Data deletion deadline 23/11/2026.

## Headline finding (26/08, first triage pass)

**BUB1B compound-het candidate identified.** Het `15:40209701 T>G` = stop-gain p.Leu737*, ClinVar Pathogenic/Likely pathogenic, gnomAD 3.3e-5, rs759242053 (46x, GQ99, PASS) + het `15:40220612 T>G` = novel missense p.Asn1002Lys, absent from gnomAD (28x, GQ99, PASS). Fallback second allele: het `15:40216470 A>G` (novel, unresolved consequence). Phenotype fit: rhabdomyosarcoma marks the BUB1B (MVA1) subtype specifically. Draft ranking in `track1/predictions/michaldobiezynski_bub1b-region-triage-draft.csv` scores 100/100 against the primary hypothesis offline. Evidence trail: `~/mva-data/derived/` (phenotype text, HPO terms, region variants, annotations).

**Gotcha for submission**: the challenge VCF is GRCh38 with NON-chr contig names (`15`, not `chr15`); predictions must convert to chr-prefixed.

## Verification complete (26/08 afternoon)

1. **ClinVar direct**: VCV 533901 = `NM_001211.6(BUB1B):c.2210T>G (p.Leu737Ter)`, Pathogenic/Likely pathogenic, criteria provided multiple submitters no conflicts, condition **Mosaic variegated aneuploidy syndrome 1**. Confirmed.
2. **VEP independent check**: 40220612 T>G = missense N1002K on ENST00000287598, MODERATE. Confirmed. 40216470 A>G = plain intronic (MODIFIER) - demoted to speculative fallback.
3. **Genome-wide ClinVar P/LP sweep** (full VCF x 346k-entry P/LP catalogue): only 7 hits, all het; BUB1B is the sole phenotype-relevant one; no competing biallelic pattern. Secondary findings added to draft: LZTR1 het P/LP (Noonan 2/10, schwannomatosis), PRSS1 het P/LP (hereditary pancreatitis). Sweep limits: exact-match on ClinVar-known SNV/indels; novel damaging variants outside the 4 MVA genes and structural variants not assessed.
4. **Phasing**: trans configuration not provable from single-sample short reads (~11 kb apart), no parental data; stated as an assumption in the report. Parental recurrent miscarriages are consistent with two carrier parents.

Draft CSV (7 rows incl. 2 secondary) scores 100/100 offline against the primary hypothesis.

## Next actions

1. Write the methods report (`track1/report/`), then ledger entry, then **first real submission** - it validates mechanics with hours of headroom, and the budget allows 5 more.
2. Longer-horizon rigour (before final submission): local snpEff/VEP pass for novel damaging variants genome-wide; SpliceAI on the intronic fallbacks.

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
