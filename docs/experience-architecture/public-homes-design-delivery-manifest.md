---
id: GKR-UX-HOMES-DESIGN-DELIVERY-001
title: Homes Públicas — Manifesto Canônico de Entrega para Design
status: active
version: 6.1.2
owner: Experience Architecture
last_updated: 2026-09-19
normative: true
maturity: v6_emitted_frozen_invalidated_for_new_execution_reissue_required
depends_on:
  - GKR-STATE-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
related:
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V5-SNAPSHOT-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V6-SNAPSHOT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
  - GKR-UX-HOMES-DESIGN-SOURCE-COMPLETENESS-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V6-CANDIDATE-001
---

# Homes Públicas — Manifesto Canônico de Entrega para Design

## 1. Finalidade

Este Manifesto governa a emissão externa das oito Homes públicas para criação pela designer.

O snapshot **v6 foi emitido, materializado e teve sua integridade validada**, mas uma revisão independente pós-emissão encontrou um P1 material dentro do próprio pacote: o Operational Flow v3.0.1 preservou linguagem pré-emissão incompatível com o uso corrente. O v6 permanece congelado e reproduzível como proveniência histórica, porém **não é válido para nova execução**. Neste estado, não existe pacote externo corrente; nova emissão/revalidação é necessária. O v5 também permanece congelado como snapshot histórico.

```text
DESIGNER
→ CREATIVE AUTHOR
→ MANUAL FIRST-CLASS

AI
→ OPTIONAL / DESIGNER-CONTROLLED

GKR
→ SOURCE OF SEMANTIC / FUNCTIONAL / EVIDENCE TRUTH

VISUAL IDENTITY
→ DESIGN-OWNED

GKR-CREATED FIGMA
→ NONE
```

## 2. Checkpoint e snapshot v6 preservado

```text
ORIGIN MAIN
→ 52f1dade6d7bfcd8c1e5d1b567d7125ac725018f

SNAPSHOT BRANCH
→ delivery/design-handoff-v6

SNAPSHOT COMMIT
→ b7fe5d62cef444c8316c66edd8ac73b703698a4a

SNAPSHOT TREE
→ 61eef7447fc5c6b36890ccb774f7011615a6abca
```

O registro reproduzível da emissão e da invalidação posterior para nova execução é `GKR-UX-HOMES-DESIGN-DELIVERY-V6-SNAPSHOT-001 v1.1.1`.

## 3. Composição canônica para próxima reemissão — 29 fontes únicas

### 3.1 Fontes comuns

1. `docs/experience-architecture/public-homes-design-handoff.md` — `GKR-UX-HOMES-DESIGN-HANDOFF-001 v1.6.3`;
2. `docs/experience-architecture/public-homes-generative-source-lock-and-prompt-template.md` — `GKR-UX-HOMES-GENINPUT-001 v2.2.15`;
3. `docs/experience-architecture/public-homes-design-production-readiness-and-figma-contract.md` — `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001 v1.2.15`;
4. `docs/experience-architecture/public-homes-design-delivery-operational-flow.md` — `GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001 v3.0.2`;
5. `docs/experience-architecture/public-homes-design-production-release.md` — `GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001 v1.2.0`.

### 3.2 Pessoa

6. `docs/experience-architecture/public-home-master-document.md` — `GKR-UX-HOME-MASTER-001 v1.0.3`;
7. `docs/experience-architecture/public-home-person-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001 v1.0.0`.

### 3.3 Organizações e Coletivos

8. `docs/experience-architecture/public-home-organizations-collectives-master-document.md` — `GKR-UX-HOME-OC-MASTER-001 v1.0.3`;
9. `docs/experience-architecture/public-home-organizations-collectives-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-OC-MEDIA-SUPPLY-001 v1.0.0`.

### 3.4 Mall

10. `docs/experience-architecture/public-home-mall-master-document.md` — `GKR-UX-HOME-MALL-MASTER-001 v1.1.1`;
11. `docs/experience-architecture/public-home-mall-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-MALL-MEDIA-SUPPLY-001 v1.0.0`.

### 3.5 Travel

