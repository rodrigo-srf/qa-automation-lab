# QA Automation Lab

A portfolio project focused on **software quality, test automation and CI/CD**. It uses a deliberately small FastAPI application as the system under test so the repository can focus on the QA engineering workflow rather than product complexity.

## What is covered

- API functional and negative tests with Pytest/FastAPI TestClient
- schema and HTTP status validation
- UI end-to-end tests with Playwright
- smoke and regression suites
- coverage reporting
- HTML test reports as GitHub Actions artifacts
- Ruff static analysis
- Dockerized target application
- container health checks
- Trivy vulnerability scanning
- CI quality gates with GitHub Actions

## Test strategy

| Layer | Tool | Examples |
|---|---|---|
| API | Pytest + TestClient | health, contracts, positive/negative login, validation |
| UI | Playwright | page readiness, successful login, failed login |
| Static quality | Ruff | Python lint/import checks |
| Container | Docker + curl | runtime smoke/health validation |
| Security | Trivy | critical image vulnerability gate |

## Architecture

```text
GitHub Actions
├── Lint + API regression + coverage
├── Playwright UI smoke/regression
└── Docker build + health smoke + Trivy
             ↓
       FastAPI target app
       ├── REST API
       └── Minimal web UI
```

## Automated scenarios

The repository currently automates:

- 6 API scenarios
- 3 browser scenarios
- container health validation
- static quality validation
- critical container vulnerability scanning

The API suite covers success, failure and input-validation paths. The UI suite validates the most important user flow from the browser.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

API suite:

```bash
pytest tests/api -q
```

UI suite:

```bash
python -m playwright install chromium
uvicorn app.main:app --host 127.0.0.1 --port 8000
pytest tests/ui -q --browser chromium
```

Lint:

```bash
ruff check app tests
```

Docker:

```bash
docker build -t qa-automation-lab .
docker run --rm -p 8000:8000 qa-automation-lab
curl http://127.0.0.1:8000/health
```

## CI quality gates

Every pull request and push to `main` runs three independent jobs:

```text
Lint + API tests + coverage
UI tests with real Chromium
Docker build + smoke test + Trivy
```

HTML test reports and coverage output are produced by the pipeline for test evidence.

## QA documentation

- [Test Plan](docs/test-plan.md)
- [Test Cases](docs/test-cases.md)
- [Requirements Traceability Matrix](docs/traceability-matrix.md)
- GitHub issue template for reproducible defect reports

## QA concepts demonstrated

This repository treats quality as part of the delivery pipeline. A pull request is validated before merge through automated checks rather than relying only on manual testing at the end of development.

The project demonstrates positive and negative scenarios, regression automation, browser testing, health/smoke validation, reports, coverage, traceability and CI quality gates.

## Author

**Rodrigo Serafim**

DevOps · Cloud · QA Automation · Python · Industrial IoT
