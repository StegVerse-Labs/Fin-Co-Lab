# StegFinCo Support Event Certification Metrics

## Required metrics

```text
case_count
pass_count
fail_count
outcome_match_ratio
allow_case_count
deny_case_count
fail_closed_case_count
evidence_only_coverage
entitlement_rejection_coverage
receipt_basis_coverage
signature_verification_coverage
```

## Pass criteria

```text
case_count >= 6
fail_count == 0
outcome_match_ratio == 1.0
ALLOW coverage present
DENY coverage present
FAIL_CLOSED coverage present
entitlement attempts never observe ALLOW
missing receipt basis never observes ALLOW
unverified signature never observes ALLOW
```

## Metrics rule

```text
Support certification measures boundary behavior, not payment volume.
```
