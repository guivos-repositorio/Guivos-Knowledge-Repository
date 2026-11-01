---
id: GKR-UX-HOMES-CROSSBRANCH-ORDER-001
title: Auditoria de integridade e ordem governada — Intelligence e Business B2
status: proposed_non_normative
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-11-01
normative: false
---

# Auditoria de integridade e ordem de integração — Homes

## Evidências documentais

A proposta de Manifesto consolidado `public-homes-consolidated-manifest-candidate-20261101.md` foi conferida contra os arquivos das duas branches de origem. As oito referências candidatas de Business e Intelligence estão alinhadas às versões de seus respectivos arquivos: Business Read First 1.0.20, Source Lock 1.1.29, Master 1.1.11, Authority Contracts 1.0.12; Intelligence Read First 1.0.10, Handoff 1.1.18, Source Lock 1.1.17 e Master 0.2.15.

O arquivo de consolidação é explicitamente `status: proposed_non_normative`, `normative: false`, `version: 0.1.0`. A indicação `7.0.55` é **alvo condicional de futura versão canônica**, não versão atribuída à fonte atual.

## Riscos e ressalvas

1. As duas branches de origem alteram o mesmo Manifesto Canônico para `7.0.54` com referências diferentes; aplicar ambas sem reconciliação pode gerar conflitos ou perda de atualizações.
2. Os Masters candidatos de Business e Intelligence ainda apresentam `status: active` no frontmatter herdado; **a branch de proposta não lhes confere vigência na main**. O Master Business continua `normative: true` como atributo da fonte; isso não torna a versão candidata autoridade atual.
3. A PR #720 passou nas validações semântica e mecânica para o SHA `857dfce13644d4d0e37cd36964b91be03b0a84de`. Esta evidência **não** se transfere para a branch Business nem para a proposta consolidada.
4. Não foram retornados workflows associados ao commit de consolidação `4e25c5b17f1bab2825cf43cf39c6cd9f8982477e`; a ausência de runs não equivale a validação.
5. A versão normativa de referência da Home Intelligence permanece GPA-006 v2.0.2, conforme decisão da direção, com 2.0.3 como versão física posterior.

## Sequência governada recomendada

**Fase A — revisão independente:** finalizar revisão e autorizações específicas de integração para PR #720 (Intelligence) e para o pacote Business B2. Não presumir que aprovação documental constitui autorização de merge.

**Fase B — seleção de ordem:** após as duas autorizações, estabelecer ordem de integração e rebase/conciliação. Se apenas uma trilha for autorizada, integrar exclusivamente suas referências e manter a outra fora do Manifesto corrente.

**Fase C — consolidação do Manifesto:** criar a versão canônica subsequente com base no estado atualizado real da `main`, jamais em numeração presumida; conciliar as oito referências somente quando seus artefatos de origem estiverem integrados. O número 7.0.55 é hipotético enquanto 7.0.54 não for canônico.

**Fase D — controles finais:** comparar diff, validar frontmatter, links, identificadores, documentos dependentes, checks do mesmo SHA e políticas de branch. Merge depende de autorização específica. Verificar publicação separadamente após integração autorizada.

## Parecer

**Integridade referencial do documento de trabalho: verificada para as oito referências. Compatibilidade de integração: condicionada.** Este relatório não libera merge, publicação, disponibilidade funcional, implantação, testes ou execução operacional. 
