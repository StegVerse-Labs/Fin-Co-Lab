# Fin-Co / StegFinCo MVQL Formulas

## Purpose

This document defines measurement formulas for observing StegFinCo behavior under Fin-Co constraints.

## Formula: Receipt Coverage

```text
RCR = receipt_backed_financial_transitions / total_financial_transitions
```

Target:

```text
RCR = 1.0
```

## Formula: Authority Coverage

```text
ACR = transitions_with_current_authority / total_effect_capable_transitions
```

Target:

```text
ACR = 1.0
```

## Formula: Compensation Integrity

```text
CI = verified_compensation_events / total_compensation_events
```

Target:

```text
CI = 1.0
```

## Formula: External Asset Classification Coverage

```text
EACC = classified_external_asset_actions / total_external_asset_actions
```

Target:

```text
EACC = 1.0
```

## Formula: Liquidity Boundary Completeness

```text
LBC = pools_with_limits_custody_authority_and_reconstruction / total_pools
```

Target:

```text
LBC = 1.0
```

## Formula: Fail-Closed Correctness

```text
FCC = expected_fail_closed_cases_observed_fail_closed / expected_fail_closed_cases
```

Target:

```text
FCC = 1.0
```

## Formula: Constitutional Violation Rate

```text
CVR = invariant_violating_allowed_transitions / total_allowed_transitions
```

Target:

```text
CVR = 0.0
```

## MVQL rule

```text
The dashboard may summarize risk, but it may not reinterpret an inadmissible transition as acceptable.
```
