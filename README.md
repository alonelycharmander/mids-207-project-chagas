# ECG-Based Chagas Disease Detection: A Machine Learning Approach Using PhysioNet Data

## Overview

This repository supports our project for **MIDS 207 – Section 08**, in which we develop machine learning algorithms to automatically detect **Chagas disease** using 12-lead ECG recordings. The project is part of the **George B. Moody PhysioNet Challenge 2025**.

## Team Members

| Name               | Email                                     |
|--------------------|--------------------------------------------|
| Marcelino Bautista | marcelino_bautista@berkeley.edu            |
| Jonah Karpman      | jonahkarpman@ischool.berkeley.edu          |
| Claire Peng        | claire_peng@ischool.berkeley.edu           |
| Tim Platz          | tim.x.platz@ischool.berkeley.edu           |
| River Jiang        | river.jiang@ischool.berkeley.edu           |

---

## Motivation

Chagas disease affects **6.5 million people** in Central and South America and causes ~10,000 deaths annually. Diagnosis is typically based on serological testing, which is limited in availability. However, ECG abnormalities caused by Chagas-induced cardiomyopathy offer an opportunity for AI-assisted screening using widely available and inexpensive ECG recordings.

This project aims to:
- Predict Chagas disease presence using 12-lead ECGs.
- Provide both binary classification and probability scores.
- Prioritize patients for confirmatory testing.
- Benchmark performance via the PhysioNet Challenge evaluation criteria, focusing on **true positive rate among the top 5% predictions**.

---

## Data Sources

We will use three key datasets provided by the PhysioNet Challenge 2025:

- **[CODE-15% Dataset](https://zenodo.org/records/4916206)**  
  ~300,000 ECGs from Brazil (2010–2016) with self-reported Chagas labels.  
  12-lead, 7.3–10.2s at 400 Hz.

- **[SaMi-Trop Dataset](https://zenodo.org/records/4905618)**  
  1,631 ECGs from confirmed Chagas patients.  
  12-lead, 7.3–10.2s at 400 Hz, serologically validated.

- **[PTB-XL Dataset](https://physionet.org/content/ptb-xl/1.0.3/)**  
  21,799 ECGs from European patients, considered Chagas-negative due to geographic region.  
  12-lead, 10s at 500 Hz.

All datasets use **WFDB format** with metadata including patient demographics and Chagas status.

---

## Generalization Challenge

The **validation and test sets** contain ECGs from hospitals and regions excluded from the training data. Our models must generalize across different:
- Locations
- Equipment
- Data collection methods

---

## Related Work

- A recent study by Swedish and Brazilian researchers achieved **36–52% sensitivity** in detecting Chagas via ECG using machine learning:  
  [PubMed Link](https://pubmed.ncbi.nlm.nih.gov/37399207/)

- Brito et al. (2021) developed an AI-enabled ECG model to detect **LVSD** in Chagas patients:  
  [PubMed Link](https://pubmed.ncbi.nlm.nih.gov/34871321/)

These works validate the feasibility and impact of ECG-based machine learning for Chagas-related cardiac abnormalities.

---

## Repository Structure

```bash
.
├── data/                   # Scripts or links for data access/preprocessing
├── notebooks/              # Exploratory and training notebooks
├── models/                 # Model definitions and training logic
├── results/                # Outputs and evaluation results
├── README.md
└── requirements.txt        # Dependencies
