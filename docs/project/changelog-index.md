---
id: GKR-CHANGELOG-INDEX-001
title: Índice de Changelogs e Registros de Atualização
status: active
version: 1.2.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-07
depends_on:
  - GKR-STATE-001
related:
  - GKR-SEMANTIC-SYNC-001
  - GKR-P0-REBASELINE-001
  - GKR-P1-REBASELINE-001
  - GKR-CHANGELOG-UXA-085-001
normative: false
---

# Índice de Changelogs e Registros de Atualização

## 1. Finalidade

Este índice organiza os registros de atualização recentes sem reescrever o ledger histórico preservado no `CHANGELOG.md` da raiz.

Changelogs registram alterações. Eles não substituem `GKR-STATE-001`, autoridades de domínio, decisões arquiteturais ou evidências de integração.

## 2. Baseline vigente

- [Registro do Estado Atual — 2.11.0 e M7.72](current-state-register.md)
- [Rebaseline do P0 após UXA-084](p0-post-uxa084-rebaseline-2026-08-06.md)
- [Rebaseline do P1 após UXA-084](p1-post-uxa084-rebaseline-2026-08-06.md)
- [Registro da reconstrução do P1](changelog-p1-post-uxa084-2026-08-06.md)
- [UXA-085 — Promoção Controlada da Galeria](changelog-uxa-085-2026-08-07.md)

Os documentos do P0 datados de 5 de agosto de 2026 permanecem fotografias históricas e devem ser lidos sob a qualificação do rebaseline pós-UXA-084.

## 3. Sequência versionada publicada

- [1.62.0 — Opportunity Boost](changelog-1.62.0-opportunity-boost.md)
- [1.63.0 — UXA-039](changelog-1.63.0-uxa-039.md)
- [1.64.0 — UXA-040](changelog-1.64.0-uxa-040.md)
- [1.65.0 — UXA-041](changelog-1.65.0-uxa-041.md)
- [1.66.0 — UXA-042](changelog-1.66.0-uxa-042.md)
- [1.67.0 — UXA-043](changelog-1.67.0-uxa-043.md)
- [1.68.0 — UXA-044](changelog-1.68.0-uxa-044.md)
- [1.69.0 — UXA-045](changelog-1.69.0-uxa-045.md)
- [1.70.0 — UXA-046](changelog-1.70.0-uxa-046.md)

A ausência de um changelog individual neste índice não invalida um incremento integrado. A comprovação de execução continua no Git, no documento da frente, no Registro do Estado Atual e no pull request correspondente.

## 4. Regra de continuidade

Novos registros deverão:

1. identificar o pacote e a baseline;
2. separar mudança de estado de manutenção documental;
3. preservar a autoridade de `GKR-STATE-001`;
4. informar limites e itens fora do escopo;
5. vincular validações e decisão de integração;
6. evitar declarar execução não comprovada.

## 5. Estado deste índice

| Elemento | Estado |
|---|---|
| ledger raiz | preservado como histórico legado |
| índice atual | ativo |
| estado transversal | `GKR-STATE-001` 2.11.0 |
| marco | M7.72 |
| última UXA integrada após merge | UXA-085 |
| próxima UXA | UXA-086, não iniciada |
| mudança arquitetural por este índice | nenhuma |
