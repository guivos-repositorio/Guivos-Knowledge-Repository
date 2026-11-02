---
id: GKR-PUBLISH-PAGES-DIRECTION-DECISION-20261101
title: Deliberação proposta — separação de merge documental e publicação GitHub Pages
status: proposed_non_normative
version: 0.1.0
owner: GKR Governance
last_updated: 2026-11-01
normative: false
---

# Proposta à direção — política de publicação do GKR

## Contexto
O workflow `.github/workflows/deploy-pages.yml` da `main` possui `push` em `main` e `workflow_dispatch`. Dessa forma, a integração documental pode desencadear publicação sem uma autorização separada. A branch `gh-pages` ainda não demonstrou os adendos Pessoa/O-C da PR #724 nos HTML inspecionados. A causa não está definitivamente confirmada; histórico completo de Actions e Settings → Pages ainda não foram verificados.

## Decisões alternativas

**P1 — Aprovar preparação técnica para publicação sob autorização (recomendada).** Autorizar **somente** criar uma branch/PR técnica candidata para retirar o gatilho `push` da publicação e manter `workflow_dispatch`, após mapear previamente riscos e mecanismos adicionais. **Não autoriza** merge, deploy, acionamento manual, alteração na `main` ou `gh-pages`.

**P2 — Solicitar diagnóstico ampliado antes de preparar PR técnica.** Exigir levantamento completo da origem efetiva do Pages, histórico e permissões dos workflows, e possível controle de ambiente antes de modificar qualquer configuração.

**P3 — Preservar temporariamente o gatilho atual.** Não preparar alteração técnica; manter o risco de disparo automático documentado e submetido a controle administrativo até nova decisão.

## Condição crítica de transição
Mesmo após aprovação de P1, **não realizar merge automático** da PR técnica: o merge que introduzir a alteração poderá executar o workflow `push` ainda vigente no commit anterior ou em avaliação, provocando um deploy não autorizado. É necessário plano de transição verificado (incluindo configurações de Actions/Pages e eventuais controles de ambiente) e uma autorização de merge específica.

## Gates independentes
1. Aprovação de desenho e preparação (P1/P2/P3).
2. Autorização específica para uma alteração técnica ativa e o respectivo merge.
3. Autorização de publicação separada com SHA, escopo, destino e rollback.
4. Validação pós-publicação e registro de evidências.

**Estado:** `policy_options_prepared / no_selection_recorded / no_main_change / no_deploy`.
