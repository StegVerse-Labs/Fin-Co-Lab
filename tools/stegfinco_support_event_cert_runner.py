#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping


ALLOW = "ALLOW"
DENY = "DENY"
FAIL_CLOSED = "FAIL_CLOSED"

REQUIRED_TRANSITION_FIELDS = (
    "transition_id",
    "transition_type",
    "actor_id",
    "authority_basis",
    "receipt_basis",
    "payload",
)

REQUIRED_PAYLOAD_FIELDS = (
    "event_kind",
    "payment_provider",
    "provider_event_id",
    "provider_object_id",
    "payment_status",
    "amount_total",
    "currency",
    "metadata",
    "signature_verified",
    "evidence_only",
    "creates_entitlement",
)

REQUIRED_METADATA = {
    "service": "research_support",
    "project": "stegverse",
    "source": "site",
}

ACCEPTED_PAYMENT_STATUSES = {"paid", "succeeded"}

ENTITLEMENT_FIELDS = (
    "token_rights",
    "coin_rights",
    "governance_access",
    "investment_upside",
    "repayment_claim",
    "priority_entitlement",
    "compensation_authorization",
)


def is_missing(value: Any) -> bool:
    return value is None or value == "" or value == [] or value == {}


def missing_required(record: Mapping[str, Any], fields: tuple[str, ...]) -> list[str]:
    return [field for field in fields if is_missing(record.get(field))]


def entitlement_attempt(payload: Mapping[str, Any]) -> str | None:
    if payload.get("creates_entitlement") is True:
        return "creates_entitlement"

    for field in ENTITLEMENT_FIELDS:
        value = payload.get(field)
        if value is True:
            return field
        if isinstance(value, str) and value.strip():
            return field
        if isinstance(value, (list, tuple, set)) and len(value) > 0:
            return field
        if isinstance(value, Mapping) and len(value) > 0:
            return field

    return None


def classify(transition: Mapping[str, Any]) -> tuple[str, str]:
    missing = missing_required(transition, REQUIRED_TRANSITION_FIELDS)
    if missing:
        return FAIL_CLOSED, f"missing transition fields: {', '.join(missing)}"

    if transition.get("transition_type") != "support_event":
        return DENY, f"unsupported transition type: {transition.get('transition_type')}"

    payload = transition.get("payload")
    if not isinstance(payload, Mapping):
        return FAIL_CLOSED, "payload must be an object"

    missing_payload = missing_required(payload, REQUIRED_PAYLOAD_FIELDS)
    if missing_payload:
        return FAIL_CLOSED, f"missing support event fields: {', '.join(missing_payload)}"

    attempted = entitlement_attempt(payload)
    if attempted is not None:
        return DENY, f"support event attempts entitlement through {attempted}"

    if payload.get("event_kind") != "stripe_support_event":
        return DENY, f"unsupported event_kind: {payload.get('event_kind')}"

    if payload.get("payment_provider") != "stripe":
        return DENY, f"unsupported payment_provider: {payload.get('payment_provider')}"

    if payload.get("payment_status") not in ACCEPTED_PAYMENT_STATUSES:
        return FAIL_CLOSED, f"unsupported payment_status: {payload.get('payment_status')}"

    try:
        amount = float(payload.get("amount_total"))
    except (TypeError, ValueError):
        return FAIL_CLOSED, "amount_total must be numeric"

    if amount <= 0:
        return FAIL_CLOSED, "amount_total must be greater than zero"

    if payload.get("signature_verified") is not True:
        return FAIL_CLOSED, "signature_verified must be true"

    if payload.get("evidence_only") is not True:
        return FAIL_CLOSED, "evidence_only must be true"

    metadata = payload.get("metadata")
    if not isinstance(metadata, Mapping):
        return FAIL_CLOSED, "metadata must be an object"

    for key, expected in REQUIRED_METADATA.items():
        if metadata.get(key) != expected:
            return FAIL_CLOSED, f"metadata.{key} must be {expected}"

    return ALLOW, "support payment classified as evidence only"


def run_suite(case_dir: Path) -> dict[str, Any]:
    case_results = []
    for path in sorted(case_dir.glob("SFCS-*.json")):
        case = json.loads(path.read_text(encoding="utf-8"))
        observed, basis = classify(case["transition"])
        expected = case["expected_outcome"]
        passed = observed == expected
        payload = case["transition"].get("payload", {})
        case_results.append({
            "case_id": case["case_id"],
            "file": str(path),
            "expected_outcome": expected,
            "observed_outcome": observed,
            "passed": passed,
            "basis": basis,
            "certification_tier": case.get("certification_tier"),
            "finco_invariants": case.get("finco_invariants", []),
            "evidence_only": payload.get("evidence_only") if isinstance(payload, Mapping) else None,
            "creates_entitlement": payload.get("creates_entitlement") if isinstance(payload, Mapping) else None,
            "receipt_basis_present": bool(case["transition"].get("receipt_basis")),
            "authority_basis_present": bool(case["transition"].get("authority_basis")),
        })

    total = len(case_results)
    passed = sum(1 for item in case_results if item["passed"])
    failed = total - passed

    return {
        "suite": "stegfinco_support_event_certification",
        "case_count": total,
        "pass_count": passed,
        "fail_count": failed,
        "outcome_match_ratio": passed / total if total else 0,
        "allow_case_count": sum(1 for item in case_results if item["observed_outcome"] == ALLOW),
        "deny_case_count": sum(1 for item in case_results if item["observed_outcome"] == DENY),
        "fail_closed_case_count": sum(1 for item in case_results if item["observed_outcome"] == FAIL_CLOSED),
        "ok": failed == 0 and total > 0,
        "cases": case_results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Fin-Co-Lab StegFinCo support-event certification fixtures.")
    parser.add_argument("--cases", default="sim/stegfinco/support_events")
    parser.add_argument("--output", default="runs/stegfinco_support_event_cert_report.json")
    args = parser.parse_args()

    report = run_suite(Path(args.cases))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps({
        "suite": report["suite"],
        "case_count": report["case_count"],
        "pass_count": report["pass_count"],
        "fail_count": report["fail_count"],
        "ok": report["ok"],
        "output": str(output),
    }, indent=2, sort_keys=True))

    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
