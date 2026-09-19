---
id: GKR-UX-HOMES-DESIGN-DELIVERY-001
title: Homes Públicas — Manifesto Canônico de Entrega para Design
status: active
version: 6.0.0
owner: Experience Architecture
last_updated: 2026-09-19
normative: true
maturity: design_delivery_v6_documentary_candidate_pre_snapshot
depends_on:
  - GKR-STATE-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
related:
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V5-SNAPSHOT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
---

# Homes Públicas — Manifesto Canônico de Entrega para Design

## 1. Finalidade

Este Manifesto define o **candidato v6** do pacote documental a ser entregue à designer e, quando útil, consumido por sistemas de IA de apoio.

O v6 corrige a hipótese operacional do v5: o pacote **não exige Figma Make e não prevê materialização direta do arquivo oficial pelo GKR ou por IA**.

## 2. Princípio do v6

```text
GKR
→ SOURCE OF TRUTH

DESIGNER
→ HUMAN CREATIVE OWNER

AI
→ OPTIONAL ASSISTIVE CONSUMER

FIGMA
→ OFFICIAL DESIGN WORKSPACE CREATED / CURATED BY DESIGNER
```

Ausência de identidade visual canônica continua sendo liberdade deliberada, não gap.

## 3. Composição canônica — 26 fontes únicas

### 3.1 Fontes comuns

1. `docs/experience-architecture/public-homes-design-handoff.md` — `GKR-UX-HOMES-DESIGN-HANDOFF-001 v2.0.0`;
2. `docs/experience-architecture/public-homes-generative-source-lock-and-prompt-template.md` — `GKR-UX-HOMES-GENINPUT-001 v3.0.0`;
3. `docs/experience-architecture/public-homes-design-production-readiness-and-figma-contract.md` — `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001 v2.0.0`;
4. `docs/experience-architecture/public-homes-design-delivery-operational-flow.md` — `GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001 v3.0.0`.

### 3.2 Pessoa

5. `docs/experience-architecture/public-home-master-document.md` — `GKR-UX-HOME-MASTER-001 v1.1.0`;
6. `docs/experience-architecture/public-home-person-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001 v1.0.0`.

### 3.3 Organizações e Coletivos

7. `docs/experience-architecture/public-home-organizations-collectives-master-document.md` — `GKR-UX-HOME-OC-MASTER-001 v1.1.0`;
8. `docs/experience-architecture/public-home-organizations-collectives-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-OC-MEDIA-SUPPLY-001 v1.0.0`.

### 3.4 Mall

9. `docs/experience-architecture/public-home-mall-master-document.md` — `GKR-UX-HOME-MALL-MASTER-001 v1.1.0`;
10. `docs/experience-architecture/public-home-mall-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-MALL-MEDIA-SUPPLY-001 v1.0.0`.

### 3.5 Travel

11. `docs/experience-architecture/public-home-travel-master-document.md` — `GKR-UX-HOME-TRAVEL-MASTER-001 v1.1.0`;
12. `docs/experience-architecture/public-home-travel-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001 v1.0.0`.

### 3.6 Media

13. `docs/experience-architecture/public-home-media-master-document.md` — `GKR-UX-HOME-MEDIA-MASTER-001 v1.1.0`;
14. `docs/product-architecture/media.md` — `GPA-005 v1.2.0`.

### 3.7 Ads

15. `docs/experience-architecture/public-home-ads-master-document.md` — `GKR-UX-HOME-ADS-MASTER-001 v1.1.0`;
16. `docs/product-architecture/ads.md` — `GPA-007 v1.3.0`.

### 3.8 Business

17. `docs/experience-architecture/public-home-business-source-lock.md` — `GKR-UX-HOME-BUSINESS-SOURCELOCK-001 v1.0.0`;
18. `docs/experience-architecture/public-home-business-master-document.md` — `GKR-UX-HOME-BUSINESS-MASTER-001 v1.1.0`;
19. `docs/experience-architecture/public-home-business-conversion-authority-v2.md` — `GKR-UX-HOME-BUSINESS-CONVERSION-002 v1.0.0`;
20. `docs/experience-architecture/public-home-business-authority-contracts.md` — `GKR-UX-HOME-BUSINESS-AUTHORITY-001 v1.0.0`;
21. `docs/product-architecture/business.md` — `GPA-004 v1.6.0`.

### 3.9 Intelligence

22. `docs/experience-architecture/public-home-intelligence-design-handoff.md` — `GKR-UX-HOME-INTELLIGENCE-HANDOFF-001 v1.0.0`;
23. `docs/experience-architecture/public-home-intelligence-source-lock.md` — `GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001 v1.0.0`;
24. `docs/experience-architecture/public-home-intelligence-master-document.md` — `GKR-UX-HOME-INTELLIGENCE-MASTER-001 v0.2.0`;
25. `docs/product-architecture/intelligence-product-source-lock.md` — `GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001 v1.0.0`;
26. `docs/product-architecture/intelligence.md` — `GPA-006 v2.0.0`.

## 4. Oito guias `00-LEIA-PRIMEIRO`

A emissão v6 deverá gerar um guia por Home contendo objetivo, checkpoint, fontes/SHAs, ordem de leitura humana, ordem de contexto para IA, invariantes, liberdades criativas, oito classes, dados que exigem lastro, inferências proibidas, questões abertas e checklist.

Os guias não serão prompts de Figma Make.

## 5. Estrutura externa planejada

`GUIVOS-HOMES-DESIGN-HANDOFF-v6/` deverá conter `00-COMUM` e oito diretórios isolados.

```text
26 FONTES CANÔNICAS
+
8 GUIAS LEIA-PRIMEIRO
=
34 ARQUIVOS EXTERNOS
```

Markdown é o formato primário para humano e IA. PDF é auxílio de leitura. ZIP é transporte. Git preserva a referência reproduzível.

## 6. Regra para IA

```text
AI CONTEXT
→ COMMON SOURCES
+ HOME LEIA-PRIMEIRO
+ HOME-SPECIFIC SOURCES

AI ROLE
→ ASSIST / SYNTHESIZE / IDEATE / CHECK

AI ROLE
≠ CANONICALIZE
≠ APPROVE
≠ OWN OFFICIAL FIGMA
```

## 7. Liberdade da designer

O pacote não define tipografia, cor, imagem, grid, composição, iconografia, motion, sistema de ilustração, atmosfera ou template visual obrigatório.

Arquivos históricos como `guivos.com 2.0` e benchmarks podem ser consultados como referência, sem se tornarem autoridade estética por inferência.

## 8. Integridade e mudança de fonte

As 26 fontes devem vir do mesmo checkpoint pós-merge da futura emissão v6. Mudança material posterior invalida apenas o contexto afetado até revalidação.

## 9. Estado

```text
V5 SNAPSHOT
→ FROZEN / HISTORICAL FOR NEW EXECUTION

V6 MANIFEST
→ DOCUMENTARY CANDIDATE
→ SNAPSHOT NOT_EMITTED

DESIGN PRODUCTION RELEASE
→ GRANTED

EXTERNAL DESIGN
→ HOLD UNTIL V6 SNAPSHOT

AI SUPPORT
→ OPTIONAL / NON-AUTHORITATIVE

DIRECT GKR/AI FIGMA MATERIALIZATION
→ OUT_OF_SCOPE
```