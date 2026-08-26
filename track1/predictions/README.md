# Predictions

Official format: `template.csv` (from the challenge Space). GRCh38 coordinates, max 10 rows, EPCR in (0, 1], compound-het pairs in ONE row (see `command-centre/STRATEGY.md`).

Naming: `michaldobiezynski_<approach>.csv` (username in filename is requested by the organisers).

Before any of these is uploaded: `python3 eval/local_scorer.py <csv> --truth eval/hypotheses/` and a ledger entry in `command-centre/SUBMISSION-LEDGER.md`.
