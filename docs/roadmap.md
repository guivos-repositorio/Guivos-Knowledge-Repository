---
title: Roadmap Arquitetural
status: active
version: 4.7.0
owner: Guivos
last_updated: 2026-07-04
---

# Roadmap Arquitetural

Este roadmap acompanha a evolução do Guivos Knowledge Repository, da Guivos Enterprise Architecture e das frentes de especificação executável da Guivos.

## Estado atual

- **Era vigente:** `GE-2 — Knowledge`.
- **Marco vigente:** `M5.4 — Enterprise Design and GLPA Registered`.
- **Modo vigente da GE-2:** `Institutional Consolidation Mode`.
- **Modo vigente da GKA:** `Institutional Writing`.
- **Sprint vigente:** `0.28.0 — Guivos Knowledge Architecture Foundation`.
- **Checkpoint vigente:** `CHECKPOINT-GKA-PREPARATION-COMPLETE`, versão `1.2.0`.
- **Matrizes de sincronização:** `GE2-SYNC-001`, `GE2-SYNC-002` e `GE2-SYNC-003`.
- **Documento atual da GKA:** `GKA-000 — Parte V — Evolução Institucional`.
- **Nova frente registrada:** `Enterprise Design & Business Specification`.
- **Especificação em desenvolvimento:** `PAS-001 — Guivos Journey`.
- **Arquitetura funcional registrada:** `GLPA-001 — Guivos Layered Product Architecture`.
- **Baseline da Foundation:** `A2-B3` — frozen.
- **Fase ativa:** `A2 — Functional Architecture Discovery`.
- **Revisão ativa:** `A2-R02 — Fundamental Model Review`, em espera operacional até a fundação documental da GKA.
- **Produto comercial oficial:** `Guivos Mall`.
- **Inteligência consolidada:** `Inteligência do Ecossistema Guivos`.
- **Modelo conceitual de conexões:** `Grafo Global da Guivos`.
- **Manifesto vigente:** `GAI-002 — Manifesto da Inteligência do Ecossistema Guivos`.
- **Novo domínio planejado:** `Guivos Economic Model`.
- **Core Capabilities candidatas:** 0.
- **Core Capabilities canônicas:** 0.

## GE-2 — Knowledge

**Estado:** Active — Institutional Consolidation Mode.

### Concluído

- [x] Aprovar `ADR-006 — Guivos Knowledge Architecture as a First-Class Architecture`.
- [x] Criar `GEF-001 — Guivos Evolution Framework`.
- [x] Formalizar `GE-2 — Knowledge`.
- [x] Registrar `M4 — Knowledge Architecture Established`.
- [x] Registrar `M5 — GKA Foundation Started`.
- [x] Registrar `M5.1 — GKA Preparation Complete`.
- [x] Registrar `M5.2 — GKA Institutional Consolidation Registered`.
- [x] Registrar `GE2-SYNC-002 — GKA Conceptual Architecture Progress Sync`.
- [x] Concluir conceitualmente as Partes II, III e IV do GKA-000.
- [x] Registrar `M5.3 — GKA Conceptual Architecture Advanced`.
- [x] Registrar `GE2-SYNC-003 — Enterprise Design and Layered Product Architecture Sync`.
- [x] Criar `GLPA-001 — Guivos Layered Product Architecture`.
- [x] Criar `PAS-001 — Guivos Journey`.
- [x] Registrar `M5.4 — Enterprise Design and GLPA Registered`.

### Fluxo atual da GE-2

```text
GKA Preparation
  -> Completed

GKA Institutional Consolidation
  -> Active

GKA-000 Partes I-IV
  -> Completed Conceptually

GKA-000 Parte V
  -> Pending Completion

Enterprise Design & Business Specification
  -> Active

PAS-001 / GLPA
  -> Current

GKA-000 Review
  -> Planned

GKA Foundation Published
  -> Planned

Resume A2-R02
  -> Planned
```

## Sprint 0.28.0 — Guivos Knowledge Architecture Foundation

**Estado:** Institutional Consolidation Active.

Atividade da GKA ainda pendente:

> Concluir a Parte V — Evolução Institucional do `GKA-000 — Guivos Knowledge Architecture`.

