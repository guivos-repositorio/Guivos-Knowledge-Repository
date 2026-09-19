---
id: GKR-UX-HOMES-DESIGN-DELIVERY-001
title: Homes Públicas — Manifesto Canônico de Entrega para Design
status: active
version: 6.0.0
owner: Experience Architecture
last_updated: 2026-09-19
normative: true
maturity: design_delivery_v6_candidate_tool_neutral_pre_snapshot
depends_on:
  - GKR-STATE-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
related:
  - GKR-UX-HOMES-DESIGN-V6-AUDIT-001
  - GKR-UX-HOMES-DESIGN-CONSUMPTION-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V4-SNAPSHOT-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V5-SNAPSHOT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
---

# Homes Públicas — Manifesto Canônico de Entrega para Design

## 1. Finalidade

Este Manifesto define a composição-alvo do pacote externo v6, orientado ao consumo pela designer e por IA opcional.

O snapshot v5 permanece histórico, congelado e reproduzível. Ele não será reescrito.

## 2. Princípio do v6

O v6 remove qualquer dependência de Figma Make ou protótipo gerado como etapa governada. Cada Home receberá um `00-LEIA-PRIMEIRO` tool-neutral.

A ausência de identidade visual canônica é deliberada: estética e sistema visual são responsabilidade criativa da designer.

## 3. Composição canônica — 27 fontes únicas

### 3.1 Fontes comuns

1. `docs/experience-architecture/public-homes-design-consumption-contract.md` — `GKR-UX-HOMES-DESIGN-CONSUMPTION-001 v1.0.0`;
2. `docs/experience-architecture/public-homes-design-handoff.md` — `GKR-UX-HOMES-DESIGN-HANDOFF-001 v2.0.0`;
3. `docs/experience-architecture/public-homes-generative-source-lock-and-prompt-template.md` — `GKR-UX-HOMES-GENINPUT-001 v3.0.0`;
4. `docs/experience-architecture/public-homes-design-production-readiness-and-figma-contract.md` — `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001 v2.0.0`;
5. `docs/experience-architecture/public-homes-design-delivery-operational-flow.md` — `GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001 v3.0.0`.

### 3.2 Pessoa

6. `docs/experience-architecture/public-home-master-document.md` — `GKR-UX-HOME-MASTER-001 v1.1.0`;
7. `docs/experience-architecture/public-home-person-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001 v1.0.0`.

### 3.3 Organizações e Coletivos

8. `docs/experience-architecture/public-home-organizations-collectives-master-document.md` — `GKR-UX-HOME-OC-MASTER-001 v1.1.0`;
9. `docs/experience-architecture/public-home-organizations-collectives-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-OC-MEDIA-SUPPLY-001 v1.0.0`.

### 3.4 Mall

10. `docs/experience-architecture/public-home-mall-master-document.md` — `GKR-UX-HOME-MALL-MASTER-001 v1.0.1`;
11. `docs/experience-architecture/public-home-mall-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-MALL-MEDIA-SUPPLY-001 v1.0.0`.

### 3.5 Travel

12. `docs/experience-architecture/public-home-travel-master-document.md` — `GKR-UX-HOME-TRAVEL-MASTER-001 v1.0.1`;
13. `docs/experience-architecture/public-home-travel-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001 v1.0.0`.

### 3.6 Media

14. `docs/experience-architecture/public-home-media-master-document.md` — `GKR-UX-HOME-MEDIA-MASTER-001 v1.0.1`;
15. `docs/product-architecture/media.md` — `GPA-005 v1.2.0`.

### 3.7 Ads

16. `docs/experience-architecture/public-home-ads-master-document.md` — `GKR-UX-HOME-ADS-MASTER-001 v1.0.1`;
17. `docs/product-architecture/ads.md` — `GPA-007 v1.3.0`.

### 3.8 Business

18. `docs/experience-architecture/public-home-business-source-lock.md` — `GKR-UX-HOME-BUSINESS-SOURCELOCK-001 v1.0.0`;
19. `docs/experience-architecture/public-home-business-master-document.md` — `GKR-UX-HOME-BUSINESS-MASTER-001 v1.1.0`;
20. `docs/experience-architecture/public-home-business-conversion-authority-v2.md` — `GKR-UX-HOME-BUSINESS-CONVERSION-002 v1.0.0`;
21. `docs/experience-architecture/public-home-business-authority-contracts.md` — `GKR-UX-HOME-BUSINESS-AUTHORITY-001 v1.0.0`;
22. `docs/product-architecture/business.md` — `GPA-004 v1.6.0`.

### 3.9 Intelligence

23. `docs/experience-architecture/public-home-intelligence-design-handoff.md` — `GKR-UX-HOME-INTELLIGENCE-HANDOFF-001 v1.0.0`;
24. `docs/experience-architecture/public-home-intelligence-source-lock.md` — `GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001 v1.0.0`;
25. `docs/experience-architecture/public-home-intelligence-master-document.md` — `GKR-UX-HOME-INTELLIGENCE-MASTER-001 v0.2.0`;
26. `docs/product-architecture/intelligence-product-source-lock.md` — `GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001 v1.0.0`;
27. `docs/product-architecture/intelligence.md` — `GPA-006 v2.0.0`.

