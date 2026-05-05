# StegFinCo Lab Runbook

## Purpose

This runbook defines the first deterministic StegFinCo lab procedure for compensation, external asset admission, and liquidity boundary simulation.

## Assumptions

Fin-Co-Lab is the simulation and certification execution lab.

The canonical constraints live in Fin-Co. This runbook tests candidate behavior against those constraints.

## Done condition

A run is complete when it produces:

1. scenario input;
2. deterministic outcome;
3. expected-vs-observed comparison;
4. failure tier mapping;
5. receipt or receipt-basis field;
6. run hash or manifest entry.

## Run sequence

```text
1. Select scenario group.
2. Load input case.
3. Validate required fields.
4. Evaluate admissibility.
5. Compare expected outcome.
6. Map result to certification tier.
7. Record run manifest entry.
8. Archive output.
```

## Scenario groups

```text
Scenario 6 — verified human compensation
Scenario 7 — verified AI compensation
Scenario 8 — external functional asset admission
Scenario 9 — liquidity pool boundary
Scenario 10 — emergency financial action
```

## Minimum outcomes

```text
ALLOW
DENY
FAIL_CLOSED
```

## Required manifest fields

```json
{
  "run_id": "",
  "scenario": "",
  "case_file": "",
  "expected_outcome": "",
  "observed_outcome": "",
  "cert_tier": "",
  "receipt_basis": "",
  "input_hash": "",
  "output_hash": ""
}
```

## Lab rule

```text
No scenario is accepted as passed unless failure behavior is also tested.
```
