# Tofu + Docker Compose Starter

---

## ⚡️ Quick Start

### 1) Local app stack
Requirements: Docker + Docker Compose

Start:
```bash
cd app
cp .env.example .env
mkdir -p secrets && echo "changeme" > secrets/app_secret.txt
docker compose up -d
```

Services:
- Web app: [http://localhost:8000](http://localhost:8000)  
  - health: `/health`  
  - metrics: `/metrics`
- Grafana: [http://localhost:3000](http://localhost:3000) (u/p: `admin` / `admin`)  
  - Datasource: `http://prometheus:9090`  
  - Dashboard: ID `1860 (Node Exporter Full)`
- Prometheus: [http://localhost:9090](http://localhost:9090)  
- Postgres: port 5432, credentials from `.env`  
- Redis: port 6379  

Stop and clean:
```bash
docker compose down        # stop
docker compose down -v     # stop + remove volumes
```

---

### 2) OpenTofu (IaC)
Requirements: OpenTofu >=1.6

Example for `dev`:
```bash
cd infra/envs/dev
tofu init
tofu fmt -check
tofu validate
AWS_ACCESS_KEY_ID=test AWS_SECRET_ACCESS_KEY=test tofu plan -lock=false -refresh=false -input=false -var-file=dev.tfvars
```

For `staging`:
```bash
cd infra/envs/staging
tofu init
tofu validate
AWS_ACCESS_KEY_ID=test AWS_SECRET_ACCESS_KEY=test tofu plan -var-file=staging.tfvars
```

For `prod`:
```bash
cd infra/envs/prod
tofu init
tofu validate
AWS_ACCESS_KEY_ID=test AWS_SECRET_ACCESS_KEY=test tofu plan -var-file=prod.tfvars
```

Plans are generated as JSON:
```
infra/envs/dev/plan_dev.json
infra/envs/staging/plan_staging.json
infra/envs/prod/plan_prod.json
```

---

### 3) Local CI checks
Build and test the web image:
```bash
cd app
docker build -t local/web:dev ./web
docker run --rm -p 8000:8000 local/web:dev
```

Lint Dockerfile:
```bash
hadolint app/web/Dockerfile
```

Security scan (IaC):
```bash
trivy config infra
```

Security scan (image):
```bash
trivy image local/web:dev
```

---

##  Repository layout

```
.
├── app/                        
│   ├── compose.yaml
│   ├── .env.example
│   ├── web/ (Dockerfile + source code)
│   ├── prometheus/prometheus.yml
│   └── grafana/provisioning/
├── infra/                      
│   ├── modules/ (vpc, security_group, ec2)
│   └── envs/
│       ├── dev/ (main.tf, dev.tfvars)
│       ├── staging/ (staging.tfvars)
│       └── prod/ (prod.tfvars)
├── infra/test/  (Terratest)
├── .github/workflows/ci.yml
└── README.md
```

---




