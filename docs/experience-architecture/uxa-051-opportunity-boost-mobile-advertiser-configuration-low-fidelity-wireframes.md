---
id: UXA-051
title: Wireframes de Baixa Fidelidade da Configuração Móvel do Anunciante do Opportunity Boost
status: active
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-02
parent: UXA-050
depends_on:
  - UXA-005
  - UXA-038
  - UXA-039
  - UXA-040
  - UXA-041
  - UXA-050
  - GEM-007-A1
  - GEM-010-A2
related:
  - UXA-052
  - UXA-042
  - UXA-046
  - UXA-048
  - GPA-007
  - M7.54
normative: false
---

# Wireframes de Baixa Fidelidade da Configuração Móvel do Anunciante do Opportunity Boost

## 1. Finalidade

Este documento materializa a referência gráfica reformulada e funcionalmente validada da configuração móvel do anunciante do Opportunity Boost em cinco wireframes de baixa fidelidade.

A versão móvel preserva as responsabilidades já validadas no fluxo para computador sem presumir responsividade automática, equivalência visual ou implementação compartilhada.

O conjunto representa:

1. elegibilidade e gate de entrada;
2. objetivo e critérios de distribuição;
3. orçamento, duração e estimativa;
4. prévia e confirmação;
5. envio para avaliação.

A UXA-052 considera o conjunto **funcionalmente válido após reformulação**.

## 2. Posição no percurso governado

```text
gestão da oportunidade
→ abrir configuração móvel
→ verificar elegibilidade e bloqueios
→ reconhecer condição limitada ativa, quando houver
→ escolher objetivo único
→ escolher, revisar ou remover critérios permitidos
→ revisar critérios protegidos e regra de público insuficiente
→ definir orçamento, duração e limite diário
→ revisar base principal e estimativa provisória
→ visualizar primeiro resultado orgânico e unidade patrocinada
→ distinguir controles demonstrativos da pessoa
→ confirmar responsabilidades
→ enviar para avaliação
→ acompanhar histórico ou revisar cancelamento
```

Configurar, confirmar, enviar ou aprovar não inicia entrega, cobrança, programação ou campanha ativa.

## 3. Canal e dimensão

- canal: aplicativo móvel;
- largura de referência: 390 pixels;
- altura de referência: 844 pixels;
- orientação: retrato;
- fidelidade: baixa;
- contexto: painel móvel de Organização ou Coletivo;
- estado: funcionalmente validado após reformulação pela UXA-052.

## 4. Princípios estruturais móveis

A versão móvel utiliza:

- uma responsabilidade principal por tela;
- progresso explícito de cinco etapas;
- identidade persistente da campanha e da versão;
- estado salvo ou versão enviada em somente leitura;
- revelação progressiva de detalhes;
- ação principal condicionada ao estado da etapa;
- retorno sem perda silenciosa do rascunho;
- separação entre estado atual e regra de exceção;
- nenhuma seleção automática;
- nenhuma ampliação silenciosa de critérios;
- nenhuma promessa de alcance, conversão ou impacto.

A redução de espaço não autoriza remover bloqueios, critérios protegidos, consequências, origem da estimativa ou confirmações.

## 5. Artefatos visuais reformulados

### 5.1 Elegibilidade e gate de entrada

![Elegibilidade móvel validada do Opportunity Boost](../assets/wireframes/uxa-051-opportunity-boost-eligibility-mobile.svg)

`docs/assets/wireframes/uxa-051-opportunity-boost-eligibility-mobile.svg`

Demonstra:

- campanha, rascunho, oportunidade e anunciante vinculados;
- etapa 1 de 5;
- estados `Atendido`, `Atendido com limite` e `Bloqueado`;
- condição limitada ativa separada da regra hipotética de bloqueio;
- regra de exceção rotulada como não ativa;
- quantidade de bloqueios críticos;
- continuidade com limite somente quando nenhum bloqueio crítico permanecer;
- condição limitada acompanhando etapas posteriores.

### 5.2 Objetivo e critérios de distribuição

![Objetivo e critérios móveis validados do Opportunity Boost](../assets/wireframes/uxa-051-opportunity-boost-objective-audience-mobile.svg)

`docs/assets/wireframes/uxa-051-opportunity-boost-objective-audience-mobile.svg`

Demonstra:

- etapa 2 de 5;
- identidade e condição limitada preservadas;
- estado posterior a uma escolha explícita;
- aviso de que nenhuma opção começa selecionada;
- objetivo único e métrica principal;
- critérios permitidos escolhidos, revisáveis e removíveis;
- origem objetiva dos critérios;
- critérios protegidos e contextos pessoais excluídos;
- regra de público insuficiente não ativa no exemplo;
- ausência de ampliação automática.

### 5.3 Orçamento, duração e estimativa

![Orçamento móvel validado do Opportunity Boost](../assets/wireframes/uxa-051-opportunity-boost-budget-schedule-mobile.svg)

`docs/assets/wireframes/uxa-051-opportunity-boost-budget-schedule-mobile.svg`

Demonstra:

- etapa 3 de 5;
- identidade, objetivo e condição limitada preservados;
- orçamento total e limite diário;
- início e término;
- uma única base principal coerente com o objetivo;
- proibição de cobrança simultânea por CPM e CPC;
- recálculo exigido quando o objetivo muda;
- estimativa provisória com fatores e atualização;
- ausência de garantia e de prorrogação automática;
- renovação automática desativada como estado informativo, não confirmação.

