---
id: GKR-UX-HOMES-PR720-PR721-RECON-GATE-001
title: Gate documental de reconciliação — PR #720 e PR #721
status: proposed_non_normative
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-11-01
normative: false
---

# Gate de reconciliação — Intelligence PR #720 e Business B2 PR #721

## Situação verificada no GitHub
As branches de ambas as PRs derivam da mesma base da `main` (SHA `8f56b4b9edf92690c1b5e8cd98060080e17fb55e`), ambas alterando `docs/experience-architecture/public-homes-design-delivery-manifest.md` para `7.0.54`.

| Check consultado | PR #720 (SHA 857dfce) | PR #721 (SHA 004e4cd) |
| --- | --- | --- |
| GKR Semantic State Validation | success | success |
| GKR Mechanical Validation | success | in_progress |

**Aprovação do check semântico não libera merge.** Os checks são evidências associadas a SHAs específicos; alterações subsequentes exigem nova validação.

## Conflito e solução documental

Há sobreposição de edição do Manifesto e colisão semântica de versão (duas propostas distintas nomeadas 7.0.54); a existência de conflito textual automático no Git não foi demonstrada pela comparação. A proposta consolidada não normativa `public-homes-consolidated-manifest-candidate-20261101.md` já referencia quatro fontes candidatas de Intelligence e quatro de Business.

Uma solução futura exige:

1. Checar o estado final dos dois PRs, seu head e todos os checks.
2. Obter autorização de integração **independente** para PR #720 e PR #721.
3. Determinar ordem. Se apenas uma for aprovada, preservar no Manifesto corrente somente a trilha autorizada.
4. Após a primeira integração autorizada, atualizar a segunda branch a partir da nova `main`; atualizar as referências e a versão real do Manifesto, em vez de sobrepor `7.0.54`.
5. Aplicar a proposta consolidada somente como insumo de comparação, jamais como substituto automático do Manifesto canônico.
6. Validar os novos SHAs (mecânica, semântica, referências, fronteiras GPA-006 v2.0.2 e Business B2), e solicitar autorização específica para merge seguinte.
7. Tratar publicação e execução operacional como gates separados.

## Restrições de autoridade

As alterações de Business B2 preservam os dez movimentos e o CTA de M07; não declaram função preditiva disponível, causalidade comprovada ou novo acesso a dados pessoais ou corporativos. Intelligence mantém a distinção Guivos Intelligence/Guivos AI e GPA-006 v2.0.2 como autoridade normativa designada pela direção, sem promoção do arquivo físico 2.0.3.

## Parecer

**PR #720: checks confirmados nos SHAs consultados; merge ainda depende de autorização. PR #721: check semântico aprovado; check mecânico ainda pendente no momento da consulta. Conflito documental: plano preparado, execução de resolução condicionada a decisão de ordem e integração.**

Este documento não autoriza merge, publicação, execução operacional ou promoção das versões candidatas.
