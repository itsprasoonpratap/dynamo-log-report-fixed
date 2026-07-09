import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def load_report():
    with REPORT_PATH.open() as f:
        return json.load(f)


def test_report_is_valid_json_object():
    """Criterion 1: Create /app/report.json containing a valid JSON object."""
    assert REPORT_PATH.exists(), "/app/report.json was not created"
    assert isinstance(load_report(), dict), "/app/report.json must contain a JSON object"


def test_total_requests():
    """Criterion 2: Include a total_requests field with the value 6."""
    report = load_report()
    assert report.get("total_requests") == 6


def test_unique_ips():
    """Criterion 3: Include a unique_ips field with the value 3."""
    report = load_report()
    assert report.get("unique_ips") == 3


def test_top_path():
    """Criterion 4: Include a top_path field with the value \"/index.html\"."""
    report = load_report()
    assert report.get("top_path") == "/index.html"
