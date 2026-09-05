---
id: GKR-JOURNEY-SCREEN-GALLERY-OPPORTUNITY-BOOST-OPERATIONS-001
title: Opportunity Boost — Operação, Relatórios e Resíduos
status: superseded
version: 0.4.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-05
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
maturity: historical_provenance_only
---

# Opportunity Boost — Operação, Relatórios e Resíduos

> **F-016-A — desmaterialização física.** Os SVGs desta frente foram removidos do corpus vigente. Qualquer nome `.svg` remanescente neste documento é **proveniência histórica**, não arquivo disponível, não autoridade visual e não autorização de Design. O contrato funcional permanece governado pelo texto e pelas autoridades funcionais relacionadas.


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


### `uxa-046-campaign-active-desktop.svg`


### `uxa-046-campaign-paused-desktop.svg`


### `uxa-046-campaign-limited-desktop.svg`


### `uxa-046-campaign-material-change-desktop.svg`


### `uxa-046-campaign-closure-desktop.svg`


## 3. Gestão da campanha — móvel

**Cobertura:** 6 SVGs · ID: `GKR-SURF-COM-004` · origem: `UXA-053` · validação: `UXA-054`

### `uxa-053-campaign-scheduled-mobile.svg`


### `uxa-053-campaign-active-mobile.svg`


### `uxa-053-campaign-paused-mobile.svg`


### `uxa-053-campaign-limited-mobile.svg`


### `uxa-053-campaign-material-change-mobile.svg`


### `uxa-053-campaign-closure-mobile.svg`


## 4. Relatórios e reconciliação

**Cobertura:** 4 SVGs · ID: `GKR-SURF-COM-004` · origem: `UXA-048` · validação: `UXA-049`

### `uxa-048-aggregated-report-overview-desktop.svg`


### `uxa-048-aggregated-report-attribution-desktop.svg`


### `uxa-048-aggregated-report-overview-mobile.svg`


### `uxa-048-aggregated-report-reconciliation-mobile.svg`


## 5. Estados residuais validados

**Cobertura:** 10 SVGs · ID: `GKR-SURF-COM-005` · origem: `UXA-055` · validação: **UXA-099**

### `uxa-055-sponsored-technical-error-mobile.svg`


### `uxa-055-sponsored-inventory-unavailable-mobile.svg`


### `uxa-055-low-organic-supply-mobile.svg`


### `uxa-055-show-less-type-mobile.svg`


### `uxa-055-hide-campaign-mobile.svg`


### `uxa-055-report-content-mobile.svg`


### `uxa-055-disable-sponsored-opportunities-mobile.svg`


### `uxa-055-review-reverse-preferences-mobile.svg`


### `uxa-055-contest-data-use-mobile.svg`


### `uxa-055-advertiser-update-failure-mobile.svg`


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
