from backend.services.preprocessing import extract_urls, extract_sender_domain, subdomain_count, uppercase_ratio
from backend.services.attachment_analyzer import DANGEROUS_EXTENSIONS

def extract_email_features(sender, subject, body, attachment_name=""):
    text = f"{subject or ''}\n{body or ''}"
    urls = extract_urls(text)
    domain = extract_sender_domain(sender)
    lower = text.lower()
    attachment = (attachment_name or "").lower()
    return {
        "urgent_keyword_count": sum(k in lower for k in ["urgent", "immediately", "act now", "expires today"]),
        "credential_keyword_count": sum(k in lower for k in ["password", "verify your account", "login", "credential", "otp"]),
        "financial_keyword_count": sum(k in lower for k in ["payment", "invoice", "refund", "bank", "transfer"]),
        "threat_keyword_count": sum(k in lower for k in ["suspended", "blocked", "locked", "terminated"]),
        "url_count": len(urls),
        "suspicious_url_count": sum(1 for u in urls if "http://" in u.lower() or any(k in u.lower() for k in ["verify", "login", "password"])),
        "has_ip_url": int(any(re.search(r"https?://\d{1,3}(?:\.\d{1,3}){3}", u) for u in urls)),
        "has_shortened_url_pattern": int(any(short in u.lower() for u in urls for short in ["bit.ly/", "tinyurl.com/", "t.co/"])),
        "sender_domain_length": len(domain),
        "subdomain_count": subdomain_count(domain),
        "suspicious_attachment": int(any(attachment.endswith(ext) for ext in DANGEROUS_EXTENSIONS)),
        "generic_greeting": int(any(g in lower for g in ["dear user", "dear customer", "valued customer"])),
        "contains_password_request": int("password" in lower),
        "contains_personal_info_request": int(any(x in lower for x in ["personal details", "date of birth", "confirm your details"])),
        "exclamation_count": text.count("!"),
        "uppercase_ratio": uppercase_ratio(text),
        "body_length": len(body or ""),
        "subject_length": len(subject or ""),
    }
