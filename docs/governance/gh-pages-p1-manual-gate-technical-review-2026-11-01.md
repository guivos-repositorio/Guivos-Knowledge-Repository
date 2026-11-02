---
id: GKR-PUBLISH-PAGES-P1-IMPLEMENTATION-REVIEW-20261101
title: Decisão P1 — candidato técnico de gatilho manual do GitHub Pages
status: approved_preparation_only
version: 0.1.0
owner: GKR Governance
last_updated: 2026-11-01
normative: false
---

# Registro de P1 e revisão técnica do gatilho

A direção da Guivos aprovou expressamente a alternativa P1, **exclusivamente para preparação e revisão documental/técnica**. Não autorizou merge, publicação, implantação ou execução operacional.

## Diff técnico mínimo
O candidato em `.github/workflows/deploy-pages.yml` remove `on.push.branches: [main]` e preserva apenas `on.workflow_dispatch`. O build MkDocs, `gh-deploy`, destino `gh-pages` e permissões ficam inalterados nesta proposta. Uma comparação textual confirmou que o gatilho é a única diferença no arquivo do workflow.

## Risco de transição não resolvido
O merge dessa PR pode acionar um deploy enquanto o gatilho `push` da versão vigente ainda estiver ativo. **Não fazer merge da PR com o pipeline atual sem conferir e implementar uma estratégia de transição segura**, com inspeção de Actions, Pages, ambientes e controles pertinentes. O risco não é eliminável apenas com o diff proposto.

## Aceites pendentes
1. Conferir todos os mecanismos de publicação e Settings → Pages.
2. Conferir o histórico completo de execução e permissões.
3. Demonstrar um procedimento de transição sem publicação não autorizada.
4. Validar o SHA candidato e obter uma **nova autorização específica de merge**.
5. Separadamente, obter autorização de publicação com SHA, destino e rollback.

**Estado:** `P1_approved_preparation / draft_workflow_candidate / transition_gate_open / no_merge_no_deploy`.
