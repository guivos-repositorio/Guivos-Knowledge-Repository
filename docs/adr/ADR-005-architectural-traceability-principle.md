---
id: ADR-005
title: Architectural Traceability Principle
status: accepted
version: 1.0.0
owner: Guivos Enterprise Architecture
last_updated: 2026-06-30
---

# ADR-005 — Architectural Traceability Principle

## Contexto

O crescimento do GKR aumenta o risco de decisões arquiteturais serem desconectadas das evidências, hipóteses, modelos e justificativas que lhes deram origem.

Sem rastreabilidade explícita, torna-se difícil:

- compreender por que uma decisão existe;
- avaliar o impacto de novas evidências;
- distinguir conhecimento consolidado de hipótese;
- revisar modelos sem perder coerência histórica;
- auditar a passagem de Research para Architecture e Execution.

## Decisão

Toda decisão arquitetural relevante da Guivos deve ser rastreável até os modelos explicativos, evidências, princípios e ativos oficiais que a sustentam.

Toda decisão permanece revisável diante de novas observações, evidências qualificadas ou resultados que contradigam seus pressupostos.

## Cadeia mínima de rastreabilidade

Quando aplicável, a cadeia deve permitir navegar entre:

```text
Fontes -> Evidências -> Síntese -> Modelo ou hipótese -> Decisão arquitetural -> Implementação -> Resultado observado
```

Nem toda decisão exigirá todos os níveis, mas decisões estruturais não podem depender apenas de preferência, autoridade pessoal ou conveniência momentânea.

## Regras

1. decisões arquiteturais devem apontar para ativos oficiais do GKR;
2. evidências utilizadas devem possuir origem identificável;
3. hipóteses não podem ser apresentadas como Canon;
4. ADRs devem declarar contexto, decisão, alternativas e consequências;
5. alterações estruturais devem incluir análise de impacto sobre dependências;
6. resultados observados que contrariem pressupostos devem originar revisão ou nova validação;
7. ausência de evidência deve ser declarada explicitamente;
8. rastreabilidade não elimina julgamento arquitetural, mas torna esse julgamento auditável.

## Classes de aplicação

| Tipo de mudança | Rastreabilidade exigida |
|---|---|
| Correção documental | referência ao documento alterado |
| Refinamento conceitual | justificativa e ativos relacionados |
| Mudança arquitetural | ADR e análise de dependências |
| Mudança estrutural | ADR, revisão arquitetural e impacto no baseline |

## Consequências positivas

- reduz decisões arbitrárias;
- melhora auditoria e continuidade institucional;
- permite revisão baseada em novas evidências;
- fortalece a separação entre Research e Architecture;
- prepara o GKR para representação futura em grafo;
- preserva memória decisória ao longo do tempo.

## Custos e limitações

- aumenta o esforço documental de decisões relevantes;
- exige disciplina na manutenção de links e metadados;
- não garante que uma decisão seja correta;
- pode gerar burocracia se aplicado sem proporcionalidade.

## Alternativas rejeitadas

### Registrar apenas a decisão final

Rejeitada porque elimina contexto, pressupostos e capacidade de revisão.

### Exigir evidência formal para qualquer alteração

Rejeitada porque criaria burocracia desproporcional para correções e mudanças operacionais simples.

### Tratar a Canon como verdade definitiva

Rejeitada porque impediria aprendizagem e revisão diante de novas evidências.

## Relação com o Baseline M1

Este ADR formaliza o princípio de governança adotado pelo `Baseline M1 — Research Foundation Complete`.

## Estado

Decisão aceita e aplicável a todas as arquiteturas e decisões estruturais registradas no GKR.
