---
id: GKR-UX-HOMES-DESIGN-DELIVERY-V7-CANDIDATE-001
title: Homes Públicas — Pacote v7 Candidato para Designer e IA Opcional
status: draft
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-09-20
normative: false
maturity: v7_candidate_pre_snapshot_revalidation
depends_on:
  - GKR-UX-HOMES-DESIGN-SOURCE-COMPLETENESS-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
related:
  - GKR-UX-HOMES-DESIGN-DELIVERY-V6-CANDIDATE-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V6-SNAPSHOT-001
---

# Homes Públicas — Pacote v7 Candidato para Designer e IA Opcional

## 1. Finalidade

Este documento registra o **novo candidato governado pré-snapshot** para reemissão do pacote externo das oito Homes após a invalidação operacional do snapshot v6.

Ele não emite, materializa, publica nem congela um novo snapshot. O objetivo desta etapa é provar a composição exata das fontes que poderão formar uma futura emissão v7 e submetê-la novamente a Semantic, Mechanical e revisão independente antes de qualquer materialização.

```text
V6 SNAPSHOT
→ FROZEN / HISTORICAL
→ INVALID FOR NEW EXECUTION
→ NOT REWRITTEN

CURRENT EXTERNAL SOURCE PACKAGE
→ NONE

V7 CANDIDATE
→ PRE-SNAPSHOT
→ REVALIDATION REQUIRED
→ NOT EMITTED
→ NOT MATERIALIZED

DESIGN PRODUCTION RELEASE
→ GRANTED
→ OPERATIONAL EXECUTION STILL PAUSED UNTIL VALID CURRENT PACKAGE EXISTS

DESIGNER
→ CREATIVE AUTHOR
→ MANUAL FIRST-CLASS

AI
→ OPTIONAL / DESIGNER-CONTROLLED

GKR-CREATED FIGMA
→ NONE

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```

## 2. Checkpoint canônico do candidato

```text
repository
→ guivos-repositorio/Guivos-Knowledge-Repository

ORIGIN MAIN
→ 1a1386bc318afa2e91f5c1ef5ffd3a80e7265cb2

PREDECESSOR SNAPSHOT
→ delivery/design-handoff-v6
→ b7fe5d62cef444c8316c66edd8ac73b703698a4a
→ FROZEN / HISTORICAL / INVALID FOR NEW EXECUTION

POST-V6 COMMON-AUTHORITY REMEDIATION
→ HANDOFF v1.6.3
→ GENINPUT v2.2.15
→ READINESS v1.2.15
→ FLOW v3.0.2
→ RELEASE v1.2.0
```

## 3. Composição candidata — 29 fontes canônicas

