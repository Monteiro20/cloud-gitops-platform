# cloud-gitops-platform

A complete cloud platform built as a personal project to consolidate
skills in DevSecOps, Infrastructure as Code, and platform engineering.

This project simulates the operational environment of a real Platform Team:
a distributed application, fully automated from commit to production deploy,
with observability, integrated security, and infrastructure defined as code.

## Tech Stack

| Layer | Technologies |
|---|---|
| Application | Python · FastAPI · Docker |
| Infrastructure | Terraform · Ansible · K3s / EKS / AKS |
| Orchestration | Kubernetes · Helm |
| GitOps & CI/CD | FluxCD · GitHub Actions |
| Security | Trivy · Semgrep · OWASP ZAP · Kyverno · Sealed Secrets · cert-manager |
| Observability | Prometheus · Grafana · Loki · OpenTelemetry |

## Repository Structure
cloud-gitops-platform/
├── infra/terraform/       # Cloud infrastructure provisioning
├── infra/ansible/         # OS and tooling configuration on nodes
├── app/                   # FastAPI application + multi-stage Dockerfile
├── k8s/                   # Kubernetes manifests
├── gitops/                # FluxCD/ArgoCD configuration
├── .github/workflows/     # CI/CD pipelines
├── scripts/               # Deploy and operations utilities
├── docs/adr/              # Architecture Decision Records
└── RUNBOOK.md             # Setup and demo guide
## Getting Started

See [RUNBOOK.md](./RUNBOOK.md) for full setup instructions.
