---
id: GKR-UX-HOMES-DESIGN-DELIVERY-V6-SNAPSHOT-001
title: Homes Públicas — Registro do Snapshot Externo de Design v6
status: active
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-09-19
parent: GKR-UX-HOMES-DESIGN-DELIVERY-001
depends_on:
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-SOURCE-COMPLETENESS-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V6-CANDIDATE-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
related:
  - GKR-UX-HOMES-DESIGN-DELIVERY-V5-SNAPSHOT-001
normative: false
maturity: design_delivery_v6_snapshot_emitted_validated_current
---

# Homes Públicas — Registro do Snapshot Externo de Design v6

## 1. Finalidade

Este registro fecha o ato humano separado de emissão/materialização do pacote v6 após a integração da PR #397.

Ele registra um fato operacional reproduzível: o pacote externo das oito Homes foi materializado para uso pela designer, com execução manual first-class e IA opcional. O ato não cria nova arquitetura, não produz Design, não cria Figma e não libera Product Engineering.

## 2. Checkpoint canônico de origem

```text
repository
→ guivos-repositorio/Guivos-Knowledge-Repository

main canônica de origem
→ 52f1dade6d7bfcd8c1e5d1b567d7125ac725018f

PR de fontes integrada
→ #397

final reviewed head da PR #397
→ 7ca0857587f87f982ea53c2ce1719c1a0ed831b6

Semantic #1404
→ SUCCESS

Mechanical #1633
→ SUCCESS

Codex re-review
→ CLEAN / NO MAJOR ISSUES
```

## 3. Snapshot externo materializado

```text
branch
→ delivery/design-handoff-v6

snapshot commit
→ b7fe5d62cef444c8316c66edd8ac73b703698a4a

snapshot tree
→ 61eef7447fc5c6b36890ccb774f7011615a6abca

parent canônico
→ 52f1dade6d7bfcd8c1e5d1b567d7125ac725018f
```

O snapshot commit possui como pai direto o checkpoint canônico de origem. A branch externa contém somente o pacote de distribuição; ela não é uma cópia operacional do GKR nem fonte canônica paralela à `main`.

## 4. Composição confirmada

```text
COMMON SOURCES
→ 5

HOME-SPECIFIC UNIQUE SOURCES
→ 24

CANONICAL SOURCES
→ 29

READ-FIRST GUIDES
→ 8

TOTAL EXTERNAL FILES
→ 37

EXTRA BLOBS
→ 0
```

As oito Homes são Pessoa, Organizações e Coletivos, Mall, Travel, Media, Ads, Business e Intelligence.

## 5. Prova de integridade das 29 fontes

As 29 fontes canônicas reutilizam diretamente os blobs do checkpoint `52f1dade6d7bfcd8c1e5d1b567d7125ac725018f`.

```text
CANONICAL SOURCES
→ 29 / 29 PRESENT

MAIN BLOB × SNAPSHOT BLOB
→ 29 / 29 EXACT MATCH

MISMATCHES
→ 0

REWRITE / SUMMARY / ADAPTATION OF CANONICAL SOURCES
→ NONE
```

Os nomes externos de arquivo organizam o pacote; não alteram ID, versão ou conteúdo das autoridades.

## 6. Validação dos oito guias

Cada Home possui exatamente um `00-LEIA-PRIMEIRO.md`.

Os guias preservam:

- Home e objetivo;
- checkpoint canônico de origem;
- lista exata de fontes, IDs, versões e blobs;
- ordem de leitura;
- resumo operacional sem criar autoridade;
- matriz das oito classes;
- dados reais necessários;
- questões abertas;
- inferências proibidas;
- liberdade criativa;
- manual-first;
- IA opcional/designer-controlled;
- prompt tool-neutral;
- checklist de autoauditoria;
- ausência de Figma criado pelo GKR como referência.

As classes são `CANONICAL`, `DESIGN_CREATIVE`, `CONTENT_CANDIDATE`, `DESIGN_HYPOTHESIS`, `PROTOTYPE_PLACEHOLDER`, `REAL_DATA_REQUIRED`, `OPEN_QUESTION` e `PROHIBITED_INFERENCE`.

