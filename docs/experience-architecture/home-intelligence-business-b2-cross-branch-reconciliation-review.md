---
id: GKR-UX-HOMES-INT-B2-CROSSBRANCH-001
title: Conciliação cruzada proposta — Intelligence PR 720 e Business B2
status: proposed_non_normative
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-11-01
normative: false
---

# Conciliação cruzada — PR #720 Intelligence e Business B2

## Evidência de sobreposição
As branches `proposal/home-intelligence-temporal-perspectives-20261101` e `proposal/homes-temporal-ai-compatibility-diagnostic-20261101` alteram `docs/experience-architecture/public-homes-design-delivery-manifest.md` independentemente, ambas para `version: 7.0.54`.

| Referência | Branch PR #720 | Branch Business B2 |
| --- | --- | --- |
| Intelligence Master | 0.2.15 | 0.2.14 |
| Intelligence Source Lock | 1.1.17 | 1.1.16 |
| Intelligence Handoff | 1.1.18 | 1.1.17 |
| Business Master | 1.1.10 | 1.1.11 |
| Business Source Lock | 1.1.28 | 1.1.29 |
| Business Authority Contracts | 1.0.11 | 1.0.12 |

## Pendências de versão identificadas
- Manifesto da PR #720 ainda remete a `Intelligence Read First v1.0.9` embora a versão candidata própria seja `1.0.10`.
- Manifesto da branch Business ainda remete a `Business Read First v1.0.19` embora a versão candidata própria seja `1.0.20`.
- A concorrência de `7.0.54` **não** concede autoridade para adotar ambas as alterações automaticamente.

## Estratégia proposta de resolução
1. Preservar as duas branches e a `main` sem merge.
2. Preparar **versão consolidada candidata 7.0.55 ou superior**, somente depois de verificar a versão canônica atual e a ordem de integração aprovada; incluir versões candidatas Intelligence e Business sem misturar suas decisões de autoridade.
3. Atualizar as referências a Leia Primeiro correspondentes em pacote coeso, observando a hierarquia dos Source Locks.
4. Exigir diff e CI da nova branch de reconciliação; registrar eventual conflito de conteúdo versus simples conflito de edição.
5. Solicitar autorização expressa e distinta para cada integração; nenhuma publicação ou operação decorre desta análise.

## Limites
A alternativa A do GPA-006 preserva `v2.0.2` como referência normativa da Home Intelligence, com arquivo físico `2.0.3`. A Business B2 autoriza preparação de versões documentais candidatas e não comprova capacidades prospectivas. Não reabrir textos principais, CTA, dez movimentos Business nem onze movimentos Intelligence sem aprovação distinta.

## Estado
`cross_branch_collision_confirmed / combined_manifest_not_published / integration_not_authorized`.
