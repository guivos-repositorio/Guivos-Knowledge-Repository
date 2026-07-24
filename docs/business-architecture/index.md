---
id: GBA-000
title: Guivos Business Architecture
status: validated
version: 0.14.0
owner: Guivos Business Architecture
last_updated: 2026-07-24
related_adrs:
  - ADR-003
  - ADR-004
---

# Guivos Business Architecture

## Definição

A Guivos Business Architecture define como o negócio da Guivos transforma necessidades em valor sustentável e como a organização se estrutura para gerar, entregar, capturar e reinvestir esse valor no fortalecimento contínuo do Ecossistema Guivos.

Ela integra a Guivos Enterprise Architecture e não substitui a Foundation, a Ecosystem Architecture, a Product Architecture ou as arquiteturas especializadas de dados, tecnologia, governança e conhecimento.

## Unidades validadas

- [BA-FND-001 — Business Architecture Foundations](foundations/index.md)
- [BA-STR-001 — Business Transformation Model](strategy/business-transformation-model.md)

## Unidade ativa

- [BA-STR-002 — Business Outcomes](strategy/business-outcomes.md) — checkpoint 0.17.0; COEM em execução; catálogo canônico pendente.
- [BA-STR-002-COR-001 — Candidate Outcome Register](strategy/candidate-outcome-register.md) — 18 candidatos em `Under Validation`; dez disposições pendentes de decisão.
- [BA-STR-002-EOVP-001 — External Outcome Validation Protocol](strategy/external-outcome-validation-protocol.md) — execução concluída; gate `Ready for COEM`.
- [BA-STR-002-EOVB-001 — Batch 01, Agency and Evolution](strategy/outcome-validation-batch-01-agency-evolution.md) — três sínteses e um cluster concluídos.
- [BA-STR-002-EOVB-002 — Batch 02, Trust](strategy/outcome-validation-batch-02-trust.md) — três sínteses e a fronteira Ecosystem–Business analisada.
- [BA-STR-002-EOVB-003 — Batch 03, Value and Continuity](strategy/outcome-validation-batch-03-value-continuity.md) — três sínteses e um ciclo empresarial de sustentação analisado.
- [BA-STR-002-EOVB-004 — Batch 04, Resilience](strategy/outcome-validation-batch-04-resilience.md) — continuidade, resiliência e crescimento responsável discriminados.
- [BA-STR-002-EOVB-005 — Batch 05, Adaptation](strategy/outcome-validation-batch-05-adaptation.md) — relevância, aprendizagem e adequação contextual discriminadas.
- [BA-STR-002-EOVB-006 — Batch 06, Coverage Completion](strategy/outcome-validation-batch-06-coverage-completion.md) — cobertura de 18 candidatos e seis clusters concluída.
- [BA-STR-002-COEM-001 — Candidate Outcome Evaluation Matrix](strategy/candidate-outcome-evaluation-matrix.md) — 10 de 18 candidatos e 4 de 6 clusters avaliados.

## Organização interna

```mermaid
graph TD
    BA[Business Architecture]
    BA --> F[Foundation]
    BA --> S[Strategy]
    BA --> C[Capabilities]
    BA --> O[Organization]
    BA --> E[Execution]
```

| Camada | Pergunta principal | Ativos previstos |
|---|---|---|
| Foundation | O que é a Business Architecture na Guivos? | Propósito, escopo, limites e princípios |
| Strategy | Como o negócio transforma necessidades em resultados? | Business Transformation Model, Outcomes e Value Chains |
| Capabilities | Do que a Guivos precisa ser capaz? | Core Business Capabilities e Capability Map |
| Organization | Como a organização sustenta as capacidades? | Organizational Model e Operating Model |
| Execution | Como o negócio funciona e é medido? | Processos, KPIs e métricas |

## Sequência arquitetural

```text
Contexto
-> Necessidade
-> Priorização Estratégica
-> Capacidade
-> Produto ou Serviço
-> Experiência
-> Ecosystem Outcome
-> Business Outcome
-> Valor Gerado
-> Valor Capturado
-> Reinvestimento
-> Novo Contexto
```

Cada nível possui responsabilidade própria e não deve ser confundido com os demais.

## Ordem por dependências

```mermaid
graph LR
    FND[BA-FND-001] --> STR1[BA-STR-001]
    STR1 --> STR2[BA-STR-002]
    STR2 --> CAP1[BA-CAP-001]
    CAP1 --> CAP2[BA-CAP-002]
    CAP2 --> STR3[BA-STR-003]
    STR3 --> ORG1[BA-ORG-001]
    ORG1 --> ORG2[BA-ORG-002]
    ORG2 --> EXE1[BA-EXE-001]
    EXE1 --> EXE2[BA-EXE-002]
```

A ordem de construção é determinada pelas dependências arquiteturais, conforme o ADR-004.

## Roadmap de unidades

1. `BA-FND-001` — Business Architecture Foundations — **Validated**
2. `BA-STR-001` — Business Transformation Model — **Validated**
3. `BA-STR-002` — Business Outcomes — **Draft 0.17.0; COEM em execução**
4. `BA-CAP-001` — Core Business Capabilities
5. `BA-CAP-002` — Capability Map
6. `BA-STR-003` — Value Chains
7. `BA-ORG-001` — Organizational Model
8. `BA-ORG-002` — Operating Model
9. `BA-EXE-001` — Business Processes
10. `BA-EXE-002` — KPIs & Metrics

## Estado de maturidade

A Business Architecture está em estado **Validated em seus fundamentos e em seu modelo de transformação**.

O BA-STR-002 possui definição, propriedades, limites, governança conceitual, primeiro COR, seis lotes externos consolidados e COEM em execução com dois clusters avaliados. Permanece `draft` até conclusão e decisão da COEM, AQS-O01, catálogos canônicos e matriz de sustentação.

## Próximo incremento candidato

Revisão humana das seis disposições cumulativas e seleção governada do próximo cluster da COEM. O incremento não poderá executar disposições automaticamente, iniciar `BA-CAP-001` ou retomar Product Engineering.
