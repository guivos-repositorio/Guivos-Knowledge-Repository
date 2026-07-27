---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.25.0
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

A correção formal da primeira entrada está registrada em [UXA-003-A1](uxa-003-a1-first-entry-functional-order.md).

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

O Mapa não entra entre a Home e a Tela Hoje. Ele é uma superfície própria da navegação recorrente e também pode ser acessado pela exploração geral, por `Explorar` e pelo bloco contextual `Perto de mim`.

## 5. Documentos ativos por responsabilidade funcional

| Responsabilidade | Documentos principais |
|---|---|
| Fundação, mapas e padrões | UXA-001, UXA-003, UXA-003-A1, UXA-005, UXA-009, UXA-011 e UXA-011-A1 |
| Página Inicial pública | [contrato](uxa-020-home-and-journey-entry.md), [validação](uxa-021-public-home-functional-validation-and-reformulation.md) e [wireframe](uxa-022-public-home-low-fidelity-wireframe.md) |
| Início protegido | [validação funcional](uxa-023-protected-journey-entry-functional-validation-and-reformulation.md) |
| Tela Hoje | [experiência diária](uxa-002-daily-experience-and-home.md), [wireframe](uxa-006-today-low-fidelity-wireframe.md) e [validação](uxa-010-today-functional-validation-and-reformulation.md) |
| Explorar e Mapa | [contrato](uxa-004-opportunities-organizations-collectives-map.md), [wireframe do Mapa](uxa-024-opportunity-map-low-fidelity-wireframe.md), [validação do Mapa](uxa-025-opportunity-map-functional-validation-and-reformulation.md), [estado sem localização](uxa-026-opportunity-map-location-disabled-state.md), [validação sem localização](uxa-027-opportunity-map-location-disabled-functional-validation-and-reformulation.md), [Lista](uxa-028-opportunity-map-list-state.md) e [validação da Lista](uxa-029-opportunity-map-list-functional-validation-and-reformulation.md) |
| Oportunidades | UXA-007, UXA-008, UXA-012 e UXA-013 |
| Organizações e Coletivos | UXA-014 a UXA-019 |

## 6. Estado atual

| Elemento | Situação compreensível | Referência técnica |
|---|---|---|
| Arquitetura da Experiência | ativa e integrada até a validação da Lista do Mapa | UXA-000 a UXA-029; UXA-003-A1 |
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
| Demais estados do Mapa | governados; wireframes não iniciados | UXA-025 |
| Referência do Mapa para computador | não iniciada | — |
| Detalhe e cadastro | validados e reformulados | UXA-007; UXA-008; UXA-012; UXA-013 |
| Organizações e Coletivos | fundação, superfícies e relações estabelecidas | UXA-014 a UXA-019 |
| Protótipo, design e testes | não iniciados | — |

## 7. Página Inicial e início protegido

A Home explica concretamente o que é a Guivos, oferece início voluntário e exploração sem personalização e não coleta relato pessoal.

O ambiente protegido explica o processo antes da autenticação e da coleta, separa conta de autorização, preserva compartilhamento mínimo e mantém personalização bloqueada antes do gate.

## 8. Tela Hoje

A Tela Hoje é a superfície recorrente pessoal posterior à compreensão inicial suficiente, revisável e autorizada.

Quando localização estiver autorizada e houver utilidade material, poderá apresentar um bloco compacto `Perto de mim`, com a ação `Abrir no mapa`.

## 9. Explorar e Mapa

`Explorar` organiza descoberta ampla por listas, busca, categorias e filtros gerais.

`Mapa` organiza a mesma descoberta pela dimensão territorial e permanece uma área própria da navegação recorrente:

```text
Hoje | Jornada | Explorar | Mapa | Eu
```

Arquivos vetoriais:

- `docs/assets/wireframes/uxa-024-opportunity-map-mobile.svg`;
- `docs/assets/wireframes/uxa-026-opportunity-map-location-disabled-mobile.svg`;
- `docs/assets/wireframes/uxa-028-opportunity-map-list-mobile.svg`.

## 10. Estado sem localização

A UXA-026 e a UXA-027 estabelecem que localização não é requisito universal para utilizar o Mapa.

A pessoa pode escolher região manual, pesquisar, filtrar, alternar modos, salvar, abrir detalhes e definir origem específica sem compartilhar a posição do dispositivo.

## 11. Visualização em Lista validada

A UXA-028 e a UXA-029 estabelecem a Lista como representação textual integral da mesma consulta territorial do Mapa.

A reformulação demonstra:

- `Lista territorial do Mapa · mesma consulta`;
- contexto `Agindo como`;
- região, busca e filtros preservados;
- total consolidado de filtros;
- quantidade e atualização dos resultados;
- ordenação explícita e explicável;
- cartões comparáveis com dados ausentes declarados;
- oportunidade selecionada preservada;
- explicação funcional e relação comercial separadas;
- salvamento e Detalhe sem localização;
- retorno ao Mapa sem perda de contexto;
- funcionamento sem mapa carregado.

A Lista não duplica `Explorar` e constitui alternativa integral para conteúdo textual, acessibilidade, baixa conectividade e indisponibilidade cartográfica.

A validação é funcional arquitetural. Teste de usabilidade e conformidade técnica de acessibilidade permanecem posteriores.

## 12. Estados funcionais do Mapa

A UXA-025 governa localização desativada, localização aproximada, localização exata temporária, ausência de resultados, carregamento, baixa conectividade, item indisponível, endereço protegido, permissão revogada, erro de fonte, contexto sem gate e mapa indisponível.

A UXA-026 a UXA-029 materializam e validam o uso sem localização e a Lista. Os demais wireframes permanecem atos separados.

## 13. Gate de personalização

Personalização material exige base suficiente, origem e finalidade identificadas, revisão real, controles de correção e limitação e autorização compatível.

Sem o gate, a pessoa pode continuar sem personalização, explorar, corrigir, pausar ou excluir.

## 14. Gate de alinhamento à Fundação

Toda superfície deverá demonstrar aderência à Essência, Propósito, Missão Operacional, Visão, Constituição e Princípios Permanentes da Guivos.

Falha material impede avanço para wireframe, protótipo, design, teste, especificação técnica ou desenvolvimento.

## 15. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar o estado sem resultados;
2. criar referência do Mapa para computador;
3. criar o wireframe gráfico do início protegido;
4. criar a referência móvel da Home;
5. validar a revisão da compreensão inicial;
6. validar a transição para a primeira Tela Hoje;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
