# Status - MVA Hackathon 2026

**Phase: setup.** Submissions close 24/10/2026 23:59 UTC. Data deletion deadline 23/11/2026.

## Next actions

1. Request dataset access: log in to Hugging Face, complete the gated-access form at https://huggingface.co/datasets/SageBio/mva-hackathon-2026-data (user action; attestation to rules required).
2. Once granted: download working set to `~/mva-data/` (start with VCFs + HPO terms; FASTQ only if re-calling proves necessary).
3. Literature pass on Mosaic Variegated Aneuploidy genetics (known genes, inheritance patterns) before touching the data.
4. First-pass Track 1 pipeline per `command-centre/STRATEGY.md`.

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
