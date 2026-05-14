# ADR 001 — Estratégia de Kubernetes Local

## Data
2025-05-13

## Contexto
O projecto requer um cluster Kubernetes para desenvolvimento e testes.
As opções consideradas foram: K3s, Minikube, Kind, e EKS/AKS directamente.

## Decisão
Usar **K3s localmente** no WSL2 para todo o desenvolvimento.
EKS/AKS apenas para validação final em cloud real.

## Razões
- K3s é uma distribuição Kubernetes certificada e leve (~70MB)
- Corre bem em WSL2 com os recursos disponíveis (7.7GB RAM)
- Elimina custos cloud durante o desenvolvimento (~$73/mês de EKS)
- Comportamento idêntico ao EKS/AKS para os fins deste projecto

## Consequências
- Não é possível testar features específicas de cloud (EKS managed node groups)
- A validação cloud tem de ser feita numa janela de tempo controlada para limitar custos