12. `docs/experience-architecture/public-home-travel-master-document.md` — `GKR-UX-HOME-TRAVEL-MASTER-001 v1.1.3`;
13. `docs/experience-architecture/public-home-travel-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001 v1.0.0`.

### 3.6 Media

14. `docs/experience-architecture/public-home-media-master-document.md` — `GKR-UX-HOME-MEDIA-MASTER-001 v1.0.1`;
15. `docs/product-architecture/media.md` — `GPA-005 v1.2.0`.

### 3.7 Ads

16. `docs/experience-architecture/public-home-ads-master-document.md` — `GKR-UX-HOME-ADS-MASTER-001 v1.0.1`;
17. `docs/product-architecture/ads.md` — `GPA-007 v1.3.0`.

### 3.8 Business

18. `docs/experience-architecture/public-home-business-source-lock.md` — `GKR-UX-HOME-BUSINESS-SOURCELOCK-001 v1.1.6`;
19. `docs/experience-architecture/public-home-business-master-document.md` — `GKR-UX-HOME-BUSINESS-MASTER-001 v1.1.3`;
20. `docs/experience-architecture/public-home-business-conversion-authority-v2.md` — `GKR-UX-HOME-BUSINESS-CONVERSION-002 v1.0.0`;
21. `docs/experience-architecture/public-home-business-authority-contracts.md` — `GKR-UX-HOME-BUSINESS-AUTHORITY-001 v1.0.3`;
22. `docs/product-architecture/business.md` — `GPA-004 v1.6.0`.

### 3.9 Intelligence

23. `docs/experience-architecture/public-home-intelligence-design-handoff.md` — `GKR-UX-HOME-INTELLIGENCE-HANDOFF-001 v1.1.10`;
24. `docs/experience-architecture/public-home-intelligence-source-lock.md` — `GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001 v1.1.9`;
25. `docs/experience-architecture/public-home-intelligence-master-document.md` — `GKR-UX-HOME-INTELLIGENCE-MASTER-001 v0.2.7`;
26. `docs/experience-architecture/public-home-intelligence-conceptual-architecture.md` — `GKR-UX-HOME-INTELLIGENCE-NARRATIVE-001 v0.2.3`;
27. `docs/experience-architecture/public-homes-value-outcome-principle.md` — `GKR-UX-HOMES-OUTCOME-001 v1.0.0`;
28. `docs/product-architecture/intelligence-product-source-lock.md` — `GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001 v1.0.1`;
29. `docs/product-architecture/intelligence.md` — `GPA-006 v2.0.1`.

## 4. Oito guias operacionais do snapshot v6

Cada Home possui `00-LEIA-PRIMEIRO.md` com checkpoint, fontes/IDs/versões/blobs, ordem de leitura, invariantes, matriz das oito classes, dados reais, questões abertas, inferências proibidas, liberdade criativa, manual-first, IA opcional, prompt tool-neutral e autoauditoria.

O guia não substitui as autoridades que lista.

## 5. Estrutura externa v6 preservada

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

```text
5 COMMON
+
24 HOME-SPECIFIC UNIQUE
=
29 CANONICAL

29 CANONICAL
+
8 GUIDES
=
37 EXTERNAL FILES
```

## 6. Integridade comprovada

```text
29 / 29 CANONICAL SOURCES PRESENT
29 / 29 MAIN BLOB × SNAPSHOT BLOB EXACT MATCH
MISMATCHES = 0
EXTRA BLOBS = 0
```

Nenhum documento canônico foi resumido, reescrito ou adaptado para formar o pacote.

## 7. Regra de consumo humano

A designer pode trabalhar sem IA:

```text
READ
→ UNDERSTAND
→ CREATE
→ AUTOAUDIT
→ HUMAN REVIEW
```

## 8. Regra de consumo com IA opcional

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

Não misturar fontes específicas de Homes diferentes por conveniência.

## 9. Formatos e transporte

```text
GIT SNAPSHOT
→ REPRODUCIBLE PACKAGE AUTHORITY

MARKDOWN
→ PRIMARY HUMAN + AI SOURCE

PDF
→ OPTIONAL HUMAN READING AID

ZIP
→ OPTIONAL TRANSPORT
```

