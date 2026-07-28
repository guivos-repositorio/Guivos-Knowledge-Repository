---
id: UXA-005
title: Programa Inicial de Wireframes de Baixa Fidelidade
status: draft
version: 0.15.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-27
parent: UXA-000
related:
  - UXA-001
  - UXA-002
  - UXA-003
  - UXA-003-A1
  - UXA-004
  - UXA-006
  - UXA-007
  - UXA-008
  - UXA-009
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
  - PAS-001
normative: false
---

# Programa Inicial de Wireframes de Baixa Fidelidade

## 1. Finalidade

Este programa materializa hipóteses de Arquitetura da Experiência em wireframes de baixa fidelidade. O objetivo é validar organização, hierarquia, conteúdo, ações e continuidade antes de identidade visual ou implementação.

## 2. Regra de ordem

Os identificadores preservam a ordem histórica de criação. Eles não determinam a ordem das telas.

```text
Página Inicial pública
→ início protegido da jornada
→ compreensão inicial revisável
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

A correção formal está registrada em [UXA-003-A1](uxa-003-a1-first-entry-functional-order.md).

## 3. Artefatos pela ordem funcional

1. Página Inicial e início da jornada — UXA-020;
2. validação da Home pública — UXA-021;
3. wireframe da Home para computador — UXA-022;
4. validação do início protegido — UXA-023;
5. wireframe da Tela Hoje — UXA-006;
6. wireframe móvel do Mapa — UXA-024;
7. validação do Mapa — UXA-025;
8. estado sem localização — UXA-026;
9. validação sem localização — UXA-027;
10. Lista do Mapa — UXA-028;
11. validação da Lista — UXA-029;
12. estado sem resultados — UXA-030;
13. validação sem resultados — UXA-031;
14. referência do Mapa para computador — UXA-032;
15. validação da referência para computador — UXA-033;
16. wireframe do Detalhe — UXA-007;
17. wireframe do Cadastro pela Organização — UXA-008.

O Mapa integra a navegação recorrente e pode ser acessado pela Home, por `Explorar`, por `Perto de mim` e pelo Detalhe.

## 4. Natureza dos artefatos

Os wireframes:

- são hipóteses estruturais para revisão;
- utilizam conteúdo ilustrativo;
- representam prioridade e relação funcional, não acabamento;
- podem ser alterados sem migração de produto;
- não definem componentes técnicos;
- não constituem especificação de implementação;
- não autorizam protótipo de alta fidelidade.

Wireframe gráfico não equivale a validação funcional. Validação funcional não equivale a teste de usabilidade, design ou desenvolvimento.

## 5. O que deverá ser validado

### 5.1 Compreensão

- A finalidade de cada superfície é compreendida rapidamente?
- Home, início protegido, Tela Hoje, Explorar e Mapa são distintos?
- Mapa e Lista representam a mesma consulta?
- A Lista territorial se diferencia de `Explorar`?
- `Agindo como`, região e localização são reconhecíveis?
- Quantidade, filtros e ordenação são compreensíveis?
- Resumo e controles dos filtros são semanticamente idênticos?
- Relação comercial está separada da relevância?
- Dados ausentes são apresentados sem inferência?
- O total zero é entendido como resultado da consulta atual?
- Cobertura, falha e indisponibilidade são distinguíveis?
- Em computador, filtros, Mapa, Lista e seleção parecem partes da mesma consulta?

### 5.2 Hierarquia

- O item mais importante ocupa a posição correta?
- O Mapa preserva espaço territorial sem ocultar contexto?
- A Lista preserva contexto antes dos resultados?
- Os cartões permitem comparação consistente?
- A seleção é reconhecível no marcador, cartão e painel?
- O painel contextual pode ser recolhido sem perder seleção?
- O estado zero apresenta diagnóstico antes da recuperação?
- As ações de recuperação possuem uma hierarquia única?
- A distribuição horizontal evita competição excessiva?

### 5.3 Autonomia

- Localização exata, aproximada, manual e desativada são alternativas reais?
- A recusa de localização preserva busca, Mapa, Lista, Detalhe e salvamento?
- Foco no Mapa ou na Lista mantém permissões e contexto?
- Mover o Mapa evita atualização silenciosa?
- A pessoa pode revisar filtros e ordenação?
- Ações de recuperação alteram somente a dimensão escolhida?
- A mudança é revisada antes de aplicar?
- O estado vazio evita preenchimento patrocinado artificial?
- Mais espaço visual evita aumentar coleta ou inferência territorial?

### 5.4 Continuidade

- A Home conduz ao início protegido, à compreensão e à Tela Hoje?
- A Tela Hoje conduz ao Mapa por um recorte compacto?
- Explorar e Mapa permanecem relacionados sem serem confundidos?
- Mapa e Lista preservam região, busca, filtros, quantidade, atualização, ordenação e seleção?
- Foco e retorno à visão dividida preservam o contexto?
- O Detalhe devolve a pessoa ao mesmo estado?
- A Lista funciona sem mapa carregado?
- Mapa e Lista preservam o mesmo total zero e cobertura?
- Uma alteração que produz zero pode ser compreendida e desfeita?
- A referência desktop mantém paridade sem criar catálogo independente?

## 6. Convenções de baixa fidelidade

| Elemento | Convenção |
|---|---|
| retângulo com borda | área funcional ou cartão |
| preenchimento escuro | ação principal ou estado selecionado |
| preenchimento cinza | resumo ou estado informativo |
| texto sublinhado | ação secundária ou explicação |
| círculos numerados | etapas, agrupamentos ou vínculo da seleção |
| linhas esquemáticas | estrutura territorial sem geografia real |
| marca textual | filtro ativo ou estado confirmado |
| ausência de marcador | posição da pessoa não utilizada |
| faixa compartilhada | painéis pertencem à mesma consulta |
| campo territorial vazio com mensagem | zero resultados sem depender da cartografia |
| aviso contextual | última alteração, cobertura ou seleção anterior |
| colunas simultâneas | visão dividida em tela ampla |
| painel recolhível | contexto da seleção sem eliminar comparação |

Cor, iconografia e tipografia não possuem significado definitivo.

## 7. Dimensões iniciais

| Wireframe | Canal | Dimensão de referência |
|---|---|---|
| Home pública | web para computador | 1.440 × 2.200 |
| Tela Hoje | aplicativo móvel | 390 × 844 |
| Mapa de Oportunidades | aplicativo móvel | 390 × 844 |
| Mapa sem localização | aplicativo móvel | 390 × 844 |
| Lista do Mapa | aplicativo móvel | 390 × 844 |
| Mapa sem resultados | aplicativo móvel | 390 × 844 |
| Mapa com resultados | web para computador | 1.440 × 1.024 |
| Mapa sem resultados | web para computador | 1.440 × 1.024 |
| Detalhe de oportunidade | aplicativo móvel | 390 × 980 |
| Cadastro pela Organização | web para computador | 1.440 × 1.024 |

As dimensões servem somente para verificar densidade e hierarquia.

## 8. Relação entre os wireframes

```text
Página Inicial pública
→ início voluntário
→ ambiente protegido
→ compreensão inicial revisada
→ Tela Hoje
→ Perto de mim
→ Mapa de Oportunidades
↔ Lista territorial do Mapa
→ resultados ou estado sem resultados
→ Detalhe de Oportunidade
→ decisão consciente

