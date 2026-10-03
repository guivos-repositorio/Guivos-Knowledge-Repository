---
id: GKR-UXA-089-PR-CHECKPOINT-001
title: Checkpoint Governado do PR da UXA-089
status: draft
version: 1.0.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-07
depends_on:
  - UXA-089
  - GKR-STATE-001
related:
  - M7.76
normative: false
---

# Checkpoint Governado do PR da UXA-089

## 1. Baseline

- repositório: `guivos-repositorio/Guivos-Knowledge-Repository`;
- base: `main`;
- base SHA: `654c044ed998e3e434de88d8c492c91f49887421`;
- branch: `agent/uxa-089-collective-request-management-functional-validation`;
- modo de integração pretendido nesta etapa: **PR rascunho, sem merge**.

## 2. Escopo controlado

A branch valida funcionalmente `GKR-SURF-COL-003 — gestão de solicitações`, reformula seis dos sete SVGs existentes e sincroniza os instrumentos documentais afetados.

Não são criados novos SVGs, IDs de superfície ou transições.

## 3. Preservações

Permanecem fora do escopo:

- validação ponta a ponta de `GKR-TRN-105`, `106`, `107`, `109` e `112`;
- fechamento de `GKR-TRN-108` enquanto `PER-106` estiver ausente;
- `GKR-SURF-PER-106`, `PER-107` e `PER-108`;
- `GKR-SURF-COL-004` a `COL-008`;
- promoção da Jornada do Coletivo;
- Resultados Empresariais;
- protótipo, teste com pessoas e Engenharia de Produto;
- UXA-090.

## 4. Gates obrigatórios do PR

Após abertura do PR rascunho deverão concluir com sucesso:

1. `GKR Semantic State Validation`;
2. `GKR Mechanical Validation`, incluindo front matter, IDs, links, navegação, whitespace, `mkdocs build --strict` e árvore rastreada limpa.

Este checkpoint não autoriza ready-for-review ou merge. Uma decisão separada será necessária após os gates.
