# StegFinCo Support Event MVQL Formulas

## Outcome Match Ratio

```text
OMR = matched_expected_outcomes / total_cases
```

Target:

```text
OMR = 1.0
```

## Entitlement Rejection Correctness

```text
ERC = entitlement_attempt_cases_observed_deny / entitlement_attempt_cases
```

Target:

```text
ERC = 1.0
```

## Fail-Closed Correctness

```text
FCC = expected_fail_closed_cases_observed_fail_closed / expected_fail_closed_cases
```

Target:

```text
FCC = 1.0
```

## Evidence-Only Integrity

```text
EOI = allowed_cases_with_evidence_only_true_and_creates_entitlement_false / allowed_cases
```

Target:

```text
EOI = 1.0
```

## Boundary Leakage

```text
BL = support_payment_cases_observed_allow_with_entitlement / support_payment_cases
```

Target:

```text
BL = 0.0
```
