---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.31.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-27
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
→ compreensão inicial revisável
→ decisão sobre persistência e personalização
→ Tela Hoje, jornada sem personalização ou exploração geral
→ Hoje | Jornada | Explorar | Mapa | Eu
```

## 5. Documentos ativos por responsabilidade funcional

| Responsabilidade | Documentos principais |
|---|---|
| Fundação, mapas e padrões | UXA-001, UXA-003, UXA-003-A1, UXA-005, UXA-009, UXA-011 e UXA-011-A1 |
| Página Inicial pública | [contrato](uxa-020-home-and-journey-entry.md), [validação](uxa-021-public-home-functional-validation-and-reformulation.md) e [wireframe](uxa-022-public-home-low-fidelity-wireframe.md) |
| Início protegido | [contrato validado](uxa-023-protected-journey-entry-functional-validation-and-reformulation.md), [wireframe móvel](uxa-034-protected-journey-entry-low-fidelity-wireframe.md) e [validação do wireframe](uxa-035-protected-journey-entry-wireframe-functional-validation-and-reformulation.md) |
| Tela Hoje | [experiência diária](uxa-002-daily-experience-and-home.md), [wireframe](uxa-006-today-low-fidelity-wireframe.md) e [validação](uxa-010-today-functional-validation-and-reformulation.md) |
| Explorar e Mapa | UXA-004 e UXA-024 a UXA-033 |
| Oportunidades | UXA-007, UXA-008, UXA-012 e UXA-013 |
| Organizações e Coletivos | UXA-014 a UXA-019 |

## 6. Estado atual

| Elemento | Situação compreensível | Referência técnica |
|---|---|---|
| Arquitetura da Experiência | ativa e integrada até a validação do início protegido móvel | UXA-000 a UXA-035; UXA-003-A1 |
| Resultados Empresariais | 18 decisões humanas; nenhum Resultado canônico | BA-STR-002; COD-018 |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |
| Página Inicial pública | validada e materializada para computador | UXA-020; UXA-021; UXA-022 |
| Referência móvel da Home | não iniciada | — |
| Início protegido móvel | funcionalmente validado e reformulado | UXA-020; UXA-023; UXA-034; UXA-035 |
| Referência do início protegido para computador | não iniciada | — |
| Compreensão inicial | contrato e gate estabelecidos; materialização posterior | UXA-011-A1; UXA-020; UXA-023; UXA-035 |
| Tela Hoje | validada e reposicionada como entrada recorrente | UXA-002; UXA-006; UXA-010 |
| Mapa de Oportunidades | estados móveis e referência desktop validados | UXA-004; UXA-024 a UXA-033 |
| Protótipo, design e testes | não iniciados | — |

## 7. Página Inicial e início protegido

A Home explica concretamente a Guivos, oferece início voluntário e exploração sem personalização e não coleta relato pessoal.

O início protegido móvel, reformulado pelas UXA-034 e UXA-035, demonstra:

- nenhum relato antes da explicação;
- dados de acesso separados do conteúdo da jornada;
- estados nomeados, pausáveis e retomáveis;
- acesso somente quando necessário;
- modalidades equivalentes e sem seleção automática;
- compartilhamento mínimo;
- voz e arquivo com explicação anterior;
- pausa, salvamento, saída e exclusão diferenciados;
- inventário antes do processamento;
- autorização inicialmente desmarcada e limitada à compreensão temporária;
- recusa sem processamento;
- persistência e personalização bloqueadas até o gate.

Arquivos vetoriais:

- `docs/assets/wireframes/uxa-034-protected-entry-explanation-mobile.svg`;
- `docs/assets/wireframes/uxa-034-protected-entry-access-mobile.svg`;
- `docs/assets/wireframes/uxa-034-protected-entry-sharing-mobile.svg`;
- `docs/assets/wireframes/uxa-034-protected-entry-review-mobile.svg`.

## 8. Tela Hoje

A Tela Hoje é a superfície recorrente posterior à compreensão inicial suficiente, revisável e autorizada.

## 9. Explorar e Mapa

`Explorar` organiza descoberta ampla por listas, busca, categorias e filtros gerais.

`Mapa` organiza a descoberta territorial. A UXA-024 a UXA-033 estabelecem o Mapa principal, uso sem localização, Lista, estado sem resultados e referência para computador.

## 10. Gate de persistência e personalização

Criar conta, digitar, gravar, enviar arquivo ou concluir relato não autoriza persistência ou personalização.

Nesta etapa, somente conteúdos revisados e marcados poderão ser autorizados para preparar uma compreensão inicial temporária e revisável.

Persistência e personalização permanecem bloqueadas até que a compreensão seja apresentada, revisada, corrigida ou limitada e decidida pela pessoa.

## 11. Gate de alinhamento à Fundação

Toda superfície deverá demonstrar aderência à Essência, Propósito, Missão Operacional, Visão, Constituição e Princípios Permanentes da Guivos.

Falha material impede avanço para wireframe, protótipo, design, teste, especificação técnica ou desenvolvimento.

## 12. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar a referência móvel da Home;
2. materializar a revisão da compreensão inicial;
3. validar a transição para a primeira Tela Hoje;
4. criar estados especializados de texto, voz e arquivos;
5. criar referência do início protegido para computador;
6. criar estados de processamento, pausa, falha e retomada;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
