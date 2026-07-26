---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.21.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-26
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
normative: false
---

# Arquitetura da Experiência da Guivos

## 1. Finalidade

A Arquitetura da Experiência transforma princípios, capacidades e contratos do Repositório de Conhecimento da Guivos em experiências compreensíveis para Pessoas, Organizações e Coletivos.

Ela governa jornadas, superfícies, navegação, voluntariedade, privacidade, compreensão do Momento Atual, explicabilidade, participação institucional e critérios para wireframes, protótipos e testes posteriores.

## 2. Limite da frente

Esta frente não inicia Engenharia de Produto, não define tecnologia, não cria design visual final, não conclui preços ou planos e não autoriza produção.

## 3. Regra de leitura dos identificadores

Os identificadores registram a ordem histórica de criação dos documentos. Eles não representam a ordem em que as telas aparecem para a pessoa.

A existência do documento **UXA-006 — Wireframe da Tela Hoje** antes do documento **UXA-022 — Wireframe da Página Inicial Pública** não significa que a Tela Hoje antecede a Home.

A correção formal está registrada em [Correção da Ordem Funcional da Primeira Entrada Pessoal](uxa-003-a1-first-entry-functional-order.md).

## 4. Ordem funcional da experiência pessoal

```text
Página Inicial pública da Guivos
→ decisão voluntária de iniciar ou explorar
→ explicação do ambiente protegido e das alternativas
→ autenticação ou criação de conta
→ finalidades, privacidade e controles
→ escolha da modalidade de relato
→ compartilhamento mínimo e progressivo
→ revisão do que foi recebido
→ autorização específica para processamento aplicável
→ compreensão inicial apresentada
→ revisão, correção, limitação e decisão
→ Tela Hoje, jornada sem personalização ou exploração geral
→ navegação recorrente: Hoje | Jornada | Explorar | Mapa | Eu
```

A Página Inicial pública antecede o início protegido e a Tela Hoje.

O Mapa de Oportunidades não entra entre a Home e a Tela Hoje. Ele é uma superfície própria da navegação recorrente e também pode ser acessado pela exploração geral da Home, por `Explorar` e pelo bloco contextual `Perto de mim` da Tela Hoje.

## 5. Documentos ativos por responsabilidade funcional

| Responsabilidade | Documentos principais |
|---|---|
| Fundação, mapas e padrões | UXA-001, UXA-003, UXA-003-A1, UXA-005, UXA-009, UXA-011 e UXA-011-A1 |
| Página Inicial pública | [Contrato da primeira entrada](uxa-020-home-and-journey-entry.md), [validação funcional](uxa-021-public-home-functional-validation-and-reformulation.md) e [wireframe gráfico](uxa-022-public-home-low-fidelity-wireframe.md) |
| Início protegido da jornada | [Validação funcional](uxa-023-protected-journey-entry-functional-validation-and-reformulation.md) |
| Tela Hoje recorrente | [Experiência diária](uxa-002-daily-experience-and-home.md), [wireframe](uxa-006-today-low-fidelity-wireframe.md) e [validação funcional](uxa-010-today-functional-validation-and-reformulation.md) |
| Explorar e Mapa | [Contrato funcional](uxa-004-opportunities-organizations-collectives-map.md), [wireframe reformulado](uxa-024-opportunity-map-low-fidelity-wireframe.md) e [validação funcional](uxa-025-opportunity-map-functional-validation-and-reformulation.md) |
| Oportunidades | UXA-007, UXA-008, UXA-012 e UXA-013 |
| Organizações e Coletivos | UXA-014, UXA-015, UXA-016, UXA-017, UXA-018 e UXA-019 |

## 6. Estado atual

| Elemento | Situação compreensível | Referência técnica |
|---|---|---|
| Arquitetura da Experiência | descoberta ativa e integrada até a validação funcional do Mapa | UXA-000 a UXA-025; UXA-003-A1 |
| Resultados Empresariais | 18 de 18 decisões humanas; nenhum Resultado canônico | BA-STR-002; COD-018 |
| Engenharia de Produto | pausada antes da primeira unidade de trabalho | W0-01 |
| Página Inicial pública | validada, reformulada e materializada para computador | UXA-020; UXA-021; UXA-022 |
| Referência móvel da Home | não iniciada | — |
| Início protegido da jornada | funcionalmente validado e reformulado | UXA-020; UXA-023 |
| Wireframe do início protegido | não iniciado | — |
| Compreensão inicial | contrato e gate estabelecidos; validação especializada posterior | UXA-011-A1; UXA-020; UXA-023 |
| Tela Hoje | validada e reposicionada como entrada recorrente | UXA-002; UXA-006; UXA-010 |
| Mapa de Oportunidades | funcionalmente validado e reformulado | UXA-004; UXA-024; UXA-025 |
| Estados alternativos do Mapa | funcionalmente governados; wireframes não iniciados | UXA-025 |
| Referência do Mapa para computador | não iniciada | — |
| Detalhe de Oportunidade | validado e reformulado | UXA-007; UXA-012 |
| Cadastro pela Organização | validado e reformulado | UXA-008; UXA-013 |
| Organizações e Coletivos | fundação, superfícies e relações estabelecidas | UXA-014 a UXA-019 |
| Protótipo, design e testes | não iniciados | — |

