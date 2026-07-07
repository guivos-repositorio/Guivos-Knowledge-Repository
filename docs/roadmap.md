---
title: Roadmap Arquitetural
status: active
version: 4.4.0
owner: Guivos
last_updated: 2026-07-04
---

# Roadmap Arquitetural

Este roadmap acompanha a evolução do Guivos Knowledge Repository e da Guivos Enterprise Architecture.

## Estado atual

- **Era vigente:** `GE-2 — Knowledge`.
- **Marco vigente:** `M5.1 — GKA Preparation Complete`.
- **Modo vigente da GKA:** `Institutional Writing`.
- **Sprint vigente:** `0.28.0 — Guivos Knowledge Architecture Foundation`.
- **Checkpoint vigente:** `CHECKPOINT-GKA-PREPARATION-COMPLETE`.
- **Documento atual:** `GKA-000 — Guivos Knowledge Architecture`.
- **Baseline da Foundation:** `A2-B3` — frozen.
- **Fase ativa:** `A2 — Functional Architecture Discovery`.
- **Revisão ativa:** `A2-R02 — Fundamental Model Review`, em espera operacional até a fundação documental da GKA.
- **Arquitetura reconhecida:** `Guivos Knowledge Architecture (GKA)`.
- **Produto comercial oficial:** `Guivos Mall`.
- **Inteligência consolidada:** `Inteligência do Ecossistema Guivos`.
- **Modelo conceitual de conexões:** `Grafo Global da Guivos`.
- **Manifesto vigente:** `GAI-002 — Manifesto da Inteligência do Ecossistema Guivos`.
- **Novo domínio planejado:** `Guivos Economic Model`.
- **Core Capabilities candidatas:** 0.
- **Core Capabilities canônicas:** 0.

## Transição de era

A partir da versão `0.27.0`, o GKR entrou em sua segunda grande era de evolução.

Após consolidar as fundações arquiteturais do ecossistema, o foco passou a ser a produção sistemática de conhecimento institucional.

As futuras arquiteturas deverão derivar de conhecimento consolidado, e esse conhecimento deverá permanecer rastreável às evidências que o originaram.

## Pipeline vigente

```text
Realidade observada
  -> Observação
  -> Hipótese
  -> Investigação
  -> Evidências
  -> Conhecimento Consolidado
  -> Canon
  -> Arquitetura
  -> Capacidades
  -> Produtos
  -> Implementação
```

## GE-2 — Knowledge

**Estado:** Active.

### Objetivo

Institucionalizar a produção de conhecimento como competência permanente da Guivos.

### Concluído

- [x] Aprovar `ADR-006 — Guivos Knowledge Architecture as a First-Class Architecture`.
- [x] Criar `GEF-001 — Guivos Evolution Framework`.
- [x] Formalizar `GE-2 — Knowledge`.
- [x] Registrar `M4 — Knowledge Architecture Established`.
- [x] Reconhecer a GKA dentro da GEA.
- [x] Definir conhecimento institucional como ativo estratégico permanente.
- [x] Concluir o planejamento da sprint `0.28.0`.
- [x] Registrar `CHECKPOINT-GE2-GKA-FOUNDATION`.
- [x] Registrar `M5 — GKA Foundation Started`.
- [x] Encerrar a fase de preparação da GKA.
- [x] Registrar `CHECKPOINT-GKA-PREPARATION-COMPLETE`.
- [x] Registrar `M5.1 — GKA Preparation Complete`.

### Fluxo atual da GE-2

```text
GKA Preparation
  -> Completed

GKA-000 Writing
  -> Active

Knowledge Architecture Review
  -> Planned

GKA Foundation Published
  -> Planned

Resume A2-R02
  -> Planned
```

## Sprint 0.28.0 — Guivos Knowledge Architecture Foundation

**Estado:** Preparation Complete — Institutional Writing Active.

Objetivo único:

> Fundar oficialmente a Guivos Knowledge Architecture sem abrir novos domínios, produtos ou arquiteturas paralelas.

Atividade atual:

> Redigir, revisar e consolidar `GKA-000 — Guivos Knowledge Architecture`.

Escopo aprovado:

1. `GKA-000 — Guivos Knowledge Architecture`;
2. `GKP-001 — Guivos Knowledge Principles`;
3. `GKM-001 — Guivos Knowledge Method`;
4. `GDP-001 — Guivos Discovery Protocol`;
5. `GEM-001 — Guivos Evidence Model`;
6. `GKC-001 — Guivos Canonical Consolidation`;
7. `GKV-001 — Guivos Knowledge Validation`;
8. `GKL-001 — Guivos Knowledge Lifecycle`.

Restrições:

- não criar documento independente de governança nesta fase;
- não criar documento independente de rastreabilidade nesta fase;
- não criar modelo independente de maturidade nesta fase;
- não abrir novas arquiteturas permanentes;
- não criar novos produtos;
- não publicar hipóteses como Canon.

### Próximas ações da sprint

- [x] Concluir preparação da GKA.
- [x] Registrar checkpoint de preparação concluída.
- [ ] Redigir integralmente `GKA-000`.
- [ ] Revisar criticamente `GKA-000`.
- [ ] Criar o domínio `docs/knowledge-architecture/` somente após aprovação do GKA-000.
- [ ] Publicar `GKA-000`.
- [ ] Derivar os sete ativos restantes.
- [ ] Sincronizar README, página inicial, MkDocs, Roadmap, Knowledge Board, Milestones e Changelog.
- [ ] Encerrar a versão `0.28.0`.

