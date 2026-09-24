---
id: GKR-UX-HOMES-DESIGN-DELIVERY-001
title: Homes Públicas — Manifesto Canônico de Entrega para Design
status: active
version: 7.0.43
owner: Experience Architecture
last_updated: 2026-09-21
normative: true
maturity: current_canonical_design_source_manifest
depends_on:
  - GKR-STATE-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
related:
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
---

# Homes Públicas — Manifesto Canônico de Entrega para Design

## 1. Finalidade

Este Manifesto define **o conjunto corrente de fontes que pode ser consumido por designer humana e, opcionalmente, por sistemas de IA** para criação e prototipação das oito Homes públicas.

```text
CANONICAL CHECKPOINT
→ CURRENT MAIN
→ RESOLVED AT CONSUMPTION TIME

SOURCE OF TRUTH
→ CURRENT MAIN

SNAPSHOT REQUIREMENT
→ NONE

HISTORICAL / CANDIDATE / CHECKPOINT / AUDIT
→ EXCLUDED FROM DESIGN AND AI INPUT

DESIGNER
→ CREATIVE AUTHOR

AI
→ OPTIONAL / DESIGNER-CONTROLLED
```

Snapshots, candidates e registros de emissão anteriores pertencem à proveniência do Git. Não são necessários para compreender ou executar o estado corrente.

## 2. Autoridades comuns e autoridade condicional de IA

Quatro autoridades são universais para o fluxo de Design:

1. `GKR-UX-HOMES-DESIGN-HANDOFF-001 v1.7.10` — `docs/experience-architecture/public-homes-design-handoff.md`;
2. `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001 v1.3.26` — `docs/experience-architecture/public-homes-design-production-readiness-and-figma-contract.md`;
3. `GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001 v3.1.3` — `docs/experience-architecture/public-homes-design-delivery-operational-flow.md`;
4. `GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001 v1.3.2` — `docs/experience-architecture/public-homes-design-production-release.md`.

Quando a designer optar por usar IA, acrescenta-se a autoridade condicional:

- `GKR-UX-HOMES-GENINPUT-001 v2.3.15` — `docs/experience-architecture/public-homes-generative-source-lock-and-prompt-template.md`.

O uso manual não exige Source Lock ou registro de execução de IA.

## 3. Fontes específicas por Home

### 3.1 Pessoa

- `GKR-UX-HOME-PERSON-READ-FIRST-001 v1.0.2` — `docs/experience-architecture/read-first/public-home-person-read-first.md`;

- `GKR-UX-HOME-MASTER-001 v1.0.6` — `docs/experience-architecture/public-home-master-document.md`;
- `GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001 v1.0.2` — `docs/experience-architecture/public-home-person-media-editorial-supply-reconciliation.md`.

### 3.2 Organizações e Coletivos

- `GKR-UX-HOME-OC-READ-FIRST-001 v1.0.2` — `docs/experience-architecture/read-first/public-home-organizations-collectives-read-first.md`;

- `GKR-UX-HOME-OC-MASTER-001 v1.0.5` — `docs/experience-architecture/public-home-organizations-collectives-master-document.md`;
- `GKR-UX-HOME-OC-MEDIA-SUPPLY-001 v1.0.1` — `docs/experience-architecture/public-home-organizations-collectives-media-editorial-supply-reconciliation.md`.

### 3.3 Mall

- `GKR-UX-HOME-MALL-READ-FIRST-001 v1.0.2` — `docs/experience-architecture/read-first/public-home-mall-read-first.md`;

- `GKR-UX-HOME-MALL-MASTER-001 v1.1.3` — `docs/experience-architecture/public-home-mall-master-document.md`;
- `GKR-UX-HOME-MALL-MEDIA-SUPPLY-001 v1.0.1` — `docs/experience-architecture/public-home-mall-media-editorial-supply-reconciliation.md`.

### 3.4 Travel

- `GKR-UX-HOME-TRAVEL-READ-FIRST-001 v1.0.2` — `docs/experience-architecture/read-first/public-home-travel-read-first.md`;

- `GKR-UX-HOME-TRAVEL-MASTER-001 v1.1.5` — `docs/experience-architecture/public-home-travel-master-document.md`;
- `GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001 v1.0.1` — `docs/experience-architecture/public-home-travel-media-editorial-supply-reconciliation.md`.

### 3.5 Media

- `GKR-UX-HOME-MEDIA-READ-FIRST-001 v1.0.1` — `docs/experience-architecture/read-first/public-home-media-read-first.md`;

- `GKR-UX-HOME-MEDIA-MASTER-001 v1.0.3` — `docs/experience-architecture/public-home-media-master-document.md`;
- `GPA-005 v1.2.0` — `docs/product-architecture/media.md`.

