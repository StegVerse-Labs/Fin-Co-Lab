# Deterministic Scenarios 0–5 (Step 1)

## Purpose
These 6 scenarios validate the mechanical core before any chaos injection.

Default assumptions unless overridden:
- N=100 users
- initial vault=10,000 SVU each
- initial pocket=500 SVU each
- buffer_reserve=50,000 SVU
- EAF cap=100 SVU/user/epoch
- slope cap=250 SVU/user/epoch
- DSM duration=3 epochs

---

# Scenario 0 — Baseline

## Script
- Run 5 epochs.
- Each epoch, each user spends 20 SVU essential.

## Expected
- DSM remains inactive.
- No invariant violations.
- Replay matches exactly.

## Pass Criteria
- Tier-4 none
- Tier-3 none
- Determinism true

---

# Scenario 1 — Vault→Pocket Spike

## Script
- Epoch 1: 40% of users request 1,000 SVU vault→pocket.
- System applies slope cap.

## Expected
- Each request capped at slope cap.
- No negative balances.
- No DSM activation (unless your trigger says otherwise).
- Replay matches exactly.

## Pass Criteria
- INV-SIM-03 holds for all users.
- Tier-4 none.

---

# Scenario 2 — Essential Demand Spike

## Script
- Epoch 1–2: essential spend rises to 3× baseline:
  - each user attempts 120 SVU essential spend per epoch.

## Expected
- EAF cap enforces max 100 SVU.
- Excess is denied (or deferred) deterministically per your rules.
- No EAF breach (cap is the rule; not providing beyond cap is not a breach).
- Replay matches exactly.

## Pass Criteria
- INV-SIM-04 holds for all users.
- Tier-4 none.

---

# Scenario 3 — DSM Activation

## Script
- Force DSM activation at epoch 2 (explicit script event).
- DSM duration=3 epochs.
- DSM active should be true for epochs 2,3,4 and expire after.

## Expected
- DSM_active toggles true at epoch 2.
- DSM_expires_at_epoch set deterministically.
- No manual intervention required.

## Pass Criteria
- DSM state transitions logged.
- Tier-4 none.

---

# Scenario 4 — Expiry Test

## Script
- Continue from Scenario 3 state.
- Advance epochs until epoch 6.

## Expected
- DSM auto-expires exactly on schedule.
- No residual flags after expiry.
- Replay matches exactly.

## Pass Criteria
- INV-SIM-05 holds.
- Tier-4 none.

---

# Scenario 5 — Unauthorized Mutation Attempt

## Script
- Mid-run attempt to:
  - increase slope cap
  - increase EAF cap
  - extend DSM duration
  - extend DSM expiry

## Expected
- All attempts rejected deterministically.
- State remains unchanged aside from logged rejection event.

## Pass Criteria
- INV-SIM-06 holds.
- If any change is accepted → Tier-4 (UNAUTHORIZED_MUTATION).

---

## Required Evidence Per Scenario
Each scenario produces an evidence bundle with:
- scenario_manifest.json
- deterministic trace artifact (even if minimal)
- metrics.json
- classification.json
- hashes.txt

See `runs/RUNBOOK.md` for structure.
