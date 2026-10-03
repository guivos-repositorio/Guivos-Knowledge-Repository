---
id: GKR-UXA-090-PR-CHECKPOINT-001
title: Checkpoint Governado do PR da UXA-090
status: draft
version: 1.0.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-07
depends_on:
  - UXA-090
  - GKR-STATE-001
related:
  - M7.77
normative: false
---

# Checkpoint Governado do PR da UXA-090

## 1. Baseline

- repositório: `guivos-repositorio/Guivos-Knowledge-Repository`;
- base: `main`;
- base SHA: `1ecfd4df0d7ee5f3cd407a2323ed210f230d3e6b`;
- branch: `agent/uxa-090-integrated-collective-request-handoffs-validation`;
- modo pretendido: **PR rascunho, sem merge**.

## 2. Escopo controlado

A branch valida integralmente `GKR-TRN-105`, `106`, `107`, `109` e `112`, formalizando identidade, estado canônico, autoridade, dados, concorrência e efeito lógico único.

`GKR-TRN-108` permanece parcial e `GKR-SURF-PER-106` permanece ausente.

## 3. Preservações

Permanecem fora do escopo:

- materialização de `PER-106`, `PER-107` e `PER-108`;
- `COL-004` a `COL-008`;
- promoção da Jornada do Coletivo;
- novos SVGs, superfícies ou transições;
- Resultados Empresariais;
- protótipo, teste com pessoas e Engenharia de Produto;
- UXA-091.

## 4. Gates obrigatórios

Após abertura do PR rascunho deverão concluir com sucesso:

1. `GKR Semantic State Validation`;
2. `GKR Mechanical Validation`, incluindo front matter, IDs, links, navegação, whitespace, `mkdocs build --strict` e árvore rastreada limpa.

Este checkpoint não autoriza ready-for-review ou merge. Uma decisão separada será necessária após os gates.
