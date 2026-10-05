from backend.services.preprocessing import uppercase_ratio

URGENCY = ["urgent", "immediately", "act now", "as soon as possible", "expires today"]
FEAR = ["suspended", "terminated", "blocked", "locked", "security alert", "legal action"]
FINANCIAL = ["payment", "invoice", "refund", "bank", "transfer", "outstanding", "wire"]
CREDENTIALS = ["password", "verify your account", "login", "sign in", "credential", "otp", "one-time code"]
PERSONAL = ["personal details", "date of birth", "address", "social security", "identity", "confirm your details"]
REWARD = ["you have won", "winner", "prize", "reward", "claim your"]
GENERIC = ["dear user", "dear customer", "valued customer", "dear member"]

def _hits(text, words):
    lower = text.lower()
    return [w for w in words if w in lower]

def analyze_email_content(subject: str, body: str):
    text = f"{subject or ''}\n{body or ''}"
    findings = []
    features = {}

    for name, words, label in [
        ("urgency", URGENCY, "Urgent language detected."),
        ("fear", FEAR, "Threat or fear language detected."),
        ("financial", FINANCIAL, "Financial-pressure language detected."),
        ("credentials", CREDENTIALS, "Credential or account-verification language detected."),
        ("personal_info", PERSONAL, "Personal-information request language detected."),
        ("reward", REWARD, "Reward or prize language detected."),
        ("generic_greeting", GENERIC, "Generic greeting detected."),
    ]:
        hits = _hits(text, words)
        features[f"{name}_keyword_count"] = len(hits)
        if name == "credentials":
            features["credential_keyword_count"] = len(hits)
        if hits:
            findings.append(f"{label} Matches: {', '.join(hits[:5])}.")

    features["exclamation_count"] = text.count("!")
    features["uppercase_ratio"] = round(uppercase_ratio(text), 3)
    features["body_length"] = len(body or "")
    features["subject_length"] = len(subject or "")

    if features["exclamation_count"] >= 3:
        findings.append("Multiple exclamation marks detected.")
    if features["uppercase_ratio"] >= 0.45 and len(text) >= 20:
        findings.append("High uppercase ratio detected.")
    if not (body or "").strip():
        findings.append("Email body is empty.")
    if not (subject or "").strip():
        findings.append("Email subject is empty.")

    return findings, features
