---
id: GEM-004-PLAN-CONTRACT-001
title: Contrato Canônico de Plano
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-004
---

# Contrato Canônico de Plano

## 1. Objetivo

Estabelecer a estrutura mínima para registrar arquétipos e planos futuros de forma comparável, rastreável e subordinada ao baseline gratuito e aos guardrails da Guivos.

## 2. Natureza

O contrato é conceitual. Não é configuração de software, contrato comercial, termo de uso, tabela de preço, regra fiscal, modelo contábil ou autorização de cobrança.

## 3. Estrutura

```yaml
plan_archetype_id: string
name: string
status:
  candidate |
  conceptually_defined |
  validation_required |
  approved_for_test |
  suspended |
  retired

audience:
  actor_type: string
  eligibility:
    - string

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
  price_defined: false

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
  limits:
    - string
  prohibited_paywalls:
    - string

lifecycle:
  activation: string
  trial: string | null
  renewal: string
  upgrade: string
  downgrade: string
  cancellation: string
  expiration: string
  grace_period: string | null

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
  market_status: not_started
  operational_status: not_started
  legal_status: not_started
  fiscal_status: not_started
  accounting_status: not_started
```

## 4. Campos obrigatórios

Não poderão ser omitidos:

- público e elegibilidade;
- fonte de financiamento;
- pagador e beneficiário;
- baseline gratuito;
- dimensões de ampliação;
- capacidades incluídas e excluídas;
- limites;
- paywalls proibidos;
- ativação, renovação, downgrade e cancelamento;
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

### Validation required

Depende de evidência de valor, comportamento, pagamento, operação ou análise especializada.

### Approved for test

Estado futuro que exigirá aprovação separada, protocolo, owner, limites e critérios de parada.

### Suspended

Interrompido por risco, dano, conflito, falha, incidente ou evidência insuficiente.

### Retired

Encerrado ou substituído por decisão futura.

## 6. Condições de interrupção

- gratuito deixa de ser útil;
- direito básico condicionado a pagamento;
- conversão por vulnerabilidade;
- cancelamento deliberadamente difícil;
- perda indevida de dados;
- acesso excessivo de organização ou patrocinador;
- trial enganoso;
- renovação obscura;
- erro material de entitlement;
- benefício pago não entregue;
- conflito ou risco sem tratamento;
- dependência especializada não atendida.

## 7. Rastreabilidade

Cada plano futuro deverá apontar para:

- arquétipo AM correspondente;
- capacidades classificadas;
- famílias RF relacionadas;
- fluxos VF relacionados;
- baseline gratuito vigente;
- política de paywall;
- gates aplicados;
- evidências;
- decisões e versões posteriores.

## 8. Regra de precedência

Quando houver conflito entre campos do plano e o baseline gratuito, direitos, guardrails ou autoridade superior, prevalece o limite mais protetivo.
