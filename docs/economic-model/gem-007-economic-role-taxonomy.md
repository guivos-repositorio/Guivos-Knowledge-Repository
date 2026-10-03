---
id: GEM-007-ECONOMIC-ROLE-TAXONOMY-001
title: Taxonomia de Papéis Econômicos dos Produtos
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-007
---

# Taxonomia de Papéis Econômicos dos Produtos

## 1. Objetivo

Classificar como um produto poderá participar de um fluxo econômico sem confundir responsabilidade funcional, liderança comercial, distribuição, entrega, evidência, suporte ou atribuição.

## 2. Estados de participação

### `primary_value_owner`

Responsável principal pela proposta de valor do fluxo. Não representa propriedade societária nem reconhecimento contábil.

### `economic_lead`

Coordena a relação econômica ou comercial futura, preservando as autoridades dos produtos componentes.

### `demand_originator`

Origina descoberta, interesse ou demanda. Origem não implica propriedade da transação.

### `distribution_surface`

Apresenta conteúdo, oferta, campanha ou oportunidade. Superfície não implica responsabilidade comercial integral.

### `fulfillment_owner`

Responde pela entrega especializada do valor ou coordena o responsável externo.

### `revenue_family_owner_candidate`

Principal candidato conceitual a determinada família de receita. Não autoriza faturamento ou reconhecimento.

### `contributing_product`

Fornece capacidade complementar a um fluxo liderado por outro produto.

### `shared_capability_provider`

Disponibiliza capacidade transversal utilizada por vários produtos.

### `evidence_provider`

Produz ou mantém evidência sobre entrega, utilização, resultado ou falha.

### `support_owner`

Responde pelo atendimento relacionado ao evento ou coordena seu encaminhamento.

### `refund_or_dispute_owner`

Responde pelo tratamento econômico de cancelamento, reembolso, chargeback ou disputa.

### `cost_bearer_candidate`

Origina ou absorve categoria de custo futura. Não define rateio ou contabilização.

### `beneficiary_product`

Recebe benefício econômico indireto sem ser o responsável principal pelo evento.

### `not_assessed`

Participação ainda não avaliada.

## 3. Dimensões obrigatórias

Cada classificação deverá registrar:

- produto;
- fluxo de valor;
- evento econômico;
- ator atendido;
- valor principal;
- responsabilidade funcional;
- produtos contribuintes;
- parceiro relacionado;
- família de receita candidata;
- custos;
- dados;
- riscos;
- evidência;
- condição de interrupção.

## 4. Regra de composição

Um produto poderá acumular estados compatíveis no mesmo fluxo, mas deverá haver separação explícita entre:

```text
valor principal
≠ liderança econômica
≠ origem de demanda
≠ distribuição
≠ entrega
≠ evidência
≠ suporte
≠ atribuição
```

## 5. Incompatibilidades condicionadas

Exigem controle adicional:

- produto que recomenda e recebe maior remuneração por uma opção;
- produto que produz evidência e recebe por resultado;
- produto que distribui publicidade e define ranking orgânico;
- produto que vende solução e controla dados individuais;
- produto que origina demanda e reivindica toda a receita;
- produto que fornece capacidade compartilhada e bloqueia saída;
- produto que coordena contrato e oculta responsáveis de entrega.

## 6. Estado de classificação

Valores permitidos:

- `candidate`;
- `conceptually_defined`;
- `validation_required`;
- `approved_for_test`;
- `suspended`;
- `retired`.

Nenhum papel do GEM-007 supera `conceptually_defined`.

## 7. Limites

A taxonomia não define:

- preços;
- centros de resultado;
- reconhecimento de receita;
- rateio;
- transfer pricing;
- permissões técnicas;
- equipes;
- ativação comercial.
