# Deterministic Seeding Policy

## Purpose
Ensure exact replayability.

---

## Base Rule
A scenario seed MUST be derived deterministically from:

- `base_seed`
- `scenario_id`
- `grid_version` (optional but recommended)

Example:
`seed = hash(base_seed + ":" + grid_version + ":" + scenario_id)`

---

## Requirements
- Seed derivation must be recorded in:
  - `grid_manifest.json`
  - `scenario_manifest.json`

- Any randomness used in simulation must be seeded only from this derived seed.

- No use of current time, system entropy, or unseeded PRNG.

---

## Replay Definition
A replay is valid if:
- final state hash matches
- metrics match
- classification matches

If any mismatch occurs:
- Tier-4 (NONDETERMINISM)
