---
id: GKR-UX-HOMES-DESIGN-DELIVERY-V8-CANDIDATE-001
title: Homes Públicas — Pacote v8 Candidato para Reemissão e Revalidação
status: draft
version: 0.3.0
owner: Experience Architecture
last_updated: 2026-09-20
normative: false
maturity: reissue_candidate_realized_by_v8_snapshot
depends_on:
  - GKR-UX-HOMES-DESIGN-SOURCE-COMPLETENESS-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
related:
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V7-CANDIDATE-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V7-SNAPSHOT-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V8-SNAPSHOT-001
---

# Homes Públicas — Pacote v8 Candidato para Reemissão e Revalidação

## 1. Finalidade

Este documento preserva a proveniência do candidato que deu origem ao pacote externo v8 das oito Homes após a invalidação do snapshot v7 para nova execução.

A materialização foi posteriormente autorizada e executada em `delivery/design-handoff-v8`, registrada por `GKR-UX-HOMES-DESIGN-DELIVERY-V8-SNAPSHOT-001 v1.0.0`. Este documento continua não normativo e não substitui o registro do snapshot v8 nem as autoridades `Manifest + Current State`.

O candidato v8 foi usado para revalidar a composição externa contra a cadeia comum final package-state agnostic integrada pela PR #407.

```text
PREPARATION BASE / MAIN
→ b660503a5da5ec5214e3e2c0eba1f1b06daa9489

PR #407
→ CLOSED / MERGED
→ FINAL REVIEWED HEAD 937c8f44428a7a2a8620740792b57728098ad2f6
→ MERGE COMMIT b660503a5da5ec5214e3e2c0eba1f1b06daa9489

V7
→ MATERIALIZED / INTEGRITY-VALIDATED
→ FROZEN / HISTORICAL
→ INVALID FOR NEW EXECUTION

V8
→ CANDIDATE PREPARED / REVALIDATED
→ SUBSTANTIVE REVALIDATION PASS
→ REALIZED BY MATERIALIZED SNAPSHOT

CURRENT EXTERNAL SOURCE PACKAGE
→ GOVERNED BY MANIFEST + CURRENT STATE
→ V8 DESIGNATION RECORDED BY SNAPSHOT REGISTRATION

delivery/design-handoff-v8
→ MATERIALIZED / INTEGRITY-VALIDATED
→ commit d7eea909b1b5cb6266d7c4a725657ccd909f0e63
→ tree 17553412f24d7a97287ddc5944b8622ecf744534
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

O/C HIGH-FIDELITY
→ NOT AUTHORIZED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```

## 3. Composição candidata v8 — 29 fontes canônicas

Cada pin abaixo foi recalculado diretamente no commit canônico de preparação `b660503a5da5ec5214e3e2c0eba1f1b06daa9489`.

### 3.1 Fontes comuns

1. `docs/experience-architecture/public-homes-design-handoff.md` — `GKR-UX-HOMES-DESIGN-HANDOFF-001 v1.6.5` — blob `6066f2b03653612d6620eba752766e6184b3f429`;
2. `docs/experience-architecture/public-homes-generative-source-lock-and-prompt-template.md` — `GKR-UX-HOMES-GENINPUT-001 v2.2.17` — blob `e2b070a6aaff7a251f2945e4e0740d39f5dd291b`;
3. `docs/experience-architecture/public-homes-design-production-readiness-and-figma-contract.md` — `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001 v1.2.17` — blob `ad73438ceef04e6e705a899c9bf0011ea06722f2`;
4. `docs/experience-architecture/public-homes-design-delivery-operational-flow.md` — `GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001 v3.0.3` — blob `fd735458523c48a2956164a03fdff26f9464e112`;
5. `docs/experience-architecture/public-homes-design-production-release.md` — `GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001 v1.2.1` — blob `a8d8c24e1da04bcb502872874dc5e104bd4bb81f`.

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

COMMON AUTHORITY CHAIN
→ HANDOFF 1.6.5
→ GENINPUT 2.2.17
→ READINESS 1.2.17
→ FLOW 3.0.3
→ RELEASE 1.2.1

SOURCE PIN METHOD
→ DIRECT READ FROM PREPARATION BASE
→ NO V7 PIN REUSE BY INFERENCE
```

## 5. Estrutura externa realizada

A materialização v8 autorizada foi executada com a seguinte estrutura:

```text
00-COMUM/
→ 5 AUTHORITIES

