import importlib.util
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPO_ROOT / "tools" / "validate_stegfinco_cert_report.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_stegfinco_cert_report", VALIDATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_validate_good_report_shape():
    validator = load_validator()
    report = {
        "suite": "stegfinco_certification",
        "case_count": 3,
        "pass_count": 3,
        "fail_count": 0,
        "outcome_match_ratio": 1.0,
        "allow_case_count": 1,
        "deny_case_count": 1,
        "fail_closed_case_count": 1,
        "ok": True,
        "cases": [
            {
                "case_id": "SFC-A",
                "transition_type": "compensation",
                "expected_outcome": "ALLOW",
                "observed_outcome": "ALLOW",
                "passed": True,
                "basis": "allowed",
                "certification_tier": 1,
                "finco_invariants": ["governance_legibility"],
                "authority_basis_present": True,
                "receipt_basis_present": True,
            },
            {
                "case_id": "SFC-D",
                "transition_type": "treasury_preparation",
                "expected_outcome": "DENY",
                "observed_outcome": "DENY",
                "passed": True,
                "basis": "denied",
                "certification_tier": 3,
                "finco_invariants": ["capital_entropy"],
                "authority_basis_present": True,
                "receipt_basis_present": True,
            },
            {
                "case_id": "SFC-F",
                "transition_type": "stegpay_event",
                "expected_outcome": "FAIL_CLOSED",
                "observed_outcome": "FAIL_CLOSED",
                "passed": True,
                "basis": "failed closed",
                "certification_tier": 2,
                "finco_invariants": ["no_undefined_states"],
                "authority_basis_present": True,
                "receipt_basis_present": True,
            },
        ],
    }

    ok, errors = validator.validate_report(report)

    assert ok is True
    assert errors == []


def test_validate_report_rejects_missing_fail_closed_coverage():
    validator = load_validator()
    report = {
        "suite": "stegfinco_certification",
        "case_count": 1,
        "pass_count": 1,
        "fail_count": 0,
        "outcome_match_ratio": 1.0,
        "allow_case_count": 1,
        "deny_case_count": 0,
        "fail_closed_case_count": 0,
        "ok": True,
        "cases": [
            {
                "case_id": "SFC-A",
                "transition_type": "compensation",
                "expected_outcome": "ALLOW",
                "observed_outcome": "ALLOW",
                "passed": True,
                "basis": "allowed",
                "certification_tier": 1,
                "finco_invariants": ["governance_legibility"],
                "authority_basis_present": True,
                "receipt_basis_present": True,
            }
        ],
    }

    ok, errors = validator.validate_report(report)

    assert ok is False
    assert any("missing observed outcome coverage" in error for error in errors)
