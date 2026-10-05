from backend.services.url_analyzer import analyze_url
from backend.services.sender_analyzer import analyze_sender
from backend.services.content_analyzer import analyze_email_content
from backend.services.attachment_analyzer import analyze_attachment
from backend.services.risk_engine import calculate_phishing_score

def test_safe_url():
    result = analyze_url("https://example.org/help")
    assert result["risk_score"] == 0

def test_raw_ip_url():
    result = analyze_url("http://198.51.100.10/verify-account")
    assert result["risk_score"] >= 30
    assert any("raw IP" in x for x in result["findings"])

def test_sender():
    result = analyze_sender("security-alert@account-check.invalid.test")
    assert result["sender_domain"] == "account-check.invalid.test"

def test_content():
    findings, features = analyze_email_content(
        "URGENT: Verify",
        "Immediately verify your password or account will be suspended."
    )
    assert features["urgency_keyword_count"] > 0
    assert features["credential_keyword_count"] > 0
    assert findings

def test_attachment():
    result = analyze_attachment("invoice.pdf.exe")
    assert result["risk_score"] >= 25

def test_risk_engine():
    sender = {"sender_risk_score": 20, "sender_findings": ["test"]}
    content = {
        "urgency_keyword_count": 1,
        "credential_keyword_count": 1,
        "generic_greeting": 1,
        "threat_keyword_count": 1,
    }
    urls = [{"risk_score": 40, "findings": ["raw IP"]}]
    attachment = {"risk_score": 25, "findings": ["double extension"]}
    result = calculate_phishing_score(sender, content, urls, attachment)
    assert result["risk_score"] == 100
    assert result["classification"].startswith("HIGH RISK")
