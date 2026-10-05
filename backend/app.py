from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database import Base, engine
from backend.routes.analysis import router as analysis_router
from backend.routes.dashboard import router as dashboard_router
from backend.models.analysis import Analysis, Indicator, URLAnalysis  # noqa: F401

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Phishing Email Detection & Awareness Dashboard",
    version="1.0.0",
    description="Defensive, explainable phishing analysis using synthetic or authorized email data.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analysis_router)
app.include_router(dashboard_router)

@app.get("/")
def root():
    return {"status": "ok", "service": "phishing-detection-dashboard"}

@app.get("/health")
def health():
    return {"status": "healthy"}
