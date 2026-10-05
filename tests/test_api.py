import os
os.environ["DATABASE_URL"] = "sqlite:///./test.db"

from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_url_endpoint():
    response = client.post("/api/analyze/url", json={"url": "https://example.org/help"})
    assert response.status_code == 200
    assert "risk_score" in response.json()

def test_email_analysis():
    response = client.post("/api/analyze", json={
        "sender": "training@example.org",
        "subject": "Cybersecurity Workshop Reminder",
        "body": "This is a normal informational reminder.",
        "attachment_name": ""
    })
    assert response.status_code == 200
    assert "classification" in response.json()
