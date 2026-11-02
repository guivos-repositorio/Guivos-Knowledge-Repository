---
id: GKR-HOMES-PUBLICATION-SYNCHRONIZATION-20261102
title: Regra candidata de sincronização entre documentos em main e GKR publicado
status: proposed_non_normative
version: 0.1.0
owner: GKR Governance
last_updated: 2026-11-02
normative: false
---

# Sincronização obrigatória — proposta para governança

## Diretriz manifestada pela direção
O repositório e o GKR publicado devem avançar alinhados. Uma alteração documental aprovada e integrada à `main` não é considerada integralmente entregue sem conferência da versão publicada correspondente.

## Critério de aceite
1. Confirmar ID, versão e conteúdo do Documento Mestre em `main`.
2. Confirmar as referências cruzadas e Manifesto vigentes.
3. Verificar versão, movimentos e redação na página do GKR publicada.
4. Registrar SHA de origem, evidências e eventuais divergências.
5. Registrar pendência de sincronização sempre que a página pública não refletir a versão aprovada.

## Pendência atual
- Pessoa: Documento Mestre 1.0.9, M06/M09/M10.
- Organizações e Coletivos: Documento Mestre 1.0.10, M03/M06/M10.
- Manifesto Canônico: 7.0.57; Source Lock generativo: 2.3.19.
- Análise anterior encontrou HTML desatualizado na branch `gh-pages`. Exige reconferência após eventual publicação.

## Limite de autorização
A obrigação de sincronizar não deve ser confundida com autorização implícita de execução de `mkdocs gh-deploy`, `workflow_dispatch`, push em `gh-pages` ou mudança técnica de workflow. A direção ainda não autorizou expressamente o ato de publicação desta correção. Uma autorização específica deve identificar fonte/commit, destino e escopo.

## Gate crítico
O workflow atual `.github/workflows/deploy-pages.yml` possui gatilho automático em push da `main`. A PR #725 propõe removê-lo, mas não foi integrada por risco de disparo involuntário durante a transição. A sincronização deve ocorrer por procedimento expressamente autorizado e verificável, sem merge incidental ou alteração de conteúdo.

**Estado:** `sync_policy_candidate_recorded / public_content_gap_open / publish_authorization_pending`.
