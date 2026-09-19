---
id: GKR-UX-HOMES-DESIGN-DELIVERY-V6-CANDIDATE-001
title: Homes Públicas — Pacote v6 Candidato para Designer e IA Opcional
status: draft
version: 0.2.0
owner: Experience Architecture
last_updated: 2026-09-19
normative: false
maturity: v6_candidate_defined_snapshot_not_emitted
depends_on:
  - GKR-UX-HOMES-DESIGN-SOURCE-COMPLETENESS-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
related:
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V5-SNAPSHOT-001
---

# Homes Públicas — Pacote v6 Candidato para Designer e IA Opcional

## 1. Finalidade

Este documento define a composição **candidata** do próximo pacote externo das oito Homes.

O v6 nasce para corrigir uma única classe de problema operacional do v5:

> **a designer deve receber documentação completa e determinística sem ser obrigada a seguir Figma Make, protótipo gerativo ou direção visual criada pelo GKR.**

O v6 permanece pré-snapshot.

```text
V5
→ LAST EMITTED SNAPSHOT
→ FROZEN

V6
→ CANDIDATE DEFINITION
→ NOT YET EMITTED
```

## 2. Princípios do v6

```text
DESIGNER
→ CREATIVE AUTHOR
→ MANUAL FIRST-CLASS

AI
→ OPTIONAL
→ DESIGNER-CONTROLLED

GKR
→ SOURCE OF SEMANTIC / FUNCTIONAL / EVIDENCE TRUTH

VISUAL IDENTITY
→ DESIGN-OWNED

GKR-CREATED FIGMA
→ NONE

MARKDOWN
→ PRIMARY HUMAN + AI SOURCE FORMAT
```

## 3. Composição candidata — 27 fontes canônicas

### 3.1 Fontes comuns

1. `docs/experience-architecture/public-homes-design-handoff.md` — `GKR-UX-HOMES-DESIGN-HANDOFF-001 v1.6.1`;
2. `docs/experience-architecture/public-homes-generative-source-lock-and-prompt-template.md` — `GKR-UX-HOMES-GENINPUT-001 v2.2.0`;
3. `docs/experience-architecture/public-homes-design-production-readiness-and-figma-contract.md` — `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001 v1.2.0`;
4. `docs/experience-architecture/public-homes-design-delivery-operational-flow.md` — `GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001 v3.0.1`;
5. `docs/experience-architecture/public-homes-design-production-release.md` — `GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001 v1.1.0`.

### 3.2 Pessoa

6. `docs/experience-architecture/public-home-master-document.md` — `GKR-UX-HOME-MASTER-001 v1.0.2`;
7. `docs/experience-architecture/public-home-person-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001 v1.0.0`.

### 3.3 Organizações e Coletivos

8. `docs/experience-architecture/public-home-organizations-collectives-master-document.md` — `GKR-UX-HOME-OC-MASTER-001 v1.0.0`;
9. `docs/experience-architecture/public-home-organizations-collectives-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-OC-MEDIA-SUPPLY-001 v1.0.0`.

### 3.4 Mall

10. `docs/experience-architecture/public-home-mall-master-document.md` — `GKR-UX-HOME-MALL-MASTER-001 v1.1.0`;
11. `docs/experience-architecture/public-home-mall-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-MALL-MEDIA-SUPPLY-001 v1.0.0`.

### 3.5 Travel

12. `docs/experience-architecture/public-home-travel-master-document.md` — `GKR-UX-HOME-TRAVEL-MASTER-001 v1.1.1`;
13. `docs/experience-architecture/public-home-travel-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001 v1.0.0`.

### 3.6 Media

14. `docs/experience-architecture/public-home-media-master-document.md` — `GKR-UX-HOME-MEDIA-MASTER-001 v1.0.1`;
15. `docs/product-architecture/media.md` — `GPA-005 v1.2.0`.

### 3.7 Ads

16. `docs/experience-architecture/public-home-ads-master-document.md` — `GKR-UX-HOME-ADS-MASTER-001 v1.0.1`;
17. `docs/product-architecture/ads.md` — `GPA-007 v1.3.0`.

### 3.8 Business

18. `docs/experience-architecture/public-home-business-source-lock.md` — `GKR-UX-HOME-BUSINESS-SOURCELOCK-001 v1.1.0`;
19. `docs/experience-architecture/public-home-business-master-document.md` — `GKR-UX-HOME-BUSINESS-MASTER-001 v1.1.1`;
20. `docs/experience-architecture/public-home-business-conversion-authority-v2.md` — `GKR-UX-HOME-BUSINESS-CONVERSION-002 v1.0.0`;
21. `docs/experience-architecture/public-home-business-authority-contracts.md` — `GKR-UX-HOME-BUSINESS-AUTHORITY-001 v1.0.0`;
22. `docs/product-architecture/business.md` — `GPA-004 v1.6.0`.

### 3.9 Intelligence

