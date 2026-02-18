# Fin-Co-Lab — Deterministic Simulation & Red-Team Wind Tunnel

**Fin-Co-Lab** is the simulation and certification execution lab for **Fin-Co** (Financial Coherence Architecture).

This repo is intentionally **not** the canonical specification.
That lives in **StegVerse-Labs/Fin-Co**.

Fin-Co-Lab exists to:
- Run deterministic simulations of core Fin-Co mechanisms
- Inject adversarial stress (red-team) in controlled ways
- Produce evidence bundles and frontier maps
- Validate certification requirements without polluting the spec repo

---

## Relationship to Fin-Co (Canonical Spec)

- **Fin-Co** (spec repo) defines invariants, protocols, constraints, and certification rules.
- **Fin-Co-Lab** implements simulations that map to those rules and produces auditable run artifacts.

See: `SPEC_LINKS.md`

---

## What’s In Here

- `sim/core_state.md` — minimal state model for deterministic simulation (Step 1)
- `sim/scenarios/Scenario_0_to_5.md` — the first 6 deterministic scenarios (Step 1)
- `sim/metrics/metrics_spec.md` — pass/fail measurements
- `sim/seeds.md` — seed policy for deterministic replay
- `runs/RUNBOOK.md` — iPhone-friendly run procedure and archive rules
- `cert/CERT_MAPPING.md` — mapping sim failures → Fin-Co failure tiers

---

## Phase Order (Execution Discipline)

1) Minimal deterministic simulation core (Scenario 0..5)
2) Failure injection (boundary/edge-case attacks)
3) UX comprehension drills (human-facing)
4) MVQL dashboard prototype (measurement-only)

---

## Non-Goals

This repo is not:
- A currency implementation
- A banking system
- A market
- A production deployment

It is a controlled lab environment.

---

## License

Add your preferred license file in this repo as needed.
