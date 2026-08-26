# Challenge brief - Rare Disease, Real Kid: MVA Hackathon 2026

Distilled 26/08/2026 from the challenge Space's source code (`SageBio/rare-disease-real-kid-mva-hackathon-2026`, sha d27c339), which is more reliable than the rendered page: the about/rules/faq/submit tabs and the actual scoring code were read in full. Confidence: high unless marked.

## The case

A real child with **Mosaic Variegated Aneuploidy (MVA)**, data shared with full family consent under WCG IRB protocol #20252010. Ground truth for Track 1 is an NHS-validated causal variant answer; the public evaluation code's docstring describes the answer key as **compound-heterozygous** ("a clinically validated compound-heterozygous answer key"), i.e. two variants.

## Key facts

| Fact | Value |
| --- | --- |
| Window | Launched 24/08/2026; submissions close **24/10/2026 23:59 UTC**; judging to ~late Nov; winners 25/11 |
| Format | Online, free, individual or teams (each member registers; Track 1 quota per member, Track 2 one per team) |
| Data | ~85 GB gated HF dataset `SageBio/mva-hackathon-2026-data`: FASTQ + VCF (BAM/CRAM optional), phenotype as HPO terms, single subject; access via gated form; no resharing; **delete within 30 days of close** |
| Compute | Bring your own; only submission files are uploaded |
| Prizes | $50,000 total: 1st $12k cash + $12k Claude credits; 2nd $7k+$7k; 3rd $4k+$4k; Innovation award $2k+$2k (judges' discretion, independent of placement) |
| Licence | Submissions (code, predictions, reports) CC BY 4.0, may be rerun by organisers; name shared in attribution |
| Coordinates | GRCh38 required |

## Track 1 - Variant Prediction (automated, live leaderboard)

- Submit via the Space: ranked CSV (max 10 rows, official template in `track1/predictions/template.csv`), a public GitHub link, and a methods report (PDF/MD, not auto-scored).
- **6 submissions max; best score counts; instant feedback** (rank points, F-max, full/partial/no match and the matching rank are returned on upload).
- Scoring (vendored in `eval/evaluation.py`): rank points (rank 1 = 100, ranks 2-3 = 50, 4-5 = 25, 6-10 = 10; half credit for one of two compound-het variants) + F-max over EPCR thresholds, computed per individual variant.
- Secondary/incidental findings don't hurt the automated score; flagged via `finding_type`, reviewed qualitatively.

## Track 2 - Drug Repurposing (expert panel)

- Submit: report (PDF/MD) characterising the variant mechanism (LoF/GoF, disrupted pathway, downstream consequence) and proposing market-approved repurposing candidates; public GitHub link; **3-minute pitch video** (YouTube/Vimeo); optional notes to judges.
- **One submission ever, no resubmission.**
- Rubric: Scientific Rigor 35%, Potential Impact 25%, Innovation 25%, Scalability 15%. Judged over ~2-3 months by researchers, clinicians and patient advocates. Explicitly hypotheses for follow-up, not treatment claims.

## Governance highlights (full detail: DATA-GOVERNANCE.md)

No recontact of family/MVA Society; no re-identification beyond family's own public posts; deletion + confirmation email by 23/11/2026; publication embargo until organisers' summary report; required acknowledgement text in README.md.

## Links

- Space: https://sagebio-rare-disease-real-kid-mva-hackathon-2026.hf.space/
- Dataset: https://huggingface.co/datasets/SageBio/mva-hackathon-2026-data
- Discussions: https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026/discussions
- Methods template (Excel) and CSV template: in the Space's `static/templates/`
