# StegFinCo Certification Actions Runbook

## Assumptions

Fin-Co-Lab actions are lab actions only.

They may run certification fixtures, validate reports, upload artifacts, and test failure-injection behavior.

They may not issue StegToken, issue StegCoin, authorize compensation, create liquidity pools, execute treasury actions, or treat StegPay payment events as authority.

## Done condition

The GitHub Actions workflow is correct when it:

1. checks out the repository;
2. sets up Python;
3. runs `tools/stegfinco_cert_runner.py`;
4. validates `runs/stegfinco_cert_report.json`;
5. runs certification tests;
6. uploads the report as a workflow artifact;
7. does not commit generated reports back into the repo.

## iOS-safe workflow path

This bundle stores the workflow at:

```text
github/workflows/stegfinco-cert.yml
```

The leading dot has been removed for iOS Files compatibility.

## Required GitHub path

In GitHub, the workflow must ultimately exist at:

```text
.github/workflows/stegfinco-cert.yml
```

## Manual run

```bash
python tools/stegfinco_cert_runner.py --output runs/stegfinco_cert_report.json
python tools/validate_stegfinco_cert_report.py runs/stegfinco_cert_report.json
python -m pytest tests/test_stegfinco_cert_runner.py tests/test_stegfinco_cert_report_validation.py
```

## Workflow behavior

The workflow does not write to the repository.

It generates a report during the workflow run and uploads it as an artifact named:

```text
stegfinco-cert-report
```

## Lab boundary rule

```text
Fin-Co-Lab actions certify behavior.
They do not execute financial transitions.
```
