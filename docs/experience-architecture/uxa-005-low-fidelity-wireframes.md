---
id: UXA-005
title: Programa Inicial de Wireframes de Baixa Fidelidade
status: draft
version: 0.6.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-26
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
  - PAS-001
normative: false
---

# Programa Inicial de Wireframes de Baixa Fidelidade

## 1. Finalidade

Este programa materializa hipóteses de Arquitetura da Experiência em wireframes de baixa fidelidade. O objetivo é validar organização, hierarquia, conteúdo, ações e continuidade entre superfícies antes de qualquer decisão de identidade visual ou implementação.

## 2. Regra de ordem

Os identificadores preservam a ordem histórica de criação dos documentos. Eles não determinam a ordem em que as telas aparecem para a pessoa.

```text
Página Inicial pública da Guivos
→ início protegido da jornada
→ compreensão inicial revisável
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

A correção formal está registrada em [Correção da Ordem Funcional da Primeira Entrada Pessoal](uxa-003-a1-first-entry-functional-order.md).

## 3. Artefatos pela ordem funcional

1. **Página Inicial da Guivos e Início da Jornada** — UXA-020;
2. **Validação da Página Inicial Pública** — UXA-021;
3. **Wireframe da Página Inicial Pública** — UXA-022, para computador;
4. **Validação do Início Protegido da Jornada** — UXA-023;
5. **Wireframe da Tela Hoje** — UXA-006, depois da compreensão inicial suficiente e autorizada;
6. **Wireframe do Mapa de Oportunidades** — UXA-024, como superfície recorrente própria;
7. **Wireframe do Detalhe de Oportunidade** — UXA-007;
8. **Wireframe do Cadastro pela Organização** — UXA-008.

O Mapa não entra entre a Home e a Tela Hoje. Ele integra a navegação recorrente e pode ser acessado pela Home, por Explorar, pelo bloco `Perto de mim` e pelo detalhe de uma oportunidade.

## 4. Natureza dos artefatos

Os wireframes:

- são hipóteses estruturais para revisão;
- utilizam conteúdo ilustrativo, não dados reais;
- representam prioridade e relação funcional, não acabamento;
- podem ser alterados sem migração de produto;
- não definem componentes técnicos;
- não constituem especificação de implementação;
- não substituem contratos especializados;
- não autorizam protótipo de alta fidelidade.

Wireframes textuais e arquivos gráficos vetoriais possuem natureza preparatória. Um arquivo gráfico materializa a hierarquia para inspeção, mas não equivale a identidade visual, protótipo navegável ou desenvolvimento.

## 5. O que deverá ser validado

### 5.1 Compreensão

- A finalidade de cada superfície é compreendida rapidamente?
- A diferença entre Home, início protegido, Tela Hoje, Explorar e Mapa é clara?
- A pessoa reconhece que a Home pública não coleta relatos pessoais?
- O participante compreende o que merece atenção na Tela Hoje?
- A alternância entre lista e mapa representa a mesma descoberta?
- Preço, condições, elegibilidade, origem e relação comercial estão claros?
- Ações principais e alternativas são distinguíveis?

### 5.2 Hierarquia

- O item mais importante ocupa a posição correta?
- A Home apresenta propósito antes das soluções comerciais?
- Os caminhos pessoal, geral e institucional permanecem distintos?
- O Mapa preserva espaço territorial sem ocultar pesquisa, filtros e privacidade?
- O cartão selecionado oferece contexto suficiente antes do detalhe?
- Estados vazios e ausência legítima permanecem possíveis?

### 5.3 Autonomia

- A pessoa consegue conhecer o ecossistema sem iniciar a jornada?
- A pessoa escolhe como relatar no ambiente protegido?
- O participante consegue alterar filtros, raio, localização e relevância?
- Localização exata, aproximada, manual e desativada são alternativas reais?
- O fluxo evita pressionar contratação ou inscrição?

### 5.4 Continuidade

- A Home conduz naturalmente ao início protegido, à compreensão e à Tela Hoje?
- A Tela Hoje conduz ao Mapa por um recorte compacto, sem incorporar o mapa completo?
- Explorar e Mapa permanecem sincronizados?
- O Mapa conduz ao Detalhe de Oportunidade preservando contexto e condições?
- O cadastro organizacional produz informações suficientes para cartão, detalhe, mapa, busca e comparação?

## 6. Convenções de baixa fidelidade

| Elemento | Convenção |
|---|---|
| retângulo com borda | área funcional ou cartão |
| preenchimento escuro | ação principal ou estado selecionado |
| preenchimento cinza | resumo, estado informativo ou área auxiliar |
| texto sublinhado | ação secundária ou explicação |
| círculos numerados | etapas ou agrupamentos |
| linhas e formas esquemáticas | estrutura territorial sem geografia real |

Cor, iconografia e tipografia não possuem significado definitivo neste programa.

## 7. Dimensões iniciais

| Wireframe | Canal | Dimensão de referência |
|---|---|---|
| Página Inicial pública da Guivos | web para computador | 1.440 × 2.200 |
| Tela Hoje | aplicativo móvel | 390 × 844 |
| Mapa de Oportunidades | aplicativo móvel | 390 × 844 |
| Detalhe de oportunidade | aplicativo móvel | 390 × 980 |
| Cadastro pela Organização | web para computador | 1.440 × 1.024 |

As dimensões servem somente para verificar densidade e hierarquia. Responsividade e adaptação a outros dispositivos permanecem pendentes.

## 8. Relação entre os wireframes

```text
Página Inicial pública da Guivos
→ início voluntário da jornada
→ ambiente protegido
→ compreensão inicial revisada e confirmada
→ Tela Hoje
→ Perto de mim
→ Mapa de Oportunidades
→ Detalhe de Oportunidade
→ decisão consciente de salvar, comparar ou iniciar processo

