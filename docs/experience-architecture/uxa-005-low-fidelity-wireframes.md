---
id: UXA-005
title: Programa Inicial de Wireframes de Baixa Fidelidade
status: draft
version: 0.17.0
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
  - UXA-035
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
→ explicação do ambiente protegido
→ acesso, quando necessário
→ escolha e rascunho mínimo
→ revisão e autorização específica
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
6. validação do wireframe móvel do início protegido — UXA-035;
7. wireframe da Tela Hoje — UXA-006;
8. wireframe móvel do Mapa — UXA-024;
9. validações e estados do Mapa — UXA-025 a UXA-033;
10. wireframe do Detalhe — UXA-007;
11. wireframe do Cadastro pela Organização — UXA-008.

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
- Nenhum relato pessoal é solicitado antes da explicação?
- Dados de acesso e conteúdo da jornada são distinguíveis?
- Os quatro artefatos são compreendidos como estados possíveis, não formulário obrigatório?
- O acesso aparece somente quando necessário?
- Sessão válida evita repetição da etapa de acesso?
- Criar conta permanece separado de autorizar processamento?
- Explorar sem personalização permanece saída legítima?
- Texto, voz, arquivo e perguntas são alternativas equivalentes?
- Nenhuma modalidade é selecionada automaticamente?
- Compartilhamento mínimo é legítimo?
- Voz e arquivo possuem explicação anterior?
- Pausar, salvar, sair e excluir possuem efeitos distintos?
- Original, transcrição, extração e interpretação são distinguíveis?
- A revisão antecede autorização específica?
- Autorizações começam desmarcadas?
- Recusar impede processamento?
- Persistência e personalização permanecem bloqueadas antes do gate?

### 5.2 Mapa e superfícies recorrentes

- Mapa e Lista representam a mesma consulta?
- Quantidade, filtros e ordenação são compreensíveis?
- Relação comercial está separada da relevância?
- Dados ausentes são apresentados sem inferência?
- Cobertura, falha e indisponibilidade são distinguíveis?
- Em computador, filtros, Mapa, Lista e seleção parecem partes da mesma consulta?

### 5.3 Autonomia

- A pessoa pode adiar, recusar, pausar ou sair sem culpa?
- Modalidades não competem como exigências?
- Compartilhamento mínimo não é tratado como insuficiência pessoal?
- A pessoa pode corrigir, limitar, remover e excluir?
- Não autorizar possui consequência clara e não punitiva?
- A recusa de localização preserva o uso do Mapa?

### 5.4 Continuidade

- A Home conduz conscientemente ao início protegido?
- O início protegido conduz a uma compreensão inicial revisável, não diretamente à persistência ou personalização?
- A compreensão revisada conduz à Tela Hoje ou à exploração geral?
- Mapa e Lista preservam consulta, quantidade, atualização, ordenação e seleção?

## 6. Convenções de baixa fidelidade

| Elemento | Convenção |
|---|---|
| retângulo com borda | área funcional ou cartão |
| preenchimento escuro | ação principal ou estado selecionado |
| preenchimento cinza | resumo ou estado informativo |
| texto sublinhado | ação secundária ou explicação |
| estado textual nomeado | posição funcional sem obrigatoriedade linear |
| caixa de seleção vazia | autorização ainda não concedida |
| declaração textual | estado de relato, acesso, rascunho ou processamento |
| ação com consequência | pausa, saída, salvamento, exclusão ou recusa explícita |
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
| Mapa e estados móveis | aplicativo móvel | 390 × 844 |
| Mapa com e sem resultados | web para computador | 1.440 × 1.024 |
| Detalhe de oportunidade | aplicativo móvel | 390 × 980 |
| Cadastro pela Organização | web para computador | 1.440 × 1.024 |

## 8. Relação entre os wireframes

```text
Página Inicial pública
→ decisão voluntária
→ explicação do ambiente protegido
→ acesso, somente quando necessário
→ modalidade e rascunho mínimo
→ revisão e autorização específica
→ compreensão inicial temporária e revisável
→ decisão sobre persistência e personalização
→ Tela Hoje ou exploração geral
→ Mapa e demais superfícies recorrentes
```

A sequência protegida é pausável e retomável. Acesso, modalidades e conteúdos poderão ser omitidos quando não aplicáveis.

## 9. Artefatos especializados

| Nome | ID | Superfície | Artefato |
|---|---|---|---|
| Página Inicial e Início | UXA-020 | primeira entrada | contrato textual |
| Validação da Home | UXA-021 | Home | hierarquia validada |
| Wireframe da Home | UXA-022 | Home | arquivo vetorial |
| Contrato do Início Protegido | UXA-023 | início protegido | validação funcional |
| Wireframe do Início Protegido | UXA-034 | início protegido | quatro arquivos vetoriais reformulados |
| Validação do Wireframe Protegido | UXA-035 | início protegido | validação funcional especializada |
| Tela Hoje | UXA-006 | recorrente | arquivo vetorial |
| Mapa e estados | UXA-024 a UXA-032 | Mapa | arquivos vetoriais móveis e desktop |
| Validações do Mapa | UXA-025, UXA-027, UXA-029, UXA-031 e UXA-033 | Mapa | validações funcionais |
| Detalhe | UXA-007 | detalhe | arquivo vetorial |
| Cadastro | UXA-008 | cadastro | arquivo vetorial |

## 10. Resultado do início protegido

A UXA-034 reformulada e a UXA-035 demonstram:

- relato separado de dados de acesso;
- estados nomeados e não obrigatórios;
- acesso condicional;
- modalidades equivalentes;
- compartilhamento mínimo;
- explicação anterior para voz e arquivo;
- rascunho com estado declarado;
- revisão do conteúdo;
- autorização desmarcada e específica;
- recusa sem processamento;
- compreensão inicial temporária;
- persistência e personalização bloqueadas antes do gate.

O conjunto é funcionalmente válido após reformulação.

## 11. Limites

Este programa não define marca, tecnologia, autenticação, armazenamento, gravação, transcrição, upload, IA, textos finais, responsividade, tablet, acessibilidade técnica, protótipo, teste de usabilidade ou Engenharia de Produto.

## 12. Próximos pontos de decisão

Os próximos pontos exigem autorizações separadas:

1. criar a referência móvel da Home;
2. materializar a revisão da compreensão inicial;
3. detalhar a primeira Tela Hoje após a transição;
4. criar estados especializados de texto, voz e arquivos;
5. criar referência do início protegido para computador;
6. criar estados de processamento, pausa, falha e retomada;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhuma etapa posterior é iniciada automaticamente.
