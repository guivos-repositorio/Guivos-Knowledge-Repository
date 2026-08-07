---
id: GKR-UXA-088-PR-CHECKPOINT-001
title: Checkpoint Governado do PR da UXA-088
status: draft
version: 1.0.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-07
depends_on:
  - UXA-088
  - GKR-STATE-001
related:
  - M7.75
normative: false
---

# Checkpoint Governado do PR da UXA-088

## 1. Baseline

- repositório: `guivos-repositorio/Guivos-Knowledge-Repository`;
- base: `main`;
- base SHA: `8d9885ad2dfddd57164ebfb56ad0dd2b9eca6693`;
- branch: `agent/uxa-088-collective-request-management-materialization`;
- modo de integração pretendido nesta etapa: **PR rascunho, sem merge**.

## 2. Escopo controlado

A branch materializa exclusivamente `GKR-SURF-COL-003 — gestão de solicitações` com sete SVGs desktop e sincroniza os instrumentos documentais afetados.

Não são criados novos IDs de superfície ou transição.

## 3. Preservações

Permanecem fora do escopo:

- validação funcional dos sete estados;
- `GKR-SURF-PER-106`, `PER-107` e `PER-108`;
- `GKR-SURF-COL-004` a `COL-008`;
- promoção da Jornada do Coletivo;
- Resultados Empresariais;
- protótipo, teste com pessoas e Engenharia de Produto;
- UXA-089.

## 4. Gates obrigatórios do PR

Após abertura do PR rascunho deverão concluir com sucesso:

1. `GKR Semantic State Validation`;
2. `GKR Mechanical Validation`, incluindo front matter, IDs, links, navegação, whitespace, `mkdocs build --strict` e árvore rastreada limpa.

Este checkpoint não autoriza ready-for-review ou merge. Uma decisão separada será necessária após os gates.