### 3.6 Ads

- `GKR-UX-HOME-ADS-READ-FIRST-001 v1.0.1` — `docs/experience-architecture/read-first/public-home-ads-read-first.md`;

- `GKR-UX-HOME-ADS-MASTER-001 v1.0.3` — `docs/experience-architecture/public-home-ads-master-document.md`;
- `GPA-007 v1.3.0` — `docs/product-architecture/ads.md`.

### 3.7 Business

- `GKR-UX-HOME-BUSINESS-READ-FIRST-001 v1.0.16` — `docs/experience-architecture/read-first/public-home-business-read-first.md`;

- `GKR-UX-HOME-BUSINESS-SOURCELOCK-001 v1.1.27` — `docs/experience-architecture/public-home-business-source-lock.md`;
- `GKR-UX-HOME-BUSINESS-MASTER-001 v1.1.8` — `docs/experience-architecture/public-home-business-master-document.md`;
- `GKR-UX-HOME-BUSINESS-CONVERSION-002 v1.0.2` — `docs/experience-architecture/public-home-business-conversion-authority-v2.md`;
- `GKR-UX-HOME-BUSINESS-AUTHORITY-001 v1.0.10` — `docs/experience-architecture/public-home-business-authority-contracts.md`;
- `GPA-004 v1.7.4` — `docs/product-architecture/business.md`;
- `GKR-PLANS-BUSINESS-001 v1.3.1` — `docs/plans/business.md`.

### 3.8 Intelligence

- `GKR-UX-HOME-INTELLIGENCE-READ-FIRST-001 v1.0.6` — `docs/experience-architecture/read-first/public-home-intelligence-read-first.md`;

- `GKR-UX-HOME-INTELLIGENCE-HANDOFF-001 v1.1.16` — `docs/experience-architecture/public-home-intelligence-design-handoff.md`;
- `GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001 v1.1.15` — `docs/experience-architecture/public-home-intelligence-source-lock.md`;
- `GKR-UX-HOME-INTELLIGENCE-MASTER-001 v0.2.12` — `docs/experience-architecture/public-home-intelligence-master-document.md`;
- `GKR-UX-HOME-INTELLIGENCE-NARRATIVE-001 v0.2.5` — `docs/experience-architecture/public-home-intelligence-conceptual-architecture.md`;
- `GKR-UX-HOMES-OUTCOME-001 v1.0.0` — `docs/experience-architecture/public-homes-value-outcome-principle.md`;
- `GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001 v1.0.2` — `docs/product-architecture/intelligence-product-source-lock.md`;
- `GPA-006 v2.0.1` — `docs/product-architecture/intelligence.md`.

## 4. Cobertura atual

```text
HOMES
→ 8 / 8

READ-FIRST ROUTERS
→ 8 / 8 CURRENT

HOME MASTERS
→ 8 / 8 CURRENT

QUICK-REFERENCE MOVEMENTS
→ 83 / 83

UNIVERSAL DESIGN AUTHORITIES
→ 4 / 4 CURRENT

OPTIONAL AI AUTHORITY
→ 1 / 1 CURRENT WHEN AI IS USED

DESIGN PRODUCTION RELEASE
→ GRANTED

GKR-CREATED FIGMA
→ NONE
```

## 5. Consumo para prototipação que atravessa Journey

Quando uma Home levar a uma experiência autenticada, carregar apenas as autoridades Journey correntes necessárias:

- `docs/journeys/index.md`;
- `docs/journeys/person.md`;
- `docs/journeys/collective.md`;
- `docs/journeys/organization.md`;
- `docs/journeys/screen-catalog.md`;
- `docs/journeys/surface-registry.md`;
- `docs/journeys/transition-registry.md`;
- autoridades autenticadas específicas citadas por essas superfícies.

Não carregar sequências históricas de validação, checkpoints, snapshots, candidatos ou auditorias concluídas.

## 6. Regra de atualização

```text
MASTER CHANGED
→ UPDATE THIS MANIFEST + AFFECTED CURRENT AUTHORITIES

NEW VALIDATED RULE
→ UPDATE EXISTING CANONICAL AUTHORITY

SNAPSHOT
→ CREATE ONLY FOR REAL EXTERNAL FREEZE / TRANSPORT NEED

CANDIDATE
→ NOT CREATED BY DEFAULT
```

## 7. Estado

```text
CURRENT DESIGN SOURCE SET
→ READY

HUMAN CONSUMPTION
→ FIRST-CLASS

AI CONSUMPTION
→ OPTIONAL / TOOL-NEUTRAL

HISTORICAL RECONSTRUCTION
→ NOT REQUIRED

DESIGNER MAY START
→ YES

PRODUCT ENGINEERING
→ NOT RELEASED
```
