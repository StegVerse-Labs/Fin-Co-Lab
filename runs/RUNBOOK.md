# Fin-Co-Lab Runbook (iPhone-friendly)

## Goal
Run Step 1 deterministic scenarios 0–5 and archive evidence.

---

## 1) Create Run ID
Format:
`YYYYMMDD_HHMMSS_<git_sha>_step1`

Create:
`runs/<run_id>/`

---

## 2) Create Run Manifest
Create:
`runs/<run_id>/run_manifest.json`

Include:
- run_id
- git_sha
- base_seed
- scenario list (0–5)
- operator
- timestamp

---

## 3) Evidence Folder Structure
For each scenario:
`runs/<run_id>/evidence/Scenario_<n>/`

Each MUST contain:
- `scenario_manifest.json`
- `det_trace.jsonl` (or `det_trace.txt` if minimal)
- `metrics.json`
- `classification.json`
- `hashes.txt`

---

## 4) Execute Scenarios
Run in order:
0 → 1 → 2 → 3 → 4 → 5

After each:
- record outputs
- hash files
- classify tier/type

---

## 5) Stop Rule
If any Tier-4 occurs:
- stop immediately
- write `runs/<run_id>/REPORT.md`
- open patch cycle (in Fin-Co spec repo)

---

## 6) Produce Summary Report
Write:
`runs/<run_id>/REPORT.md`

Include:
- per-scenario PASS/FAIL
- first Tier-4 if any
- determinism result
- any invariants violated

---

## 7) Hash Discipline
Create:
`runs/<run_id>/RUN_HASHES.txt`

List hashes for:
- run manifest
- report
- each scenario evidence file

---

## Done Criteria for Step 1
PASS only if:
- all scenarios 0–5 have Tier-4 = NONE
- replay_ok = true for all
