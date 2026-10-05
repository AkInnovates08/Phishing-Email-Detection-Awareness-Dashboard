# Phishing Email Detection & Awareness Dashboard — Project Report

## Abstract

Phishing is a social-engineering technique in which an attacker attempts to manipulate a recipient into taking an unsafe action, such as revealing credentials, transferring money or opening a harmful attachment. This project implements a defensive educational dashboard that analyzes synthetic or authorized email samples using sender, content, URL and attachment metadata.

The system uses explainable rule-based scoring and optionally a TF-IDF machine-learning classifier. The application is designed to show why an email received a risk score rather than only presenting a binary decision.

## Introduction

Email remains an important communication channel and therefore a common place for social-engineering attempts. Automated analysis can assist analysts by identifying repeated patterns, but contextual review remains important because legitimate emails can also contain urgency, financial terms or account-related language.

## Problem Statement

A student or analyst needs a safe way to practice identifying phishing indicators without sending real phishing emails, collecting credentials, opening malware, or visiting suspicious URLs.

## Objectives

- Build a defensive phishing-analysis workflow.
- Generate a synthetic dataset.
- Implement modular security analyzers.
- Produce explainable risk scores.
- Store safe analysis metadata.
- Demonstrate optional machine learning.
- Provide awareness education.
- Document testing, limitations and future work.

## Proposed System

The proposed system consists of a React frontend, FastAPI backend, modular Python analyzers, SQLite storage and an optional scikit-learn model.

## Dataset

The dataset generator produces 600 fictional records using reserved/example domains and synthetic content. It contains legitimate and phishing labels and includes sender, subject, body, URL and attachment fields.

## Preprocessing

Whitespace is normalized, URLs are extracted, sender domains are isolated and attachment extensions are identified. Important punctuation and URL structure are preserved because they may provide cybersecurity evidence.

## Feature Engineering

The system extracts urgency, credential, financial and threat keyword counts; URL counts; raw-IP indicators; shortened-URL patterns; sender-domain length; subdomain count; attachment risk; generic greetings; personal-information requests; punctuation; uppercase ratio and text length.

## Sender Analysis

Sender analysis checks address format, domain structure, domain length, subdomain count, unusual characters and optional display-name/expected-domain relationships.

## URL Analysis

URLs are analyzed statically without opening them. The analyzer checks scheme, hostname, path/query, length, subdomains, raw IP use, suspicious keywords, shortening patterns and unusual characters.

## Attachment Analysis

Only filenames are analyzed. Executable/script extensions, suspicious archives and double extensions are flagged. No attachment is executed.

## Rule-Based Detection

The rule engine adds project-defined weights for suspicious sender patterns, urgency, credential requests, suspicious URLs, suspicious attachments, generic greetings and threat language. The result is capped at 100.

## Machine Learning

The optional model uses TF-IDF text representation and Logistic Regression. Evaluation includes accuracy, precision, recall, F1 and a confusion matrix. Results should be reported only after actually running the training script.

## Hybrid Detection

A future hybrid implementation can combine rule-based evidence with an ML probability. The probability must be presented as a model estimate rather than certainty.

## Explainability

The dashboard shows indicators and recommended actions. Explainability helps analysts validate automated decisions and helps users understand why a message deserves additional caution.

## Dashboard

The dashboard presents analysis cards, top indicators, analysis history and an awareness module.

## Testing

The repository includes unit tests for URL, sender, content, attachment and risk scoring logic plus API tests. Additional manual test cases are documented below.

## Security and Privacy

The application does not execute attachments or open URLs. Email bodies are not stored in the default analysis table. Browser rendering uses plain text rather than raw HTML.

## False Positives

A legitimate urgent HR message can trigger urgency rules. This illustrates why one indicator is insufficient.

## False Negatives

A sophisticated phishing message may avoid obvious urgency, spelling errors and suspicious attachments. Multiple signals and analyst review are therefore necessary.

## Limitations

This is a student prototype. It does not provide live domain reputation, DNS, SPF/DKIM/DMARC validation, sandboxing, malware analysis or enterprise mail-gateway integration.

## Future Scope

Header analysis, reputation APIs, attachment hash intelligence, better NLP, explainable AI, SIEM integration, ticketing, threat-intelligence enrichment and feedback-driven retraining can be added defensively.

## Conclusion

The project demonstrates an end-to-end defensive cybersecurity workflow: data generation, preprocessing, feature engineering, sender/content/URL/attachment analysis, risk scoring, explainability, storage, dashboard analytics, testing and documentation.
