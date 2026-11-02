---
id: GKR-UX-HOMES-POSTMERGE-AUDIT-20261101
title: Auditoria documental pós-merge — oito Homes públicas
status: proposed_non_normative
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-11-01
normative: false
---

# Auditoria pós-merge das oito Homes

## Escopo e limite
Revisão estática de `main` após os merges autorizados das PRs #720 (Intelligence) e #722 (Business B2). O relatório não altera o Manifesto vigente nem autoriza publicação, deploy ou operação.

## Resultado — Documentos Mestres

| Home | Versão declarada no Manifesto 7.0.55 | Versão efetiva em main | Conclusão |
| --- | --- | --- | --- |
| Pessoa | 1.0.8 | 1.0.8 | Alinhado |
| Organizações e Coletivos | **1.0.7** | **1.0.9** | **Divergência real — corrigir referência** |
| Mall | 1.1.4 | 1.1.4 | Alinhado |
| Travel | 1.1.6 | 1.1.6 | Alinhado |
| Media | 1.0.3 | 1.0.3 | Alinhado |
| Ads | 1.0.3 | 1.0.3 | Alinhado |
| Business | 1.1.11 | 1.1.11 | Alinhado |
| Intelligence | 0.2.15 | 0.2.15 | Alinhado |

As oito fontes Mestre consultadas apresentam `status: active` no frontmatter de `main`; isso não equivale a validação de experiência ou operação.

## Referências auxiliares inspecionadas
- Read First Pessoa `1.0.5` e O/C `1.0.5`: coerentes com Manifesto.
- Read First Mall `1.0.4`, Travel `1.0.4`, Media `1.0.2`, Ads `1.0.2`: coerentes com Manifesto.
- Read First Business `1.0.20`, Source Lock Business `1.1.29`, Authority Contracts Business `1.0.12`, Conversão Business `1.0.3`: coerentes com Manifesto.
- Read First Intelligence `1.0.10`, Source Lock Intelligence `1.1.17`, Handoff Intelligence `1.1.18`: coerentes com Manifesto.
- Handoff comum das oito Homes `1.7.13`: coerente com Manifesto.

## Pendência de correção
O Manifesto `7.0.55` apresenta `GKR-UX-HOME-OC-MASTER-001 v1.0.7`, enquanto o Mestre atual em `main` é `v1.0.9`. Recomenda-se criar versão candidata seguinte do Manifesto, com alteração pontual de referência, comparar diffs e validar checks, sem alterar textos, autoridades ou jornada de O/C.

A presente auditoria não cobriu exaustivamente todos os arquivos auxiliares, links externos, regras de publicação, runtime, deploy ou a cadeia completa de dependências. Nenhum desses itens deve ser presumido validado por este parecer.

## Parecer
**Conformidade referencial parcial: sete dos oito Mestres alinhados; uma divergência documental confirmada em Organizações e Coletivos.** As fontes prioritárias auxiliares consultadas coincidem com o Manifesto. Manter publicação e operação bloqueadas; correção documental candidata pode ser proposta sob governança, com merge sujeito a autorização específica.