## Ciclo de maturidade do conhecimento

A GE-2 passa a distinguir quatro estados:

```text
Ideia
  -> Hipótese
  -> Conhecimento Consolidado
  -> Canon
```

Essa classificação orientará a promoção de conceitos e evitará que ideias promissoras sejam incorporadas prematuramente à arquitetura permanente.

## Regras metodológicas ativas

- Canon First;
- Primazia da Canon;
- Prudência Arquitetural;
- Conservação Arquitetural;
- Maturidade Arquitetural;
- Encerramento de Concepção;
- Decision Rule 002 — Institutional Writing Readiness.

## A2-R01 — Foundation Architecture Review

**Estado:** Completed — Frozen in A2-B3.

- [x] Evidence Matrix.
- [x] Canonical Consolidation.
- [x] Readiness Assessment.
- [x] Validation.
- [x] Audit.
- [x] Baseline.

## A2-R02 — Fundamental Model Review

**Estado:** Active — Execution Ready — Operationally Paused.

- [x] Abrir formalmente a revisão.
- [x] Congelar a metodologia da FMEM.
- [x] Formalizar Discovery Mode e proteção da Canon.
- [x] Criar `A2-R02-FMEM-001`.
- [x] Definir corpus, rastreabilidade e critérios de promoção.
- [ ] Extrair evidências de `KU-FM-001`.
- [ ] Extrair evidências de `KU-FM-002`.
- [ ] Extrair evidências de `KU-FM-003`.
- [ ] Consolidar observações.
- [ ] Consolidar regularidades.
- [ ] Formular e testar hipóteses.
- [ ] Identificar candidatos fundamentais.
- [ ] Executar Canonical Consolidation.
- [ ] Avaliar readiness.
- [ ] Validar, auditar e congelar `K1 — Fundamental Knowledge Frozen`.

A execução será retomada após a conclusão da fundação documental da GKA.

## Intelligence Architecture

**Estado:** Core Concepts Consolidated — Technical Architecture Pending.

### Concluído

- [x] Consolidar `GAI-001 — Guivos Artificial Intelligence Knowledge Model`.
- [x] Criar `GAI-002 — Manifesto da Inteligência do Ecossistema Guivos`.
- [x] Adotar a expressão pública e conceitual `Inteligência do Ecossistema Guivos`.
- [x] Consolidar o `Grafo Global da Guivos` como modelo conceitual de conexões.
- [x] Relacionar inteligência, contexto, jornadas, experiências, conhecimento e evidências.
- [x] Consolidar autonomia humana, explicabilidade, privacidade e limites superiores.
- [x] Registrar o patrimônio cumulativo como vantagem arquitetural.

### Pendente

- [ ] Definir ontologia formal do grafo.
- [ ] Definir modelo lógico e físico.
- [ ] Selecionar tecnologias específicas.
- [ ] Definir governança operacional de dados e consentimento.
- [ ] Definir auditoria algorítmica.
- [ ] Definir controles técnicos de privacidade e segurança.
- [ ] Definir critérios quantitativos de evidência e qualidade.

## Guivos Economic Model

**Estado:** Planned — Domain Created.

### Objetivo

Descrever como a Guivos sustenta economicamente o ecossistema sem contrariar seu propósito.

### Princípio inicial

Planos pagos poderão acelerar, ampliar e personalizar jornadas, mas não deverão impedir que participantes de planos gratuitos descubram oportunidades, participem do ecossistema e evoluam.

### Entregáveis previstos

- [x] Criar o domínio `docs/economic-model/`.
- [ ] Consolidar princípios econômicos.
- [ ] Definir arquitetura de receitas.
- [ ] Definir planos gratuitos e pagos.
- [ ] Definir critérios de aceleração sem bloqueio.
- [ ] Definir incentivos, recompensas e benefícios.
- [ ] Definir economia de parceiros.
- [ ] Definir métricas econômicas.
- [ ] Validar aderência à Foundation.

## Próximas revisões

- [ ] Retomar A2-R02 após a GKA Foundation.
- [ ] Product Architecture Review.
- [ ] Business Architecture Review.
- [ ] Cross-Architecture Review.
- [ ] Core Capability consolidation.
- [ ] Operational Architecture.
- [ ] Platform Engineering.
- [ ] Canon 1.0.

## Tópicos arquiteturais abertos

| Tema | Estado | Dependências |
|---|---|---|
| Guivos Knowledge Architecture Foundation | Active — Institutional Writing | ADR-006, M4, M5 e M5.1 |
| Fundamental Knowledge Frozen | Planned | A2-R02 concluída |
| Guivos Economic Model | Planned / Domain Created | Fundamental Model, GCCM, Business Outcomes e Product Architecture |
| Global Governance Model | Planned | Governance Architecture e expansão global |
| Organizational Model | Planned | Outcomes e Capabilities |
| Operating Model | Planned | Organizational Model e PRA |
| AI Governance | Planned | Intelligence Architecture, Data Governance e Security |
| Knowledge Graph Logical Model | Planned | GCCM, PRA e Intelligence Architecture |
| Enterprise Metrics Framework | Planned | Outcomes, Economic Model e Operating Model |
| Enterprise Ontology | Deferred | Fundamental Knowledge Frozen |

## Ponto exato de retomada

Abrir `CHECKPOINT-GKA-PREPARATION-COMPLETE` e iniciar a redação institucional de `GKA-000 — Guivos Knowledge Architecture`, começando pela Parte I — Identidade da GKA.

Não criar a pasta `knowledge-architecture/` antes da aprovação do GKA-000.