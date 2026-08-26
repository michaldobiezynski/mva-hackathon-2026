# Checklists

## Getting started

- [ ] Log in to Hugging Face; complete the gated-access form on the dataset page (attests to the rules; approval is auto-gated).
- [ ] Read the Official Rules tab once in full (source mirrored in the Space repo `tabs/rules.py`).
- [ ] Create `~/mva-data/` and download the working set there (`python3 scripts/fetch_data.py --list` first; VCF + HPO before FASTQ).
- [ ] Literature pass: current MVA gene list (OMIM/PubMed), inheritance, known variant classes.
- [ ] Record data environments in DATA-GOVERNANCE.md's table as they are created.

## Before EVERY Track 1 submission (6 slots, guard them)

- [ ] CSV passes `python3 eval/local_scorer.py <csv>` (format-clean, ranks as intended).
- [ ] Scored against all current hypotheses: `--truth eval/hypotheses/`.
- [ ] Compound-het candidates are pair rows, not split singles.
- [ ] All 10 rows used; ordering deliberate; EPCR values in (0, 1].
- [ ] Filename: `michaldobiezynski_<approach>.csv`.
- [ ] Methods report (PDF/MD, filename `michaldobiezynski_track1_report.*`) updated to match this CSV.
- [ ] GitHub repo public and current (required field on the form).
- [ ] Ledger entry written BEFORE uploading (plan, what this probe should learn); outcome recorded after.

## Before THE Track 2 submission (one shot)

- [ ] Report maps to the rubric: mechanism (35), impact (25), innovation (25), scalability (15).
- [ ] Candidates framed as hypotheses for follow-up; no treatment claims.
- [ ] Fresh-context adversarial review completed; findings triaged and actioned.
- [ ] 3-minute video recorded, uploaded (YouTube/Vimeo), link checked from a logged-out browser.
- [ ] GitHub repo public, reproducible, no data.
- [ ] Not submitted before [[FILL: chosen freeze date, e.g. 20/10]] unless the report has been stable for a week.

## Repo hygiene (before flipping public, and periodically)

- [ ] `python3 scripts/selfcheck.py` passes (no data files, no secrets, no unfilled markers in public-facing docs).
- [ ] `git log` history contains no data files ever committed.
- [ ] Acknowledgement text present in README.

## Close-out (after 24/10)

- [ ] Data deletion by **23/11/2026** + confirmation email (checklist in DATA-GOVERNANCE.md).
- [ ] Embargo respected for any writing-up plans.