| # | Path | Autoridade | Versão | Blob |
|---:|---|---|---|---|
| 1 | `docs/experience-architecture/public-homes-design-handoff.md` | `GKR-UX-HOMES-DESIGN-HANDOFF-001` | `1.6.3` | `0427afa0c99cbfe5189661ef4bea606b1008ec7f` |
| 2 | `docs/experience-architecture/public-homes-generative-source-lock-and-prompt-template.md` | `GKR-UX-HOMES-GENINPUT-001` | `2.2.15` | `e696d73767b77d1346b646bcab6e1af0105af762` |
| 3 | `docs/experience-architecture/public-homes-design-production-readiness-and-figma-contract.md` | `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001` | `1.2.15` | `a087487c98ee133787ea184849d0995b3523f907` |
| 4 | `docs/experience-architecture/public-homes-design-delivery-operational-flow.md` | `GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001` | `3.0.2` | `18a135f717fd90e1fa4a80230f0561d04902bbd1` |
| 5 | `docs/experience-architecture/public-homes-design-production-release.md` | `GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001` | `1.2.0` | `414fb213f44494b00eed09b6dab6c460295cb726` |
| 6 | `docs/experience-architecture/public-home-master-document.md` | `GKR-UX-HOME-MASTER-001` | `1.0.3` | `2c33978024dc98e694c719c4b72b1de76206c4cb` |
| 7 | `docs/experience-architecture/public-home-person-media-editorial-supply-reconciliation.md` | `GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001` | `1.0.0` | `72bb3fcb8a5cdcfa0256a0c789b996085f8c1d7e` |
| 8 | `docs/experience-architecture/public-home-organizations-collectives-master-document.md` | `GKR-UX-HOME-OC-MASTER-001` | `1.0.3` | `adcc030791a50649f44ad95ef75d202e7b61a1d7` |
| 9 | `docs/experience-architecture/public-home-organizations-collectives-media-editorial-supply-reconciliation.md` | `GKR-UX-HOME-OC-MEDIA-SUPPLY-001` | `1.0.0` | `e8aa2e343eba9aa2568ed7219c72a968453c7257` |
| 10 | `docs/experience-architecture/public-home-mall-master-document.md` | `GKR-UX-HOME-MALL-MASTER-001` | `1.1.1` | `c0422565d5da42bff334583203623fb529388226` |
| 11 | `docs/experience-architecture/public-home-mall-media-editorial-supply-reconciliation.md` | `GKR-UX-HOME-MALL-MEDIA-SUPPLY-001` | `1.0.0` | `986cf6bb35cccd71f9ea681836a29e14281dae7c` |
| 12 | `docs/experience-architecture/public-home-travel-master-document.md` | `GKR-UX-HOME-TRAVEL-MASTER-001` | `1.1.3` | `cf1933cab5d1d968d8c2f88525548a8ca11955ff` |
| 13 | `docs/experience-architecture/public-home-travel-media-editorial-supply-reconciliation.md` | `GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001` | `1.0.0` | `77e90af980fe0b315abc6ade079c096ce1755f6f` |
| 14 | `docs/experience-architecture/public-home-media-master-document.md` | `GKR-UX-HOME-MEDIA-MASTER-001` | `1.0.1` | `71f8eae8731ec448a8b513e4f82857399af85c95` |
| 15 | `docs/product-architecture/media.md` | `GPA-005` | `1.2.0` | `59ddb05ffc9b3d6d6e6f27fc405f82e4bc6ee260` |
| 16 | `docs/experience-architecture/public-home-ads-master-document.md` | `GKR-UX-HOME-ADS-MASTER-001` | `1.0.1` | `372a53199716acd409b691e2c67ed1d56d9200f4` |
| 17 | `docs/product-architecture/ads.md` | `GPA-007` | `1.3.0` | `91558e7cbf0d1f91904ad2587061a2342f8899c8` |
| 18 | `docs/experience-architecture/public-home-business-source-lock.md` | `GKR-UX-HOME-BUSINESS-SOURCELOCK-001` | `1.1.6` | `d4f39dee8764fb114c518f6edcddccd292f31e0d` |
| 19 | `docs/experience-architecture/public-home-business-master-document.md` | `GKR-UX-HOME-BUSINESS-MASTER-001` | `1.1.3` | `743032b01301c54bab9912d92c41e290191708cc` |
| 20 | `docs/experience-architecture/public-home-business-conversion-authority-v2.md` | `GKR-UX-HOME-BUSINESS-CONVERSION-002` | `1.0.0` | `f95d5fa88bbc98d29f57d3defeebaccb734437d3` |
| 21 | `docs/experience-architecture/public-home-business-authority-contracts.md` | `GKR-UX-HOME-BUSINESS-AUTHORITY-001` | `1.0.3` | `e7979cc8aded2f5e27e0d047cea80f79ed942d1f` |
| 22 | `docs/product-architecture/business.md` | `GPA-004` | `1.6.0` | `e931780925604d2a8f51e29c3716024cc43d7fec` |
| 23 | `docs/experience-architecture/public-home-intelligence-design-handoff.md` | `GKR-UX-HOME-INTELLIGENCE-HANDOFF-001` | `1.1.10` | `b677df020cce03a1e4e9bd28bc17144c3e0f7b71` |
| 24 | `docs/experience-architecture/public-home-intelligence-source-lock.md` | `GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001` | `1.1.9` | `0a2cbb7685ee7d58da705d9a978560bf0b92484e` |
| 25 | `docs/experience-architecture/public-home-intelligence-master-document.md` | `GKR-UX-HOME-INTELLIGENCE-MASTER-001` | `0.2.7` | `25f3b70a6c84190e410bb82d6c3ed1721c5b12d2` |
| 26 | `docs/experience-architecture/public-home-intelligence-conceptual-architecture.md` | `GKR-UX-HOME-INTELLIGENCE-NARRATIVE-001` | `0.2.3` | `c5e3342882e59bbeb347c3a4c728425228c47204` |
| 27 | `docs/experience-architecture/public-homes-value-outcome-principle.md` | `GKR-UX-HOMES-OUTCOME-001` | `1.0.0` | `83b50c25536888eb44299d168d44af7c4d096f05` |
| 28 | `docs/product-architecture/intelligence-product-source-lock.md` | `GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001` | `1.0.1` | `3300d7ba5751518620fc61fa02561eabef5bf1b6` |
| 29 | `docs/product-architecture/intelligence.md` | `GPA-006` | `2.0.1` | `0c8211ed5b46942de5fa23e1aa4c52ac1363681d` |

