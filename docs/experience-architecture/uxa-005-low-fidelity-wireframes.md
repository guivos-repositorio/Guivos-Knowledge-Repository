---
id: UXA-005
title: Programa Inicial de Wireframes de Baixa Fidelidade
status: draft
version: 0.33.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-02
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
  - UXA-047
  - UXA-048
  - UXA-049
  - UXA-050
  - UXA-051
  - UXA-052
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
23. validação e reformulação da gestão da campanha ativa — UXA-047;
24. relatório agregado — UXA-048;
25. validação e reformulação do relatório agregado — UXA-049;
26. validação transversal do conjunto completo do Opportunity Boost — UXA-050;
27. configuração móvel do anunciante — UXA-051;
28. validação e reformulação da configuração móvel — UXA-052.

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

### 5.7 Opportunity Boost — gestão da campanha ativa validada

A UXA-047 confirmou, após reformulação:

- campanha programada distinguível de campanha ativa;
- ativação condicionada à permanência dos gates;
- orçamento total, reservado, utilizado e saldo não utilizado compreensíveis;
- indicadores operacionais associados a período e atualização;
- impressões e cliques separados de conversão, atribuição e impacto;
- estado ativo mostrando período, frequência, capacidade, informação material e política;
- limitação distinguível de pausa e apresentada como entrega reduzida;
- limite diário preservado e período sem ampliação automática;
- atualização de capacidade sem promessa de normalização imediata;
- pausa voluntária, pausa automática e suspensão por política com consequências próprias;
- pausa interrompendo novos eventos sem apagar eventos válidos anteriores;
- período podendo continuar e expirar durante a pausa;
- condição de retomada visível e controle indisponível enquanto houver bloqueio;
- alteração material comparando versão aprovada e alterada;
- nova avaliação ou descarte sem entrega automática;
- cancelamento bloqueado até motivo e confirmações completas;
- estados finais e reconciliação distinguíveis;
- histórico e registro operacional preservados;
- saldo mantido como candidato, não como devolução confirmada.

### 5.8 Opportunity Boost — relatório agregado validado

A UXA-049 confirmou, após reformulação:

- entrega, interação, atribuição candidata e autorrelato distinguíveis;
- proveniência e estado apresentados junto de cada camada;
- orçamento total, utilizado e saldo não utilizado com significados claros;
- impressões, cliques, salvamentos, interesses e inscrições com rótulo, unidade e período;
- `não disponível`, `não exibido por agregação` e zero separados;
- supressão sem confirmação de existência ou ausência individual;
- limiar definitivo preservado para política especializada;
- atribuição candidata apresentada em agregados por tipo de evento;
- nenhuma linha representando pessoa ou sequência individual;
- versão da regra candidata vinculada ao período consultado;
- associação patrocinada, origem orgânica e origem indeterminada preservadas;
- dupla atribuição silenciosa proibida;
- autorrelato declarado e não verificado automaticamente;
- autorrelato não somado a eventos instrumentados;
- quantidade declarada sujeita a supressão;
- dados provisórios, em revisão, parcialmente reconciliados e reconciliados distinguíveis;
- reconciliação separada por tipo e unidade de evento;
- impressões e cliques não somados em total heterogêneo;
- saldo candidato sem promessa de crédito ou devolução;
- lista de visualizadores e dados individuais ausentes;
- conversão, causalidade e impacto humano não inferidos;
- versão móvel preservando hierarquia, proveniência, linguagem e limites.

### 5.9 Opportunity Boost — conjunto completo validado transversalmente

A UXA-050 confirma:

- 25 wireframes formando um percurso único;
- identidade da campanha preservada entre configuração, entrega, gestão e relatório;
- versão aprovada vinculada aos eventos correspondentes;
- alteração material sem reescrita do histórico;
- autoridade única das transições de estado;
- configuração e aprovação sem início automático de entrega;
- prévia e unidade entregue materialmente compatíveis;
- Lista e Mapa mantendo a mesma consulta;
- controles da pessoa sem identificação ou lista para o anunciante;
- preferência negativa prevalecendo sobre entrega contratada;
- orgânico e patrocinado separados até atribuição e relatório;
- identidade contínua do Boost Social Financiado;
- orçamento, saldo e reconciliação sem promessa financeira;
- histórico funcional e versão da regra candidata preservados;
- cobertura por canal explicitamente controlada.

