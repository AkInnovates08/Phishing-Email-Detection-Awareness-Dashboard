from pathlib import Path
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "phishing_email_dataset.csv"
MODEL = ROOT / "models" / "phishing_tfidf.joblib"

df = pd.read_csv(DATA)
text = df["subject"].fillna("") + " " + df["body"].fillna("")
y = (df["label"] == "PHISHING").astype(int)
_, X_test, _, y_test = train_test_split(text, y, test_size=0.25, random_state=42, stratify=y)

model = joblib.load(MODEL)
pred = model.predict(X_test)

print(classification_report(y_test, pred, target_names=["LEGITIMATE", "PHISHING"], zero_division=0))
print("Confusion matrix:")
print(confusion_matrix(y_test, pred))
