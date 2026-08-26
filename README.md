# MVA Hackathon 2026 - genotype-informed variant prediction and drug repurposing

Entry for [Rare Disease, Real Kid: MVA Hackathon 2026](https://sagebio-rare-disease-real-kid-mva-hackathon-2026.hf.space/), organised by Sage Bionetworks, the MVA Society, Hugging Face and BEACON, with prize sponsorship from AWS and Anthropic.

The challenge: identify the causal variant(s) behind a real child's Mosaic Variegated Aneuploidy (Track 1) and propose repurposed, market-approved medications targeting the disrupted mechanism (Track 2).

**This repository contains no patient data.** The dataset is gated and non-redistributable; see [DATA-GOVERNANCE.md](DATA-GOVERNANCE.md). Only the small number of candidate variants named in the submission (which the submission itself makes public) and chromosome-level aggregate statistics appear here. Everything in this repository is released under CC BY 4.0 per the hackathon rules.

## Track 1 - Variant Prediction

**Result: 100.0/100 rank points, F-max 1.000, full match at rank 1** (submission 1 of 6, 26/08/2026).

A phenotype-first triage: the HPO cluster (rhabdomyosarcoma, nephrocalcinosis, IUGR, short stature, failure to thrive, parental recurrent miscarriages) is a chromosomal-instability signature, so the four established MVA genes were tested before any genome-wide work. The answer is a compound-heterozygous *BUB1B* genotype: a ClinVar-established stop-gain p.Leu737Ter paired with a novel missense p.Asn1002Lys.

Every annotation was verified against a second independent source, and a genome-wide sweep against the full ClinVar pathogenic catalogue confirmed no competing explanation exists.

- Predictions: [`track1/predictions/`](track1/predictions/) (official format, GRCh38)
- Methods report: [`track1/report/`](track1/report/)

## Track 2 - Drug Repurposing

Mechanism-grounded, genotype-filtered repurposing hypotheses. The central argument: p.Leu737Ter is functionally null, but p.Asn1002Lys yields full-length protein, so abundance-raising interventions have a substrate to act on in this child specifically. The primary candidate family is NAD+ repletion acting through the SIRT2/BubR1-Lys668 stabilisation axis, the one published intervention that raises this exact protein in this exact insufficiency model. Senolytics are proposed as a secondary, downstream option, and checkpoint-weakening oncology agents are explicitly ruled out.

All candidates are framed as hypotheses for follow-up, never as evidence that any medicine works.

- Report: [`track2/report/`](track2/report/)
- Working notes and literature verification: [`track2/notes/`](track2/notes/)

## Reproducibility

The whole analysis runs on a laptop from the supplied VCF plus the HPO terms, using public resources only (ClinVar, gnomAD, Ensembl VEP, UniProt, MyVariant.info). A reader with their own granted dataset access can reproduce it end to end.

Offline validation and what-if scoring of a predictions CSV, using the challenge's own evaluator (vendored with attribution, never edited):

```sh
python3 eval/local_scorer.py track1/predictions/<file>.csv --truth eval/hypotheses/
```

Repository hygiene gate (refuses genomic data files and secrets anywhere in the tree):

```sh
python3 scripts/selfcheck.py
```

Working state, decisions and the submission ledger are in [`STATUS.md`](STATUS.md) and [`command-centre/`](command-centre/).

## Acknowledgement

This work was made possible through the Hackathon, organized by Sage Bionetworks in partnership with the MVA Society, Hugging Face, and BEACON (The Benchmarking, Evaluation, and Assessment Consortium for Science), with prize sponsorship from AWS and Anthropic. We are deeply grateful to the child and their family who generously contributed their data and their story to advance research into this rare disease. We acknowledge their trust in making this Hackathon possible.
