# UX Drill Playbook (Step 3)

## Purpose

Step 3 tests whether humans interacting with Fin-Co mechanisms:

- Understand core guardrails
- Recognize caps and expiry
- Avoid panic cascades
- Avoid surrendering autonomy
- Interpret DSM correctly
- Interpret EAF correctly

Without:

- Scoring individuals
- Punishing misunderstanding
- Creating behavioral control systems

This is a comprehension and clarity test only.

---

## Core Principle

UX drills measure:
- System clarity
- Communication adequacy
- Human confusion vectors

They do NOT measure:
- User competence
- User intelligence
- Eligibility
- Moral behavior

---

## What Step 3 Tests

1) Can users understand slope caps?
2) Can users understand essential caps?
3) Do users understand DSM expiry?
4) Can users distinguish denial vs collapse?
5) Can users detect phishing-style misinformation?
6) Do users understand that no master authority exists?

---

## Structure of a Drill

Each drill must contain:

- Scenario prompt (clear and simple)
- User-facing system message
- Multiple possible user responses
- Expected safe response(s)
- Observed confusion patterns
- System improvement recommendation

---

## Execution Rules

- Drills may be simulated or run with volunteer testers.
- No personal identifiers recorded.
- Only aggregate confusion patterns logged.
- No penalties.
- No gating access based on results.

---

## Evidence Per Drill

For each drill:

- `drill_manifest.json`
- `prompt.md`
- `system_message.md`
- `response_matrix.json`
- `analysis.md`
- `aggregate_results.json`

---

## Pass Criteria (Step 3)

Step 3 PASS if:

- No drill reveals systemic misunderstanding of invariants.
- Confusion does not produce structural fragility (panic cascades).
- No system message implies hidden authority.
- No message implies permanence of emergency state.

If misunderstanding consistently appears:
- UX must be revised.
- Rerun drill.
