---
id: GEM-003-REVENUE-FAMILY-CONTRACT-001
title: Contrato Canônico de Família de Receita
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-003
---

# Contrato Canônico de Família de Receita

## 1. Objetivo

Estabelecer a estrutura mínima para registrar famílias e mecanismos de receita de forma comparável, rastreável e subordinada aos guardrails da Guivos.

## 2. Natureza

O contrato é conceitual. Não é contrato comercial, especificação de API, modelo contábil, regra fiscal, tabela de preço ou autorização operacional.

## 3. Estrutura

```yaml
revenue_family_id: string
name: string
status:
  candidate |
  conceptually_admissible |
  validation_required |
  approved_for_test |
  suspended |
  rejected |
  retired

value_reference:
  flow_ids:
    - string
  value_object: string
  realized_value_condition: string
  evidence_required:
    - string

actors:
  payer: string
  primary_beneficiary: string
  economic_receivers:
    - string
  affected_parties:
    - string

revenue:
  mechanism: string
  candidate_charge_basis:
    - string
  recurring: boolean
  restricted_funds: boolean
  pass_through_possible: boolean
  price_defined: false

products:
  - string

economic_events:
  - entitlement
  - billing_eligibility
  - billing
  - payment
  - settlement
  - recognition_dependency
  - renewal
  - cancellation
  - refund
  - reversal
  - dispute
  - expiration

governance:
  disclosures:
    - string
  conflicts:
    - string
  data_involved:
    - string
  authority_limits:
    - string
  prohibited_behaviors:
    - string
  interruption_conditions:
    - string

validation:
  hypotheses:
    - string
  required_evidence:
    - string
  unresolved_dependencies:
    - string
  market_validation_status: not_started
  legal_validation_status: not_started
  fiscal_validation_status: not_started
  accounting_validation_status: not_started
```

## 4. Campos obrigatórios

Não poderão ser omitidos:

- referência ao fluxo de valor;
- pagador;
- beneficiário;
- recebedores;
- contraprestação;
- base de cobrança candidata;
- eventos econômicos;
- repasse ou recurso vinculado;
- disclosures;
- conflitos;
- dados envolvidos;
- interrupções;
- hipóteses e evidências;
- dependências não resolvidas.

## 5. Regras de status

### Candidate

Hipótese registrada, ainda sem avaliação suficiente.

### Conceptually admissible

Compatível com a arquitetura e guardrails em nível documental.

### Validation required

Depende de evidência empírica, operacional, jurídica, fiscal, contábil ou de mercado.

### Approved for test

Estado futuro que exigirá aprovação separada, protocolo, owner e limites de teste.

### Suspended

Interrompida por risco, conflito, falha, incidente ou ausência de evidência.

### Rejected

Incompatível com autoridade superior ou incapaz de satisfazer gates.

### Retired

Encerrada após uso ou substituição futura.

## 6. Condições de interrupção

- exploração de vulnerabilidade;
- influência comercial oculta;
- uso incompatível de dados;
- falha de entrega relevante;
- incapacidade de contestação;
- fraude material;
- destruição de valor;
- captura desproporcional;
- conflito não mitigado;
- ausência de disclosure;
- risco jurídico, fiscal ou contábil não tratado;
- concentração intolerável.

## 7. Rastreabilidade

Cada mecanismo futuro deverá apontar para:

- família RF correspondente;
- fluxo VF correspondente;
- produto relacionado;
- autoridade de Foundation e Business Architecture;
- gates aplicados;
- evidências;
- decisões posteriores.
