import re
from backend.services.preprocessing import extract_sender_domain, subdomain_count

SUSPICIOUS_CHARS = re.compile(r"[^a-zA-Z0-9.\-_@ ]")
FREE_MAIL_DOMAINS = {"gmail.com", "outlook.com", "yahoo.com", "proton.me"}

def analyze_sender(sender: str, display_name: str = "", expected_domain: str = ""):
    findings = []
    score = 0
    sender = (sender or "").strip()
    domain = extract_sender_domain(sender)

    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", sender):
        findings.append("Sender address format is invalid or unusual.")
        score += 15

    if not domain:
        findings.append("No sender domain could be extracted.")
        score += 10
    else:
        if len(domain) > 45:
            findings.append("Sender domain is unusually long.")
            score += 5
        if subdomain_count(domain) >= 3:
            findings.append("Sender domain contains many subdomains.")
            score += 5
        if any(ch in domain for ch in "_%"):
            findings.append("Sender domain contains unusual characters.")
            score += 5

        if expected_domain and domain != expected_domain.lower():
            findings.append("Sender domain does not match the supplied expected domain.")
            score += 10

        if display_name:
            display_domain = display_name.lower().replace(" ", "")
            if domain and display_domain and display_domain not in domain:
                findings.append("Display name may not match the sender domain.")
                score += 10

        if domain in FREE_MAIL_DOMAINS and expected_domain:
            findings.append("Sender uses a public mail domain instead of the expected organization domain.")
            score += 5

    return {
        "sender_domain": domain,
        "sender_risk_score": min(score, 100),
        "sender_findings": findings,
    }
