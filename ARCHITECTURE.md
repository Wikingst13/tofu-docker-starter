```mermaid
flowchart TB
  %% ===== Local Dev (Docker Compose) =====
  subgraph Local["Local Dev — Docker Compose"]
    Prom[Prometheus] -->|scrapes /metrics| Web[FastAPI Web App]
    Prom -->|scrapes /metrics| NodeExp[Node Exporter]
    Graf[Grafana] <-->|queries| Prom
    Web -->|queries| DB[(Postgres)]
    Web -->|cache ops| Redis[(Redis)]
  end

  %% ===== IaC (OpenTofu, AWS design plan-only) =====
  subgraph IaC["OpenTofu — AWS design (plan-only, no apply)"]
    VPC[VPC]
    Sub1[Public Subnet A]
    Sub2[Public Subnet B]
    IGW[Internet Gateway]
    SG[Security Group]
    EC2[EC2 Instance]

    VPC --> Sub1
    VPC --> Sub2
    Sub1 -->|route| IGW
    Sub2 -->|route| IGW
    SG -->|allows inbound| EC2
    EC2 -->|in| Sub1
  end