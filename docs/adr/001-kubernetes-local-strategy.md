# ADR 001 — Local Kubernetes Strategy

## Date
2025-05-14

## Context
The project requires a Kubernetes cluster for development and testing.
Options considered: K3s, Minikube, Kind, and EKS/AKS directly.

## Decision
Use **K3s locally** on WSL2 for all development.
EKS/AKS only for final cloud validation.

## Reasons
- K3s is a certified, lightweight Kubernetes distribution (~70MB)
- Runs well on WSL2 with available resources (7.7GB RAM)
- Eliminates cloud costs during development (~$73/month for EKS)
- Identical behaviour to EKS/AKS for the purposes of this project

## Consequences
- Cloud-specific features (EKS managed node groups) cannot be tested locally
- Cloud validation must be done in a controlled time window to limit costs
