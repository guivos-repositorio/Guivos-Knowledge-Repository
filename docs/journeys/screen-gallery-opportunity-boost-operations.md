---
id: GKR-JOURNEY-SCREEN-GALLERY-OPPORTUNITY-BOOST-OPERATIONS-001
title: Opportunity Boost — Operação, Relatórios e Resíduos
status: active
version: 0.4.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
parent: GKR-JOURNEY-SCREEN-GALLERY-001
related:
  - UXA-081
  - UXA-082
  - UXA-083
  - UXA-084
  - UXA-085
  - UXA-099
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Opportunity Boost — Operação, Relatórios e Resíduos

[← Configuração e Exposição](screen-gallery-opportunity-boost-exposure.md) · [Índice](screen-gallery.md) · [Matriz por SVG](screen-gallery-traceability-matrix.md)

## 1. Ordem funcional de inspeção

```text
campanha configurada
→ gestão da campanha
→ relatório e reconciliação
→ estado residual, quando ocorrer
```

## 2. Gestão da campanha — computador

**Cobertura:** 6 SVGs · ID: `GKR-SURF-COM-004` · origem: `UXA-046` · validação: `UXA-047`

### `uxa-046-campaign-scheduled-desktop.svg`

![](../assets/wireframes/uxa-046-campaign-scheduled-desktop.svg){ width="320" loading="lazy" }

### `uxa-046-campaign-active-desktop.svg`

![](../assets/wireframes/uxa-046-campaign-active-desktop.svg){ width="320" loading="lazy" }

### `uxa-046-campaign-paused-desktop.svg`

![](../assets/wireframes/uxa-046-campaign-paused-desktop.svg){ width="320" loading="lazy" }

### `uxa-046-campaign-limited-desktop.svg`

![](../assets/wireframes/uxa-046-campaign-limited-desktop.svg){ width="320" loading="lazy" }

### `uxa-046-campaign-material-change-desktop.svg`

![](../assets/wireframes/uxa-046-campaign-material-change-desktop.svg){ width="320" loading="lazy" }

### `uxa-046-campaign-closure-desktop.svg`

![](../assets/wireframes/uxa-046-campaign-closure-desktop.svg){ width="320" loading="lazy" }

## 3. Gestão da campanha — móvel

**Cobertura:** 6 SVGs · ID: `GKR-SURF-COM-004` · origem: `UXA-053` · validação: `UXA-054`

### `uxa-053-campaign-scheduled-mobile.svg`

![](../assets/wireframes/uxa-053-campaign-scheduled-mobile.svg){ width="320" loading="lazy" }

### `uxa-053-campaign-active-mobile.svg`

![](../assets/wireframes/uxa-053-campaign-active-mobile.svg){ width="320" loading="lazy" }

### `uxa-053-campaign-paused-mobile.svg`

![](../assets/wireframes/uxa-053-campaign-paused-mobile.svg){ width="320" loading="lazy" }

### `uxa-053-campaign-limited-mobile.svg`

![](../assets/wireframes/uxa-053-campaign-limited-mobile.svg){ width="320" loading="lazy" }

### `uxa-053-campaign-material-change-mobile.svg`

![](../assets/wireframes/uxa-053-campaign-material-change-mobile.svg){ width="320" loading="lazy" }

### `uxa-053-campaign-closure-mobile.svg`

![](../assets/wireframes/uxa-053-campaign-closure-mobile.svg){ width="320" loading="lazy" }

## 4. Relatórios e reconciliação

**Cobertura:** 4 SVGs · ID: `GKR-SURF-COM-004` · origem: `UXA-048` · validação: `UXA-049`

### `uxa-048-aggregated-report-overview-desktop.svg`

![](../assets/wireframes/uxa-048-aggregated-report-overview-desktop.svg){ width="320" loading="lazy" }

### `uxa-048-aggregated-report-attribution-desktop.svg`

![](../assets/wireframes/uxa-048-aggregated-report-attribution-desktop.svg){ width="320" loading="lazy" }

### `uxa-048-aggregated-report-overview-mobile.svg`

![](../assets/wireframes/uxa-048-aggregated-report-overview-mobile.svg){ width="320" loading="lazy" }

### `uxa-048-aggregated-report-reconciliation-mobile.svg`

![](../assets/wireframes/uxa-048-aggregated-report-reconciliation-mobile.svg){ width="320" loading="lazy" }

## 5. Estados residuais validados

**Cobertura:** 10 SVGs · ID: `GKR-SURF-COM-005` · origem: `UXA-055` · validação: **UXA-099**

### `uxa-055-sponsored-technical-error-mobile.svg`

![](../assets/wireframes/uxa-055-sponsored-technical-error-mobile.svg){ width="320" loading="lazy" }

### `uxa-055-sponsored-inventory-unavailable-mobile.svg`

![](../assets/wireframes/uxa-055-sponsored-inventory-unavailable-mobile.svg){ width="320" loading="lazy" }

### `uxa-055-low-organic-supply-mobile.svg`

![](../assets/wireframes/uxa-055-low-organic-supply-mobile.svg){ width="320" loading="lazy" }

### `uxa-055-show-less-type-mobile.svg`

![](../assets/wireframes/uxa-055-show-less-type-mobile.svg){ width="320" loading="lazy" }

### `uxa-055-hide-campaign-mobile.svg`

![](../assets/wireframes/uxa-055-hide-campaign-mobile.svg){ width="320" loading="lazy" }

### `uxa-055-report-content-mobile.svg`

![](../assets/wireframes/uxa-055-report-content-mobile.svg){ width="320" loading="lazy" }

### `uxa-055-disable-sponsored-opportunities-mobile.svg`

![](../assets/wireframes/uxa-055-disable-sponsored-opportunities-mobile.svg){ width="320" loading="lazy" }

### `uxa-055-review-reverse-preferences-mobile.svg`

![](../assets/wireframes/uxa-055-review-reverse-preferences-mobile.svg){ width="320" loading="lazy" }

### `uxa-055-contest-data-use-mobile.svg`

![](../assets/wireframes/uxa-055-contest-data-use-mobile.svg){ width="320" loading="lazy" }

### `uxa-055-advertiser-update-failure-mobile.svg`

![](../assets/wireframes/uxa-055-advertiser-update-failure-mobile.svg){ width="320" loading="lazy" }

## 6. Resultado da UXA-099

- oito estados foram aprovados sem alteração visual;
- falha de atualização material foi reformulada para preservar a versão confirmada sem manter entrega futura ativa por inércia;
- revisão/reversão de preferências foi reformulada para explicitar data, superfície e escopo;
- repetição da mesma intenção é funcionalmente idempotente;
- erro técnico, zero inventário e baixa oferta permanecem estados distintos;
- denúncia, contestação e preferência permanecem fluxos distintos;
- a identidade da pessoa não é revelada ao anunciante.

## 7. Limite

Os dez estados possuem validação funcional específica pela UXA-099. Essa validação não promove automaticamente `TRN-305`, `TRN-304` ou `TRN-306`, não cria política jurídica final e não inicia implementação.

O status `active` registra o instrumento de inspeção; não promove jornadas nem Engenharia de Produto.

[← Configuração e Exposição](screen-gallery-opportunity-boost-exposure.md) · [Índice](screen-gallery.md) · [Matriz por SVG](screen-gallery-traceability-matrix.md)
