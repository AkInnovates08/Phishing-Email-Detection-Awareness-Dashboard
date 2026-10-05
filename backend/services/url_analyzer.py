import ipaddress
import re
from urllib.parse import urlparse

SHORTENER_PATTERNS = {
    "bit.ly", "tinyurl.com", "t.co", "is.gd", "ow.ly", "buff.ly", "cutt.ly"
}
SUSPICIOUS_KEYWORDS = {
    "verify", "login", "signin", "password", "credential", "secure", "update",
    "payment", "invoice", "account", "confirm", "unlock", "reset"
}

def analyze_url(url: str):
    findings = []
    score = 0
    raw = (url or "").strip()
    try:
        parsed = urlparse(raw)
    except ValueError:
        return {"url": raw, "risk_score": 30, "findings": ["URL could not be parsed safely."]}

    scheme = parsed.scheme.lower()
    host = (parsed.hostname or "").lower()
    path_query = f"{parsed.path}?{parsed.query}".lower()

    if scheme != "https":
        findings.append("URL does not use HTTPS.")
        score += 10

    try:
        ipaddress.ip_address(host)
        findings.append("Hostname is a raw IP address.")
        score += 20
    except ValueError:
        pass

    if len(raw) > 120:
        findings.append("URL is unusually long.")
        score += 5

    if len(host) > 50:
        findings.append("Hostname is unusually long.")
        score += 5

    subdomains = max(0, len(host.split(".")) - 2) if host else 0
    if subdomains >= 3:
        findings.append("Hostname contains many subdomains.")
        score += 5

    if host in SHORTENER_PATTERNS:
        findings.append("URL matches a common shortening-service hostname.")
        score += 10

    hits = sorted(k for k in SUSPICIOUS_KEYWORDS if k in path_query)
    if hits:
        findings.append(f"Security-sensitive keywords appear in the URL: {', '.join(hits[:6])}.")
        score += min(15, 3 * len(hits))

    if any(ch in raw for ch in ["@", "\\", "{", "}", "<", ">"]):
        findings.append("URL contains unusual characters.")
        score += 5

    return {
        "url": raw,
        "risk_score": min(score, 100),
        "findings": findings,
        "scheme": scheme,
        "hostname": host,
        "path": parsed.path,
        "query": parsed.query,
    }
