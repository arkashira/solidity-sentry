# dataflow.md

## System Dataflow Architecture – Solidity‑Sentry

```
+---------------------+          +---------------------+          +---------------------+
|  External Data      |          |  Ingestion Layer    |          |  Processing/        |
|  Sources (GitHub,   |  --->    |  (GitHub Webhooks,  |  --->    |  Transform Layer    |
|  GitHub API, CI     |          |  GitHub Actions,    |          |  (Static Analysis,  |
|  Code Review APIs)  |          |  GitHub REST API)   |          |   Optimization,     |
|  (public repos)     |          |  (Auth: OAuth2)     |          |   Issue Extraction) |
+---------------------+          +---------------------+          +---------------------+
          |                               |                               |
          |                               |                               |
          v                               v                               v
+---------------------+          +---------------------+          +---------------------+
|  Storage Tier       |          |  Query/Serving Layer|          |  Egress to User     |
|  (PostgreSQL, S3)   |          |  (GraphQL, REST API)|          |  (Web UI, CLI, CLI  |
|  (Auth: IAM, S3    |          |  (Auth: JWT, OAuth) |          |   Plugins)          |
|  Encryption)        |          |  (Rate‑limit, CORS) |          |  (Auth: JWT, OAuth) |
+---------------------+          +---------------------+          +---------------------+
```

### 1. External Data Sources
| Source | Data Type | Frequency | Auth |
|--------|-----------|-----------|------|
| **GitHub Repositories** | Solidity source files, commit history | On‑push via Webhooks | OAuth2 (repo scope) |
| **GitHub Actions** | CI job logs, artifact metadata | Triggered by workflow | OAuth2 |
| **GitHub REST API** | Repository metadata, branch refs | Polling (5 min) | OAuth2 |
| **Code Review APIs** (e.g., GitHub PR reviews) | Review comments, issue references | On‑event | OAuth2 |
| **External Linter/Formatter APIs** (optional) | Pre‑analysis results | On‑request | API key |

### 2. Ingestion Layer
- **GitHub Webhook Listener**  
  - Receives `push`, `pull_request`, `check_run` events.  
  - Validates payload signature, queues job in **RabbitMQ**.  
- **GitHub Actions Runner**  
  - Executes `solidity‑sentry` CLI on the repository.  
  - Pushes analysis artifacts to **S3** (bucket: `solidity-sentry-artifacts`).  
- **GitHub REST Poller**  
  - Periodically fetches new commits for repos not covered by webhooks.  
  - Enqueues jobs in **RabbitMQ**.  
- **Auth Boundary**: All ingestion endpoints require a signed JWT issued by the Auth Service (Auth0/Keycloak). OAuth2 tokens are refreshed per repo.

### 3. Processing / Transform Layer
- **Worker Service (Node.js / Rust)**  
  - Consumes job queue, pulls repo snapshot from GitHub.  
  - Runs **solidity‑sentry** static analyzer.  
  - Transforms raw JSON output into normalized **Issue** objects.  
  - Applies optimization hints (gas usage, best‑practice patterns).  
  - Stores results in **PostgreSQL** (`issues`, `repos`, `analysis_runs`).  
  - Uploads raw logs to **S3** (bucket: `solidity-sentry-logs`).  
- **Data Enrichment Service**  
  - Cross‑references issues with public vulnerability databases (e.g., SWC registry).  
  - Adds severity scores, CVE references.  
- **Auth Boundary**: Workers authenticate to PostgreSQL via IAM roles; S3 access via signed URLs.

### 4. Storage Tier
| Layer | Technology | Purpose | Security |
|-------|------------|---------|----------|
| **Relational DB** | PostgreSQL (RDS) | Persist analysis metadata, issue catalog, user repos | IAM roles, encryption at rest |
| **Object Store** | Amazon S3 | Store raw analysis logs, artifacts, CI logs | Bucket policies, SSE‑S3 |
| **Cache** | Redis | Fast lookup of recent analysis results | VPC‑only access |
| **Search** | OpenSearch | Full‑text search over issue descriptions | IAM policies, encryption |

### 5. Query / Serving Layer
- **GraphQL API** (`api.solidity-sentry.com/graphql`)  
  - Endpoints: `repoIssues`, `analysisRun`, `suggestions`.  
  - Pagination, filtering by severity, file path.  
  - Rate‑limit (100 req/min per user).  
- **REST API** (`api.solidity-sentry.com/v1/`)  
  - Legacy endpoints for CI integration.  
- **Auth Boundary**: JWT bearer tokens issued by Auth Service; scopes: `read:repo`, `write:repo`.  
- **Rate‑limit & CORS**: Managed by API Gateway (AWS API Gateway / CloudFront).

### 6. Egress to User
| Channel | Interface | Auth | Features |
|---------|-----------|------|----------|
| **Web UI** | React SPA (`app.solidity-sentry.com`) | JWT (SSO) | Interactive dashboards, issue drill‑down, inline suggestions |
| **CLI Plugin** | `solidity-sentry-cli` | OAuth2 token | Local analysis, auto‑fix suggestions |
| **GitHub App** | Pull‑request comments | App JWT | Auto‑comment on PRs with findings |
| **Webhook** | `POST /webhook/analysis` | HMAC signature | Push results to external systems (e.g., Slack, Jira) |

- **Auth Boundary**: All egress endpoints enforce JWT validation; CLI uses OAuth2 device flow; GitHub App uses signed JWT per installation.

---

**Key Security & Compliance Notes**

- All data in transit is TLS‑encrypted.  
- IAM roles are least‑privilege; S3 buckets have bucket policies restricting cross‑account access.  
- GDPR: Users can request deletion; data retention policy set to 90 days for raw logs.  
- Logging: CloudWatch logs for all services, with audit trail for compliance.  

---