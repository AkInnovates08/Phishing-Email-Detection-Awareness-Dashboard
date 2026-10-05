from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models.analysis import Analysis, Indicator, URLAnalysis
from backend.schemas import AnalyzeRequest, URLRequest
from backend.services.preprocessing import clean_text, extract_urls
from backend.services.sender_analyzer import analyze_sender
from backend.services.content_analyzer import analyze_email_content
from backend.services.url_analyzer import analyze_url
from backend.services.attachment_analyzer import analyze_attachment
from backend.services.feature_engineering import extract_email_features
from backend.services.risk_engine import calculate_phishing_score
from backend.services.ml_service import predict_probability

router = APIRouter(prefix="/api", tags=["analysis"])

@router.post("/analyze")
def analyze_email(payload: AnalyzeRequest, db: Session = Depends(get_db)):
    sender = clean_text(payload.sender)
    subject = clean_text(payload.subject)
    body = clean_text(payload.body)

    sender_result = analyze_sender(sender)
    content_findings, content_features = analyze_email_content(subject, body)
    attachment_result = analyze_attachment(payload.attachment_name or "")
    urls = extract_urls(f"{subject}\n{body}")
    url_results = [analyze_url(u) for u in urls]
    risk = calculate_phishing_score(sender_result, content_features, url_results, attachment_result)
    ml_probability = predict_probability(subject, body)

    record = Analysis(
        sender_domain=sender_result["sender_domain"],
        subject=subject,
        risk_score=risk["risk_score"],
        classification=risk["classification"],
    )
    db.add(record)
    db.flush()

    for typ, desc, sev in risk["indicators"]:
        db.add(Indicator(
            analysis_id=record.analysis_id,
            indicator_type=typ,
            description=desc,
            severity=sev,
        ))

    for result in url_results:
        db.add(URLAnalysis(
            analysis_id=record.analysis_id,
            url_safe_representation=result["url"],
            risk_score=result["risk_score"],
            findings=" | ".join(result["findings"]),
        ))

    db.commit()

    return {
        "analysis_id": record.analysis_id,
        "risk_score": risk["risk_score"],
        "classification": risk["classification"],
        "sender_findings": sender_result["sender_findings"],
        "content_findings": content_findings,
        "attachment_findings": attachment_result["findings"],
        "url_results": [
            {"url": r["url"], "risk_score": r["risk_score"], "findings": r["findings"]}
            for r in url_results
        ],
        "indicators": [
            {"indicator_type": t, "description": d, "severity": s}
            for t, d, s in risk["indicators"]
        ],
        "recommendations": risk["recommendations"],
        "ml_probability": ml_probability,
        "features": extract_email_features(sender, subject, body, payload.attachment_name or ""),
    }

@router.post("/analyze/url")
def analyze_single_url(payload: URLRequest):
    return analyze_url(payload.url)

@router.get("/analyses")
def list_analyses(db: Session = Depends(get_db)):
    rows = db.query(Analysis).order_by(Analysis.created_at.desc()).limit(200).all()
    return [
        {
            "analysis_id": r.analysis_id,
            "sender_domain": r.sender_domain,
            "subject": r.subject,
            "risk_score": r.risk_score,
            "classification": r.classification,
            "created_at": r.created_at.isoformat(),
        }
        for r in rows
    ]

@router.get("/analyses/{analysis_id}")
def get_analysis(analysis_id: int, db: Session = Depends(get_db)):
    row = db.query(Analysis).filter(Analysis.analysis_id == analysis_id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Analysis not found.")
    return {
        "analysis_id": row.analysis_id,
        "sender_domain": row.sender_domain,
        "subject": row.subject,
        "risk_score": row.risk_score,
        "classification": row.classification,
        "created_at": row.created_at.isoformat(),
        "indicators": [
            {
                "indicator_type": x.indicator_type,
                "description": x.description,
                "severity": x.severity,
            } for x in row.indicators
        ],
        "urls": [
            {
                "url": x.url_safe_representation,
                "risk_score": x.risk_score,
                "findings": [f for f in x.findings.split(" | ") if f],
            } for x in row.urls
        ],
    }

@router.delete("/analyses/{analysis_id}")
def delete_analysis(analysis_id: int, db: Session = Depends(get_db)):
    row = db.query(Analysis).filter(Analysis.analysis_id == analysis_id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Analysis not found.")
    db.delete(row)
    db.commit()
    return {"status": "deleted", "analysis_id": analysis_id}