### 5.4 Prévia e confirmação

![Prévia móvel validada do Opportunity Boost](../assets/wireframes/uxa-051-opportunity-boost-preview-confirmation-mobile.svg)

`docs/assets/wireframes/uxa-051-opportunity-boost-preview-confirmation-mobile.svg`

Demonstra:

- etapa 4 de 5;
- identidade, rascunho e condição limitada preservados;
- primeiro resultado orgânico anterior ao espaço patrocinado;
- natureza patrocinada anterior ao conteúdo;
- controles da pessoa identificados como demonstração;
- aviso de que esses controles não são ações do anunciante;
- resumo reaberto e revisável;
- possibilidade de recálculo após revisão;
- confirmações afirmativas inicialmente desmarcadas;
- envio indisponível enquanto houver pendências.

### 5.5 Envio para avaliação

![Envio móvel validado para avaliação do Opportunity Boost](../assets/wireframes/uxa-051-opportunity-boost-submission-mobile.svg)

`docs/assets/wireframes/uxa-051-opportunity-boost-submission-mobile.svg`

Demonstra:

- etapa 5 de 5;
- estado `Em avaliação`;
- identificador e versão enviada em somente leitura;
- resumo com condição limitada;
- itens que serão verificados;
- ausência de entrega antes da aprovação e programação válida;
- ausência de cobrança real;
- próximos estados possíveis sem promessa;
- histórico acessível;
- revisão e confirmação separadas antes do cancelamento;
- preservação da versão enviada e do histórico.

## 6. Continuidade entre as etapas

O conjunto preserva a mesma campanha por meio de:

- identificador da campanha;
- oportunidade vinculada;
- anunciante responsável;
- rascunho ou versão enviada;
- objetivo principal após a escolha;
- condição limitada, quando ativa;
- orçamento e período após a definição;
- estado atual da configuração.

Voltar permite revisar o rascunho sem confirmar alterações incompletas. Nenhuma revisão altera silenciosamente critérios, base, orçamento, período ou condição.

## 7. Semântica dos gates

```text
Atendido
→ permite continuidade

Atendido com limite
→ permite continuidade com alcance ou entrega potencialmente reduzida

Bloqueado
→ impede continuidade até correção
```

Regras hipotéticas são rotuladas como `não ativas neste exemplo`. A interface não converte condição limitada em bloqueio e não permite que contratação de plano substitua aprovação, segurança, atualização, capacidade ou responsabilidade institucional.

## 8. Seleções, estados e confirmações

- objetivo utiliza escolha única;
- o estado selecionado representa escolha explícita posterior;
- critérios permitidos podem ser revisados ou removidos;
- critérios protegidos não aparecem como opções selecionáveis;
- público insuficiente aparece como regra de exceção;
- renovação automática é estado desativado, não caixa de consentimento;
- estimativa é cálculo provisório com atualização;
- resumo permanece acessível antes da confirmação;
- confirmações finais exigem ações afirmativas independentes;
- abandonar ou voltar não confirma escolhas pendentes;
- envio somente ocorre após revisão completa;
- cancelamento exige revisão e confirmação separada.

## 9. Proteções preservadas

- pagamento não altera relevância orgânica;
- primeiro resultado orgânico permanece orgânico;
- contexto protegido não alimenta publicidade;
- critério novo não é adicionado silenciosamente;
- público insuficiente limita ou bloqueia sem expansão automática;
- condição limitada permanece visível e não garante entrega;
- CPM e CPC não são cobrados simultaneamente;
- orçamento e estimativa não garantem resultado;
- renovação automática permanece desativada por padrão;
- prévia não representa posição orgânica comprada;
- controles demonstrativos da pessoa não são ações do anunciante;
- envio e aprovação não iniciam entrega;
- anunciante não recebe lista de pessoas;
- cancelamento preserva histórico;
- nenhum texto cria urgência, culpa ou escassez artificial.

## 10. Resultado funcional

A pergunta funcional do conjunto é:

> **A pessoa anunciante reconhece a mesma campanha e o mesmo rascunho, compreende o progresso, distingue estados atuais de exceções, realiza escolhas explícitas, interpreta estimativa e renovação corretamente, revisa a prévia e envia ou cancela sem iniciar entrega, cobrança ou ações da pessoa participante?**

A UXA-052 responde afirmativamente após as reformulações registradas.

## 11. Estado funcional

`functionally_valid_after_reformulation — five mobile advertiser configuration wireframes preserve campaign identity, draft continuity, state semantics, explicit choice, provisional estimation, participant-control boundaries, affirmative confirmation and reviewed cancellation`.

## 12. Limites

Este conjunto não cria:

- gestão móvel da campanha ativa;
- estados completos de erro técnico;
- experiência operacional de inventário insuficiente;
- experiência detalhada de preferências publicitárias;
- design visual final;
- responsividade implementada;
- acessibilidade técnica;
- protótipo navegável;
- teste com Organizações ou Coletivos;
- política final de preços, publicidade, atribuição ou reconciliação;
- algoritmo, checkout, cobrança, campanha real ou Engenharia de Produto.

## 13. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar gestão móvel da campanha ativa;
2. criar estados de erro, inventário insuficiente e preferência publicitária;
3. definir protocolo de protótipo de baixa ou média fidelidade;
4. preparar plano de teste com Organizações e Coletivos;
5. desenvolver política especializada de publicidade, atribuição, agregação e reconciliação.

Nenhum ato é iniciado automaticamente.
