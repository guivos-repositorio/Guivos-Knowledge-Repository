---
id: GKR-CANON-MATRIX-001
title: Matriz de Consolidação Canônica
status: active
version: 1.73.0
owner: Guivos
last_updated: 2026-07-25
depends_on:
  - GKR-STATE-001
related:
  - GKR-CANON-MATRIX-COD-003
  - GKR-R6-RESUMPTION-001
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - BA-STR-002-COD-SUB-003
  - COD-003
  - M7.5
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
| CODR | Manter ativo | 3 de 18 decisões registradas |
| COR | Refinar | 17 candidatos `Under Validation`; 1 `Merged` |
| `ECO-CAND-003` | Manter `Under Validation` | formulação combinada pendente de nova COEM |
| `ECO-CAND-005` | Unificar em `ECO-CAND-003` | estado `Merged`; formulação e evidências preservadas |
| Outcomes canônicos | Pendente | zero códigos ou catálogos canônicos |
| Business Capabilities | Pendente | posteriores ao BA-STR-002 |
| produtos especializados | Preservar para rebaseline | ordem histórica não autoriza início |
| Commercial Model e Go-to-Market | Pendente | posteriores às dependências arquiteturais |
| Market Validation | Manter em paralelo | execução própria ainda pendente |
| validador mecânico | Manter | workflow permanente do GKR |

## 4. Resultado de COD-003

A alternativa `A — Aceitar Merge into ECO-CAND-003` foi consolidada como decisão humana.

### Formulação combinada candidata

> O ecossistema preserva condições reais, contextualmente adequadas e não coercitivas para que Pessoas, Organizações e Coletivos exerçam agência efetiva e situada ao definir, revisar, pausar, recusar, abandonar ou renovar seus próprios próximos passos diante de mudanças, aprendizados e limites legítimos, individualmente ou em relações de co-agência.

A decisão:

- preserva `ECO-CAND-005` como registro histórico e rastreável;
- altera seu estado para `Merged`;
- mantém `ECO-CAND-003` em `Under Validation`;
- não cria código canônico;
- não inicia AQS-O01, Business Capabilities ou Product Engineering.

## 5. Addendum vigente

O addendum vigente é `Canonical Consolidation Matrix 1.73.0 — COD-003`.

## 6. Próximo ato

Preparar a submissão de `ECO-CAND-002 — Acesso a possibilidades relevantes` à quarta decisão humana individual sobre a recomendação `Reformulate`.
