---
id: GKR-UX-HOMES-INT-BUSINESS-INTEGRATION-ORDER-001
title: Ordem de integração — alternativas para decisão da direção
status: proposed_non_normative
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-11-01
normative: false
---

# Ordem de integração — PR #720 e PR #721

## Checks confirmados

Na consulta de 01/11/2026, os workflows **GKR Semantic State Validation** e **GKR Mechanical Validation** retornaram `completed/success` para os SHAs `857dfce13644d4d0e37cd36964b91be03b0a84de` (Intelligence, PR #720) e `004e4cda6ecd340722a561fbcfd7bb734e461670` (Business B2, PR #721).

Esta comprovação é vinculada aos SHAs consultados. Qualquer reconciliação subsequente requer novas validações.

## Alternativas de sequenciamento

**A — Intelligence → Business B2 (recomendada):** priorizar a deliberação independente de integração da PR #720, mantendo o Manifesto específico desse pacote; se autorizada e integrada, atualizar o pacote da PR #721 sobre a nova main, reconciliar versão/referências e submeter novos checks e autorização de merge separada.

**B — Business B2 → Intelligence:** mesma governança e validações, com ordem invertida.

**C — Suspender definição:** manter ambas em draft/revisão documental até deliberação posterior.

## Restrições

Uma **decisão de ordem não é autorização de merge**. Não realizar merge, rebase operacional, publicação nem execução de produto com base nesta escolha. A versão consolidada de Manifesto segue insumo não normativo. Respeitar GPA-006 v2.0.2, textos/CTA do M07 Business, autoridades e fronteiras de dados.

## Próximo gate

Obter escolha expressa da direção quanto à ordem A/B/C, e autorização separada para o merge específico de cada PR quando todos os controles finais forem atendidos.
