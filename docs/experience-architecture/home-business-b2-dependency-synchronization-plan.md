---
id: GKR-UX-HOME-BUSINESS-B2-DEPENDENCY-SYNC-001
title: Business B2 — Handoff aplicável e plano de sincronização documental
status: proposed_non_normative
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-11-01
normative: false
---

# Business B2 — Handoff e plano de sincronização

## Handoff identificado

O Handoff aplicável à Home Business **não é um documento individual** em `public-home-business-design-handoff.md`. O contrato encontrado é o **Handoff Canônico das Oito Homes**:
- `docs/experience-architecture/public-homes-design-handoff.md`
- `GKR-UX-HOMES-DESIGN-HANDOFF-001 v1.7.13` (versão consultada em main)
- **seção 4.7 — Guivos Business**; a seção remete ao pacote específico definido pelo Manifesto vigente.

A composição correta envolve esse Handoff comum, o Manifesto e o conjunto específico Business. **Não criar Handoff individual sem decisão de arquitetura.**

## Referências de estado

| Fonte | Estado vigente consultado | Candidato na branch B2 | Tratamento |
| --- | --- | --- | --- |
| Documento Mestre Business | 1.1.10 | 1.1.11 | adendo M07 não vigente, sem alteração do headline, supporting copy e CTA |
| Business Source Lock | 1.1.28 | 1.1.29 | adendo não vigente; referências internas às versões anteriores requerem reconciliação condicionada |
| Authority Contracts | 1.0.11 | 1.0.12 | adendo ao Contrato 7 não vigente |
| Leia Primeiro Business | 1.0.19 | não preparado | manter corrente; nova versão candidata apenas após deliberação normativa do conteúdo |
| Manifesto Canônico das Homes | 7.0.53 na branch B2 | não preparado | preservar pacote corrente até decisão; eventual atualização coordenada |
| Handoff Canônico das Oito Homes | 1.7.13 | não preparado | avaliar apenas adendo curto à seção 4.7 ou referência; sem duplicar narrativa do M07 |

## Sequência de sincronização proposta

1. **Auditoria de não regressão:** confirmar invariância da direção principal de M07, supporting copy, CTA, 10 movimentos, autoridade de dados e autonomia.
2. **Deliberação normativa do texto candidato:** obter aprovação expressa de inclusão dos adendos e sua classificação normativa. A autorização B2 atual se limita à preparação.
3. **Reconciliar fontes Business como pacote único:** Master 1.1.11, Source Lock 1.1.29, Contrato 7 1.0.12, corrigindo referências internas somente quando autorizadas.
4. **Preparar dependentes:** Leia Primeiro Business, seção 4.7 do Handoff comum **se necessário**, e Manifesto das Oito Homes; aumentar versões e alinhar links/IDs com o pacote aprovado, não criar fonte paralela.
5. **Validação:** verificar frontmatter, referências, IDs, MkDocs strict build, estados semânticos, diff e checks do SHA final; registrar evidências.
6. **Integração separada:** merge apenas com autorização específica; publicação/execução operacional continuam independentes.

## Restrições

Não alterar o GPA-004/GPA-006, não apresentar cenários futuros como previsão determinística ou recurso vigente, não inferir dados pessoais ou KPIs internos, não promover a PR #720 por dependência, não efetuar merge e não antecipar divulgação das versões candidatas no Manifesto canônico.

## Conclusão

**Handoff aplicável localizado: comum às oito Homes, seção 4.7 Business.** O sincronismo das referências está especificado e condicionado à deliberação normativa de conteúdo. `handoff_identified / sync_plan_prepared / no_promotion`.
