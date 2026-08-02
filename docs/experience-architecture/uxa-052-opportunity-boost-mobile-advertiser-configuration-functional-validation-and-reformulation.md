---
id: UXA-052
title: Validação Funcional e Reformulação dos Wireframes da Configuração Móvel do Anunciante do Opportunity Boost
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-02
parent: UXA-051
depends_on:
  - UXA-005
  - UXA-038
  - UXA-039
  - UXA-040
  - UXA-041
  - UXA-050
  - UXA-051
  - GEM-007-A1
  - GEM-010-A2
related:
  - UXA-042
  - UXA-046
  - UXA-048
  - GPA-007
  - M7.54
normative: false
---

# Validação Funcional e Reformulação dos Wireframes da Configuração Móvel do Anunciante do Opportunity Boost

## 1. Finalidade

Este documento valida funcionalmente os cinco wireframes móveis criados pela UXA-051 e registra as reformulações necessárias para preservar continuidade, compreensão e voluntariedade em tela pequena.

A pergunta de validação é:

> **A pessoa anunciante consegue reconhecer a mesma campanha e o mesmo rascunho, compreender a etapa atual, distinguir condição ativa de regra de exceção, revisar objetivo, critérios, orçamento e prévia e enviar ou cancelar sem acreditar que confirmou automaticamente uma escolha, iniciou entrega ou executou uma ação da pessoa participante?**

## 2. Resultado

O conjunto é considerado **funcionalmente válido após reformulação**.

A validação aprova a hierarquia e o comportamento funcional de baixa fidelidade. Ela não aprova design visual, responsividade técnica, acessibilidade técnica, política final, algoritmo, cobrança, protótipo, teste com usuários ou Engenharia de Produto.

## 3. Escopo examinado

Foram examinados:

1. progresso e navegação entre cinco etapas;
2. identidade da campanha e da versão candidata;
3. estado salvo e retorno entre etapas;
4. gates atendido, limitado e bloqueado;
5. condição limitada ativa;
6. regra de bloqueio crítico;
7. objetivo único e estado após escolha;
8. critérios escolhidos, removíveis e protegidos;
9. regra de público insuficiente;
10. orçamento total, limite diário e período;
11. base principal e estimativa agregada;
12. renovação automática;
13. primeiro resultado orgânico e espaço patrocinado;
14. controles demonstrativos da pessoa;
15. resumo revisável e confirmações afirmativas;
16. versão enviada, avaliação, histórico e cancelamento.

## 4. Lacunas identificadas

### 4.1 Identidade incompleta entre etapas

O identificador da campanha e a versão do rascunho apareciam integralmente apenas em parte das telas. Orçamento e outras etapas poderiam ser interpretados como uma configuração diferente ou um novo cálculo sem vínculo explícito.

### 4.2 Condições hipotéticas pareciam estados ativos

O exemplo de bloqueio crítico e a regra de público insuficiente apareciam junto do estado atual sem declaração suficientemente forte de que não estavam ativos naquele exemplo.

### 4.3 Objetivo escolhido parecia contradizer a regra inicial

A tela declarava que nenhuma opção vinha selecionada automaticamente e, ao mesmo tempo, mostrava uma opção selecionada sem rotular claramente que se tratava do estado posterior a uma escolha explícita.

### 4.4 Condição limitada não acompanhava visualmente o percurso

A capacidade limitada era apresentada no gate inicial, mas não permanecia reconhecível nas etapas de critérios, orçamento, prévia e envio.

### 4.5 Renovação automática parecia uma confirmação

Uma caixa vazia junto do texto sobre renovação automática poderia ser interpretada como opção que precisava ser marcada para desativar ou como consentimento pendente.

### 4.6 Proveniência da estimativa insuficiente

A estimativa não apresentava momento do cálculo nem declarava claramente que poderia mudar após revisão de critérios, capacidade ou valores.

### 4.7 Controles da pessoa pareciam ações do anunciante

Na prévia, `Por que estou vendo isto?`, `Ocultar` e `Denunciar` apareciam como links comuns, sem informar que eram demonstrações dos controles oferecidos à pessoa participante.

### 4.8 Cancelamento parecia ação imediata

A superfície final oferecia `Cancelar envio` sem uma etapa visível de revisão e confirmação separada, embora a consequência fosse relevante e devesse preservar a versão enviada e o histórico.

## 5. Reformulação aprovada

### 5.1 Identidade persistente

As cinco telas passam a apresentar, conforme o estado:

- identificador `BST-2026-081`;
- rascunho ou versão enviada;
- oportunidade vinculada;
- condição limitada quando ativa;
- indicação de rascunho salvo ou versão somente leitura.

A interface não mistura campanhas, rascunhos ou versões.

### 5.2 Estados atuais e regras de exceção

Condições hipotéticas passam a utilizar o rótulo:

`REGRA DE EXCEÇÃO · NÃO ATIVA NESTE EXEMPLO`.

A condição limitada ativa permanece separada e acompanha o percurso.

### 5.3 Objetivo após escolha explícita

A tela passa a declarar:

> **Estado após escolha explícita; nenhuma opção começa selecionada.**

O objetivo selecionado é reconhecido como decisão realizada naquela etapa, continua revisável e permanece associado à métrica principal.

### 5.4 Critérios revisáveis

Os critérios escolhidos passam a oferecer `Revisar ou remover`.

A superfície confirma que:

- a origem é objetiva;
- nenhum critério será ampliado silenciosamente;
- critérios protegidos não aparecem como opções;
- voltar não confirma alterações incompletas.

### 5.5 Condição limitada transversal

A condição limitada passa a ser visível em:

