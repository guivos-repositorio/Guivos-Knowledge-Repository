---
id: GKR-ORG-OPPORTUNITY-BOOST-ENTITLEMENT-001
title: Organização — Entitlement de Opportunity Boost — Reconciliação Canônica
status: active
version: 1.0.0
owner: Guivos Economic Model
last_updated: 2026-10-03
normative: true
maturity: entitlement_mapping_reconciled
depends_on:
  - GKR-PLANS-ORGANIZATION-001
  - GEM-007-A1
  - GPA-007
related:
  - GEM-010-A2
  - GKR-UX-G5-OPPORTUNITY-BOOST-VALIDATION-001
---

# Organização — Entitlement de Opportunity Boost — Reconciliação Canônica

## 1. Finalidade

Reconciliar o entitlement de Opportunity Boost para os planos atuais de Organização sem inventar benefício de plano, verba de mídia, desconto, checkout ou cobrança operacional.

Este ato fecha `SP-GAP-010` no limite documental vigente.

## 2. Regra central

```text
CONecta
ELEVA
TRANSFORMA
→ DO NOT GRANT OPPORTUNITY BOOST ENTITLEMENT BY PLAN ALONE

OPPORTUNITY BOOST
→ SEPARATE ADS PURCHASE / AUTHORITY

PLAN PRESENCE
≠ BILLING AUTHORIZATION
≠ MEDIA BUDGET
≠ DISCOUNT
≠ GUARANTEED INVENTORY
```

## 3. Mapeamento corrente

| Plano de Organização | Entitlement automático de Boost | Verba de Boost incluída | Regra corrente |
|---|---|---|---|
| Conecta | não | não | pode contratar somente por autoridade Ads/econômica própria e elegibilidade aplicável |
| Eleva | não | não | pode contratar somente por autoridade Ads/econômica própria e elegibilidade aplicável |
| Transforma | não por padrão | não por padrão | contrato específico pode conceder capacidade própria, mas isso deve estar expresso; o nome do plano não basta |

## 4. Compra separada

O Opportunity Boost permanece compra separada do plano de Organização.

```text
ORGANIZATION PLAN
+
OPPORTUNITY BOOST
→ DISTINCT ECONOMIC OBJECTS
```

A assinatura institucional não inclui verba de Boost por padrão.

## 5. Elegibilidade

Entitlement econômico e elegibilidade publicitária são dimensões distintas.

Para contratar/operar Boost, quando a operação existir, continuam necessários:

- oportunidade/atividade/programa elegível e ativo;
- autoridade institucional aplicável;
- elegibilidade publicitária;
- inventário patrocinado permitido;
- orçamento autorizado;
- políticas e proteções aplicáveis.

```text
ENTITLEMENT
≠ AD ELIGIBILITY

PAYMENT CAPACITY
≠ AD ELIGIBILITY
```

## 6. Contrato específico

Uma contratação institucional específica pode futuramente incluir capacidade relacionada a Opportunity Boost somente quando:

- estiver explicitamente prevista;
- possuir escopo e limites definidos;
- preservar separação entre assinatura e orçamento de mídia;
- não comprar relevância orgânica;
- não transferir autoridade do Ads ou da superfície anfitriã.

Não se presume essa capacidade por `Transforma`, por preço, por escala ou por semelhança com qualquer plano Business.

## 7. Pricing e cobrança

Este ato não converte os parâmetros candidatos de `GEM-010-A2` em oferta pública ou cobrança autorizada.

```text
GEM-010-A2
→ CANDIDATE PARAMETERS

PUBLIC OFFER
→ NOT AUTHORIZED

BILLING
→ NOT AUTHORIZED
```

## 8. Não inferências

```text
CONecta
≠ BOOST INCLUDED

ELEVA
≠ BOOST INCLUDED

TRANSFORMA
≠ BOOST INCLUDED BY DEFAULT

BUSINESS TIER
≠ ORGANIZATION BOOST ENTITLEMENT

BOOST ENTITLEMENT
≠ ORGANIC PRIORITY
≠ GUARANTEED DELIVERY
≠ GUARANTEED RESULT
```

## 9. Estado de SP-GAP-010

```text
SP-GAP-010
→ CURRENT PLAN ENTITLEMENT MAPPING RECONCILED

AUTOMATIC PLAN ENTITLEMENT
→ NONE

SEPARATE ADS PURCHASE
→ REQUIRED UNLESS EXPLICIT CONTRACTUAL AUTHORITY EXISTS

PRICING / BILLING / OPERATION
→ STILL NOT RELEASED
```

## 10. Estado

```text
ORGANIZATION OPPORTUNITY BOOST ENTITLEMENT
→ RECONCILED

PRODUCT ENGINEERING
→ NOT RELEASED
```