Explorar em lista
↔ visualizar no Mapa
↔ abrir Detalhe de Oportunidade

Organização
→ cadastro governado da oportunidade
→ avaliação e ativação
→ apresentação na Tela Hoje, em Explorar, no Mapa ou em intervenção contextual
```

O início da jornada não garante recomendação. O cadastro não garante ativação. A ativação não garante apresentação. A apresentação não representa recomendação definitiva nem contratação.

Antes da compreensão inicial confirmada, as soluções poderão apresentar somente conteúdo geral, institucional, editorial ou resultante de busca explícita, sem afirmar relevância pessoal.

## 9. Artefatos especializados

| Nome completo | Identificador | Superfície | Artefato visual |
|---|---|---|---|
| [Página Inicial da Guivos e Início da Jornada](uxa-020-home-and-journey-entry.md) | UXA-020 | Home e início protegido | wireframes textuais |
| [Validação da Página Inicial Pública](uxa-021-public-home-functional-validation-and-reformulation.md) | UXA-021 | Home pública | hierarquia validada |
| [Wireframe da Página Inicial Pública](uxa-022-public-home-low-fidelity-wireframe.md) | UXA-022 | Home pública | [arquivo vetorial](../assets/wireframes/uxa-022-public-home-desktop.svg) |
| [Validação do Início Protegido](uxa-023-protected-journey-entry-functional-validation-and-reformulation.md) | UXA-023 | início protegido | contrato validado; wireframe pendente |
| [Wireframe da Tela Hoje](uxa-006-today-low-fidelity-wireframe.md) | UXA-006 | Tela Hoje | [arquivo vetorial](../assets/wireframes/uxa-006-hoje-mobile.svg) |
| [Wireframe do Mapa de Oportunidades](uxa-024-opportunity-map-low-fidelity-wireframe.md) | UXA-024 | Mapa recorrente | [arquivo vetorial](../assets/wireframes/uxa-024-opportunity-map-mobile.svg) |
| [Wireframe do Detalhe de Oportunidade](uxa-007-opportunity-detail-low-fidelity-wireframe.md) | UXA-007 | detalhe | [arquivo vetorial](../assets/wireframes/uxa-007-opportunity-detail-mobile.svg) |
| [Wireframe do Cadastro pela Organização](uxa-008-organization-opportunity-registration-low-fidelity-wireframe.md) | UXA-008 | cadastro | [arquivo vetorial](../assets/wireframes/uxa-008-organization-opportunity-registration-desktop.svg) |

## 10. Resultado do Mapa de Oportunidades

O wireframe gráfico do Mapa materializa:

- contexto de atuação explícito;
- pesquisa territorial;
- alternância entre mapa e lista;
- filtros compactos;
- mapa esquemático sem geografia real;
- camadas de oportunidades, Organizações, Coletivos e eventos;
- agrupamentos e pontos selecionáveis;
- localização aproximada declarada;
- cartão resumido de oportunidade;
- preço, distância, data, vagas, acessibilidade e origem;
- explicação de relevância e relação comercial;
- ações de detalhe, salvamento e rota;
- navegação recorrente com Mapa selecionado.

O arquivo representa conteúdo ilustrativo e não cria localidades, ofertas, coordenadas ou dados reais.

## 11. Limites

Este programa não:

- aprova navegação como definitiva;
- define marca, paleta, tipografia ou ilustração;
- define tecnologia ou fornecedor de mapas;
- cria geocodificação, rotas ou rastreamento;
- define textos finais de interface;
- conclui acessibilidade ou responsividade;
- cria protótipo navegável;
- executa teste de usabilidade;
- define preço ou oferta comercial real;
- inicia Engenharia de Produto.

## 12. Próximos pontos de decisão

Os próximos pontos deverão ser autorizados separadamente e poderão:

1. validar funcionalmente o wireframe do Mapa de Oportunidades;
2. criar estados alternativos do Mapa;
3. criar referência do Mapa para computador;
4. criar o wireframe gráfico do início protegido;
5. criar a referência móvel da Home;
6. validar a compreensão inicial e seus controles;
7. detalhar a primeira Tela Hoje após a transição;
8. retomar independentemente os testes dos Resultados Empresariais.

Nenhuma etapa posterior é iniciada automaticamente.
