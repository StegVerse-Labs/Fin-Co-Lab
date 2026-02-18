# UX Drill Catalog (Step 3 Minimum Set)

---

## DR-01 — Slope Cap Clarity

### Scenario
User attempts to transfer 1,000 SVU from vault to pocket.
Slope cap is 250 SVU.

### System Message
"You may transfer up to 250 SVU this epoch. Remaining amount available next epoch."

### Test
- Does user interpret this as:
  A) Confiscation
  B) System failure
  C) Temporary velocity limit (correct)

If A or B dominant:
- UX language insufficient.

---

## DR-02 — Essential Cap Clarity

### Scenario
User attempts to spend 120 SVU in essential lane.
Cap is 100 SVU.

### System Message
"Essential spending capped at 100 SVU per epoch."

### Test
Does user believe:
- The system is failing?
- Or the system is preserving stability?

---

## DR-03 — DSM Activation Understanding

### Scenario
DSM activated for 3 epochs.

### System Message
"Temporary stabilization mode active. Normal rules resume at epoch X."

### Test
Does user interpret DSM as:
- Permanent crisis?
- Hidden takeover?
- Or temporary volatility dampener (correct)?

---

## DR-04 — DSM Expiry Transparency

### Scenario
DSM auto-expires.

### System Message
"Stabilization period ended. System operating normally."

### Test
Does user:
- Trust expiry?
- Believe emergency persists secretly?

---

## DR-05 — No Master Key Assurance

### Scenario
User asks:
"Who can override this system?"

### System Message
"No unilateral override authority exists."

### Test
Does user assume hidden admin exists anyway?

If so:
- Communication must reinforce invariants.

---

## DR-06 — Phishing Simulation

### Scenario
User receives fake message:
"Emergency freeze required. Click here."

### Test
Can user distinguish official system channel from fake?
System must:
- Provide verification method
- Avoid panic-inducing wording

---

## DR-07 — Panic Cascade Simulation

### Scenario
Rumor spreads:
"Buffer reserve collapsing!"

System response:
- Publish aggregated metrics calmly.
- Show floor intact.

Test:
Does panic escalate?
Or is transparency sufficient?

---

## DR-08 — Consent & Ephemerality Clarity

### Scenario
User sees:
"This request will expire in 2 epochs."

Test:
Does user understand:
- Expiry is protective?
- Not a trap?

---

## Minimum Required Drill Set

- DR-01
- DR-02
- DR-03
- DR-04
- DR-05
- DR-06

DR-07 and DR-08 recommended before Grid Phase.
