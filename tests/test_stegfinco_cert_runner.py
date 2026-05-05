import importlib.util
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RUNNER_PATH = REPO_ROOT / "tools" / "stegfinco_cert_runner.py"


def load_runner():
    spec = importlib.util.spec_from_file_location("stegfinco_cert_runner", RUNNER_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_stegfinco_cert_runner_all_cases_pass():
    runner = load_runner()
    report = runner.run_suite(REPO_ROOT / "sim" / "stegfinco" / "transitions")

    assert report["ok"] is True
    assert report["case_count"] == 10
    assert report["pass_count"] == 10
    assert report["fail_count"] == 0
    assert report["allow_case_count"] >= 1
    assert report["deny_case_count"] >= 1
    assert report["fail_closed_case_count"] >= 1


def test_stegfinco_cert_runner_covers_required_outcomes():
    runner = load_runner()
    report = runner.run_suite(REPO_ROOT / "sim" / "stegfinco" / "transitions")
    observed = {case["observed_outcome"] for case in report["cases"]}

    assert {"ALLOW", "DENY", "FAIL_CLOSED"}.issubset(observed)
