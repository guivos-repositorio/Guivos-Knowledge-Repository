---
id: GKR-UX-HOME-INTELLIGENCE-GPA006-ADJUDICATION-001
title: Adjudicação documental preliminar da versão GPA-006 para a PR 720
status: proposed_non_normative
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-11-01
normative: false
---

# Adjudicação documental preliminar — GPA-006 × Home Intelligence

## Evidência histórica adicional — origem demonstrada de 2.0.3

O commit [`601f0d6d98767b9dae399dbf0990e3361e8a064b`](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/commit/601f0d6d98767b9dae399dbf0990e3361e8a064b), associado à **PR #566 — Intelligence: contract cross-surface provenance and explainability**, modificou `docs/product-architecture/intelligence.md` da seguinte maneira, segundo o patch recuperado:
- `version: 2.0.2` → `version: 2.0.3`;
- `last_updated: 2026-09-25` → `2026-10-03`;
- acrescentou ao campo `related` a referência `GKR-INTELLIGENCE-SURFACE-PROVENANCE-EXPLAINABILITY-001`.
O patch desse arquivo **não altera a frase de autoridade da seção 1**, que permanece `GPA-006 v2.0.2`. Portanto, a causa imediata da divergência está identificada: **versionamento físico associado à inclusão de uma referência ao contrato de proveniência, sem propagação da versão na declaração interna**.

**Interpretação limitada pela evidência:** o patch indica atualização de metadados e da dependência de proveniência no GPA-006. Ele não constitui por si só decisão formal para promover todos os Source Locks e documentos congelados a `v2.0.3`. A decisão sobre qual versão deve governar as referências canônicas ainda requer reconciliação institucional, embora a origem material da divergência já não seja desconhecida.

## Evidências estáticas verificadas na main
1. `docs/product-architecture/intelligence.md`: frontmatter `version: 2.0.3`, `last_updated: 2026-10-03`; seção 1 declara expressamente a autoridade `GPA-006 v2.0.2`.
2. `docs/product-architecture/intelligence-product-source-lock.md`: `version: 1.0.3`, congelando e referenciando em múltiplos pontos `GPA-006 v2.0.2`, enquanto a fonte de produto tem metadado 2.0.3.
3. Documento Mestre, Home Source Lock, Design Handoff e manifesto de entrega mantêm a referência à autoridade `GPA-006 v2.0.2`, inclusive nas versões candidatas da PR #720.

## Distinção essencial
**Versão do artefato físico ≠ versão da autoridade ratificada.** Uma revisão posterior do frontmatter pode registrar ajustes não normativos ou uma nova autoridade, mas não é possível escolher uma dessas hipóteses apenas com os arquivos lidos. A versão `2.0.3` é comprovada como metadado físico; a versão `2.0.2` é comprovada como declaração textual de autoridade congelada. Não existe base documental suficiente nesta revisão para promover `2.0.3` a versão normativa nem para rebaixar seu frontmatter para `2.0.2`.

## Resultado e critérios de encerramento
**Resultado: divergence_origin_traced / authority_promotion_not_adjudicated.** Manter `GPA-006 v2.0.2` como referência declarada nas autoridades vigentes, **sem afirmar que a divergência está resolvida**.

Antes de integrar PR #720:
- confrontar o commit 601f0d6d e a PR #566 com a decisão/autorização que rege a promoção normativa de metadados do GPA-006;
- diferenciar alteração editorial de alteração normativa e identificar o aprovador e escopo;
- verificar a hierarquia entre GPA-006 e Product Source Lock;
- registrar ato documental competente para eventual correção das referências, nunca por inferência;
- verificar as validações da PR (checks/build) e o manifesto por evidência real;
- preservar a `main` até decisão de integração independente.

## Restrições e localização
Esta análise pertence à **área Experiência e Journey** e não muda os arquivos canônicos de `product-architecture`. Não concede autorização de engenharia, implementação, gates, teste ou publicação. Os demais documentos candidatos permanecem exclusivamente na branch da PR #720.
