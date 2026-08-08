---
id: GKR-JOURNEY-SCREEN-GALLERY-PLANS-001
title: Planos, Comparação e Cobrança — Galeria Canônica
status: active
version: 0.4.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-08
related:
  - UXA-100
  - UXA-100-A1
  - UXA-100-A2
  - UXA-100-A3
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Planos, Comparação e Cobrança — Galeria Canônica

## 1. Finalidade

Esta galeria reúne as nove referências visuais de Planos da UXA-100 para **Pessoa, Coletivo e Organização**.

A UXA-100-A2 aprovou funcionalmente os nove ativos. A UXA-100-A3 os promoveu ao conjunto canônico e esta versão sincroniza a nomenclatura e a leitura conceitual sem criar novos ativos, superfícies, transições ou perfis.

Taxonomia vigente:

| Contexto | Planos |
|---|---|
| Pessoa | Free · Plus · Pro |
| Coletivo | Livre · Mobiliza · Impacta · Rede |
| Organização | Conecta · Eleva · Transforma |
| Guivos Business | Start · Growth · Scale · Enterprise — produto separado, sem SVG próprio nesta galeria |

## 2. Pessoa — perfil R29

Superfícies canônicas relacionadas: `PER-301` a `PER-304`.

### 2.1 Tela dedicada de Planos

![Pessoa — tela dedicada de Planos](../assets/wireframes/uxa-100-person-plans-screen-mobile.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-person-plans-screen-mobile.svg)

### 2.2 Fluxo de plano, cobrança e pagamento

![Pessoa — fluxo de planos e pagamentos](../assets/wireframes/uxa-100-person-plans-payments-flow-board.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-person-plans-payments-flow-board.svg)

### 2.3 Comparação incremental

![Pessoa — comparação incremental](../assets/wireframes/uxa-100-person-plan-incremental-benefits-comparison.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-person-plan-incremental-benefits-comparison.svg)

## 3. Coletivo — perfil R30

Superfícies canônicas relacionadas: `COL-301` a `COL-304`.

Taxonomia sincronizada: **Livre · Mobiliza · Impacta · Rede**.

### 3.1 Tela dedicada de Planos

![Coletivo — tela dedicada de Planos](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

### 3.2 Fluxo de plano, cobrança e pagamento

![Coletivo — fluxo de planos e pagamentos](../assets/wireframes/uxa-100-collective-plans-payments-flow-board.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-collective-plans-payments-flow-board.svg)

### 3.3 Comparação incremental

![Coletivo — comparação incremental](../assets/wireframes/uxa-100-collective-plan-incremental-benefits-comparison.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-collective-plan-incremental-benefits-comparison.svg)

## 4. Organização — perfil R31

Superfícies canônicas relacionadas: `ORG-301` a `ORG-304`.

Taxonomia sincronizada: **Conecta · Eleva · Transforma**.

A separação obrigatória é **Organização ≠ Guivos Business** e **Organização Transforma ≠ Guivos Business Enterprise**.

### 4.1 Tela dedicada de Planos

![Organização — tela dedicada de Planos](../assets/wireframes/uxa-100-organization-plans-screen-desktop.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-organization-plans-screen-desktop.svg)

### 4.2 Fluxo de plano, cobrança e pagamento

![Organização — fluxo de planos e pagamentos](../assets/wireframes/uxa-100-organization-plans-payments-flow-board.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-organization-plans-payments-flow-board.svg)

### 4.3 Comparação incremental

![Organização — comparação incremental](../assets/wireframes/uxa-100-organization-plan-incremental-benefits-comparison.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-organization-plan-incremental-benefits-comparison.svg)

## 5. Fragmentação canônica

```text
*-301 Planos e comparação
├── contratação autônoma → *-302 revisão → *-304 resultado/recuperação → *-301
├── downgrade/cancelamento → *-303 gestão do ciclo → *-304 → *-301
└── quando necessário → BND-002 contratação/dimensionamento assistido
```

A comparação incremental permanece estado de `*-301`. O processamento de pagamento permanece transitório e não recebe superfície própria. Sucesso e falha são estados distintos de `*-304` porque compartilham a mesma responsabilidade de resultado/recuperação sem compartilhar a consequência.

`BND-002` não representa Enterprise ou Scale; representa a necessidade de contratação/dimensionamento assistido quando o autoatendimento não é suficiente.

## 6. Contagem canônica da frente

| Participante | Tela Planos | Board de fluxo | Comparação incremental | Total canônico | Perfil |
|---|---:|---:|---:|---:|---|
| Pessoa | 1 | 1 | 1 | 3 | R29 |
| Coletivo | 1 | 1 | 1 | 3 | R30 |
| Organização | 1 | 1 | 1 | 3 | R31 |
| **Total** | **3** | **3** | **3** | **9** | **3 perfis** |

A galeria global permanece em **118 SVGs canônicos**, todos com a maturidade documental já governada. Nenhum SVG ou perfil é criado para Guivos Business nesta frente.

## 7. Maturidade das transições

- `TRN-401` a `405`: localmente validadas;
- `TRN-411` a `415`: localmente validadas;
- `TRN-416`: parcial, pois o processo após `BND-002` não foi materializado;
- `TRN-421` a `425`: localmente validadas;
- `TRN-426`: parcial, pela mesma fronteira de contratação/dimensionamento assistido.

Nenhuma transição de Planos é apresentada como implementação técnica ou cobrança real.

## 8. Proteções

- plano pago não compra relevância, confiança, legitimidade, mérito, impacto ou evolução;
- oportunidade pública não é escondida para vender plano;
- benefícios herdados não aparecem como novidades;
- `BND-002` não simula checkout autônomo definitivo;
- Organização e Guivos Business não são tratados como sinônimos;
- falha de pagamento não presume ativação;
- data de início e recorrência aparecem antes da confirmação;
- downgrade/cancelamento exibem consequências e tratam capacidades excedentes antes da efetivação;
- assinatura permanece separada de transação, comissão, taxa de pagamento e tributo;
- validação funcional e promoção documental não equivalem a implementação.