---
title: Architectural Milestones
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-06-30
---

# Architectural Milestones

Registro oficial dos principais marcos de maturidade arquitetural da Guivos.

## Visão geral

| Marco | Estado | Finalidade |
|---|---|---|
| A0 — GKR Foundation | Completed | Estabelecer o repositório, a documentação oficial e a infraestrutura de publicação |
| A1 — Institutional Architecture Complete | Completed | Consolidar identidade, macroestrutura, permanência, princípios e governança arquitetural |
| A2 — Functional Architecture Discovery | Active | Descobrir e validar as Core Capabilities permanentes da Guivos |
| A3 — Operational Architecture | Planned | Descrever como as Core Capabilities cooperam na Plataforma Guivos |
| A4 — Platform Engineering | Planned | Materializar progressivamente as arquiteturas de referência |
| A5 — Canon 1.0 | Planned | Consolidar a primeira versão canônica integrada da arquitetura funcional e operacional |

## A0 — GKR Foundation

**Estado:** Completed.

Resultados principais:

- repositório oficial criado;
- Markdown e Git definidos como base documental e histórica;
- MkDocs, Mermaid, GitHub Pages e publicação derivada configurados;
- Foundation, GEB, Product Architecture, Business Architecture e Research iniciados;
- baseline e mecanismos de rastreabilidade estabelecidos.

## A1 — Institutional Architecture Complete

**Estado:** Completed.

### Critério de conclusão

A Guivos possui uma arquitetura institucional suficientemente estável para orientar a descoberta funcional e a realização progressiva sem exigir expansão estrutural contínua.

### Escopo consolidado

- Foundation Architecture;
- Guivos Enterprise Architecture;
- estrutura principal do GEB;
- estrutura superior da Product Architecture;
- fundamentos da Business Architecture;
- Research Domain e protocolo de pesquisa;
- governança documental e arquitetural existente;
- Permanence Layer Model;
- princípios de maturidade institucional e realização progressiva;
- separação entre Permanent Architecture, Reference Architecture, Enterprise Programs e Enterprise Delivery.

### Regra de estabilidade

A conclusão de A1 não significa imutabilidade. Mudanças estruturais futuras exigem problema arquitetural comprovado, análise de impacto, evidência suficiente e o mecanismo de governança adequado.

## A2 — Functional Architecture Discovery

**Estado:** Active.

### Objetivo

Descobrir o conjunto mínimo e suficiente de capacidades institucionais permanentes que explica aquilo que a Guivos deve ser capaz de realizar em sua maturidade.

### Entregável principal

`GCCM-001 — Guivos Core Capability Model`.

### Método

1. extrair evidências dos ativos existentes do GKR;
2. identificar responsabilidades, verbos institucionais, objetivos e relações;
3. agrupar evidências semanticamente equivalentes;
4. formular capacidades candidatas;
5. aplicar critérios de admissão;
6. aplicar testes de irredutibilidade, independência tecnológica e cobertura da missão;
7. consolidar o catálogo somente após validação.

### Restrições

- não criar Core Capabilities por brainstorming isolado;
- não confundir produtos, funcionalidades, serviços ou tecnologias com Core Capabilities;
- buscar o menor conjunto suficiente;
- manter rastreabilidade entre evidência, candidata, decisão e catálogo.

## A3 — Operational Architecture

**Estado:** Planned.

Entregáveis previstos:

- `PRA-001 — Platform Reference Architecture`;
- arquiteturas de referência por domínio;
- modelo de cooperação entre Core Capabilities;
- fluxos conceituais, responsabilidades e fronteiras operacionais.

## A4 — Platform Engineering

**Estado:** Planned.

Objetivo:

Transformar arquiteturas de referência em Enterprise Programs e Enterprise Delivery, preservando a separação entre visão institucional e escolhas de implementação.

## A5 — Canon 1.0

**Estado:** Planned.

Critério preliminar:

Primeira consolidação integrada da Foundation, GEA, GCCM, PRA e arquiteturas de referência essenciais, com rastreabilidade suficiente para orientar programas de implementação.

## Regra de transição

Um marco somente muda de estado quando seus critérios de conclusão estiverem demonstrados no GKR. A mudança de marco não promove automaticamente hipóteses, drafts ou ativos experimentais à Canon.
