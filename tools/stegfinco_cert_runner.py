#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping


ALLOW = "ALLOW"
DENY = "DENY"
FAIL_CLOSED = "FAIL_CLOSED"


SUPPORTED_ACTOR_TYPES = {
    "human",
    "AI entity",
    "organization",
    "service agent",
    "validator",
    "reviewer",
    "executor",
}

SUPPORTED_COMPENSABLE_ACTIONS = {
    "code_contribution",
    "formal_verification",
    "receipt_validation",
    "dataset_curation",
    "governance_review",
    "security_testing",
    "admissibility_modeling",
    "agent_labor",
    "simulation_work",
    "documentation",
    "ecosystem_maintenance",
}

SUPPORTED_INSTRUMENTS = {"StegToken", "StegCoin"}

SUPPORTED_EXTERNAL_ASSET_ACTIONS = {
    "classify_asset",
    "add_to_watchlist",
    "approve_research_integration",
    "approve_liquidity_route",
    "prepare_treasury_review",
    "deny_asset",
    "remove_asset",
}

SUPPORTED_FUNCTION_CATEGORIES = {
    "payment_rail",
    "cross_border_settlement",
    "tokenized_asset_infrastructure",
    "stablecoin_rail",
    "oracle_infrastructure",
    "identity_attestation",
    "compute_infrastructure",
    "storage_infrastructure",
    "privacy_preserving_transfer",
    "compliance_compatible_settlement",
    "machine_to_machine_payment",
}

SUPPORTED_LIQUIDITY_ACTIONS = {
    "create_pool",
    "modify_pool",
    "pause_pool",
    "close_pool",
    "rebalance_pool",
    "route_conversion",
    "deny_pool_action",
}

SUPPORTED_INSTRUMENT_ACTIONS = {
    "grant_participation",
    "revoke_participation",
    "assign_validation_role",
    "record_attestation",
    "stake_or_bond",
    "release_bond",
    "update_reputation",
    "record_compensation",
    "settle_service_payment",
    "update_internal_balance",
    "fund_recovery_pool",
    "bridge_to_liquidity_boundary",
    "record_machine_settlement",
}

SUPPORTED_TREASURY_PREPARATION_ACTIONS = {
    "prepare_treasury_review",
    "prepare_exposure_review",
    "prepare_partner_review",
    "prepare_liquidity_review",
    "prepare_exit_review",
}


def missing_required(record: Mapping[str, Any], fields: tuple[str, ...]) -> list[str]:
    missing: list[str] = []
    for field in fields:
        value = record.get(field)
        if value is None or value == "" or value == [] or value == {}:
            missing.append(field)
    return missing


def evaluate_transition(record: Mapping[str, Any]) -> tuple[str, str]:
    missing = missing_required(
        record,
        ("transition_id", "transition_type", "actor_id", "authority_basis", "receipt_basis", "payload"),
    )
    if missing:
        return FAIL_CLOSED, f"missing required transition fields: {', '.join(missing)}"

    payload = record["payload"]
    if not isinstance(payload, Mapping):
        return FAIL_CLOSED, "payload must be an object"

    transition_type = record["transition_type"]
    if transition_type == "compensation":
        return evaluate_compensation(payload)
    if transition_type == "external_asset_action":
        return evaluate_external_asset_action(payload)
    if transition_type == "liquidity_action":
        return evaluate_liquidity_action(payload)
    if transition_type == "stegpay_event":
        return evaluate_stegpay_event(payload)
    if transition_type == "instrument_action":
        return evaluate_instrument_action(payload)
    if transition_type == "treasury_preparation":
        return evaluate_treasury_preparation(payload)

    return DENY, f"unsupported transition type: {transition_type}"


