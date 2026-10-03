---
id: GKR-UX-PER010-MASTER-001
title: Jornada da Pessoa — PER-010 — Meus Objetivos — Documento Mestre de Superfície
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-25
normative: false
maturity: current_surface_design_definition
depends_on:
  - GKR-UX-PERSON-JOURNEY-READ-FIRST-001
  - GKR-UX-PERSON-JOURNEY-FLOW-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-UX-D5-C1-001
  - GKR-UX-D5-C4B-001
  - PAS-001-OBJ-FOUNDATION-001
  - PAS-001-OBJ-VIEW-001
related:
  - GKR-UX-PER008-MASTER-001
  - GKR-JOURNEY-PERSON-001
  - PER-008
  - PER-010
  - PER-011
  - PER-012
  - TRN-008
  - TRN-009
---

# Jornada da Pessoa — PER-010 — Meus Objetivos — Documento Mestre de Superfície

## 1. Finalidade

Este documento consolida a definição corrente de consumo de `PER-010 — Meus Objetivos` para designer humana, IA opcional, Produto, UX, Research, Legal/Privacidade e Engenharia.

`Meus Objetivos` existe para permitir que a Pessoa **compreenda, organize, revise e controle as direções e objetivos da própria jornada**, preservando autoria, autonomia, revisabilidade, privacidade e distinção entre declaração, sugestão, inferência e decisão confirmada.

A superfície não deve funcionar como painel de cobrança, produtividade, competição ou julgamento pessoal.

Este documento não cria layout, wireframe, UI, protótipo, sistema visual ou implementação.

## 2. Papel na Jornada

O handoff corrente com `Hoje` é:

```text
PER-008 — HOJE
→ TRN-008 / INTEGRALMENTE VALIDADA
→ PER-010 — MEUS OBJETIVOS
→ TRN-009 / INTEGRALMENTE VALIDADA
→ PER-008 — HOJE
```

Abrir `Meus Objetivos` não cria, confirma, altera ou prioriza um objetivo.

Retornar a `Hoje` não salva edição incompleta, não cria progresso e deve reconsultar o estado canônico vigente.

Não existem handoffs diretos contratados:

```text
PER-010 ↔ PER-011
PER-010 ↔ PER-012
```

Relação semântica entre capacidades não autoriza navegação direta.

## 3. Job da Pessoa

Em `Meus Objetivos`, a Pessoa precisa conseguir, conforme estado e autorização:

1. compreender quais objetivos existem;
2. distinguir objetivos de intenções, sonhos, possibilidades, tarefas e oportunidades;
3. diferenciar objetivo assumido de proposta ou inferência;
4. compreender estado e prioridade separadamente;
5. organizar objetivos sem hierarquia moral;
6. revisar formulação, significado, prioridade e atualidade;
7. compreender critérios, marcos e evidências;
8. compreender progresso sem falsa precisão;
9. reconhecer dependências e conflitos;
10. criar ou assumir conscientemente objetivos;
11. editar, pausar, retomar, reformular, retirar, concluir ou reabrir quando aplicável;
12. consultar histórico;
13. controlar compartilhamentos e proteger conteúdo sensível;
14. compreender quais capacidades utilizam determinado objetivo;
15. permanecer em exploração quando ainda não houver definição suficiente.

## 4. Definições que não podem ser colapsadas

```text
OBJETIVO
≠ TAREFA
≠ OPORTUNIDADE
≠ PRIORIDADE
≠ DESEJO EXTERNO
≠ OBRIGAÇÃO
```

Um objetivo representa resultado, condição, transformação ou direção que a Pessoa deseja alcançar, desenvolver, preservar ou experimentar.

Um objetivo pode permanecer amplo, exploratório ou incompleto sem perder legitimidade.

A Guivos não deve exigir precisão artificial.

## 5. Autoria e aceitação consciente

Todo objetivo ativo deve possuir autoria ou aceitação consciente da Pessoa.

Fontes possíveis podem incluir:

