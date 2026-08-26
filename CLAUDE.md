# MVA Hackathon 2026 - working rules for this repo

Challenge: Rare Disease, Real Kid: MVA Hackathon 2026 (Sage Bionetworks / MVA Society / HF / BEACON). Submissions close **24/10/2026 23:59 UTC**. Command centre: `command-centre/`. Live state: `STATUS.md`.

Non-negotiables, in priority order:

1. **Patient data never enters this repo.** Dataset files and anything embedding the child's individual-level genotypes live in `~/mva-data/` only. Read `DATA-GOVERNANCE.md` before touching data. Data deletion deadline after close: 23/11/2026, with confirmation email.
2. **Submission budget is tiny: 6 for Track 1 (best score counts), 1 for Track 2 (no redo).** Never submit anything through the Space without (a) running `python3 eval/local_scorer.py` on the CSV, (b) recording the plan and outcome in `command-centre/SUBMISSION-LEDGER.md`. Track 2 is single-shot: it goes out only after an adversarial review pass, near the deadline.
3. `eval/evaluation.py` is vendored verbatim from the challenge Space (CC BY 4.0, attributed); never edit it, wrap it from `local_scorer.py` instead. Scoring mechanics and their traps are documented in `command-centre/STRATEGY.md` - read it before designing any submission CSV.
4. This repo must be **public at submission time** (a public GitHub link is a required deliverable in both tracks). Keep the history clean enough to flip visibility without scrubbing: `python3 scripts/selfcheck.py` gates data files and secrets.
5. Predictions use GRCh38 coordinates; compound-het pairs go in ONE row (see STRATEGY.md for why splitting them halves the score).
6. Update `STATUS.md` before ending a session. British English throughout.
