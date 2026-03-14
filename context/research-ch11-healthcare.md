# Research Notes: Chapter 11 — AI in Healthcare and Medical Imaging

## Date: 2026-03-14
## Status: COMPLETE

---

## 1. Healthcare Ecosystem

### Key Stakeholders
- **Hospitals/Clinics**: acute care, diagnostics, surgical facilities
- **Insurers/Payers**: risk pooling, claims processing, reimbursement
- **Pharma/Biotech**: drug discovery, manufacturing, clinical trials
- **Regulators**: FDA (US), EMA (EU), national health agencies
- **Patients/Society**: data subjects, care recipients

### Digital Health Transformation Drivers
1. EHR adoption — longitudinal patient data at scale
2. Medical device connectivity (IoMT) — real-time physiological monitoring
3. Genomics cost collapse — next-gen sequencing now <$1000 per whole genome
4. Interoperability standards: **HL7 FHIR** (API standard for health data exchange)

### EHR Systems
- Structured data: ICD-10 (diagnoses), SNOMED-CT (clinical concepts), LOINC (labs), RxNorm (medications)
- Unstructured: clinical notes, radiology reports, discharge summaries
- AI approaches: transformer models pre-trained on clinical text (BioBERT, ClinicalBERT, Med-BERT)
- Challenges: missing data, inconsistent coding, access controls (HIPAA, GDPR)

---

## 2. Drug Discovery

### Pipeline (10-15 years, $1-2B average cost)
1. Target identification (genomics, proteomics, network biology)
2. Hit discovery — virtual screening of 10^6–10^9 compounds
3. Lead optimisation — improve ADMET properties
4. Pre-clinical — animal models, safety/efficacy
5. Clinical trials Phase I (safety) → II (efficacy) → III (large trial)
6. Regulatory approval → post-market surveillance

### AI Approaches
- **Virtual screening**: ML classifiers rank compound libraries by predicted binding affinity
  - Ligand-based: QSAR models, fingerprint similarity (Morgan fingerprints)
  - Structure-based: docking + ML scoring function
- **Graph Neural Networks**: molecules as graphs; message passing on atom-bond graph
- **Generative molecular design**:
  - Junction-Tree VAE: encodes molecule to latent space; Bayesian optimization in latent space
  - MolGAN: graph GAN for molecule generation
  - RL-based SMILES generation with reward shaping (QED, activity, synthesisability)
- **ADMET prediction**: GNN/RF predict toxicity, solubility, metabolic stability, hERG inhibition

### AlphaFold 2 (2021, Jumper et al., Nature)
- Task: predict 3D protein structure from amino acid sequence
- Architecture: Evoformer (48 transformer blocks updating MSA + pair representations) + Structure Module (IPA)
- Output: all-atom coordinates + per-residue pLDDT confidence
- Impact: 200M+ structures in AlphaFold DB; accelerated neglected disease drug discovery

---

## 3. Personalized Medicine

### Precision Medicine
- Stratify patients by molecular subtype for targeted therapy
- Biomarkers: measurable predictors of treatment response (genomic mutations, protein levels, imaging features)
- Companion diagnostics: IVD co-approved with drug to identify responsive subpopulation
- Examples: HER2+ breast cancer (trastuzumab), BRAF V600E melanoma (vemurafenib)

### Pharmacogenomics
- CYP450 polymorphisms → 4 metaboliser phenotypes (poor/normal/rapid/ultrarapid)
- HLA typing for adverse reaction prediction (abacavir hypersensitivity HLA-B*57:01)
- ML-guided dosing: warfarin (IWPC algorithm), tacrolimus

### Digital Twins
- Continuously updated multi-modal patient model
- Applications: disease progression simulation, therapy planning, personalised radiation
- Challenges: model calibration, biological complexity, regulatory framework

### Clinical Decision Support (CDSS)
- Sepsis early warning: NEWS2 score; AI variants improve specificity
- Drug interaction checking
- Differential diagnosis ranking (probabilistic, NLP-driven)

---

## 4. Medical Imaging Physics

### X-Ray / CT
- X-ray: Beer-Lambert attenuation I = I0 * e^(-μx); dense tissue = bright
- CT: fan-beam projections + filtered back-projection reconstruction (or iterative)
- Hounsfield Units: bone ~+1000, water=0, air=-1000
- Risk: ionising radiation dose; fast, high spatial resolution

### MRI
- Nuclear magnetic resonance of H protons
- B0 field aligns spins; RF pulse excites; T1/T2 relaxation encodes tissue type
- k-space → Fourier transform → image
- Advantages: no radiation, excellent soft-tissue contrast
- Variants: fMRI (BOLD signal), DWI, MRA, MRS

