---
id: GKR-UX-HOME-TRAVEL-READ-FIRST-001
title: 00 — Leia Primeiro — Home Pública — Guivos Travel
status: active
version: 1.0.1
owner: Experience Architecture
last_updated: 2026-09-21
normative: false
maturity: current_design_routing
depends_on:
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
related:
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
---

# 00 — Leia Primeiro — Home Pública — Guivos Travel

## 1. Função

Este arquivo é **camada de roteamento**, não nova autoridade de produto ou Design. Ele indica por onde começar para criar a Home Guivos Travel sem reconstruir histórico, snapshots, checkpoints, PRs ou explorações antigas.

```text
SOURCE OF TRUTH
→ CURRENT MAIN

THIS FILE
→ READ-FIRST / ROUTING ONLY
→ NOT A SUBSTITUTE FOR MASTER OR PRODUCT AUTHORITY

DESIGNER
→ CREATIVE AUTHOR

AI
→ OPTIONAL / DESIGNER-CONTROLLED
```

## 2. Ler nesta ordem

### Autoridades universais de Design

1. `GKR-UX-HOMES-DESIGN-HANDOFF-001`;
2. `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001`;
3. `GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001`;
4. `GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001`.

### Fontes específicas desta Home

1. `GKR-UX-HOME-TRAVEL-MASTER-001 v1.1.5` — `docs/experience-architecture/public-home-travel-master-document.md`;
2. `GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001 v1.0.1` — `docs/experience-architecture/public-home-travel-media-editorial-supply-reconciliation.md`;

Se a designer optar por IA, acrescentar `GKR-UX-HOMES-GENINPUT-001` e preparar Source Lock/prompt somente para essa execução.

## 3. Liberdade criativa

O GKR governa significado, função, narrativa, papéis, limites, evidências, nomenclatura e claims sustentáveis.

A designer governa tipografia, paleta, imagens, ilustração, iconografia, grid, composição, componentes, ritmo, motion, atmosfera e direção visual, salvo texto ou regra explicitamente congelados por autoridade corrente.

Não existe obrigação de reproduzir Figma, SVG, snapshot, estética, layout ou exploração histórica.

## 4. Não carregar por padrão

- auditorias e remediações concluídas;
- candidates e snapshots;
- PRs/checkpoints históricos;
- produtores visuais absorvidos;
- documentos superseded;
- fontes de outras Homes sem necessidade concreta.

## 5. Journey

Carregar Journey adicionalmente **somente quando a solução atravessar da Home pública para experiência autenticada**. Nesse caso, partir de `docs/journeys/index.md` e dos registries correntes, sem reconstruir sequências históricas de UXA.

## 6. Estado

```text
HOME
→ READY FOR EXTERNAL DESIGN

MANUAL DESIGN
→ FIRST-CLASS

AI-ASSISTED DESIGN
→ OPTIONAL

SNAPSHOT REQUIREMENT
→ NONE

PRODUCT ENGINEERING
→ NOT RELEASED BY THIS FILE
```
