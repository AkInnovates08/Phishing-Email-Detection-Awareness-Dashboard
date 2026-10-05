from pathlib import Path
import joblib

MODEL_PATH = Path(__file__).resolve().parent.parent.parent / "models" / "phishing_tfidf.joblib"

def predict_probability(subject: str, body: str):
    if not MODEL_PATH.exists():
        return None
    try:
        model = joblib.load(MODEL_PATH)
        text = f"{subject or ''} {body or ''}"
        probability = float(model.predict_proba([text])[0][1])
        return round(probability, 4)
    except Exception:
        return None
