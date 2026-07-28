---
id: UXA-005
title: Programa Inicial de Wireframes de Baixa Fidelidade
status: draft
version: 0.16.0
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
  - UXA-034
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

## 3. Artefatos pela ordem funcional

1. Página Inicial e início da jornada — UXA-020;
2. validação da Home pública — UXA-021;
3. wireframe da Home para computador — UXA-022;
4. validação do início protegido — UXA-023;
5. wireframe móvel do início protegido — UXA-034;
6. wireframe da Tela Hoje — UXA-006;
7. wireframe móvel do Mapa — UXA-024;
8. validação do Mapa — UXA-025;
9. estado sem localização — UXA-026;
10. validação sem localização — UXA-027;
11. Lista do Mapa — UXA-028;
12. validação da Lista — UXA-029;
13. estado sem resultados — UXA-030;
14. validação sem resultados — UXA-031;
15. referência do Mapa para computador — UXA-032;
16. validação da referência para computador — UXA-033;
17. wireframe do Detalhe — UXA-007;
18. wireframe do Cadastro pela Organização — UXA-008.

## 4. Natureza dos artefatos

Os wireframes:

- são hipóteses estruturais para revisão;
- utilizam conteúdo ilustrativo;
- representam prioridade e relação funcional, não acabamento;
- não definem componentes técnicos;
- não constituem especificação de implementação;
- não autorizam protótipo de alta fidelidade.

Wireframe gráfico não equivale a validação funcional. Validação funcional não equivale a teste de usabilidade, design ou desenvolvimento.

## 5. O que deverá ser validado

### 5.1 Primeira entrada e início protegido

- A pessoa entende que saiu da Home pública?
- O ambiente protegido é explicado antes da autenticação?
- Fica claro que nenhuma coleta começou automaticamente?
- Entrar, criar conta e recuperar acesso são alternativas compreensíveis?
- Criar conta permanece separado de autorizar processamento?
- Explorar sem personalização permanece uma saída legítima?
- Texto, voz, arquivo e perguntas são percebidos como alternativas?
- A pessoa entende que pode começar com pouco?
- Finalidade e privacidade aparecem antes do uso material?
- Pausar, salvar rascunho e excluir possuem efeitos distintos?
- Original, transcrição, extração e interpretação são distinguíveis?
- A revisão antecede a autorização específica?
- Personalização permanece bloqueada antes do gate?

### 5.2 Mapa e superfícies recorrentes

- Mapa e Lista representam a mesma consulta?
- Quantidade, filtros e ordenação são compreensíveis?
- Resumo e controles dos filtros são semanticamente idênticos?
- Relação comercial está separada da relevância?
- Dados ausentes são apresentados sem inferência?
- O total zero é entendido como resultado da consulta atual?
- Cobertura, falha e indisponibilidade são distinguíveis?
- Em computador, filtros, Mapa, Lista e seleção parecem partes da mesma consulta?
- A seleção é reconhecível no marcador, cartão e painel?
- O painel contextual pode ser recolhido sem perder seleção?
- Foco e retorno preservam contexto?

### 5.3 Autonomia

- A pessoa pode adiar, recusar, pausar ou sair sem culpa?
- Modalidades não competem como exigências?
- Compartilhamento mínimo não é tratado como insuficiência pessoal?
- Voz e arquivos possuem explicação anterior?
- A pessoa pode corrigir, limitar, remover e excluir?
- A recusa de localização preserva o uso do Mapa?
- Mover o Mapa evita atualização silenciosa?
- O estado vazio evita preenchimento patrocinado artificial?

### 5.4 Continuidade

- A Home conduz conscientemente ao início protegido?
- O início protegido conduz a uma compreensão inicial revisável, não diretamente à personalização?
- A compreensão revisada conduz à Tela Hoje ou à exploração geral?
- Mapa e Lista preservam consulta, quantidade, atualização, ordenação e seleção?
- O Detalhe devolve a pessoa ao mesmo estado?
- A Lista funciona sem mapa carregado?

## 6. Convenções de baixa fidelidade