### PET
- Radiotracer (18F-FDG) → positron emission → annihilation → two 511 keV photons in coincidence
- Metabolic/functional imaging; combined with CT/MRI for anatomical co-localisation
- Uses: oncology staging, amyloid/tau imaging (Alzheimer's)

### Ultrasound
- High-frequency sound (2–15 MHz) reflected at tissue boundaries
- B-mode: 2D cross-section in real time
- Doppler: blood flow velocity
- Advantages: portable, real-time, no radiation
- Disadvantages: operator-dependent, poor bone/air penetration

---

## 5. AI for Medical Image Analysis

### Classification
- Transfer learning from ImageNet (Inception, ResNet, EfficientNet) fine-tuned on medical datasets
- Esteva et al. 2017 (Nature): skin cancer classification, 757 categories, non-inferior to 21 dermatologists
- Gulshan et al. 2016 (JAMA): diabetic retinopathy from fundus photos, AUC 0.99

### Detection
- Lesion detection: pulmonary nodule (lung CT CAD), polyp (colonoscopy), microcalcification (mammography)
- RetinaNet / Faster R-CNN adapted for medical imaging
- Challenges: class imbalance (foreground << background), small object scale
- Solutions: focal loss, hard example mining, FPN multi-scale features

### Segmentation
- **U-Net** (Ronneberger et al. 2015): encoder-decoder + skip connections
  - Encoder: contracting path (conv + maxpool)
  - Decoder: expanding path (transposed conv)
  - Skip connections preserve fine spatial detail
  - Works with limited labelled data (~100s images)
- Applications: organ segmentation (liver, prostate, brain), tumour delineation, retinal vessels
- 3D extensions: V-Net, nnU-Net (self-configuring)

### Registration
- Align pre-op image to intraoperative space
- Rigid: rotation+translation; deformable: dense displacement field
- Metrics: mutual information (multi-modal), SSD (mono-modal)
- Learning-based: VoxelMorph — CNN predicts deformation field in single pass

---

## 6. Ground Truth and Clinical Integration

### Annotation Challenges
- Requires expert clinicians (radiologists, pathologists)
- Inter-rater variability on ambiguous cases
- Active learning, weak supervision (MIL from report-level labels), self-supervised pretraining

### Radiologist-AI Collaboration
- AI as second reader or triage/worklist prioritisation tool
- Studies: human-AI team outperforms either alone
- Alert fatigue: too many alerts reduce compliance; need calibrated specificity thresholds

### Regulatory Framework
- FDA: 510(k) or De Novo for SaMD; analytical + clinical validation required
- EU MDR 2017/745: clinical evidence, post-market surveillance, ISO 13485 QMS
- Locked algorithm vs. adaptive/continuously-learning: additional requirements for latter

---

## 7. Medical NLP

### Clinical Text Terminologies
- ICD-10: disease classification (70,000+ codes) — billing, epidemiology
- SNOMED-CT: clinical concepts (350,000+ terms) — semantic interoperability
- LOINC: lab observations; RxNorm: medications; UMLS: meta-thesaurus

### NLP Challenges in Clinical Text
- Abbreviations/jargon ("SOB" = shortness of breath)
- Negation ("no evidence of..."); uncertainty ("cannot exclude...")
- Temporal expressions ("3 days ago", "since 2018")
- Implicit information

### De-identification
- PHI: names, dates, phone numbers, locations, MRN, biometrics
- Methods: rule-based regex; NER-based (BiLSTM-CRF, BERT); synthetic replacement
- Regulations: HIPAA Safe Harbor (18 identifiers); GDPR pseudonymisation/anonymisation

### NLP Applications
- **NER for clinical text**: BioBERT/ClinicalBERT for disease/medication/procedure extraction
- **Relation extraction**: (aspirin) -[treats]-> (chest pain)
- **Report classification**: structure radiology impressions; population studies
- **Clinical summarisation**: extractive (TextRank) vs. abstractive (BART, T5); safety concerns
- **Medical chatbots**: symptom checkers, chronic disease coaching; LLM-based with hallucination risks

---

## 8. Medical Robotics and IoMT

### IoMT
- Consumer wearables: smartwatches (ECG, SpO2), CGMs, smart inhalers
- Clinical remote monitoring: patch ECG, implantable loop recorders, remote ICU
- AI: arrhythmia detection (FDA-cleared Apple Watch); fall detection
- Pipeline: edge processing → gateway → cloud → clinician alert

### Cybersecurity
- Constraints: legacy OS, limited patching, constrained compute
- Threats: ransomware, insulin pump/pacemaker spoofing
- Defences: network segmentation, ML-based anomaly detection, encrypted firmware
- Standards: IEC 62443, FDA guidance on premarket cybersecurity

### Surgical Robotics (da Vinci)
- Surgeon console + patient-side cart (4 arms) + EndoWrist instruments + 3D vision
- 7 DoF instruments; motion scaling and tremor filtering
- Benefits: reduced blood loss, shorter stay, improved dexterity
- Limitation: limited haptic feedback, high cost

### Navigation and Registration
- Pre-operative image to intraoperative space registration
- Tracking: optical (IR + reflective markers) or electromagnetic
- AR overlay: project anatomy on surgical field
- AI phase recognition: CNN on laparoscopic video (Cholec80 dataset)

---

## 9. Ethics, Regulation, and Fairness

### GDPR and Health Data
- Special Category data (Art. 9): explicit consent or other legal basis required
- Pseudonymisation vs. anonymisation
- Data minimisation, purpose limitation, storage limits
- DPIA mandatory for high-risk AI health applications

### Federated Learning
- Train locally at each hospital; share only gradients
- FedAvg aggregation; FedProx for heterogeneous data
- Gradient inversion attacks → add differential privacy noise
- Formula: w* = argmin Σ (n_k/n) L_k(w)

### Privacy-Preserving ML
- Federated learning, differential privacy (ε-DP), secure MPC, homomorphic encryption, synthetic data
- Trade-offs: accuracy, communication cost, computational cost

### Bias Sources
- Dataset bias: demographic underrepresentation
- Label bias: historical clinical inequalities encoded in training labels
- Deployment shift: train on academic hospital, deploy in community setting
- Proxy variables: zip code, insurance type encoding race/SES

### Racial Identity in Medical Images
- Banerjee et al. (2021): DL models predict race from X-ray/CT/MRI with high accuracy
- Holds even on images degraded beyond human readability
- Implication: model may silently use race as feature; fairness audits needed

### Fairness Metrics
- Equalised odds: equal TPR and FPR across groups
- Predictive parity: equal PPV across groups
- Calibration: predicted probabilities match actual frequencies across groups
- Individual fairness: similar inputs → similar outputs
- Multiple metrics are mutually incompatible (Chouldechova's impossibility result)

### Explainability
- Grad-CAM: saliency heatmap from final conv layer gradients
- LIME: local linear surrogate
- SHAP: Shapley values with efficiency/symmetry/dummy/additivity axioms
- Clinical need: trust, error detection, regulation (EU AI Act High Risk, GDPR Art. 22)

---

## Key References Added to bibliography/references.bib

1. `brownArtificialIntelligenceDrugDiscovery2020` — Brown (2020), Royal Society of Chemistry
2. `jumperHighlyAccurateProtein2021` — AlphaFold 2, Nature 2021
3. `blassDrugDiscoveryDevelopment2015` — Blass (2015), Academic Press
4. `bocciaPersonalisedHealthCare2020` — Boccia et al. (2020), Springer
5. `estevaSkincancerDeepNeural2017` — Esteva et al. (2017), Nature
6. `gulshankumarRetinalFundusImages2016` — Gulshan et al. (2016), JAMA
7. `ronnebergerUnetConvolutionalNetworks2015` — U-Net, MICCAI 2015
8. `bushbergEssentialPhysicsMedicalImaging2020` — Bushberg et al. (2020), Wolters Kluwer
9. `smithIntroductionMedicalImaging2010` — Smith & Webb (2010), CUP
10. `banerjeeReadingRaceAI2021` — Banerjee et al. (2021), arXiv
11. `challenArtificialIntelligenceBias2019` — Challen et al. (2019), BMJ Q&S
12. `selvarajuGradCAMVisualExplanations2017` — Grad-CAM, ICCV 2017
13. `molnarInterpretableMachineLearning2019` — Molnar (2019), Lulu
14. `itgovernanceprivacyteamEUGDPR2020` — IT Gov Privacy Team (2020)
15. `juhnArtificialIntelligenceNLP2020` — Juhn & Liu (2020), J Allergy Clin Immunol
16. `schweikardMedicalRobotics2015` — Schweikard & Ernst (2015), Springer
17. `cardonaInternetMedicalThings2021` — Cardona et al. (2021), CRC Press
18. `mccradddenPatientSafetyQuality2020` — McCradden et al. (2020), JAMIA
19. `liTwoDecadesFederated2020` — Li et al. (2020), IEEE Signal Processing Magazine
20. `sorinDeepLearningNLP2020` — Sorin et al. (2020), JACR
21. `costigliolaHealthcareOverviewNew2012` — Costigliola ed. (2012), Springer
