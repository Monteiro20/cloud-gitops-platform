# RUNBOOK

Guia operacional do projecto — setup, demo e troubleshooting.

---

## Pré-requisitos

| Ferramenta | Versão | Como instalar |
|---|---|---|
| Ubuntu (WSL2) | 22.04 LTS | `wsl --install` no PowerShell |
| Docker | 29.4+ | [docs.docker.com](https://docs.docker.com/engine/install/ubuntu/) |
| kubectl | 1.36+ | `curl -LO ...` (ver docs oficiais) |
| Terraform | 1.15+ | `apt install terraform` (repo HashiCorp) |
| Ansible | 2.10+ | `apt install ansible` |
| Git | 2.34+ | `apt install git` |

---

## Setup do ambiente (feito uma vez)

### 1. Clonar o repositório

```bash
git clone https://github.com/Monteiro20/cloud-gitops-platform.git
cd cloud-gitops-platform
```

### 2. Iniciar o Docker

```bash
sudo service docker start
docker run hello-world   # confirmar que funciona
```

### 3. Confirmar ferramentas

```bash
docker --version
python3 --version
kubectl version --client
terraform --version
ansible --version
```

---

## Fluxo de trabalho Git

```bash
# Trabalhar sempre na branch dev
git checkout dev

# Após alterações
git add .
git commit -m "tipo: descrição curta"
git push origin dev

# Quando a feature está pronta — abrir Pull Request dev → main no GitHub
```

### Convenção de commits

| Prefixo | Quando usar |
|---|---|
| `feat:` | nova funcionalidade |
| `fix:` | correcção de bug |
| `docs:` | documentação |
| `chore:` | configuração, dependências |
| `ci:` | alterações ao pipeline |
| `infra:` | infraestrutura (Terraform/Ansible) |

---

## Estado actual do projecto

| Fase | Descrição | Estado |
|---|---|---|
| Fase 1 | Estrutura do repositório | ✅ Concluída |
| Fase 2 | Terraform + Ansible | 🔲 Por fazer |
| Fase 3 | Aplicação + Docker | 🔲 Por fazer |
| Fase 4 | Kubernetes manifests | 🔲 Por fazer |
| Fase 5 | GitOps | 🔲 Por fazer |
| Fase 6 | CI/CD | 🔲 Por fazer |
| Fase 7 | DevSecOps | 🔲 Por fazer |
| Fase 8 | Observabilidade | 🔲 Por fazer |
| Fase 9 | Scripts | 🔲 Por fazer |
| Fase 10 | Documentação final | 🔲 Por fazer |

---

## Decisões de arquitectura

Consulta a pasta [`docs/adr/`](./docs/adr/) para as decisões técnicas e o raciocínio por trás delas.
