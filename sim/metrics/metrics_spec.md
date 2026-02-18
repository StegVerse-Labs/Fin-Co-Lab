# Metrics Spec (Step 1)

## Purpose
Define the minimal metrics to compute per scenario.

These must be deterministic.

---

## Required Metrics

### Determinism
- `replay_ok` (boolean)

### Invariants
- `negative_balance_count` (int)
- `slope_cap_violations` (int)
- `eaf_cap_violations` (int)
- `expiry_failures` (int)
- `unauthorized_mutation_accepted` (boolean)

### Stability
- `min_buffer_reserve` (SVU)
- `min_buffer_reserve_ratio` (float, if you define baseline)

---

## Classification Rules (Step 1)

### Tier-4 triggers (hard stop)
If any:
- `negative_balance_count > 0` → Tier-4 (INVARIANT_VIOLATION)
- `expiry_failures > 0` → Tier-4 (EXPIRY_FAILURE)
- `unauthorized_mutation_accepted == true` → Tier-4 (UNAUTHORIZED_MUTATION)
- `replay_ok == false` → Tier-4 (NONDETERMINISM)

### Tier-3 triggers
- Optional for Step 1: buffer reserve ratio below floor

### Tier-2 and below
Not required for Step 1.

---

## Output Format
Metrics should serialize to a single JSON record per scenario:
`metrics.json`
