# AI Drug Repurposing System

AI-powered Drug Repurposing Platform that combines Machine Learning, Biomedical NLP, BioBERT embeddings, TF-IDF literature mining, and binding affinity prediction to identify potential drug candidates for infectious and bacterial diseases.

---

# Live Demo

🔗 https://ai-drug-repurposing-system-nadwtvmzox96xcpvytrnjh.streamlit.app

---

# Overview

Drug repurposing is the process of identifying new therapeutic applications for existing drugs. Traditional drug discovery is expensive and time-consuming, making AI-assisted repurposing an important research direction.

This project integrates Machine Learning, Biomedical Literature Mining, Semantic Similarity Analysis, and Predictive Modeling to estimate the effectiveness of existing drugs against multiple infectious diseases.

The platform analyzes drug-disease relationships using TF-IDF vectorization, BioBERT embeddings, Random Forest models, and Artificial Neural Networks (ANN) to generate disease-specific drug rankings and comparative analytics.

---

# Features

✅ Multi-Drug Analysis
✅ Disease-Specific Effectiveness Prediction
✅ Drug Ranking Engine
✅ TF-IDF Literature Similarity Scoring
✅ BioBERT Semantic Analysis
✅ Binding Affinity Prediction
✅ Interactive Streamlit Dashboard
✅ Drug-Disease Heatmap Visualization
✅ Comparative Model Analytics
✅ CSV Result Export
✅ Biomedical Dataset Integration

---

# Tech Stack

## Frontend

* Streamlit

## Backend

* Python

## Machine Learning

* Scikit-Learn
* Random Forest Regressor
* Artificial Neural Network (ANN)

## NLP & Semantic Analysis

* TF-IDF Vectorization
* BioBERT
* Sentence Transformers

## Data Processing

* Pandas
* NumPy

## Visualization

* Matplotlib
* Seaborn

---

# Datasets Used

* BindingDB
* DrugBank
* ChEMBL
* PubMed

---

# System Architecture

```text
Drug Input
    ↓
TF-IDF Literature Mining
    ↓
BioBERT Semantic Similarity Analysis
    ↓
Binding Affinity Prediction
    ↓
Machine Learning Evaluation
    ↓
Score Aggregation
    ↓
Drug Ranking Engine
    ↓
Visualization Dashboard
```

---

# Workflow

1. User selects or inputs a drug candidate.
2. Biomedical literature is processed using TF-IDF vectorization.
3. BioBERT embeddings generate semantic similarity relationships.
4. Binding affinity prediction models estimate effectiveness.
5. Random Forest and ANN models evaluate prediction scores.
6. Scores are aggregated and ranked disease-wise.
7. Results are visualized through interactive dashboards and heatmaps.

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

# Challenges Faced

* Processing large biomedical datasets efficiently
* Managing BioBERT embedding computations
* Optimizing semantic similarity workflows
* Balancing prediction accuracy with processing time
* Integrating multiple biomedical datasets into a unified pipeline

---

# Current Limitations

* Predictions are research-oriented and not clinically validated
* Limited dataset availability for certain diseases
* BioBERT inference can increase processing time for large-scale analysis
* Model accuracy can improve with larger biomedical datasets

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

# Production Improvements

* Graph Neural Networks (GNN)
* Molecular Fingerprint Features
* Knowledge Graph Visualization
* Real-Time PubMed Integration
* Clinical Trial Validation
* Transformer-Based Drug Discovery Models
* Explainable AI Dashboard

---

# Resume Highlights

* Built an AI-powered Drug Repurposing Platform using Machine Learning and Biomedical NLP techniques.
* Implemented TF-IDF and BioBERT for biomedical literature mining and semantic similarity analysis.
* Developed Random Forest and ANN models for binding affinity and effectiveness prediction.
* Designed an interactive Streamlit dashboard with heatmaps, ranking systems, and comparative analytics.
* Integrated biomedical datasets including BindingDB, DrugBank, ChEMBL, and PubMed.
* Automated disease-specific drug ranking and recommendation workflows.

---

# Why This Project Matters

Traditional drug discovery is resource-intensive and time-consuming. This project explores how AI, Machine Learning, and Biomedical NLP can assist in accelerating early-stage drug repurposing research and decision-making for infectious diseases.

---

# Author

## Prakhar Yadav

Full Stack Developer | AI Enthusiast | Backend Developer

GitHub: https://github.com/prakhar051
