---
title: Architectural Milestones
status: active
version: 2.0.0
owner: Guivos
last_updated: 2026-07-02
---

# Architectural Milestones

Registro oficial dos principais marcos de maturidade arquitetural da Guivos.

## Visão geral

| Marco | Estado | Finalidade |
|---|---|---|
| A0 — GKR Foundation | Completed | Estabelecer o repositório e a infraestrutura documental |
| A1 — Institutional Architecture Complete | Completed | Consolidar macroestrutura, permanência e governança |
| M3 — Foundation Architecture Frozen | Completed | Congelar a primeira arquitetura integralmente revisada |
| A2 — Functional Architecture Discovery | Active | Descobrir e validar as Core Capabilities permanentes |
| A3 — Operational Architecture | Planned | Descrever cooperação e fluxos entre capacidades |
| A4 — Platform Engineering | Planned | Materializar arquiteturas de referência |
| A5 — Canon 1.0 | Planned | Consolidar a primeira Canon integrada |

## A0 — GKR Foundation

**Estado:** Completed.

Resultados:

- repositório oficial criado;
- Markdown, Git e publicação configurados;
- Foundation, GEB, Product, Business e Research iniciados;
- mecanismos de baseline e rastreabilidade estabelecidos.

## A1 — Institutional Architecture Complete

**Estado:** Completed.

Resultados:

- macroestrutura da GEA consolidada;
- `GEA-PLM-001 — Permanence Layer Model` validado;
- separação entre Permanent Architecture, Reference Architecture, Enterprise Programs e Enterprise Delivery;
- regras de estabilidade e mudança institucional formalizadas.

## M3 — Foundation Architecture Frozen

**Estado:** Completed em 02/07/2026.

### Critério de conclusão

A Foundation foi analisada integralmente, consolidada, avaliada, validada, auditada e congelada como referência permanente da GEA.

### Evidências

- 6 documentos revisados;
- 173 afirmações institucionais atômicas;
- 43 grupos de significado;
- 50 invariantes provisórios consolidados em 18;
- 54 responsabilidades provisórias consolidadas em 16;
- `A2-R01-RA-001` com resultado `READY`;
- `AV-A2-001` com decisão `APPROVED WITH RECOMMENDATIONS`;
- `A2-R01-AUD-001` com resultado `PASS`;
- `A2-B3` congelada.

### Efeito

- Foundation torna-se referência normativa para arquiteturas dependentes;
- mudanças futuras exigem revisão formal;
- `A2-R02 — Fundamental Model Review` fica autorizada.

## A2 — Functional Architecture Discovery

**Estado:** Active.

### Objetivo

Descobrir o conjunto mínimo e suficiente de capacidades institucionais permanentes da Guivos.

### Entregável principal

`GCCM-001 — Guivos Core Capability Model`.

### Revisões

| Revisão | Estado |
|---|---|
| A2-R01 — Foundation Architecture Review | Completed — Frozen in A2-B3 |
| A2-R02 — Fundamental Model Review | Authorized — Next |
| A2-R03 — Business Architecture Review | Planned |
| A2-R04 — Product Architecture Review | Planned |
| A2-R05 — Cross-Architecture Review | Planned |

### Restrições

- nenhuma Core Capability por brainstorming isolado;
- produtos, funcionalidades, serviços e tecnologias não são Core Capabilities;
- toda candidata exige convergência multiarquitetura;
- o catálogo deve representar o menor conjunto suficiente;
- rastreabilidade é obrigatória.

## A3 — Operational Architecture

**Estado:** Planned.

Entregáveis previstos:

- `PRA-001 — Platform Reference Architecture`;
- arquiteturas de referência por domínio;
- modelo de cooperação entre Core Capabilities;
- fluxos conceituais, responsabilidades e fronteiras.

## A4 — Platform Engineering

**Estado:** Planned.

Transformar arquiteturas de referência em Enterprise Programs e Enterprise Delivery, preservando a separação entre visão e implementação.

## A5 — Canon 1.0

**Estado:** Planned.

Primeira consolidação integrada da Foundation, GEA, GCCM, PRA e arquiteturas de referência essenciais.

## Regra de transição

Um marco somente muda de estado quando seus critérios de conclusão estiverem demonstrados no GKR. Nenhuma hipótese, draft ou ativo experimental é promovido automaticamente à Canon.