## 4. Prova de composição pré-snapshot

```text
CANONICAL SOURCE PATHS
→ 29 / 29 PRESENT

DECLARED ID × ACTUAL ID
→ 29 / 29 MATCH

DECLARED VERSION × ACTUAL VERSION
→ 29 / 29 MATCH

COMMON AUTHORITIES AFTER POST-V6 REMEDIATION
→ 5 / 5 CURRENT

SOURCE STATUS
→ 19 ACTIVE
→ 6 DRAFT
→ 4 CONSOLIDATED
→ NO STATUS PROMOTION PERFORMED BY THIS CANDIDATE

PRIOR SOURCE-COMPLETENESS BASELINE
→ C1–C15 PASS
→ 8 / 8 HOMES
→ 120 / 120

V7 READ-FIRST GUIDES
→ NOT MATERIALIZED YET

PLANNED SNAPSHOT COMPOSITION
→ 29 CANONICAL SOURCES
→ 8 READ-FIRST GUIDES
→ 37 FILES TOTAL
```

Os estados documentais nativos das fontes são preservados. Este candidato não promove documentos `draft` para `active`; ele apenas congela quais revisões seriam consumidas caso uma futura emissão v7 seja autorizada.

## 5. Revalidação exigida antes de snapshot

A prova estrutural acima é necessária, mas não suficiente. O histórico do v6 demonstrou que preservação byte-a-byte e completude estrutural não substituem revisão de coerência operacional.

Antes de qualquer emissão v7 são obrigatórios:

1. Semantic no HEAD final do candidato;
2. Mechanical no mesmo HEAD;
3. revisão independente no mesmo HEAD;
4. adjudicação e remediação de qualquer finding material;
5. Ready for Review como ato separado;
6. merge como ato separado;
7. **somente após integração**, decisão humana separada sobre emissão/materialização do snapshot v7.

```text
EXACT-HEAD SEMANTIC
→ PENDING

EXACT-HEAD MECHANICAL
→ PENDING

INDEPENDENT REVIEW
→ PENDING

V7 SNAPSHOT EMISSION
→ NOT AUTHORIZED BY THIS CANDIDATE

DELIVERY BRANCH
→ NOT CREATED

CURRENT EXTERNAL SOURCE PACKAGE
→ NONE

OPERATIONAL DESIGN EXECUTION
→ PAUSED
```

## 6. Política dos oito guias v7

Os oito `00-LEIA-PRIMEIRO.md` serão materializados apenas se o snapshot v7 for posteriormente autorizado.

Cada guia deverá registrar:

1. Home;
2. objetivo;
3. checkpoint canônico de origem;
4. fontes, IDs, versões e blobs exatos;
5. ordem de leitura;
6. invariantes;
7. oito classes operacionais;
8. dados reais necessários;
9. questões abertas;
10. inferências proibidas;
11. liberdade criativa;
12. manual-first;
13. IA opcional;
14. prompt tool-neutral;
15. autoauditoria;
16. ausência de Figma criado pelo GKR como referência.

O guia não substitui as autoridades listadas.

## 7. Estado

```text
GKR-UX-HOMES-DESIGN-DELIVERY-V7-CANDIDATE-001
→ DRAFT v0.1.0
→ PRE-SNAPSHOT REVALIDATION CANDIDATE

ORIGIN MAIN
→ 1a1386bc318afa2e91f5c1ef5ffd3a80e7265cb2

V6
→ FROZEN / HISTORICAL / INVALID FOR NEW EXECUTION

V7
→ CANDIDATE ONLY
→ NOT EMITTED
→ NOT MATERIALIZED

CURRENT EXTERNAL SOURCE PACKAGE
→ NONE

NEXT GOVERNED GATE
→ EXACT-HEAD SEMANTIC + MECHANICAL
→ INDEPENDENT REVIEW

MATERIALIZATION
→ REQUIRES SEPARATE HUMAN AUTHORIZATION AFTER CANDIDATE INTEGRATION
```
