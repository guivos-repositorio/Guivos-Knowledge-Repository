---
id: GKR-CANON-MATRIX-001
title: Matriz de Consolidação Canônica
status: active
version: 1.74.0
owner: Guivos
last_updated: 2026-07-25
depends_on:
  - GKR-STATE-001
related:
  - GKR-CANON-MATRIX-COD-004-SUBMISSION
  - GKR-R6-RESUMPTION-001
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - BA-STR-002-COD-SUB-004
  - COD-003
  - M7.5.1
normative: false
---

# Matriz de Consolidação Canônica

## 1. Finalidade

Esta matriz central registra decisões consolidadas de maior alcance e aponta para autoridades e addenda que preservam o detalhamento. Ela não substitui documentos normativos, ADRs, validações, auditorias ou registros de decisão.

## 2. Vocabulário de decisão

| Decisão | Significado |
|---|---|
| Manter | elemento permanece válido sem alteração estrutural |
| Refinar | elemento permanece, com precisão adicional |
| Unificar | elementos redundantes são consolidados sob uma autoridade |
| Remover | elemento deixa de integrar o estado vigente |
| Historical only | elemento permanece como evidência histórica |
| Pendente | depende de evidência ou autoridade competente |

## 3. Decisões estruturais vigentes

| Elemento | Decisão | Autoridade e situação |
|---|---|---|
| GKR como fonte oficial | Manter | ADR-001 e governança vigente |
| Foundation Architecture | Manter congelada | baseline A2-B3 |
| Guivos Journey | Manter | `PAS-001 1.0.0 active`; nove capacidades concluídas |
| Product Engineering | Manter pausado | antes do W0-01; execução 0% |
| Guivos Economic Model | Manter documentariamente concluído | `GEM-001` a `GEM-010`; validação real pendente |
| remediação R1–R5 | Manter concluída | `GKR-R5-VALIDATION-001` com `PASS` |
| R6 | Manter concluído | retomada governada registrada |
| A2-R03 | Manter ativa | em execução |
| BA-STR-002 | Manter ativo | Business Outcomes como prioridade atual |
| validação externa e COEM | Manter concluídas | 18/18 candidatos e 6/6 clusters |
| `COD-001` | Manter | `Reformulate` aceito para `ECO-CAND-001` |
| `COD-002` | Manter | `Reformulate` aceito para `ECO-CAND-003` |
| `COD-003` | Manter | `Merge into ECO-CAND-003` aceito para `ECO-CAND-005` |
| CODR | Manter ativo | 3 de 18 decisões; 1 submissão aguardando resposta |
| COR | Manter | 17 candidatos `Under Validation`; 1 `Merged` |
| `ECO-CAND-003` | Manter `Under Validation` | formulação combinada pendente de nova COEM |
| `ECO-CAND-005` | Unificar em `ECO-CAND-003` | estado `Merged`; formulação e evidências preservadas |
| `ECO-CAND-002` | Pendente | submetido sobre `Reformulate`; decisão humana própria necessária |
| `COD-004` | Pendente | não existe antes da manifestação humana |
| Outcomes canônicos | Pendente | zero códigos ou catálogos canônicos |
| Business Capabilities | Pendente | posteriores ao BA-STR-002 |
| produtos especializados | Preservar para rebaseline | ordem histórica não autoriza início |
| Commercial Model e Go-to-Market | Pendente | posteriores às dependências arquiteturais |
| Market Validation | Manter em paralelo | execução própria ainda pendente |
| validador mecânico | Manter | workflow permanente do GKR |

## 4. Resultado de COD-003 preservado

A alternativa `A — Aceitar Merge into ECO-CAND-003` permanece consolidada. `ECO-CAND-005` está `Merged`, com rastreabilidade preservada, e `ECO-CAND-003` continua `Under Validation`.

## 5. Submissão corrente

`BA-STR-002-COD-SUB-004` oferece ao Fundador:

```text
A — Aceitar Reformulate
B — Rejeitar Reformulate, com fundamentação
C — Devolver para nova análise
```

A alternativa A é recomendada. Ela propõe a formulação candidata:

> Pessoas, Organizações e Coletivos dispõem de acesso real a possibilidades legítimas, compreensíveis e manejáveis, compatíveis com seu contexto, objetivos, restrições e fatores de conversão, preservando liberdade substantiva para compará-las e escolhê-las sem que a abundância de opções seja tratada como evidência de valor.

Nenhuma alternativa foi consolidada como decisão. O COR permanece inalterado.

## 6. Addendum vigente

O addendum vigente é `Canonical Consolidation Matrix 1.74.0 — ECO-CAND-002 Decision Submission`.

## 7. Próximo ato

Registrar a manifestação humana e somente então definir se será criado `COD-004`, se a recomendação será rejeitada ou se o candidato retornará à análise.
