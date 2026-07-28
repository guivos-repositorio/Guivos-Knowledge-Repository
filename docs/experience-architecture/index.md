---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.32.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-28
related:
  - PAS-001
  - PAS-001-CAPABILITY-MAP-001
  - GLPA-001
  - GIA-000
  - UXA-001
  - UXA-002
  - UXA-003
  - UXA-003-A1
  - UXA-004
  - UXA-005
  - UXA-006
  - UXA-007
  - UXA-008
  - UXA-009
  - UXA-010
  - UXA-011
  - UXA-011-A1
  - UXA-012
  - UXA-013
  - UXA-014
  - UXA-015
  - UXA-016
  - UXA-017
  - UXA-018
  - UXA-019
  - UXA-020
  - UXA-021
  - UXA-022
  - UXA-023
  - UXA-024
  - UXA-025
  - UXA-026
  - UXA-027
  - UXA-028
  - UXA-029
  - UXA-030
  - UXA-031
  - UXA-032
  - UXA-033
  - UXA-034
  - UXA-035
  - UXA-036
normative: false
---

# Arquitetura da Experiência da Guivos

## 1. Finalidade

A Arquitetura da Experiência transforma princípios, capacidades e contratos do Repositório de Conhecimento da Guivos em experiências compreensíveis para Pessoas, Organizações e Coletivos.

Ela governa jornadas, superfícies, navegação, voluntariedade, privacidade, compreensão, explicabilidade e critérios para wireframes, protótipos e testes posteriores.

## 2. Limite da frente

Esta frente não inicia Engenharia de Produto, não define tecnologia, não cria design visual final e não autoriza produção.

## 3. Regra de leitura dos identificadores

Os identificadores registram a ordem histórica de criação dos documentos. Eles não representam a ordem das telas.

A correção formal da primeira entrada está registrada em [UXA-003-A1](uxa-003-a1-first-entry-functional-order.md).

## 4. Ordem funcional da experiência pessoal

```text
Página Inicial pública
→ decisão voluntária de iniciar ou explorar
→ explicação do ambiente protegido
→ acesso, somente quando necessário
→ escolha e rascunho mínimo
→ revisão e autorização específica
→ processamento visível e interrompível
→ compreensão inicial apresentada como hipótese
→ revisão, correção, limitação ou rejeição
→ decisão separada sobre persistência
→ decisão separada sobre personalização
→ Tela Hoje, jornada sem personalização ou exploração geral
→ Hoje | Jornada | Explorar | Mapa | Eu
```

## 5. Documentos ativos por responsabilidade funcional

| Responsabilidade | Documentos principais |
|---|---|
| Fundação, mapas e padrões | UXA-001, UXA-003, UXA-003-A1, UXA-005, UXA-009, UXA-011 e UXA-011-A1 |
| Página Inicial pública | [contrato](uxa-020-home-and-journey-entry.md), [validação](uxa-021-public-home-functional-validation-and-reformulation.md) e [wireframe](uxa-022-public-home-low-fidelity-wireframe.md) |
| Início protegido | [contrato validado](uxa-023-protected-journey-entry-functional-validation-and-reformulation.md), [wireframe móvel](uxa-034-protected-journey-entry-low-fidelity-wireframe.md) e [validação do wireframe](uxa-035-protected-journey-entry-wireframe-functional-validation-and-reformulation.md) |
| Compreensão inicial | [contrato de explicabilidade](uxa-011-a1-moment-progress-and-next-step-explainability.md) e [wireframe móvel](uxa-036-initial-understanding-low-fidelity-wireframe.md) |
| Tela Hoje | [experiência diária](uxa-002-daily-experience-and-home.md), [wireframe](uxa-006-today-low-fidelity-wireframe.md) e [validação](uxa-010-today-functional-validation-and-reformulation.md) |
| Explorar e Mapa | UXA-004 e UXA-024 a UXA-033 |
| Oportunidades | UXA-007, UXA-008, UXA-012 e UXA-013 |
| Organizações e Coletivos | UXA-014 a UXA-019 |

## 6. Estado atual