## 7. Estrutura do pacote

```text
00-COMUM/
→ 5 autoridades comuns

01-HOME-PESSOA/
02-HOME-ORGANIZACOES-E-COLETIVOS/
03-HOME-MALL/
04-HOME-TRAVEL/
05-HOME-MEDIA/
06-HOME-ADS/
07-HOME-BUSINESS/
08-HOME-INTELLIGENCE/
```

Cada diretório de Home contém seu `00-LEIA-PRIMEIRO.md` e somente as fontes específicas autorizadas para aquele contexto.

## 8. Contrato de criação preservado

```text
DESIGNER
→ CREATIVE AUTHOR
→ MANUAL FIRST-CLASS

AI
→ OPTIONAL / DESIGNER-CONTROLLED

GKR
→ SEMANTIC / FUNCTIONAL / EVIDENCE SOURCE OF TRUTH

VISUAL IDENTITY
→ DESIGN-OWNED

GKR-CREATED FIGMA
→ NONE
```

Tipografia, paleta, imagem, composição, grid, motion, iconografia, componentes, atmosfera e direção visual permanecem sob autoria da designer, dentro dos limites das fontes.

## 9. Formato e transporte

```text
GIT SNAPSHOT V6
→ REPRODUCIBLE PACKAGE AUTHORITY

MARKDOWN
→ PRIMARY HUMAN + AI SOURCE FORMAT

ZIP
→ OPTIONAL TRANSPORT ONLY

PDF
→ OPTIONAL HUMAN READING AID ONLY
```

Nenhum ZIP ou PDF substitui o snapshot Git.

## 10. Mudança após a emissão

```text
NON-MATERIAL SOURCE CHANGE
→ RECORDED REVIEW MAY PRESERVE PACKAGE

MATERIAL SOURCE CHANGE
→ AFFECTED HOME INVALIDATED FOR NEW EXECUTION
→ REISSUE / REVALIDATE
```

Mudança criativa da designer que não altera contrato semântico não exige reemissão.

## 11. Preservação das emissões anteriores

```text
v1 → delivery/design-handoff-v1
v2 → delivery/design-handoff-v2
v3 → delivery/design-handoff-v3
v4 → delivery/design-handoff-v4
v5 → delivery/design-handoff-v5
v6 → delivery/design-handoff-v6
```

O v6 não reescreve snapshots anteriores. O v5 permanece congelado como proveniência histórica.

## 12. Limites

A emissão v6 não autoriza automaticamente:

- Product Engineering;
- frontend/backend;
- publicação/deploy;
- nova arquitetura de produto;
- Marketing/GTM;
- high-fidelity autenticado O/C;
- UXA-102/V5;
- qualquer Figma produzido pelo GKR.

O Design Production Release já estava concedido separadamente para produção externa pela designer e permanece válido.

## 13. Estado

```text
V6 SNAPSHOT
→ EMITTED / MATERIALIZED / VALIDATED
→ CURRENT EXTERNAL SOURCE PACKAGE

BRANCH
→ delivery/design-handoff-v6

SNAPSHOT COMMIT
→ b7fe5d62cef444c8316c66edd8ac73b703698a4a

SNAPSHOT TREE
→ 61eef7447fc5c6b36890ccb774f7011615a6abca

CANONICAL BLOB PRESERVATION
→ 29 / 29 EXACT MATCH

DESIGN PRODUCTION RELEASE
→ GRANTED

DESIGNER
→ CREATIVE AUTHOR

AI
→ OPTIONAL / DESIGNER-CONTROLLED

GKR-CREATED FIGMA
→ NONE

FINAL DESIGN ACCEPTANCE
→ HUMAN / SEPARATE

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```

## 14. Síntese

> **A emissão externa v6 está materializada e reproduzível em `delivery/design-handoff-v6`, congelada no commit `b7fe5d62cef444c8316c66edd8ac73b703698a4a` e tree `61eef7447fc5c6b36890ccb774f7011615a6abca`, com 29/29 fontes canônicas byte-preservadas, oito guias tool-neutral, 37 arquivos externos, designer como autora criativa, IA opcional e nenhum Figma criado pelo GKR como referência.**
