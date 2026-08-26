# Track 2: Allele-resolved drug repurposing hypotheses for BUB1B-related mosaic variegated aneuploidy

Participant: `michaldobiezynski`. Code and analysis: https://github.com/michaldobiezynski/mva-hackathon-2026

**Framing statement.** Everything below is a hypothesis for further investigation. Nothing here is evidence that any medicine works for this child or for MVA, and nothing here is medical advice; the one clinical item in this report (section 3.1) is an existing published surveillance guideline, reproduced so that it reaches the people who can act on it, not a recommendation of mine. Candidates are ordered by how directly the underlying evidence connects to this proband's specific genotype, and each states what would have to be shown before it could be taken seriously.

**A note to the family.** A plain-language summary of what this report says, without jargon, is in section 7.

---

## 1. Variant mechanism characterisation

### 1.1 The genotype

Track 1 identified, and the challenge's automated evaluation confirmed, a compound-heterozygous *BUB1B* genotype (GRCh38):

| Allele | Variant | Consequence | Read support | Evidence |
| --- | --- | --- | --- | --- |
| A | chr15:40209701 T>G | `NM_001211.6:c.2210T>G`, p.Leu737Ter (stop-gain) | AD 21,25 (DP 46), GQ 99, PASS | ClinVar VCV000533901, Pathogenic/Likely pathogenic for MVA1, multiple submitters, no conflicts; gnomAD AF 3.3e-5 |
| B | chr15:40220612 T>G | p.Asn1002Lys (missense) | AD 15,13 (DP 28), GQ 99, PASS | Absent from gnomAD; VEP MODERATE impact on ENST00000287598 |

