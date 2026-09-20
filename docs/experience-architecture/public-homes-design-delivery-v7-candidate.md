---
id: GKR-UX-HOMES-DESIGN-DELIVERY-V7-CANDIDATE-001
title: Homes Públicas — Pacote v7 Candidato para Reemissão e Revalidação
status: draft
version: 0.2.1
owner: Experience Architecture
last_updated: 2026-09-20
normative: false
maturity: reissue_candidate_revalidated_merged_materialization_decision_pending
depends_on:
  - GKR-UX-HOMES-DESIGN-SOURCE-COMPLETENESS-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
related:
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V6-CANDIDATE-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V6-SNAPSHOT-001
---

# Homes Públicas — Pacote v7 Candidato para Reemissão e Revalidação

## 1. Finalidade

Este documento prepara o próximo pacote externo das oito Homes após a invalidação do snapshot v6 para nova execução.

Ele **não materializa** um novo snapshot, não cria branch `delivery/design-handoff-v7`, não libera execução operacional, não cria Figma e não libera Product Engineering.

O candidato v7 existe para revalidar a composição externa contra as autoridades canônicas corrigidas após os dois P1 pós-emissão do v6.

```text
PREPARATION BASE / MAIN
→ 1a1386bc318afa2e91f5c1ef5ffd3a80e7265cb2

V6
→ FROZEN / HISTORICAL
→ INVALID FOR NEW EXECUTION

V7
→ CANDIDATE PREPARED
→ REVALIDATION PASS
→ MATERIALIZATION DECISION PENDING / SEPARATE HUMAN ACT

CURRENT EXTERNAL SOURCE PACKAGE
→ NONE
```

