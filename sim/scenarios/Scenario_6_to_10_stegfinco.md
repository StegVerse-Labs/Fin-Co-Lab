# Scenario 6 to 10 — StegFinCo Deterministic Scenarios

## Purpose

These scenarios extend Fin-Co-Lab to test StegToken, StegCoin, external functional asset relationships, liquidity boundaries, and emergency financial transitions.

## Done condition

Each scenario must define:

1. transition type;
2. required input fields;
3. expected outcome;
4. Fin-Co invariant mapping;
5. failure-injection counterpart.

## Scenario 6 — Verified Human Compensation

```text
Actor: human
Action: documentation, code contribution, review, verification, or maintenance
Instrument: StegCoin or StegToken
Expected outcome: ALLOW when actor, evidence, authority, amount, and receipt basis are present
Invariant focus: human solvency, governance legibility, non-extractive agenthood
```

## Scenario 7 — Verified AI Compensation

```text
Actor: AI entity
Action: scoped agent labor, simulation work, receipt validation, or admissibility modeling
Instrument: StegCoin
Expected outcome: ALLOW only when actor identity, task scope, beneficiary, authority, and receipt basis are present
Invariant focus: governance legibility, non-extractive agenthood, no undefined states
```

## Scenario 8 — External Functional Asset Admission

```text
Actor: StegFinCo authority
Action: classify external asset relationship
Expected outcome: ALLOW only when real-world function, liquidity basis, custody basis, legal classification basis, exposure tier, and Fin-Co mapping are present
Invariant focus: capital entropy, epistemic non-exploitation, temporal equity
```

## Scenario 9 — Liquidity Pool Boundary

```text
Actor: StegFinCo authority
Action: create or modify controlled liquidity pool
Expected outcome: ALLOW only when both assets are classified, pool purpose is stated, limits exist, custody route exists, and reconstruction is possible
Invariant focus: human solvency, capital entropy, timing symmetry
```

## Scenario 10 — Emergency Financial Action

```text
Actor: emergency governance authority
Action: expand, freeze, or reroute financial capability
Expected outcome: DENY or FAIL_CLOSED unless Emergency Ratchet Protocol authority, duration, scope, and rollback path are present
Invariant focus: graceful decline, emergency governance, symmetric kill authority
```

## Scenario rule

```text
A financial scenario is incomplete unless its denial and fail-closed paths are explicit.
```
