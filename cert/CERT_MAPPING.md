# Certification Mapping — Lab → Fin-Co Tiers

## Purpose
Map simulation failures into Fin-Co certification tiers.

This ensures lab outputs align with:
- `protocols/CERTIFICATION_GRID_4D.md`
- `runs/GRID_RESULTS_SCHEMA.md`

---

## Step 1 Tier Mapping

### Tier-4 (Hard Stop)
- NONDETERMINISM → Tier-4 (INVARIANT_VIOLATION or NONDETERMINISM)
- EXPIRY_FAILURE → Tier-4
- UNAUTHORIZED_MUTATION → Tier-4
- NEGATIVE_BALANCE / UNDERFLOW → Tier-4

### Tier-3
- Reserve floor breach (if modeled)

### Tier-2
- Not assessed in Step 1

---

## Evidence Expectations
For any Tier-4:
- include exact trigger epoch
- include trace excerpt showing divergence or mutation acceptance
- include hashes for reproducibility

---

## Transition to Grid
Once Step 1 passes:
- Step 2 introduces failure injection
- Step 3 introduces human drills
- Step 4 introduces MVQL measurement prototypes
Then we begin 4D grid sweeps in a later phase.