- declaração direta;
- formulação construída a partir de expressão da Pessoa;
- proposta da Guivos;
- contexto autorizado;
- fonte externa autorizada.

Uma proposta ou inferência não deve ser apresentada como objetivo confirmado.

```text
SUGESTÃO
≠ OBJETIVO CONFIRMADO

INFERÊNCIA
≠ DECISÃO DA PESSOA
```

Interação, pesquisa, compra, conteúdo consumido ou comportamento não criam objetivo ativo por si.

## 6. Estados funcionais

A solução deve conseguir representar, quando aplicável, estados como:

- exploração;
- proposto;
- confirmado;
- ativo;
- pausado;
- bloqueado;
- em revisão;
- concluído;
- retirado;
- arquivado/histórico;
- reaberto ou reativado quando autorizado.

Esses estados pertencem à responsabilidade de `PER-010`.

```text
ESTADO DO OBJETIVO
≠ NOVA SUPERFÍCIE
≠ NOVO PER-ID
```

A transição entre estados deve respeitar a autoridade funcional da Capacidade de Objetivos.

## 7. Portfólio de objetivos

A Pessoa pode possuir múltiplos objetivos simultaneamente.

A organização pode permitir perspectivas como:

- ativos;
- em exploração;
- pausados;
- bloqueados;
- em revisão;
- concluídos;
- retirados;
- históricos;
- sensíveis;
- sem prioridade;
- com conflitos;
- próximos de revisão.

Um mesmo objetivo pode aparecer em mais de uma perspectiva sem ser duplicado funcionalmente.

Filtros, ordenação ou agrupamento não devem alterar o estado do objetivo.

## 8. Estado e prioridade são independentes

Prioridade deve permanecer separada do estado funcional.

```text
OBJETIVO ATIVO
≠ OBJETIVO PRIORITÁRIO

SEM PRIORIDADE DEFINIDA
≠ OBJETIVO INVÁLIDO
```

A solução pode distinguir:

- prioridade declarada;
- prioridade sugerida;
- motivo da sugestão;
- contexto ou período da prioridade.

Prioridade sugerida não deve parecer decisão já aplicada.

Receita, patrocínio, disponibilidade comercial ou interesse organizacional não devem determinar objetivo ou prioridade pessoal.

## 9. Formulação e significado

A Pessoa deve poder compreender e revisar:

- o que o objetivo representa;
- por que importa, quando declarado;
- origem;
- formulação;
- significado;
- estado;
- prioridade;
- prazo, quando aplicável;
- critérios;
- marcos;
- relações;
- dependências;
- evidências;
- progresso;
- atualidade;
- histórico.

Ausência de motivação registrada não reduz a legitimidade do objetivo.

Prazo não é obrigatório para todo objetivo.

## 10. Critérios e marcos

A Pessoa pode indicar o que representaria avanço ou conclusão.

Objetivos sem critério formal continuam legítimos.

A ausência de critério deve ser apresentada como estado informativo e revisável, não como erro.

Marcos não devem ser fabricados para produzir sensação de progresso.

## 11. Progresso

Progresso só deve ser apresentado de forma compatível com a natureza do objetivo e com evidência disponível.

Podem existir, conforme autoridade:

- marco alcançado;
- condição mantida;
- progresso declarado;
- progresso inferido;
- progresso ainda não avaliado;
- ausência de evidência suficiente;
- mudança ou redução de condição anteriormente mantida.

Não deve existir percentual apenas para tornar a experiência visualmente atraente.

```text
AUSÊNCIA DE EVIDÊNCIA
≠ AUSÊNCIA DE PROGRESSO

PROGRESSO INFERIDO
≠ PROGRESSO CONFIRMADO
```

## 12. Progresso inferido

Quando houver inferência legítima sobre progresso, ela deve ser explicitamente identificada como inferência.

A Pessoa deve poder:

- compreender a base;
- revisar evidências;
- confirmar quando aplicável;
- contestar;
- corrigir;
- manter em aberto.

A inferência não pode produzir conclusão silenciosa.

## 13. Evidências

