# Fin-Co-Lab StegFinCo Support Event Certification Add-on

## Assumptions

This add-on belongs in Fin-Co-Lab.

StegPay verifies support-payment evidence.

StegFinCo classifies support-payment evidence.

Fin-Co-Lab independently certifies the boundary behavior.

## Done condition

The add-on is complete when Fin-Co-Lab contains:

```text
cert/STEGFINCO_SUPPORT_EVENT_CERT_MAPPING.md
runs/STEGFINCO_SUPPORT_EVENT_CERT_RUNBOOK.md
sim/scenarios/Scenario_16_to_21_stegfinco_support_event_certification.md
sim/stegfinco/support_events/SFCS-01_support_event_allow.json
sim/stegfinco/support_events/SFCS-02_support_event_deny_entitlement.json
sim/stegfinco/support_events/SFCS-03_support_event_fail_wrong_metadata.json
sim/stegfinco/support_events/SFCS-04_support_event_fail_missing_receipt.json
sim/stegfinco/support_events/SFCS-05_support_event_fail_unverified_signature.json
sim/stegfinco/support_events/SFCS-06_support_event_fail_evidence_only_false.json
tools/stegfinco_support_event_cert_runner.py
tests/test_stegfinco_support_event_cert_runner.py
github/workflows/stegfinco-support-event-cert.yml
```

## Expected behavior

```text
verified support evidence → ALLOW
support entitlement attempt → DENY
missing/wrong evidence basis → FAIL_CLOSED
```

## iOS workflow note

The workflow is included at:

```text
github/workflows/stegfinco-support-event-cert.yml
```

The leading dot has been removed for iOS display and Files-app compatibility.

In GitHub, place it at:

```text
.github/workflows/stegfinco-support-event-cert.yml
```

## Boundary

```text
Payment is evidence.
Governance creates authority.
StegFinCo controls effect.
Fin-Co-Lab certifies the boundary.
```
