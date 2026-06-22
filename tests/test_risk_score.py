import json
import os
import sys
import tempfile

import pytest

from risk_score import compute_risk_score, main


def test_compute_risk_score_happy_path():
    issues = [{"severity": "low"}, {"severity": "high"}]
    gas = 20
    score = compute_risk_score(issues, gas)
    # low=1, high=5 => weighted=6, raw=26
    assert score == 26


def test_compute_risk_score_clamp_over():
    # 10 critical issues => 100 weighted severity
    issues = [{"severity": "critical"}] * 10
    gas = 50
    score = compute_risk_score(issues, gas)
    assert score == 100  # clamped to 100


def test_compute_risk_score_clamp_under():
    issues = []
    gas = -10
    score = compute_risk_score(issues, gas)
    assert score == 0  # clamped to 0


def test_compute_risk_score_invalid_severity():
    issues = [{"severity": "unknown"}]
    gas = 0
    with pytest.raises(ValueError, match="Unknown severity"):
        compute_risk_score(issues, gas)


def test_compute_risk_score_invalid_gas_type():
    issues = [{"severity": "low"}]
    gas = "high"
    with pytest.raises(TypeError, match="gas_impact must be a numeric type"):
        compute_risk_score(issues, gas)


def test_cli_output(monkeypatch, capsys):
    # Create a temporary JSON file with a single medium issue
    with tempfile.NamedTemporaryFile("w+", delete=False) as tmp:
        json.dump([{"severity": "medium"}], tmp)
        tmp_path = tmp.name

    # Monkeypatch sys.argv to simulate CLI invocation
    monkeypatch.setattr(sys, "argv", ["risk_score", tmp_path, "--gas", "15"])
    # Run the CLI
    main()
    captured = capsys.readouterr()
    # Clean up temp file
    os.unlink(tmp_path)

    assert "Risk Score:" in captured.out
    # medium=3 + gas 15 = 18
    assert "18" in captured.out
