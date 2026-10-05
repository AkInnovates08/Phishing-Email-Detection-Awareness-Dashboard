DANGEROUS_EXTENSIONS = {
    ".exe", ".scr", ".bat", ".cmd", ".js", ".vbs", ".ps1", ".jar", ".msi"
}
ARCHIVE_EXTENSIONS = {".zip", ".rar", ".7z", ".iso"}

def analyze_attachment(filename: str):
    filename = (filename or "").strip().lower()
    findings = []
    score = 0

    if not filename:
        return {"risk_score": 0, "findings": []}

    parts = filename.split(".")
    if len(parts) >= 3:
        last_two = ".".join(parts[-2:])
        if any(last_two.endswith(ext) for ext in DANGEROUS_EXTENSIONS):
            findings.append("Double-extension pattern detected.")
            score += 25

    extension = "." + parts[-1] if len(parts) > 1 else ""
    if extension in DANGEROUS_EXTENSIONS:
        findings.append(f"Potentially executable/script attachment extension: {extension}.")
        score += 25
    elif extension in ARCHIVE_EXTENSIONS:
        findings.append(f"Archive attachment requires caution: {extension}.")
        score += 10

    return {"risk_score": min(score, 100), "findings": findings}
