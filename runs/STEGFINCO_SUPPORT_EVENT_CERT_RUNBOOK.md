# StegFinCo Support Event Certification Runbook

## Assumptions

This runbook validates support-payment evidence classification inside Fin-Co-Lab.

The lab runner mirrors the StegFinCo support-event boundary independently from the StegFinCo repo.

## Done condition

A support-event certification run is complete when it produces:

1. fixture ID;
2. expected outcome;
3. observed outcome;
4. pass/fail status;
5. Fin-Co invariant mapping;
6. evidence-only and entitlement flags;
7. certification report.

## Run command

```bash
python tools/stegfinco_support_event_cert_runner.py
```

## Optional output path

```bash
python tools/stegfinco_support_event_cert_runner.py --output runs/stegfinco_support_event_cert_report.json
```

## Expected result

```text
all cases pass
```

## Boundary rule

```text
Payment is evidence.
Governance creates authority.
StegFinCo controls effect.
Fin-Co-Lab certifies the boundary.
```
