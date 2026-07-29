---
id: UXA-005
title: Programa Inicial de Wireframes de Baixa Fidelidade
status: draft
version: 0.22.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-28
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
  - UXA-036
  - UXA-037
  - UXA-038
  - UXA-039
  - UXA-040
  - UXA-041
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
→ processamento temporário visível e interrompível
→ compreensão inicial apresentada como hipótese
→ revisão por afirmação
→ decisões sobre persistência e personalização
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
7. wireframe móvel da compreensão inicial — UXA-036;
8. validação do wireframe móvel da compreensão inicial — UXA-037;
9. wireframe da Tela Hoje — UXA-006;
10. wireframe móvel do Mapa — UXA-024;
11. validações e estados do Mapa — UXA-025 a UXA-033;
12. wireframe do Detalhe — UXA-007;
13. wireframe do Cadastro pela Organização — UXA-008;
14. contrato funcional reformulado do Opportunity Boost — UXA-038;
15. validação funcional especializada do Opportunity Boost — UXA-039;
16. wireframes do fluxo do anunciante do Opportunity Boost — UXA-040;
17. validação e reformulação dos wireframes do anunciante — UXA-041;
18. cartão, explicação, Lista, Mapa, gestão ativa e relatório do Boost — pendentes.

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
- O acesso aparece somente quando necessário?
- Criar conta permanece separado de autorizar processamento?
- Explorar sem personalização permanece saída legítima?
- Texto, voz, arquivo e perguntas são alternativas equivalentes?
- Compartilhamento mínimo é legítimo?
- Pausar, salvar, sair e excluir possuem efeitos distintos?
- A revisão antecede autorização específica?
- Autorizações começam desmarcadas?
- Recusar impede processamento?

### 5.2 Compreensão inicial

- Somente conteúdos autorizados entram no processamento?
- Interromper possui efeito explícito e impede tarefa oculta?
- Afirmações confirmadas, inferidas e desconhecidas são separadas?
- Momento Atual, avanço e Próximo Passo permanecem distintos?
- A compreensão é percebida como hipótese, não diagnóstico?
- Nenhuma resposta de revisão começa selecionada?
- Uma afirmação pode permanecer em aberto?
- Corrigir interpretação preserva o relato original?
- Persistência e personalização são escolhas únicas e independentes?
- Base insuficiente evita hipótese artificial e pressão?

### 5.3 Mapa e superfícies recorrentes

- Mapa e Lista representam a mesma consulta?
- Quantidade, filtros e ordenação são compreensíveis?
- Relação comercial está separada da relevância?
- Dados ausentes são apresentados sem inferência?
- Cobertura, falha e indisponibilidade são distinguíveis?
- Em computador, filtros, Mapa, Lista e seleção parecem partes da mesma consulta?

### 5.4 Opportunity Boost — fluxo do anunciante validado

A UXA-041 confirmou, após reformulação:

- gates com estados atendido, limitado e bloqueado;
- plano elegível sem substituir aprovação, capacidade ou segurança;
- objetivo único sem seleção automática;
- métrica principal compreensível;
- critérios escolhidos e revisáveis;
- critérios proibidos antes do envio;
- público insuficiente sem ampliação silenciosa;
- orçamento, limite diário e duração sem promessa de resultado;
- base principal coerente com o objetivo;
- CPM e CPC não simultâneos;
- alcance estimado distinguível de garantia;
- ausência de renovação automática;
- primeiro resultado orgânico anterior ao anúncio;
- confirmações afirmativas inicialmente desmarcadas;
- envio para avaliação sem entrega;
- cancelamento com retorno ao rascunho e histórico preservado.

Os próximos artefatos deverão demonstrar:

- cartão patrocinado independente;
- explicação `Por que estou vendo isto?`;
- Boost Social Financiado com financiador e beneficiário identificados;
- controles de ocultação com escopo e reversibilidade;
- redução da publicidade quando faltar inventário orgânico;
- marcador e agrupamento patrocinado próprios no Mapa;
- gestão da campanha ativa;
- relatório separado em entrega, interação, atribuição candidata e autorrelato;
- pausa e cancelamento com saldo, consequência e histórico visíveis.

### 5.5 Autonomia

- A pessoa pode adiar, recusar, pausar ou sair sem culpa?
- Compartilhamento mínimo não é tratado como insuficiência pessoal?
- Recusar localização preserva o uso do Mapa?
- Ocultar publicidade preserva o catálogo orgânico?
- Denúncia e preferência são tratadas como ações distintas?
- O anunciante pode salvar rascunho, voltar e cancelar com efeito conhecido?

### 5.6 Continuidade

- A Home conduz conscientemente ao início protegido?
- O início protegido conduz à compreensão inicial revisável?
- A compreensão revisada conduz à Tela Hoje ou à exploração geral conforme a condição escolhida?
- Mapa e Lista preservam consulta, quantidade, atualização, ordenação e seleção?
- A gestão da oportunidade conduz ao Boost somente quando não houver bloqueio crítico?
- O fluxo do anunciante termina em avaliação sem iniciar entrega?

## 6. Convenções de baixa fidelidade

