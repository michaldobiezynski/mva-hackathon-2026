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

## Variant interpretation evidence

The two candidate alleles were characterised beyond the annotation used for ranking. This evidence post-dates the ranked submission and does not change it; it is included because Track 1 is also assessed qualitatively.

**Allele A, `chr15:40209701 T>G`, p.Leu737Ter.** ClinVar VCV000533901, Pathogenic/Likely pathogenic for *Mosaic variegated aneuploidy syndrome 1*, multiple submitters with no conflicts; gnomAD 3.3e-5; AD 21,25 at DP 46, GQ 99. The premature stop lies 748 nt upstream of the final exon-exon junction of a 3,153-nt CDS, so nonsense-mediated decay is predicted. The stop codon's identity is determined by the substitution itself: of the six leucine codons, only TTA yields a stop under a position-2 T>G, so the premature codon is **TGA** (`eval/stop_codon_identity.py`).

**Allele B, `chr15:40220612 T>G`, p.Asn1002Lys.** Absent from gnomAD; AD 15,13 at DP 28, GQ 99. Several computational lines agree it is damaging and probably destabilising. They are not fully independent (the burial analysis and the ΔΔG derive from the same AlphaFold model), and none of them measures protein abundance:

| Evidence | Result |
| --- | --- |
| Sequence predictors (dbNSFP) | AlphaMissense **pathogenic (0.92)**; ESM1b deleterious; SIFT 0.00; PolyPhen-2 HDIV 1.00; ClinPred 0.99; VEST4 0.89; CADD 24.5. Dissenting: MetaSVM, PrimateAI, BayesDel, REVEL 0.47 |
| Conservation | phyloP 100-way 4.87; GERP++ RS 4.84 |
| Structure (AlphaFold AF-O60566-F1) | Buried, 76th percentile by neighbour count, in a confidently modelled region (pLDDT 91.1); all 136 neighbours intra-domain |
| Thermodynamics (ThermoMPNN ΔΔG) | **+1.51 kcal/mol, destabilising rather than neutral**, 75th percentile of the domain's 5,415 substitutions. Interpret narrowly: 84% of substitutions in this domain are predicted destabilising, and all 19 at this site are, so the scan constrains the site rather than this substitution |

The dissenting predictors are the ensembles that incorporate allele frequency, which is expected behaviour for an ultra-rare variant with no population signal to learn from.

**ACMG criteria**: PM2 (absent from gnomAD), PP3 (computational support), PP4 (phenotype highly specific for the gene). **PM3 is unavailable** because phase is unrecoverable here: the variants are 10,911 bp apart, beyond read-backed phasing, and no parental samples exist. That is what keeps the variant short of a confident Likely Pathogenic call, and trio sequencing would supply it. Formal classification belongs to a clinical laboratory; the criteria are named so the gap is explicit.

Methods and caveats for the structural and ΔΔG work are in `REPRODUCE-DDG.md`.

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
