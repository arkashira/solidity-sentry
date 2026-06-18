# STORIES.md – Solidity‑Sentry

## Overview
Solidity‑Sentry is a static analysis and optimization engine for Solidity smart contracts.  
It identifies common pitfalls (reentrancy, overflow, gas‑inefficiency, etc.), suggests fixes, and integrates with CI/CD pipelines to enforce quality before deployment.

The following backlog is grouped into **epics** that reflect the MVP delivery order.  
Each story follows the format:

```
As a <role>, I want <goal>, so that <benefit>
```

Acceptance criteria are written in a test‑driven style.

---

## Epics

| Epic | Description |
|------|-------------|
| **E1 – Core Analyzer** | Build the static analysis engine that parses Solidity, detects issues, and reports them. |
| **E2 – Fix Suggestions** | Provide actionable, automated fix suggestions for detected issues. |
| **E3 – CI/CD Integration** | Enable easy integration with GitHub Actions, GitLab CI, and local pre‑commit hooks. |
| **E4 – User Interface** | Offer a CLI and a web UI for developers to run analyses locally or view results in the browser. |
| **E5 – Documentation & Samples** | Deliver comprehensive docs, tutorials, and example contracts. |
| **E6 – Performance & Scalability** | Optimize analysis speed for large codebases and support incremental analysis. |

---

## User Story Backlog

### Epic E1 – Core Analyzer

| # | Story | Acceptance Criteria |
|---|-------|---------------------|
| **E1‑S1** | **As a developer, I want the tool to parse Solidity files, so that I can analyze my contracts.** | - CLI command `sentry analyze <path>` accepts a directory or file.<br>- Parser builds an AST without crashing on Solidity 0.8.x syntax.<br>- Errors for unsupported syntax are reported with line numbers. |
| **E1‑S2** | **As a developer, I want the analyzer to detect reentrancy vulnerabilities, so that I can fix them before deployment.** | - Reentrancy patterns (e.g., external calls before state changes) are flagged.<br>- Report includes file, line, and a brief explanation.<br>- False‑positive rate < 5% on the `auto` dataset. |
| **E1‑S3** | **As a developer, I want the analyzer to detect arithmetic overflows/underflows, so that I can add SafeMath or use Solidity 0.8.x checks.** | - Detects unchecked arithmetic in all arithmetic operations.<br>- Suggests `unchecked {}` or `SafeMath` usage.<br>- Report includes severity (low/medium/high). |
| **E1‑S4** | **As a developer, I want the analyzer to detect gas‑inefficient patterns, so that I can optimize contract cost.** | - Flags patterns like `for` loops with dynamic bounds, unnecessary storage writes.<br>- Provides estimated gas savings. |
| **E1‑S5** | **As a developer, I want the analyzer to support Solidity 0.8.x and 0.7.x, so that I can analyze legacy contracts.** | - Parser auto‑detects compiler version from `pragma`.<br>- Analysis rules adjust accordingly. |

### Epic E2 – Fix Suggestions

| # | Story | Acceptance Criteria |
|---|-------|---------------------|
| **E2‑S1** | **As a developer, I want the tool to suggest automated patches for reentrancy, so that I can apply fixes quickly.** | - Generates a diff file with the recommended change.<br>- Diff can be applied with `sentry apply <diff>`.<br>- Patch compiles without errors. |
| **E2‑S2** | **As a developer, I want the tool to suggest SafeMath wrappers for unchecked arithmetic, so that I can secure my contracts.** | - Inserts `using SafeMath for uint256;` where needed.<br>- Adds import statement if not present. |
| **E2‑S3** | **As a developer, I want the tool to suggest gas‑optimizations, so that I can reduce deployment and execution costs.** | - Recommends refactoring loops, using `uint256` instead of `uint` where appropriate.<br>- Provides before/after gas estimates. |

### Epic E3 – CI/CD Integration

