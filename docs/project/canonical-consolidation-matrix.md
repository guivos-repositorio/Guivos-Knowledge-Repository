---
id: GKR-CANON-MATRIX-001
title: Matriz de Consolidação Canônica
status: active
version: 1.72.0
owner: Guivos
last_updated: 2026-07-25
depends_on:
  - GKR-STATE-001
related:
  - GKR-CANON-MATRIX-COD-003-SUBMISSION
  - GKR-R6-RESUMPTION-001
  - BA-STR-002-CODR-001
  - BA-STR-002-COD-SUB-003
  - COD-002
  - M7.4.1
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
| COR, validação externa e COEM | Manter concluídos | 18/18 candidatos e 6/6 clusters |
| `COD-001` | Manter | `Reformulate` aceito para `ECO-CAND-001` |
| `COD-002` | Manter | `Reformulate` aceito para `ECO-CAND-003` |
| CODR | Manter ativo | 2 de 18 decisões; 1 submissão aguardando resposta |
| `ECO-CAND-003` | Manter `Under Validation` | Agência efetiva e situada pendente de nova COEM |
| `ECO-CAND-005` | Pendente | submetido sobre `Merge into ECO-CAND-003` |
| `COD-003` | Pendente | não existe antes da manifestação humana |
| Outcomes canônicos | Pendente | zero códigos ou catálogos canônicos |
| Business Capabilities | Pendente | posteriores ao BA-STR-002 |
| produtos especializados | Preservar para rebaseline | ordem histórica não autoriza início |
| Commercial Model e Go-to-Market | Pendente | posteriores às dependências arquiteturais |
| Market Validation | Manter em paralelo | execução própria ainda pendente |
| validador mecânico | Manter | workflow permanente do GKR |

## 4. Resultado de COD-002 preservado

A alternativa `A — Aceitar Reformulate` permanece consolidada para `ECO-CAND-003`.

A formulação candidata vigente continua:

> O ecossistema preserva condições reais, contextualmente adequadas e não coercitivas para que Pessoas, Organizações e Coletivos exerçam agência efetiva e situada ao definir, revisar, pausar, recusar ou renovar seus próprios próximos passos, individualmente ou em relações de co-agência.

## 5. Submissão corrente

`BA-STR-002-COD-SUB-003` oferece ao Fundador:

```text
A — Aceitar Merge into ECO-CAND-003
B — Rejeitar a fusão, com fundamentação
C — Devolver para nova análise
```

A alternativa A é recomendada. Ela propõe preservar `ECO-CAND-005` como registro rastreável, incorporando sua dimensão de continuidade adaptativa à formulação candidata de Agência efetiva e situada.

Nenhuma alternativa foi consolidada como decisão. O COR permanece inalterado.

## 6. Addendum vigente

O addendum vigente é `Canonical Consolidation Matrix 1.72.0 — ECO-CAND-005 Decision Submission`.

## 7. Próximo ato

Registrar a manifestação humana e somente então definir se será criado `COD-003`, se `ECO-CAND-005` será preservado como candidato independente ou se retornará à análise.
