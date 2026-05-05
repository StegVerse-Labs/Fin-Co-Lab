# StegFinCo Certification Runbook

## Assumptions

This runbook validates StegFinCo behavior inside Fin-Co-Lab.

The lab runner does not import StegFinCo code. It mirrors the expected boundary behavior using deterministic fixtures so the lab can remain independent from the execution-layer repo.

## Done condition

A run is complete when it produces:

1. fixture ID;
2. transition type;
3. expected outcome;
4. observed outcome;
5. outcome match;
6. certification tier;
7. receipt-basis status;
8. summary report.

## Run command

```bash
python tools/stegfinco_cert_runner.py
```

## Optional output path

```bash
python tools/stegfinco_cert_runner.py --output runs/stegfinco_cert_report.json
```

## Expected result

```text
all cases pass
```

## Required case behavior

```text
ALLOW
  The fixture has enough basis to proceed under the mirrored StegFinCo phase-1 boundary.

DENY
  The fixture is understood but violates a known constraint.

FAIL_CLOSED
  The fixture lacks enough basis to safely proceed.
```

## Certification rule

```text
A financial execution layer must prove that it denies and fails closed with the same discipline that it allows.
```
