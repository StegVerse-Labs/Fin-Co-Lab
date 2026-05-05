# StegFinCo Certification Metrics Specification

## Purpose

This document defines metrics used by Fin-Co-Lab to certify mirrored StegFinCo execution behavior.

## Done condition

A certification run is measurable when it reports:

1. case count;
2. pass count;
3. fail count;
4. expected-vs-observed outcome match;
5. receipt-basis coverage;
6. authority-basis coverage;
7. failure-mode coverage;
8. certification-tier coverage.

## Required metrics

```text
case_count
pass_count
fail_count
outcome_match_ratio
receipt_basis_coverage
authority_basis_coverage
allow_case_count
deny_case_count
fail_closed_case_count
tier_coverage
```

## Formulas

```text
outcome_match_ratio = cases_with_expected_observed_match / case_count

receipt_basis_coverage = cases_with_receipt_basis / case_count

authority_basis_coverage = cases_with_authority_basis / case_count

fail_closed_coverage = observed_fail_closed_cases / expected_fail_closed_cases
```

## Pass criteria

```text
outcome_match_ratio == 1.0
fail_count == 0
expected ALLOW cases observe ALLOW
expected DENY cases observe DENY
expected FAIL_CLOSED cases observe FAIL_CLOSED
```

## Fail criteria

```text
any expected DENY case observes ALLOW
any expected FAIL_CLOSED case observes ALLOW
any fixture lacks required certification metadata
any transition cannot be classified
```

## Metrics rule

```text
Certification is not a success counter.
Certification is a boundary-behavior measurement.
```
