---
title: Knowledge Board
status: active
version: 2.5.0
owner: Guivos
last_updated: 2026-07-01
---

# Knowledge Board

Painel oficial de acompanhamento do patrimônio intelectual e arquitetural da Guivos.

## Estado institucional

| Ativo | Estado | Finalidade |
|---|---|---|
| M1 — Research Foundation Complete | Frozen | Referência estável dos fundamentos |
| M2.0 — Architectural Evolution Hypothesis | Experimental | Preservar hipóteses estruturantes fora da Canon |
| GEA-PLM-001 — Permanence Layer Model | Validated | Organizar ativos por permanência, horizonte e governança |
| A1 — Institutional Architecture Complete | Completed | Encerrar a expansão estrutural contínua da arquitetura institucional |
| A2 — Functional Architecture Discovery | Active | Descobrir as Core Capabilities permanentes da Guivos |
| GCCM-001 — Guivos Core Capability Model | Discovery 0.2.0 | Extrair, testar e validar capacidades a partir do GKR |

Consulte:

- [Architectural Milestones](architectural-milestones.md)
- [GCCM-001](../reference-architecture/gccm-001.md)
- [Baseline M1](BASELINE-M1.md)
- [Checkpoint M2.0](CHECKPOINT-M2.0.md)
- [Permanence Layer Model](../enterprise-architecture/permanence-layer-model.md)

## Legenda

| Status | Significado |
|---|---|
| ⬜ | Não iniciado |
| 🟦 | Em descoberta |
| 🟨 | Hipótese ou proposta estruturada |
| 🟧 | Em experimentação, consolidação ou validação |
| 🟩 | Consolidado no GKR |

## Architectural Milestones

| Marco | Status |
|---|:---:|
| A0 — GKR Foundation | 🟩 |
| A1 — Institutional Architecture Complete | 🟩 |
| A2 — Functional Architecture Discovery | 🟦 Active |
| A3 — Operational Architecture | ⬜ |
| A4 — Platform Engineering | ⬜ |
| A5 — Canon 1.0 | ⬜ |

## A2 — Functional Architecture Discovery

### Entregável ativo

`GCCM-001 — Guivos Core Capability Model`, versão `0.2.0`.

### Estado do GCCM

| Elemento | Estado |
|---|:---:|
| Propósito e pergunta arquitetural | 🟩 |
| Definição de Core Capability | 🟩 |
| Princípios de descoberta | 🟩 |
| Core Capability Admission Rule | 🟩 |
| Testes de destruição e irredutibilidade | 🟩 |
| Estrutura de evidências | 🟩 |
| Inventário de evidências | 🟦 Iniciado |
| Primeira fonte analisada | 🟩 |
| Agrupamento semântico multifuente | ⬜ |
| Registro de candidatas | ⬜ |
| Teste de cobertura da missão | ⬜ |
| Validação arquitetural | ⬜ |
| Catálogo canônico | ⬜ |

> Nenhuma Core Capability está canônica nesta versão.

### Primeira Evidence Extraction

| Campo | Resultado |
|---|---|
| Fonte | `GEB-P01-F01 — Essência da Guivos` |
| Estado da fonte | `consolidated` |
| Afirmações institucionais | 29 |
| Grupos de significado | 5 |
| Invariantes provisórios | 6 |
| Responsabilidades institucionais | 9 |
| Agrupamentos observados | 6 |
| Core Capabilities candidatas | 0 |

### Agrupamentos observados

| ID | Agrupamento | Natureza | Estado |
|---|---|---|---|
| EV-F01-01 | Compreensão de contexto | Funcional | Observed |
| EV-F01-02 | Identificação de possibilidades relevantes | Funcional | Observed |
| EV-F01-03 | Conexão e fortalecimento do ecossistema | Funcional | Observed |
| EV-F01-04 | Apoio à progressão da jornada | Funcional | Observed |
| EV-F01-05 | Preservação da autonomia | Constitucional | Observed |
| EV-F01-06 | Governança de aderência à jornada | Constitucional | Observed |

Os agrupamentos dependem de confirmação cruzada. Não representam Core Capabilities.

### Aprendizados registrados

