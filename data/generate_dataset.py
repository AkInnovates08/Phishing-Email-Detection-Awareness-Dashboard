from pathlib import Path
import csv
import random

random.seed(42)
OUT = Path(__file__).resolve().parent / "phishing_email_dataset.csv"

legitimate = [
    ("training@example.org", "Cybersecurity Workshop Reminder", "This is a reminder about the cybersecurity workshop. No action is required."),
    ("hr@example.com", "HR Project Update", "The monthly project update is available for review during normal business hours."),
    ("university@example.edu", "University Notice", "The semester timetable has been published on the university portal."),
    ("newsletter@example.net", "Monthly Newsletter", "Here is the monthly newsletter with community updates and upcoming events."),
    ("shopping@example.com", "Order Confirmation", "Your fictional order has been recorded. Please review the confirmation in your account."),
    ("security@example.org", "Password Change Confirmation", "Your password was changed successfully. If you made this change, no further action is required."),
    ("meetings@example.org", "Meeting Reminder", "This is a reminder for the project meeting scheduled for tomorrow."),
]

phishing = [
    ("security-alert@account-check.invalid.test", "URGENT: Verify Your Account Immediately", "Immediately verify your password or your account will be suspended."),
    ("billing@invoice-check.invalid.test", "Outstanding Invoice Requires Payment", "Your outstanding payment is due today. Verify your account details to avoid service interruption."),
    ("rewards@claim-prize.invalid.test", "You Have Won a Prize", "You have won a reward. Confirm your personal details to claim your prize."),
    ("admin@password-reset.invalid.test", "Password Expires Today", "Your password expires today. Login and verify your credentials immediately."),
    ("delivery@parcel-update.invalid.test", "Delivery Verification Required", "Confirm your account information to complete the fictional delivery request."),
    ("executive@urgent-request.invalid.test", "Urgent Executive Request", "Please make the requested payment immediately and confirm when complete."),
]

safe_urls = [
    "https://example.org/info",
    "https://example.com/help",
    "https://example.net/news"
]
phish_urls = [
    "http://198.51.100.10/verify-account",
    "http://198.51.100.20/login-password",
    "http://203.0.113.25/payment-confirm",
    "https://account.verify.invalid.test/confirm"
]

rows = []
for i in range(1, 601):
    is_phish = i % 2 == 0
    template = random.choice(phishing if is_phish else legitimate)
    sender, subject, body = template
    if is_phish:
        url = random.choice(phish_urls)
        attachment = random.choice(["", "", "invoice.pdf.exe", "document.js"])
        label = "PHISHING"
    else:
        url = random.choice(safe_urls)
        attachment = random.choice(["", "", "agenda.pdf", "workshop-notes.txt"])
        label = "LEGITIMATE"

    rows.append({
        "email_id": f"EML-{i:04d}",
        "sender": sender,
        "sender_domain": sender.split("@")[-1],
        "subject": subject,
        "body": body,
        "urls": url,
        "attachment_name": attachment,
        "label": label,
    })

with OUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"Generated {len(rows)} synthetic records: {OUT}")
