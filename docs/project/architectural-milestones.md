---
title: Architectural Milestones
status: active
version: 4.1.0
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
| M4 — Knowledge Architecture Established | Completed | Reconhecer a GKA como arquitetura de primeira classe e iniciar GE-2 |
| M5 — GKA Foundation Started | Active | Iniciar a fundação documental da GKA com escopo e checkpoint definidos |
| A2 — Functional Architecture Discovery | Active | Descobrir e validar estruturas funcionais e Core Capabilities |
| K1 — Fundamental Knowledge Frozen | Planned | Congelar o conhecimento fundamental após A2-R02 |
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

## M4 — Knowledge Architecture Established

**Estado:** Completed em 04/07/2026.

### Critério de conclusão

A Guivos reconheceu formalmente a `Guivos Knowledge Architecture (GKA)` como arquitetura de primeira classe por meio do `ADR-006`.

### Resultados

- `ADR-006 — Guivos Knowledge Architecture as a First-Class Architecture` aprovado;
- `GEF-001 — Guivos Evolution Framework` criado;
- `GE-2 — Knowledge` iniciada;
- GEA atualizada para reconhecer a GKA;
- conhecimento institucional reconhecido como ativo estratégico permanente;
- Canon redefinida como conhecimento institucional vigente mais confiável, estável e revisável;
- fluxo realidade → evidências → conhecimento → Canon → arquitetura → produtos formalizado;
- regra de que arquiteturas permanentes devem derivar de conhecimento consolidado formalizada.

## M5 — GKA Foundation Started

**Estado:** Active em 04/07/2026.

### Critério de abertura

O planejamento da versão `0.28.0 — Guivos Knowledge Architecture Foundation` foi concluído e preservado no `CHECKPOINT-GE2-GKA-FOUNDATION`.

### Escopo aprovado

- `GKA-000 — Guivos Knowledge Architecture`;
- `GKP-001 — Guivos Knowledge Principles`;
- `GKM-001 — Guivos Knowledge Method`;
- `GDP-001 — Guivos Discovery Protocol`;
- `GEM-001 — Guivos Evidence Model`;
- `GKC-001 — Guivos Canonical Consolidation`;
- `GKV-001 — Guivos Knowledge Validation`;
- `GKL-001 — Guivos Knowledge Lifecycle`.

### Restrições

- nenhum novo produto;
- nenhuma nova arquitetura permanente;
- nenhum novo domínio estrutural paralelo;
- nenhuma hipótese promovida diretamente à Canon;
- a pasta `knowledge-architecture/` somente será criada após aprovação do GKA-000.

### Critério de conclusão futuro

M5 será concluído quando os oito ativos da fundação da GKA estiverem publicados, sincronizados e revisados.

## A2 — Functional Architecture Discovery

**Estado:** Active — Operationally Paused.

### Revisões

| Revisão | Estado |
|---|---|
| A2-R01 — Foundation Architecture Review | Completed — Frozen in A2-B3 |
| A2-R02 — Fundamental Model Review | Active — Execution Ready — Operationally Paused |
| A2-R03 — Business Architecture Review | Planned |
| A2-R04 — Product Architecture Review | Planned |
| A2-R05 — Cross-Architecture Review | Planned |

### Restrições

- nenhuma Core Capability nasce por brainstorming isolado;
- produtos, funcionalidades, serviços e tecnologias não são automaticamente Core Capabilities;
- toda candidata exige convergência e rastreabilidade;
- o catálogo deve representar o menor conjunto suficiente;
- hipóteses permanecem fora da Canon até validação.

## K1 — Fundamental Knowledge Frozen

**Estado:** Planned.

Critérios previstos:

- corpus integralmente analisado;
- FMEM concluída;
- Canonical Consolidation concluída;
- princípios fundamentais rastreados às evidências;
- readiness demonstrado;
- validação formal registrada;
- auditoria concluída;
- baseline de conhecimento congelada.

## Guivos Economic Model

**Estado:** Domain Created — Development Planned.

O domínio foi criado em 04/07/2026. Seu desenvolvimento detalhado ocorrerá após dependências suficientes do Modelo Fundamental, GCCM, Business Architecture, Product Architecture e Business Outcomes.

## Regra de transição

Um marco somente muda de estado quando seus critérios de conclusão estiverem demonstrados no GKR. Nenhuma hipótese, draft ou ativo experimental é promovido automaticamente à Canon.