import importlib.util
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RUNNER_PATH = REPO_ROOT / "tools" / "stegfinco_support_event_cert_runner.py"


def load_runner():
    spec = importlib.util.spec_from_file_location("stegfinco_support_event_cert_runner", RUNNER_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_support_event_certification_all_cases_pass():
    runner = load_runner()
    report = runner.run_suite(REPO_ROOT / "sim" / "stegfinco" / "support_events")

    assert report["ok"] is True
    assert report["case_count"] == 6
    assert report["pass_count"] == 6
    assert report["fail_count"] == 0


def test_support_event_certification_covers_required_outcomes():
    runner = load_runner()
    report = runner.run_suite(REPO_ROOT / "sim" / "stegfinco" / "support_events")
    observed = {case["observed_outcome"] for case in report["cases"]}

    assert {"ALLOW", "DENY", "FAIL_CLOSED"}.issubset(observed)


def test_support_event_certification_never_allows_entitlement():
    runner = load_runner()
    report = runner.run_suite(REPO_ROOT / "sim" / "stegfinco" / "support_events")

    for case in report["cases"]:
        if case["creates_entitlement"] is True:
            assert case["observed_outcome"] != "ALLOW"
