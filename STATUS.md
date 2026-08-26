# Status - MVA Hackathon 2026

**Phase: Track 1 scored at maximum; Track 2 drafted and reviewed, awaiting submission.** Submissions close 24/10/2026 23:59 UTC. Data deletion deadline 23/11/2026.

## Headline finding (26/08, first triage pass)

**BUB1B compound-het candidate identified.** Het `15:40209701 T>G` = stop-gain p.Leu737*, ClinVar Pathogenic/Likely pathogenic, gnomAD 3.3e-5, rs759242053 (46x, GQ99, PASS) + het `15:40220612 T>G` = novel missense p.Asn1002Lys, absent from gnomAD (28x, GQ99, PASS). Fallback second allele: het `15:40216470 A>G` (novel, unresolved consequence). Phenotype fit: rhabdomyosarcoma marks the BUB1B (MVA1) subtype specifically. Draft ranking in `track1/predictions/michaldobiezynski_bub1b-region-triage-draft.csv` scores 100/100 against the primary hypothesis offline. Evidence trail: `~/mva-data/derived/` (phenotype text, HPO terms, region variants, annotations).

**Gotcha for submission**: the challenge VCF is GRCh38 with NON-chr contig names (`15`, not `chr15`); predictions must convert to chr-prefixed.

## Verification complete (26/08 afternoon)

1. **ClinVar direct**: VCV 533901 = `NM_001211.6(BUB1B):c.2210T>G (p.Leu737Ter)`, Pathogenic/Likely pathogenic, criteria provided multiple submitters no conflicts, condition **Mosaic variegated aneuploidy syndrome 1**. Confirmed.
2. **VEP independent check**: 40220612 T>G = missense N1002K on ENST00000287598, MODERATE. Confirmed. 40216470 A>G = plain intronic (MODIFIER) - demoted to speculative fallback.
3. **Genome-wide ClinVar P/LP sweep** (full VCF x 346k-entry P/LP catalogue): only 7 hits, all het; BUB1B is the sole phenotype-relevant one; no competing biallelic pattern. Secondary findings added to draft: LZTR1 het P/LP (Noonan 2/10, schwannomatosis), PRSS1 het P/LP (hereditary pancreatitis). Sweep limits: exact-match on ClinVar-known SNV/indels; novel damaging variants outside the 4 MVA genes and structural variants not assessed.
4. **Phasing**: trans configuration not provable from single-sample short reads (~11 kb apart), no parental data; stated as an assumption in the report. Parental recurrent miscarriages are consistent with two carrier parents.

Draft CSV (7 rows incl. 2 secondary) scores 100/100 offline against the primary hypothesis.

## TRACK 1 AUTOMATED SCORE MAXED (26/08, submission 1 of 6)

**100.0/100 rank points, F-max 1.000, full match at rank 1.** The validated answer is our primary hypothesis: BUB1B p.Leu737Ter (chr15:40209701 T>G) + p.Asn1002Lys (chr15:40220612 T>G). Ledger updated; slots 2-6 remain but cannot improve the automated score.

**Leaderboard reality (26/08)**: 10+ participants already at 100/1.000, several with bub1b filenames. The automated metric is saturated; ranking among the 100s will come down to the post-close qualitative evaluation of methods/reports, secondary findings quality, and Track 2.

## Track 2 status (26/08) - draft complete, review loop closed

Report at `track2/report/michaldobiezynski_track2_report.md` (~7,000 words). **Not submitted; single shot, submit near the 24/10 deadline.**

Four adversarial review rounds, all findings verified against primary sources before actioning (triage tables in `track2/notes/mechanism-review.md`):
- Judge-panel lens: 58/100 -> 74/100 after round 1 fixes; round 2 caught four defects my own fixes introduced.
- Science lens (clinical geneticist / cancer biologist): found the safety-critical error, three factual errors and two arguments that inverted; round 2 verified the fixes landed and caught one applied in name only plus an overclaim in my own reasoning.
- Reviewer's closing verdict: the report is at the churn point; remaining work is presentational, not substantive.

Content now: allele-resolved candidates (readthrough for the null allele, NAD+/SIRT2 stabilisation for the missense allele, mitochondrial/proteostasis, senolytics, plus a negative recommendation); a systematic Open Targets druggability search establishing that no direct pharmacology exists; AlphaMissense/predictor evidence with ACMG criteria for both residues; the UGA-A context finding; the conditional dosage-ceiling argument; a dose-response gating experiment with a stop rule for the dominant-negative case; and a plain-language family section carrying the safety caveats.

**The safety finding that matters most**: this child's own tumour type (rhabdomyosarcoma) is a published NAMPT dependency where NAD+ depletion causes complete regression in orthotopic models, so the NAD+ candidate proposes the opposite of a curative intervention in their cancer. Stated as a gating question in both the expert and family sections.

Remaining optional work (none of it changes a conclusion): ddG estimate for N1002K; figures (domain schematic, depth/BAF plot); a second worked example, made cheap by `eval/target_druggability.py` running on any Ensembl gene.

## Next actions

Nothing is time-critical before October. In priority order when work resumes:

1. **Resubmit Track 1** with the improved report (now carrying the mosaicism analysis). Safe: only the best score counts and we hold the maximum, so a resubmission cannot lose ground. Uses one of the 5 remaining slots.
2. **Submit Track 2** near the deadline (single shot, no resubmission). Requires: the 3-minute pitch video (`video/SCRIPT.md`) and a final read-through.
3. **Flip the repo PUBLIC** before close - it is a required deliverable for both tracks. Currently private on purpose while the leaderboard is live; `scripts/selfcheck.py --strict` passes clean, so it is presentable whenever wanted.
4. Optional, none of it conclusion-changing: ddG estimate for N1002K; figures; a second worked example for the scalability claim.

Dataset access: **ACCEPTED** (confirmed 26/08 in HF settings/gated-repos; account already held access, no new form needed). **Full corpus downloaded** to `~/mva-data/` on 26/08 (~79 GiB: 8 WGS FASTQ lane pairs + `WGS_EX2312012_HGWCNDSX7.vcf.gz` + .tbi + phenotype docx + README; verified against the repo tree, download exit 0). The FASTQs are the deletion-obligation bulk; the analysis starts from the VCF.

## Submission budget

Track 1: **5/6 remaining** (slot 1 spent 26/08, scored 100/100 - the maximum, so the remaining slots cannot improve the automated score and exist only for report upgrades). Track 2: **1/1 remaining, unspent**. Ledger: `command-centre/SUBMISSION-LEDGER.md`.

## Decisions log

| Date | Decision | Why |
| --- | --- | --- |
| 26/08 | Kit scaffolded; challenge Space source read in full (about/rules/faq/tracks/evaluation) | Gradio app is JS-rendered; the Space repo is the readable source of truth |
| 26/08 | Vendored the Space's `evaluation.py` for offline scoring | Protects the 6-submission budget; CC BY 4.0 permits it with attribution |

## Session log

| Date | What happened |
| --- | --- |
| 26/08 | Kit scaffolded from challenge source; local scorer verified against the official template CSV |
| 26/08 | Dataset access confirmed ACCEPTED; VCF working set downloaded to ~/mva-data/ (logged in DATA-GOVERNANCE.md) |
| 26/08 | Track 1 submission 1: 100/100, F-max 1.000, full match rank 1. Track 2 drafted and taken through four adversarial review rounds |
