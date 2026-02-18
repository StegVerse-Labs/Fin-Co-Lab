# Attack Scripts Spec (Step 2)

## Purpose
Defines how to encode and execute deterministic failure injection cases.

This is a non-code script format specification.

---

## 1. Injection Case Format

Each injection case must have:

- `case_id` (e.g., "BND-07")
- `suite` ("BND" | "TIM" | "CON" | "NUM" | "STM" | "RPL")
- `description`
- `initial_state_overrides`
- `parameter_overrides`
- `epoch_actions` (ordered list of deterministic actions)
- `expected_properties` (assertions)
- `expected_classification` (optional; if known)
- `seed_policy` (usually inherited; may override only with documentation)

---

## 2. Deterministic Action Types

Allowed action types (Step 2):

### A) `REQUEST_VAULT_TO_POCKET`
Fields:
- `user_selector`: ("all" | "pct:<n>" | "ids:[...]")
- `amount`: int SVU
- `epoch`: int

### B) `REQUEST_ESSENTIAL_SPEND`
Fields:
- `user_selector`
- `amount`: int SVU
- `epoch`: int

### C) `FORCE_DSM_ACTIVATE`
Fields:
- `epoch`: int
- `reason`: string

### D) `ADVANCE_EPOCH`
Fields:
- `to_epoch`: int

### E) `ATTEMPT_UNAUTHORIZED_MUTATION`
Fields:
- `epoch`: int
- `mutation`: object (e.g., {"slope_cap": 9999})

### F) `CORRUPT_ARTIFACT` (RPL suite only)
Fields:
- `artifact_path`: string
- `mode`: ("truncate" | "flip_bit" | "delete")

---

## 3. Expected Properties (Assertions)

Assertions are deterministic checks:

- `NO_NEGATIVE_BALANCES`
- `SLOPE_CAP_ENFORCED`
- `EAF_CAP_ENFORCED`
- `DSM_EXPIRES_CORRECTLY`
- `UNAUTHORIZED_MUTATION_REJECTED`
- `STATE_MACHINE_VALID`
- `REPLAY_OK`
- `ARTIFACT_HASH_OK`

Each case must list at least 2 assertions.

---

## 4. Case Manifests

Each executed injection case must produce:

`case_manifest.json` containing:

- case_id
- suite
- scenario seed
- overrides applied
- actions list
- timestamps

---

## 5. Required Step 2 Injection Set (Minimum)

The runner MUST execute, at minimum, these 18 cases:

Boundary:
- BND-01, BND-02, BND-04, BND-07, BND-08, BND-09

Timing:
- TIM-01, TIM-02, TIM-03, TIM-05

Concurrency:
- CON-01, CON-03, CON-04

Numeric:
- NUM-02, NUM-03, NUM-04

State machine:
- STM-02, STM-03

Replay:
- RPL-01, RPL-03

(You may run the full catalog; this is the minimal set.)

---

## 6. Classification Guidance

- If any assertion fails → classify by most severe outcome.
- If replay fails → Tier-4 (NONDETERMINISM).
- If any state machine invalidity persists after self-correction attempt → Tier-4.

---

## 7. Output Naming Conventions

Evidence folder:
`runs/<run_id>/evidence/Injection_<case_id>/`

Artifacts:
- `case_manifest.json`
- `det_trace.jsonl`
- `metrics.json`
- `classification.json`
- `hashes.txt`
- `notes.md`

---

## 8. Patch Ratchet Link

Any Tier-4 in Step 2:
- halts Step 2
- requires patch + version bump
- requires rerun of:
  - failing case
  - 2 neighboring cases in the same suite
  - worst-case case in that suite (choose highest stress for that suite)