23. `docs/experience-architecture/public-home-intelligence-design-handoff.md` — `GKR-UX-HOME-INTELLIGENCE-HANDOFF-001 v1.0.0`;
24. `docs/experience-architecture/public-home-intelligence-source-lock.md` — `GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001 v1.0.0`;
25. `docs/experience-architecture/public-home-intelligence-master-document.md` — `GKR-UX-HOME-INTELLIGENCE-MASTER-001 v0.2.0`;
26. `docs/product-architecture/intelligence-product-source-lock.md` — `GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001 v1.0.0`;
27. `docs/product-architecture/intelligence.md` — `GPA-006 v2.0.0`.

## 4. Oito guias de consumo v6

O snapshot v6 deverá gerar um `00-LEIA-PRIMEIRO.md` para cada Home.

Cada guia deve conter:

1. nome da Home;
2. objetivo do pacote;
3. commit canônico de origem;
4. lista exata de fontes, IDs, versões e blobs;
5. ordem de leitura;
6. resumo dos invariantes sem criar nova autoridade;
7. matriz das oito classes operacionais;
8. lista de dados reais necessários;
9. questões abertas;
10. inferências proibidas;
11. liberdade criativa da designer;
12. instrução manual-first;
13. instrução de IA opcional;
14. prompt tool-neutral para IA, caso seja usada;
15. checklist de autoauditoria;
16. indicação explícita de que nenhum Figma criado pelo GKR é referência.

## 5. Estrutura externa candidata

```text
GUIVOS-HOMES-DESIGN-HANDOFF-v6/
│
├── 00-COMUM/
│   ├── 01-Handoff-Canonico-das-Homes.md
│   ├── 02-Source-Lock-e-Prompt-IA-Opcional.md
│   ├── 03-Prontidao-de-Producao-e-Contrato-Designer-IA.md
│   ├── 04-Fluxo-Operacional-Designer-First.md
│   └── 05-Design-Production-Release.md
│
├── 01-HOME-PESSOA/
├── 02-HOME-ORGANIZACOES-E-COLETIVOS/
├── 03-HOME-MALL/
├── 04-HOME-TRAVEL/
├── 05-HOME-MEDIA/
├── 06-HOME-ADS/
├── 07-HOME-BUSINESS/
└── 08-HOME-INTELLIGENCE/
```

Cada diretório de Home contém:

- `00-LEIA-PRIMEIRO.md`;
- somente as fontes específicas daquela Home.

## 6. Contagem candidata

```text
COMMON SOURCES
→ 5

HOME-SPECIFIC UNIQUE SOURCES
→ 22

CANONICAL SOURCES TOTAL
→ 27

READ-FIRST GUIDES
→ 8

TOTAL EXTERNAL FILES
→ 35
```

## 7. Regra de consumo humano

A designer pode trabalhar somente com leitura humana dos documentos.

Ela não precisa usar IA.

```text
READ
→ UNDERSTAND
→ CREATE
→ AUTOAUDIT
→ HUMAN REVIEW
```

## 8. Regra de consumo por IA

Quando a designer optar por IA:

```text
00-COMUM
+
00-LEIA-PRIMEIRO
+
HOME-SPECIFIC SOURCES
↓
OPTIONAL AI
↓
PROPOSAL / HYPOTHESIS
↓
DESIGNER JUDGMENT
```

Não carregar as oito Homes ao mesmo tempo.

## 9. Formatos

```text
MARKDOWN
→ PRIMARY SOURCE

PDF
→ OPTIONAL HUMAN READING AID

ZIP
→ OPTIONAL TRANSPORT

GIT SNAPSHOT
→ REPRODUCIBLE PACKAGE AUTHORITY
```

Nenhum resumo substitui o Markdown integral.

## 10. Mudança após emissão

```text
NON-MATERIAL SOURCE CHANGE
→ RECORDED REVIEW MAY PRESERVE PACKAGE

MATERIAL SOURCE CHANGE
→ AFFECTED HOME INVALIDATED FOR NEW EXECUTION
→ REISSUE / REVALIDATE
```

Mudança criativa feita pela designer sem alterar contrato semântico não exige alteração do GKR.

## 11. Gates antes da emissão

O v6 somente se torna elegível para snapshot após:

- C1–C15 = PASS para 8/8 Homes;
- 27/27 fontes existentes;
- ID/versão/path reconciliados;
- Semantic Validation = SUCCESS;
- Mechanical Validation = SUCCESS;
- revisão independente limpa no HEAD exato;
- zero finding material aberto;
- ato humano separado autorizando emissão/materialização.

## 12. Estado

```text
V6 PACKAGE DEFINITION
→ PREPARED / CANDIDATE

C1–C15
→ CANDIDATE PASS / 8 OF 8

SNAPSHOT V6
→ NOT EMITTED

DESIGNER PRODUCTION
→ EXTERNAL / DESIGNER-OWNED

AI
→ OPTIONAL

GKR-CREATED FIGMA
→ NONE

PRODUCT ENGINEERING
→ NOT RELEASED
```