- a Foundation produz identidade, limites, obrigações e critérios de decisão;
- evidências funcionais e restrições constitucionais não devem ser confundidas;
- nem toda evidência deve originar uma Core Capability;
- `Institutional Functions` foi rejeitada como camada arquitetural permanente;
- agrupamentos analíticos permanecem ferramentas do método até demonstração de valor arquitetural próprio.

## Pending Strategic Domains

| Tema | Estado | Dependência | Observação |
|---|---|---|---|
| Enterprise Economic Model | Planned / Deferred | GCCM, Business Outcomes e Core Business Capabilities | Pendência formal da Business Architecture |
| Global Governance Model | Planned | Governance Architecture e expansão global | Escopo ainda não definido |
| Organizational Model | Planned | Business Outcomes, Capabilities e Value Chains | Previsto em BA-ORG-001 |
| Operating Model | Planned | Organizational Model e PRA | Previsto em BA-ORG-002 |
| AI Governance | Planned | AI, Data Governance e Security Reference Architectures | Aguardar A3 |
| Knowledge Graph Logical Model | Planned | GCCM, PRA e Data & Intelligence Architecture | Aguardar definição conceitual do domínio |
| Enterprise Metrics Framework | Planned | Outcomes, Economic Model e Operating Model | Aguardar dependências |

### Enterprise Economic Model

Escopo preliminar reconhecido:

- geração, captura e distribuição de valor;
- compartilhamento de valor entre participantes do ecossistema;
- reinvestimento;
- incentivos econômicos;
- sustentabilidade de longo prazo;
- monetização;
- efeitos de rede;
- equilíbrio entre impacto e sustentabilidade empresarial.

O registro é uma pendência estratégica. Não cria uma nova arquitetura nem antecipa decisões sobre monetização, preços ou mecanismos econômicos.

## Arquitetura institucional

| Ativo | Estado |
|---|:---:|
| Foundation Architecture | 🟩 |
| Guivos Enterprise Architecture | 🟩 |
| Permanence Layer Model | 🟩 |
| Institutional Permanence | 🟩 |
| Vision First | 🟩 |
| Architectural Gravity | 🟩 |
| Progressive Realization | 🟩 |
| Downward Influence | 🟩 |
| Layer Integrity | 🟩 |

### Camadas de permanência

| Camada | Horizonte | Finalidade |
|---|---|---|
| Permanent Architecture | Décadas | Identidade, princípios, Canon e macroestrutura |
| Reference Architecture | Anos | Melhor forma arquitetural conhecida de realizar a visão |
| Enterprise Programs | Meses e ciclos plurianuais | Programas estratégicos que realizam a arquitetura |
| Enterprise Delivery | Dias, semanas e releases | Execução, código, infraestrutura e releases |

## Ciclo de maturidade experimental

`Idea -> Hypothesis -> Experimental -> Validated -> Canonical -> Deprecated`

A progressão não é automática e nenhum ativo entra na Canon apenas por elegância conceitual.

## Hipóteses arquiteturais estruturantes

| Ativo | Natureza | Estado | Observação |
|---|---|---|---|
| Guivos Meta-Model — GMM | Architectural Meta-Hypothesis | Hypothesis | Fora da Canon |
| Guivos Knowledge System — GKS | Domínio institucional proposto | Hypothesis | Fora da Canon |
| Knowledge Validation Framework — GKVF | Componente candidato | Idea | Não iniciado |
| Knowledge Validation Standards — KVS | Padrões candidatos | Idea | Não iniciado |

## Maturidade das arquiteturas

| Arquitetura | Maturidade |
|---|---|
| Foundation Architecture | Stable |
| Ecosystem Architecture / GEB | Validated no modelo fundamental; demais modelos em evolução |
| Product Architecture | Stable na estrutura superior |
| Business Architecture | Validated em Foundations e Strategy inicial; Outcomes e Economic Model pendentes |
| Data & Intelligence Architecture | Draft |
| Technology Architecture | Draft |
| Governance Architecture | Draft |
| Knowledge Architecture | Draft |
| Reference Architecture / GCCM | Discovery 0.2.0 |

## Foundation Architecture