01-HOME-PESSOA/
02-HOME-ORGANIZACOES-E-COLETIVOS/
03-HOME-MALL/
04-HOME-TRAVEL/
05-HOME-MEDIA/
06-HOME-ADS/
07-HOME-BUSINESS/
08-HOME-INTELLIGENCE/
```

```text
29 CANONICAL SOURCES
+
8 READ-FIRST GUIDES
=
37 EXTERNAL FILES
```

Os oito guias registram o checkpoint efetivo de emissão, os 29 pins aplicáveis e a mesma precedência designer-first / IA opcional.

## 6. Revalidation gates satisfeitos antes da materialização

A materialização v8 foi executada somente após:

- 29/29 fontes confirmadas;
- path / ID / version / blob reconciliados;
- common-authority chain sem contradição operacional;
- Semantic Validation = SUCCESS no HEAD final do candidato;
- Mechanical Validation = SUCCESS no HEAD final do candidato;
- revisão independente limpa no HEAD exato;
- zero finding material aberto;
- decisão humana separada autorizando materialização.

## 7. Evidência de revalidação substantiva

A primeira revalidação integral do candidato v8 foi concluída no HEAD exato `539b9b9503e09863cb421e2432fca3fca40871f7`.

```text
CANONICAL SOURCES
→ 29 / 29 CONFIRMED

COMMON AUTHORITY CHAIN
→ HANDOFF 1.6.5
→ GENINPUT 2.2.17
→ READINESS 1.2.17
→ FLOW 3.0.3
→ RELEASE 1.2.1

REVIEWED HEAD
→ 539b9b9503e09863cb421e2432fca3fca40871f7

SEMANTIC #1498
→ SUCCESS

MECHANICAL #1721
→ SUCCESS

INDEPENDENT CODEX REVIEW
→ CLEAN / NO MAJOR ISSUES
→ REVIEWED COMMIT 539b9b9503

OPEN REVIEW THREADS
→ 0

SUBSTANTIVE REVALIDATION RESULT
→ PASS
→ EVIDENCE HEAD 539b9b9503e09863cb421e2432fca3fca40871f7

FINAL DOCUMENTARY HEAD VALIDATION
→ EXTERNAL PR GATE
→ STATUS MUST NOT BE SELF-ASSERTED INSIDE THIS FILE
→ READ FROM PR #408 EXACT-HEAD GATES / REVIEW EVIDENCE

CURRENT EXTERNAL SOURCE PACKAGE
→ GOVERNED BY MANIFEST + CURRENT STATE

delivery/design-handoff-v8
→ MATERIALIZED / INTEGRITY-VALIDATED
→ FROZEN

MATERIALIZATION
→ SEPARATE HUMAN-GOVERNED ACT
→ EXPLICITLY AUTHORIZED
→ EXECUTED FROM main 00791d1e09b5e75b33c223e38164eeee1be0c6cd
```

## 8. Regra de imutabilidade

```text
V6
→ DO NOT MODIFY
→ FROZEN / HISTORICAL

V7
→ DO NOT MODIFY
→ FROZEN / HISTORICAL
→ INVALID FOR NEW EXECUTION

V8 CANDIDATE
→ NON-NORMATIVE PROVENANCE
→ REALIZED BY V8 SNAPSHOT

delivery/design-handoff-v8
→ DO NOT MODIFY
→ FROZEN
```

## 9. Estado

```text
V8 CANDIDATE
→ PREPARED / REVALIDATED
→ NON-NORMATIVE PROVENANCE
→ 29 / 29 SOURCE PINS RECALCULATED
→ SUBSTANTIVE REVALIDATION PASS
→ REALIZED BY GKR-UX-HOMES-DESIGN-DELIVERY-V8-SNAPSHOT-001

CURRENT EXTERNAL SOURCE PACKAGE
→ GOVERNED BY MANIFEST + CURRENT STATE
→ V8 SNAPSHOT DESIGNATION

MATERIALIZATION
→ AUTHORIZED / EXECUTED
→ branch delivery/design-handoff-v8
→ commit d7eea909b1b5cb6266d7c4a725657ccd909f0e63
→ tree 17553412f24d7a97287ddc5944b8622ecf744534

DESIGN PRODUCTION RELEASE
→ GRANTED AS HUMAN AUTHORITY
→ OPERATIONAL EXECUTION REQUIRES VALID CURRENT PACKAGE

AI
→ OPTIONAL / DESIGNER-CONTROLLED

GKR-CREATED FIGMA
→ NONE

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```