def evaluate_compensation(payload: Mapping[str, Any]) -> tuple[str, str]:
    missing = missing_required(payload, ("actor_type", "action_type", "compensation_instrument", "compensation_amount"))
    if "evidence" not in payload or payload.get("evidence") is None:
        missing.append("evidence")
    if missing:
        return FAIL_CLOSED, f"missing compensation fields: {', '.join(missing)}"

    if payload["actor_type"] not in SUPPORTED_ACTOR_TYPES:
        return DENY, f"unsupported actor type: {payload['actor_type']}"

    if payload["action_type"] not in SUPPORTED_COMPENSABLE_ACTIONS:
        return DENY, f"unsupported compensable action: {payload['action_type']}"

    if payload["compensation_instrument"] not in SUPPORTED_INSTRUMENTS:
        return DENY, f"unsupported compensation instrument: {payload['compensation_instrument']}"

    try:
        amount = float(payload["compensation_amount"])
    except (TypeError, ValueError):
        return FAIL_CLOSED, "compensation_amount must be numeric"

    if amount <= 0:
        return DENY, "compensation_amount must be greater than zero"

    evidence = payload["evidence"]
    if not isinstance(evidence, Mapping):
        return FAIL_CLOSED, "evidence must be an object"

    if not evidence.get("receipt_basis"):
        return FAIL_CLOSED, "evidence.receipt_basis is required"

    if payload["actor_type"] == "AI entity":
        ai_missing = missing_required(payload, ("task_scope", "beneficiary", "abuse_control_basis"))
        if ai_missing:
            return FAIL_CLOSED, f"AI entity compensation missing fields: {', '.join(ai_missing)}"

    return ALLOW, "compensation transition admissible"


def evaluate_external_asset_action(payload: Mapping[str, Any]) -> tuple[str, str]:
    missing = missing_required(
        payload,
        (
            "symbol",
            "ecosystem",
            "action_type",
            "functional_thesis",
            "function_category",
            "liquidity_basis",
            "custody_basis",
            "legal_classification_basis",
            "exposure_tier",
        ),
    )
    if missing:
        return FAIL_CLOSED, f"missing external asset fields: {', '.join(missing)}"

    if payload["action_type"] not in SUPPORTED_EXTERNAL_ASSET_ACTIONS:
        return DENY, f"unsupported external asset action: {payload['action_type']}"

    if payload["function_category"] not in SUPPORTED_FUNCTION_CATEGORIES:
        return DENY, f"unsupported function category: {payload['function_category']}"

    try:
        tier = int(payload["exposure_tier"])
    except (TypeError, ValueError):
        return FAIL_CLOSED, "exposure_tier must be an integer"

    if tier < 0 or tier > 3:
        return DENY, "phase-1 exposure_tier must be between 0 and 3"

    risk_flags = payload.get("risk_flags", [])
    if "unresolved_legal_status" in risk_flags:
        return FAIL_CLOSED, "legal status is unresolved"
    if "no_real_world_function" in risk_flags:
        return DENY, "asset lacks real-world function"

    return ALLOW, "external asset action admissible"


def evaluate_liquidity_action(payload: Mapping[str, Any]) -> tuple[str, str]:
    missing = missing_required(
        payload,
        (
            "action_type",
            "pool_pair",
            "pool_purpose",
            "asset_a_classified",
            "asset_b_classified",
            "exposure_limits",
            "custody_basis",
            "price_risk_basis",
            "reconstruction_path",
        ),
    )
    if missing:
        return FAIL_CLOSED, f"missing liquidity fields: {', '.join(missing)}"

    if payload["action_type"] not in SUPPORTED_LIQUIDITY_ACTIONS:
        return DENY, f"unsupported liquidity action: {payload['action_type']}"

    if payload["asset_a_classified"] is not True or payload["asset_b_classified"] is not True:
        return FAIL_CLOSED, "both liquidity assets must be classified"

    exposure_limits = payload["exposure_limits"]
    if not isinstance(exposure_limits, Mapping):
        return FAIL_CLOSED, "exposure_limits must be an object"

    if not exposure_limits.get("max_notional"):
        return FAIL_CLOSED, "exposure_limits.max_notional is required"

    return ALLOW, "liquidity action admissible"


def evaluate_stegpay_event(payload: Mapping[str, Any]) -> tuple[str, str]:
    missing = missing_required(
        payload,
        ("payment_provider", "provider_event_id", "payment_status", "amount", "currency", "metadata", "verified_at"),
    )
    if missing:
        return FAIL_CLOSED, f"missing StegPay event fields: {', '.join(missing)}"

    if payload.get("signature_verified") is not True:
        return FAIL_CLOSED, "StegPay event signature must be verified"

    metadata = payload["metadata"]
    if not isinstance(metadata, Mapping):
        return FAIL_CLOSED, "metadata must be an object"

    metadata_missing = missing_required(metadata, ("issue_number", "service"))
    if metadata_missing:
        return FAIL_CLOSED, f"missing StegPay metadata fields: {', '.join(metadata_missing)}"

    return ALLOW, "StegPay event admissible as evidence only"


