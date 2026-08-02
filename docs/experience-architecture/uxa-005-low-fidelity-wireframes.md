---
id: UXA-005
title: Programa Inicial de Wireframes de Baixa Fidelidade
status: draft
version: 0.27.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-01
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
  - UXA-042
  - UXA-043
  - UXA-044
  - UXA-045
  - UXA-046
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
16. wireframes do fluxo do anunciante — UXA-040;
17. validação e reformulação dos wireframes do anunciante — UXA-041;
18. cartão patrocinado e explicação — UXA-042;
19. validação e reformulação do cartão e da explicação — UXA-043;
20. estados patrocinados para Lista e Mapa — UXA-044;
21. validação e reformulação dos estados patrocinados — UXA-045;
22. gestão da campanha ativa — UXA-046;
23. validação da gestão da campanha ativa — pendente;
24. relatório agregado — pendente.

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
- objetivo único sem seleção automática;
- critérios escolhidos e revisáveis;
- critérios proibidos antes do envio;
- público insuficiente sem ampliação silenciosa;
- orçamento, limite diário e duração sem promessa de resultado;
- base principal coerente com o objetivo;
- CPM e CPC não simultâneos;
- alcance estimado distinguível de garantia;
- ausência de renovação automática;
- primeiro resultado orgânico anterior ao anúncio;
- confirmações inicialmente desmarcadas;
- envio para avaliação sem entrega;
- cancelamento com retorno ao rascunho e histórico preservado.

### 5.5 Opportunity Boost — cartão e explicação validados

A UXA-043 confirmou, após reformulação:

- natureza patrocinada reconhecível antes do conteúdo;
- primeiro resultado orgânico antes do anúncio padrão e social;
- anunciante, financiador e beneficiário compreensíveis;
- publicidade distinguível de recomendação;
- critérios utilizados gerais e objetivos;
- critérios protegidos e contextos pessoais excluídos;
- ausência de lista de visualizadores;
- correspondência orgânica e distribuição paga separadas;
- ocultação, redução, desativação e reversão com escopos próprios;
- denúncia de conteúdo separada de contestação de dados;
- Boost Social Financiado sem transferência de autoridade;
- ocultação sem redução do catálogo orgânico.

### 5.6 Opportunity Boost — Lista e Mapa patrocinados validados

A UXA-045 confirmou, após reformulação:

- Lista e Mapa representam a mesma consulta territorial;
- resultados orgânicos e unidades pagas possuem contagens separadas;
- primeiro resultado orgânico aparece antes da unidade paga;
- inventário patrocinado não participa da ordenação orgânica;
- filtros de oportunidades e preferência publicitária são áreas distintas;
- marcadores e agrupamentos patrocinados são distinguíveis;
- marcador patrocinado não cobre oportunidade orgânica;
- marcador e cartão selecionados compartilham identificador;
- selecionar no Mapa não altera a ordem da Lista;
- localização permanece opcional;
- proximidade, distância e seleção não representam afinidade;
- mover o Mapa não executa consulta automática;
- `Pesquisar nesta área` exige decisão explícita;
- ocultação sincronizada preserva catálogo orgânico;
- pouca oferta orgânica reduz publicidade.

### 5.7 Opportunity Boost — gestão da campanha ativa pendente de validação

A UXA-046 deverá ser validada quanto a:

- estado programado ser distinguível de entrega ativa;
- orçamento reservado, utilizado e saldo serem compreensíveis;
- indicadores operacionais não parecerem relatório final ou impacto;
- estado ativo mostrar período, frequência, capacidade e informação material;
- limitação ser distinguível de pausa;
- limitação não sugerir aceleração de orçamento ou ampliação automática do período;
- pausa voluntária, pausa automática e suspensão por política terem consequências próprias;
- condição de retomada ser visível;
- alteração material comparar versão aprovada e alterada;
- nova avaliação não iniciar entrega automaticamente;
- cancelamento mostrar entrega futura, eventos válidos, orçamento utilizado e saldo candidato;
- confirmação de cancelamento começar desmarcada;
- estados finais e reconciliação serem distinguíveis;
- histórico permanecer acessível;
- linguagem e foco serem acessíveis.

O próximo artefato deverá ainda demonstrar relatório separado em entrega, interação, atribuição candidata e autorrelato.

### 5.8 Autonomia

- A pessoa pode adiar, recusar, pausar ou sair sem culpa?
- Recusar localização preserva o Mapa?
- Ocultar publicidade preserva o catálogo orgânico?
- Denúncia, contestação e preferência são ações distintas?
- O anunciante pode pausar, retomar ou cancelar com efeito conhecido?
- Alteração material não força confirmação ou nova entrega?

### 5.9 Continuidade

