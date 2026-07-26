---
id: GKR-CANON-MATRIX-001
title: Matriz de Consolidação Canônica
status: active
version: 2.3.0
owner: Guivos
last_updated: 2026-07-26
depends_on:
  - GKR-STATE-001
related:
  - GKR-CANON-MATRIX-UXA-005
  - GKR-CANON-MATRIX-UXA-001
  - GKR-CANON-MATRIX-COD-017
  - GKR-R6-RESUMPTION-001
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-017
  - UXA-000
  - UXA-001
  - UXA-002
  - UXA-003
  - UXA-004
  - UXA-005
  - UXA-006
  - UXA-007
  - UXA-008
  - M7.19.2
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
| Pausar | trabalho permanece válido, sem execução adicional até nova autorização |
| Discovery | hipótese e arquitetura inicial em desenvolvimento, sem promoção a implementação |
| Wireframe | hipótese estrutural visual para validação, sem design ou implementação |
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
| A2-R03 | Manter ativa e pausar operacionalmente | após `COD-017` e antes de `BUS-CAND-010` |
| BA-STR-002 | Manter ativo e pausado | 17 de 18 decisões; nenhuma submissão aberta |
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
| `COD-010` | Manter | `Merge into BUS-CAND-003` aceito para `BUS-CAND-002` |
| `COD-011` | Manter | `Reformulate` aceito para `BUS-CAND-003` |
| `COD-012` | Manter | `Reformulate` aceito para `BUS-CAND-004` |
| `COD-013` | Manter | `Reformulate` aceito para `BUS-CAND-005` |
| `COD-014` | Manter | `Reject` aceito para `BUS-CAND-006` |
| `COD-015` | Manter | `Reject` aceito para `BUS-CAND-007` |
| `COD-016` | Manter | `Reject` aceito para `BUS-CAND-008` |
| `COD-017` | Manter | `Reject` aceito para `BUS-CAND-009` |
| CODR | Manter ativo | 17 de 18 decisões; 0 submissões abertas |
| COR | Refinar | 10 `Under Validation`; 2 `Merged`; 6 `Rejected` |
| `ECO-CAND-002` | Refinar e manter `Under Validation` | formulação revisada registrada; nova COEM pendente |
| `ECO-CAND-003` | Manter `Under Validation` | formulação combinada pendente de nova COEM |
| `ECO-CAND-004` | Remover do catálogo de Outcomes | `Rejected`; experiência preservada na Jornada e como evidência |
| `ECO-CAND-005` | Unificar em `ECO-CAND-003` | `Merged`; formulação e evidências preservadas |
| `ECO-CAND-006` | Refinar e manter `Under Validation` | formulação de saúde relacional registrada; nova COEM pendente |
| `ECO-CAND-007` | Refinar e manter `Under Validation` | formulação de participação inclusiva, digna e efetiva registrada; nova COEM pendente |
| `ECO-CAND-008` | Refinar e manter `Under Validation` | formulação de participação protegida, justa e contestável registrada; nova COEM pendente |
| `BUS-CAND-001` | Remover do catálogo de Business Outcomes | `Rejected`; conteúdo preservado como autoridade constitucional e obrigação de governança |
| `BUS-CAND-002` | Unificar em `BUS-CAND-003` | `Merged`; formulação, evidências e rastreabilidade preservadas |
| `BUS-CAND-003` | Refinar e manter `Under Validation` | `COD-011`; formulação revisada registrada; nova COEM pendente |
| `BUS-CAND-004` | Refinar e manter `Under Validation` | `COD-012`; legitimidade institucional sustentada registrada; confiança preservada como avaliação associada |
| `BUS-CAND-005` | Refinar e manter `Under Validation` | `COD-013`; continuidade econômica sustentável registrada; nova COEM pendente |
| `BUS-CAND-006` | Remover do catálogo de Business Outcomes | `COD-014`; crescimento rejeitado como Outcome permanente; expansão responsável preservada como trajetória opcional |
| `BUS-CAND-007` | Remover do catálogo de Business Outcomes | `COD-015`; aprendizado rejeitado como Outcome permanente; aprendizagem e adaptação preservadas como capacidades sustentadoras |
| `BUS-CAND-008` | Remover do catálogo de Business Outcomes | `COD-016`; saúde das relações de parceria rejeitada como Outcome permanente; governança de parceiros e gestão de alianças preservadas |
| `BUS-CAND-009` | Remover do catálogo de Business Outcomes | `COD-017`; coerência global com adequação contextual rejeitada como Outcome permanente; princípio arquitetural e critério governado preservados |
| `BUS-CAND-010` | Manter pendente | `Under Validation`; decisão individual e eventual fusão não antecipadas |
| `BA-STR-002-COD-SUB-018` | Pendente | não criado |
| `COD-018` | Pendente | não criado |
| Experience Architecture | Discovery | `UXA-000` a `UXA-004` integrados |
| programa de wireframes | Wireframe | `UXA-005` criado; método e gates registrados |
| tela `Hoje` | Wireframe | `UXA-006`; estrutura móvel inicial criada |
| detalhe de oportunidade | Wireframe | `UXA-007`; preço, relevância, elegibilidade e transparência estruturados |
| cadastro pela Organização | Wireframe | `UXA-008`; onze etapas e preço detalhado em desktop |
| navegação pessoal | Discovery | Hoje, Jornada, Explorar, Mapa e Eu |
| experiência da Organização | Discovery | visão geral, oportunidades, programas, coletivos, resultados e gestão |
| experiência do Coletivo | Discovery | início, atividades, pessoas, mapa, recursos e gestão |
| controle de relevância | Refinar em Discovery | explícito, explicável, ajustável e contestável |
| fluxo de oportunidades | Refinar em Discovery | cadastro, avaliação, ativação, apresentação e encerramento separados |
| preços e condições | Refinar em Wireframe | preço principal, custo total, taxas, cancelamento e relação comercial visíveis |
| Mapa | Discovery | oportunidades, Organizações, Coletivos e atividades; localização de participantes bloqueada |
| protótipo navegável | Pendente | não iniciado |
| design visual | Pendente | não iniciado |
| testes de usabilidade | Pendente | não iniciados |
| Outcomes canônicos | Pendente | zero códigos ou catálogos canônicos |
| Business Capabilities | Pendente | posteriores ao BA-STR-002 |
| produtos especializados | Preservar para rebaseline | ordem histórica não autoriza início |
| Commercial Model e Go-to-Market | Pendente | posteriores às dependências arquiteturais |
| Market Validation | Manter em paralelo | execução própria ainda pendente |
| validador mecânico | Manter | workflow permanente do GKR |

