from pathlib import Path
import joblib

MODEL = Path(__file__).resolve().parent.parent / "models" / "phishing_tfidf.joblib"

def predict(subject: str, body: str):
    model = joblib.load(MODEL)
    text = f"{subject} {body}"
    probability = float(model.predict_proba([text])[0][1])
    label = "PHISHING" if probability >= 0.5 else "LEGITIMATE"
    return {"label": label, "phishing_probability": round(probability, 4)}
