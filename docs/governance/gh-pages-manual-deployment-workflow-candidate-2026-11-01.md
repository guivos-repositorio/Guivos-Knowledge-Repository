---
id: GKR-PUBLISH-PAGES-MANUAL-WORKFLOW-CANDIDATE-20261101
title: Proposta de publicação manual governada — GitHub Pages
status: proposed_non_normative
version: 0.1.0
owner: GKR Governance
last_updated: 2026-11-01
normative: false
---

# Proposta de separação entre merge documental e publicação

## Estado verificado
O workflow ativo `.github/workflows/deploy-pages.yml` dispara em `push` na `main` e em `workflow_dispatch`; executa `mkdocs build --clean` e `mkdocs gh-deploy --force --clean --remote-branch gh-pages`, com `contents: write`. A busca de runs diretamente pelo SHA de merge da PR #724 devolveu uma lista vazia. **Não foi possível recuperar o histórico completo de GitHub Actions nem as configurações de Settings → Pages pelas ações disponíveis.** Portanto, a causa específica do atraso de publicação permanece não comprovada.

## Mudança candidata do workflow (não executada)
Substituir apenas:
```yaml
on:
  push:
    branches:
      - main
  workflow_dispatch:
```
por:
```yaml
on:
  workflow_dispatch:
```

Com isso, um push ou merge documental deixa de disparar **esse** workflow automaticamente. A manutenção de `workflow_dispatch` permite acionamento manual **somente após autorização formal da direção**, com SHA/escopo, registro de quem autorizou, mecanismo de reversão e verificação pós-deploy. A troca do gatilho não garante isoladamente impedir outros mecanismos de publicação nem comprova que existe ambiente protegido.

## Gates obrigatórios
1. Revisar o inventário integral de workflows e a configuração efetiva de GitHub Pages, distinguindo publicação por branch e por Actions.
2. Deliberar expressamente sobre a mudança do workflow e sua governança; a concordância atual cobre apenas **elaboração da proposta**.
3. Se aprovada, criar PR isolada do workflow com validação sintática e revisão de privilégios, sem executar o deploy.
4. Obter autorização específica de merge da PR de configuração. Avaliar que esse próprio merge, **antes da mudança entrar na main**, pode acionar o gatilho automático ainda vigente: exigir janela segura/controle comprovado antes de integrar.
5. Após controle técnico comprovado, preparar build e inspeção de conteúdo em ambiente isolado.
6. Publicar exclusivamente por autorização separada, após conferir SHA aprovado, destino, método, rollback, logs e URL pública.

## Limites
Não disparar `workflow_dispatch`; não executar `mkdocs gh-deploy`; não modificar `gh-pages`; não alegar bloqueio efetivo de outros pipelines sem auditá-los; não confundir aprovação da documentação com autorização de publicação.

**Estado:** `workflow_manual_only_proposal_prepared / settings_and_runs_pending / no_deploy`.
