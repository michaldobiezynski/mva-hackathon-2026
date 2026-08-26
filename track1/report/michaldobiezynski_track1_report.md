# Track 1 methods report - phenotype-anchored triage with adversarial verification

Participant: `michaldobiezynski`. Accompanies predictions file `michaldobiezynski_bub1b-triage-v1.csv` (submission 1 of 6). Code: https://github.com/michaldobiezynski/mva-hackathon-2026 (private during the live leaderboard phase to avoid leaking candidates; will be public by challenge close).

## Approach overview

Phenotype-first: the HPO cluster (rhabdomyosarcoma, nephrocalcinosis, IUGR/SGA, short stature, failure to thrive, parental recurrent miscarriages) is a coherent chromosomal-instability signature, so the first pass tested the four established MVA genes before any genome-wide work. Every candidate annotation was then independently verified against a second source, and a genome-wide ClinVar sweep checked that no competing pathogenic pattern exists outside the prior genes. The ranked list was score-tested offline against explicit ground-truth hypotheses using the challenge's own published evaluator before this submission was made.

## Data processing

- Input: provided GATK 4.2.4 germline VCF (`WGS_EX2312012_HGWCNDSX7.vcf.gz`), single sample, GRCh38. Note: the VCF uses non-`chr` contig names (reference FASTA `GCA_000001405.15_GRCh38_no_alt..._no_chr`); coordinates were converted to `chr`-prefixed GRCh38 for submission. FASTQs were not used (no re-calling).
- Phenotype: all eight HPO terms extracted from the provided clinical document.
- Gene regions (GRCh38, via MyGene.info, ±5 kb): BUB1B, CEP57, TRIP13, CENATAC. All PASS variants in these regions extracted: 47 variants.
- Annotation: MyVariant.info batch (gnomAD AF, ClinVar, snpEff) with `assembly=hg38` (the API defaults to hg19 and silently mis-keys GRCh38 queries; the corrected run resolved 46/47 variants).

## Candidate identification and ranking

Filtering to rare (gnomAD AF < 0.01 or absent) heterozygous/homozygous calls left a single compelling gene: **BUB1B**, which is also the MVA subtype specifically associated with malignancy (rhabdomyosarcoma reported), matching this proband's presentation.

EPCR values encode relative confidence in the compound-het pairings of the same anchor allele, not calibrated probabilities: 0.60 for the missense pairing (both alleles protein-altering, one ClinVar-established), then 0.15/0.08 for intronic pairings, 0.06 for the anchor alone, and ≤0.03 for secondary rows.

## Evidence per candidate

| Rank | Variant(s), GRCh38 | Gene | Key evidence |
| --- | --- | --- | --- |
| 1 | chr15:40209701 T>G + chr15:40220612 T>G | BUB1B | Anchor: het stop-gain p.Leu737Ter, ClinVar VCV000533901 Pathogenic/Likely pathogenic for *Mosaic variegated aneuploidy syndrome 1* (multiple submitters, no conflicts), gnomAD 3.3e-5, 46x GQ99. Partner: het novel missense p.Asn1002Lys (ENST00000287598), absent from gnomAD, VEP-confirmed MODERATE, 28x GQ99. Classic MVA1 architecture: truncating + missense. |
| 2 | chr15:40209701 T>G + chr15:40216470 A>G | BUB1B | Same anchor; partner is a novel het intronic variant (VEP: intron, MODIFIER), 46x GQ99. Speculative splice/regulatory second allele; retained because deep-intronic second alleles are documented in recessive disease. |
| 3 | chr15:40209701 T>G + chr15:40192892 C>T | BUB1B | Same anchor; partner rare intronic rs185599777 (AF 0.002). Weakest pairing. |
| 4 | chr15:40209701 T>G | BUB1B | Anchor alone, covering the case where the second allele is a structural or otherwise uncalled variant invisible to this short-read SNV/indel VCF. |
| 5 | chr5:893132 G>C + chr5:902436 A>G | TRIP13 | Secondary: two rare TRIP13 hets (AF 0.0013/0.0084); MVA3 is also cancer-predisposing, but phenotype fit and variant impact are far weaker. |
| 6-7 | chr22:20996720 C>G; chr7:142750561 C>T | LZTR1; PRSS1 | Secondary/incidental: het ClinVar P/LP in dominant-condition genes (Noonan 2/10 and LZTR1-related schwannomatosis; hereditary/recurrent pancreatitis), surfaced by the genome-wide sweep. Unrelated to the primary phenotype; flagged for clinical review. |

