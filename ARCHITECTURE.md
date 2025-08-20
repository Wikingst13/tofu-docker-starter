# Architecture Diagram

```mermaid
flowchart LR
  subgraph Local[Local Dev - Docker Compose]
    Web[FastAPI Web App] -->|reads/writes| DB[(Postgres)]
    Web --> Redis[(Redis)]
    Prom[Prometheus] -->|scrapes| Web
    Prom -->|scrapes| NodeExp[Node Exporter]
    Prom -->|scrapes| cAdvisor[cAdvisor]
    Graf[Grafana] --> Prom
  end

  subgraph IaC[OpenTofu - AWS design (no apply)]
    VPC[VPC]
    Sub1[Public Subnet A] --> IGW[Internet Gateway]
    Sub2[Public Subnet B] --> IGW
    EC2[EC2 Instance] -->|in| Sub1
    SG[Security Group] --> EC2
  end
```