## 10. Mudança após emissão

Mudança criativa da designer sem alteração de contrato não exige reemissão.

Mudança material nas fontes ou invariantes da Home exige adjudicação e, quando afetar nova execução, reissue/revalidation. Mudança não material pode preservar o snapshot após review registrado.

## 11. Finding pós-emissão e efeito governado

A revisão independente da PR #402 sobre o HEAD `615ec67af2f3d463747bdb309fc49cb88e557137` encontrou um P1 material no pacote emitido:

```text
SNAPSHOT V6 FLOW
→ GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001 v3.0.1
→ SOURCE COMPLETENESS AUDIT = IN PROGRESS
→ V6 PACKAGE = NOT YET ELIGIBLE

ADJUDICATION
→ VALID MATERIAL CONTRADICTION

CANONICAL REMEDIATION
→ FLOW v3.0.2
→ RELEASE v1.2.0

FROZEN V6 SNAPSHOT
→ NOT REWRITTEN
→ INVALID FOR NEW EXECUTION

CURRENT EXTERNAL SOURCE PACKAGE
→ NONE
→ REISSUE / REVALIDATION REQUIRED
```

## 12. Segundo finding pós-emissão — autoridades comuns da próxima reemissão

O re-review Codex da PR #402 sobre o HEAD `b815e0f07f5f59bde2fbbd23288a65b1816cb2e4` identificou outro P1 material antes de qualquer nova emissão:

```text
P1 — RECONCILE THE COMMON AUTHORITIES BEFORE REISSUING
→ VALID

GENINPUT v2.2.14
→ GENERATIVE EXECUTION = AUTHORIZED TO EXECUTE
→ STALE RELEASE / V6-CANDIDATE REFERENCES

READINESS v1.2.14
→ AI-ASSISTED DESIGN = AUTHORIZED TO EXECUTE
→ STALE RELEASE / CURRENT-CANDIDATE REFERENCES

REMEDIATION
→ HANDOFF v1.6.3
→ GENINPUT v2.2.15
→ READINESS v1.2.15
→ FLOW v3.0.2
→ RELEASE v1.2.0
→ CURRENT EXTERNAL SOURCE PACKAGE = NONE
→ OPERATIONAL EXECUTION = PAUSED
→ NEW CANDIDATE / REISSUE REQUIRED BEFORE MATERIALIZATION
```

Esse finding não altera o snapshot v6 histórico. Ele corrige as autoridades canônicas que poderão compor uma futura reemissão.

## 13. Snapshots históricos

`delivery/design-handoff-v1` até `delivery/design-handoff-v5` permanecem congelados. O v5 está registrado em `GKR-UX-HOMES-DESIGN-DELIVERY-V5-SNAPSHOT-001`.

O v6 não reescreve nenhuma emissão anterior. Após o finding pós-emissão, ele permanece congelado como proveniência histórica e não deve ser usado para nova execução.

## 14. Estado

```text
V5
→ FROZEN / HISTORICAL

V6
→ EMITTED / MATERIALIZED / INTEGRITY-VALIDATED
→ FROZEN / HISTORICAL
→ INVALID FOR NEW EXECUTION AFTER POST-EMISSION P1

CURRENT EXTERNAL SOURCE PACKAGE
→ NONE
→ REISSUE / REVALIDATION REQUIRED

SNAPSHOT
→ delivery/design-handoff-v6
→ commit b7fe5d62cef444c8316c66edd8ac73b703698a4a
→ tree 61eef7447fc5c6b36890ccb774f7011615a6abca

DESIGN PRODUCTION RELEASE
→ GRANTED

EXTERNAL DESIGNER PRODUCTION AUTHORIZATION
→ RELEASED

OPERATIONAL EXECUTION
→ PAUSED UNTIL VALID CURRENT PACKAGE EXISTS

AI
→ OPTIONAL / DESIGNER-CONTROLLED

GKR-CREATED FIGMA
→ NONE

FINAL DESIGN ACCEPTANCE
→ HUMAN / SEPARATE

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```