- gate de entrada;
- resumo do objetivo;
- orçamento;
- prévia;
- versão enviada.

Ela não equivale a bloqueio, não acelera orçamento e não garante entrega.

### 5.6 Estimativa com estado e atualização

A estimativa passa a ser rotulada como `cálculo provisório` e informa:

- fatores considerados;
- data e hora de atualização;
- possibilidade de mudança após revisão;
- ausência de garantia;
- ausência de prorrogação automática do período.

### 5.7 Renovação como estado informativo

A caixa de seleção é removida.

A superfície passa a declarar:

`RENOVAÇÃO AUTOMÁTICA: DESATIVADA POR PADRÃO`.

Esse estado não exige confirmação e não cria novo orçamento automaticamente.

### 5.8 Controles demonstrativos da pessoa

A prévia passa a identificar:

`CONTROLES EXIBIDOS À PESSOA · DEMONSTRAÇÃO`.

A superfície esclarece que esses controles não são ações do anunciante durante a configuração.

### 5.9 Revisão antes do cancelamento

A ação passa a ser `Revisar cancelamento`.

A superfície declara previamente que o cancelamento:

- exige confirmação separada;
- encerra a avaliação;
- devolve a campanha ao rascunho;
- não inicia entrega;
- preserva histórico e versão enviada.

## 6. Critérios funcionais confirmados

Após a reformulação, o conjunto demonstra que:

- as cinco telas representam a mesma campanha;
- rascunho e versão enviada são distinguíveis;
- a etapa atual é reconhecível sem depender apenas de cor;
- voltar preserva o rascunho sem confirmar alterações incompletas;
- condição limitada ativa não é confundida com bloqueio;
- regras de exceção não parecem estados atuais;
- objetivo único começa desmarcado no estado inicial;
- seleção exibida representa escolha explícita posterior;
- métrica principal permanece vinculada ao objetivo;
- critérios escolhidos podem ser revisados ou removidos;
- critérios protegidos permanecem excluídos;
- público insuficiente não provoca expansão automática;
- orçamento total, limite diário e período permanecem separados;
- CPM e CPC não são simultâneos;
- alteração de objetivo exige recálculo;
- estimativa possui estado, atualização e limites;
- renovação automática é um estado desativado, não consentimento;
- primeiro resultado orgânico precede o espaço patrocinado;
- publicidade é identificada antes do conteúdo;
- controles da pessoa são reconhecidos como demonstração;
- resumo pode ser reaberto antes das confirmações;
- confirmações começam desmarcadas e são independentes;
- envio não inicia aprovação, programação, entrega ou cobrança;
- versão enviada permanece em somente leitura;
- cancelamento exige revisão e confirmação separada;
- histórico permanece acessível.

## 7. Estado dos artefatos reformulados

A referência validada contém:

1. `uxa-051-opportunity-boost-eligibility-mobile.svg`;
2. `uxa-051-opportunity-boost-objective-audience-mobile.svg`;
3. `uxa-051-opportunity-boost-budget-schedule-mobile.svg`;
4. `uxa-051-opportunity-boost-preview-confirmation-mobile.svg`;
5. `uxa-051-opportunity-boost-submission-mobile.svg`.

Todos permanecem em baixa fidelidade, com dimensão de referência de 390 × 844 pixels.

## 8. Consistência com o canal para computador

A versão móvel preserva as mesmas responsabilidades funcionais do fluxo para computador:

| Responsabilidade | Computador | Aplicativo móvel |
|---|---|---|
| elegibilidade e gates | validada | validada após reformulação |
| objetivo e critérios | validada | validada após reformulação |
| orçamento e período | validada | validada após reformulação |
| prévia e confirmação | validada | validada após reformulação |
| envio para avaliação | validada | validada após reformulação |

Composição, densidade e revelação progressiva podem variar por canal, mas o significado material não pode variar.

## 9. Proteções preservadas

- pagamento não altera relevância orgânica;
- contexto protegido não alimenta publicidade;
- primeiro resultado orgânico permanece orgânico;
- critério novo não é adicionado silenciosamente;
- público insuficiente limita ou bloqueia sem expansão automática;
- condição limitada não equivale a inelegibilidade;
- orçamento e estimativa não garantem resultado;
- renovação automática permanece desativada;
- envio não inicia entrega ou cobrança;
- aprovação não inicia entrega automaticamente;
- controles da pessoa não identificam visualizadores para o anunciante;
- cancelamento preserva histórico;
- nenhuma urgência, culpa ou escassez artificial é utilizada.

## 10. Estado funcional

`functionally_valid_after_reformulation — five mobile advertiser configuration wireframes preserve campaign identity, draft continuity, active and exceptional states, explicit choices, provisional estimates, participant-control boundaries, affirmative confirmation and reviewed cancellation; prototype and testing not authorized`.

## 11. Limites

Esta validação não cria:

- gestão móvel da campanha ativa;
- estados completos de erro técnico;
- inventário insuficiente operacional;
- experiência detalhada de preferência publicitária;
- design visual final;
- responsividade implementada;
- acessibilidade técnica;
- protótipo navegável;
- teste com Organizações ou Coletivos;
- política final de preços, publicidade, atribuição ou reconciliação;
- algoritmo, antifraude, checkout, cobrança, campanha real ou Engenharia de Produto.

## 12. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar gestão móvel da campanha ativa;
2. criar estados de erro, inventário insuficiente e preferência publicitária;
3. definir protocolo de protótipo de baixa ou média fidelidade;
4. preparar plano de teste com Organizações e Coletivos;
5. desenvolver política especializada de publicidade, atribuição, agregação e reconciliação.

Nenhum ato é iniciado automaticamente.