Both calls sit at balanced allelic depth with maximal genotype quality. This is the canonical MVA1 architecture: affected individuals typically carry one missense allele together with one allele producing premature termination or absent transcript ([OMIM 257300](https://omim.org/entry/257300), MVA1 phenotype; gene entry [OMIM 602860](https://omim.org/entry/602860); [Ochiai et al. 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9616775/)).

**Phase.** The two variants are **10,911 bp apart**, far beyond the reach of short-read or read-backed phasing, and no parental genotypes are available. Phase is therefore not merely unproven here, it is unrecoverable from the supplied data; trio or long-read sequencing would settle it. The trans configuration is inferred from the phenotype and the established MVA1 architecture.

### 1.2 What BubR1 does, and what these alleles do to it

BubR1 (1050 aa; [UniProt O60566](https://www.uniprot.org/uniprotkb/O60566)) is a core component of the spindle assembly checkpoint (SAC). Within the mitotic checkpoint complex it acts as a stoichiometric inhibitor of Cdc20, restraining the anaphase-promoting complex/cyclosome until every kinetochore is correctly attached ([Bolanos-Garcia review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8066494/)). Below a threshold of function, chromosomes missegregate and the cell population accumulates the shifting, non-clonal aneuploidies that give MVA its name.

**The quantitative fact that makes a stabilisation strategy coherent.** Suijkerbuijk et al. titrated BUBR1 in human cells with shRNA, generating a residual-protein gradient (8.5%, 10%, 14%, 58%, 77% of normal) that mimics patient genotypes. Premature chromatid separation scaled continuously with the reduction, and **aneuploidy appeared specifically in cells with residual BUBR1 below 50%** ([Suijkerbuijk et al. 2008, *Hum Genet*](https://pubmed.ncbi.nlm.nih.gov/18932004/)). BubR1 function is therefore dosage-dependent with a threshold, which means the therapeutic target is *crossing a threshold*, not restoring wild-type function.

Mapping the alleles onto the domain structure (UniProt feature coordinates):

- **p.Leu737Ter** terminates translation at residue 737, upstream of the entire kinase-fold domain (766-1050). The premature stop lies far upstream of the final exon-exon junction of a 3,153-nt coding sequence, so nonsense-mediated decay of this transcript is expected. Treat this allele as producing no functional protein.
- **p.Asn1002Lys** substitutes a single residue inside the kinase-fold domain of an otherwise **full-length protein**.

### 1.3 What the missense allele probably does, correctly framed

An earlier draft of this report assumed the missense allele is damaging because it impairs kinase activity. That reasoning is wrong, and correcting it changes the conclusion in a useful direction.

**Human BubR1 is a pseudokinase.** Its kinase-fold domain binds nucleotide but does not deliver catalytic activity in vitro, and BUBR1 catalytic activity is dispensable for error-free chromosome segregation in human cells ([Suijkerbuijk et al. 2012](https://www.hubrecht.eu/app/uploads/2017/11/Kops_Research_2012_Suijkerbuijk_The-vertebrate-mitotic-checkpoint-protein-BUBR1-is-an-unusual-psuedokinase.pdf); reviewed in [Adventures of the undead at kinetochores](https://pmc.ncbi.nlm.nih.gov/articles/PMC8018434/)). The domain instead works structurally: together with the adjacent KARD motif it promotes kinetochore recruitment of PP2A-B56, regulating checkpoint silencing and chromosome alignment.

So p.Asn1002Lys cannot be pathogenic by abolishing catalysis, because there is no catalysis to abolish. The plausible mechanisms are (i) destabilising the protein, lowering steady-state BubR1 and pushing total function under the Suijkerbuijk threshold, or (ii) impairing the pseudokinase domain's scaffolding role in PP2A-B56 recruitment. **Mechanism (i) is directly druggable by abundance-raising strategies; mechanism (ii) is not.** Distinguishing them is the single most informative experiment in this report, and it is a protein-level measurement, not a hard one.

Crucially, this reframing also means the checkpoint's core stoichiometric Cdc20-inhibitory function, which is kinase-independent and mediated by regions N-terminal to the substitution, is plausibly intact on allele B. There is something worth stabilising.

### 1.4 The two therapeutic openings this genotype creates

Each allele fails differently, and each failure mode has its own class of intervention:

| Allele | Failure mode | Intervention class it exposes |
| --- | --- | --- |
| A: p.Leu737Ter | Premature stop codon; transcript likely degraded | **Nonsense readthrough** (section 2.1) |
| B: p.Asn1002Lys | Full-length protein, possibly destabilised | **Abundance/stability raising** (section 2.2) |

A child with two truncating alleles would need readthrough or gene replacement rather than stabilisation; a child with two missense alleles would have no readthrough target. Classifying each allele by the *product it yields* is what generates the candidate list, and it is the transferable idea in this report.

### 1.5 Downstream consequences that create further targets

1. **Proteostasis and mitochondrial failure.** In a *Drosophila* neural-stem-cell model of SAC depletion built explicitly as an MVA model, complex aneuploidy compromises stemness through proteostasis failure and mitochondrial dysfunction, and **restoring mitochondrial function recovers brain size** ([González-Blanco et al. 2026, *Nat Commun*](https://www.nature.com/articles/s41467-026-70521-0)).
2. **Senescence burden.** BubR1-insufficient mice develop progeroid phenotypes driven substantially by p16^Ink4a^-positive senescent cells, and clearing those cells delays onset and progression ([Baker et al. 2011, *Nature* 479:232](https://www.nature.com/articles/nature10600)). Two features described in this child, low muscle mass and failure to thrive, overlap with features seen in that model, which is why its findings are relevant here.
3. **Cancer predisposition.** This child's rhabdomyosarcoma is consistent with the malignancy risk specific to the BUB1B subtype, unlike the CEP57 subtype where malignancy is typically absent. Every candidate below must be assessed for its predicted direction of effect on cancer risk.

### 1.6 What the proband's own data can and cannot show

I attempted to quantify mosaic aneuploidy directly from the supplied bulk WGS VCF, using per-chromosome median depth and dispersion of heterozygous allele balance (`eval/mosaicism_scan.tsv`; code in the repository).

Median depth is flat at 44x across chr1-18 (ratios 1.00), with chrX at 0.50 as expected for a male proband. No dominant clonal aneuploidy is present. Chromosomes 20-22 show wider allele-balance dispersion (sd ~0.13 vs ~0.09) and 4.5-7% higher depth, but the male chrX "heterozygous" calls, which are necessarily artefactual, carry the same signature, so short-chromosome GC/mapping bias is the more parsimonious explanation.

Three caveats, stated precisely:

- **This method is crude.** It is unphased and detects only substantial clonal imbalance. The field-standard approach is a phased-BAF-plus-coverage hidden Markov model (MoChA), which detects allelic imbalance at low cell fractions; running it would convert this negative into a much stronger one, and is planned before any use of these data as a baseline.
- **The negative is specific, not general.** Random per-cell whole-chromosome events in different directions do largely cancel in bulk data; that is not the same as saying bulk WGS cannot detect mosaicism at all, which would be false.
- **Tissue matters.** MVA mosaicism is classically assayed on cultured cells, and PHA-stimulated lymphocyte culture selects against aneuploid cells, so blood may be among the least informative tissues available.

Mosaic fraction is the natural biomarker for whether any intervention in section 2 is working, and it cannot be read from these data. That gap shapes section 3.2.

---

## 2. Repurposing candidates

### 2.0 Candidate decision table

| # | Candidate | Target allele / mechanism | Evidence tier | Regulatory tractability | Paediatric safety | Predicted effect on cancer risk | Cheapest falsification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Readthrough (ataluren; ELX-02; aminoglycosides) | Allele A: TGA premature stop | Human trials in other nonsense diseases; none in MVA | Ataluren contested; ELX-02 investigational; gentamicin approved but toxic | Ataluren used in children (DMD); aminoglycoside oto/nephrotoxicity a serious concern | Neutral to favourable if BubR1 rises | Readthrough reporter + BubR1 immunoblot in patient cells |
| 2 | NAD+ repletion (nicotinamide; NR/NMN) | Allele B: SIRT2-dependent BubR1 stabilisation | Mouse in vivo BubR1 increase; human RCTs only for unrelated endpoints | Nicotinamide widely available; NMN/NR are supplements | Extensive human exposure to nicotinamide | Favourable, on Baker 2013 | BubR1 immunoblot ± NAD+ precursor in patient cells |
| 3 | Mitochondrial/proteostasis support | Downstream of aneuploidy in an MVA model | Genetic rescue in *Drosophila* MVA model | Agents vary; several are supplements or approved | Varies by agent | Unknown | Mitochondrial function assay in patient cells |
| 4 | Senolytics (dasatinib + quercetin) | Downstream senescence burden | Mouse BubR1 model; human trials in other indications | Dasatinib approved (oncology) | Serious concerns in a child | Unclear | Measure p16/SASP burden first |
| 5 | **Avoid**: Mps1/TTK, Aurora B inhibitors | Further SAC weakening | Mechanistic | n/a | n/a | Adverse | n/a |

### 2.1 Allele A: nonsense readthrough, the tightest genotype link in this case

**The specific fact.** `c.2210T>G` changes codon 737 from **TTA to TGA**: of the six leucine codons, TTA is the only one that a T>G substitution at codon position 2 converts into a stop, so the identity of the premature stop codon is determined unambiguously by the variant itself (arithmetic in the repository). The premature stop is therefore **TGA (UGA in mRNA)**.

**Why that matters.** UGA is the leakiest stop codon, with the highest intrinsic readthrough potential, and ataluren promotes dose-dependent readthrough of all three nonsense codons **with highest efficiency at UGA** ([Ataluren review](https://www.mdpi.com/1424-8247/14/8/785); [mechanism study](https://pubmed.ncbi.nlm.nih.gov/24483936/)). This proband's truncating allele is thus in the most readthrough-amenable class, in a disease where the therapeutic goal is crossing a 50% dosage threshold rather than achieving full restoration. Partial readthrough of allele A adds full-length wild-type protein, which is exactly the currency the Suijkerbuijk threshold is denominated in.

**Candidate agents.** Ataluren (oral, extensive paediatric exposure in Duchenne muscular dystrophy); ELX-02 (investigational aminoglycoside analogue); gentamicin (approved but with real oto- and nephrotoxicity).

**The honest case against.** Ataluren's regulatory position is contested and its efficacy in DMD disputed; aminoglycoside toxicity is unacceptable for chronic paediatric use; readthrough efficiency is typically low single-digit percentages; and readthrough is inseparable from the NMD question, since a transcript degraded before translation cannot be read through, which is why NMD-inhibition combination approaches exist and why measuring allele A transcript abundance comes first.

**Falsification ladder:**
1. Is allele A transcript present at all in patient cells (allele-specific expression by RNA-seq or allele-specific qPCR)? If NMD has removed it, readthrough alone cannot work, and the question becomes whether NMD inhibition plus readthrough is viable.
2. Does readthrough agent exposure produce detectable full-length BubR1 in patient-derived cells?
3. Does any increase reduce missegregation or aneuploidy fraction?

### 2.2 Allele B: NAD+ repletion to stabilise the full-length product

**Mechanism link.** BubR1 abundance is regulated by acetylation at Lys668: CBP-mediated acetylation primes degradation, and the NAD+-dependent deacetylase SIRT2 opposes it. Overexpressing SIRT2 or treating mice with the NAD+ precursor NMN **increases BubR1 abundance in vivo**, and SIRT2 overexpression extends median lifespan in BubR1-hypomorphic mice ([North et al. 2014, *EMBO J* 33:1438](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4194088/)).

**Why raising BubR1 is the right direction, and why it plausibly reduces rather than raises cancer risk.** Sustained BubR1 overexpression in mice attenuates aneuploidy, reduces chromosomal instability and tumorigenesis **even in the presence of oncogenic Ras**, and extends median and maximum lifespan ([Baker et al. 2013, *Nat Cell Biol* 15:96](https://www.nature.com/articles/ncb2643)). In a cancer-predisposition syndrome this matters more than anything else in the section: the intervention direction is the one shown to be protective in the corresponding mouse model, not merely non-harmful.

**Convergence with the MVA model literature.** Restoring mitochondrial function rescues the MVA phenotype in the *Drosophila* model above, and NAD+ repletion improves mitochondrial function; the two lines of evidence point the same way through different routes, which strengthens both.

**Candidate agents.** Nicotinamide (widely available; the only NAD+ precursor with phase 3 RCT evidence in an oncology-prevention endpoint) and nicotinamide riboside / NMN (NMN is the agent with the direct BubR1 evidence, but both are marketed as supplements rather than approved medicines, which is a regulatory obstacle rather than a biological one).

**The honest evidence picture on nicotinamide's human trials.** In ONTRAC ([NEJM 2015](https://www.nejm.org/doi/full/10.1056/NEJMoa1506197)), 500 mg twice daily reduced new non-melanoma skin cancers by 23% (P=0.02) in 386 immunocompetent high-risk patients, with no notable safety signal and no benefit persisting after discontinuation. The replication attempt failed: in solid-organ transplant recipients ([NEJM 2023](https://www.nejm.org/doi/full/10.1056/NEJMoa2203086)) nicotinamide did not reduce keratinocyte cancers, though that trial stopped early at 158 participants for poor recruitment and is underpowered rather than decisively negative. These trials concern a different disease mechanism and endpoint; they are cited for tolerability and precedent, not as evidence of benefit here.

**Falsification ladder, ordered so the gating question comes first:**
1. **Does the p.Asn1002Lys product retain function, and is it destabilised?** Immunoblot for steady-state BubR1 in patient-derived cells, plus a checkpoint-function readout. This distinguishes mechanism (i) from (ii) in section 1.3 and determines whether anything below is worth doing.
2. Does NAD+ precursor exposure raise BubR1 protein levels in those cells?
3. Does any increase reduce missegregation rates or aneuploidy fraction?
4. Only then: paediatric dosing and safety, with cancer-risk direction informed by Baker 2013.

### 2.3 Mitochondrial and proteostasis support

The MVA-specific *Drosophila* work rescued the phenotype through autophagy activation, ROS scavenging, and restoration of mitochondrial proteostasis. Those interventions were genetic, so their pharmacological translation is unclaimed ground: rapamycin (approved) for the TOR axis, N-acetylcysteine or mitochondria-targeted antioxidants for the ROS axis. This is the least mature candidate class here and is included because it is the only intervention evidence generated in an explicitly MVA-framed model, and because it converges with candidate 2.

### 2.4 Senolytics for the downstream senescence burden

The senescent-cell clearance experiments that founded the senolytics field were performed in BubR1-hypomorphic mice, so dasatinib plus quercetin is an obvious candidate for a BUB1B disorder, and obviousness is not an argument against correctness. It remains secondary because it targets a downstream consequence rather than the checkpoint defect; because the mouse evidence concerns ageing phenotypes rather than the malignancy risk and growth failure that dominate this child's presentation; and because dasatinib in a child with a malignancy history raises safety questions beyond what this analysis can weigh. The defensible near-term step is measuring senescent-cell burden (p16 expression, SASP markers) in patient-derived cells to establish whether the burden this proposal targets is elevated at all.

### 2.5 A negative recommendation: avoid further checkpoint weakening

Mps1/TTK and Aurora B inhibitors are in oncology development precisely because they abrogate the spindle assembly checkpoint. In a patient whose checkpoint is already below threshold, they are mechanistically contraindicated outside a deliberately tumour-directed context under specialist oversight. A repurposing analysis that only generates candidates and never rules any out has not finished the mechanistic reasoning.

---

## 3. Potential impact

### 3.1 The most immediately useful output: existing surveillance guidance

Confirming a BUB1B-related MVA diagnosis has a concrete clinical implication that already exists in published guidance and requires no new research: **Wilms tumour surveillance by renal ultrasonography every three to four months until age five** is recommended for individuals with cytogenetically confirmed MVA and/or BUB1B mutations ([Orphanet](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=1052&amp=&lng=EN); this reflects current UK recommendations), against a documented background of high malignancy incidence in the BUB1B subtype, including Wilms tumour, rhabdomyosarcoma and leukaemia, typically presenting in early childhood.

This is not a recommendation of mine and it is for the child's clinical team to apply or to have already applied. It is reproduced here because a report that establishes the genotype and stops short of noting the surveillance implication would have withheld the most immediately actionable consequence of its own finding.

### 3.2 Research impact

- **For this child**: two candidate intervention classes aimed at the causal mechanism rather than symptom management, each with a cheap first experiment that can rule it out before anyone's expectations are raised.
- **For others with MVA**: the allele-classification step generalises. Any patient retaining a full-length allele is a candidate for stabilisation; any patient with a premature stop codon, particularly UGA, is a candidate for readthrough; the two are complementary, and many MVA1 patients carrying one missense plus one truncating allele are candidates for both at once.
- **A measurement gap worth closing regardless**: mosaic fraction is the natural biomarker for disease burden and for any intervention, and section 1.6 shows the supplied bulk WGS cannot deliver it. Establishing single-cell or cytogenetic mosaicism measurement for this child is a prerequisite for evaluating any of this, and is useful even if every candidate above fails.

---

## 4. Innovation

**Correction to an earlier claim.** A previous draft asserted that intervention prior art in MVA was limited to case reports. That was wrong: [González-Blanco et al. 2026, *Nat Commun*](https://www.nature.com/articles/s41467-026-70521-0) is an explicitly MVA-framed intervention study in which mitochondrial and proteostasis rescue recovers brain size in a *Drosophila* SAC-depletion model. That work is incorporated above as candidate 2.3 and as convergent support for candidate 2.2. Correcting this strengthens the report rather than weakening it, and it would have been visible to any judge familiar with the 2026 literature.

What remains novel, to the best of a literature search conducted 26/08/2026 across PubMed, Europe PMC and general web search (no publication proposing NAD+ repletion, senolytics, or nonsense readthrough for MVA was found):

1. **Allele-resolved candidate generation.** The two alleles are treated as separate therapeutic problems with separate solution classes, rather than the genotype being treated as one lesion. This is what produces the readthrough candidate, which a gene-level analysis cannot see.
2. **The stop-codon identity as a therapeutic determinant.** Deriving TGA from the coding change, and connecting it to the readthrough-efficiency hierarchy, turns a routine annotation into candidate selection.
3. **The pseudokinase correction.** Recognising that BubR1's kinase activity is dispensable reframes what the missense allele can and cannot be doing, and makes the stabilisation hypothesis more plausible rather than less.

The method is reusable: identify the causal variant, classify each allele by the product it yields, ask what is known to raise or stabilise that specific protein or to rescue that specific lesion class, and filter by whether the patient's own allelic architecture leaves anything for the intervention to act on.

---

## 5. Scalability

The analysis runs on a laptop from a VCF plus HPO terms, using public resources only (ClinVar, gnomAD, Ensembl VEP, UniProt, MyVariant.info), with code in the repository.

The generalisable pattern:

1. Identify the causal variant(s).
2. **Classify each allele by the product it yields**: no protein (premature stop, with the stop codon identity recorded), full-length but altered, or absent transcript.
3. Establish whether the disorder is dosage-dependent with a threshold, since that determines whether partial rescue is meaningful.
4. Map each allele's failure mode to intervention classes: readthrough for premature stops; abundance or stability raising for full-length products; pathway rescue for downstream consequences.
5. **Filter by allelic architecture**: stabilisation needs a stabilisable product, readthrough needs a premature stop. This step eliminates candidates that otherwise look attractive.
6. Identify the biomarker for the mechanism and check honestly whether available data can measure it.
7. Rank by regulatory tractability and state the cheapest falsifying experiment for each.

Steps 2-5 apply to any dosage-dependent loss-of-function disorder, a large class. Step 6 is the one most often skipped, and it is what makes the difference between a plausible proposal and a testable one.

**Honest limitation of this section**: the pattern is demonstrated on one case. A second worked example on a public case would be needed before calling it a validated pipeline rather than a described method.

---

## 6. Limitations

- The functional consequence of p.Asn1002Lys is **inferred, not measured**; whether it destabilises the protein or impairs PP2A-B56 scaffolding determines whether candidate 2.2 is viable at all. No in-silico structural or stability prediction was run for this draft; that is the first gap to close.
- **Phase is unrecoverable** from the supplied data (variants 10,911 bp apart, no parental samples), so the trans configuration is inferred from phenotype and the established MVA1 architecture.
- NMD of allele A is **predicted from position, not measured**; the readthrough candidate depends on it and step 1 of section 2.1 addresses it directly.
- The NAD+/BubR1 evidence is from mouse and overexpression systems, not human MVA cells; the human nicotinamide trials concern an unrelated endpoint and did not replicate in a second population.
- The mosaicism analysis used a crude in-house method rather than the field-standard phased-BAF HMM, and blood may be the least informative tissue for MVA mosaicism.
- No wet-lab validation of any kind was performed. This is a computational analysis of public evidence plus the supplied genomic data.

---

## 7. Summary for the family, in plain language

Your child's genetic result points to a gene called *BUB1B*. It carries the instructions for a protein that acts like a quality inspector during cell division: it holds each cell back from dividing until all the chromosomes are lined up properly. Your child has two changes in this gene, one inherited from each parent, and together they leave too little of that protein working.

The two changes are different, and that turns out to matter. One is like a sentence that stops halfway, so no usable protein gets made from it. The other still makes a complete protein, just with one letter altered.

That difference opens two separate ideas worth researching. For the halted instruction, there are medicines already used in other genetic conditions that can sometimes persuade a cell to read straight past that kind of stop, and the specific stop in your child's gene is the type that responds best. For the complete-but-altered protein, there is laboratory research showing that raising the amount of this exact protein is possible, and that in mice more of it protects against the chromosome problems and against cancer.

**None of this is a treatment, and none of it is ready to try.** These are ideas that researchers would need to test first in cells grown in a laboratory, starting with cheap experiments designed to rule the wrong ideas out quickly. This report also flags one thing that is already established practice rather than research: children with this genetic result are recommended to have regular kidney scans every few months in early childhood, which is something for your child's medical team to confirm they have in hand.

We are grateful that you shared your child's data. It is what made any of this possible.

---

## Acknowledgement

This work was made possible through the Hackathon, organized by Sage Bionetworks in partnership with the MVA Society, Hugging Face, and BEACON (The Benchmarking, Evaluation, and Assessment Consortium for Science), with prize sponsorship from AWS and Anthropic. We are deeply grateful to the child and their family who generously contributed their data and their story to advance research into this rare disease. We acknowledge their trust in making this Hackathon possible.
