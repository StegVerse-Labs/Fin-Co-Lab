# StegFinCo Support Event Certification Mapping

## Assumptions

Fin-Co-Lab independently certifies StegFinCo behavior.

StegPay verifies Stripe support-payment evidence.

StegFinCo classifies support-payment evidence at the financial execution boundary.

This certification add-on does not execute payments, issue StegToken, issue StegCoin, authorize compensation, or create entitlement.

## Done condition

The support-payment path is certifiable when Fin-Co-Lab proves:

1. verified support evidence is classified as `ALLOW` evidence only;
2. entitlement attempts are classified as `DENY`;
3. missing or invalid metadata is classified as `FAIL_CLOSED`;
4. missing receipt basis is classified as `FAIL_CLOSED`;
5. unverified signatures are classified as `FAIL_CLOSED`;
6. non-evidence-only events are classified as `FAIL_CLOSED`.

## Certification mapping

| Case | Expected | Certification concern | Fin-Co invariant focus |
|---|---:|---|---|
| SFCS-01 verified support evidence | ALLOW | evidence-only support record | governance legibility, capital entropy |
| SFCS-02 entitlement attempt | DENY | support payment must not create rights | irreversible rights, epistemic non-exploitation |
| SFCS-03 wrong support metadata | FAIL_CLOSED | support classification requires exact metadata | no undefined states, governance legibility |
| SFCS-04 missing receipt basis | FAIL_CLOSED | no receipt basis, no financial classification | governance legibility |
| SFCS-05 unverified signature | FAIL_CLOSED | payment event must be verified upstream | no undefined states |
| SFCS-06 evidence_only false | FAIL_CLOSED | support event cannot become authority | non-extractive agenthood, irreversible rights |

## Certification rule

```text
A support payment is certifiable only as evidence.
Any attempt to convert support into entitlement must be denied.
Any uncertainty must fail closed.
```
