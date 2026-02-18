# MVQL Metrics — Formula Definitions

All formulas must:

- Be deterministic
- Use integer arithmetic where possible
- Be reproducible from evidence artifacts
- Avoid individual tracking

---

# 1) Essential Access Integrity (EAI)

EAI_score =
  1 - (EAF_breach_count / total_epochs)

Expected:
EAF_breach_count = 0

If >0:
- automatic Red signal
- certification violation

---

# 2) Volatility Stress Index (VSI)

VSI =
  weighted_sum(
    normalized_vault_to_pocket_velocity,
    DSM_activation_rate,
    buffer_draw_rate
  )

Weights must be versioned.
No dynamic reweighting allowed mid-run.

---

# 3) Participation Capacity Index (PCI)

PCI =
  normalized_active_users *
  normalized_median_pocket_liquidity *
  normalized_vault_distribution_spread

Must not:
- Penalize concentration directly
- Enforce redistribution

Only measure participation health.

---

# 4) Panic Containment Index (PCI-2)

PCI2 =
  1 - (panic_spike_events / total_epochs)

Panic_spike_event defined as:
- slope cap hit > X% of users in same epoch

Threshold X must be versioned.

---

# 5) Governance Transparency Index (GTI)

GTI =
  1 - (
    missed_expiry_events +
    delayed_publication_events
  ) / total_review_events

All governance events must be logged.

---

# Required Publication Discipline

For each MVQL snapshot:
- Publish formulas used
- Publish version
- Publish timestamp
- Publish hash of underlying metrics