| Unidade | Status |
|---|:---:|
| Essência | 🟩 Analisada na A2.2 |
| Propósito | 🟩 |
| Missão Operacional | 🟩 |
| Visão de Longo Prazo | 🟩 |
| Constituição | 🟩 |
| Princípios Permanentes | 🟩 |
| PP-11 — Maturidade institucional | 🟩 |
| PP-12 — Visão antes da execução | 🟩 |
| PP-13 — Realização progressiva | 🟩 |
| PP-14 — Permanência proporcional à mudança | 🟩 |

## Ecosystem Architecture / GEB

| Unidade | Status |
|---|:---:|
| KU-FM-001 — Fenômeno da Evolução | 🟩 |
| KU-FM-002 — Modelo Fundamental da Jornada | 🟩 |
| KU-FM-003 — Quatro Naturezas Fundamentais | 🟩 |
| Modelo do Participante | 🟨 |
| Identidade | 🟨 |
| Capacidades | 🟨 |
| Papéis | 🟨 |
| Modelo da Oportunidade | 🟨 |
| Modelo da Experiência | ⬜ |
| Relacionamentos | ⬜ |
| Conhecimento do Ecossistema | ⬜ |

## Product Architecture

| Produto | Status |
|---|:---:|
| Guivos Journey | 🟩 |
| Guivos Marketplace | 🟧 |
| Guivos Travel | 🟩 |
| Guivos Business | 🟩 |
| Guivos Media | 🟩 |
| Guivos Intelligence | 🟩 |
| Guivos Ads | 🟩 |

## Business Architecture

| Ordem | Unidade | Maturidade | Status |
|---:|---|---|:---:|
| 1 | BA-FND-001 — Business Architecture Foundations | Validated | 🟩 |
| 2 | BA-STR-001 — Business Transformation Model | Validated | 🟩 |
| 3 | BA-STR-002 — Business Outcomes | Draft | 🟧 |
| 4 | BA-CAP-001 — Core Business Capabilities | Draft | ⬜ |
| 5 | BA-CAP-002 — Capability Map | Draft | ⬜ |
| 6 | BA-STR-003 — Value Chains | Draft | ⬜ |
| 7 | Enterprise Economic Model | Planned / Deferred | 🟨 |
| 8 | BA-ORG-001 — Organizational Model | Draft | ⬜ |
| 9 | BA-ORG-002 — Operating Model | Draft | ⬜ |
| 10 | BA-EXE-001 — Business Processes | Draft | ⬜ |
| 11 | BA-EXE-002 — KPIs & Metrics | Draft | ⬜ |

## Research

| Ativo | Status |
|---|:---:|
| Research Domain | 🟩 |
| RP-001 — Ecosystem Research Program | 🟧 |
| RP-001 Research Protocol | 🟩 |
| Estado da Arte — Ciclo 1 | 🟨 |
| MS-001 | 🟧 |
| Evidence Registry | ⬜ |
| Ecosystem Phenomena Catalog — EPC | ⬜ |
| Architectural Recommendations | ⬜ |

O Evidence Registry e a validação da MS-001 permanecem pendentes. A abertura da A2 não os torna concluídos.

## Governança documental

| Ativo | Status |
|---|:---:|
| GKR como representação canônica da Guivos madura | 🟩 |
| Markdown como formato oficial | 🟩 |
| Pipeline GitHub -> Markdown -> Mermaid -> Site -> PDF | 🟩 |
| Glossário Canônico | 🟩 |
| Matriz de Consolidação Canônica | 🟩 |
| Roadmap Arquitetural | 🟩 |
| Architectural Milestones | 🟩 |
| GCCM-001 | 🟦 0.2.0 |
| ADR-003 — Architectural Ownership | 🟩 |
| ADR-004 — Architectural Dependency Order | 🟩 |
| ADR-005 — Architectural Traceability Principle | 🟩 |
| AV-001 — GEA Structure Validation | 🟧 |

## Fase atual

`A2 — Functional Architecture Discovery`, em execução.

## Objetivo principal

Descobrir, validar e consolidar o conjunto mínimo e suficiente de Core Capabilities permanentes da Guivos, com rastreabilidade até as evidências existentes no GKR.

## Próxima atividade

Analisar a próxima unidade da Foundation Architecture e confrontar suas evidências com os seis agrupamentos observados na Essência.

## Última consolidação

Primeira Evidence Extraction do GCCM registrada em 01/07/2026, com análise de `GEB-P01-F01 — Essência da Guivos` e nenhuma Core Capability promovida.
