# AI Drug Repurposing System

AI-powered Drug Repurposing Platform that combines Machine Learning, BioBERT embeddings, TF-IDF literature mining, and binding affinity prediction to identify potential drug candidates for infectious diseases.

---

## Overview

Drug repurposing is the process of discovering new therapeutic applications for existing drugs.

This project integrates Machine Learning, Biomedical Literature Mining, and Semantic Similarity Analysis to estimate the effectiveness of existing drugs against multiple infectious diseases.

The platform analyzes drug-disease relationships using TF-IDF, BioBERT embeddings, Random Forest, and Artificial Neural Networks (ANN).

---

## Features

✅ Multi-Drug Analysis

✅ Disease-Specific Effectiveness Prediction

✅ Drug Ranking Engine

✅ TF-IDF Literature Similarity Scoring

✅ BioBERT Semantic Analysis

✅ Binding Affinity Prediction

✅ Interactive Streamlit Dashboard

✅ Drug-Disease Heatmap Visualization

✅ Model Comparison Analytics

✅ CSV Result Export

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Machine Learning

* Scikit-Learn
* Random Forest Regressor
* Artificial Neural Network (ANN)

### NLP

* TF-IDF Vectorization
* BioBERT
* Sentence Transformers

### Data Processing

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

---

## Datasets Used

* BindingDB
* DrugBank
* ChEMBL
* PubMed

---

## Workflow

```text
Drug Input
    ↓
TF-IDF Literature Analysis
    ↓
BioBERT Semantic Similarity
    ↓
Binding Affinity Prediction
    ↓
Score Aggregation
    ↓
Drug Ranking
    ↓
Visualization Dashboard
```

---

# Application Screenshots

## Home Page

![Home Page](screenshots/home_page.png)

---

## Prediction Results

![Prediction Results](screenshots/prediction_results.png)

---

## Drug-Disease Heatmap

![Heatmap](screenshots/effectiveness_heatmap.png)

---

## Drug Effectiveness Comparison

![Effectiveness Comparison](screenshots/effectiveness_comparison.png)

---

## Model Evaluation Comparison

![Model Accuracy](screenshots/model_accuracy.png)

---

## Random Forest Evaluation

![Random Forest Accuracy](screenshots/random_forest_accuracy.png)

---

## Random Forest Performance Trend

![Random Forest Trend](screenshots/random_forest_trend.png)

---

## ANN Evaluation

![ANN Accuracy](screenshots/ann_accuracy.png)

---

## ANN Performance Trend

![ANN Trend](screenshots/ann_trend.png)

---

# Model Performance

| Model         | Evaluation Score |
| ------------- | ---------------- |
| Random Forest | 60.8%            |
| ANN           | 48.5%            |

---

# Key Outputs

The platform generates:

* Drug Effectiveness Score (%)
* Binding Affinity Score
* TF-IDF Similarity Score
* BioBERT Similarity Score
* Literature Evidence Score
* Disease-wise Drug Ranking
* Comparative Drug Analysis

---

# Installation

## Clone Repository

```bash
git clone https://github.com/prakhar051/ai-drug-repurposing-system.git
cd ai-drug-repurposing-system
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app.py
```

---

# Repository Structure

```text
ai-drug-repurposing-system/
│
├── app.py
├── backend.py
├── dataset_builder.py
├── trainer.py
├── requirements.txt
├── README.md
│
├── data/
│   └── processed/
│       ├── bindingdb_clean.csv
│       ├── chembl_clean.csv
│       ├── drugbank_clean_final.csv
│       ├── pubmed_small.csv
│       ├── pubmed_embeddings.npy
│       ├── demo_results.csv
│       └── side_effects_clean.csv
│
├── screenshots/
│   ├── home_page.png
│   ├── prediction_results.png
│   ├── effectiveness_heatmap.png
│   ├── effectiveness_comparison.png
│   ├── model_accuracy.png
│   ├── random_forest_accuracy.png
│   ├── random_forest_trend.png
│   ├── ann_accuracy.png
│   └── ann_trend.png
│
└── README.md
```

---

# Future Enhancements

* Graph Neural Networks (GNN)
* Molecular Fingerprint Features
* Knowledge Graph Visualization
* Real-Time PubMed Integration
* Clinical Trial Validation
* Transformer-Based Drug Discovery Models
* Explainable AI Dashboard

---

# Resume Highlights

* Built an AI-powered Drug Repurposing Platform using Machine Learning and NLP techniques.
* Implemented TF-IDF and BioBERT for biomedical literature mining and semantic similarity analysis.
* Developed Random Forest and ANN models for binding affinity and effectiveness prediction.
* Designed an interactive Streamlit dashboard with heatmaps, ranking panels, and comparative analytics.
* Integrated biomedical datasets including BindingDB, DrugBank, ChEMBL, and PubMed.
* Automated drug ranking and disease-specific recommendation workflows.

---

## Author

**Prakhar Yadav**

Machine Learning Engineer | AI Developer | Python Developer

GitHub: https://github.com/prakhar051
