---
id: GKR-CANON-MATRIX-001
title: Matriz de Consolidação Canônica
status: active
version: 1.86.0
owner: Guivos
last_updated: 2026-07-25
depends_on:
  - GKR-STATE-001
related:
  - GKR-CANON-MATRIX-COD-010-SUBMISSION
  - GKR-R6-RESUMPTION-001
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - BA-STR-002-COD-SUB-010
  - COD-009
  - M7.11.1
normative: false
---

# Matriz de Consolidação Canônica

## 1. Finalidade

Esta matriz central registra decisões consolidadas de maior alcance e aponta para autoridades e addenda que preservam o detalhamento.

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
| `COD-006` | Manter | `Reformulate` aceito para `ECO-CAND-006` |
| `COD-007` | Manter | `Reformulate` aceito para `ECO-CAND-007` |
| `COD-008` | Manter | `Reformulate` aceito para `ECO-CAND-008` |
| `COD-009` | Manter | `Reject` aceito para `BUS-CAND-001` |
| CODR | Manter ativo | 9 de 18 decisões; 1 submissão aberta |
| COR | Manter | 15 `Under Validation`; 1 `Merged`; 2 `Rejected` |
| `ECO-CAND-002` | Refinar e manter `Under Validation` | formulação revisada registrada; nova COEM pendente |
| `ECO-CAND-003` | Manter `Under Validation` | formulação combinada pendente de nova COEM |
| `ECO-CAND-004` | Remover do catálogo de Outcomes | `Rejected`; experiência preservada na Jornada e como evidência |
| `ECO-CAND-005` | Unificar em `ECO-CAND-003` | `Merged`; formulação e evidências preservadas |
| `ECO-CAND-006` | Refinar e manter `Under Validation` | formulação de saúde relacional registrada; nova COEM pendente |
| `ECO-CAND-007` | Refinar e manter `Under Validation` | formulação de participação inclusiva, digna e efetiva registrada; nova COEM pendente |
| `ECO-CAND-008` | Refinar e manter `Under Validation` | formulação de participação protegida, justa e contestável registrada; nova COEM pendente |
| `BUS-CAND-001` | Remover do catálogo de Business Outcomes | `Rejected`; conteúdo preservado como autoridade constitucional e obrigação de governança |
| `BUS-CAND-002` | Pendente | `Merge into BUS-CAND-003` submetido; sem decisão humana ou alteração no COR |
| `BUS-CAND-003` | Manter `Under Validation` | alvo proposto; recomendação própria `Reformulate` ainda pendente |
| Outcomes canônicos | Pendente | zero códigos ou catálogos canônicos |
| Business Capabilities | Pendente | posteriores ao BA-STR-002 |
| produtos especializados | Preservar para rebaseline | ordem histórica não autoriza início |
| Commercial Model e Go-to-Market | Pendente | posteriores às dependências arquiteturais |
| Market Validation | Manter em paralelo | execução própria ainda pendente |
| validador mecânico | Manter | workflow permanente do GKR |

## 4. Submissão de BUS-CAND-002

A COEM recomenda `Merge into BUS-CAND-003` para **Relevância contínua das respostas**:

> As respostas organizadas pela Guivos permanecem relevantes diante da mudança de contextos, necessidades e prioridades dos participantes.

A formulação combinada candidata é:

> A Guivos sustenta condições para habilitar valor legítimo com consistência e relevância contextual, detectando mudanças materiais e ajustando proposições, capacidades e respostas de forma coerente, sem presumir controle unilateral sobre o valor realizado pelos participantes nem tratar personalização, satisfação pontual, disponibilidade técnica ou velocidade de resposta como prova suficiente.

A submissão preserva:

- formulação original, evidências e rastreabilidade de `BUS-CAND-002`;
- `BUS-CAND-002` e `BUS-CAND-003` em `Under Validation`;
- a recomendação própria `Reformulate` do alvo;
- relevância como propriedade observável, sem garantia universal ou permanente;
- separação entre submissão, decisão humana, alteração do COR e nova COEM;
- `COD-010` inexistente até manifestação humana explícita.

## 5. Limites

A submissão não:

- executa a fusão;
- aprova ou canonicaliza `BUS-CAND-003`;
- transforma personalização, satisfação pontual, disponibilidade técnica ou velocidade de resposta em prova de relevância;
- atribui à Guivos controle unilateral sobre valor vivido;
- altera o COR;
- inicia AQS-O01, Business Capabilities ou Product Engineering.

## 6. Addendum vigente

O addendum vigente é `Canonical Consolidation Matrix 1.86.0 — BUS-CAND-002 Decision Submission`.

## 7. Próximo ato

Receber a manifestação do Fundador sobre `BA-STR-002-COD-SUB-010`.