### 5.10 Opportunity Boost — configuração móvel validada

A UXA-052 confirmou, após reformulação:

- cinco telas preservando a mesma campanha, rascunho e versão enviada;
- progresso e responsabilidade principal compreensíveis;
- estado salvo e retorno sem confirmação silenciosa;
- condição limitada ativa separada de bloqueio;
- regras de exceção explicitamente não ativas no exemplo;
- objetivo selecionado somente após escolha explícita;
- critérios escolhidos revisáveis ou removíveis;
- critérios protegidos excluídos;
- público insuficiente sem expansão automática;
- orçamento, limite diário, período e base principal separados;
- estimativa provisória com fatores, atualização e recálculo;
- renovação automática desativada como estado informativo;
- primeiro resultado orgânico anterior ao anúncio;
- controles da pessoa identificados como demonstração;
- resumo reaberto antes da confirmação;
- confirmações começando desmarcadas;
- envio separado de aprovação, programação, entrega e cobrança;
- versão enviada em somente leitura;
- cancelamento com revisão e confirmação separadas;
- histórico preservado.

### 5.11 Autonomia

- A pessoa pode adiar, recusar, pausar ou sair sem culpa?
- Recusar localização preserva o Mapa?
- Ocultar publicidade preserva o catálogo orgânico?
- Denúncia, contestação e preferência são ações distintas?
- O anunciante pode pausar, retomar ou cancelar com efeito conhecido?
- Alteração material não força confirmação ou nova entrega?
- O anunciante pode consultar dados ausentes ou suprimidos sem ser induzido a inferir zero ou causa?
- Preferências negativas prevalecem sobre a entrega contratada?
- O anunciante móvel pode voltar e revisar sem perda ou confirmação silenciosa do rascunho?

### 5.12 Continuidade

