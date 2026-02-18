# Step 2 Report — Failure Injection

- **Run ID:** `<run_id>`
- **Repo / Commit:** `StegVerse-Labs/Fin-Co-Lab` / `<git_sha>`
- **Base Seed:** `<base_seed>`
- **Case Pack:** `sim/failure_injection/cases/minimum/`
- **Operator:** `<name_or_role>`
- **Started:** `<ISO>`
- **Completed:** `<ISO>`

---

## 1) Executive Summary

- **Total Cases Expected:** `<n_expected>`
- **Total Cases Completed:** `<n_completed>`
- **Unexpected Tier-4 Count:** `<n_unexpected_tier4>`
- **Expected Tier-4 Count:** `<n_expected_tier4>` (should be 1: RPL-03)
- **PASS Step 2:** `<true|false>`

---

## 2) Case Results (Checklist)

List each case with:
- status: PASS / FAIL
- tier
- type
- replay_ok (if applicable)
- evidence path

Example format:

- `BND-01` — PASS — Tier 0 — NONE — replay_ok=true — `runs/<run_id>/evidence/Injection_BND-01/`
- `RPL-03` — PASS (expected failure) — Tier 4 — EVIDENCE_CORRUPTION_DETECTED — replay_ok=n/a — `...`

---

## 3) Unexpected Tier-4 Findings (If Any)

For each unexpected Tier-4:

### `<case_id>`
- Failure Type: `<type>`
- Epoch: `<t>`
- Symptom: `<short>`
- Likely Root Cause: `<short>`
- Invariant Implicated: `<list>`
- Evidence: `<path>`

---

## 4) Patch Log (If Applied)

Each patch entry:

- Patch ID: `<id>`
- Description: `<short>`
- Files changed: `<paths>`
- Version bump (lab + spec if needed): `<x.y.z>`
- Retest set: `<case_ids>`
- Outcome: `<pass/fail>`

---

## 5) Determinism & Evidence Integrity

- Determinism failures (count): `<n>`
- Evidence hash mismatches detected: `<n>`
- RPL-03 corruption detection: `<PASS/FAIL>`

---

## 6) Decision

- **Decision:** `<PASS|FAIL>`
- **Next Move:** Step 3 (UX comprehension drill scaffolding) OR patch and rerun Step 2.
