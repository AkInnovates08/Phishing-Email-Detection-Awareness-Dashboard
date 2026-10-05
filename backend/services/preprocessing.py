import re
from urllib.parse import urlparse

URL_RE = re.compile(r"https?://[^\s<>'\"]+", re.I)

def clean_text(text: str) -> str:
    # Keep punctuation and URLs because they can be useful evidence.
    return re.sub(r"\s+", " ", (text or "").strip())

def extract_urls(text: str):
    return [u.rstrip(".,);]}>") for u in URL_RE.findall(text or "")]

def extract_sender_domain(sender: str) -> str:
    sender = (sender or "").strip()
    if "@" not in sender:
        return ""
    return sender.rsplit("@", 1)[1].lower()

def subdomain_count(hostname: str) -> int:
    if not hostname:
        return 0
    parts = hostname.split(".")
    return max(0, len(parts) - 2)

def extract_attachment_extension(filename: str) -> str:
    filename = (filename or "").lower().strip()
    if "." not in filename:
        return ""
    return "." + filename.rsplit(".", 1)[1]

def uppercase_ratio(text: str) -> float:
    letters = [c for c in (text or "") if c.isalpha()]
    if not letters:
        return 0.0
    return sum(c.isupper() for c in letters) / len(letters)

def count_keywords(text: str, keywords):
    lower = (text or "").lower()
    return sum(lower.count(k.lower()) for k in keywords)
