# Phishing Email Detection & Awareness Dashboard

A defensive cybersecurity project that analyzes email content and identifies potential phishing indicators using explainable rule-based detection, static URL analysis, sender analysis, attachment filename analysis, and optional machine learning.

The project is designed for cybersecurity education, awareness training, portfolio development, and local security analysis.

---

## Table of Contents

- [Overview](#overview)
- [Objectives](#objectives)
- [Key Features](#key-features)
- [How the System Works](#how-the-system-works)
- [Detection Indicators](#detection-indicators)
- [Risk Scoring](#risk-scoring)
- [Risk Classification](#risk-classification)
- [Machine Learning](#machine-learning)
- [Dashboard](#dashboard)
- [Awareness Module](#awareness-module)
- [Technology Stack](#technology-stack)
- [Project Architecture](#project-architecture)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Testing](#testing)
- [API Endpoints](#api-endpoints)
- [Example Analysis](#example-analysis)
- [Security and Privacy](#security-and-privacy)
- [Safe Demonstration Policy](#safe-demonstration-policy)
- [ML Evaluation Disclaimer](#ml-evaluation-disclaimer)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [Learning Outcomes](#learning-outcomes)
- [Interview Questions](#interview-questions)
- [GitHub Proof Checklist](#github-proof-checklist)
- [Author](#author)

---

# Overview

Phishing is one of the most common social engineering techniques used to trick users into revealing sensitive information, opening malicious attachments, or visiting unsafe websites.

The **Phishing Email Detection & Awareness Dashboard** provides a safe environment for analyzing email messages and understanding why a message may be considered suspicious.

The system evaluates:

- Sender information
- Sender domain patterns
- Email subject
- Email body
- URLs
- Urgency and manipulation language
- Credential-related requests
- Threat and fear language
- Generic greetings
- Attachment filenames
- Suspicious file extensions
- Machine-learning text classification

The application produces an explainable risk score, classification, detected indicators, recommendations, and analysis history.

The project is intended for **defensive cybersecurity education only**.

---

# Objectives

The main objectives of this project are:

1. Detect common phishing indicators in email messages.
2. Provide an explainable risk score instead of only a prediction label.
3. Analyze sender and domain characteristics.
4. Detect urgency, threats, credential requests, and manipulation language.
5. Perform static URL analysis without visiting URLs.
6. Identify suspicious attachment filenames without executing files.
7. Provide an optional machine-learning classification layer.
8. Maintain a history of analyzed messages.
9. Provide cybersecurity awareness education.
10. Demonstrate a practical SOC-style email analysis workflow.
11. Provide a local, free, and safe cybersecurity learning environment.

---

# Key Features

## 1. Email Analyzer

Analyze an email using:

- Sender address
- Subject
- Email body
- URLs
- Attachment filename

The analyzer produces:

- Risk score
- Risk classification
- Detected indicators
- Explanation
- Recommendations

---

## 2. Sender Analysis

The sender analyzer checks for indicators such as:

- Suspicious sender patterns
- Unusual domains
- Domain mismatch patterns
- Suspicious domain structure
- Potential impersonation indicators
- Free or unusual domain patterns

The result is used as one component of the overall risk assessment.

A sender indicator alone does not prove that an email is phishing.

---

## 3. Content Analysis

The content analyzer searches for suspicious language patterns including:

- Urgency
- Threats
- Fear
- Credential requests
- Account verification requests
- Password-related requests
- Generic greetings
- Suspicious calls to action

Example suspicious language:

```text
Your account will be suspended immediately.
Verify your password now.
Failure to respond will result in account closure.
```

These indicators increase the risk score but should always be interpreted in context.

---

## 4. Static URL Analysis

The project analyzes URLs without opening or visiting them.

The URL analyzer can identify indicators such as:

- HTTP instead of HTTPS
- IP-address-based URLs
- Suspicious domains
- Excessive URL length
- Suspicious path patterns
- Credential-related URL paths
- URL shortening patterns
- Suspicious query parameters

Example:

```text
http://198.51.100.10/verify-account
```

This URL can be analyzed as text without connecting to it.

Important:

> HTTPS does not automatically mean that a website is trustworthy.

---

## 5. Attachment Filename Analysis

The project analyzes attachment filenames only.

Examples of suspicious filenames:

```text
invoice.pdf.exe
password_reset.scr
document.zip
account_update.bat
```

The system does not execute, open, or download attachments.

---

## 6. Explainable Risk Score

Instead of returning only:

```text
PHISHING
```

the system explains why the message received its risk score.

Example:

```text
Risk Score: 85

Classification:
HIGH RISK / LIKELY PHISHING

Detected Indicators:
- Credential request
- Urgency language
- Suspicious URL
- Executable attachment extension
- Threat language
```

---

## 7. Analysis History

The application stores previous analysis results locally.

History can include:

- Sender
- Subject
- Risk score
- Classification
- Detected indicators
- Timestamp

This allows users to review previously analyzed messages.

---

## 8. Security Awareness Module

The Awareness section provides educational guidance about:

- How phishing works
- Common phishing indicators
- Safe email handling
- URL safety
- Attachment safety
- Password security
- Multi-factor authentication
- Reporting suspicious messages

---

## 9. Dashboard

The dashboard provides a visual overview of analyzed emails.

Example metrics include:

- Total analyses
- High-risk emails
- Suspicious emails
- Lower-risk emails
- Average risk score
- Classification distribution

Charts are provided using the React frontend.

---

# How the System Works

The project follows a multi-stage analysis pipeline.

```text
                    Email Input
                         |
                         v
              +---------------------+
              | Input Preprocessing |
              +---------------------+
                         |
                         v
        +-------------------------------+
        | Feature / Indicator Analysis  |
        +-------------------------------+
          |       |       |       |
          v       v       v       v
       Sender  Content   URL   Attachment
          |       |       |       |
          +-------+-------+-------+
                  |
                  v
          Rule-Based Risk Engine
                  |
                  v
             Risk Score
                  |
                  v
           Classification
                  |
                  v
        Explanation + Recommendations
                  |
                  v
             Database
                  |
                  v
              Dashboard
```

---

# Detection Indicators

The project analyzes multiple categories of indicators.

| Category | Examples |
|---|---|
| Sender | Suspicious domain, unusual sender |
| Subject | Urgency, account warning |
| Body | Credential request, threat language |
| URL | IP address, HTTP, suspicious path |
| Attachment | `.exe`, `.scr`, `.bat`, suspicious double extension |
| Social Engineering | Fear, urgency, pressure |
| Greeting | Generic greeting patterns |

No individual indicator should automatically be treated as proof of phishing.

---

# Risk Scoring

The project uses an explainable rule-based scoring model.

The implemented scoring weights include:

| Indicator | Score |
|---|---:|
| Suspicious sender | +15 |
| Urgency language | +10 |
| Credential request | +20 |
| Suspicious URL | +20 |
| Suspicious attachment | +25 |
| Generic greeting | +5 |
| Threat/fear language | +10 |

The final score is capped at:

```text
100
```

Example:

```text
Sender indicator      +15
Urgency               +10
Credential request    +20
Suspicious URL        +20
Attachment            +25
--------------------------------
Total                  90
```

Final score:

```text
90 / 100
```

---

# Risk Classification

The current classification thresholds are:

| Risk Score | Classification |
|---:|---|
| 0–20 | LOW RISK |
| 21–40 | MODERATE RISK |
| 41–70 | SUSPICIOUS |
| 71–100 | HIGH RISK / LIKELY PHISHING |

These thresholds are project-level assumptions intended for demonstration and educational purposes.

They should be calibrated against representative real-world datasets before being used for production security decisions.

---

# Machine Learning

The project includes an optional machine-learning component.

The current ML pipeline uses:

- TF-IDF text features
- Logistic Regression
- Scikit-learn
- Train/test split
- Classification metrics
- Confusion matrix
- Joblib model persistence

The model is trained using the generated synthetic dataset.

Training command:

```powershell
python ml/train_model.py
```

The trained model is saved as:

```text
models/phishing_tfidf.joblib
```

---

# ML Evaluation

The current synthetic dataset produced the following evaluation result:

```text
Accuracy : 1.0
Precision: 1.0
Recall   : 1.0
F1       : 1.0
```

Confusion matrix:

```text
[[75  0]
 [ 0 75]]
```

These results were obtained from the project's controlled synthetic dataset.

They should **not** be interpreted as proof of 100% accuracy against real-world phishing emails.

Synthetic datasets can be easier to classify because their patterns are more controlled and predictable.

---

# Dashboard

The React dashboard contains the following main sections:

## Email Analyzer

Analyze email content and display:

- Risk score
- Classification
- Indicators
- Explanations
- Recommendations

## Dashboard

View:

- Analysis statistics
- Risk distribution
- Historical analysis data
- Summary metrics

## History

Review previous email analyses.

## Awareness

Learn about phishing prevention and safe email handling.

---

# Technology Stack

## Backend

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Pydantic

## Machine Learning

- Scikit-learn
- TF-IDF
- Logistic Regression
- Pandas
- NumPy
- Joblib

## Frontend

- React
- Vite
- JavaScript
- CSS
- Recharts

## Testing

- Pytest
- FastAPI TestClient

## Development Tools

- Visual Studio Code
- Git
- GitHub
- PowerShell

---

# Project Architecture

```text
Frontend
   |
   | HTTP Requests
   v
FastAPI Backend
   |
   +-------------------+
   |                   |
   v                   v
Analysis Services    Database
   |
   +-----------------------+
   |       |       |       |
   v       v       v       v
Sender  Content   URL  Attachment
Analyzer Analyzer Analyzer Analyzer
   |
   v
Feature Engineering
   |
   +----------------+
   |                |
   v                v
Risk Engine      ML Model
   |                |
   +-------+--------+
           |
           v
    Analysis Result
           |
           v
       Dashboard
```

---

# Project Structure

```text
Phishing-Email-Detection-Awareness-Dashboard/
│
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── schemas.py
│   │
│   ├── models/
│   │   └── analysis.py
│   │
│   ├── routes/
│   │   ├── analysis.py
│   │   └── dashboard.py
│   │
│   ├── services/
│   │   ├── preprocessing.py
│   │   ├── sender_analyzer.py
│   │   ├── content_analyzer.py
│   │   ├── url_analyzer.py
│   │   ├── attachment_analyzer.py
│   │   ├── feature_engineering.py
│   │   ├── risk_engine.py
│   │   └── ml_service.py
│   │
│   └── utils/
│       └── safety.py
│
├── data/
│   ├── generate_dataset.py
│   └── phishing_email_dataset.csv
│
├── ml/
│   ├── train_model.py
│   ├── evaluation.py
│   └── predict.py
│
├── models/
│   └── phishing_tfidf.joblib
│
├── frontend/
│   ├── package.json
│   ├── index.html
│   ├── vite.config.js
│   │
│   └── src/
│       ├── main.jsx
│       └── styles.css
│
├── tests/
│   ├── test_analyzers.py
│   └── test_api.py
│
├── docs/
│   ├── architecture.md
│   ├── industry_mapping.md
│   ├── demo_samples.txt
│   ├── screenshot_checklist.md
│   ├── test_plan.md
│   └── interview_notes.md
│
├── reports/
│   └── project_report.md
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

---

# Dataset

The project generates a synthetic dataset for safe experimentation.

Dataset generation:

```powershell
python data/generate_dataset.py
```

The generator creates:

```text
600 synthetic records
```

The generated dataset contains fields such as:

```text
email_id
sender
sender_domain
subject
body
urls
attachment_name
label
```

Example structure:

```text
email_id,sender,sender_domain,subject,body,urls,attachment_name,label
```

The dataset is intended for educational machine-learning experiments.

---

# Installation

## Requirements

Install the following software before starting:

- Python 3.10+
- Node.js
- npm
- Git
- Visual Studio Code

---

# Backend Installation

Open PowerShell inside the project directory.

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

Your terminal should show:

```text
(.venv)
```

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Install Python dependencies:

```powershell
python -m pip install -r requirements.txt
```

---

# Generate Dataset

Run:

```powershell
python data/generate_dataset.py
```

Expected output:

```text
Generated 600 synthetic records:
...\data\phishing_email_dataset.csv
```

---

# Train Machine Learning Model

Run:

```powershell
python ml/train_model.py
```

Expected output:

```text
Accuracy : 1.0
Precision: 1.0
Recall   : 1.0
F1       : 1.0

Confusion matrix:
[[75  0]
 [ 0 75]]
```

The trained model will be stored at:

```text
models/phishing_tfidf.joblib
```

---

# Run Tests

Run:

```powershell
pytest -q
```

Expected result:

```text
9 passed
```

If FastAPI is missing, install the project dependencies again:

```powershell
python -m pip install -r requirements.txt
```

Then run:

```powershell
pytest -q
```

---

# Running the Backend

Start the FastAPI server:

```powershell
python -m uvicorn backend.app:app --reload
```

Backend address:

```text
http://127.0.0.1:8000
```

Health check:

```text
http://127.0.0.1:8000/health
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Running the Frontend

Open a second PowerShell terminal.

Navigate to the frontend:

```powershell
cd frontend
```

Install Node dependencies:

```powershell
npm install
```

Start the development server:

```powershell
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:5173
```

---

# Complete Execution Commands

## Terminal 1 — Backend

From the project root:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python data/generate_dataset.py
python ml/train_model.py
pytest -q
python -m uvicorn backend.app:app --reload
```

## Terminal 2 — Frontend

```powershell
cd frontend
npm install
npm run dev
```

Then open:

```text
http://localhost:5173
```

---

# API Endpoints

The FastAPI backend provides endpoints for analysis and dashboard functionality.

The interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

The API supports functionality for:

- Email analysis
- URL analysis
- Analysis history
- Dashboard statistics
- Health checking

Use Swagger UI to inspect request and response schemas.

---

# Example Analysis

## Safe Example

Sender:

```text
training@example.org
```

Subject:

```text
Cybersecurity Workshop Reminder
```

Body:

```text
This is a normal informational reminder for the scheduled cybersecurity workshop.
```

Attachment:

```text
workshop-notes.txt
```

This example is intended to represent a normal informational email.

---

# Safe Phishing Demonstration

The project includes a safe synthetic demonstration.

Example sender:

```text
security-alert@account-check.invalid.test
```

Subject:

```text
URGENT: Verify Your Account Immediately
```

Body:

```text
Immediately verify your password or your account will be suspended.
Visit http://198.51.100.10/verify-account
```

Attachment:

```text
invoice.pdf.exe
```

The application should identify multiple suspicious indicators, such as:

- Urgency
- Credential request
- Threat language
- Suspicious URL
- IP-address-based URL
- Suspicious attachment extension

The example uses reserved/documentation IP space and fictional domains for safe demonstration.

---

# Security and Privacy

This project is designed with defensive security principles.

## The project does not:

- Send phishing emails
- Collect passwords
- Collect credentials
- Create credential-harvesting pages
- Attack websites
- Attack real users
- Scan external systems
- Visit submitted URLs
- Execute uploaded files
- Download malicious content
- Perform exploitation
- Perform credential attacks

## URL Safety

URLs are treated as text.

The application performs static analysis and does not navigate to submitted URLs.

## Attachment Safety

Attachments are analyzed by filename only.

The project does not execute uploaded files.

## Dataset Safety

The included dataset is synthetic and intended for educational use.

---

# Safe Demonstration Policy

Only use:

- Synthetic emails
- Fictional senders
- Reserved example domains
- Documentation IP addresses
- Local test data
- Authorized environments

Do not use this project to target real organizations, users, websites, or systems.

---

# False Positives and Context

A phishing detector cannot determine malicious intent from one indicator alone.

For example:

```text
URGENT
```

does not automatically mean an email is phishing.

Similarly:

```text
https://example.com
```

does not automatically mean the email is safe.

The project therefore combines multiple indicators and provides explanations instead of treating one signal as definitive proof.

Users should verify suspicious communications through trusted channels.

---

# Testing

The project includes automated tests for:

- Sender analysis
- Content analysis
- URL analysis
- Attachment analysis
- Risk scoring
- API functionality

Run the complete test suite:

```powershell
pytest -q
```

Expected result for the prepared project:

```text
9 passed
```

---

# Dashboard Workflow

A typical workflow is:

```text
1. Open the dashboard
       |
       v
2. Enter or load a synthetic email
       |
       v
3. Analyze the email
       |
       v
4. Review risk score
       |
       v
5. Review detected indicators
       |
       v
6. Read explanation
       |
       v
7. Follow recommendations
       |
       v
8. Review analysis in History
       |
       v
9. Review statistics in Dashboard
```

---

# SOC Workflow Demonstration

The project can be used to demonstrate a simplified Security Operations Center workflow.

```text
Email Received
      |
      v
Initial Analysis
      |
      v
Indicator Identification
      |
      +-------------------+
      |                   |
      v                   v
Sender Analysis      Content Analysis
      |                   |
      +---------+---------+
                |
                v
          URL Analysis
                |
                v
       Attachment Analysis
                |
                v
          Risk Scoring
                |
                v
       Classification
                |
                v
       Analyst Decision
```

Possible analyst actions:

```text
LOW RISK
    -> Continue normal handling

MODERATE RISK
    -> Verify context

SUSPICIOUS
    -> Perform additional verification

HIGH RISK / LIKELY PHISHING
    -> Avoid interacting with links or attachments
    -> Report through the appropriate security process
```

---

# MITRE ATT&CK Context

The project demonstrates concepts related to defensive detection of social engineering and phishing activity.

Relevant high-level cybersecurity concepts include:

- Phishing
- Spearphishing
- Malicious link awareness
- Malicious attachment awareness
- Credential theft awareness
- Social engineering detection

The project is intended to demonstrate detection and awareness concepts rather than offensive execution.

---

# Limitations

This project is an educational prototype and should not be considered a production-grade email security gateway.

Current limitations include:

1. Synthetic training data.
2. Rule-based scoring assumptions.
3. Limited sender reputation intelligence.
4. No live threat-intelligence feeds.
5. No real-time mail-server integration.
6. Static URL analysis only.
7. Filename-based attachment analysis.
8. Limited natural-language understanding.
9. No sandbox execution.
10. No enterprise SIEM integration.

---

# Future Improvements

Possible future improvements include:

## Machine Learning

- Random Forest
- Naive Bayes
- Gradient Boosting
- Ensemble models
- Transformer-based text classification
- Model calibration
- Explainable AI

## Cybersecurity Intelligence

- Domain reputation APIs
- Threat-intelligence feeds
- DNS analysis
- WHOIS-based enrichment
- Reputation scoring
- IOC enrichment

These integrations should only be added in authorized defensive environments.

## Email Integration

Future versions could integrate with:

- Mailbox ingestion
- Security operations workflows
- SIEM platforms
- Ticketing systems
- Incident response systems

## Advanced Detection

Potential additions:

- Brand impersonation detection
- Homograph detection
- HTML email analysis
- Header analysis
- SPF/DKIM/DMARC analysis
- Advanced NLP
- Behavioral analysis
- Anomaly detection

---

# Learning Outcomes

By completing this project, the developer can demonstrate practical knowledge of:

### Cybersecurity

- Phishing detection
- Social engineering
- Email security
- Indicator analysis
- Risk assessment
- Security awareness
- Defensive security

### Machine Learning

- Dataset generation
- Data preprocessing
- Feature engineering
- TF-IDF
- Classification
- Model evaluation
- Confusion matrices
- Precision
- Recall
- F1-score

### Backend Development

- FastAPI
- REST APIs
- Pydantic
- SQLAlchemy
- SQLite
- API testing

### Frontend Development

- React
- Vite
- Dashboard design
- Data visualization
- API integration

### Software Engineering

- Modular architecture
- Automated testing
- Documentation
- Git/GitHub
- Virtual environments
- Project structure

---


---



---

# Troubleshooting

## FastAPI Not Found

Error:

```text
ModuleNotFoundError: No module named 'fastapi'
```

Solution:

```powershell
python -m pip install -r requirements.txt
```

Verify:

```powershell
python -c "import fastapi; print(fastapi.__version__)"
```

---

## Uvicorn Import Error

Use:

```powershell
python -m uvicorn backend.app:app --reload
```

instead of:

```powershell
uvicorn backend.app:app --reload
```

This ensures Uvicorn runs using the active Python environment.

---

## PowerShell Virtual Environment Activation

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then:

```powershell
.venv\Scripts\Activate.ps1
```

---

## Frontend Dependencies Missing

Navigate to:

```powershell
cd frontend
```

Then:

```powershell
npm install
```

Start:

```powershell
npm run dev
```

---

# Complete Quick Start

If the environment is already configured, the project can be started with:

### Backend

```powershell
.venv\Scripts\Activate.ps1
python data/generate_dataset.py
python ml/train_model.py
pytest -q
python -m uvicorn backend.app:app --reload
```

### Frontend

Open another terminal:

```powershell
cd frontend
npm install
npm run dev
```

Open:

```text
http://localhost:5173
```

---

# Project Status

Current implementation includes:

```text
Dataset Generation        Complete
Synthetic Dataset         Complete
Rule-Based Detection      Complete
Sender Analysis           Complete
Content Analysis          Complete
URL Analysis              Complete
Attachment Analysis       Complete
Risk Scoring              Complete
ML Training               Complete
FastAPI Backend            Complete
React Frontend             Complete
Dashboard                  Complete
History                    Complete
Awareness Module           Complete
Automated Testing           Complete
Documentation              Complete
```

---

# Disclaimer

This project is developed for educational, defensive cybersecurity, and awareness purposes.

It is not intended to facilitate phishing, credential theft, unauthorized access, malware deployment, exploitation or attacks against real users or systems.

Only analyze data that you are authorized to analyze.

---


---

# License

This project is intended for educational and portfolio purposes.

If you reuse or extend the project, maintain the defensive and educational security principles described in this README.