Evidências podem possuir naturezas diferentes, como:

- declaração da Pessoa;
- observação;
- evidência institucional;
- evidência contextual;
- inferência;
- outras fontes autorizadas.

A solução deve preservar, quando aplicável:

- origem;
- natureza;
- relação com o objetivo;
- atualidade;
- confiança quando legitimamente aplicável;
- contestação;
- conflitos entre evidências.

Evidências conflitantes devem permanecer visíveis como conflito legítimo e impedir conclusão silenciosa.

## 14. Dependências e relações

Objetivos podem possuir relações como dependência, apoio, conflito ou sequência quando contratadas pela autoridade funcional.

A experiência deve explicar dependências relevantes sem apresentá-las como impossibilidade absoluta quando houver alternativas.

Relações sugeridas pela Guivos permanecem sugestões até confirmação quando produzirem efeito relevante.

## 15. Conflitos

Quando objetivos entrarem em tensão, a Guivos pode tornar o conflito compreensível.

Não deve decidir silenciosamente qual objetivo prevalece.

A Pessoa pode, conforme contrato funcional:

- revisar;
- alterar prioridade;
- criar sequência;
- pausar;
- reformular;
- retirar.

Conflito não é falha pessoal.

## 16. Domínios de Evolução

Um objetivo pode possuir `0..n domain_link` conforme o modelo corrente de Domínios de Evolução.

```text
DOMÍNIO DE EVOLUÇÃO
≠ OBJETIVO
≠ PRIORIDADE
≠ SCORE
```

Vincular um objetivo a um domínio não determina importância, mérito ou progresso.

## 17. Contexto Vivo

Objetivos devem ser compreendidos à luz do contexto vigente.

A superfície pode apresentar contexto relevante quando autorizado, mas não deve:

- transformar contexto em objetivo automaticamente;
- inferir prioridade como decisão;
- manter informação revogada como vigente;
- expor conteúdo sensível sem necessidade.

Mudanças relevantes de contexto podem justificar revisão, não mutação silenciosa.

## 18. Ações conscientes

Conforme estado e autorização, a Pessoa pode possuir controles para:

- criar;
- confirmar;
- editar;
- ativar;
- revisar;
- alterar prioridade;
- pausar;
- retomar;
- reformular;
- retirar;
- concluir;
- reabrir ou reativar;
- controlar compartilhamento.

A presença de um controle não executa a ação.

Ações com impacto material devem exigir intenção compatível e confirmação proporcional.

## 19. Pausa, retirada e conclusão

Pausar um objetivo não representa fracasso.

Retirar um objetivo deve fazer com que ele deixe de orientar novas decisões.

Concluir um objetivo não deve equivaler automaticamente a avaliação de transformação pessoal.

Objetivos pausados, alterados, substituídos, retirados ou abandonados não devem ser apresentados como falhas pessoais.

Quando a autoridade permitir reabertura, conclusão anterior permanece parte do histórico.

## 20. Histórico

O histórico pode permitir compreender:

- criação;
- confirmação;
- mudanças de formulação;
- alterações de prioridade;
- pausas e retomadas;
- revisões;
- evidências relevantes;
- conclusão;
- retirada;
- reabertura.

Histórico não deve ser usado como mecanismo de cobrança ou score pessoal.

## 21. Explicabilidade

A Pessoa deve poder compreender, quando material:

- por que um objetivo aparece;
- sua origem;
- por que determinada prioridade foi sugerida;
- por que está próximo de revisão;
- por que determinado progresso foi reconhecido ou inferido;
- por que uma conclusão foi sugerida;
- quais evidências foram consideradas;
- quais capacidades utilizam o objetivo.

Explicação não deve afirmar que uma sugestão representa a escolha correta.

## 22. Compartilhamento e privacidade

A existência de um objetivo não autoriza compartilhamento automático.

Objetivos sensíveis devem receber proteção proporcional.

A solução deve evitar exposição desnecessária em:

- resumos;
- notificações;
- dispositivos compartilhados;
- superfícies não necessárias à finalidade.