## 2. Princípios preservados

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

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```

## 3. Composição candidata v7 — 29 fontes canônicas

Cada pin abaixo foi recalculado diretamente no commit canônico de preparação `1a1386bc318afa2e91f5c1ef5ffd3a80e7265cb2`.

### 3.1 Fontes comuns

1. `docs/experience-architecture/public-homes-design-handoff.md` — `GKR-UX-HOMES-DESIGN-HANDOFF-001 v1.6.3` — blob `0427afa0c99cbfe5189661ef4bea606b1008ec7f`;
2. `docs/experience-architecture/public-homes-generative-source-lock-and-prompt-template.md` — `GKR-UX-HOMES-GENINPUT-001 v2.2.15` — blob `e696d73767b77d1346b646bcab6e1af0105af762`;
3. `docs/experience-architecture/public-homes-design-production-readiness-and-figma-contract.md` — `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001 v1.2.15` — blob `a087487c98ee133787ea184849d0995b3523f907`;
4. `docs/experience-architecture/public-homes-design-delivery-operational-flow.md` — `GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001 v3.0.2` — blob `18a135f717fd90e1fa4a80230f0561d04902bbd1`;
5. `docs/experience-architecture/public-homes-design-production-release.md` — `GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001 v1.2.0` — blob `414fb213f44494b00eed09b6dab6c460295cb726`.

### 3.2 Pessoa

6. `docs/experience-architecture/public-home-master-document.md` — `GKR-UX-HOME-MASTER-001 v1.0.3` — blob `2c33978024dc98e694c719c4b72b1de76206c4cb`;
7. `docs/experience-architecture/public-home-person-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001 v1.0.0` — blob `72bb3fcb8a5cdcfa0256a0c789b996085f8c1d7e`.

### 3.3 Organizações e Coletivos

8. `docs/experience-architecture/public-home-organizations-collectives-master-document.md` — `GKR-UX-HOME-OC-MASTER-001 v1.0.3` — blob `adcc030791a50649f44ad95ef75d202e7b61a1d7`;
9. `docs/experience-architecture/public-home-organizations-collectives-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-OC-MEDIA-SUPPLY-001 v1.0.0` — blob `e8aa2e343eba9aa2568ed7219c72a968453c7257`.

### 3.4 Mall

10. `docs/experience-architecture/public-home-mall-master-document.md` — `GKR-UX-HOME-MALL-MASTER-001 v1.1.1` — blob `c0422565d5da42bff334583203623fb529388226`;
11. `docs/experience-architecture/public-home-mall-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-MALL-MEDIA-SUPPLY-001 v1.0.0` — blob `986cf6bb35cccd71f9ea681836a29e14281dae7c`.

### 3.5 Travel

12. `docs/experience-architecture/public-home-travel-master-document.md` — `GKR-UX-HOME-TRAVEL-MASTER-001 v1.1.3` — blob `cf1933cab5d1d968d8c2f88525548a8ca11955ff`;
13. `docs/experience-architecture/public-home-travel-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001 v1.0.0` — blob `77e90af980fe0b315abc6ade079c096ce1755f6f`.

### 3.6 Media

14. `docs/experience-architecture/public-home-media-master-document.md` — `GKR-UX-HOME-MEDIA-MASTER-001 v1.0.1` — blob `71f8eae8731ec448a8b513e4f82857399af85c95`;
15. `docs/product-architecture/media.md` — `GPA-005 v1.2.0` — blob `59ddb05ffc9b3d6d6e6f27fc405f82e4bc6ee260`.

### 3.7 Ads

16. `docs/experience-architecture/public-home-ads-master-document.md` — `GKR-UX-HOME-ADS-MASTER-001 v1.0.1` — blob `372a53199716acd409b691e2c67ed1d56d9200f4`;
17. `docs/product-architecture/ads.md` — `GPA-007 v1.3.0` — blob `91558e7cbf0d1f91904ad2587061a2342f8899c8`.

### 3.8 Business

18. `docs/experience-architecture/public-home-business-source-lock.md` — `GKR-UX-HOME-BUSINESS-SOURCELOCK-001 v1.1.6` — blob `d4f39dee8764fb114c518f6edcddccd292f31e0d`;
19. `docs/experience-architecture/public-home-business-master-document.md` — `GKR-UX-HOME-BUSINESS-MASTER-001 v1.1.3` — blob `743032b01301c54bab9912d92c41e290191708cc`;
20. `docs/experience-architecture/public-home-business-conversion-authority-v2.md` — `GKR-UX-HOME-BUSINESS-CONVERSION-002 v1.0.0` — blob `f95d5fa88bbc98d29f57d3defeebaccb734437d3`;
21. `docs/experience-architecture/public-home-business-authority-contracts.md` — `GKR-UX-HOME-BUSINESS-AUTHORITY-001 v1.0.3` — blob `e7979cc8aded2f5e27e0d047cea80f79ed942d1f`;
22. `docs/product-architecture/business.md` — `GPA-004 v1.6.0` — blob `e931780925604d2a8f51e29c3716024cc43d7fec`.

### 3.9 Intelligence

23. `docs/experience-architecture/public-home-intelligence-design-handoff.md` — `GKR-UX-HOME-INTELLIGENCE-HANDOFF-001 v1.1.10` — blob `b677df020cce03a1e4e9bd28bc17144c3e0f7b71`;
24. `docs/experience-architecture/public-home-intelligence-source-lock.md` — `GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001 v1.1.9` — blob `0a2cbb7685ee7d58da705d9a978560bf0b92484e`;
25. `docs/experience-architecture/public-home-intelligence-master-document.md` — `GKR-UX-HOME-INTELLIGENCE-MASTER-001 v0.2.7` — blob `25f3b70a6c84190e410bb82d6c3ed1721c5b12d2`;
26. `docs/experience-architecture/public-home-intelligence-conceptual-architecture.md` — `GKR-UX-HOME-INTELLIGENCE-NARRATIVE-001 v0.2.3` — blob `c5e3342882e59bbeb347c3a4c728425228c47204`;
27. `docs/experience-architecture/public-homes-value-outcome-principle.md` — `GKR-UX-HOMES-OUTCOME-001 v1.0.0` — blob `83b50c25536888eb44299d168d44af7c4d096f05`;
28. `docs/product-architecture/intelligence-product-source-lock.md` — `GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001 v1.0.1` — blob `3300d7ba5751518620fc61fa02561eabef5bf1b6`;
29. `docs/product-architecture/intelligence.md` — `GPA-006 v2.0.1` — blob `0c8211ed5b46942de5fa23e1aa4c52ac1363681d`.

## 4. Resultado da recomputação

```text
CANONICAL SOURCES EXPECTED
→ 29

CANONICAL SOURCES FOUND
→ 29 / 29

COMMON SOURCES
→ 5 / 5

HOME-SPECIFIC UNIQUE SOURCES
→ 24 / 24

