---
id: GKR-PAGES-P1-SAFE-TRANSITION-001
title: PR 725 — plano de transição segura antes da alteração do workflow de publicação
status: proposed_non_normative
version: 0.1.0
owner: GKR Governance
last_updated: 2026-11-01
normative: false
---

# Gate de transição segura — PR #725

## Evidências
- PR #725, head `26b784db2dcff968ff85d588b28c1c7bbbdb1e2c`: checks mecânico e semântico concluídos com sucesso; sem divergência da `main` no momento da conferência.
- Workflow vigente `.github/workflows/deploy-pages.yml` está configurado para `push` na `main` e `workflow_dispatch`; executa `mkdocs gh-deploy --force --clean --remote-branch gh-pages`.
- A PR candidata remove somente o gatilho de `push`, preservando `workflow_dispatch`.
- As ferramentas GitHub conectadas nesta sessão não oferecem leitura/alteração das configurações de Actions, Pages ou environments, nem listagem global de runs do workflow. Logo **não há evidência de bloqueio de publicação**.

## Procedimento candidato, SEM EXECUÇÃO
1. Inventariar workflows que podem publicar e confirmar a fonte real de GitHub Pages em configurações administrativas.
2. Avaliar e escolher controle pré-merge com evidência: suspensão temporária do workflow de deploy por administrador autorizado, bloqueio efetivo de publicação por environment/regras, ou outro mecanismo seguro comprovado. A simples edição do workflow na PR não é suficiente.
3. Obter autorização separada para o controle temporário, documentando responsável, alcance, mecanismo de restauração, rollback e evidência de que não houve deploy.
4. Executar o controle somente em etapa expressamente autorizada; verificar que o gatilho automático está efetivamente neutralizado **antes** do merge.
5. Solicitar autorização específica de merge da PR #725 com SHA e checks atualizados; sem autorização, manter draft.
6. Após merge autorizado, confirmar que o workflow final em `main` responde somente a `workflow_dispatch`; avaliar restauração de controles temporários sem disparo automático.
7. Tratar eventual atualização pública do conteúdo da PR #724 como **outro ato**, exigindo autorização de publicação com SHA, conteúdo, destino e rollback.

## Bloqueio
**NÃO MERGEAR PR #725 enquanto o controle pré-merge não estiver comprovado.** Não acionar manualmente workflow, não desabilitar Actions, não escrever em `gh-pages` e não publicar sem autorização independente.

**Estado:** `technical_checks_pass / transition_not_proven / merge_blocked / deploy_not_authorized`.