| Elemento | Convenção |
|---|---|
| retângulo com borda | área funcional ou cartão |
| preenchimento escuro | ação principal ou estado selecionado conscientemente |
| preenchimento cinza | resumo, informação ou ação indisponível |
| texto sublinhado | ação secundária ou explicação |
| estado textual nomeado | posição funcional sem obrigatoriedade linear |
| círculo vazio | escolha única ainda não realizada |
| caixa vazia | autorização múltipla ainda não concedida |
| caixa preenchida | escolha múltipla realizada conscientemente |
| borda tracejada | ação indisponível ou regra de exceção |
| ação com consequência | pausa, saída, salvamento, exclusão ou recusa explícita |
| selo textual anterior | natureza patrocinada reconhecível antes do conteúdo |
| espaço patrocinado delimitado | distribuição paga sem integração silenciosa ao ranking orgânico |

Cor, iconografia e tipografia não possuem significado definitivo.

## 7. Dimensões iniciais

| Wireframe | Canal | Dimensão de referência |
|---|---|---|
| Home pública | web para computador | 1.440 × 2.200 |
| Início protegido — quatro estados | aplicativo móvel | 390 × 844 cada |
| Compreensão inicial — cinco estados | aplicativo móvel | 390 × 844 cada |
| Tela Hoje | aplicativo móvel | 390 × 844 |
| Mapa e estados móveis | aplicativo móvel | 390 × 844 |
| Mapa com e sem resultados | web para computador | 1.440 × 1.024 |
| Detalhe de oportunidade | aplicativo móvel | 390 × 980 |
| Cadastro pela Organização | web para computador | 1.440 × 1.024 |
| Fluxo do anunciante do Opportunity Boost — cinco estados | web para computador | 1.440 × 1.024 cada |
| Cartão, explicação, Lista, Mapa, gestão ativa e relatório do Boost | computador e aplicativo móvel | pendentes |

## 8. Relação entre os wireframes

Fluxo institucional relacionado:

```text
oportunidade aprovada e ativa
→ gestão da oportunidade
→ elegibilidade para impulsionamento
→ objetivo e critérios
→ orçamento e duração
→ prévia e confirmação
→ envio para avaliação
→ ajustes, rejeição ou aprovação
→ campanha futura
→ pausa, encerramento ou cancelamento
→ relatório agregado e reconciliação
```

## 9. Artefatos especializados

| Nome | ID | Superfície | Artefato |
|---|---|---|---|
| Página Inicial e Início | UXA-020 | primeira entrada | contrato textual |
| Validação da Home | UXA-021 | Home | hierarquia validada |
| Wireframe da Home | UXA-022 | Home | arquivo vetorial |
| Contrato do Início Protegido | UXA-023 | início protegido | validação funcional |
| Wireframe do Início Protegido | UXA-034 | início protegido | quatro arquivos vetoriais reformulados |
| Validação do Wireframe Protegido | UXA-035 | início protegido | validação funcional especializada |
| Wireframe da Compreensão Inicial | UXA-036 | compreensão inicial | cinco arquivos vetoriais reformulados |
| Validação da Compreensão Inicial | UXA-037 | compreensão inicial | validação funcional especializada |
| Tela Hoje | UXA-006 | recorrente | arquivo vetorial |
| Mapa e estados | UXA-024 a UXA-032 | Mapa | arquivos vetoriais móveis e desktop |
| Validações do Mapa | UXA-025, UXA-027, UXA-029, UXA-031 e UXA-033 | Mapa | validações funcionais |
| Detalhe | UXA-007 | detalhe | arquivo vetorial |
| Cadastro | UXA-008 | cadastro | arquivo vetorial |
| Contrato do Opportunity Boost | UXA-038 | Explorar, Lista, Mapa e gestão | contrato funcional reformulado |
| Validação do Opportunity Boost | UXA-039 | anunciante e participante | validação funcional especializada |
| Fluxo do anunciante | UXA-040 | painel institucional | cinco arquivos vetoriais reformulados |
| Validação do fluxo do anunciante | UXA-041 | painel institucional | validação funcional especializada |

## 10. Resultados validados

### 10.1 Compreensão inicial

A UXA-036 reformulada e a UXA-037 demonstram processamento sem tarefa oculta, afirmações individualizadas, revisão sem resposta padrão, relato original separado, persistência e personalização independentes, base insuficiente sem pressão e continuidade sem personalização.

### 10.2 Opportunity Boost

A UXA-038 a UXA-041 demonstram experiência funcional governada e fluxo inicial do anunciante validado, com elegibilidade explicável, critérios explícitos, base coerente, orgânico anterior ao anúncio, confirmação afirmativa e cancelamento compreensível.

## 11. Limites

Este programa não define marca, tecnologia, autenticação, armazenamento, IA, textos finais, responsividade, tablet, acessibilidade técnica, algoritmo publicitário, cobrança, protótipo, teste de usabilidade ou Engenharia de Produto.

## 12. Próximos pontos de decisão

Os próximos pontos exigem autorizações separadas:

1. criar wireframes do cartão patrocinado e da explicação de distribuição;
2. criar estados patrocinados para Lista e Mapa;
3. criar wireframes de gestão da campanha ativa;
4. criar wireframe do relatório agregado;
5. validar funcionalmente o conjunto completo do Opportunity Boost;
6. criar a referência móvel da Home;
7. validar a transição para a primeira Tela Hoje;
8. criar estados especializados de processamento, pausa, falha e retomada;
9. criar referência do início protegido e da compreensão para computador;
10. criar referência para tablet, caso priorizada.

Nenhuma etapa posterior é iniciada automaticamente.
