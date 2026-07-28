---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.29.0
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

O Mapa não entra entre a Home e a Tela Hoje. Ele é uma superfície recorrente e também pode ser acessado por `Explorar`, exploração geral e `Perto de mim`.

## 5. Documentos ativos por responsabilidade funcional

| Responsabilidade | Documentos principais |
|---|---|
| Fundação, mapas e padrões | UXA-001, UXA-003, UXA-003-A1, UXA-005, UXA-009, UXA-011 e UXA-011-A1 |
| Página Inicial pública | [contrato](uxa-020-home-and-journey-entry.md), [validação](uxa-021-public-home-functional-validation-and-reformulation.md) e [wireframe](uxa-022-public-home-low-fidelity-wireframe.md) |
| Início protegido | [validação funcional](uxa-023-protected-journey-entry-functional-validation-and-reformulation.md) |
| Tela Hoje | [experiência diária](uxa-002-daily-experience-and-home.md), [wireframe](uxa-006-today-low-fidelity-wireframe.md) e [validação](uxa-010-today-functional-validation-and-reformulation.md) |
| Explorar e Mapa | [contrato](uxa-004-opportunities-organizations-collectives-map.md), [wireframe móvel](uxa-024-opportunity-map-low-fidelity-wireframe.md), [validação do Mapa](uxa-025-opportunity-map-functional-validation-and-reformulation.md), [estado sem localização](uxa-026-opportunity-map-location-disabled-state.md), [validação sem localização](uxa-027-opportunity-map-location-disabled-functional-validation-and-reformulation.md), [Lista](uxa-028-opportunity-map-list-state.md), [validação da Lista](uxa-029-opportunity-map-list-functional-validation-and-reformulation.md), [estado sem resultados](uxa-030-opportunity-map-no-results-state.md), [validação sem resultados](uxa-031-opportunity-map-no-results-functional-validation-and-reformulation.md), [referência para computador](uxa-032-opportunity-map-desktop-reference.md) e [validação desktop](uxa-033-opportunity-map-desktop-functional-validation-and-reformulation.md) |
| Oportunidades | UXA-007, UXA-008, UXA-012 e UXA-013 |
| Organizações e Coletivos | UXA-014 a UXA-019 |

## 6. Estado atual

| Elemento | Situação compreensível | Referência técnica |
|---|---|---|
| Arquitetura da Experiência | ativa e integrada até a validação desktop do Mapa | UXA-000 a UXA-033; UXA-003-A1 |
| Resultados Empresariais | 18 decisões humanas; nenhum Resultado canônico | BA-STR-002; COD-018 |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |
| Página Inicial pública | validada e materializada para computador | UXA-020; UXA-021; UXA-022 |
| Referência móvel da Home | não iniciada | — |
| Início protegido | funcionalmente validado e reformulado; wireframe pendente | UXA-020; UXA-023 |
| Compreensão inicial | contrato e gate estabelecidos; validação posterior | UXA-011-A1; UXA-020; UXA-023 |
| Tela Hoje | validada e reposicionada como entrada recorrente | UXA-002; UXA-006; UXA-010 |
| Mapa de Oportunidades | funcionalmente validado e reformulado | UXA-004; UXA-024; UXA-025 |
| Estado sem localização | funcionalmente validado e reformulado | UXA-026; UXA-027 |
| Visualização em Lista | funcionalmente validada e reformulada | UXA-028; UXA-029 |
| Estado sem resultados | funcionalmente validado e reformulado | UXA-030; UXA-031 |
| Referência para computador | funcionalmente validada e reformulada | UXA-032; UXA-033 |
| Referência para tablet | não iniciada | — |
| Demais estados do Mapa | governados; wireframes não iniciados | UXA-025 |
| Detalhe e cadastro | validados e reformulados | UXA-007; UXA-008; UXA-012; UXA-013 |
| Organizações e Coletivos | fundação, superfícies e relações estabelecidas | UXA-014 a UXA-019 |
| Protótipo, design e testes | não iniciados | — |

## 7. Página Inicial e início protegido

A Home explica concretamente a Guivos, oferece início voluntário e exploração sem personalização e não coleta relato pessoal.

O ambiente protegido explica o processo antes da autenticação e da coleta, separa conta de autorização e mantém personalização bloqueada antes do gate.

## 8. Tela Hoje

