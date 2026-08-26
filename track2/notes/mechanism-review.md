# Track 2 mechanism review - working notes (26/08)

Foundation: the Track 1 answer is confirmed (100/100): BUB1B compound het, p.Leu737Ter (ClinVar P/LP for MVA1) + p.Asn1002Lys (novel missense). Everything below builds on that genotype.

## Disease mechanism (literature-verified)

- BubR1 (BUB1B) is a core spindle-assembly-checkpoint (SAC) protein: stoichiometric Cdc20 inhibitor within the mitotic checkpoint complex, restraining APC/C activation until kinetochores attach. Loss/insufficiency -> chromosome missegregation -> mosaic aneuploidy. [PMC8066494; OMIM 602860]
- **Dose dependence is the key fact**: aneuploidy appears when residual BUB1B expression falls below ~50%; severity tracks residual protein. [PMC8066494 and refs therein]
- The classic MVA1 allelic architecture is exactly ours: families carry one missense + one truncating/absent-transcript allele (Hanks et al. pattern). [OMIM 602860; PMC9616775]
- BubR1-insufficient mice: MVA phenotype in embryos, pregnancy loss parallels in humans (fits the parental recurrent-miscarriage history). [PMID 24981203]
- BubR1H/H hypomorphic mice are a progeria model: short lifespan, sarcopenia, lordokyphosis, cataracts, fat loss, arterial stiffening; several map onto the proband's low muscle mass / failure to thrive. [Baker 2011, Nature 479:232]

## Genotype-specific leverage (the personalisation story)

The two alleles are NOT equivalent therapeutic targets:
- p.Leu737Ter: premature stop; the allele likely yields no functional protein (NMD or C-terminally truncated product missing the kinase region - domain claim TO VERIFY against a BubR1 domain map).
- p.Asn1002Lys: full-length protein with a single substitution. **This allele produces stabilisable protein.** Any intervention that raises steady-state BubR1 abundance acts on the missense allele's product.

This genotype-dependence is the rigor+innovation core: BubR1-raising strategies only make sense because one allele is full-length. A patient with two truncating alleles would gain nothing.

## Candidate directions (all: hypotheses for investigation, never treatment claims)

### 1. NAD+ repletion -> SIRT2-mediated BubR1 stabilisation
- Mechanism: BubR1 is acetylated at K668; NAD+-dependent SIRT2 deacetylates and stabilises it. NMN treatment increases BubR1 abundance in vivo; SIRT2 overexpression extends BubR1H/H lifespan. [North et al. 2014, EMBO J 33:1438, PMC4194088; PMID 24920578]
- Repurposing shape: NMN / nicotinamide riboside are supplements, not approved medicines - regulatory framing needs care. **Nicotinamide (high-dose vitamin B3) is pharmacy-available and has RCT evidence in skin-cancer chemoprevention (ONTRAC - TO VERIFY next pass)**; a cancer-chemoprevention-adjacent NAD+ precursor in a cancer-predisposition syndrome is a tidy story.
- Open questions: does NAD+ repletion raise BubR1 in human cells with this allele class; does N1002K alter SIRT2 interaction or K668 acetylation dynamics; paediatric dosing/safety evidence.

### 2. Senolytics for the downstream progeroid burden
- Mechanism: BubR1 insufficiency -> accelerated accumulation of p16Ink4a-positive senescent cells; genetic clearance in BubR1H/H mice delays ageing-associated disorders. [Baker et al. 2011, Nature 479:232]
- Repurposing shape: dasatinib (approved, CML) + quercetin - the senolytic combination developed from this exact mouse framework, already in human trials for other indications.
- Caveats: treats downstream consequence, not the checkpoint defect; dasatinib in a child is a serious safety question; strictly a research hypothesis for models/ex vivo first.

### 3. Contra-indication insight (cheap rigour points)
Drugs that further weaken the SAC (Mps1/TTK or Aurora B inhibitors, in trials for oncology) are mechanistically contraindicated in MVA outside tumour-directed contexts; worth one paragraph in the report as mechanism-literate safety reasoning.

## Next passes

1. Verify BubR1 domain map (does L737* remove the kinase domain; is NMD expected from the exon position).
2. Verify ONTRAC nicotinamide trial details before citing.
3. Prior-art sweep: has anyone proposed NAD+ repletion or senolytics for MVA1 specifically? (Innovation criterion depends on this.)
4. Mosaicism quantification from the FASTQs (per-chromosome depth) - on-theme evidence for the report and a personal severity baseline.
5. Draft report to the rubric; adversarial review; sit on it; submit near deadline (single shot).
