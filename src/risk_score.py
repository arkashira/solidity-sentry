import argparse
import json
import sys
from typing import Dict, List

SEVERITY_WEIGHTS = {
    "low": 1,
    "medium": 3,
    "high": 5,
    "critical": 10,
}

def compute_risk_score(issues: List[Dict], gas_impact: float) -> int:
    """
    Compute a risk score between 0 and 100.

    Parameters
    ----------
    issues : List[Dict]
        Each dict must contain a 'severity' key with one of the
        recognised severity levels: low, medium, high, critical.
    gas_impact : float
        Numeric value representing gas‑optimization impact. 0–100 is
        expected but values outside this range are clamped.

    Returns
    -------
    int
        Final risk score rounded to the nearest integer, clamped to
        the inclusive range [0, 100].

    Raises
    ------
    ValueError
        If an issue contains an unknown severity level.
    TypeError
        If gas_impact is not a number.
    """
    if not isinstance(gas_impact, (int, float)):
        raise TypeError("gas_impact must be a numeric type")

    weighted_severity = 0
    for issue in issues:
        sev = issue.get("severity")
        if sev not in SEVERITY_WEIGHTS:
            raise ValueError(f"Unknown severity: {sev}")
        weighted_severity += SEVERITY_WEIGHTS[sev]

    raw_score = weighted_severity + gas_impact
    # Clamp to [0, 100]
    if raw_score < 0:
        raw_score = 0
    if raw_score > 100:
        raw_score = 100

    return int(round(raw_score))

def _load_issues(path: str) -> List[Dict]:
    """Load a JSON list of issue dictionaries from a file."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("Issues file must contain a JSON array")
    return data

def main() -> None:
    """CLI entry point for computing a risk score."""
    parser = argparse.ArgumentParser(
        description="Compute Solidity contract risk score."
    )
    parser.add_argument(
        "issues_file",
        help="Path to JSON file containing a list of issue objects",
    )
    parser.add_argument(
        "--gas",
        type=float,
        default=0.0,
        help="Gas optimization impact (0–100). Defaults to 0.",
    )
    args = parser.parse_args()

    issues = _load_issues(args.issues_file)
    score = compute_risk_score(issues, args.gas)
    print(f"Risk Score: {score}")

if __name__ == "__main__":
    main()
