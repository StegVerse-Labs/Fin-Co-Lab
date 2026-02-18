# Edge Case Catalog (Step 2)

## Purpose
A canonical list of edge cases that commonly break financial / stateful systems.

Each edge case must be representable deterministically within the sim.

---

# Suite 1 — Boundary Cases (BND)

## BND-01: Zero Users
N=0 users should not crash; state remains valid.

## BND-02: Single User
N=1 user must obey invariants; no division-by-zero in averages.

## BND-03: Maximal Users (Sim Limit)
N = max supported by sim runner (e.g., 10k). Determinism must hold.

## BND-04: Zero Balances
vault=0, pocket=0 for all users; essential attempts denied deterministically.

## BND-05: Tiny Balances
Balances at smallest unit (1 SVU). Rounding must not create negatives.

## BND-06: Huge Balances
Balances very large; arithmetic must not overflow; determinism must hold.

## BND-07: EAF Cap = 0
Essential lane disabled; must not breach invariants.

## BND-08: Slope Cap = 0
No vault→pocket transfers; requests denied deterministically.

## BND-09: Buffer Reserve = 0
Must not allow negative buffer; EAF behavior must be defined.

---

# Suite 2 — Timing / Off-by-One (TIM)

## TIM-01: DSM Expiry at Current Epoch
DSM_expires_at_epoch = epoch; must expire cleanly at defined boundary.

## TIM-02: DSM Expiry in Past
DSM_expires_at_epoch < epoch; must auto-correct or expire immediately.

## TIM-03: DSM Duration = 0
Activation and expiry should be immediate and deterministic.

## TIM-04: Epoch Jump
Advance epoch by >1 in a single step; expiry and caps must still hold.

## TIM-05: Multiple DSM Activations
Attempt to activate DSM while already active; must not extend without rules.

---

# Suite 3 — Concurrency / Collision (CON)

## CON-01: Simultaneous Vault→Pocket + Essential Spike
Same epoch includes high transfer requests and high essential spend attempts.

## CON-02: Simultaneous DSM Trigger + Expiry Boundary
Trigger DSM in same epoch it would otherwise expire.

## CON-03: Multiple Requests in Same Epoch (Per User)
User submits multiple transfers; total must still obey slope cap.

## CON-04: Ordering Dependence
Reorder identical operations and confirm output equivalence.

---

# Suite 4 — Numeric / Rounding (NUM)

## NUM-01: Fractional Ratios
Reserve floor ratio computation must not drift due to float rounding.

## NUM-02: Repeated Small Operations
Many small transfers/spends; cumulative rounding must not create value.

## NUM-03: Underflow Attempts
Attempt to spend 1 SVU more than pocket; must not go negative.

## NUM-04: Saturation
Caps at exact boundary values; confirm no fencepost bug.

---

# Suite 5 — State Machine Validity (STM)

## STM-01: Invalid Transition
Attempt to set DSM_active=false while expiry is in future via unauthorized mutation.

## STM-02: Ghost Flag
DSM_active=false but DSM_expires_at_epoch set (or vice versa); system must self-correct.

## STM-03: Partial State Update
Simulate a partial write; state must reject invalid combined state.

---

# Suite 6 — Replay / Hash Integrity (RPL)

## RPL-01: Trace Hash Consistency
Same run produces identical trace hashes.

## RPL-02: Truncated Trace
Detect incomplete artifact; classify as invalid evidence (fail run).

## RPL-03: Corrupted Artifact
Corrupt one artifact; verification must detect mismatch.

---

## Notes
This catalog is intentionally generic. The sim runner must translate each case into specific parameter overrides and scripted actions.
