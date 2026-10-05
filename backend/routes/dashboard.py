from collections import Counter
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models.analysis import Analysis, Indicator

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])

@router.get("/stats")
def stats(db: Session = Depends(get_db)):
    rows = db.query(Analysis).all()
    total = len(rows)
    likely = sum(r.classification.startswith("HIGH RISK") for r in rows)
    suspicious = sum(r.classification == "SUSPICIOUS" for r in rows)
    low = sum(r.classification in {"LOW RISK", "MODERATE RISK"} for r in rows)
    avg = round(sum(r.risk_score for r in rows) / total, 2) if total else 0
    return {
        "total_emails": total,
        "likely_phishing": likely,
        "suspicious": suspicious,
        "low_risk": low,
        "average_risk_score": avg,
    }

@router.get("/indicators")
def indicators(db: Session = Depends(get_db)):
    rows = db.query(Indicator).all()
    counts = Counter(r.indicator_type for r in rows)
    return [{"indicator": k, "count": v} for k, v in counts.most_common(10)]