Quando houver compartilhamento autorizado, a Pessoa deve conseguir compreender destinatário, finalidade e escopo conforme autoridade vigente.

## 23. Retorno a Hoje

`TRN-009 — PER-010 → PER-008` é integralmente validada.

```text
RETORNAR A HOJE
≠ SALVAR EDIÇÃO INCOMPLETA
≠ ALTERAR PRIORIDADE
≠ CRIAR PROGRESSO
≠ CONFIRMAR SUGESTÃO
≠ CONCLUIR OBJETIVO
```

O retorno deve reconsultar o estado canônico vigente.

## 24. Ausência e estados vazios

São estados legítimos:

- nenhum objetivo registrado;
- nenhum objetivo ativo;
- objetivos somente em exploração;
- ausência de prioridade definida;
- ausência de critério;
- ausência de evidência suficiente;
- ausência de progresso avaliado;
- ausência de conflito;
- ausência de histórico relevante.

A solução não deve fabricar objetivos, prioridades, progresso ou evidências para preencher a superfície.

## 25. Falha e recuperação

Falhas não devem produzir mutações silenciosas.

A recuperação deve:

- preservar estado canônico;
- evitar duplicidade;
- informar resultado real;
- permitir nova tentativa quando legítima;
- não converter edição incompleta em alteração;
- não ampliar autorização;
- não criar objetivo ou progresso.

## 26. Proteções

Devem permanecer verdadeiras:

- objetivos pertencem à Pessoa;
- a Guivos não escolhe objetivos pela Pessoa;
- sugestão não equivale a decisão;
- inferência não equivale a confirmação;
- prioridade não equivale a estado;
- quantidade de objetivos não mede valor pessoal;
- ambição não mede mérito;
- conclusão não mede sucesso humano;
- ausência de progresso observado não prova ausência de avanço;
- pausa não é fracasso;
- retirada não é fracasso;
- objetivo sensível não deve ser exposto indevidamente;
- patrocínio não determina objetivo;
- navegação não altera objeto;
- relação semântica não cria handoff.

## 27. Linguagem

A linguagem deve:

- preservar autoria;
- evitar cobrança;
- evitar julgamento moral;
- evitar gamificação coercitiva;
- evitar score humano;
- diferenciar sugestão, inferência, estado e decisão;
- tratar objetivos exploratórios como legítimos;
- comunicar incerteza;
- explicar progresso sem falsa precisão;
- tratar pausa, retirada e reformulação sem linguagem de fracasso.

## 28. Acessibilidade

A futura solução deve considerar:

- operação por teclado;
- foco visível;
- hierarquia compreensível sem depender apenas de cor;
- estados anunciáveis por tecnologia assistiva;
- rótulos compreensíveis;
- controles com nome e consequência claros;
- zoom e responsividade;
- preferência por movimento reduzido;
- conteúdo histórico e relações compreensíveis sem depender apenas de visualização gráfica.

## 29. Conteúdo sintético para Design

Design pode simular:

- objetivos fictícios;
- estados diversos;
- objetivo em exploração;
- prioridade declarada e sugerida;
- objetivo sem prioridade;
- objetivo sem critério;
- marcos fictícios;
- evidências fictícias;
- progresso declarado e inferido;
- conflito fictício;
- dependência fictícia;
- pausa, retirada, conclusão e reabertura;
- estado vazio;
- falha e recuperação.

Não pode apresentar como real:

- objetivo da Pessoa;
- dado pessoal real;
- evidência real;
- progresso real;
- conclusão real;
- prioridade real;
- compartilhamento real;
- score humano;
- implementação técnica.

## 30. Liberdade de Design

A designer pode decidir:

- quantidade de frames;
- composição;
- componentes;
- hierarquia;
- tipografia;
- paleta;
- iconografia;
- densidade;
- representação de portfólio;
- representação de estados;
- representação de relações;
- representação de progresso;
- filtros;
- agrupamentos;
- motion;
- microinterações;
- responsividade.

O GKR não define baseline visual obrigatório para `PER-010`.

