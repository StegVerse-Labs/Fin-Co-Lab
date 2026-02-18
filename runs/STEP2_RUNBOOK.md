# Step 2 Runbook — Failure Injection (iPhone-friendly)

## Goal
Execute the Step 2 minimum injection case pack and produce an auditable archive.

Step 2 PASS requires:
- All injection cases executed
- Zero unresolved Tier-4 outcomes
- Deterministic replay holds for all cases
- Evidence integrity checks pass

---

## 1) Create Run ID

Format:
`YYYYMMDD_HHMMSS_<git_sha>_step2`

Create folder:
`runs/<run_id>/`

---

## 2) Create Run Manifest

Copy:
`runs/STEP2_RUN_MANIFEST_TEMPLATE.json`

Save as:
`runs/<run_id>/run_manifest.json`

Fill in:
- git sha
- base seed
- case pack path
- operator

---

## 3) Case Pack Location

Expected location:
`sim/failure_injection/cases/minimum/`

Run all `*.json` files in that folder.

If you add cases:
- update the manifest list
- do not silently skip anything

---

## 4) Evidence Structure (Per Case)

For each injection case:
`runs/<run_id>/evidence/Injection_<case_id>/`

Must include:
- `case_manifest.json`
- `det_trace.jsonl` (or minimal trace)
- `metrics.json`
- `classification.json`
- `hashes.txt`
- `notes.md` (what happened, 3–8 lines)

---

## 5) Execution Order

Recommended order:
1) BND
2) TIM
3) CON
4) NUM
5) STM
6) RPL

Within a suite, lexicographic by case_id.

---

## 6) Stop Rule

If any case yields Tier-4 **that is not expected**:
- STOP immediately
- Write interim report
- Open patch cycle
- Rerun minimal retest set after patch

Expected Tier-4:
- RPL-03 is expected to classify Tier-4 evidence corruption detection.

All other Tier-4 outcomes are failures.

---

## 7) Retest (Minimal Set) After Patch

If a case fails Tier-4 (unexpected):

Rerun:
- the failing case
- 2 neighboring cases in same suite (closest IDs)
- the suite’s “worst case” (choose highest stress / most coupled)

Document this in the Step 2 report under Patch Log.

---

## 8) Produce Step 2 Report

Copy:
`runs/STEP2_REPORT_TEMPLATE.md`

Save as:
`runs/<run_id>/REPORT.md`

Fill it in.

---

## 9) Hash Discipline

Create:
`runs/<run_id>/RUN_HASHES.txt`

Include hashes for:
- run_manifest.json
- REPORT.md
- each evidence file across all cases

---

## 10) Done Criteria

Step 2 PASS only if:
- every case has evidence bundle
- replay_ok true for all cases except artifact-corruption detection cases where replay is not the goal
- no unresolved Tier-4 failures remain
- RPL-03 correctly detected corruption and produced expected Tier-4 classification