SOURCE PIN METHOD
→ DIRECT READ FROM PREPARATION BASE
→ NO V6 PIN REUSE BY INFERENCE
```

## 5. Oito guias operacionais previstos para v7

Se a materialização for posteriormente autorizada, cada Home deverá receber exatamente um `00-LEIA-PRIMEIRO.md` contendo:

1. nome da Home;
2. objetivo do pacote;
3. commit canônico de origem efetivo da emissão;
4. lista exata de fontes, IDs, versões e blobs;
5. ordem de leitura;
6. invariantes;
7. matriz das oito classes operacionais;
8. dados reais necessários;
9. questões abertas;
10. inferências proibidas;
11. liberdade criativa da designer;
12. manual-first;
13. IA opcional;
14. prompt tool-neutral quando aplicável;
15. checklist de autoauditoria;
16. declaração explícita de que nenhum Figma criado pelo GKR é referência.

## 6. Estrutura externa candidata

A estrutura prevista é:

```text
GUIVOS-HOMES-DESIGN-HANDOFF-v7/
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
29 CANONICAL SOURCES
+
8 READ-FIRST GUIDES
=
37 EXPECTED EXTERNAL FILES
```

## 7. Revalidation gates before any materialization

A materialização v7 somente pode ser considerada após:

- 29/29 fontes confirmadas;
- path / ID / version / blob reconciliados;
- common-authority chain sem contradição operacional;
- Semantic Validation = SUCCESS no HEAD final;
- Mechanical Validation = SUCCESS no HEAD final;
- revisão independente limpa no HEAD exato;
- zero finding material aberto;
- decisão humana separada autorizando materialização.

## 8. Regra de imutabilidade

```text
V6 SNAPSHOT
→ DO NOT MODIFY
→ delivery/design-handoff-v6 REMAINS FROZEN

V7 CANDIDATE
→ DOCUMENTARY PREPARATION ONLY

delivery/design-handoff-v7
→ NOT CREATED
→ NOT AUTHORIZED YET
```

## 9. Revalidation and post-merge evidence

A revalidação documental final do candidato foi concluída no HEAD exato `0418b219d4d4a746498cf8b8032b5018f333e29e` e integrada em `main` pela PR #405.

```text
CANONICAL SOURCES
→ 29 / 29 CONFIRMED

COMMON-AUTHORITY CHAIN
→ HANDOFF 1.6.3
→ GENINPUT 2.2.15
→ READINESS 1.2.15
→ FLOW 3.0.2
→ RELEASE 1.2.0

FINAL PRE-MERGE HEAD
→ 0418b219d4d4a746498cf8b8032b5018f333e29e

SEMANTIC #1463
→ SUCCESS

MECHANICAL #1689
→ SUCCESS

INDEPENDENT CODEX REVIEW
→ CLEAN / NO MAJOR ISSUES
→ REVIEWED COMMIT 0418b219d4

PR #405
→ MERGED

MERGE COMMIT / MAIN
→ 574814b561a933291fd3e7539f814f4187398277

POST-MERGE SOURCE PIN RECHECK
→ 29 / 29 EXACT MATCH

delivery/design-handoff-v7
→ NOT PRESENT

OPEN REVIEW THREADS AT FINAL REVIEWED HEAD
→ 0

REVALIDATION RESULT
→ PASS

MATERIALIZATION
→ NOT AUTHORIZED BY REVALIDATION OR MERGE
→ REQUIRES SEPARATE EXPLICIT HUMAN ACT
```

## 10. Estado

```text
V7 CANDIDATE
→ PREPARED / REVALIDATED
→ MERGED INTO MAIN BY PR #405
→ NON-NORMATIVE
→ REVALIDATION PASS
→ 29 / 29 CANONICAL SOURCES CONFIRMED
→ POST-MERGE 29 / 29 SOURCE PINS RECONFIRMED
→ SEMANTIC #1463 = SUCCESS
→ MECHANICAL #1689 = SUCCESS
→ INDEPENDENT CODEX REVIEW = CLEAN / NO MAJOR ISSUES
→ FINAL REVIEWED HEAD = 0418b219d4d4a746498cf8b8032b5018f333e29e
→ MAIN = 574814b561a933291fd3e7539f814f4187398277

CURRENT EXTERNAL SOURCE PACKAGE
→ NONE

MATERIALIZATION
→ DECISION PENDING
→ SEPARATE HUMAN-GOVERNED ACT
→ NOT AUTHORIZED BY REVALIDATION

DESIGN PRODUCTION RELEASE
→ GRANTED AS HUMAN AUTHORITY
→ OPERATIONAL EXECUTION STILL PAUSED

AI
→ OPTIONAL / DESIGNER-CONTROLLED

GKR-CREATED FIGMA
→ NONE

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```
