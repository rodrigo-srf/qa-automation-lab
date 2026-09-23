# Test Plan

## Objective

Validate the critical behavior of the QA Automation Lab target application and ensure defects are detected before merge through automated quality gates.

## Scope

### In scope

- health endpoint
- user lookup contract
- authentication success/failure
- request schema validation
- home page readiness
- browser login flows
- container startup and health

### Out of scope

- performance/load testing
- accessibility certification
- production security penetration testing

## Test levels

- API functional testing
- UI end-to-end testing
- smoke testing
- regression testing
- static code quality
- container security scanning

## Entry criteria

- application builds successfully
- Python dependencies install successfully
- test environment starts and health endpoint responds

## Exit criteria

- all automated tests pass
- no critical Trivy finding configured to fail the pipeline
- lint passes
- coverage report is generated

## Risks

- UI tests depend on browser availability
- CI runners can introduce transient network/package-install failures
- this lab application is intentionally small and does not model every production risk
