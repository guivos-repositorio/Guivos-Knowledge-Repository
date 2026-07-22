---
id: GEM-007-PRODUCT-ECONOMIC-ROLE-CONTRACT-001
title: Contrato Canônico de Papel Econômico do Produto
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-007
---

# Contrato Canônico de Papel Econômico do Produto

## 1. Objetivo

Definir a estrutura documental mínima para registrar o papel econômico de cada produto sem criar configuração técnica, centro de resultado, P&L, regra contábil ou autorização comercial.

## 2. Contrato

```yaml
product_economic_role_id: string
product_id: string
name: string

status:
  candidate |
  conceptually_defined |
  validation_required |
  approved_for_test |
  suspended |
  retired

functional_authority:
  source_documents:
    - string
  preserved_boundaries:
    - string

economic_role:
  primary_role: string
  secondary_roles:
    - string
  participation_states:
    - primary_value_owner
    - economic_lead
    - demand_originator
    - distribution_surface
    - fulfillment_owner
    - revenue_family_owner_candidate
    - contributing_product
    - shared_capability_provider
    - evidence_provider
    - support_owner
    - refund_or_dispute_owner
    - cost_bearer_candidate
    - beneficiary_product

value:
  primary_value_flow: string
  supporting_value_flows:
    - string
  actors:
    - string
  primary_beneficiary: string
  potential_payers:
    - string

revenue:
  primary_candidate_families:
    - string
  shared_candidate_families:
    - string
  price_defined: false
  allocation_defined: false
  revenue_recognition_defined: false

partners:
  predominant_categories:
    - string
  relationship_dependencies:
    - string

economic_events:
  owned_candidates:
    - string
  contributed_events:
    - string
  fulfillment_responsibility: not_defined
  support_responsibility: not_defined
  refund_or_dispute_responsibility: not_defined

costs:
  direct_categories:
    - string
  shared_categories:
    - string
  allocation_defined: false

data_and_authority:
  required_data:
    - string
  prohibited_access:
    - string
  human_authority_preserved: true

governance:
  conflicts:
    - string
  concentration_risks:
    - string
  guardrails:
    - string
  interruption_conditions:
    - string

validation:
  value_status: not_started
  market_status: not_started
  commercial_status: not_started
  operational_status: not_started
  accounting_status: not_started
  legal_status: not_started
  privacy_status: not_started
  security_status: not_started
```

## 3. Regras de preenchimento

- `primary_role` deverá ser único por versão do contrato;
- famílias compartilhadas não poderão ser contabilizadas integralmente em vários produtos;
- o pagador não poderá receber autoridade indevida;
- `owned_candidates` descreve eventos candidatos, não eventos implementados;
- responsabilidades `not_defined` bloqueiam teste e operação;
- custos compartilhados deverão permanecer visíveis mesmo sem rateio;
- dados proibidos prevalecem sobre conveniência comercial;
- `approved_for_test` exigirá ciclo separado.

## 4. Evidências futuras

O contrato poderá referenciar futuramente:

- pesquisa de valor;
- teste de oferta;
- comportamento observado;
- custos reais;
- qualidade;
- capacidade operacional;
- privacidade;
- segurança;
- tratamento jurídico, fiscal e contábil.

Nenhuma dessas evidências é criada pelo GEM-007.

## 5. Não constitui

- configuração de produto;
- API;
- banco de dados;
- P&L;
- plano de contas;
- centro de resultado;
- centro de custo;
- contrato jurídico;
- tabela comercial;
- regra de billing;
- autorização de faturamento;
- autorização de teste ou produção.
