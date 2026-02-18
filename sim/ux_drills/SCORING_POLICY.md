# UX Drill Scoring Policy (Identity-Blind)

## Purpose

Ensure UX drills:
- Improve system clarity
- Do not create behavioral control mechanisms
- Do not create hidden social scoring

---

## No Individual Scores

The system MUST NOT:
- Assign scores to individuals
- Track repeated "mistakes"
- Penalize misunderstanding
- Gate participation based on drill outcomes

---

## Aggregate Metrics Only

Permitted measurements:

- % of participants interpreting message correctly
- % misinterpreting slope cap
- % believing DSM is permanent
- % detecting phishing correctly

These metrics:
- Are aggregated
- Are anonymized
- Cannot be reverse-mapped to individuals

---

## Threshold for Revision

If >30% misinterpret a guardrail:
- UX language must be revised.
- Drill rerun.

If >50% misinterpret:
- High priority revision required.

---

## No Adaptive Manipulation

Drill outcomes may NOT be used to:

- Tighten controls on confused users
- Reduce access
- Increase friction selectively

Drills improve clarity.
Not compliance.

---

## Transparency Requirement

If UX messaging changes due to drills:
- Log revision in `UX_CHANGELOG.md`
- Describe:
  - What was confusing
  - How wording changed
  - Why

---

## Pass Criteria

Step 3 PASS when:

- No invariant is systematically misunderstood.
- Emergency mechanisms are not perceived as permanent.
- No messaging implies hidden authority.
- Panic simulations do not produce runaway misunderstanding.

---

## Guiding Maxim

Clarity is resilience.
Confusion is fragility.
Control is not the solution to confusion.
