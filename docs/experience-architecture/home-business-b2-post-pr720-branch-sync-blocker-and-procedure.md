---
id: GKR-UX-HOME-BUSINESS-B2-POST720-SYNC-001
title: PR #721 — sincronização de histórico pendente após merge da PR #720
status: proposed_non_normative
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-11-01
normative: false
---

# PR #721 — pendência de sincronização com main

## Estado apurado
- PR #720 já integrada à main, merge commit `5c4e0124789a0f8b8bdb62cd1ab4e51b16aab8a9`.
- PR #721 branch `proposal/homes-temporal-ai-compatibility-diagnostic-20261101` contém Manifesto 7.0.55 candidato no commit `4732aa7fb3d630b0905c2d80be59f6f4e346516f`.
- O Manifesto candidato contém Intelligence (Master 0.2.15; Source Lock 1.1.17; Handoff 1.1.18; Leia Primeiro 1.0.10) e Business B2 (Master 1.1.11; Source Lock 1.1.29; Authority Contracts 1.0.12; Leia Primeiro 1.0.20).
- A comparação GitHub ainda indicava `ahead_by: 19`, `behind_by: 16` (antes deste registro).
- Nenhum workflow foi retornado para o commit do Manifesto `4732aa7` no instante da consulta.

## Bloqueio operacional

A ação disponível para **merge de Pull Request** não se aplica à sincronização de `main` na branch de origem. Não foi encontrada ação direta `update branch` ou `merge branch`. Não substituir o histórico com `update_ref(force=true)`; não simular sincronização alterando somente o Manifesto; não tentar merge da PR #721 antes de resolver a divergência.

## Procedimento controlado recomendado

Em ambiente Git autorizado, aplicar merge **de main para a branch de PR #721** (não o inverso) e inspecionar possíveis conflitos:

```bash
git fetch origin main proposal/homes-temporal-ai-compatibility-diagnostic-20261101
git switch proposal/homes-temporal-ai-compatibility-diagnostic-20261101
git merge --no-ff origin/main
# Resolver eventuais conflitos preservando Intelligence já integrado e Business B2 candidato
git diff --check
# Rodar validações mecânica e semântica do GKR, conforme scripts documentados no repositório
git push origin proposal/homes-temporal-ai-compatibility-diagnostic-20261101
```

A execução de merge da base para a branch ainda é **pendente**; comandos são procedimento de referência, não operações realizadas. Caso haja conflito no Manifesto, manter `7.0.55` com a reconciliação das oito referências comprovadas e conferir o restante do conteúdo original. Validar os workflows do **novo head** e o `behind_by=0` antes de propor autorização independente de merge da PR #721.

## Gate

`business_manifest_reconciled / git_history_sync_pending / new_checks_pending / PR721_merge_not_authorized`.
