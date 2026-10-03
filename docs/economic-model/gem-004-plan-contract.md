---
id: GEM-004-PLAN-CONTRACT-001
title: Contrato Canônico de Plano
status: active
version: 0.2.0
owner: Guivos Economic Model
last_updated: 2026-07-28
parent: GEM-004
related:
  - GEM-004-A1
  - GEM-004-A2
  - GEM-010-A1
  - GEM-COMMERCIAL-BASELINE-001
  - M7.39
---

# Contrato Canônico de Plano

## 1. Objetivo

Estabelecer a estrutura mínima para registrar arquétipos e planos comerciais candidatos de forma comparável, rastreável e subordinada ao baseline gratuito e aos guardrails da Guivos.

## 2. Natureza

O contrato é documental. Não é configuração de software, contrato com cliente, termo de uso, regra fiscal, modelo contábil ou autorização de cobrança.

Quando um preço estiver preenchido, ele continuará candidato até aprovação de oferta pública.

## 3. Estrutura

```yaml
plan_id: string
plan_archetype_id: string
name: string
status:
  candidate |
  conceptually_defined |
  candidate_for_validation |
  approved_for_test |
  approved_for_offer |
  suspended |
  retired

audience:
  actor_type:
    person |
    collective |
    organization |
    funded_beneficiary
  eligibility:
    - string
  market: string

funding:
  source:
    free |
    self_paid |
    organization_funded |
    sponsor_funded |
    partner_funded |
    hybrid
  payer: string | null
  beneficiary: string

pricing:
  currency: string
  monthly_price: number | null
  annual_price: number | null
  annual_billing: prepaid | not_applicable | contracted
  starting_from: boolean
  quote_required: boolean
  taxes_defined: false
  transaction_fees_included: false
  commercial_status: candidate_for_validation

value:
  universal_baseline_preserved: true
  extension_dimensions:
    - depth
    - speed
    - convenience
    - personalization
    - capacity
    - automation
    - collaboration
    - support
    - intelligence
    - integration
    - management
    - combination

entitlements:
  included:
    - string
  excluded:
    - string
  periodic_limits:
    - resource: string
      quantity: number | null
      period: week | month | contract | none
      cumulative: false
  concurrent_limits:
    - resource: string
      quantity: number | null
  contracted_capacity:
    enabled: boolean
    dimensions:
      - string
  fair_use_applies: boolean
  prohibited_paywalls:
    - string

commercial_events:
  subscription_separate_from_transaction: true
  paid_publication_allowed: boolean
  transaction_commission_defined: false
  payment_fee_defined: false

lifecycle:
  activation: string
  trial: string | null
  renewal: string
  upgrade: string
  downgrade: string
  cancellation: string
  expiration: string
  grace_period: string | null

experience:
  allowed_offer_surfaces:
    - string
  prohibited_offer_moments:
    - string
  free_alternatives:
    - string
  limit_message: string

data_and_rights:
  data_access_after_downgrade: string
  export_available: true
  correction_available: true
  deletion_available: true
  appeal_available: true
  funder_access_limits:
    - string

governance:
  disclosures:
    - string
  conflicts:
    - string
  risks:
    - string
  interruption_conditions:
    - string

validation:
  value_hypothesis: string
  willingness_to_pay_status: not_started
  free_utility_status: not_started
  market_status: not_started
  operational_status: not_started
  financial_status: not_started
  legal_status: not_started
  fiscal_status: not_started
  accounting_status: not_started
  privacy_status: not_started
  security_status: not_started
```

## 4. Campos obrigatórios

Não poderão ser omitidos:

- identificador e arquétipo;
- público, elegibilidade e mercado;
- fonte de financiamento;
- pagador e beneficiário;
- moeda e preços candidatos;
- condição mensal, anual ou sob consulta;
- baseline gratuito;
- dimensões de ampliação;
- capacidades incluídas e excluídas;
- limites periódicos e simultâneos;
- capacidade contratada e uso justo;
- paywalls proibidos;
- separação entre assinatura e transação;
- ativação, renovação, downgrade e cancelamento;
- superfícies permitidas e momentos proibidos;
- alternativas gratuitas;
- tratamento de dados;
- acesso do financiador;
- disclosures;
- riscos e interrupções;
- hipóteses e dependências.

## 5. Regras de status

### Candidate

Hipótese registrada sem avaliação suficiente.

### Conceptually defined

Arquétipo compatível com o GEM-004 em nível documental.

### Candidate for validation

Plano possui nome, benefícios, limites e preço candidatos, mas não foi testado nem autorizado para oferta.

### Approved for test

Estado futuro que exigirá aprovação separada, protocolo, owner, população, limites e critérios de parada.

### Approved for offer

Estado futuro que exigirá validações de mercado, operação, finanças, jurídico, fiscal, contabilidade, privacidade, segurança e decisão competente.

### Suspended

Interrompido por risco, dano, conflito, falha, incidente ou evidência insuficiente.

### Retired

Encerrado ou substituído por decisão futura.

## 6. Condições de interrupção

- gratuito deixa de ser útil;
- oportunidade pública é ocultada para pressionar pagamento;
- direito básico é condicionado a pagamento;
- conversão utiliza vulnerabilidade;
- cancelamento é deliberadamente difícil;
- dado próprio é perdido indevidamente;
- acesso de Organização ou patrocinador é excessivo;
- trial é enganoso;
- renovação é obscura;
- entitlement possui erro material;
- benefício pago não é entregue;
- publicação existente perde visibilidade após limite;
- plano pago altera relevância orgânica;
- capacidade sem limite fixo é vendida sem dimensionamento;
- conflito ou risco permanece sem tratamento;
- dependência especializada não é atendida.

## 7. Rastreabilidade

Cada plano deverá apontar para:

- arquétipo AM correspondente;
- GEM-004-A1;
- GEM-004-A2;
- capacidades classificadas;
- famílias RF relacionadas;
- fluxos VF relacionados;
- baseline gratuito vigente;
- política de paywall;
- GEM-010-A1;
- gates aplicados;
- evidências;
- decisões e versões posteriores.

## 8. Regra de precedência

Quando houver conflito entre o plano e o baseline gratuito, direitos, guardrails ou autoridade superior, prevalecerá o limite mais protetivo.
