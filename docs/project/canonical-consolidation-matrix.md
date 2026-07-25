---
id: GKR-CANON-MATRIX-001
title: Matriz de Consolidação Canônica
status: active
version: 1.70.0
owner: Guivos
last_updated: 2026-07-24
depends_on:
  - GKR-STATE-001
related:
  - GKR-CANON-MATRIX-GKR-R6
  - GKR-R6-RESUMPTION-001
  - BA-STR-002-CODR-001
  - BA-STR-002-COD-SUB-002
  - M7.3.5
normative: false
---

# Matriz de Consolidação Canônica

## 1. Finalidade

Esta matriz central registra decisões consolidadas de maior alcance e aponta para as autoridades e addenda que preservam o detalhamento. Ela não substitui documentos normativos, ADRs, validações, auditorias ou registros de decisão.

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
| A2-R03 | Retomar | ativa em execução |
| BA-STR-002 | Retomar | Business Outcomes como prioridade atual |
| COR, validação externa e COEM | Manter concluídos | 18/18 candidatos e 6/6 clusters |
| `COD-001` | Manter | `ECO-CAND-001` com `Reformulate` aceito |
| CODR | Manter ativo | 1 de 18 decisões registradas |
| `ECO-CAND-003` | Pendente | submetido à manifestação humana |
| `COD-002` | Pendente | não existe antes da manifestação |
| Outcomes canônicos | Pendente | zero códigos ou catálogos canônicos |
| Business Capabilities | Pendente | posteriores ao BA-STR-002 |
| produtos especializados | Preservar para rebaseline | ordem histórica não autoriza início |
| Commercial Model e Go-to-Market | Pendente | posteriores às dependências arquiteturais |
| Market Validation | Manter em paralelo | execução própria ainda pendente |
| validador mecânico | Manter | workflow permanente do GKR |

## 4. Resultado da remediação

As não conformidades `NC-MAJ-01` a `NC-MAJ-07` e `NC-MIN-01` a `NC-MIN-03` foram corrigidas conforme seus incrementos e validadas mecanicamente em R5.

`GKR-REMEDIATION-002` está concluído. O R6 não reabre a remediação; apenas devolve a prioridade ao fluxo arquitetural correto.

## 5. Decisão corrente

O addendum vigente é `Canonical Consolidation Matrix 1.70.0 — R6 Governed Resumption`.

A submissão `BA-STR-002-COD-SUB-002` oferece três alternativas ao Fundador:

```text
A — Aceitar Reformulate
B — Rejeitar Reformulate, com fundamentação
C — Devolver para nova análise
```

Nenhuma alternativa foi consolidada como decisão.

## 6. Próximo ato

Registrar a manifestação humana e somente então definir se será criado `COD-002` ou se o candidato retornará à análise.
