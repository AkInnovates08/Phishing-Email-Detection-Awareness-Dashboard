from typing import List, Optional
from pydantic import BaseModel, Field

class AnalyzeRequest(BaseModel):
    sender: str = Field(default="", max_length=500)
    subject: str = Field(default="", max_length=500)
    body: str = Field(default="", max_length=20000)
    attachment_name: Optional[str] = Field(default="", max_length=255)

class URLRequest(BaseModel):
    url: str = Field(min_length=1, max_length=3000)

class IndicatorOut(BaseModel):
    indicator_type: str
    description: str
    severity: str

class URLFindingOut(BaseModel):
    url: str
    risk_score: float
    findings: List[str]

class AnalysisResponse(BaseModel):
    analysis_id: int
    risk_score: float
    classification: str
    sender_findings: List[str]
    content_findings: List[str]
    attachment_findings: List[str]
    url_results: List[URLFindingOut]
    indicators: List[IndicatorOut]
    recommendations: List[str]
    ml_probability: Optional[float] = None

class HistoryItem(BaseModel):
    analysis_id: int
    sender_domain: str
    subject: str
    risk_score: float
    classification: str
    created_at: str

class DashboardStats(BaseModel):
    total_emails: int
    likely_phishing: int
    suspicious: int
    low_risk: int
    average_risk_score: float