- A Home conduz conscientemente ao início protegido?
- A compreensão revisada conduz à Tela Hoje ou à exploração geral conforme a condição escolhida?
- Mapa e Lista preservam consulta, quantidade, atualização, ordenação e seleção?
- O fluxo do anunciante termina em avaliação sem iniciar entrega?
- Cartão e explicação preservam natureza comercial?
- Os estados patrocinados preservam consulta e preferências entre Lista e Mapa?
- A campanha programada conduz ao estado ativo somente na condição válida?
- Pausa, limitação, alteração material e encerramento preservam orçamento e histórico?

## 6. Convenções de baixa fidelidade

| Elemento | Convenção |
|---|---|
| retângulo com borda | área funcional ou cartão |
| preenchimento escuro | ação principal ou estado selecionado conscientemente |
| preenchimento cinza | resumo, informação ou ação indisponível |
| texto sublinhado | ação secundária ou explicação |
| estado textual nomeado | posição funcional sem obrigatoriedade linear |
| círculo vazio | escolha única ainda não realizada |
| caixa vazia | confirmação ainda não concedida |
| caixa preenchida | escolha realizada conscientemente |
| borda tracejada | limitação ou regra de exceção |
| ação com consequência | pausa, saída, cancelamento ou recusa explícita |
| selo textual anterior | natureza patrocinada antes do conteúdo |
| espaço patrocinado delimitado | distribuição paga separada do ranking orgânico |
| círculo com identificador O | marcador orgânico |
| quadrado com identificador P | marcador patrocinado |
| texto `selecionado` | vínculo entre marcador e cartão |
| agrupamento textual | contagens orgânicas e patrocinadas separadas |
| gate `Pesquisar nesta área` | consulta territorial após ação explícita |
| estado de campanha em caixa textual | situação operacional independente de cor |
| comparação lado a lado | versão aprovada e alteração material |

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
| Fluxo do anunciante — cinco estados | web para computador | 1.440 × 1.024 cada |
| Cartão e explicação padrão | móvel e computador | 390 × 844 e 1.440 × 1.024 |
| Boost Social Financiado | aplicativo móvel | 390 × 844 cada |
| Lista e Mapa patrocinados | móvel e computador | 390 × 844 e 1.440 × 1.024 |
| Gestão da campanha ativa — seis estados | web para computador | 1.440 × 1.024 cada |
| Relatório agregado | computador e aplicativo móvel | pendente |

## 8. Relação entre os wireframes

```text
oportunidade aprovada e ativa
→ elegibilidade para impulsionamento
→ objetivo e critérios
→ orçamento e duração
→ prévia e confirmação
→ envio para avaliação
→ aprovação e programação
→ campanha ativa
→ limitação | pausa | alteração material
→ conclusão | cancelamento
→ reconciliação
→ relatório agregado
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
| Validação do fluxo | UXA-041 | painel institucional | validação funcional especializada |
| Cartão e explicação | UXA-042 | experiência da pessoa | seis arquivos vetoriais reformulados |
| Validação do cartão | UXA-043 | participante | validação funcional especializada |
| Lista e Mapa patrocinados | UXA-044 | Mapa e Lista | quatro arquivos vetoriais reformulados |
| Validação de Lista e Mapa | UXA-045 | participante | validação funcional especializada |
| Gestão da campanha ativa | UXA-046 | painel institucional | seis arquivos vetoriais |

## 10. Resultados validados e materializados

### 10.1 Compreensão inicial

A UXA-036 reformulada e a UXA-037 demonstram processamento sem tarefa oculta, afirmações individualizadas, revisão sem resposta padrão, relato original separado, persistência e personalização independentes e base insuficiente sem pressão.

### 10.2 Opportunity Boost

A UXA-038 a UXA-041 demonstram experiência funcional governada e fluxo inicial do anunciante validado.

A UXA-042 reformulada e a UXA-043 demonstram cartão, explicação, controles e variação social funcionalmente válidos.

A UXA-044 reformulada e a UXA-045 demonstram Lista e Mapa patrocinados funcionalmente válidos em móvel e computador.

A UXA-046 materializa gestão de campanha em seis estados para computador, ainda sem validação funcional própria.

## 11. Limites

Este programa não define marca, tecnologia, autenticação, armazenamento, IA, textos finais, responsividade, tablet, acessibilidade técnica, algoritmo publicitário, tecnologia cartográfica, cobrança, protótipo, teste de usabilidade ou Engenharia de Produto.

## 12. Próximos pontos de decisão

Os próximos pontos exigem autorizações separadas:

1. validar funcionalmente e reformular os wireframes da UXA-046;
2. criar wireframe do relatório agregado;
3. validar funcionalmente o conjunto completo do Opportunity Boost;
4. criar estados móveis de gestão, se priorizados;
5. criar estados de erro, inventário insuficiente e preferência publicitária;
6. criar a referência móvel da Home;
7. validar a transição para a primeira Tela Hoje;
8. criar referência do início protegido e da compreensão para computador;
9. criar referência para tablet, caso priorizada.

Nenhuma etapa posterior é iniciada automaticamente.
