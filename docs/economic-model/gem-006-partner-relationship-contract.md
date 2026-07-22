---
id: GEM-006-PARTNER-RELATIONSHIP-CONTRACT-001
title: Contrato Canônico de Relacionamento de Parceiros
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-006
---

# Contrato Canônico de Relacionamento de Parceiros

## 1. Objetivo

Definir o registro conceitual mínimo de um relacionamento de parceiro, sem constituir contrato jurídico, cadastro operacional ou autorização de ativação.

## 2. Contrato

```yaml
partner_relationship_id: string
partner_id: string
name: string

status:
  candidate |
  under_assessment |
  conditionally_approved |
  approved |
  activating |
  active_limited |
  active |
  under_review |
  suspended |
  exiting |
  terminated |
  archived

classification:
  partner_categories:
    - string
  relationship_archetypes:
    - string
  risk_class: not_assessed

scope:
  products:
    - string
  territories:
    - string
  audiences:
    - string
  permitted_roles:
    - string
  prohibited_roles:
    - string

value_exchange:
  partner_contributions:
    - string
  guivos_contributions:
    - string
  participant_benefits:
    - string
  evidence:
    - string

economics:
  revenue_families:
    - string
  remuneration_mechanisms:
    - string
  price_defined: false
  commission_defined: false
  settlement_defined: false
  restricted_funds: false
  reward_funding: false

responsibilities:
  delivery_owner: null
  support_owner: null
  refund_owner: null
  dispute_owner: null
  evidence_owner: null
  incident_owner: null

quality:
  requirements:
    - string
  evidence:
    - string
  thresholds_defined: false

data:
  purposes:
    - string
  permitted_access:
    - string
  prohibited_access:
    - string
  retention_defined: false

governance:
  disclosures:
    - string
  conflicts:
    - string
  fraud_risks:
    - string
  concentration_risks:
    - string
  interruption_conditions:
    - string

lifecycle:
  activation_requirements:
    - string
  review_conditions:
    - string
  suspension_treatment: string
  exit_treatment: string
  continuity_treatment: string

validation:
  commercial_status: not_started
  operational_status: not_started
  legal_status: not_started
  fiscal_status: not_started
  accounting_status: not_started
  privacy_status: not_started
  security_status: not_started
```

## 3. Regras

- cada relacionamento possui escopo próprio;
- múltiplos papéis exigem permissões separadas;
- preço, comissão e settlement permanecem indefinidos;
- responsabilidade não poderá ficar implícita;
- acesso a dados depende de finalidade;
- qualidade exige evidência;
- ativação depende de gates;
- saída preserva obrigações.

## 4. Status

`approved` significa elegibilidade conceitual para futura ativação, não operação autorizada.

`active` é estado reservado a operação futura e não é alcançado neste ciclo.

## 5. Natureza

Este contrato não é:

- contrato jurídico;
- cadastro de CRM;
- configuração de software;
- API;
- tabela comercial;
- termo de parceria;
- DPA;
- autorização de cobrança;
- autorização de acesso a dados.

## 6. Fora do escopo

- preenchimento com parceiro real;
- assinatura;
- integração;
- implementação;
- ativação.