| Elemento | Situação compreensível | Referência técnica |
|---|---|---|
| Arquitetura da Experiência | ativa e integrada até a compreensão inicial móvel | UXA-000 a UXA-036; UXA-003-A1 |
| Resultados Empresariais | 18 decisões humanas; nenhum Resultado canônico | BA-STR-002; COD-018 |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |
| Página Inicial pública | validada e materializada para computador | UXA-020; UXA-021; UXA-022 |
| Referência móvel da Home | não iniciada | — |
| Início protegido móvel | funcionalmente validado e reformulado | UXA-020; UXA-023; UXA-034; UXA-035 |
| Compreensão inicial móvel | quatro estados criados; validação funcional pendente | UXA-011-A1; UXA-036 |
| Referência do início protegido e compreensão para computador | não iniciada | — |
| Tela Hoje | validada e reposicionada como entrada recorrente | UXA-002; UXA-006; UXA-010 |
| Mapa de Oportunidades | estados móveis e referência desktop validados | UXA-004; UXA-024 a UXA-033 |
| Protótipo, design e testes | não iniciados | — |

## 7. Início protegido

A UXA-034 reformulada e a UXA-035 demonstram:

- nenhum relato antes da explicação;
- dados de acesso separados do conteúdo da jornada;
- estados nomeados, pausáveis e retomáveis;
- acesso somente quando necessário;
- modalidades equivalentes e sem seleção automática;
- compartilhamento mínimo;
- revisão anterior ao processamento;
- autorização específica e inicialmente desmarcada;
- recusa sem processamento;
- persistência e personalização bloqueadas até o gate.

## 8. Compreensão inicial móvel

A UXA-036 materializa:

- processamento limitado aos conteúdos autorizados;
- inventário do que está dentro e fora do processamento;
- finalidade, interrupção e retorno às autorizações;
- hipótese inicial sem diagnóstico ou certeza;
- Momento Atual, avanço e possibilidade de Próximo Passo separados;
- origem, natureza, confiança, lacunas e desconhecidos;
- ausência de avanço quando não houver evidência suficiente;
- correção, contestação, limitação e rejeição por afirmação;
- relato original separado da interpretação;
- persistência e personalização como decisões independentes;
- continuidade sem personalização;
- transição consciente para a Tela Hoje;
- base insuficiente sem hipótese artificial.

Arquivos vetoriais:

- `docs/assets/wireframes/uxa-036-initial-understanding-processing-mobile.svg`;
- `docs/assets/wireframes/uxa-036-initial-understanding-presentation-mobile.svg`;
- `docs/assets/wireframes/uxa-036-initial-understanding-review-mobile.svg`;
- `docs/assets/wireframes/uxa-036-initial-understanding-decision-mobile.svg`.

A referência ainda não foi funcionalmente validada.

## 9. Tela Hoje

A Tela Hoje é a superfície recorrente posterior à compreensão inicial suficiente, revisável e autorizada.

Sem personalização, poderá apresentar jornada geral, controles e exploração sem chamar possibilidades de recomendações pessoais.

## 10. Explorar e Mapa

`Explorar` organiza descoberta ampla por listas, busca, categorias e filtros gerais.

`Mapa` organiza a descoberta territorial. A UXA-024 a UXA-033 estabelecem o Mapa principal, uso sem localização, Lista, estado sem resultados e referência para computador.

## 11. Gate de persistência e personalização

Criar conta, digitar, gravar, enviar arquivo, concluir relato ou receber uma hipótese não autoriza persistência ou personalização.

Persistência e personalização são decisões separadas, posteriores à apresentação e revisão da compreensão inicial.

## 12. Gate de alinhamento à Fundação

Toda superfície deverá demonstrar aderência à Essência, Propósito, Missão Operacional, Visão, Constituição e Princípios Permanentes da Guivos.

Falha material impede avanço para wireframe, protótipo, design, teste, especificação técnica ou desenvolvimento.

## 13. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. validar funcionalmente o wireframe móvel da compreensão inicial;
2. criar a referência móvel da Home;
3. validar a transição para a primeira Tela Hoje;
4. criar estados de processamento, pausa, falha e retomada;
5. criar referência do início protegido e da compreensão para computador;
6. criar estados especializados de texto, voz e arquivos;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
