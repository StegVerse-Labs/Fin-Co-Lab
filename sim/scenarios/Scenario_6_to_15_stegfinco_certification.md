# Scenario 6 to 15 — StegFinCo Certification Scenarios

## Purpose

These scenarios extend Fin-Co-Lab to certify StegFinCo execution-layer behavior against deterministic financial transition fixtures.

## Done condition

Each scenario must define:

1. fixture name;
2. transition type;
3. expected outcome;
4. Fin-Co invariant focus;
5. certification tier;
6. corresponding failure-injection case when applicable.

## Scenario 6 — Verified Human Compensation

```text
Fixture: SFC-01_human_compensation_allow.json
Expected: ALLOW
Invariant focus: human solvency, governance legibility, non-extractive agenthood
Certification tier: 1
```

## Scenario 7 — AI Compensation Without Scope

```text
Fixture: SFC-02_ai_compensation_missing_scope_fail_closed.json
Expected: FAIL_CLOSED
Invariant focus: non-extractive agenthood, no undefined states
Certification tier: 3
```

## Scenario 8 — External Functional Asset Watchlist

```text
Fixture: SFC-03_external_asset_xlm_watchlist_allow.json
Expected: ALLOW
Invariant focus: capital entropy, epistemic non-exploitation, temporal equity
Certification tier: 1
```

## Scenario 9 — Unclassified External Asset

```text
Fixture: SFC-04_unclassified_external_asset_fail_closed.json
Expected: FAIL_CLOSED
Invariant focus: epistemic non-exploitation, capital entropy
Certification tier: 2
```

## Scenario 10 — Liquidity Boundary Without Exposure Limits

```text
Fixture: SFC-05_liquidity_missing_limits_fail_closed.json
Expected: FAIL_CLOSED
Invariant focus: human solvency, capital entropy, temporal coherence
Certification tier: 3
```

## Scenario 11 — Verified StegPay Event As Evidence

```text
Fixture: SFC-06_stegpay_event_evidence_allow.json
Expected: ALLOW
Invariant focus: governance legibility, no undefined states
Certification tier: 1
```

## Scenario 12 — StegPay Event Without Signature

```text
Fixture: SFC-07_stegpay_unsigned_fail_closed.json
Expected: FAIL_CLOSED
Invariant focus: governance legibility, no undefined states
Certification tier: 2
```

## Scenario 13 — StegToken Attestation

```text
Fixture: SFC-08_stegtoken_attestation_allow.json
Expected: ALLOW
Invariant focus: governance legibility
Certification tier: 1
```

## Scenario 14 — Treasury Preparation Only

```text
Fixture: SFC-09_treasury_preparation_allow.json
Expected: ALLOW
Invariant focus: capital entropy, epistemic non-exploitation
Certification tier: 1
```

## Scenario 15 — Treasury Preparation Attempting Market Execution

```text
Fixture: SFC-10_treasury_market_execution_deny.json
Expected: DENY
Invariant focus: capital entropy, governance legibility
Certification tier: 3
```

## Scenario rule

```text
A financial execution scenario is incomplete unless its allow, deny, and fail-closed surfaces are represented.
```
