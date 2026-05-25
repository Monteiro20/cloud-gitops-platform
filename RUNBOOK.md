# RUNBOOK

Operational guide for the project — setup, demo, and troubleshooting.

---

## Prerequisites

| Tool | Version | Install |
|---|---|---|
| Ubuntu (WSL2) | 22.04 LTS | `wsl --install` in PowerShell |
| Docker | 29.4+ | [docs.docker.com](https://docs.docker.com/engine/install/ubuntu/) |
| kubectl | 1.36+ | Official docs |
| Terraform | 1.15+ | HashiCorp repo |
| Ansible | 2.10+ | `apt install ansible` |
| Git | 2.34+ | `apt install git` |

---

## Environment Setup (once)

### 1. Clone the repository

```bash
git clone https://github.com/Monteiro20/cloud-gitops-platform.git
cd cloud-gitops-platform
```

### 2. Start Docker

```bash
sudo service docker start
docker run hello-world
```

### 3. Verify tools

```bash
make status
```

---

## Git Workflow

```bash
# Always work on the dev branch
git checkout dev

# After changes
git add .
git commit -m "type: short description"
git push origin dev

# When a feature is ready — open a Pull Request dev → main on GitHub
```

### Commit Convention

| Prefix | When to use |
|---|---|
| `feat:` | new feature |
| `fix:` | bug fix |
| `docs:` | documentation |
| `chore:` | configuration, dependencies |
| `ci:` | pipeline changes |
| `infra:` | infrastructure (Terraform/Ansible) |

---

## Project Status

| Phase | Description | Status |
|---|---|---|
| Phase 1 | Repository structure | ✅ Done |
| Phase 2 | Terraform + Ansible | ✅ Done |
| Phase 3 | Application + Docker | ✅ Done |
| Phase 4 | Kubernetes manifests | ✅ Done |
| Phase 5 | GitOps | 🔲 Pending |
| Phase 6 | CI/CD | 🔲 Pending |
| Phase 7 | DevSecOps | 🔲 Pending |
| Phase 8 | Observability | 🔲 Pending |
| Phase 9 | Scripts | 🔲 Pending |
| Phase 10 | Final documentation | 🔲 Pending |

---

## Architecture Decisions

See [`docs/adr/`](./docs/adr/) for technical decisions and their reasoning.
