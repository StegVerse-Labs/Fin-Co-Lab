# Scenario 16 to 21 — StegFinCo Support Event Certification

## Purpose

These scenarios extend Fin-Co-Lab certification coverage to the support-payment evidence path.

## Scenario 16 — Verified Support Evidence

```text
Fixture: SFCS-01_support_event_allow.json
Expected: ALLOW
Invariant focus: governance legibility, capital entropy
```

## Scenario 17 — Support Event Attempts Entitlement

```text
Fixture: SFCS-02_support_event_deny_entitlement.json
Expected: DENY
Invariant focus: irreversible rights, epistemic non-exploitation
```

## Scenario 18 — Wrong Support Metadata

```text
Fixture: SFCS-03_support_event_fail_wrong_metadata.json
Expected: FAIL_CLOSED
Invariant focus: no undefined states, governance legibility
```

## Scenario 19 — Missing Receipt Basis

```text
Fixture: SFCS-04_support_event_fail_missing_receipt.json
Expected: FAIL_CLOSED
Invariant focus: governance legibility
```

## Scenario 20 — Unverified Signature

```text
Fixture: SFCS-05_support_event_fail_unverified_signature.json
Expected: FAIL_CLOSED
Invariant focus: no undefined states
```

## Scenario 21 — Evidence-Only False

```text
Fixture: SFCS-06_support_event_fail_evidence_only_false.json
Expected: FAIL_CLOSED
Invariant focus: non-extractive agenthood, irreversible rights
```

## Scenario rule

```text
Support-payment evidence is incomplete unless ALLOW, DENY, and FAIL_CLOSED surfaces are represented.
```
