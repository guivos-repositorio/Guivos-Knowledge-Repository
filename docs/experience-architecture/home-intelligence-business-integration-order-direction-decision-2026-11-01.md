---
id: GKR-UX-HOMES-INT-BUSINESS-INTEGRATION-ORDER-DECISION-001
title: Decisão da direção — ordem Intelligence antes de Business B2
status: approved_sequencing_only
version: 1.0.0
owner: Direção da Guivos
last_updated: 2026-11-01
normative: false
---

# Decisão da direção — alternativa A

A direção da Guivos selecionou a **alternativa A** na deliberação de sequenciamento entre as PRs #720 e #721.

## Ordem aprovada para análise de integração

1. **Primeira:** PR #720 — Home Guivos Intelligence.
2. **Segunda:** PR #721 — Home Guivos Business B2.

Esta decisão define **exclusivamente a ordem governada de integração futura**. A seleção não autoriza nem executa merge, rebase, publicação, alteração operacional, implantação, testes de capacidade, aprovação de gates ou promoção de documentos à `main`.

## Dependências para execução futura

- Submeter a PR #720 à autorização específica de integração, considerando o estado e checks de seu SHA final.
- Somente após eventual integração **expressamente autorizada** de Intelligence, planejar a reconciliação documental da PR #721 com a nova `main`, sem rebase ou merge automático.
- Reconciliar o Manifesto para evitar sobreposição entre duas propostas originalmente numeradas `7.0.54`; a versão consolidada `7.0.55` permanece alvo condicional, não versão vigente.
- Solicitar checks de novo SHA e decisão independente de integração para Business B2.
- Preservar GPA-006 v2.0.2 como referência normativa designada da Home Intelligence, e manter inalterados textos principais, CTA e autoridades do M07 Business.

## Estado

`integration_order_approved / PR720_first / PR721_second / merge_not_authorized / publication_not_authorized`.
