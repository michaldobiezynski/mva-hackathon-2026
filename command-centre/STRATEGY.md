# Strategy

## What the scoring code actually rewards (read from `eval/evaluation.py`, vendored from the Space)

These are mechanics, not guesses; the exact code that scores submissions is public.

1. **Compound-het pairs must be ONE row.** A full match requires `row.variants == true_variants` as a set. If the truth is a pair and you submit the two variants as separate rows, the best you can get is a partial match: **half points**. So every compound-het hypothesis goes in as a pair row (`chrom_2/pos_2/ref_2/alt_2` filled). Submitting the constituent singles as additional lower-ranked rows costs nothing and hedges nothing extra; the pair row is what matters.
2. **The answer is almost certainly a pair.** The evaluator's own docstring: "a clinically validated compound-heterozygous answer key". Half-credit-for-one-of-two is also advertised on the Overview tab. Plan the pipeline around recessive/biallelic candidates from the start. (Confidence: high that the key is compound-het; the docstring could in principle be stale.)
3. **Rank 1 is worth double rank 2.** Tiers: rank 1 = 100, ranks 2-3 = 50, 4-5 = 25, 6-10 = 10, >10 = 0. Ordering effort concentrates at the top of the list.
4. **Low-confidence extra rows are free.** Rank points ignore rows below the true match; F-max sweeps thresholds over the submitted EPCR values, so junk below the optimal threshold never enters precision. Always submit all 10 rows, ranked honestly. The only way an extra row hurts is by sitting ABOVE the true variant.
5. **Each submission is an oracle query.** Upload feedback instantly reveals full/partial/no match and the rank. Six submissions x 10 rows = up to 60 candidate slots with exact-match feedback. Treat the budget as an adaptive search: early submissions carry the pipeline's best 10 ranked candidates AND maximise information (e.g. diverse gene coverage); later submissions re-rank based on what the feedback ruled out. Only the best score counts, so a low-scoring probe costs nothing but the slot.
6. **EPCR must be in (0, 1]**, max 10 rows, `finding_type` in {primary, secondary}; the parser hard-rejects violations. `eval/local_scorer.py` runs this exact parser offline; never spend a slot on a format error.

## Track 1 plan

- **Domain prior first.** MVA is classically caused by biallelic variants in a small set of spindle-assembly-checkpoint genes; from literature, BUB1B is the canonical MVA gene, with CEP57 and TRIP13 also established (moderate confidence from background knowledge; verify against current literature/OMIM before relying on it). The family already has an NHS-confirmed diagnosis, so the variant is findable with sound methods; this is a needle-known-to-exist search.
- **Pipeline shape:** work from the provided VCFs (re-calling from FASTQ on a laptop is the expensive path; only if VCF quality demands it). Annotate (VEP/ClinVar/gnomAD frequencies), filter to rare + protein-affecting, genotype-filter for biallelic configurations, rank by HPO-phenotype match (the dataset ships HPO terms; tools like Exomiser/LIRICAL are built for exactly this) plus known-gene prior.
- **Feasibility screen before committing** (ICML lesson): confirm the VCF sizes and that annotation is laptop-tractable before promising a fancy method. The claims-vs-compute check applies to pipelines too.
- **Secondary findings are a free qualitative bonus**: they don't dent the automated score and the judges review them; include well-supported ones with clear `notes`.

## Track 2 plan (single-shot; 35% rigor, 25% impact, 25% innovation, 15% scalability)

- Do it AFTER Track 1 stabilises: the mechanism story inherits credibility from the variant identification.
- Structure the report to the rubric: mechanism characterisation (LoF/GoF, pathway, downstream consequence) -> candidate drugs with mechanism-linked rationale -> what validation would look like -> how the approach generalises (scalability is 15% and cheap to earn with an honest generalisation section).
- Frame candidates strictly as hypotheses for follow-up; overclaiming a treatment for a real, named child's condition is both a rules problem and a rigor deduction.
- Draft early, adversarially review (fresh-context red team), sit on it, submit near the deadline. One shot.

## Lessons ported from previous campaigns

- **Substance gates, not structure gates**: `scripts/selfcheck.py` fails on unfilled `[[FILL` markers and on any genomic data file in the tree, the two silent catastrophes for this challenge.
- **Evidence is append-only**: analysis outputs and scorer runs land in timestamped files; nothing gets overwritten.
- **State dashboard**: `STATUS.md` carries budget, phase and next actions across sessions.
- **Two months, not a weekend**: the risk profile inverts vs micro1; here the failure mode is drift and a rushed final week, not scope. The ledger + status discipline is the countermeasure. Deadline pressure is artificial until October; data deletion (23/11) is the only truly unforgiving date.
