# Solidity Sentry – Risk Scoring

Solidity Sentry is a lightweight Python tool that calculates a single risk score
for a Solidity contract. The score is a number between **0** (perfect) and **100**
(critical). It is derived from the weighted severity of detected issues and
gas‑optimization impact.

## Features

- **Weighted severity**: Issues are scored using a simple severity weight
  table (`low=1`, `medium=3`, `high=5`, `critical=10`).
- **Gas impact**: A numeric value (0–100) representing gas‑optimization
  impact is added to the weighted severity.
- **Clamped score**: The final score is clamped to the 0–100 range.
- **CLI**: Run from the command line to score a contract based on a JSON
  file of issues.

## Usage
