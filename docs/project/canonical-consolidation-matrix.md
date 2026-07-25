---
id: GKR-CANON-MATRIX-001
title: Matriz de Consolidação Canônica
status: active
version: 1.78.0
owner: Guivos
last_updated: 2026-07-25
depends_on:
  - GKR-STATE-001
related:
  - GKR-CANON-MATRIX-COD-006-SUBMISSION
  - GKR-R6-RESUMPTION-001
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - BA-STR-002-COD-SUB-006
  - COD-005
  - M7.7.1
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
| Remover do catálogo | candidato não integra o catálogo futuro, mas permanece rastreável |
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
| `COD-004` | Manter | `Reformulate` aceito para `ECO-CAND-002` |
| `COD-005` | Manter | `Reject` aceito para `ECO-CAND-004` |
| CODR | Manter ativo | 5 de 18 decisões; 1 submissão aberta |
| COR | Manter | 16 `Under Validation`; 1 `Merged`; 1 `Rejected` |
| `ECO-CAND-002` | Refinar e manter `Under Validation` | formulação revisada registrada; nova COEM pendente |
| `ECO-CAND-003` | Manter `Under Validation` | formulação combinada pendente de nova COEM |
| `ECO-CAND-004` | Remover do catálogo de Outcomes | `Rejected`; experiência preservada na Jornada e como evidência |
| `ECO-CAND-005` | Unificar em `ECO-CAND-003` | `Merged`; formulação e evidências preservadas |
| `ECO-CAND-006` | Pendente | `Reformulate` submetido; sem decisão humana ou alteração no COR |
| Outcomes canônicos | Pendente | zero códigos ou catálogos canônicos |
| Business Capabilities | Pendente | posteriores ao BA-STR-002 |
| produtos especializados | Preservar para rebaseline | ordem histórica não autoriza início |
| Commercial Model e Go-to-Market | Pendente | posteriores às dependências arquiteturais |
| Market Validation | Manter em paralelo | execução própria ainda pendente |
| validador mecânico | Manter | workflow permanente do GKR |

## 4. Submissão de ECO-CAND-006

A COEM recomenda `Reformulate` e a submissão apresenta a formulação candidata **Saúde relacional no ecossistema**:

> O ecossistema sustenta condições para que Pessoas, Organizações e Coletivos estabeleçam e preservem relações voluntárias, diversas e reciprocamente construtivas, capazes de ampliar cooperação, acesso e valor recíproco sem restringir autonomia, excluir terceiros ou produzir dano material.

A submissão preserva:

- a formulação original;
- os resultados dos quatro testes;
- diversidade estrutural, reciprocidade e autonomia como dimensões materiais;
- exclusão, restrição e dano material como contraevidências obrigatórias;
- a distinção entre saúde relacional, guardrails de proteção e confiança institucional;
- `ECO-CAND-006` em `Under Validation`;
- `COD-006` inexistente até manifestação humana explícita.

## 5. Limites

A submissão não:

- transforma quantidade, densidade, intensidade ou coesão das conexões em evidência suficiente;
- cria Outcome canônico;
- altera o COR;
- inicia AQS-O01, Business Capabilities ou Product Engineering.

## 6. Addendum vigente

O addendum vigente é `Canonical Consolidation Matrix 1.78.0 — ECO-CAND-006 Decision Submission`.

## 7. Próximo ato

Receber a manifestação do Fundador sobre `BA-STR-002-COD-SUB-006`.