- A Home conduz conscientemente ao início protegido?
- A compreensão revisada conduz à Tela Hoje ou à exploração geral conforme a condição escolhida?
- Mapa e Lista preservam consulta, quantidade, atualização, ordenação e seleção?
- O fluxo do anunciante termina em avaliação sem iniciar entrega?
- Cartão e explicação preservam natureza comercial?
- Os estados patrocinados preservam consulta e preferências entre Lista e Mapa?
- A campanha programada conduz ao estado ativo somente na condição válida?
- Pausa, limitação, alteração material e encerramento preservam orçamento e histórico?
- O encerramento conduz a reconciliação e relatório sem reescrever origens ou prometer devolução?
- A mesma identidade e versão aprovada permanecem reconhecíveis ao longo do percurso?
- Configuração móvel e configuração para computador preservam responsabilidades equivalentes sem presumir composição idêntica?

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
| ação indisponível textual | condição ainda não atendida |
| camada numerada do relatório | entrega, interação, atribuição candidata ou autorrelato |
| rótulo de proveniência | instrumentado, calculado, declarado, não disponível ou em revisão |
| estado `não disponível` | ausência de dado sem substituição por zero |
| estado `não exibido por agregação` | supressão de contagem sem confirmação individual |
| regra candidata versionada | método e período preservados no histórico |
| agregado por tipo de evento | mensuração sem linha ou sequência individual |
| identidade transversal da campanha | vínculo entre oportunidade, versão, estado, entrega e relatório |
| progresso móvel de etapa | posição no fluxo sem autorizar avanço automático |
| resumo expansível móvel | conteúdo secundário acessível sem ocultar condição material |
| ação móvel condicionada | continuidade somente após gates, escolhas e confirmações válidos |
| regra de exceção não ativa | condição hipotética separada do estado atual |
| estado informativo móvel | condição como renovação desativada sem caixa de consentimento |
| controles da pessoa em demonstração | ações visíveis na prévia sem serem controles do anunciante |
| revisão de cancelamento | consequência apresentada antes da confirmação separada |

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
| Configuração móvel do anunciante — cinco estados | aplicativo móvel | 390 × 844 cada |
| Cartão e explicação padrão | móvel e computador | 390 × 844 e 1.440 × 1.024 |
| Boost Social Financiado | aplicativo móvel | 390 × 844 cada |
| Lista e Mapa patrocinados | móvel e computador | 390 × 844 e 1.440 × 1.024 |
| Gestão da campanha ativa — seis estados | web para computador | 1.440 × 1.024 cada |
| Relatório agregado — quatro estados | computador e aplicativo móvel | 1.440 × 1.024 e 390 × 844 |

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
→ cartão | Lista | Mapa patrocinados
→ explicação e controles
→ limitação | pausa | alteração material
→ conclusão | cancelamento | suspensão
→ reconciliação
→ relatório agregado
```

A configuração móvel materializa e valida as cinco primeiras responsabilidades sem alterar a autoridade das transições posteriores.

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
| Fluxo do anunciante para computador | UXA-040 | painel institucional | cinco arquivos vetoriais reformulados |
| Validação do fluxo para computador | UXA-041 | painel institucional | validação funcional especializada |
| Configuração móvel do anunciante | UXA-051 | painel institucional móvel | cinco arquivos vetoriais reformulados |
| Validação da configuração móvel | UXA-052 | painel institucional móvel | validação funcional especializada |
| Cartão e explicação | UXA-042 | experiência da pessoa | seis arquivos vetoriais reformulados |
| Validação do cartão | UXA-043 | participante | validação funcional especializada |
| Lista e Mapa patrocinados | UXA-044 | Mapa e Lista | quatro arquivos vetoriais reformulados |
| Validação de Lista e Mapa | UXA-045 | participante | validação funcional especializada |
| Gestão da campanha ativa | UXA-046 | painel institucional | seis arquivos vetoriais reformulados |
| Validação da gestão ativa | UXA-047 | painel institucional | validação funcional especializada |
| Relatório agregado | UXA-048 | painel institucional | quatro arquivos vetoriais reformulados |
| Validação do relatório agregado | UXA-049 | painel institucional | validação funcional especializada |
| Validação transversal do conjunto | UXA-050 | anunciante e participante | consolidação funcional de 25 wireframes |

## 10. Resultados validados e materializados

### 10.1 Compreensão inicial

A UXA-036 reformulada e a UXA-037 demonstram processamento sem tarefa oculta, afirmações individualizadas, revisão sem resposta padrão, relato original separado, persistência e personalização independentes e base insuficiente sem pressão.

### 10.2 Opportunity Boost

A UXA-038 a UXA-041 demonstram experiência funcional governada e fluxo inicial do anunciante para computador validado.

A UXA-042 reformulada e a UXA-043 demonstram cartão, explicação, controles e variação social funcionalmente válidos.

A UXA-044 reformulada e a UXA-045 demonstram Lista e Mapa patrocinados funcionalmente válidos em móvel e computador.

A UXA-046 reformulada e a UXA-047 demonstram gestão de campanha funcionalmente válida em seis estados para computador.

A UXA-048 reformulada e a UXA-049 demonstram relatório agregado funcionalmente válido em quatro estados para computador e móvel.

A UXA-050 demonstra que os 25 wireframes anteriores formam um percurso único, com identidade, versão aprovada, estados, controles, origem, histórico, mensuração e cobertura por canal consolidados.

A UXA-051 reformulada e a UXA-052 demonstram configuração móvel funcionalmente válida em cinco estados. O Opportunity Boost passa a possuir 30 wireframes materializados, com configuração validada em computador e aplicativo móvel.

## 11. Limites

Este programa não define marca, tecnologia, autenticação, armazenamento, IA, textos finais, responsividade, tablet, acessibilidade técnica, algoritmo publicitário, tecnologia cartográfica, política final de atribuição, agregação, reconciliação, cobrança, protótipo, teste de usabilidade ou Engenharia de Produto.

Gestão móvel, estados completos de erro, inventário insuficiente e preferência publicitária permanecem não materializados ou não concluídos.

## 12. Próximos pontos de decisão

Os próximos pontos exigem autorizações separadas:

1. criar gestão móvel da campanha ativa;
2. criar estados de erro, inventário insuficiente e preferência publicitária;
3. definir protocolo de protótipo de baixa ou média fidelidade;
4. preparar plano de teste com Pessoas, Organizações e Coletivos;
5. criar a referência móvel da Home;
6. validar a transição para a primeira Tela Hoje;
7. criar referência do início protegido e da compreensão para computador;
8. criar referência para tablet, caso priorizada.

Nenhuma etapa posterior é iniciada automaticamente.