| Elemento | Convenção |
|---|---|
| retângulo com borda | área funcional ou cartão |
| preenchimento escuro | ação principal ou estado selecionado |
| preenchimento cinza | resumo ou estado informativo |
| texto sublinhado | ação secundária ou explicação |
| círculos numerados | etapas, agrupamentos ou vínculo da seleção |
| faixa de progresso | posição na sequência sem obrigatoriedade linear |
| caixa de seleção vazia | autorização ainda não concedida |
| declaração textual | estado de coleta, proteção ou processamento |
| ausência de marcador | posição da pessoa não utilizada |
| faixa compartilhada | painéis pertencem à mesma consulta |
| painel recolhível | contexto da seleção sem eliminar comparação |

Cor, iconografia e tipografia não possuem significado definitivo.

## 7. Dimensões iniciais

| Wireframe | Canal | Dimensão de referência |
|---|---|---|
| Home pública | web para computador | 1.440 × 2.200 |
| Início protegido — quatro estados | aplicativo móvel | 390 × 844 cada |
| Tela Hoje | aplicativo móvel | 390 × 844 |
| Mapa de Oportunidades | aplicativo móvel | 390 × 844 |
| Mapa sem localização | aplicativo móvel | 390 × 844 |
| Lista do Mapa | aplicativo móvel | 390 × 844 |
| Mapa sem resultados | aplicativo móvel | 390 × 844 |
| Mapa com resultados | web para computador | 1.440 × 1.024 |
| Mapa sem resultados | web para computador | 1.440 × 1.024 |
| Detalhe de oportunidade | aplicativo móvel | 390 × 980 |
| Cadastro pela Organização | web para computador | 1.440 × 1.024 |

## 8. Relação entre os wireframes

```text
Página Inicial pública
→ decisão voluntária
→ explicação do ambiente protegido
→ acesso protegido
→ modalidade e compartilhamento mínimo
→ revisão e autorização específica
→ compreensão inicial revisável
→ Tela Hoje ou exploração geral
→ Mapa e demais superfícies recorrentes
```

A sequência protegida não é formulário linear obrigatório. Etapas podem ser pausadas, retomadas ou omitidas quando isso preservar compreensão e autonomia.

## 9. Artefatos especializados

| Nome | ID | Superfície | Artefato |
|---|---|---|---|
| Página Inicial e Início | UXA-020 | primeira entrada | contrato textual |
| Validação da Home | UXA-021 | Home | hierarquia validada |
| Wireframe da Home | UXA-022 | Home | arquivo vetorial |
| Validação do Início Protegido | UXA-023 | início protegido | contrato validado |
| Wireframe do Início Protegido | UXA-034 | início protegido | quatro arquivos vetoriais móveis |
| Tela Hoje | UXA-006 | recorrente | arquivo vetorial |
| Mapa e estados | UXA-024 a UXA-032 | Mapa | arquivos vetoriais móveis e desktop |
| Validações do Mapa | UXA-025, UXA-027, UXA-029, UXA-031 e UXA-033 | Mapa | validações funcionais |
| Detalhe | UXA-007 | detalhe | arquivo vetorial |
| Cadastro | UXA-008 | cadastro | arquivo vetorial |

## 10. Resultado do início protegido

A UXA-034 demonstra:

- nenhuma coleta automática;
- conta separada de autorização;
- alternativas de acesso e exploração;
- modalidades equivalentes;
- compartilhamento mínimo;
- finalidade e privacidade;
- rascunho protegido;
- revisão do conteúdo;
- correção, remoção e limitação;
- autorização específica;
- personalização bloqueada antes do gate.

A validação funcional especializada do conjunto permanece não iniciada.

## 11. Limites

Este programa não define marca, tecnologia, autenticação, gravação, transcrição, upload, IA, textos finais, responsividade, tablet, acessibilidade técnica, protótipo, teste de usabilidade ou Engenharia de Produto.

## 12. Próximos pontos de decisão

Os próximos pontos exigem autorizações separadas:

1. validar funcionalmente o wireframe móvel do início protegido;
2. criar a referência móvel da Home;
3. validar a compreensão inicial;
4. detalhar a primeira Tela Hoje após a transição;
5. criar estados especializados de texto, voz e arquivos;
6. criar referência do início protegido para computador;
7. criar outros estados do Mapa;
8. retomar independentemente os testes dos Resultados Empresariais.

Nenhuma etapa posterior é iniciada automaticamente.
