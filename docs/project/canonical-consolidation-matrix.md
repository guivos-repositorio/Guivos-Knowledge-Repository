---
id: GKR-CANON-MATRIX-001
title: Matriz de Consolidação Canônica
status: active
version: 2.2.0
owner: Guivos
last_updated: 2026-07-25
depends_on:
  - GKR-STATE-001
related:
  - GKR-CANON-MATRIX-UXA-001
  - UXA-000
  - UXA-001
  - UXA-002
  - UXA-003
  - UXA-004
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-017
  - M7.19.1
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
| A2-R03 | Pausar operacionalmente | após `COD-017` e antes de `BUS-CAND-010` |
| BA-STR-002 | Manter ativo e pausado | 17 de 18 decisões; nenhuma submissão aberta |
| validação externa e COEM | Manter concluídas | 18/18 candidatos e 6/6 clusters |
| `COD-001` a `COD-017` | Manter | decisões humanas registradas e rastreáveis |
| CODR | Manter ativo | 17 de 18 decisões; 0 submissões abertas |
| COR | Refinar | 10 `Under Validation`; 2 `Merged`; 6 `Rejected` |
| `BUS-CAND-010` | Manter pendente | `Under Validation`; decisão e fusão não antecipadas |
| `BA-STR-002-COD-SUB-018` | Pendente | não criado |
| `COD-018` | Pendente | não criado |
| Experience Architecture | Discovery | `UXA-000` a `UXA-004` criados para validação |
| tela `Hoje` | Discovery | hipótese de entrada orientada por utilidade material |
| navegação pessoal | Discovery | Hoje, Jornada, Explorar, Mapa e Eu |
| experiência da Organização | Discovery | visão geral, oportunidades, programas, coletivos, resultados e gestão |
| experiência do Coletivo | Discovery | início, atividades, pessoas, mapa, recursos e gestão |
| controle de relevância | Refinar em Discovery | explícito, explicável, ajustável e contestável |
| fluxo de oportunidades | Refinar em Discovery | cadastro, avaliação, ativação, apresentação e encerramento separados |
| preços e condições | Refinar em Discovery | transparência no cartão, detalhe, comparação, mapa e confirmação |
| Mapa | Discovery | oportunidades, Organizações, Coletivos e atividades; localização de participantes bloqueada |
| wireframes | Pendente | não iniciados |
| protótipos | Pendente | não iniciados |
| testes de usabilidade | Pendente | não iniciados |
| Outcomes canônicos | Pendente | zero códigos ou catálogos canônicos |
| Business Capabilities | Pendente | posteriores ao BA-STR-002 |
| produtos especializados | Preservar para rebaseline | ordem histórica não autoriza início |
| Commercial Model e Go-to-Market | Pendente | posteriores às dependências arquiteturais |
| Market Validation | Manter em paralelo | execução própria ainda pendente |
| validador mecânico | Manter | workflow permanente do GKR |

## 4. Decisões de Outcomes preservadas

| Candidato | Decisão vigente |
|---|---|
| ECO-CAND-001 | `Reformulate` aceito; nova COEM pendente |
| ECO-CAND-002 | `Reformulate` aceito; nova COEM pendente |
| ECO-CAND-003 | `Reformulate` aceito; formulação combinada pendente de nova COEM |
| ECO-CAND-004 | `Rejected`; experiência preservada na Jornada |
| ECO-CAND-005 | `Merged into ECO-CAND-003` |
| ECO-CAND-006 | `Reformulate` aceito; nova COEM pendente |
| ECO-CAND-007 | `Reformulate` aceito; nova COEM pendente |
| ECO-CAND-008 | `Reformulate` aceito; nova COEM pendente |
| BUS-CAND-001 | `Rejected`; autoridade constitucional preservada |
| BUS-CAND-002 | `Merged into BUS-CAND-003` |
| BUS-CAND-003 | `Reformulate` aceito; nova COEM pendente |
| BUS-CAND-004 | `Reformulate` aceito; nova COEM pendente |
| BUS-CAND-005 | `Reformulate` aceito; nova COEM pendente |
| BUS-CAND-006 | `Rejected`; expansão responsável preservada |
| BUS-CAND-007 | `Rejected`; aprendizagem e adaptação preservadas como capacidades |
| BUS-CAND-008 | `Rejected`; governança de parceiros preservada |
| BUS-CAND-009 | `Rejected`; coerência e adequação preservadas como princípio |
| BUS-CAND-010 | `Under Validation`; decisão pendente |

## 5. Resultado deste incremento

O incremento:

- integra a pausa governada antes de `BUS-CAND-010`;
- cria a frente de Experience Architecture em Discovery;
- preserva as capacidades e contratos normativos do `PAS-001`;
- propõe a tela `Hoje` como superfície de retorno por utilidade;
- propõe mapas de navegação e telas para Pessoa, Organização e Coletivo;
- define o fluxo inicial de cadastro e apresentação de oportunidades;
- estabelece transparência de preços, elegibilidade e relações comerciais;
- define o Mapa como superfície contextual com proteção de localização;
- não inicia wireframes, protótipos, testes ou Product Engineering.

## 6. Addendum vigente

O addendum vigente é `Canonical Consolidation Matrix 2.2.0 — UXA-001 Experience Architecture Discovery`.

## 7. Próximo ato

Receber a validação do Fundador sobre `UXA-001` a `UXA-004` e decidir entre refinamento da arquitetura de informação ou autorização de wireframes de baixa fidelidade.
