flowchart LR
  %% ----- Local Dev (Docker Compose) -----
  subgraph Local["Local Dev — Docker Compose"]
    Web[FastAPI Web App] -->|reads/writes| DB[(Postgres)]
    Web --> Redis[(Redis)]
    Prom[Prometheus] -->|scrapes| Web
    Prom -->|scrapes| NodeExp[Node Exporter]
    Graf[Grafana] --> Prom
  end

  %% ----- IaC (OpenTofu, plan‑only) -----
  subgraph IaC["OpenTofu — AWS design (plan‑only, no apply)"]
    direction TB
    VPC[VPC]
    Sub1[Public Subnet A]
    Sub2[Public Subnet B]
    IGW[Internet Gateway]
    SG[Security Group]
    EC2[EC2 Instance]

    VPC --- Sub1
    VPC --- Sub2
    Sub1 --> IGW
    Sub2 --> IGW
    SG --> EC2
    EC2 --> Sub1
  end