---
id: GEM-007-ECONOMIC-EVENT-OWNERSHIP-MAP-001
title: Mapa de Responsabilidade por Eventos Econômicos
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-007
---

# Mapa de Responsabilidade por Eventos Econômicos

## 1. Objetivo

Definir como produtos deverão registrar responsabilidade principal e contribuições em eventos econômicos compartilhados, sem implementar ledger, billing ou contabilidade.

## 2. Eventos candidatos

- descoberta;
- recomendação;
- acesso;
- lead consentido;
- proposta;
- entitlement;
- contratação;
- pedido;
- reserva;
- pagamento;
- settlement;
- entrega;
- utilização;
- evidência;
- reconhecimento;
- recompensa;
- cancelamento;
- reembolso;
- chargeback;
- disputa;
- renovação;
- expiração.

## 3. Campos mínimos

```yaml
economic_event_id: string
event_type: string
status: candidate
originating_product: string | null
primary_economic_owner: string
contributing_products:
  - string
fulfillment_owner: string | null
support_owner: string | null
refund_or_dispute_owner: string | null
partner_responsibility: string | null
payer: string | null
primary_beneficiary: string
receivers:
  - string
pass_through_expected: false
restricted_resource_expected: false
revenue_recognition_defined: false
cost_allocation_defined: false
evidence_required:
  - string
failure_treatment: string
```

## 4. Regras de ownership

- `primary_economic_owner` deverá ser único;
- origem poderá ser diferente da responsabilidade principal;
- produto de distribuição poderá ser diferente do produto de entrega;
- parceiro responsável não elimina deveres próprios da Guivos;
- recebimento financeiro não prova receita integral;
- responsabilidade por reembolso deverá ser compreensível antes de teste;
- ausência de owner bloqueia autorização futura;
- mudança de owner deverá manter trilha documental.

## 5. Mapa inicial

| Evento | Owner candidato predominante | Contribuições possíveis |
|---|---|---|
| contexto e próximo passo | Journey | Intelligence, Media, Business |
| pedido de produto | Mall | Journey, Ads, Intelligence, fornecedor |
| reserva turística | Travel | Journey, Mall, Ads, operador |
| solução organizacional | Business | Journey, Media, Intelligence, Mall, Travel, Ads |
| produção editorial | Media | Business, Ads, Intelligence, produtor |
| insight ou relatório | Intelligence | Business, Journey, produto consumidor |
| campanha publicitária | Ads | Media, produto anfitrião, Intelligence |
| recompensa resgatada em oferta | produto de resgate | Journey, Business, financiador, fornecedor |

## 6. Exemplos

### Compra originada no Journey

```text
Journey = originating_product
Mall = primary_economic_owner
fornecedor = fulfillment responsibility
Mall ou ator definido = refund_or_dispute_owner
```

### Conteúdo patrocinado

```text
Ads = economic lead da relação publicitária
Media = fulfillment owner do conteúdo
produto anfitrião = distribution surface e experiência
```

### Solução Business com Intelligence

```text
Business = primary economic owner da solução institucional
Intelligence = contributing product e owner da capacidade analítica
```

## 7. Limites

O mapa não define:

- eventos implementados;
- reconhecimento contábil;
- merchant of record;
- gateway;
- settlement;
- contratos;
- percentuais;
- rateio;
- operação.