Explorar
↔ consulta territorial no Mapa
↔ Mapa e Lista sem perda de contexto
↔ visão dividida em tela ampla
↔ foco no Mapa ou na Lista
↔ retorno à visão dividida
↔ ajuste consciente da consulta
```

O início da jornada não garante recomendação. Cadastro não garante ativação. Apresentação não representa contratação.

## 9. Artefatos especializados

| Nome | ID | Superfície | Artefato |
|---|---|---|---|
| [Página Inicial e Início](uxa-020-home-and-journey-entry.md) | UXA-020 | primeira entrada | contrato textual |
| [Validação da Home](uxa-021-public-home-functional-validation-and-reformulation.md) | UXA-021 | Home | hierarquia validada |
| [Wireframe da Home](uxa-022-public-home-low-fidelity-wireframe.md) | UXA-022 | Home | arquivo vetorial |
| [Validação do Início Protegido](uxa-023-protected-journey-entry-functional-validation-and-reformulation.md) | UXA-023 | início protegido | contrato validado |
| [Tela Hoje](uxa-006-today-low-fidelity-wireframe.md) | UXA-006 | recorrente | arquivo vetorial |
| [Mapa](uxa-024-opportunity-map-low-fidelity-wireframe.md) | UXA-024 | Mapa | arquivo vetorial móvel |
| [Validação do Mapa](uxa-025-opportunity-map-functional-validation-and-reformulation.md) | UXA-025 | Mapa | validação funcional |
| [Mapa sem Localização](uxa-026-opportunity-map-location-disabled-state.md) | UXA-026 | estado alternativo | arquivo vetorial |
| [Validação sem Localização](uxa-027-opportunity-map-location-disabled-functional-validation-and-reformulation.md) | UXA-027 | estado alternativo | validação funcional |
| [Lista do Mapa](uxa-028-opportunity-map-list-state.md) | UXA-028 | modo alternativo | arquivo vetorial reformulado |
| [Validação da Lista](uxa-029-opportunity-map-list-functional-validation-and-reformulation.md) | UXA-029 | modo alternativo | validação funcional |
| [Mapa sem Resultados](uxa-030-opportunity-map-no-results-state.md) | UXA-030 | estado alternativo | arquivo vetorial reformulado |
| [Validação sem Resultados](uxa-031-opportunity-map-no-results-functional-validation-and-reformulation.md) | UXA-031 | estado alternativo | validação funcional |
| [Mapa para Computador](uxa-032-opportunity-map-desktop-reference.md) | UXA-032 | tela ampla | dois arquivos vetoriais reformulados |
| [Validação Desktop](uxa-033-opportunity-map-desktop-functional-validation-and-reformulation.md) | UXA-033 | tela ampla | validação funcional |
| [Detalhe](uxa-007-opportunity-detail-low-fidelity-wireframe.md) | UXA-007 | detalhe | arquivo vetorial |
| [Cadastro](uxa-008-organization-opportunity-registration-low-fidelity-wireframe.md) | UXA-008 | cadastro | arquivo vetorial |

## 10. Resultados móveis validados

A Lista, o estado sem localização e o estado sem resultados preservam consulta, localização opcional, explicabilidade, seleção, cobertura e operação textual sem mapa carregado.

## 11. Referência desktop validada

A UXA-032 reformulada e a UXA-033 demonstram:

- consulta territorial compartilhada;
- filtros consistentes;
- visão dividida;
- foco sem perda de contexto;
- movimento sem atualização automática;
- seleção `Marcador 1` sincronizada;
- cartões comparáveis e explicáveis;
- painel contextual recolhível;
- recuperação concentrada no painel de consulta;
- seleção anterior explicável;
- localização opcional;
- Lista integral sem mapa carregado.

A referência é funcionalmente válida após reformulação.

## 12. Demais estados funcionais do Mapa

Permanecem governados, sem wireframes específicos:

- localização aproximada;
- localização exata temporária;
- carregamento;
- baixa conectividade;
- item indisponível;
- endereço protegido;
- permissão revogada;
- erro de fonte;
- contexto sem gate;
- mapa indisponível.

## 13. Limites

Este programa não define marca, tecnologia, geocodificação, rotas, textos finais, responsividade, tablet, acessibilidade técnica, protótipo, teste de usabilidade, preço real ou Engenharia de Produto.

## 14. Próximos pontos de decisão

Os próximos pontos exigem autorizações separadas:

1. criar o wireframe do início protegido;
2. criar a referência móvel da Home;
3. validar a compreensão inicial;
4. detalhar a primeira Tela Hoje após a transição;
5. criar outros estados alternativos do Mapa;
6. criar referência para tablet, caso priorizada;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhuma etapa posterior é iniciada automaticamente.
