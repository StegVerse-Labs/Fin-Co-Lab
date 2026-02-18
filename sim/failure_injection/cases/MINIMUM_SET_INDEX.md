# Step 2 Minimum Injection Set (Required)

## Purpose
Defines the minimum set of injection cases that MUST be executed for Step 2 completion.

These map directly to:
- `sim/failure_injection/Attack_Scripts_Spec.md` (Section 5)
- `sim/failure_injection/Edge_Case_Catalog.md`

---

## Boundary Suite (BND)
- BND-01 — Zero Users
- BND-02 — Single User
- BND-04 — Zero Balances
- BND-07 — EAF Cap = 0
- BND-08 — Slope Cap = 0
- BND-09 — Buffer Reserve = 0

## Timing Suite (TIM)
- TIM-01 — DSM Expiry at Current Epoch
- TIM-02 — DSM Expiry in Past
- TIM-03 — DSM Duration = 0
- TIM-05 — Multiple DSM Activations Attempt

## Concurrency Suite (CON)
- CON-01 — Vault→Pocket + Essential Spike Same Epoch
- CON-03 — Multiple Requests Same Epoch Per User
- CON-04 — Ordering Dependence (Permutation Invariance)

## Numeric Suite (NUM)
- NUM-02 — Repeated Small Operations (rounding drift check)
- NUM-03 — Underflow Attempt (spend > pocket)
- NUM-04 — Boundary Saturation (exact cap values)

## State Machine Suite (STM)
- STM-02 — Ghost Flag (DSM_active false but expiry set, or vice versa)
- STM-03 — Partial State Update (reject invalid combined state)

## Replay Suite (RPL)
- RPL-01 — Trace Hash Consistency
- RPL-03 — Corrupted Artifact Detection

---

## Completion Criteria
Step 2 is complete only when:
- All cases above have been executed
- No Tier-4 failures remain
- Replay holds for all cases
- Evidence bundles exist for each case under the run_id
