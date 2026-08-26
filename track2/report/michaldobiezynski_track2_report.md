# Track 2: Genotype-informed drug repurposing hypotheses for BUB1B-related mosaic variegated aneuploidy

Participant: `michaldobiezynski`. Code and analysis: https://github.com/michaldobiezynski/mva-hackathon-2026

**Framing statement.** Everything below is a hypothesis for further investigation. Nothing here is evidence that any medicine works for this child or for MVA, and nothing here is medical advice. The proposals are ordered by how directly the underlying evidence connects to this proband's specific genotype, and each carries an explicit statement of what would have to be shown before it could be taken seriously by a clinician.

---

## 1. Variant mechanism characterisation

### 1.1 The genotype

Track 1 identified, and the challenge's automated evaluation confirmed, a compound-heterozygous *BUB1B* genotype (GRCh38):

| Allele | Variant | Consequence | Evidence |
| --- | --- | --- | --- |
| A | chr15:40209701 T>G | `NM_001211.6:c.2210T>G`, p.Leu737Ter (stop-gain) | ClinVar VCV000533901, Pathogenic/Likely pathogenic for *Mosaic variegated aneuploidy syndrome 1*, multiple submitters, no conflicts; gnomAD AF 3.3e-5; 46x, GQ99 |
| B | chr15:40220612 T>G | p.Asn1002Lys (missense) | Absent from gnomAD; VEP MODERATE impact on ENST00000287598; 28x, GQ99 |

