# cloud-gitops-platform

Plataforma cloud de referência construída como projecto pessoal para consolidar
competências em DevSecOps, Infrastructure as Code e engenharia de plataformas.

O projecto simula o ambiente operacional de um Platform Team real: uma aplicação
distribuída, completamente automatizada desde o commit até ao deploy em produção,
com observabilidade, segurança integrada e infraestrutura definida como código.

## Stack tecnológica

| Camada | Tecnologias |
|---|---|
| Aplicação | Python · FastAPI · Docker |
| Infraestrutura | Terraform · Ansible · K3s / EKS / AKS |
| Orquestração | Kubernetes · Helm |
| GitOps & CI/CD | FluxCD · GitHub Actions |
| Segurança | Trivy · Semgrep · OWASP ZAP · Kyverno · Sealed Secrets · cert-manager |
| Observabilidade | Prometheus · Grafana · Loki · OpenTelemetry |

## Estrutura do repositório
cloud-gitops-platform/
├── infra/terraform/       # Provisionamento de infraestrutura cloud
├── infra/ansible/         # Configuração de SO e ferramentas nos nós
├── app/                   # API FastAPI + Dockerfile multi-stage
├── k8s/                   # Manifests Kubernetes
├── gitops/                # Configuração FluxCD/ArgoCD
├── .github/workflows/     # Pipelines CI/CD
├── scripts/               # Utilitários de deploy e operação
├── docs/adr/              # Architecture Decision Records
└── RUNBOOK.md             # Guia de setup e demo
## Como começar

Consulta o [RUNBOOK.md](./RUNBOOK.md) para instruções completas.
