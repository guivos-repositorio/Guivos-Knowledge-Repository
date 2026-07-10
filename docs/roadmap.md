---
title: Roadmap Arquitetural
status: active
version: 4.8.0
owner: Guivos
last_updated: 2026-07-04
---

# Roadmap Arquitetural

Este roadmap acompanha a evolução do Guivos Knowledge Repository, da Guivos Enterprise Architecture e das frentes de especificação executável da Guivos.

## Estado atual

- **Era vigente:** `GE-2 — Knowledge`.
- **Marco vigente:** `M5.5 — Context and Architecture Engineering Checkpoint`.
- **Modo vigente da GE-2:** `Institutional Consolidation Mode`.
- **Modo vigente da GKA:** `Institutional Writing`.
- **Sprint vigente:** `0.28.0 — Guivos Knowledge Architecture Foundation`.
- **Checkpoint vigente:** `CHECKPOINT-ARCHITECTURE-ENGINEERING-PAUSE`, versão `1.0.0`.
- **Matrizes de sincronização:** `GE2-SYNC-001`, `GE2-SYNC-002`, `GE2-SYNC-003` e `GE2-SYNC-004`.
- **Documento atual da GKA:** `GKA-000 — Parte V — Evolução Institucional`.
- **Frente registrada:** `Enterprise Design & Business Specification`.
- **Especificação preservada:** `PAS-001 — Guivos Journey`, versão `0.2.0`.
- **Arquitetura funcional vigente:** `GLPA-001 — Guivos Layered Product Architecture`.
- **Foco de retomada:** `Architecture Engineering Sprint`.
- **Conceitos candidatos preservados:** Captura Multimodal, CIE, LPM, GPMA e Intelligence Engines.
- **Baseline da Foundation:** `A2-B3` — frozen.
- **Revisão ativa:** `A2-R02 — Fundamental Model Review`, em espera operacional.
- **Produto comercial oficial:** `Guivos Mall`.
- **Novo domínio planejado:** `Guivos Economic Model`.

## GE-2 — Knowledge

**Estado:** Active — Institutional Consolidation Mode.

### Marcos concluídos

- [x] `M4 — Knowledge Architecture Established`;
- [x] `M5 — GKA Foundation Started`;
- [x] `M5.1 — GKA Preparation Complete`;
- [x] `M5.2 — GKA Institutional Consolidation Registered`;
- [x] `M5.3 — GKA Conceptual Architecture Advanced`;
- [x] `M5.4 — Enterprise Design and GLPA Registered`;
- [x] `M5.5 — Context and Architecture Engineering Checkpoint`.

### Fluxo atual

```text
GKA-000 Partes I-IV
  -> Completed Conceptually

GKA-000 Parte V
  -> Pending Completion

Enterprise Design & Business Specification
  -> Active

PAS-001 / GLPA
  -> Preserved

Context and Participant Model Discovery
  -> Synchronized

Architecture Engineering Sprint
  -> Next

GKA-000 Review and Publication
  -> Planned

Resume A2-R02
  -> Planned
```

## Enterprise Design & Business Specification

**Estado:** Active — Paused at Architecture Engineering Checkpoint.

Backlog executivo preservado:

1. Arquitetura funcional dos produtos;
2. Guivos Economic Model;
3. Commercial Model;
4. Go-to-Market.

## PAS-001 — Guivos Journey

**Estado:** Draft 0.2.0 — Preserved.

Conteúdo consolidado:

- Product Philosophy;
- Visão do Produto;
- Journey como Experience Layer;
- Captura Multimodal de Contexto;
- voz como canal prioritário;
- regras de consentimento, revisão e explicabilidade;
- LPM como conceito candidato;
- CIE como capacidade candidata;
- hierarquia GPA → PAS → JFA → FDS → UX → Technical.

O PAS não será expandido antes da definição da taxonomia e do meta-modelo do GKR.

## Contexto e Modelo Vivo do Participante

**Estado:** Discovery / Engineering Candidate.

Conceitos preservados:

- Captura Multimodal de Contexto;
- `Living Participant Model (LPM)`;
- `Context Intelligence Engine (CIE)`;
- possíveis especializações para Pessoa, Organização e Coletivo;
- distinção entre memória contextual do participante e memória relacional do Grafo Global;
- família candidata de Intelligence Engines.

Nenhum desses conceitos foi promovido automaticamente à Canon.

## Architecture Engineering Sprint

**Estado:** Next — Not Started.

Objetivo:

> Projetar a estrutura definitiva do GKR antes de expandir o conjunto de documentos permanentes.

Entregáveis previstos:

1. taxonomia oficial de artefatos;
2. meta-modelo do GKR;
3. categorias documentais;
4. dependências permitidas;
5. ciclo de vida de artefatos;
6. critérios de promoção à Canon;
7. regras de nomenclatura e identificadores;
8. ponto único de manutenção de conceitos estruturais.

## Ativos candidatos pendentes de decisão

| Ativo | Estado | Condição |
|---|---|---|
| GTF — Guivos Transformation Framework | Candidate | Architecture Engineering Sprint |
| GCM — Guivos Conceptual Model | Candidate | Architecture Engineering Sprint |
| GPMA — Guivos Participant Model Architecture | Candidate | Architecture Engineering Sprint |
| GIA detalhada por Intelligence Engines | Candidate | Architecture Engineering Sprint |
| GLS — Guivos Language System | Candidate | Architecture Engineering Sprint |
| GDP — Guivos Design Principles | Candidate | Architecture Engineering Sprint |
| GDF — Guivos Decision Framework | Candidate | Architecture Engineering Sprint |
| GAME — Guivos Architecture Methodology & Engineering | Candidate | Architecture Engineering Sprint |
| JFA — Journey Functional Architecture | Candidate / Planned | Taxonomia aprovada |
| FDS — Functional Domain Specifications | Candidate / Planned | JFA aprovada |

## Restrições

- não criar novos documentos estruturais apenas por utilidade aparente;
- não promover hipóteses diretamente à Canon;
- não criar GTF, GCM, GPMA, GLS, GDP, GDF ou GAME antes do sprint;
- não criar `docs/knowledge-architecture/` antes da aprovação integral do GKA-000;
- preservar o PAS-001 sem transformar candidatos em componentes técnicos obrigatórios.

## Guivos Economic Model

**Estado:** Planned — Domain Created.

Seu desenvolvimento detalhado permanece posterior à consolidação suficiente da arquitetura funcional e conceitual.

## Ponto exato de retomada

Retomar pelo `Architecture Engineering Sprint`.

Primeira atividade:

> Projetar a taxonomia oficial e o meta-modelo do Guivos Knowledge Repository.

Somente depois decidir quais ativos candidatos devem ser criados e retomar o PAS-001 pela JFA e pela Captura Multimodal de Contexto.

A conclusão da Parte V do `GKA-000` permanece pendente antes da criação de `docs/knowledge-architecture/`.