---
title: Architectural Milestones
status: active
version: 4.5.0
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
| M5.1 — GKA Preparation Complete | Completed | Encerrar a preparação da GKA e iniciar a redação institucional do GKA-000 |
| M5.2 — GKA Institutional Consolidation Registered | Completed | Registrar decisões metodológicas posteriores à preparação da GKA |
| M5.3 — GKA Conceptual Architecture Advanced | Completed | Registrar conclusão conceitual das Partes II, III e IV do GKA-000 |
| M5.4 — Enterprise Design and GLPA Registered | Completed | Registrar frente de especificação executável, PAS-001 e GLPA |
| A2 — Functional Architecture Discovery | Active | Descobrir e validar estruturas funcionais e Core Capabilities |
| K1 — Fundamental Knowledge Frozen | Planned | Congelar o conhecimento fundamental após A2-R02 |
| A3 — Operational Architecture | Planned | Descrever cooperação e fluxos entre capacidades |
| A4 — Platform Engineering | Planned | Materializar arquiteturas de referência |
| A5 — Canon 1.0 | Planned | Consolidar a primeira Canon integrada |

## M5.4 — Enterprise Design and GLPA Registered

**Estado:** Completed em 04/07/2026.

### Critério de conclusão

As decisões tomadas durante a transição para a especificação executável da Guivos foram registradas no GKR, incluindo a criação da `GLPA-001 — Guivos Layered Product Architecture` e o início do `PAS-001 — Guivos Journey`.

### Resultados

- `GE2-SYNC-003 — Enterprise Design and Layered Product Architecture Sync` criado;
- `GLPA-001 — Guivos Layered Product Architecture` criado e aprovado como referência funcional;
- `PAS-001 — Guivos Journey` criado em estado `draft`;
- Arquitetura de Produtos atualizada para a versão `1.2.0`;
- Guivos Journey atualizado para a versão `1.2.0`, reconhecido como Experience Layer;
- Roadmap atualizado para `4.7.0`;
- Knowledge Board atualizado para `4.7.0`;
- Glossário atualizado para `1.7.0`;
- Changelog atualizado para `0.28.4`;
- MkDocs atualizado com GLPA, PAS-001 e GE2-SYNC-003.

### Decisão estrutural

A Guivos passa a organizar sua arquitetura funcional de produtos por camadas:

- Experience Layer — Guivos Journey;
- Intelligence Layer — Guivos Intelligence;
- Service Layer — Guivos Business, Mall, Travel, Media e Ads;
- Platform Layer — capacidades técnicas comuns.

### Efeito

O próximo trabalho é retomar o `PAS-001 — Guivos Journey`, consolidando a GLPA dentro da especificação funcional do Journey e avançando para a arquitetura funcional completa do produto/camada.

A conclusão da Parte V do `GKA-000` permanece pendente antes da criação de `docs/knowledge-architecture/`.

## Marcos anteriores preservados

Os marcos `M3`, `M3.1`, `M4`, `M5`, `M5.1`, `M5.2` e `M5.3` permanecem válidos conforme versões anteriores deste documento.

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