Estados internos não criam novas superfícies.

## 31. Uso por IA

Quando IA for usada para explorar `PER-010`, o contexto mínimo deve incluir:

1. `GKR-UX-PERSON-JOURNEY-READ-FIRST-001`;
2. `GKR-UX-PERSON-JOURNEY-FLOW-001`;
3. este Documento Mestre;
4. Surface Registry e detalhamento da Pessoa;
5. Transition Registry;
6. `GKR-UX-D5-C1-001`;
7. `GKR-UX-D5-C4B-001`;
8. `PAS-001-OBJ-FOUNDATION-001`;
9. `PAS-001-OBJ-VIEW-001`;
10. `GKR-UX-PER008-MASTER-001` para a fronteira com `Hoje`.

A IA não pode:

- escolher objetivo pela Pessoa;
- transformar inferência em objetivo;
- criar prioridade silenciosamente;
- inventar progresso;
- inventar evidência;
- concluir objetivo;
- criar score humano;
- expor objetivo sensível;
- transformar estados em novos `PER-IDs`;
- criar handoff direto para `PER-011` ou `PER-012`;
- alterar `TRN-008/009`;
- iniciar Product Engineering.

## 32. Critérios de Aceite Funcional

Uma futura solução visual de `PER-010` é aceitável quando:

1. preserva autoria da Pessoa;
2. distingue objetivo de tarefa, oportunidade e prioridade;
3. distingue sugestão/inferência de objetivo confirmado;
4. permite objetivos amplos ou exploratórios;
5. estado e prioridade permanecem independentes;
6. múltiplos objetivos podem coexistir;
7. filtros não alteram objetos;
8. progresso não usa falsa precisão;
9. progresso inferido é explicitamente identificado;
10. ausência de evidência não vira ausência de progresso;
11. evidências conflitantes não produzem conclusão silenciosa;
12. dependências não são apresentadas como impossibilidade absoluta sem base;
13. conflitos não são resolvidos silenciosamente pela Guivos;
14. pausa, retirada e reformulação não são tratadas como fracasso;
15. objetivos sensíveis recebem proteção proporcional;
16. compartilhamento não é presumido;
17. `TRN-008/009` permanecem integralmente validadas;
18. retorno a `Hoje` não salva edição incompleta nem cria progresso;
19. não cria handoff direto para `PER-011/012`;
20. estados internos não criam novos `PER-IDs`;
21. Product Engineering permanece não liberado.

## 33. Limites

Este Documento Mestre não:

- cria tela final;
- cria Figma;
- cria protótipo;
- implementa Objetivos;
- define algoritmo de priorização;
- define score de progresso;
- escolhe objetivo;
- cria obrigação;
- cria objetivo a partir de comportamento;
- autoriza compartilhamento;
- define integralmente Próximos Passos;
- define integralmente Evolução;
- cria navegação direta `PER-010 ↔ PER-011/012`;
- altera `TRN-008/009`;
- executa testes com usuários;
- inicia Product Engineering.

## 34. Estado Corrente

```text
PER-010 MASTER
→ CURRENT DESIGN DEFINITION

ENTRY
→ TRN-008 / INTEGRALLY VALIDATED

RETURN
→ TRN-009 / INTEGRALLY VALIDATED

CORE
→ UNDERSTAND
→ ORGANIZE
→ REVIEW
→ CONTROL OBJECTIVES

AUTHORSHIP
→ PERSON

STATE
→ SEPARATE FROM PRIORITY

PROGRESS
→ EVIDENCE-COMPATIBLE
→ NO FALSE PRECISION

INFERENCE
→ EXPLICIT
→ REVIEWABLE

DIRECT HANDOFFS TO PER-011 / PER-012
→ NONE CONTRACTED

NEXT DOCUMENTATION TARGET
→ PER-011 — MEUS PRÓXIMOS PASSOS

NEW VISUAL MATERIALIZATION
→ NONE

PRODUCT ENGINEERING
→ NOT RELEASED BY THIS DOCUMENT
```
