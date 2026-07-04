---
title: Architectural Milestones
status: active
version: 3.0.0
owner: Guivos
last_updated: 2026-07-04
---

# Architectural Milestones

Registro oficial dos principais marcos de maturidade arquitetural da Guivos.

## Visão geral

| Marco | Estado | Finalidade |
|---|---|---|
| A0 — GKR Foundation | Completed | Estabelecer o repositório e a infraestrutura documental |
| A1 — Institutional Architecture Complete | Completed | Consolidar macroestrutura, permanência e governança |
| M3 — Foundation Architecture Frozen | Completed | Congelar a primeira arquitetura integralmente revisada |
| M3.1 — Fundamental Discovery Method Frozen | Completed | Congelar o método de execução da FMEM antes da extração |
| A2 — Functional Architecture Discovery | Active | Descobrir e validar estruturas funcionais e Core Capabilities |
| M4 — Fundamental Model Frozen | Planned | Congelar o Modelo Fundamental após revisão completa |
| A3 — Operational Architecture | Planned | Descrever cooperação e fluxos entre capacidades |
| A4 — Platform Engineering | Planned | Materializar arquiteturas de referência |
| A5 — Canon 1.0 | Planned | Consolidar a primeira Canon integrada |

## M3 — Foundation Architecture Frozen

**Estado:** Completed em 02/07/2026.

Resultados:

- seis documentos revisados;
- 173 afirmações institucionais atômicas;
- 43 grupos de significado;
- 18 invariantes consolidados;
- 16 responsabilidades consolidadas;
- readiness `READY`;
- validação aprovada com recomendações;
- auditoria `PASS`;
- baseline `A2-B3` congelada.

## M3.1 — Fundamental Discovery Method Frozen

**Estado:** Completed em 04/07/2026.

### Critério de conclusão

A metodologia da `A2-R02 — Fundamental Model Review` foi definida e congelada antes da extração do corpus.

### Resultados

- `Discovery Mode` formalizado;
- `Canon Mode` protegido;
- pipeline evidência → observação → regularidade → hipótese → revisão → consolidação formalizado;
- corpus principal definido;
- rastreabilidade obrigatória estabelecida;
- critérios de promoção futura registrados;
- `A2-R02-FMEM-001` criado em estado `execution-ready`;
- nenhuma evidência, hipótese ou alteração canônica registrada antecipadamente.

### Efeito

A revisão do Modelo Fundamental pode iniciar sua execução sobre o corpus oficial sem novas discussões metodológicas intermediárias.

## A2 — Functional Architecture Discovery

**Estado:** Active.

### Revisões

| Revisão | Estado |
|---|---|
| A2-R01 — Foundation Architecture Review | Completed — Frozen in A2-B3 |
| A2-R02 — Fundamental Model Review | Active — Execution Ready |
| A2-R03 — Business Architecture Review | Planned |
| A2-R04 — Product Architecture Review | Planned |
| A2-R05 — Cross-Architecture Review | Planned |

### Restrições

- nenhuma Core Capability nasce por brainstorming isolado;
- produtos, funcionalidades, serviços e tecnologias não são automaticamente Core Capabilities;
- toda candidata exige convergência e rastreabilidade;
- o catálogo deve representar o menor conjunto suficiente;
- hipóteses permanecem fora da Canon até validação.

## M4 — Fundamental Model Frozen

**Estado:** Planned.

Critérios previstos:

- corpus integralmente analisado;
- FMEM concluída;
- Canonical Consolidation concluída;
- readiness demonstrado;
- validação formal registrada;
- auditoria concluída;
- baseline `A2-B4` congelada.

## Guivos Economic Model

**Estado:** Domain Created — Development Planned.

O domínio foi criado em 04/07/2026. Seu desenvolvimento detalhado ocorrerá após dependências suficientes do Modelo Fundamental, GCCM, Business Architecture, Product Architecture e Business Outcomes.

## Regra de transição

Um marco somente muda de estado quando seus critérios de conclusão estiverem demonstrados no GKR. Nenhuma hipótese, draft ou ativo experimental é promovido automaticamente à Canon.