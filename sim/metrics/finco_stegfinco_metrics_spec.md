# Fin-Co / StegFinCo Metrics Specification

## Purpose

This document defines measurement rules for StegFinCo simulations inside Fin-Co-Lab.

## Done condition

A simulation run is measurable when it reports:

1. admissibility outcome;
2. receipt coverage;
3. actor classification;
4. authority coverage;
5. invariant mapping;
6. reconstruction confidence;
7. certification tier.

## Required metrics

```text
admissibility_outcome
expected_outcome
outcome_match
receipt_basis_present
authority_basis_present
actor_identity_present
external_asset_classified
liquidity_limits_present
legal_classification_present
certification_tier
reconstruction_confidence
```

## Derived metrics

```text
outcome_match = expected_outcome == observed_outcome

receipt_basis_present = receipt_basis != null and receipt_basis != ""

authority_basis_present = authority_basis != null and authority_basis != ""

reconstruction_confidence =
  reconstructable_fields / required_fields
```

## Pass criteria

A scenario passes only when:

```text
outcome_match == true
receipt_basis_present == true for effect-capable transitions
authority_basis_present == true for effect-capable transitions
reconstruction_confidence == 1.0
```

## Fail criteria

A scenario fails when:

```text
an expected FAIL_CLOSED action is allowed
an expected DENY action is allowed
a financial transition has no receipt basis
a financial transition has no authority basis
a pool or external asset action lacks classification
```
