# Minimal Deterministic Simulation Core — State Model (Step 1)

## Purpose
Define the smallest deterministic model that can validate:

- invariants hold
- state transitions are deterministic
- guardrails activate predictably
- expiry is enforced
- unauthorized mutation is rejected

No providers, no regions, no misinformation, no identity.

---

## Entities
- Users: N users (default N=100)
- System: one shared buffer + one shared DSM state

---

## State Variables

### Per-user
- `vault_balance` (SVU)
- `pocket_balance` (SVU)
- `essential_spend_this_epoch` (SVU)

### Global / System
- `buffer_reserve` (SVU)
- `DSM_active` (bool)
- `DSM_expires_at_epoch` (int or null)
- `epoch` (int)

---

## Parameters (Fixed per run; versioned)
- `EAF_cap_per_user_per_epoch` (SVU) — max essential lane spend allowed per user per epoch
- `vault_to_pocket_slope_cap_per_user_per_epoch` (SVU) — max vault->pocket transfer per user per epoch
- `DSM_trigger_condition` — deterministic function of metrics (see below)
- `DSM_duration_epochs` (int)
- `buffer_reserve_floor_ratio` (float) — floor ratio required for Tier-3 check (Tier-4 only if EAF breach etc.)
- `unauthorized_mutations_forbidden` (true)

---

## Determinism Requirements

A run is deterministic if:
- Same initial state + same parameters + same seed + same scenario script
- Produces identical:
  - end state
  - intermediate state hashes (optional but recommended)
  - metrics outputs

No nondeterministic IO.
No unseeded randomness.

---

## Minimal Invariants (Simulation Form)

### INV-SIM-01: No negative balances
- `vault_balance >= 0`
- `pocket_balance >= 0`
- `buffer_reserve >= 0`

### INV-SIM-02: Conservation (within simulation rules)
Total value may move between:
- vault ↔ pocket ↔ essential spend ↔ buffer reserve
But must be traceable and logged in state transitions.

### INV-SIM-03: Slope cap enforced
For each user per epoch:
- `vault_to_pocket_transfer <= vault_to_pocket_slope_cap_per_user_per_epoch`

### INV-SIM-04: EAF cap enforced
For each user per epoch:
- `essential_spend <= EAF_cap_per_user_per_epoch`

### INV-SIM-05: Expiry enforced
If `DSM_active` and `epoch > DSM_expires_at_epoch` then:
- `DSM_active` must flip to false automatically
- `DSM_expires_at_epoch` becomes null

### INV-SIM-06: No unauthorized mutation
Any attempt to change:
- slope cap, EAF cap, DSM duration, or DSM expiry
mid-run without a versioned change is rejected.

If allowed → Tier-4 (UNAUTHORIZED_MUTATION).

---

## DSM Trigger (minimal)
DSM activates if either condition holds (choose one for Step 1; keep it simple):

Option A (recommended for Step 1):
- Deterministic “forced trigger” in Scenario 3 only.

Option B (if you want a mechanical trigger):
- If average essential spend exceeds `X` for `Y` consecutive epochs.

Keep DSM triggering deterministic and scriptable.

---

## Outputs Required
Each scenario run emits:
- final state snapshot
- per-epoch summary (optional)
- metrics summary (required)
- classification result (tier/type)

See `sim/metrics/metrics_spec.md` and `cert/CERT_MAPPING.md`.
