import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

BASE = Path("data/processed")
MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE / "final_dataset.csv")

X = df[["Binding", "TFIDF", "BioBERT"]]
y = df["Label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

rf = RandomForestClassifier(n_estimators=200)
rf.fit(X_train, y_train)

ann = MLPClassifier(hidden_layer_sizes=(64,32), max_iter=300)
ann.fit(X_train, y_train)

# SAVE
joblib.dump(rf, MODEL_DIR / "rf_model.pkl")
joblib.dump(ann, MODEL_DIR / "ann_model.pkl")

# PRINT ACCURACY
print("RF Accuracy:", accuracy_score(y_test, rf.predict(X_test)))
print("ANN Accuracy:", accuracy_score(y_test, ann.predict(X_test)))