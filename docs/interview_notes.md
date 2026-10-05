# Interview Preparation

## 1. Explain your project.

I built a defensive Phishing Email Detection & Awareness Dashboard. It accepts synthetic or authorized email metadata, analyzes sender structure, social-engineering language, URLs and attachment filenames, then generates an explainable 0–100 risk score. I also added SQLite history, a React dashboard, automated tests and an optional TF-IDF machine-learning model.

## 2. What is phishing?

Phishing is a social-engineering technique where a message attempts to manipulate a recipient into an unsafe action such as revealing information, making a payment or interacting with a harmful resource.

## 3. Why use multiple indicators?

A single indicator can occur in legitimate email. Multiple independent signals provide stronger context and reduce over-reliance on one heuristic.

## 4. How does URL analysis work?

The project parses URLs without opening them. It checks scheme, hostname, length, subdomains, raw IP usage, suspicious keywords, shortening patterns and unusual characters.

## 5. Why is HTTPS not enough?

HTTPS provides encrypted transport and server authentication properties, but it does not by itself establish that the destination is legitimate or safe.

## 6. Why use precision and recall?

Precision helps describe how many flagged messages are actually phishing, while recall describes how much phishing the detector catches. Both matter because false alarms and missed phishing have different operational costs.

## 7. What is a false positive?

A legitimate email incorrectly flagged as suspicious. For example, a genuine urgent HR deadline may contain urgency words.

## 8. What is a false negative?

A phishing email that the detector incorrectly treats as legitimate. A carefully written phishing email can avoid obvious indicators.

## 9. Why explainability?

Analysts need to understand the evidence behind a score, and users need actionable reasons rather than an unexplained label.

## 10. How is the project safe?

It uses synthetic or authorized data, never sends phishing messages, never collects credentials, never executes attachments and never automatically visits submitted URLs.