| # | Story | Acceptance Criteria |
|---|-------|---------------------|
| **E3‑S1** | **As a DevOps engineer, I want a GitHub Action that runs Solidity‑Sentry on pull requests, so that code quality is enforced automatically.** | - Action YAML file `sentry.yml` is provided.<br>- Action fails the PR if any high‑severity issue is found.<br>- Summary comment is posted with issue list. |
| **E3‑S2** | **As a DevOps engineer, I want a pre‑commit hook that runs Solidity‑Sentry locally, so that developers catch issues early.** | - Hook script `pre-commit` runs on staged Solidity files.<br>- Hook aborts commit if any critical issue is detected. |
| **E3‑S3** | **As a CI engineer, I want the tool to output results in SARIF format, so that I can integrate with SonarQube or GitHub Code Scanning.** | - `sentry export --format sarif > results.sarif` produces valid SARIF.<br>- All findings are mapped to SARIF rules. |

### Epic E4 – User Interface

| # | Story | Acceptance Criteria |
|---|-------|---------------------|
| **E4‑S1** | **As a developer, I want a CLI that displays findings in a readable table, so that I can quickly scan issues.** | - `sentry analyze` prints a table with columns: File, Line, Severity, Rule, Description.<br>- Supports `--json` flag for machine parsing. |
| **E4‑S2** | **As a developer, I want a web UI that visualizes findings per file, so that I can navigate large projects.** | - Web app serves a dashboard at `http://localhost:3000`.<br>- File tree view with expandable nodes.<br>- Clicking a node shows issues in that file. |
| **E4‑S3** | **As a developer, I want the web UI to allow inline editing and auto‑apply patches, so that I can fix issues directly.** | - Inline editor highlights problematic code.<br>- “Apply Fix” button applies the suggested patch and re‑runs analysis. |

### Epic E5 – Documentation & Samples

| # | Story | Acceptance Criteria |
|---|-------|---------------------|
| **E5‑S1** | **As a new user, I want a quick‑start guide, so that I can install and run the tool in minutes.** | - README contains installation steps for Linux/macOS/Windows.<br>- Includes a sample contract and a command that produces a non‑empty report. |
| **E5‑S2** | **As a developer, I want a reference guide for all supported rules, so that I can understand each issue.** | - Markdown page lists all rules with description, severity, and example. |
| **E5‑S3** | **As a maintainer, I want example CI configurations for GitHub and GitLab, so that contributors can set up pipelines.** | - YAML snippets for both platforms included in docs. |

### Epic E6 – Performance & Scalability

| # | Story | Acceptance Criteria |
|---|-------|---------------------|
| **E6‑S1** | **As a team lead, I want the analyzer to finish a 10 kLOC project in under 30 seconds, so that it fits into CI pipelines.** | - Benchmark on the `auto` dataset shows <30 s for 10 kLOC.<br>- CPU usage ≤ 70% on a single core. |
| **E6‑S2** | **As a developer, I want incremental analysis support, so that only changed files are re‑analyzed.** | - `sentry analyze --incremental` reads a `.sentry_cache` file.<br>- Only files with modified timestamps are parsed. |
| **E6‑S3** | **As a user, I want parallel analysis across multiple cores, so that large projects run faster.** | - `sentry analyze --workers N` splits work across N processes.<br>- Results are merged correctly. |

---

## MVP Release Order

1. **E1‑S1** – Basic parsing & CLI.  
2. **E1‑S2, E1‑S3, E1‑S4** – Core rule set (reentrancy, overflow, gas).  
3. **E3‑S1** – GitHub Action integration.  
4. **E4‑S1** – CLI output table.  
5. **E2‑S1** – Automated patch generation for reentrancy.  
6. **E5‑S1** – Quick‑start guide.  
7. **E3‑S2** – Pre‑commit hook.  
8. **E1‑S5** – Solidity 0.7.x support.  
9. **E2‑S2, E2‑S3** – Additional fix suggestions.  
10. **E4‑S2** – Web UI dashboard.  
11. **E5‑S2** – Full rule reference.  
12. **E6‑S1, E6‑S2** – Performance tuning & incremental analysis.  
13. **E4‑S3** – Inline editor & auto‑apply.  
14. **E5‑S3** – CI config examples.  
15. **E6‑S3** – Parallel analysis.

---

## Definition of Done (DoD)

- Unit tests cover ≥90% of rule logic.  
- Integration tests validate CI hooks and SARIF output.  
- Documentation passes linting and includes examples.  
- Release candidate tagged in GitHub.  
- All stories marked **Done** in the project board.  

---
