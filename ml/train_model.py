from pathlib import Path
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "phishing_email_dataset.csv"
MODEL = ROOT / "models" / "phishing_tfidf.joblib"

if not DATA.exists():
    raise SystemExit("Dataset not found. Run: python data/generate_dataset.py")

df = pd.read_csv(DATA)
text = (df["subject"].fillna("") + " " + df["body"].fillna(""))
y = (df["label"] == "PHISHING").astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    text, y, test_size=0.25, random_state=42, stratify=y
)

model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=1)),
    ("clf", LogisticRegression(max_iter=1000, random_state=42)),
])

model.fit(X_train, y_train)
pred = model.predict(X_test)

print("Accuracy :", round(accuracy_score(y_test, pred), 4))
print("Precision:", round(precision_score(y_test, pred, zero_division=0), 4))
print("Recall   :", round(recall_score(y_test, pred, zero_division=0), 4))
print("F1       :", round(f1_score(y_test, pred, zero_division=0), 4))
print("Confusion matrix:")
print(confusion_matrix(y_test, pred))

MODEL.parent.mkdir(exist_ok=True)
joblib.dump(model, MODEL)
print(f"Saved model: {MODEL}")
