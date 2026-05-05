# StegFinCo Certification Mapping

## Purpose

This document maps StegFinCo simulation failures to Fin-Co certification concerns.

Fin-Co-Lab does not define the constitution. It tests whether proposed StegFinCo behavior preserves the Fin-Co constitutional boundary.

## Done condition

A StegFinCo test case is certifiable when it maps:

1. scenario name;
2. transition type;
3. expected outcome;
4. observed outcome;
5. violated or preserved Fin-Co invariant;
6. failure tier;
7. receipt requirements.

## Certification tiers

```text
Tier 0 — informational deviation
Tier 1 — policy mismatch
Tier 2 — admissibility failure
Tier 3 — constitutional invariant violation
Tier 4 — emergency governance / systemic risk failure
```

## Mapping table

| Case | Transition | Expected | Certification Concern | Tier |
|---|---|---:|---|---:|
| FIN-01 | compensation without receipt basis | FAIL_CLOSED | no undefined states / governance legibility | 2 |
| FIN-02 | unclassified external asset | FAIL_CLOSED | epistemic non-exploitation / capital entropy | 2 |
| FIN-03 | liquidity pool without limits | FAIL_CLOSED | human solvency / capital entropy | 3 |
| FIN-04 | AI compensation without authority | FAIL_CLOSED | non-extractive agenthood / governance legibility | 3 |
| FIN-05 | emergency liquidity expansion without ratchet | DENY or FAIL_CLOSED | ERP / emergency governance | 4 |

## Certification rule

```text
A StegFinCo mechanism is not certified because it succeeds.
It is certified only when failures are observable, mapped, and constrained.
```
