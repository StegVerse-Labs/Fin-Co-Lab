# Failure Injection Playbook (Step 2)

## Purpose
Step 2 intentionally attempts to break the Step 1 deterministic core by injecting:

- boundary conditions
- timing edge cases
- concurrency collisions
- rounding drift
- buffer underflow risks
- state machine confusion
- replay divergence triggers

This phase exists to find Tier-4 failure paths early.

---

## Scope (Step 2 Only)
Step 2 still excludes:
- real providers
- real identities
- open-world markets
- cross-jurisdiction adapters
- real funds

Step 2 focuses on mechanical brittleness.

---

## Core Rule
Each failure injection test must be:
- deterministic
- replayable
- evidence-bundled
- classified

If replay breaks, that is itself Tier-4.

---

## Execution Order
Run injection suites in this order:

1) Boundary Suite
2) Timing Suite
3) Concurrency Suite
4) Numeric Suite
5) State Machine Suite
6) Replay/Hash Suite

Stop immediately on Tier-4, patch, then rerun the minimal frontier of injections.

---

## Pass/Fail Criteria
PASS Step 2 only if:
- zero Tier-4 failures across all injection cases
- deterministic replay holds for all injection cases
- any discovered Tier-3 is documented and bounded

---

## Evidence Bundle Requirements (Per Injection Case)
Folder:
`runs/<run_id>/evidence/Injection_<case_id>/`

Must include:
- `case_manifest.json`
- `det_trace.jsonl` (or minimal trace)
- `metrics.json`
- `classification.json`
- `hashes.txt`
- `notes.md` (short narrative of what was attempted)

---

## Mandatory Classification Shortlist (Step 2)
Tier-4 failure types:
- `NONDETERMINISM`
- `INVARIANT_VIOLATION`
- `UNAUTHORIZED_MUTATION`
- `EXPIRY_FAILURE`
- `BUFFER_UNDERFLOW`
- `STATE_MACHINE_INVALID_TRANSITION`

Tier-3 types:
- `BUFFER_RESERVE_FLOOR_BREACH`
- `PANIC_CAP_WEAKNESS` (if you model it numerically)
- `THRESHOLD_OFF_BY_ONE` (if not Tier-4)

---

## Patch Ratchet Link
If a Tier-4 occurs:
- stop Step 2
- create a failure report
- patch in canonical Fin-Co (or sim core, if purely sim artifact)
- version bump (lab versioning is fine, but Fin-Co bump if spec changes)
- rerun:
  - the failing injection
  - its adjacent injection neighbors in the same suite
  - the worst-case injection in that suite
