---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.30.0
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
Página Inicial pública da Guivos
→ decisão voluntária de iniciar ou explorar
→ explicação do ambiente protegido
→ autenticação ou criação de conta
→ finalidades, privacidade e controles
→ compartilhamento mínimo e progressivo
→ revisão do que foi recebido
→ autorização aplicável
→ compreensão inicial apresentada
→ revisão, correção, limitação e decisão
→ Tela Hoje, jornada sem personalização ou exploração geral
→ Hoje | Jornada | Explorar | Mapa | Eu
```

## 5. Documentos ativos por responsabilidade funcional

| Responsabilidade | Documentos principais |
|---|---|
| Fundação, mapas e padrões | UXA-001, UXA-003, UXA-003-A1, UXA-005, UXA-009, UXA-011 e UXA-011-A1 |
| Página Inicial pública | [contrato](uxa-020-home-and-journey-entry.md), [validação](uxa-021-public-home-functional-validation-and-reformulation.md) e [wireframe](uxa-022-public-home-low-fidelity-wireframe.md) |
| Início protegido | [validação funcional](uxa-023-protected-journey-entry-functional-validation-and-reformulation.md) e [wireframe móvel](uxa-034-protected-journey-entry-low-fidelity-wireframe.md) |
| Tela Hoje | [experiência diária](uxa-002-daily-experience-and-home.md), [wireframe](uxa-006-today-low-fidelity-wireframe.md) e [validação](uxa-010-today-functional-validation-and-reformulation.md) |
| Explorar e Mapa | UXA-004 e UXA-024 a UXA-033 |
| Oportunidades | UXA-007, UXA-008, UXA-012 e UXA-013 |
| Organizações e Coletivos | UXA-014 a UXA-019 |

## 6. Estado atual

| Elemento | Situação compreensível | Referência técnica |
|---|---|---|
| Arquitetura da Experiência | ativa e integrada até o wireframe móvel do início protegido | UXA-000 a UXA-034; UXA-003-A1 |
| Resultados Empresariais | 18 decisões humanas; nenhum Resultado canônico | BA-STR-002; COD-018 |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |
| Página Inicial pública | validada e materializada para computador | UXA-020; UXA-021; UXA-022 |
| Referência móvel da Home | não iniciada | — |
| Início protegido | funcionalmente validado e materializado em quatro estados móveis; validação do wireframe pendente | UXA-020; UXA-023; UXA-034 |
| Referência do início protegido para computador | não iniciada | — |
| Compreensão inicial | contrato e gate estabelecidos; validação posterior | UXA-011-A1; UXA-020; UXA-023 |
| Tela Hoje | validada e reposicionada como entrada recorrente | UXA-002; UXA-006; UXA-010 |
| Mapa de Oportunidades | funcionalmente validado e reformulado | UXA-004; UXA-024; UXA-025 |
| Estados móveis do Mapa | sem localização, Lista e sem resultados validados | UXA-026 a UXA-031 |
| Referência para computador | funcionalmente validada e reformulada | UXA-032; UXA-033 |
| Referência para tablet | não iniciada | — |
| Protótipo, design e testes | não iniciados | — |

## 7. Página Inicial e início protegido

A Home explica concretamente a Guivos, oferece início voluntário e exploração sem personalização e não coleta relato pessoal.

O início protegido explica o processo antes da autenticação e da coleta, separa conta de autorização e mantém personalização bloqueada antes do gate.

A UXA-034 materializa quatro estados móveis:

1. explicação anterior à autenticação;
2. acesso protegido sem coleta iniciada;
3. modalidade e compartilhamento mínimo;
4. revisão e autorização específica.

Arquivos vetoriais:

- `docs/assets/wireframes/uxa-034-protected-entry-explanation-mobile.svg`;
- `docs/assets/wireframes/uxa-034-protected-entry-access-mobile.svg`;
- `docs/assets/wireframes/uxa-034-protected-entry-sharing-mobile.svg`;
- `docs/assets/wireframes/uxa-034-protected-entry-review-mobile.svg`.

O conjunto demonstra ausência de coleta automática, alternativas de acesso, modalidades equivalentes, compartilhamento mínimo, finalidade, privacidade, rascunho protegido, revisão, controles e autorização específica.

## 8. Tela Hoje

A Tela Hoje é a superfície recorrente posterior à compreensão inicial suficiente, revisável e autorizada.

## 9. Explorar e Mapa

`Explorar` organiza descoberta ampla por listas, busca, categorias e filtros gerais.

`Mapa` organiza a descoberta pela dimensão territorial e permanece na navegação:

```text
Hoje | Jornada | Explorar | Mapa | Eu
```

A UXA-024 a UXA-033 estabelecem o Mapa principal, uso sem localização, Lista, estado sem resultados e referência para computador.

## 10. Gate de personalização

Personalização material exige base suficiente, origem e finalidade identificadas, revisão real, controles e autorização compatível.

Criar conta, digitar, gravar, enviar arquivo ou concluir relato não autoriza personalização.

Sem gate, a pessoa pode continuar sem personalização, explorar, corrigir, pausar ou excluir.

## 11. Gate de alinhamento à Fundação

Toda superfície deverá demonstrar aderência à Essência, Propósito, Missão Operacional, Visão, Constituição e Princípios Permanentes da Guivos.

Falha material impede avanço para wireframe, protótipo, design, teste, especificação técnica ou desenvolvimento.

## 12. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. validar funcionalmente o wireframe móvel do início protegido;
2. criar a referência móvel da Home;
3. validar a revisão da compreensão inicial;
4. validar a transição para a primeira Tela Hoje;
5. criar estados especializados de texto, voz e arquivos;
6. criar referência do início protegido para computador;
7. criar outros estados do Mapa;
8. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
