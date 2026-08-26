# Reproducing the ΔΔG calculation

Predicts the folding free-energy change for p.Asn1002Lys in the BubR1 pseudokinase domain, using ThermoMPNN (Dieckhaus et al., *PNAS* 2024). Runs on CPU in a few minutes; no GPU, no MSA, no licence.

## Why the domain is extracted rather than using the full-length model

ThermoMPNN evaluates a structure's local environment. In a 1050-residue multi-domain AlphaFold model, the *relative placement* of domains is far less reliable than the fold of each domain, so a residue can appear buried purely because of arbitrary inter-domain packing.

`eval/structural_context.py` was used to check whether that risk applies here. Asn1002 has **129 of 129** heavy-atom neighbours within 10 Å coming from inside the pseudokinase domain (766-1050) and none from outside, so extracting the domain loses nothing and the calculation is well posed.

The same check disqualifies the equivalent calculation at Leu737: **82 of its 128** neighbours come from outside the domain, so any ΔΔG there would be dominated by model packing rather than by the residue's real environment. That number is why this report makes no ΔΔG claim for the readthrough site.

## Steps

```sh
# 1. Structure (AlphaFold DB; confirm the current version via the API rather than
#    guessing the filename, which changes between releases)
curl -s "https://alphafold.ebi.ac.uk/api/prediction/O60566" | python3 -c "import json,sys; print(json.load(sys.stdin)[0]['pdbUrl'])"
curl -o AF-O60566.pdb "https://alphafold.ebi.ac.uk/files/AF-O60566-F1-model_v6.pdb"

# 2. Confirm the residue's environment is intra-domain before truncating
.venv/bin/python eval/structural_context.py AF-O60566.pdb 1002 737

# 3. Extract residues 766-1050, preserving original numbering
#    (the extracted file is committed as eval/bubr1_kinase_domain.pdb)

# 4. ThermoMPNN
git clone --depth 1 https://github.com/Kuhlman-Lab/ThermoMPNN.git
python3 -m venv .venv
.venv/bin/pip install torch pytorch-lightning omegaconf biopython pandas tqdm torchmetrics wandb

# GOTCHA: local.yaml ships with the authors' cluster paths hardcoded, and inference
# fails with FileNotFoundError on /proj/kuhl_lab/ThermoMPNN/vanilla_model_weights/v_48_020.pt.
# The weights are bundled in the clone; repoint thermompnn_dir at it:
sed -i '' "s|/proj/kuhl_lab/ThermoMPNN|$PWD/ThermoMPNN|" ThermoMPNN/local.yaml

cd ThermoMPNN
WANDB_MODE=disabled ../.venv/bin/python analysis/custom_inference.py \
    --pdb ../eval/bubr1_kinase_domain.pdb --chain A --out_dir ../eval/

# 5. Summarise (establishes the sign convention from the data, not from assumption)
.venv/bin/python eval/ddg_analysis.py --residue 1002 --mutation K
```

Output is a site-saturation scan: 285 positions × 20 residues = 5,700 predictions, committed as `eval/ddg_ssm_kinase_domain.csv`.

## Result

```
N1002K: ddG = +1.507 kcal/mol (75th percentile of all substitutions in this domain)
site mean +1.630 (81st percentile of 285 sites): more substitution-sensitive than average
```

Statistics exclude the 285 identity substitutions (wildtype == mutation), which are not substitutions and would otherwise pad the low end of the distribution.

Sign convention is established internally rather than taken on trust: identity substitutions score exactly +0.0000, and X→Pro averages +1.86 against an overall mean of +0.87, so **positive values are destabilising**.

## Caveats

- ThermoMPNN was trained largely on small monomeric domains; applying it to a domain excised from a large multi-domain protein is a reasonable but not fully validated use.
- The input is a predicted structure, not an experimental one. Domain-internal pLDDT averages 81.9, and Asn1002 itself sits at 91.1, so the local model is confident, but it remains a model.
- A predicted ΔΔG is not a measured one. The definitive experiment is an immunoblot for steady-state BubR1 in patient-derived cells.