This is the canonical MVA1 allelic architecture: affected individuals typically carry one missense allele together with one allele producing premature termination or absent transcript ([OMIM 602860](https://omim.org/entry/602860); [Ochiai et al. 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9616775/)).

### 1.2 What BubR1 does, and what these alleles do to it

BubR1 (1050 aa; [UniProt O60566](https://www.uniprot.org/uniprotkb/O60566)) is a core component of the spindle assembly checkpoint (SAC). Within the mitotic checkpoint complex it acts as a stoichiometric inhibitor of Cdc20, restraining the anaphase-promoting complex/cyclosome until every kinetochore is correctly attached; it also has a kinase-dependent role at kinetochores ([Bolanos-Garcia review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8066494/)). When BubR1 function falls below a threshold, chromosomes missegregate and the cell population accumulates the shifting, non-clonal aneuploidies that give MVA its name.

The critical quantitative fact for any therapeutic reasoning here is that **the defect is dose-dependent**: aneuploidy emerges once residual *BUB1B* expression falls below roughly half of normal, and severity tracks the residual level. This is what makes MVA a candidate for a stabilisation strategy rather than only a gene-replacement one: the goal is not to restore wild-type function but to push residual functional protein back above a threshold.

Mapping the two alleles onto the domain structure (UniProt feature coordinates):

- **p.Leu737Ter** terminates translation at residue 737, upstream of the entire protein kinase domain (766-1050, active site 882, ATP-binding 772-780). Whether or not the transcript escapes nonsense-mediated decay, this allele cannot yield kinase-competent protein and loses the whole C-terminus. Treat it as functionally null.
- **p.Asn1002Lys** substitutes a single residue inside the kinase domain of an otherwise **full-length protein**. Its kinase function is plausibly impaired (this is unproven and is the single most important experimental unknown in this report), but the N-terminal regions that mediate the stoichiometric, kinase-independent Cdc20-inhibitory role are structurally intact.

### 1.3 The therapeutic implication that follows

Because allele B produces full-length protein, **this child has a molecular substrate that abundance-raising interventions could act on; a child with two truncating alleles would not.** Every proposal in section 2 rests on that distinction, which is why they are presented as genotype-informed rather than as generic MVA proposals.

Two further mechanistic consequences shape the candidate list:

1. **Downstream senescence burden.** BubR1-insufficient mice (BubR1^H/H^) develop a progeroid phenotype (short lifespan, sarcopenia, cataracts, fat loss, arterial stiffening) driven substantially by accumulation of p16^Ink4a^-positive senescent cells; genetically clearing those cells delays the onset and progression of those disorders ([Baker et al. 2011, *Nature* 479:232](https://www.nature.com/articles/nature10600)). Chromosomally unstable cells more generally enter senescence with an inflammatory secretory phenotype ([Santaguida/He et al.](https://www.nature.com/articles/s41389-018-0072-4)). Some of this proband's burden (low muscle mass, failure to thrive) is phenotypically adjacent to that mouse model.
2. **Cancer predisposition is the acute risk.** The rhabdomyosarcoma that triggered investigation reflects the BUB1B subtype's specific association with malignancy, unlike the CEP57 subtype where cancer is typically absent. Any proposal must be evaluated against whether it plausibly raises or lowers tumour risk.

### 1.4 What the proband's own data can and cannot show

I attempted to quantify the degree of mosaic aneuploidy directly from the supplied bulk WGS VCF, using per-chromosome median read depth and the dispersion of heterozygous allele balance (`~/mva-data/derived/mosaicism_scan.tsv`; code in the repository).

**Result: a methodological negative.** Median depth is flat at 44x across chr1-18 (ratios 1.00), with chrX at 0.50 (consistent with a male proband). No dominant clonal aneuploidy is present in this blood-derived sample. Chromosomes 20-22 show modestly wider allele-balance dispersion (sd ~0.13 vs ~0.09) and 4.5-7% higher depth, but the male chrX "heterozygous" calls, which are necessarily artefactual, display the same signature, so short-chromosome GC/mapping bias is the more parsimonious explanation than genuine mosaicism.

This is the expected result: bulk sequencing averages over cells, and *variegated* aneuploidy is by definition non-clonal, so it largely cancels out. Quantifying this child's mosaicism (the natural biomarker for whether any intervention is working) requires single-cell sequencing or conventional cytogenetics on cultured cells. **I flag this as an evidence gap rather than presenting a null result as a finding**, and it directly shapes the trial design in section 3.

---

## 2. Repurposing candidates

### 2.1 Primary: NAD+ repletion to stabilise the full-length allele's product

**Mechanism link.** BubR1 abundance is regulated post-translationally through acetylation at Lys668: the NAD+-dependent deacetylase SIRT2 maintains the deacetylated state, opposing CBP-mediated acetylation, and BubR1 levels decline with age as NAD+ falls. Overexpressing SIRT2, or treating mice with the NAD+ precursor nicotinamide mononucleotide (NMN), **increases BubR1 abundance in vivo**, and SIRT2 overexpression extends median lifespan in BubR1-hypomorphic mice ([North et al. 2014, *EMBO J* 33:1438](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4194088/); [commentary](https://pubmed.ncbi.nlm.nih.gov/24920578/)).

This is the rare case where a published intervention raises the abundance of the exact protein this child is short of, in a mouse model of the exact insufficiency.

**Why this genotype specifically.** Lys668 lies at residue 668, i.e. **within the portion retained by both alleles in principle but present as full-length protein only from allele B** (allele A stops at 737 and is functionally null regardless). Raising BubR1 abundance therefore means raising the p.Asn1002Lys product. The hypothesis is that pushing that product's steady-state level upward moves total functional BubR1 back toward the ~50% threshold below which aneuploidy emerges, provided the missense protein retains partial function.

**Candidate agents, in order of regulatory tractability:**

| Agent | Status | Notes |
| --- | --- | --- |
| Nicotinamide (vitamin B3) | Widely available; extensive human dosing experience | The only NAD+ precursor with phase 3 oncology-prevention RCT evidence (below) |
| Nicotinamide riboside / NMN | Sold as supplements in most jurisdictions, not approved medicines | NMN is the agent with the direct BubR1 evidence; regulatory status is the obstacle, not the biology |

**The honest evidence picture on nicotinamide.** In ONTRAC ([NEJM 2015](https://www.nejm.org/doi/full/10.1056/NEJMoa1506197)), 500 mg twice daily for 12 months reduced new non-melanoma skin cancers by 23% (P=0.02) in 386 immunocompetent high-risk patients, with no notable safety signal and no benefit persisting after discontinuation. **The replication attempt failed**: in solid-organ transplant recipients ([NEJM 2023](https://www.nejm.org/doi/full/10.1056/NEJMoa2203086)), nicotinamide did not reduce keratinocyte cancers or actinic keratoses; that trial enrolled 158 of its target and stopped early for poor recruitment, so it is underpowered rather than decisively negative, and a non-significant trend toward fewer invasive SCCs was observed. A chemoprevention effect that does not survive into a second population is weak ground for extrapolating to a different disease mechanism in a child, and I present it as supporting context for tolerability and precedent, **not** as evidence of benefit here.

**What would have to be shown before this could be taken seriously (in order):**
1. In patient-derived cells (fibroblasts or lymphoblastoid lines carrying this compound-heterozygous genotype), does NAD+ precursor exposure raise BubR1 protein levels? If the missense product is destabilised or the SIRT2 axis is not limiting in these cells, the hypothesis dies here, cheaply.
2. Does any such increase reduce missegregation rates or aneuploidy fraction in those cells?
3. Does the p.Asn1002Lys product retain measurable checkpoint function (kinase-independent Cdc20 inhibition), i.e. is there anything worth stabilising?
4. Only then: paediatric dosing, safety and, critically, the direction of the effect on cancer risk in a cancer-predisposition syndrome.

### 2.2 Secondary: senolytics for the downstream senescence burden

**Mechanism link.** The senescent-cell clearance experiments that founded the senolytics field were performed in BubR1-hypomorphic mice, i.e. in this gene's own insufficiency model, and clearance both delayed onset and slowed progression of established age-related pathology ([Baker et al. 2011](https://www.nature.com/articles/nature10600)). Senolysis has also extended healthspan in progeroid chromosomal-instability models.

**Candidate agents.** Dasatinib (approved tyrosine-kinase inhibitor) combined with quercetin is the senolytic pairing developed from that framework and already in human trials for other indications.

**Why this is secondary, stated plainly.** It targets a downstream consequence rather than the checkpoint defect; the mouse evidence concerns ageing phenotypes rather than the cancer predisposition or growth failure that dominate this child's presentation; and dasatinib in a child with an active malignancy history raises safety questions I am not positioned to weigh. It belongs in ex vivo and model work, not near a treatment discussion, and the most defensible near-term step is measuring senescent-cell burden (p16 expression, SASP markers) in patient-derived cells to establish whether the burden this proposal targets is even elevated in this child.

### 2.3 A negative recommendation: avoid further checkpoint weakening

Mechanism-literate care includes knowing what not to give. Mps1/TTK and Aurora B inhibitors, in oncology development precisely because they abrogate the spindle assembly checkpoint, would further compromise an already insufficient checkpoint. Outside a deliberately tumour-directed context with explicit specialist oversight, they are mechanistically contraindicated in BUB1B-related MVA. I include this because a repurposing analysis that only generates candidates, and never rules any out, is not doing the mechanistic reasoning it claims to do.

---

## 3. Potential impact

If step 1 of the section 2.1 experimental ladder succeeded (an NAD+ precursor measurably raises BubR1 protein in cells with this genotype), the consequences would be:

- **For this child**: a candidate, orally available, well-characterised intervention aimed at the causal mechanism rather than at symptom management, which is the current standard of care in MVA. The realistic near-term benefit is a research pathway, not a treatment.
- **For MVA more broadly**: the strategy applies to any patient whose genotype retains one full-length allele, which the literature suggests is the common MVA1 architecture (missense plus truncating). It does not apply to biallelic-truncating patients, and that boundary is itself clinically useful information.
- **For the field**: a concrete instance of protein-abundance rescue in a dose-dependent haploinsufficiency-like disorder, where the therapeutic question is threshold-crossing rather than function-restoration.

Both proposals also come with a measurable endpoint problem that this report identifies rather than glosses (section 1.4): mosaicism fraction is the natural biomarker, and it cannot be read from bulk WGS. Establishing single-cell or cytogenetic mosaicism measurement for this child would be a prerequisite for evaluating any intervention, and is a useful contribution independent of whether these particular drugs pan out.

---

## 4. Innovation

A literature sweep (26/08/2026) found **no published proposal of NAD+ repletion or senolytic therapy for mosaic variegated aneuploidy**, despite the adjacent literature being well developed: the aneuploidy-to-senescence link, senolysis in progeroid CIN mice, NAD+ depletion in chromosomally unstable cells, and the 2024 *Nature Reviews Genetics* review of MVA in development, ageing and cancer ([s41576-024-00762-6](https://www.nature.com/articles/s41576-024-00762-6)). Existing intervention prior art in MVA1 is limited to case-level reports such as haematopoietic stem-cell transplantation ([PMC6500003](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6500003/)).

What is novel here is not the observation that SIRT2 stabilises BubR1, which is a decade old, but **the connection of that axis to a specific patient genotype via the argument that only a retained full-length allele makes abundance-raising coherent**, together with the identification of the biomarker gap that would otherwise make any trial uninterpretable.

The method is also reusable: start from the confirmed causal variant, ask what is known to raise or stabilise that specific protein, then filter the resulting candidates by whether the patient's own allelic architecture leaves anything for the intervention to act on.

---

## 5. Scalability

The pipeline that produced this report runs on a laptop from a VCF plus HPO terms, using public resources only (ClinVar, gnomAD, Ensembl VEP, UniProt, MyVariant.info), and the analysis code is in the repository. Applying it to another undiagnosed individual means substituting their variant file and phenotype terms.

The generalisable pattern:

1. Identify the causal variant and, critically, **classify each allele by what protein product it yields** (null vs full-length-but-altered).
2. Search for interventions known to modulate the abundance, stability or post-translational regulation of that specific protein.
3. **Filter by allelic architecture**: abundance-raising strategies require a stabilisable product; this step eliminates candidates that would otherwise look attractive.
4. Identify the measurable biomarker for the disease mechanism, and check honestly whether the available data can measure it.
5. Rank candidates by regulatory tractability, and state what experiment would falsify each hypothesis most cheaply.

Steps 1-3 apply to any dose-dependent loss-of-function disorder, which is a large class. Step 4 is the step most often skipped, and it is what turns a plausible-sounding proposal into a testable one.

---

## 6. Limitations

- The functional consequence of p.Asn1002Lys is **inferred, not measured**. If that product is non-functional or unstable, the primary proposal fails.
- **Phase is unproven**: with a single sample and no parental genotypes, the trans configuration of the two variants is inferred from the phenotype and from the classic MVA1 architecture rather than demonstrated. The parental history of recurrent miscarriage is consistent with two carrier parents.
- The NAD+/BubR1 evidence is from mouse tissue and overexpression systems, not from human MVA cells; the human clinical nicotinamide evidence concerns skin-cancer chemoprevention, an entirely different endpoint, and did not replicate in a second population.
- Senolytic evidence concerns ageing phenotypes in mice, not paediatric MVA.
- No wet-lab validation of any kind was performed; this is a computational analysis of public evidence plus the supplied genomic data.

---

## Acknowledgement

This work was made possible through the Hackathon, organized by Sage Bionetworks in partnership with the MVA Society, Hugging Face, and BEACON (The Benchmarking, Evaluation, and Assessment Consortium for Science), with prize sponsorship from AWS and Anthropic. We are deeply grateful to the child and their family who generously contributed their data and their story to advance research into this rare disease. We acknowledge their trust in making this Hackathon possible.
