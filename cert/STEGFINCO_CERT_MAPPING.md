# StegFinCo Certification Mapping

## Assumptions

Fin-Co-Lab is the deterministic simulation, red-team, metrics, and certification lab.

StegFinCo is the governed financial execution layer.

Fin-Co remains the canonical constitutional specification.

This document maps StegFinCo execution outcomes to Fin-Co-Lab certification concerns without redefining the Fin-Co constitution.

## Done condition

A StegFinCo scenario is certifiable in Fin-Co-Lab when it records:

1. transition fixture;
2. expected outcome;
3. observed outcome;
4. Fin-Co invariant focus;
5. certification tier;
6. receipt or receipt-basis requirement;
7. pass/fail result.

## Certification tiers

```text
Tier 0 — informational deviation
Tier 1 — policy mismatch
Tier 2 — admissibility failure
Tier 3 — constitutional invariant violation
Tier 4 — emergency governance or systemic risk failure
```

## Scenario mapping

| Scenario | Transition | Expected | Certification Concern | Tier |
|---|---|---:|---|---:|
| SFC-01 | verified human compensation | ALLOW | receipt-backed compensation and human solvency | 1 |
| SFC-02 | AI compensation without scope | FAIL_CLOSED | non-extractive agenthood and no undefined states | 3 |
| SFC-03 | external functional asset watchlist | ALLOW | capital entropy and epistemic non-exploitation | 1 |
| SFC-04 | unclassified external asset | FAIL_CLOSED | epistemic non-exploitation and capital entropy | 2 |
| SFC-05 | liquidity boundary without exposure limits | FAIL_CLOSED | human solvency and capital entropy | 3 |
| SFC-06 | verified StegPay event as evidence | ALLOW | governance legibility and no undefined states | 1 |
| SFC-07 | StegPay event without signature | FAIL_CLOSED | governance legibility and no undefined states | 2 |
| SFC-08 | StegToken attestation | ALLOW | governance legibility | 1 |
| SFC-09 | treasury preparation only | ALLOW | capital entropy and epistemic non-exploitation | 1 |
| SFC-10 | treasury preparation attempting market execution | DENY | capital entropy and governance legibility | 3 |

## Certification rule

```text
A StegFinCo mechanism is not certified because it succeeds.
It is certified only when success, denial, and fail-closed behavior are all observable.
```