Frente paralela registrada:

> Especificar funcionalmente a Guivos por meio de `Enterprise Design & Business Specification`, iniciando pelo `PAS-001 — Guivos Journey` e pela `GLPA-001`.

Restrições:

- não criar documento independente de governança nesta fase;
- não criar documento independente de rastreabilidade nesta fase;
- não abrir novas arquiteturas permanentes sem validação;
- não publicar hipóteses como Canon;
- não criar `docs/knowledge-architecture/` antes da aprovação integral do GKA-000.

## Enterprise Design & Business Specification

**Estado:** Active — Execution Specification Started.

Objetivo:

> Transformar a arquitetura institucional da Guivos em especificações funcionais, operacionais, econômicas e comerciais suficientes para orientar Produto, UX, Engenharia, Comercial, Marketing e investidores.

### Backlog executivo

1. Arquitetura funcional dos produtos;
2. Guivos Economic Model;
3. Commercial Model;
4. Go-to-Market.

### Ordem inicial dos produtos/camadas

1. Guivos Journey;
2. Guivos Mall;
3. Guivos Business;
4. Guivos Intelligence;
5. Guivos Ads;
6. Guivos Media;
7. Guivos Travel.

## GLPA-001 — Guivos Layered Product Architecture

**Estado:** Approved 1.0.0.

A GLPA organiza a Guivos por camadas funcionais:

| Camada | Componente |
|---|---|
| Experience Layer | Guivos Journey |
| Intelligence Layer | Guivos Intelligence |
| Service Layer | Guivos Business, Mall, Travel, Media e Ads |
| Platform Layer | APIs, Graph, Auth, Billing, Search, Notifications, Security e capacidades comuns |

## PAS-001 — Guivos Journey

**Estado:** Draft 0.1.0.

Conteúdo iniciado:

- Product Philosophy;
- Visão do Produto;
- definição do Journey como Experience Layer;
- princípios de produto;
- limites do Journey;
- relação com Intelligence, Business, Mall, Media, Travel e Ads.

Próxima atividade:

> Retomar pela consolidação da GLPA dentro do PAS-001 e avançar para Missão, Objetivos Estratégicos, Público-alvo, Arquitetura Funcional, Fluxos, IA, Integrações, Modelo Econômico, KPIs e Roadmap.

## A2-R02 — Fundamental Model Review

**Estado:** Active — Execution Ready — Operationally Paused.

A execução será retomada após a conclusão da fundação documental da GKA.

## Guivos Economic Model

**Estado:** Planned — Domain Created.

O desenvolvimento detalhado ocorrerá após a especificação funcional inicial do Journey e das responsabilidades econômicas dos produtos/camadas.

## Tópicos arquiteturais abertos

| Tema | Estado | Dependências |
|---|---|---|
| Guivos Knowledge Architecture Foundation | Active — Institutional Consolidation | ADR-006, M4, M5, M5.1, M5.2, M5.3 e M5.4 |
| Enterprise Design & Business Specification | Active | Product Architecture, Business Architecture, Economic Model |
| GLPA-001 | Approved | Product Architecture |
| PAS-001 — Guivos Journey | Draft | GLPA-001 |
| GEA-DOC-001 — Architectural Document Standard | Planned | Conclusão da GKA Foundation |
| GEA-DOC-002 — Architectural Artifact Taxonomy | Planned | Conclusão da GKA Foundation |
| Fundamental Knowledge Frozen | Planned | A2-R02 concluída |
| Guivos Economic Model | Planned / Domain Created | Product Architecture, Business Model, Business Outcomes |
| Enterprise Ontology | Deferred | Fundamental Knowledge Frozen |

## Ponto exato de retomada

Retomar pelo `PAS-001 — Guivos Journey`, consolidando a `GLPA-001 — Guivos Layered Product Architecture` como fundamento da arquitetura funcional do produto/camada.

Depois avançar para a arquitetura funcional completa do Journey antes de seguir para Modelo Econômico, Mall, Business, Ads, Media, Travel e Go-to-Market.

A conclusão da Parte V do `GKA-000` permanece pendente antes da criação de `docs/knowledge-architecture/`.