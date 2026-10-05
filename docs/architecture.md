# System Architecture

```text
                    +----------------------+
                    |       User           |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |    React Dashboard   |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |     FastAPI API      |
                    +----------+-----------+
                               |
        +----------------------+----------------------+
        |                      |                      |
        v                      v                      v
 Sender Analyzer       Content Analyzer        URL Analyzer
        |                      |                      |
        +----------------------+----------------------+
                               |
                    +----------v-----------+
                    | Attachment Analyzer  |
                    +----------+-----------+
                               |
                    +----------v-----------+
                    | Rule-Based Risk      |
                    | Scoring Engine       |
                    +----------+-----------+
                               |
                    +----------v-----------+
                    | Optional TF-IDF ML   |
                    +----------+-----------+
                               |
                    +----------v-----------+
                    | Explainable Result   |
                    +----------+-----------+
                         |            |
                         v            v
                    SQLite DB     Dashboard
```

Data flow:

1. User submits safe email metadata.
2. API validates and normalizes input.
3. Sender analyzer extracts domain and structural signals.
4. Content analyzer detects social-engineering language.
5. URL analyzer performs static parsing only.
6. Attachment analyzer checks filenames/extensions only.
7. Feature engineering creates structured indicators.
8. Rule engine creates an explainable 0–100 score.
9. Optional ML model provides a probability estimate when trained.
10. Metadata and findings are stored in SQLite.
11. Dashboard displays current analysis and history.