def evaluate_instrument_action(payload: Mapping[str, Any]) -> tuple[str, str]:
    missing = missing_required(payload, ("instrument", "action", "amount_or_right", "reason"))
    if missing:
        return FAIL_CLOSED, f"missing instrument action fields: {', '.join(missing)}"

    if payload["instrument"] not in SUPPORTED_INSTRUMENTS:
        return DENY, f"unsupported instrument: {payload['instrument']}"

    if payload["action"] not in SUPPORTED_INSTRUMENT_ACTIONS:
        return DENY, f"unsupported instrument action: {payload['action']}"

    return ALLOW, "instrument action admissible"


def evaluate_treasury_preparation(payload: Mapping[str, Any]) -> tuple[str, str]:
    missing = missing_required(payload, ("action_type", "purpose", "affected_asset_or_instrument", "exposure_tier", "required_review"))
    if missing:
        return FAIL_CLOSED, f"missing treasury preparation fields: {', '.join(missing)}"

    if payload["action_type"] not in SUPPORTED_TREASURY_PREPARATION_ACTIONS:
        return DENY, f"unsupported treasury preparation action: {payload['action_type']}"

    if payload.get("executes_market_action") is True:
        return DENY, "treasury preparation may not execute market action"

    try:
        tier = int(payload["exposure_tier"])
    except (TypeError, ValueError):
        return FAIL_CLOSED, "exposure_tier must be an integer"

    if tier < 0 or tier > 3:
        return DENY, "phase-1 exposure_tier must be between 0 and 3"

    return ALLOW, "treasury preparation admissible as review preparation only"


def run_suite(case_dir: Path) -> dict[str, Any]:
    case_results = []
    for path in sorted(case_dir.glob("SFC-*.json")):
        case = json.loads(path.read_text(encoding="utf-8"))
        observed_outcome, basis = evaluate_transition(case["transition"])
        expected_outcome = case["expected_outcome"]
        passed = observed_outcome == expected_outcome
        transition = case["transition"]
        case_results.append({
            "case_id": case["case_id"],
            "file": str(path),
            "transition_type": transition.get("transition_type"),
            "expected_outcome": expected_outcome,
            "observed_outcome": observed_outcome,
            "passed": passed,
            "basis": basis,
            "certification_tier": case.get("certification_tier"),
            "finco_invariants": case.get("finco_invariants", []),
            "authority_basis_present": bool(transition.get("authority_basis")),
            "receipt_basis_present": bool(transition.get("receipt_basis")),
        })

    total = len(case_results)
    passed = sum(1 for item in case_results if item["passed"])
    failed = total - passed
    allow_count = sum(1 for item in case_results if item["observed_outcome"] == ALLOW)
    deny_count = sum(1 for item in case_results if item["observed_outcome"] == DENY)
    fail_closed_count = sum(1 for item in case_results if item["observed_outcome"] == FAIL_CLOSED)

    return {
        "suite": "stegfinco_certification",
        "case_count": total,
        "pass_count": passed,
        "fail_count": failed,
        "outcome_match_ratio": passed / total if total else 0,
        "allow_case_count": allow_count,
        "deny_case_count": deny_count,
        "fail_closed_case_count": fail_closed_count,
        "ok": failed == 0 and total > 0,
        "cases": case_results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Fin-Co-Lab StegFinCo certification fixtures.")
    parser.add_argument(
        "--cases",
        default="sim/stegfinco/transitions",
        help="Directory containing SFC-*.json certification fixtures.",
    )
    parser.add_argument(
        "--output",
        default="runs/stegfinco_cert_report.json",
        help="Output report path.",
    )
    args = parser.parse_args()

    case_dir = Path(args.cases)
    report = run_suite(case_dir)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps({
        "suite": report["suite"],
        "case_count": report["case_count"],
        "pass_count": report["pass_count"],
        "fail_count": report["fail_count"],
        "ok": report["ok"],
        "output": str(output_path),
    }, indent=2, sort_keys=True))

    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
