---
id: GKR-PUBLISH-PAGES-SYNC-DIAGNOSTIC-20261101
title: Diagnóstico de sincronização main e GitHub Pages após PR 724
status: proposed_non_normative
version: 0.1.0
owner: GKR Governance
last_updated: 2026-11-01
normative: false
---

# Diagnóstico de sincronização documental e publicação

## Evidência confirmada

1. A PR #724 foi integrada à `main` sob autorização específica, commit de merge `9c154e625abee69177d84092c737632b8d12c6ad`.
2. Em `main`, Mestre Pessoa 1.0.9, Mestre O/C 1.0.10, Leia Primeiro Pessoa/O/C 1.0.6, Manifesto 7.0.57 e Source Lock generativo 2.3.19 têm referências coerentes.
3. A branch `gh-pages` existe e contém os HTML de ambos os Documentos Mestres, mas as passagens novas de Pessoa e O/C integradas pela PR #724 **não foram localizadas** nos respectivos HTML durante a verificação.
4. O `mkdocs.yml` aponta corretamente os oito Documentos Mestres na navegação. `requirements.txt` contém `mkdocs-material`, `mkdocs-mermaid2-plugin` e `mkdocs-print-site-plugin`.
5. O workflow confirmado `.github/workflows/gkr-mechanical-validation.yml` é acionado por `pull_request` ou `workflow_dispatch`, e utiliza `permissions: contents: read`; não constitui, por si, prova de publicação.
6. Não foi possível inspecionar diretamente a versão navegável do site nesta sessão. A comparação é dos arquivos do repositório.

## Diagnóstico

**Divergência de artefatos de publicação confirmada** para os dois Mestres, por ausência dos novos textos em `gh-pages`. A causa raiz não está demonstrada: configurações efetivas do GitHub Pages, workflow de deploy, estado do job, fonte de Pages, gatilhos e eventuais bloqueios exigem conferência adicional. Não presumir que o HTML de `gh-pages` seja a única fonte utilizada pelo site sem verificar a configuração do Pages.

## Plano de restauração — sujeito a autorização separada

**G0 — Inspeção (não publica):** identificar configuração efetiva Pages (branch ou GitHub Actions), workflow responsável, SHA e horário do último deploy, permissões de escrita e logs. Comparar `main`, `gh-pages` e a URL pública. Anotar evidências.

**G1 — Preparação local controlada (não publica):** a partir do SHA autorizado da `main`, executar em ambiente isolado `mkdocs build --strict` com dependências fixadas; conferir links, navegação, assets e presença dos seis adendos no HTML gerado. Não enviar artefatos públicos.

**G2 — Solicitação de publicação:** submeter à direção a fonte exata, SHA, destino, método de deploy, critérios de rollback e provas de G0/G1. Aprovação de merge documental **não equivale** a autorização de publicação.

**G3 — Deploy autorizado:** somente após autorização explícita, publicar via mecanismo configurado; conferir site, integridade, cache e referências, preservar registro do SHA e possibilidade de reversão.

## Não autorização

Este documento **não** autoriza workflow de deploy, push em `gh-pages`, alteração de configuração de Pages, publicação, implantação, execução de aplicativo, nem merge deste diagnóstico.

**Estado:** `source_main_updated / gh_pages_html_outdated_for_person_oc / root_cause_pending / publish_not_authorized`.
