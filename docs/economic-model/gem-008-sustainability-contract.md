---
id: GEM-008-SUSTAINABILITY-CONTRACT-001
title: Contrato Canônico de Sustentabilidade
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-22
parent: GEM-008
---

# Contrato Canônico de Sustentabilidade

## 1. Objetivo

Definir o conjunto mínimo de campos para descrever sustentabilidade de um ecossistema, produto, fluxo, programa, capacidade compartilhada ou relacionamento, sem constituir orçamento, demonstração financeira ou configuração técnica.

## 2. Contrato

```yaml
sustainability_scope_id: string
scope_type:
  ecosystem |
  product |
  value_flow |
  program |
  shared_capability |
  partner_relationship

status:
  not_assessed |
  conceptually_supported |
  evidence_required |
  capacity_constrained |
  economically_fragile |
  dependency_exposed |
  remediation_required |
  at_risk |
  unsustainable |
  blocked

value:
  primary_value: string
  beneficiaries:
    - string
  universal_free_impact: string
  essential_value_dependency: boolean

costs:
  direct_categories:
    - string
  structural_categories:
    - string
  shared_categories:
    - string
  risk_categories:
    - string
  externalities:
    - string
  amounts_defined: false
  allocation_defined: false

funding:
  candidate_sources:
    - string
  restricted_sources:
    - string
  recurring_source_validated: false
  concentration_assessed: false

obligations:
  protected_obligations:
    - string
  coverage_validated: false

capacity:
  critical_capabilities:
    - string
  current_status: not_assessed
  saturation_threshold_defined: false

reserves:
  required_classes:
    - string
  targets_defined: false
  funded_status: not_assessed

subsidies:
  source: string | null
  destination: string | null
  purpose: string | null
  amount_defined: false
  review_defined: false

reinvestment:
  candidate_destinations:
    - string
  priority_defined: false
  allocation_authorized: false

resilience:
  concentration_risks:
    - string
  substitution_defined: false
  continuity_defined: false
  exit_defined: false

governance:
  owner: string | null
  evidence:
    - string
  review_conditions:
    - string
  interruption_conditions:
    - string

validation:
  value_status: not_started
  cost_status: not_started
  capacity_status: not_started
  financial_status: not_started
  operational_status: not_started
  legal_status: not_started
  fiscal_status: not_started
  accounting_status: not_started
  privacy_status: not_started
  security_status: not_started
```

## 3. Regras

- campos `false`, `not_assessed`, `not_started` ou `null` não poderão ser interpretados como aprovados;
- ausência de owner, cobertura ou continuidade bloqueará afirmação de prontidão;
- valores, alocações e targets deverão permanecer indefinidos;
- fontes restritas deverão ser explicitadas;
- externalidades e obrigações deverão permanecer visíveis;
- o contrato poderá apoiar documentação futura, mas não substitui validação especializada.

## 4. Não constitui

- orçamento;
- demonstração financeira;
- plano de contas;
- política contábil;
- fluxo de caixa;
- reserva constituída;
- autorização de gasto;
- P&L;
- unit economics;
- projeção;
- API, banco de dados ou configuração técnica;
- autorização de teste, operação ou produção.