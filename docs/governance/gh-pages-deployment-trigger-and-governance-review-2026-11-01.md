---
id: GKR-PUBLISH-PAGES-TRIGGER-REVIEW-20261101
title: Inspeção do gatilho de publicação automática do GitHub Pages
status: proposed_non_normative
version: 0.1.0
owner: GKR Governance
last_updated: 2026-11-01
normative: false
---

# GitHub Pages — mecanismo identificado e risco de governança

## Configuração efetivamente encontrada na main

Arquivo `.github/workflows/deploy-pages.yml`:

- Workflow: `Deploy GKR to GitHub Pages`.
- Evento automático: `on.push.branches: [main]`.
- Evento manual adicional: `workflow_dispatch`.
- Permissões declaradas: `contents: write`.
- Build: `mkdocs build --clean`.
- Publicação em `gh-pages`: `mkdocs gh-deploy --force --clean --remote-branch gh-pages`.

**Implicação:** qualquer push futuro em main pode iniciar uma publicação automática; o merge documental e o deploy não estão tecnicamente separados por este workflow. A direção exige autorização expressa para publicar, portanto é necessário revisar esse acoplamento. Não alterar o workflow nesta auditoria sem decisão específica.

## Evidência de sincronização

- A `main` após PR #724 contém os seis textos aprovados (Pessoa M06/M09/M10; O/C M03/M06/M10).
- Os HTML correspondentes consultados em `gh-pages` não apresentam as novas passagens.
- A consulta de workflow runs pelo SHA do commit de merge `9c154e625abee69177d84092c737632b8d12c6ad` retornou lista vazia. Isso **não demonstra**, por si só, desabilitação, falha ou ausência definitiva do deploy: é necessário consultar o histórico completo do workflow e configurações de Actions/Pages.
- A consulta à página pública via fonte externa não foi bem-sucedida.

## Diagnóstico e verificações ainda necessárias

1. Consultar histórico completo de `Deploy GKR to GitHub Pages`, inclusive runs associados a outros SHAs, estado, permissões, logs e eventuais falhas.
2. Confirmar a origem configurada em Settings → Pages (branch `gh-pages` / root versus GitHub Actions).
3. Confirmar o SHA realmente presente no conteúdo publicado e eventual atraso/cache.
4. Decidir se o deploy deve permanecer automático ou exigir uma autorização específica por `workflow_dispatch` ou gate de aprovação.
5. Caso autorizado, preparar mudança isolada de workflow e validar o comportamento sem acionar publicação nesta fase.
6. Autorização para editar workflow, merge e publicação devem ser atos distintos.

## Estado

`workflow_found_auto_push_main / gh_pages_stale_for_pr724 / root_cause_not_confirmed / no_deploy_authorized`.

Este documento é exclusivamente diagnóstico; não altera o pipeline de produção, o site ou a branch `gh-pages`.
