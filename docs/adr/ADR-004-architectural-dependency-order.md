---
id: ADR-004
title: Architectural Dependency Order
status: accepted
version: 1.0.0
owner: Guivos Enterprise Architecture
last_updated: 2026-06-28
---

# ADR-004 — Architectural Dependency Order

## Contexto

A evolução da GEA não deve ocorrer apenas por uma sequência editorial de documentos. Cada unidade arquitetural depende de conceitos, modelos e decisões anteriores. Consolidar uma unidade antes de suas dependências aumenta risco de retrabalho, inconsistência e dependências circulares.

## Decisão

Uma unidade arquitetural somente pode ser consolidada quando todos os conceitos dos quais depende estiverem, no mínimo, em estado `validated`.

O roadmap da GEA deve ser organizado por dependências arquiteturais, e não apenas por ordem temática ou documental.

## Regras

1. Toda unidade deve declarar suas dependências explícitas.
2. Dependências devem apontar para ativos oficiais do GKR.
3. Unidades dependentes não podem redefinir conceitos de suas dependências.
4. Dependências circulares devem ser eliminadas antes da consolidação.
5. Alterações em uma unidade exigem análise de impacto sobre suas dependentes.
6. O estado `stable` exige que todas as dependências estejam, no mínimo, `validated`.
7. Exceções exigem justificativa e ADR específico.

## Aplicação inicial na Business Architecture

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

## Consequências positivas

- reduz retrabalho;
- evita consolidação prematura;
- melhora rastreabilidade;
- permite análise de impacto;
- organiza o roadmap por lógica arquitetural;
- prepara a GEA para representação futura em grafo de conhecimento.

## Custos e limitações

- pode impedir o avanço de unidades enquanto dependências não forem validadas;
- exige manutenção de metadados de dependência;
- torna revisões transversais obrigatórias após alterações estruturais.

## Alternativas rejeitadas

### Evolução apenas por ordem de documentos

Rejeitada porque não representa as relações reais entre os ativos.

### Consolidação paralela sem dependências explícitas

Rejeitada porque aumenta risco de conflito e duplicidade.

## Estado

Decisão aceita e aplicável a todas as arquiteturas da GEA.
