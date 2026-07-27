---
id: UXA-005
title: Programa Inicial de Wireframes de Baixa Fidelidade
status: draft
version: 0.11.0
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
  - PAS-001
normative: false
---

# Programa Inicial de Wireframes de Baixa Fidelidade

## 1. Finalidade

Este programa materializa hipóteses de Arquitetura da Experiência em wireframes de baixa fidelidade. O objetivo é validar organização, hierarquia, conteúdo, ações e continuidade antes de identidade visual ou implementação.

## 2. Regra de ordem

Os identificadores preservam a ordem histórica de criação dos documentos. Eles não determinam a ordem das telas.

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
6. wireframe do Mapa — UXA-024;
7. validação do Mapa — UXA-025;
8. estado do Mapa sem localização — UXA-026;
9. validação do estado sem localização — UXA-027;
10. visualização em Lista do Mapa — UXA-028;
11. validação da Lista do Mapa — UXA-029;
12. wireframe do Detalhe — UXA-007;
13. wireframe do Cadastro pela Organização — UXA-008.

O Mapa integra a navegação recorrente e pode ser acessado pela Home, por `Explorar`, pelo bloco `Perto de mim` e pelo Detalhe.

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
- A diferença entre Home, início protegido, Tela Hoje, Explorar e Mapa é clara?
- Mapa e Lista representam a mesma consulta?
- A Lista territorial se diferencia de `Explorar`?
- A pessoa reconhece `Agindo como`, região e estado de localização?
- Quantidade, filtros e ordenação são compreensíveis?
- Relação comercial está separada de relevância?
- Dados ausentes são apresentados sem inferência?

### 5.2 Hierarquia

- O item mais importante ocupa a posição correta?
- A Home apresenta propósito antes das soluções comerciais?
- O Mapa preserva espaço territorial sem ocultar busca, filtros e privacidade?
- A Lista preserva contexto antes dos resultados?
- O total de filtros ativos é visível?
- A ordenação possui explicação acessível?
- Os cartões permitem comparação consistente?
- A oportunidade selecionada permanece reconhecível?

### 5.3 Autonomia

- A pessoa consegue conhecer o ecossistema sem iniciar a jornada?
- Localização exata, aproximada, manual e desativada são alternativas reais?
- A recusa de localização preserva busca, Mapa, Lista, Detalhe e salvamento?
- A troca de modo mantém permissões e contexto?
- A pessoa pode revisar filtros e ordenação?
- O fluxo evita pressão para consentimento ou contratação?

### 5.4 Continuidade

- A Home conduz ao início protegido, à compreensão e à Tela Hoje?
- A Tela Hoje conduz ao Mapa por um recorte compacto?
- Explorar e Mapa permanecem relacionados sem serem confundidos?
- Mapa e Lista preservam região, busca, filtros, quantidade, ordenação e seleção?
- O Detalhe devolve a pessoa ao mesmo contexto?
- A Lista funciona sem mapa carregado?

## 6. Convenções de baixa fidelidade

| Elemento | Convenção |
|---|---|
| retângulo com borda | área funcional ou cartão |
| preenchimento escuro | ação principal ou estado selecionado |
| preenchimento cinza | resumo ou estado informativo |
| texto sublinhado | ação secundária ou explicação |
| círculos numerados | etapas ou agrupamentos |
| linhas esquemáticas | estrutura territorial sem geografia real |
| marca textual | filtro ativo ou estado confirmado sem depender de cor |
| ausência de marcador | posição da pessoa não utilizada |
| declaração textual | confirmação de estado, contexto ou incerteza |

Cor, iconografia e tipografia não possuem significado definitivo.

## 7. Dimensões iniciais

| Wireframe | Canal | Dimensão de referência |
|---|---|---|
| Home pública | web para computador | 1.440 × 2.200 |
| Tela Hoje | aplicativo móvel | 390 × 844 |
| Mapa de Oportunidades | aplicativo móvel | 390 × 844 |
| Mapa sem localização | aplicativo móvel | 390 × 844 |
| Lista do Mapa | aplicativo móvel | 390 × 844 |
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
→ Detalhe de Oportunidade
→ decisão consciente