## Verification performed

1. ClinVar queried directly (E-utilities) for the anchor: VCV000533901, condition MVA1, P/LP with no conflicts.
2. Ensembl VEP queried independently of the primary annotator for both partner candidates; annotations agreed (missense N1002K confirmed; the intronic fallback demoted accordingly).
3. Genome-wide sweep: proband VCF intersected with the full ClinVar P/LP catalogue (346,282 entries): 7 hits genome-wide, all heterozygous; BUB1B is the only phenotype-concordant hit and the only gene with a plausible biallelic configuration among rare variants. No competing explanation found.
4. Offline scoring: the published evaluator (`evaluation.py` from the challenge Space, vendored with attribution) was run against explicit hypothesis files; this CSV scores 100/100 rank points and F-max 1.0 if hypothesis 1 is the validated answer.

## Additional analysis: direct mosaicism assessment (honest negative)

Because the condition is defined by *mosaic* aneuploidy, I tested whether the supplied bulk WGS could quantify it directly, using per-chromosome median read depth and the dispersion of heterozygous allele balance across PASS biallelic SNVs (output: `mosaicism_scan.tsv`; code in the repository).

Median depth is flat at 44x across chr1-18 (ratios 1.00) with chrX at 0.50, consistent with a male proband and with **no dominant clonal aneuploidy** in this blood-derived sample. Chromosomes 20-22 show modestly wider allele-balance dispersion (sd ~0.13 vs ~0.09 elsewhere) and 4.5-7% higher depth; however, the male chrX "heterozygous" calls, which are necessarily artefactual, carry the same signature, so short-chromosome GC/mapping bias is a more parsimonious explanation than genuine mosaicism.

This is the expected outcome rather than a disappointment: bulk sequencing averages across cells, and variegated aneuploidy is by definition non-clonal, so it largely cancels. Quantifying this child's mosaic fraction, the natural biomarker for disease burden and for any future intervention, requires single-cell sequencing or conventional cytogenetics on cultured cells. I report this as an evidence gap, not as a finding.

## Limitations

- **Phasing**: the trans configuration of the rank-1 pair is inferred, not proven (single sample, variants ~11 kb apart, no parental genotypes). The parental recurrent-miscarriage history is consistent with two carrier parents.
- The genome-wide sweep matches ClinVar-known SNV/indels exactly; novel damaging variants outside the four MVA genes and structural variants were not assessed in this iteration.
- No FASTQ-level analysis (no re-calling, no SV calling) in this pass.

## Reproducibility

Region extraction, annotation, verification and offline scoring are single-command Python/awk steps over the provided VCF, documented in the repository (`STATUS.md`, `eval/`, `scripts/`); versions: GATK VCF as provided, MyVariant.info and Ensembl VEP REST queried 26/08/2026, ClinVar VCF snapshot 26/08/2026.

---

This work was made possible through the Hackathon, organized by Sage Bionetworks in partnership with the MVA Society, Hugging Face, and BEACON (The Benchmarking, Evaluation, and Assessment Consortium for Science), with prize sponsorship from AWS and Anthropic. We are deeply grateful to the child and their family who generously contributed their data and their story to advance research into this rare disease. We acknowledge their trust in making this Hackathon possible.