## 4. Oito guias operacionais v6

A emissão v6 gerará oito arquivos `00-LEIA-PRIMEIRO.md`, um por Home.

Cada guia será tool-neutral e deverá conter:

- Home e objetivo;
- checkpoint do pacote;
- fontes e versões;
- ordem de autoridade;
- matriz `CANONICAL / DESIGN_CREATIVE / CONTENT_CANDIDATE / DESIGN_HYPOTHESIS / PROTOTYPE_PLACEHOLDER / REAL_DATA_REQUIRED / OPEN_QUESTION / PROHIBITED_INFERENCE`;
- dados/assets reais necessários;
- referências históricas excluídas como autoridade;
- declaração explícita de que a designer pode criar manualmente e que IA é opcional.

Os guias não conterão prompt obrigatório de Figma Make nem instrução de criação de arquivo.

## 5. Estrutura externa v6

A futura `delivery/design-handoff-v6` deverá conter `00-COMUM` e oito diretórios isolados: Pessoa, Organizações-e-Coletivos, Mall, Travel, Media, Ads, Business e Intelligence.

Os **27 arquivos canônicos** devem reutilizar os blobs do mesmo checkpoint pós-merge. Os oito guias serão materializados especificamente para a emissão.

Contagem planejada:

```text
27 FONTES CANÔNICAS
+
8 GUIAS 00-LEIA-PRIMEIRO
=
35 ARQUIVOS EXTERNOS
```

### 5.1 Integridade, formato e transporte

A emissão v6 deverá preservar:

1. os 27 documentos canônicos extraídos do **mesmo commit pós-merge**;
2. conteúdo canônico reutilizado sem resumo ou adaptação silenciosa;
3. IDs, versões e conteúdo interno preservados;
4. oito `00-LEIA-PRIMEIRO` como artefatos operacionais da emissão;
5. registro do commit de origem e commit/tree da emissão;
6. `delivery/design-handoff-v6` separada dos snapshots v1–v5;
7. v1–v5 históricos e imutáveis;
8. Markdown como formato primário para humanos e IA;
9. PDF apenas como conveniência de leitura;
10. ZIP apenas como embalagem de transferência;
11. qualquer ZIP derivado exclusivamente do snapshot v6 validado;
12. prevalência do snapshot Git registrado em caso de divergência;
13. isolamento das fontes específicas de cada Home;
14. nenhuma referência externa incorporada às 27 fontes sem adjudicação.

```text
SNAPSHOT GIT V6
→ REPRODUCIBLE AUTHORITY OF THE EXTERNAL PACKAGE

ZIP
→ TRANSFER CONVENIENCE ONLY

PDF
→ HUMAN READING AID ONLY

MARKDOWN
→ PRIMARY SOURCE FORMAT
```

### 5.2 Mudança de fonte após a emissão

Se qualquer uma das 27 fontes sofrer mudança depois do snapshot, classificar o impacto.

```text
NON-MATERIAL CHANGE
→ MAY PRESERVE SNAPSHOT AFTER RECORDED REVIEW

MATERIAL CHANGE TO MEANING / INVARIANT / SOURCE PACKAGE / CLASSES / BOUNDARIES
→ AFFECTED HOME PACKAGE INVALIDATED FOR NEW CONSUMPTION
→ REISSUE / REVALIDATE BEFORE CONTINUING
```

Uma alteração puramente criativa no artefato externo da designer que não modifica o contrato do GKR não exige reemissão do pacote fonte.

## 6. Regra para sistemas de IA

IA é opcional. Quando utilizada, recebe `00-COMUM` + `00-LEIA-PRIMEIRO` da Home + fontes específicas, sem autoridade adicional e sem etapa generativa obrigatória.

## 7. Materiais fora do pacote inicial

- snapshots v1–v4;
- GENINPUTs históricos de checkpoint;
- benchmarks;
- rascunhos de conversa;
- documentação de Engenharia;
- pricing não formalizado;
- assets ou brand book visual inexistentes como suposta obrigação.

Referências adicionais entram somente para resolver dúvida concreta e permanecem `INSPIRATION_ONLY` ou fonte adicional explicitamente declarada, conforme sua natureza.

## 8. Gate de emissão v6

A emissão v6 exige remediação tool-neutral, revisão 8/8 dos Masters, reconciliação de estados obsoletos, auditoria de prescrições estéticas, fechamento das fontes, Semantic + Mechanical, revisão independente, zero finding material, merge governado, captura do `main`, geração dos oito guias e validação do snapshot.

## 9. Estado

```text
V5
→ FROZEN / HISTORICAL
→ delivery/design-handoff-v5
V6
→ CANDIDATE / UNDER REMEDIATION
→ NOT YET EMITTED
DESIGN CONSUMPTION
→ TOOL-NEUTRAL
GKR FIGMA MATERIALIZATION
→ OUT OF PROCESS
DESIGNER
→ PRIMARY CREATIVE AUTHOR
AI
→ OPTIONAL SUPPORT
```
