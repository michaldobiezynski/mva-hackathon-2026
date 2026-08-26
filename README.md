# MVA Hackathon 2026 - [[FILL: approach name]]

Entry for [Rare Disease, Real Kid: MVA Hackathon 2026](https://sagebio-rare-disease-real-kid-mva-hackathon-2026.hf.space/), organised by Sage Bionetworks, the MVA Society, Hugging Face and BEACON, with prize sponsorship from AWS and Anthropic.

The challenge: identify the causal variant(s) behind a real child's Mosaic Variegated Aneuploidy (Track 1) and propose repurposed, market-approved medications targeting the disrupted mechanism (Track 2).

**This repository contains no patient data.** The dataset is gated and non-redistributable; see [DATA-GOVERNANCE.md](DATA-GOVERNANCE.md). Everything here (code, predictions, reports) is released under CC BY 4.0 per the hackathon rules.

## Track 1 - Variant Prediction

[[FILL: approach summary - pipeline, tools, ranking rationale]]

- Predictions: `track1/predictions/` (ranked CSVs in the official format, GRCh38)
- Methods report: `track1/report/`

## Track 2 - Drug Repurposing

[[FILL: mechanism characterisation and repurposing rationale summary]]

- Report: `track2/report/`
- Pitch video: [[FILL: YouTube/Vimeo link]]

## Reproducibility

[[FILL: exact commands to regenerate the predictions from the gated dataset, for a reader who has been granted their own data access]]

Offline scoring/validation of a predictions CSV (uses the challenge's own vendored evaluator):

```sh
python3 eval/local_scorer.py track1/predictions/<file>.csv --truth eval/hypotheses/
```

## Acknowledgement

This work was made possible through the Hackathon, organized by Sage Bionetworks in partnership with the MVA Society, Hugging Face, and BEACON (The Benchmarking, Evaluation, and Assessment Consortium for Science), with prize sponsorship from AWS and Anthropic. We are deeply grateful to the child and their family who generously contributed their data and their story to advance research into this rare disease. We acknowledge their trust in making this Hackathon possible.