A Tela Hoje é a superfície recorrente posterior à compreensão inicial suficiente, revisável e autorizada.

Quando localização estiver autorizada e houver utilidade material, poderá apresentar `Perto de mim`, com `Abrir no mapa`.

## 9. Explorar e Mapa

`Explorar` organiza descoberta ampla por listas, busca, categorias e filtros gerais.

`Mapa` organiza a descoberta pela dimensão territorial e permanece na navegação:

```text
Hoje | Jornada | Explorar | Mapa | Eu
```

Arquivos vetoriais:

- `docs/assets/wireframes/uxa-024-opportunity-map-mobile.svg`;
- `docs/assets/wireframes/uxa-026-opportunity-map-location-disabled-mobile.svg`;
- `docs/assets/wireframes/uxa-028-opportunity-map-list-mobile.svg`;
- `docs/assets/wireframes/uxa-030-opportunity-map-no-results-mobile.svg`;
- `docs/assets/wireframes/uxa-032-opportunity-map-desktop.svg`;
- `docs/assets/wireframes/uxa-032-opportunity-map-no-results-desktop.svg`.

## 10. Estado sem localização

A UXA-026 e a UXA-027 estabelecem que localização não é requisito universal para utilizar o Mapa.

A pessoa pode escolher região manual, pesquisar, filtrar, salvar, abrir detalhes e definir origem específica sem compartilhar posição.

## 11. Visualização em Lista

A UXA-028 e a UXA-029 estabelecem a Lista como representação textual integral da mesma consulta territorial do Mapa.

A Lista preserva contexto, região, busca, filtros, quantidade, atualização, ordenação, cartões comparáveis, seleção, explicação, relação comercial e operação sem mapa carregado.

## 12. Estado sem resultados

A UXA-030 e a UXA-031 estabelecem que o total zero representa somente ausência de correspondências para a consulta executada.

O estado preserva contexto, cobertura verificável, revisão antes de ajustes, `Desfazer` condicional, seleção anterior, distinção entre ausência e falha, localização opcional e ausência de preenchimento patrocinado artificial.

## 13. Referência para computador validada

A UXA-032 e a UXA-033 estabelecem a primeira referência validada para tela ampla.

A reformulação demonstra:

- faixa `Consulta territorial ativa`;
- filtros semanticamente consistentes;
- `Visão dividida ativa`;
- foco no Mapa ou na Lista com contexto preservado;
- retorno à visão dividida;
- movimento do Mapa sem atualização silenciosa;
- `Pesquisar nesta área` condicionado ao movimento;
- seleção `Marcador 1` sincronizada;
- cartões comparáveis com origem e explicação;
- `Entender ordenação`;
- relação comercial rotulada;
- painel contextual recolhível;
- recuperação do estado zero concentrada no painel de consulta;
- seleção anterior explicável;
- Lista integral sem mapa carregado.

A referência possui dois arquivos de 1.440 por 1.024 pixels e é funcionalmente válida após reformulação.

Ela não conclui responsividade, pontos de quebra, tablet, design, protótipo, teste com usuários, acessibilidade técnica ou desenvolvimento.

## 14. Estados funcionais do Mapa

A UXA-025 governa localização desativada, aproximada e temporária, ausência de resultados, carregamento, baixa conectividade, item indisponível, endereço protegido, permissão revogada, erro de fonte, contexto sem gate e mapa indisponível.

A UXA-026 a UXA-033 materializam e validam o uso sem localização, a Lista, o estado sem resultados e a referência para computador. Os demais wireframes permanecem atos separados.

## 15. Gate de personalização

Personalização material exige base suficiente, origem e finalidade identificadas, revisão real, controles e autorização compatível.

Sem gate, a pessoa pode continuar sem personalização, explorar, corrigir, pausar ou excluir.

## 16. Gate de alinhamento à Fundação

Toda superfície deverá demonstrar aderência à Essência, Propósito, Missão Operacional, Visão, Constituição e Princípios Permanentes da Guivos.

Falha material impede avanço para wireframe, protótipo, design, teste, especificação técnica ou desenvolvimento.

## 17. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar o wireframe gráfico do início protegido;
2. criar a referência móvel da Home;
3. validar a revisão da compreensão inicial;
4. validar a transição para a primeira Tela Hoje;
5. criar outros estados alternativos do Mapa;
6. criar referência específica para tablet, caso priorizada;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
