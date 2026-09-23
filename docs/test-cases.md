# Test Cases

| ID | Layer | Scenario | Expected result | Automation |
|---|---|---|---|---|
| API-001 | API | GET /health | 200 and `status=ok` | Pytest |
| API-002 | API | Existing user lookup | 200 with expected contract | Pytest |
| API-003 | API | Missing user lookup | 404 with error detail | Pytest |
| API-004 | API | Valid login | 200, authenticated true, token present | Pytest |
| API-005 | API | Invalid password | 401 | Pytest |
| API-006 | API | Invalid input schema | 422 | Pytest |
| UI-001 | UI | Open home page | Title/header/status visible | Playwright |
| UI-002 | UI | Valid login in browser | `Login successful` | Playwright |
| UI-003 | UI | Invalid login in browser | `Login failed` | Playwright |
| OPS-001 | Smoke | Container health | `/health` responds successfully | GitHub Actions |
| SEC-001 | Security | Container scan | No blocking critical finding | Trivy |
