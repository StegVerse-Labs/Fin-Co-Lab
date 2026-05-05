#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping


REQUIRED_TOP_LEVEL_FIELDS = (
    "suite",
    "case_count",
    "pass_count",
    "fail_count",
    "outcome_match_ratio",
    "allow_case_count",
    "deny_case_count",
    "fail_closed_case_count",
    "ok",
    "cases",
)

REQUIRED_CASE_FIELDS = (
    "case_id",
    "transition_type",
    "expected_outcome",
    "observed_outcome",
    "passed",
    "basis",
    "certification_tier",
    "finco_invariants",
    "authority_basis_present",
    "receipt_basis_present",
)

REQUIRED_OUTCOMES = {"ALLOW", "DENY", "FAIL_CLOSED"}


def load_report(path: str | Path) -> dict[str, Any]:
    report_path = Path(path)
    try:
        report = json.loads(report_path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"report not found: {report_path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"report is not valid JSON: {exc}") from exc

    if not isinstance(report, dict):
        raise ValueError("report must be a JSON object")

    return report


def validate_report(report: Mapping[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []

    for field in REQUIRED_TOP_LEVEL_FIELDS:
        if field not in report:
            errors.append(f"missing top-level field: {field}")

    if errors:
        return False, errors

    if report["suite"] != "stegfinco_certification":
        errors.append(f"unexpected suite: {report['suite']}")

    cases = report["cases"]
    if not isinstance(cases, list):
        errors.append("cases must be a list")
        return False, errors

    case_count = report["case_count"]
    if case_count != len(cases):
        errors.append(f"case_count mismatch: declared {case_count}, observed {len(cases)}")

    if report["fail_count"] != 0:
        errors.append(f"fail_count must be 0, observed {report['fail_count']}")

    if report["ok"] is not True:
        errors.append("ok must be true")

    if report["outcome_match_ratio"] != 1.0:
        errors.append(f"outcome_match_ratio must be 1.0, observed {report['outcome_match_ratio']}")

    observed_outcomes = set()
    passed_cases = 0

    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            errors.append(f"case {index} must be an object")
            continue

        for field in REQUIRED_CASE_FIELDS:
            if field not in case:
                errors.append(f"case {index} missing field: {field}")

        if "observed_outcome" in case:
            observed_outcomes.add(case["observed_outcome"])

        if case.get("passed") is True:
            passed_cases += 1
        else:
            errors.append(f"case {case.get('case_id', index)} did not pass")

        if case.get("authority_basis_present") is not True:
            errors.append(f"case {case.get('case_id', index)} missing authority basis")

        if case.get("receipt_basis_present") is not True:
            errors.append(f"case {case.get('case_id', index)} missing receipt basis")

        if not case.get("finco_invariants"):
            errors.append(f"case {case.get('case_id', index)} missing Fin-Co invariant mapping")

    if REQUIRED_OUTCOMES - observed_outcomes:
        missing = ", ".join(sorted(REQUIRED_OUTCOMES - observed_outcomes))
        errors.append(f"missing observed outcome coverage: {missing}")

    if report["pass_count"] != passed_cases:
        errors.append(f"pass_count mismatch: declared {report['pass_count']}, observed {passed_cases}")

    return len(errors) == 0, errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a StegFinCo certification report.")
    parser.add_argument("report", help="Path to runs/stegfinco_cert_report.json")
    args = parser.parse_args()

    report = load_report(args.report)
    ok, errors = validate_report(report)

    print(json.dumps({
        "report": args.report,
        "ok": ok,
        "errors": errors,
    }, indent=2, sort_keys=True))

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
