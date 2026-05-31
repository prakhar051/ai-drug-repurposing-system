import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

st.set_page_config(
    page_title="AI Drug Repurposing System",
    layout="wide"
)

st.title("AI Drug Repurposing System")
st.write("AI-powered Drug Repurposing Dashboard")

DATA_FILE = Path("data/processed/demo_results.csv")

df = pd.read_csv(DATA_FILE)

# Metrics
col1, col2 = st.columns(2)

col1.metric("Total Drugs", df["Drug"].nunique())
col2.metric("Total Diseases", df["Disease"].nunique())

# Table
st.subheader("Prediction Results")
st.dataframe(df)

# Effectiveness Chart
st.subheader("Drug Effectiveness Comparison")

fig1, ax1 = plt.subplots(figsize=(10,6))

sns.barplot(
    data=df,
    x="Disease",
    y="Effectiveness %",
    hue="Drug",
    ax=ax1
)

plt.xticks(rotation=30)

st.pyplot(fig1)

# Heatmap
st.subheader("Drug-Disease Heatmap")

pivot = df.pivot(
    index="Drug",
    columns="Disease",
    values="Effectiveness %"
)

fig2, ax2 = plt.subplots(figsize=(8,6))

sns.heatmap(
    pivot,
    annot=True,
    cmap="coolwarm",
    ax=ax2
)

st.pyplot(fig2)

# Ranking
st.subheader("Best Drug Recommendation Per Disease")

ranking = (
    df
    .sort_values("Effectiveness %", ascending=False)
    .groupby("Disease")
    .first()
    .reset_index()
)

st.dataframe(
    ranking[
        ["Disease", "Drug", "Effectiveness %"]
    ]
)

# Ranking Chart
st.subheader("Top Drug Effectiveness")

fig3, ax3 = plt.subplots(figsize=(8,5))

sns.barplot(
    data=ranking,
    x="Disease",
    y="Effectiveness %",
    hue="Drug",
    ax=ax3
)

plt.xticks(rotation=30)

st.pyplot(fig3)

# Model Comparison
st.subheader("Model Evaluation")

model_df = pd.DataFrame({
    "Model": ["Random Forest", "ANN"],
    "Score": [60.8, 48.5]
})

fig4, ax4 = plt.subplots()

sns.barplot(
    data=model_df,
    x="Model",
    y="Score",
    ax=ax4
)

st.pyplot(fig4)

# Download
csv = df.to_csv(index=False).encode()

st.download_button(
    "Download Results CSV",
    csv,
    "drug_repurposing_results.csv",
    "text/csv"
)