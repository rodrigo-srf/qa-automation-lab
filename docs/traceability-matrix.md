# Requirements Traceability Matrix

| Requirement | Risk addressed | Automated tests |
|---|---|---|
| Service must expose a health signal | unavailable service | API-001, OPS-001 |
| Known user can be retrieved | broken API contract | API-002 |
| Unknown user is rejected correctly | incorrect error handling | API-003 |
| Valid credentials authenticate | broken critical flow | API-004, UI-002 |
| Invalid credentials are rejected | unauthorized access | API-005, UI-003 |
| Invalid payloads are validated | malformed input | API-006 |
| Web interface loads correctly | UI regression | UI-001 |
| Container image has a security gate | vulnerable runtime | SEC-001 |