## 4. Resultado de COD-017 preservado

A alternativa `A — Aceitar Reject` permanece consolidada para `BUS-CAND-009`.

A decisão preserva formulação, evidências, rastreabilidade, princípios de coerência e adequação, sem criar código canônico ou iniciar fases posteriores.

## 5. Resultado de UXA-001 preservado

O incremento anterior:

- integrou a pausa governada antes de `BUS-CAND-010`;
- criou a frente de Experience Architecture em Discovery;
- preservou as capacidades e contratos normativos do `PAS-001`;
- propôs a tela `Hoje`, navegação, jornadas, oportunidades, Organizações, Coletivos e Mapa;
- não iniciou Product Engineering.

## 6. Resultado de UXA-005

O incremento atual:

- cria um programa explícito de wireframes;
- materializa três superfícies prioritárias;
- registra critérios de aceite e perguntas de validação;
- utiliza valores ilustrativos em locale pt-BR;
- preserva preço, custo total, elegibilidade e relação comercial como informações materiais;
- mantém envio, ativação, apresentação e contratação como estados distintos;
- não inicia protótipo, design visual, testes ou Product Engineering.

## 7. Addendum vigente

O addendum vigente é `Canonical Consolidation Matrix 2.3.0 — UXA-005 Initial Low-Fidelity Wireframes`.

## 8. Próximo ato

Receber a validação do Fundador sobre `UXA-005` a `UXA-008` e decidir entre reformulação, estados alternativos ou autorização separada de protótipo navegável de baixa fidelidade.
