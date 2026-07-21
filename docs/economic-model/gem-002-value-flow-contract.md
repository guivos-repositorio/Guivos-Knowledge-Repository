---
id: GEM-002-VALUE-FLOW-CONTRACT-001
title: Contrato Canônico de Fluxo de Valor
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-20
parent: GEM-002
---

# Contrato Canônico de Fluxo de Valor

## 1. Objetivo

Estabelecer a estrutura mínima para registrar fluxos econômicos de forma rastreável, comparável e subordinada aos guardrails da Guivos.

## 2. Escopo

O contrato é conceitual. Não é API, contrato comercial, modelo contábil, tabela de preço ou autorização de operação.

## 3. Estrutura

```yaml
flow_id: string
name: string
status: candidate | under_validation | approved | suspended | retired

trigger:
  need_or_potential: string
  initiating_actor: string

actors:
  source: string
  intermediaries:
    - string
  beneficiary: string
  possible_payer: string | null
  possible_receiver: string | null

value:
  source_id: string
  object_id: string
  proposition: string
  expected_benefit: string
  dimensions:
    - transformation
    - economic
    - social
    - relational
    - intellectual
    - experience
    - organizational
    - network

delivery:
  product_or_channel: string
  conditions:
    - string
  realization_event: string
  evidence:
    - string

contributions:
  - actor: string
    contribution: string
    cost_or_risk: string

economic_boundaries:
  possible_capture_point: string | null
  possible_sharing:
    - string
  possible_reinvestment:
    - string
  pricing_defined: false

governance:
  data_involved:
    - string
  authority_limits:
    - string
  conflicts:
    - string
  guardrails:
    - string
  externalities:
    - string
  interruption_conditions:
    - string

lifecycle:
  starts_when: string
  completes_when: string
  fails_when: string
  contestation: string
  correction: string
  retirement: string
```

## 4. Regras de preenchimento

1. todo fluxo deve possuir beneficiário identificável;
2. pagador e beneficiário podem ser atores diferentes;
3. intermediário não recebe autoridade por participar da entrega;
4. ponto de captura candidato não constitui receita aprovada;
5. contribuição deverá registrar custo ou risco relevante;
6. evidência deverá ser proporcional ao resultado alegado;
7. dados e finalidade deverão ser explícitos;
8. conflitos e externalidades não poderão ser omitidos;
9. falha, contestação e correção deverão ser previstas;
10. `pricing_defined` permanecerá `false` durante o GEM-002.

## 5. Estados de governança

- `candidate`: hipótese registrada;
- `under_validation`: análise pelos gates em andamento;
- `approved`: fluxo conceitualmente admissível para blocos posteriores;
- `suspended`: risco, conflito ou evidência insuficiente;
- `retired`: fluxo substituído ou incompatível.

A aprovação conceitual não autoriza lançamento, contrato ou implementação.

## 6. Critérios de validade

Um registro é válido quando:

- usa IDs canônicos;
- distingue proposta, entrega e realização;
- registra todos os atores materiais;
- identifica custos e riscos;
- não presume monetização;
- preserva autonomia e autoridade;
- inclui caminho de falha e contestação;
- possui rastreabilidade às fontes e objetos de valor.
