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

A sincronização de 2026-08-08 preserva os nove arquivos, os perfis `R29/R30/R31`, superfícies, transições e validações existentes. Somente os seis SVGs de Coletivo/Organização tiveram nomenclatura e cópia alinhadas à taxonomia global vigente. Os três SVGs de Pessoa permanecem sem alteração porque `Free · Plus · Pro` já estava consistente.

Taxonomia visual vigente:

- Pessoa: `Free · Plus · Pro`;
- Coletivo: `Livre · Mobiliza · Impacta · Rede`;
- Organização: `Conecta · Eleva · Transforma`.

Guivos Business (`Start · Growth · Scale · Enterprise`) não recebe SVG ou perfil nesta galeria porque é produto especializado, não quarto participante da UXA-100.

## 2. Pessoa — perfil R29

Superfícies: `PER-301` a `PER-304`.

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

Superfícies: `COL-301` a `COL-304`.

A leitura dos planos é `Livre · Mobiliza · Impacta · Rede`. Mobiliza, Impacta e Rede expressam função/capacidade operacional e não constituem escala de mérito ou evolução do Coletivo.

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

Superfícies: `ORG-301` a `ORG-304`.

A leitura dos planos é `Conecta · Eleva · Transforma`. Esses planos pertencem à jornada institucional da Organização e são estruturalmente separados do produto Guivos Business.

> **Organização Transforma ≠ Guivos Business Enterprise.**

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
├── mudança autonomamente configurável → *-302 revisão → *-304 resultado/recuperação → *-301
├── downgrade/cancelamento → *-303 gestão do ciclo → *-304 → *-301
└── quando configuração exigir processo assistido → BND-002
```

`BND-002` significa **contratação/dimensionamento assistido** e não Enterprise, Scale, Rede ou Transforma.

A comparação incremental permanece estado de `*-301`. Processamento de pagamento permanece transitório. Sucesso e falha pertencem a `*-304` com consequências distintas.

## 6. Contagem canônica da frente

| Participante | Tela Planos | Board de fluxo | Comparação incremental | Total canônico | Perfil |
|---|---:|---:|---:|---:|---|
| Pessoa | 1 | 1 | 1 | 3 | R29 |
| Coletivo | 1 | 1 | 1 | 3 | R30 |
| Organização | 1 | 1 | 1 | 3 | R31 |
| **Total** | **3** | **3** | **3** | **9** | **3 perfis** |

A galeria global permanece com **118 SVGs canônicos**, todos com validação funcional documental vigente no escopo já governado. Nenhum SVG é adicionado ou removido pela sincronização taxonômica.

## 7. Maturidade das transições

- `TRN-401` a `405`: localmente validadas;
- `TRN-411` a `415`: localmente validadas;
- `TRN-416`: parcial; processo posterior a `BND-002` não materializado;
- `TRN-421` a `425`: localmente validadas;
- `TRN-426`: parcial pela mesma razão.

A correção semântica não promove nenhuma transição.

## 8. Proteções

- plano pago não compra relevância, confiança, legitimidade, impacto ou evolução;
- oportunidade pública não é escondida para vender plano;
- benefícios herdados não aparecem como novidades;
- contratação assistida não simula checkout autônomo;
- falha de pagamento não presume ativação;
- data de início e recorrência aparecem antes da confirmação;
- downgrade/cancelamento explicitam consequências e excedentes;
- assinatura permanece separada de transação, comissão, taxa e tributo;
- Organização permanece separada de Guivos Business;
- validação funcional e promoção documental não equivalem a implementação.