Explorar em descoberta ampla
↔ abrir consulta territorial no Mapa
↔ alternar Mapa e Lista sem perder contexto
```

O início da jornada não garante recomendação. Cadastro não garante ativação. Apresentação não representa recomendação definitiva nem contratação.

## 9. Artefatos especializados

| Nome | ID | Superfície | Artefato |
|---|---|---|---|
| [Página Inicial e Início](uxa-020-home-and-journey-entry.md) | UXA-020 | primeira entrada | contrato textual |
| [Validação da Home](uxa-021-public-home-functional-validation-and-reformulation.md) | UXA-021 | Home | hierarquia validada |
| [Wireframe da Home](uxa-022-public-home-low-fidelity-wireframe.md) | UXA-022 | Home | arquivo vetorial |
| [Validação do Início Protegido](uxa-023-protected-journey-entry-functional-validation-and-reformulation.md) | UXA-023 | início protegido | contrato validado |
| [Tela Hoje](uxa-006-today-low-fidelity-wireframe.md) | UXA-006 | recorrente | arquivo vetorial |
| [Mapa](uxa-024-opportunity-map-low-fidelity-wireframe.md) | UXA-024 | Mapa | arquivo vetorial |
| [Validação do Mapa](uxa-025-opportunity-map-functional-validation-and-reformulation.md) | UXA-025 | Mapa | validação funcional |
| [Mapa sem Localização](uxa-026-opportunity-map-location-disabled-state.md) | UXA-026 | estado alternativo | arquivo vetorial |
| [Validação sem Localização](uxa-027-opportunity-map-location-disabled-functional-validation-and-reformulation.md) | UXA-027 | estado alternativo | validação funcional |
| [Lista do Mapa](uxa-028-opportunity-map-list-state.md) | UXA-028 | modo alternativo | arquivo vetorial reformulado |
| [Validação da Lista](uxa-029-opportunity-map-list-functional-validation-and-reformulation.md) | UXA-029 | modo alternativo | validação funcional |
| [Detalhe](uxa-007-opportunity-detail-low-fidelity-wireframe.md) | UXA-007 | detalhe | arquivo vetorial |
| [Cadastro](uxa-008-organization-opportunity-registration-low-fidelity-wireframe.md) | UXA-008 | cadastro | arquivo vetorial |

## 10. Resultado validado da Lista

A UXA-028 reformulada demonstra:

- Lista territorial da mesma consulta do Mapa;
- contexto `Agindo como`;
- região manual e posição não acessada;
- pesquisa e filtros preservados;
- total consolidado de filtros;
- quantidade e atualização dos resultados;
- ordenação explicável;
- cartões comparáveis e incertezas declaradas;
- item selecionado preservado;
- explicação funcional e comércio separados;
- salvamento, origem e Detalhe;
- retorno ao Mapa;
- funcionamento sem mapa carregado.

A UXA-029 considera a Lista funcionalmente válida após reformulação.

## 11. Demais estados funcionais do Mapa

Permanecem governados, sem wireframes específicos:

- localização aproximada;
- localização exata temporária;
- ausência de resultados;
- carregamento;
- baixa conectividade;
- item indisponível;
- endereço protegido;
- permissão revogada;
- erro de fonte;
- contexto sem gate;
- mapa indisponível.

## 12. Limites

Este programa não define marca, tecnologia, geocodificação, rotas, textos finais, responsividade, acessibilidade técnica, protótipo, teste de usabilidade, preço real ou Engenharia de Produto.

## 13. Próximos pontos de decisão

Os próximos pontos exigem autorizações separadas:

1. criar o estado sem resultados;
2. criar referência do Mapa para computador;
3. criar o wireframe do início protegido;
4. criar a referência móvel da Home;
5. validar a compreensão inicial;
6. detalhar a primeira Tela Hoje após a transição;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhuma etapa posterior é iniciada automaticamente.
