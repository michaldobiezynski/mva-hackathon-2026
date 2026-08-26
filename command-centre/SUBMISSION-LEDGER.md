# Submission ledger

The budget IS the strategy: 6 Track 1 slots (best counts, instant feedback = oracle queries) and 1 Track 2 slot (no redo). Write the plan BEFORE uploading; record the outcome after. Never upload unplanned.

## Track 1 (6 slots)

| # | Date | CSV | Plan / what this probe should learn | Rank points | F-max | Match feedback | Lesson |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 26/08 | michaldobiezynski_bub1b-triage-v1.csv | Best current hypothesis (BUB1B stop+missense pair rank 1) + fallbacks + secondaries. Branch outcomes: 100 = primary confirmed, done; 50 + "full at rank 2/3" = which fallback pairing is right; 50 + "partial at rank 1" = anchor right, second allele not yet found (hunt SV/deep intronic); 0 = answer outside BUB1B rows entirely, rethink. Also validates submission mechanics. | **100.0** | **1.000** | ✅ Full match at rank 1 (threshold 0.6) | Primary hypothesis IS the validated answer: BUB1B p.Leu737Ter + p.Asn1002Lys. Automated score maxed on slot 1; slots 2-6 not needed for score. Leaderboard shows 10+ participants already at 100/1.000 (many BUB1B filenames): differentiation = qualitative methods review + Track 2. |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |
| 5 | | | | | | | |
| 6 | | | | | | | |

Guideline: slot 1 after the first credible pipeline pass (it also validates mechanics end to end); keep at least 2 slots for the final two weeks.

## Track 2 (1 slot)

| Date | Report | Video | Adversarial review done? | Outcome |
| --- | --- | --- | --- | --- |
| | | | | |
