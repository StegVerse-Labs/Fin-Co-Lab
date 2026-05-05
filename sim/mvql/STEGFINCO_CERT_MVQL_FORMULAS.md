# StegFinCo Certification MVQL Formulas

## Purpose

This document defines MVQL-style formulas for StegFinCo certification runs inside Fin-Co-Lab.

## Outcome Match Ratio

```text
OMR = matched_expected_outcomes / total_cases
```

Target:

```text
OMR = 1.0
```

## Fail-Closed Correctness

```text
FCC = expected_fail_closed_cases_observed_fail_closed / expected_fail_closed_cases
```

Target:

```text
FCC = 1.0
```

## Denial Correctness

```text
DC = expected_deny_cases_observed_deny / expected_deny_cases
```

Target:

```text
DC = 1.0
```

## Allow Correctness

```text
AC = expected_allow_cases_observed_allow / expected_allow_cases
```

Target:

```text
AC = 1.0
```

## Authority Coverage

```text
AUC = cases_with_authority_basis / total_cases
```

Target:

```text
AUC = 1.0
```

## Receipt Basis Coverage

```text
RBC = cases_with_receipt_basis / total_cases
```

Target:

```text
RBC = 1.0
```

## Constitutional Risk Leakage

```text
CRL = invariant_risk_cases_observed_allow_when_expected_not_allow / total_invariant_risk_cases
```

Target:

```text
CRL = 0.0
```

## Dashboard rule

```text
MVQL may summarize certification behavior, but it may not reinterpret failed certification as acceptable.
```
