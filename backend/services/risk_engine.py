def calculate_phishing_score(sender_result, content_features, url_results, attachment_result):
    score = 0
    reasons = []
    indicators = []

    if sender_result["sender_risk_score"] > 0:
        score += 15
        indicators.append(("sender", "Suspicious sender pattern detected.", "medium"))
        reasons.append("Sender analysis produced risk findings.")

    if content_features.get("urgency_keyword_count", 0) > 0:
        score += 10
        indicators.append(("urgency", "Urgent language detected.", "medium"))

    if content_features.get("credential_keyword_count", 0) > 0:
        score += 20
        indicators.append(("credential_request", "Credential/account-verification language detected.", "high"))

    if any(r["risk_score"] >= 15 for r in url_results):
        score += 20
        indicators.append(("suspicious_url", "One or more URLs have elevated static risk.", "high"))

    if attachment_result["risk_score"] > 0:
        score += 25
        indicators.append(("attachment", "Attachment filename requires caution.", "high"))

    if content_features.get("generic_greeting", 0):
        score += 5
        indicators.append(("generic_greeting", "Generic greeting detected.", "low"))

    if content_features.get("threat_keyword_count", 0) > 0:
        score += 10
        indicators.append(("threat", "Threat/fear language detected.", "high"))

    score = min(100, score)

    if score <= 20:
        classification = "LOW RISK"
    elif score <= 40:
        classification = "MODERATE RISK"
    elif score <= 70:
        classification = "SUSPICIOUS"
    else:
        classification = "HIGH RISK / LIKELY PHISHING"

    recommendations = []
    if score >= 41:
        recommendations.extend([
            "Do not click links in the message.",
            "Do not open unexpected attachments.",
            "Verify the sender through a trusted channel.",
            "Use the organization's official website or application directly.",
            "Report the message to the security team if appropriate.",
        ])
    else:
        recommendations.extend([
            "Still verify unexpected requests before acting.",
            "Avoid sharing credentials or sensitive information by email.",
        ])

    return {
        "risk_score": score,
        "classification": classification,
        "indicators": indicators,
        "recommendations": recommendations,
    }