## 7. Página Inicial pública

A Home explica concretamente o que é a Guivos, oferece `Iniciar minha jornada` e `Explorar sem personalização`, apresenta caminhos pessoais, gerais e institucionais e não coleta texto pessoal, voz, arquivos ou fontes externas.

O wireframe está registrado como **UXA-022 — Wireframe de Baixa Fidelidade da Página Inicial Pública da Guivos**.

Arquivo vetorial:

`docs/assets/wireframes/uxa-022-public-home-desktop.svg`

A referência possui dimensão estrutural de 1.440 por 2.200 pixels para web em computador e não representa design, implementação ou versão móvel.

## 8. Início protegido da jornada

O ambiente protegido foi considerado funcionalmente válido após reformulação.

Ele explica antes da autenticação e da coleta, separa conta de autorização, preserva compartilhamento mínimo, trata modalidades como alternativas, exige revisão antes do processamento material, torna estados e falhas verificáveis, protege informações sensíveis e apresenta compreensão inicial revisável.

A personalização permanece bloqueada antes do gate.

## 9. Tela Hoje

A Tela Hoje é a superfície recorrente pessoal posterior à compreensão inicial suficiente, revisável e autorizada.

Ela não deverá receber o primeiro relato completo nem apresentar oportunidades como personalizadas antes do gate.

O wireframe permanece registrado como **UXA-006 — Wireframe de Baixa Fidelidade da Tela Hoje**.

Quando localização estiver autorizada e houver utilidade material, a Tela Hoje poderá exibir um bloco compacto `Perto de mim`, com a ação `Abrir no mapa`. O mapa completo não será incorporado à Tela Hoje.

## 10. Explorar e Mapa

`Explorar` organiza a descoberta ampla por lista, busca, categorias e filtros.

`Mapa` organiza a mesma descoberta pela dimensão territorial e permanece uma área própria da navegação recorrente:

```text
Hoje | Jornada | Explorar | Mapa | Eu
```

O wireframe móvel reformulado está registrado como **UXA-024 — Wireframe de Baixa Fidelidade do Mapa de Oportunidades**.

A validação funcional está registrada como **UXA-025 — Validação Funcional e Reformulação do Mapa de Oportunidades**.

Arquivo vetorial:

`docs/assets/wireframes/uxa-024-opportunity-map-mobile.svg`

A referência possui dimensão de 390 por 844 pixels e demonstra:

- `Agindo como: Minha jornada`;
- pesquisa territorial;
- Mapa e Lista sincronizados;
- filtros ativos, quantidade de filtros e limpeza;
- quantidade de resultados;
- `Pesquisar nesta área`;
- camadas e legenda;
- localização aproximada e privacidade;
- cartão selecionado com preço, acessibilidade, relevância e relação comercial;
- rota condicionada à disponibilidade segura do endereço;
- navegação recorrente com Mapa selecionado.

A localização poderá ser exata e temporária, aproximada, informada por cidade, selecionada por região ou desativada.

O Mapa não deverá mostrar localização de participantes, revelar residências ou locais sensíveis, exigir rastreamento contínuo ou presumir interesse somente pela proximidade.

## 11. Estados funcionais do Mapa

A UXA-025 governa localização desativada, localização aproximada, localização exata temporária, ausência de resultados, carregamento, baixa conectividade, item indisponível, endereço protegido, permissão revogada, erro de fonte, contexto sem gate e mapa indisponível.

A criação de wireframes específicos permanece ato separado.

## 12. Gate de personalização

Personalização material exige base suficiente, origem e finalidade identificadas, distinção entre naturezas da informação, revisão real, controles de correção e limitação, autorização compatível, ausência de conflito material e incertezas visíveis.

Sem o gate, a pessoa poderá continuar sem personalização, explorar, corrigir, pausar ou excluir.

## 13. Gate de alinhamento à Fundação

Toda superfície deverá demonstrar aderência à Essência, Propósito, Missão Operacional, Visão de Longo Prazo, Constituição e Princípios Permanentes da Guivos.

Falha material impede avanço para wireframe, protótipo, design, teste, especificação técnica ou desenvolvimento.

## 14. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar estados alternativos do Mapa, começando por Lista ou localização desativada;
2. criar referência do Mapa para computador;
3. criar o wireframe gráfico do início protegido da jornada;
4. criar a referência móvel da Página Inicial pública;
5. validar a revisão da compreensão inicial;
6. validar a transição para a primeira Tela Hoje;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
