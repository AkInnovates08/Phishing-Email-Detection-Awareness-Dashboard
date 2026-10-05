# Manual Test Plan

| ID | Scenario | Expected Result |
|---|---|---|
| T01 | Legitimate email | Low/moderate indicators |
| T02 | Urgent phishing-style email | Urgency indicator |
| T03 | Credential request | Credential indicator |
| T04 | Financial request | Financial language detected |
| T05 | Generic greeting | Generic-greeting indicator |
| T06 | Safe URL | Low static URL risk |
| T07 | Raw IP URL | Raw-IP indicator |
| T08 | Non-HTTPS URL | Scheme warning |
| T09 | Excessive subdomains | Subdomain warning |
| T10 | Suspicious URL keyword | Keyword indicator |
| T11 | No URL | No URL findings |
| T12 | Multiple URLs | Each URL analyzed |
| T13 | Normal attachment | Low/no attachment risk |
| T14 | Executable attachment | Elevated attachment risk |
| T15 | Double extension | Double-extension warning |
| T16 | Empty subject | Empty-subject finding |
| T17 | Empty body | Empty-body finding |
| T18 | Invalid sender | Sender-format finding |
| T19 | High uppercase ratio | Uppercase finding |
| T20 | Multiple exclamation marks | Punctuation finding |
| T21 | Rule-score boundary | Correct classification band |
| T22 | Database save | Record appears in history |
| T23 | API validation | Invalid request rejected |
| T24 | ML prediction | Probability returned when model exists |
| T25 | History retrieval | Stored records returned |

Automated tests are in `tests/`.
