---
id: UXA-041
title: Validação Funcional e Reformulação dos Wireframes do Fluxo do Anunciante do Opportunity Boost
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-28
parent: UXA-040
depends_on:
  - UXA-005
  - UXA-009
  - UXA-038
  - UXA-039
  - UXA-040
  - GEM-007-A1
  - GEM-010-A2
related:
  - GPA-007
  - M7.43
normative: false
---

# Validação Funcional e Reformulação dos Wireframes do Fluxo do Anunciante do Opportunity Boost

## 1. Finalidade

Este documento valida funcionalmente os cinco wireframes para computador criados pela UXA-040 e registra as reformulações necessárias para que elegibilidade, objetivo, critérios, orçamento, prévia e envio preservem transparência, voluntariedade e separação entre publicidade e relevância orgânica.

A pergunta de validação é:

> **O anunciante compreende por que pode ou não impulsionar, escolhe conscientemente objetivo, critérios, orçamento e duração, distingue estimativa de garantia, revisa a apresentação patrocinada e envia a campanha sem acreditar que comprou relevância orgânica, recomendação ou resultado?**

## 2. Resultado

O conjunto é considerado **funcionalmente válido após reformulação**.

A validação não aprova design visual, textos jurídicos, política publicitária final, algoritmo, precificação, cobrança, acessibilidade técnica, protótipo, teste com usuários ou Engenharia de Produto.

## 3. Escopo examinado

Foram examinados:

1. elegibilidade do plano e da oportunidade;
2. estados atendido, limitado e bloqueado;
3. objetivo único e métrica principal;
4. critérios escolhidos e critérios proibidos;
5. público estimado insuficiente;
6. orçamento total, limite diário e duração;
7. coerência entre objetivo e base de cobrança;
8. estimativa agregada sem garantia;
9. ordem entre resultado orgânico e espaço patrocinado;
10. confirmação afirmativa;
11. envio para avaliação;
12. cancelamento, histórico e próximos estados.

## 4. Lacunas identificadas

### 4.1 Atenção e bloqueio pouco distinguíveis

A capacidade aparecia como `Atenção`, mas a superfície não informava se essa condição impedia o avanço ou apenas limitava a campanha.

### 4.2 Critérios pareciam aplicados automaticamente

Região, idioma, categoria e modalidade eram exibidos preenchidos, sem indicar que haviam sido escolhidos ou confirmados pelo anunciante.

### 4.3 Estado de público insuficiente parecia ativo simultaneamente

A regra de exceção para público insuficiente aparecia ao lado do estado inicial sem objetivo, podendo ser interpretada como diagnóstico atual da campanha.

### 4.4 Base de cobrança incompatível com o objetivo

O exemplo selecionava o objetivo `Levar pessoas ao detalhe`, cuja métrica é clique válido, mas apresentava CPM como base principal da campanha.

### 4.5 Prévia contrariava a preservação do primeiro resultado orgânico

O cartão impulsionado era exibido antes do resultado orgânico, embora a própria superfície declarasse que o primeiro resultado orgânico seria preservado.

### 4.6 Cancelamento sem consequência visível

A ação `Cancelar envio` não informava se a avaliação seria encerrada, se a campanha voltaria a rascunho ou se existiria entrega ou cobrança.

## 5. Reformulação aprovada

### 5.1 Semântica dos gates

Cada condição passa a utilizar uma das três naturezas:

- `Atendido` — permite continuidade;
- `Atendido com limite` — permite continuidade, mas limita alcance ou entrega;
- `Bloqueado` — impede continuidade e exige ação corretiva.

A superfície informa a quantidade de bloqueios críticos e deixa explícito que limite operacional não equivale a inelegibilidade.

### 5.2 Critérios afirmativos e revisáveis

Os critérios permitidos passam a ser apresentados como `Critérios escolhidos pelo anunciante`, com controles visuais de seleção, origem objetiva e ação para revisar ou remover.

Nenhum critério novo será adicionado silenciosamente quando a estimativa for pequena.

### 5.3 Exceção de público insuficiente

O estado passa a ser rotulado como `Regra de exceção — não ativa neste exemplo`, separado da estimativa atual.

Quando ativo, deverá informar:

- motivo;
- critérios responsáveis pela limitação;
- possibilidade de revisar manualmente;
- proibição de expansão automática;
- consequência: campanha limitada ou bloqueada.

### 5.4 Base principal coerente

Para o objetivo `Levar pessoas ao detalhe`, a base principal passa a ser `CPC — clique válido`.

A superfície declara que:

- a base deriva do objetivo e da política aplicável;
- somente uma base principal será utilizada;
- CPM e CPC não serão cobrados simultaneamente;
- a base não poderá ser alterada silenciosamente.

### 5.5 Ordem orgânica preservada

A prévia reformulada apresenta:

1. primeiro resultado orgânico;
2. espaço patrocinado identificado depois do primeiro orgânico;
3. explicação de distribuição e controles;
4. aviso de que a posição é publicitária e não altera ordenação orgânica.

### 5.6 Cancelamento compreensível

A superfície de envio passa a declarar:

> **Cancelar encerra a avaliação e devolve a campanha ao estado de rascunho. Nenhuma entrega começa e nenhuma cobrança real é iniciada por este artefato.**

A ação deverá exigir confirmação futura e preservar histórico da decisão.

## 6. Critérios funcionais confirmados

Após a reformulação, o conjunto demonstra que:

- plano elegível não substitui aprovação, capacidade, segurança ou responsável;
- estados atendido, limitado e bloqueado possuem consequências distintas;
- objetivo único começa desmarcado;
- métrica principal é compreensível;
- critérios utilizados são escolhidos e revisáveis;
- critérios protegidos permanecem excluídos;
- público insuficiente não provoca expansão automática;
- orçamento, limite diário e duração são explícitos;
- base principal é coerente com o objetivo;
- somente uma base de cobrança principal é utilizada;
- estimativa não equivale a garantia;
- primeiro resultado orgânico aparece antes do espaço patrocinado;
- anúncio é identificado antes da interação;
- confirmação final começa desmarcada;
- envio não inicia entrega;
- ajustes, rejeição e aprovação permanecem estados distintos;
- cancelamento possui efeito conhecido;
- histórico permanece acessível.

## 7. Estado dos artefatos reformulados

A referência validada contém:

1. `uxa-040-opportunity-boost-eligibility-desktop.svg`;
2. `uxa-040-opportunity-boost-objective-audience-desktop.svg`;
3. `uxa-040-opportunity-boost-budget-schedule-desktop.svg`;
4. `uxa-040-opportunity-boost-preview-confirmation-desktop.svg`;
5. `uxa-040-opportunity-boost-submission-desktop.svg`.

Todos permanecem em baixa fidelidade, com dimensão de referência de 1.440 × 1.024 pixels.

## 8. Proteções preservadas

- pagamento não compra relevância, confiança, recomendação ou impacto;
- compreensão inicial, Momento Atual e Próximo Passo não alimentam segmentação;
- critérios protegidos não aparecem como opções;
- oferta orgânica permanece visível;
- estimativas permanecem agregadas;
- nenhuma renovação automática é habilitada por padrão;
- nenhum orçamento é aumentado automaticamente;
- nenhum envio inicia campanha ou cobrança;
- nenhum prazo ou aprovação é prometido.

## 9. Limites

Esta validação não cria:

- cartão patrocinado independente para a pessoa;
- explicação completa `Por que estou vendo isto?`;
- estados patrocinados para Lista ou Mapa;
- gestão de campanha ativa;
- relatório agregado;
- teste com usuários;
- design visual;
- protótipo;
- algoritmo, checkout, cobrança ou Engenharia de Produto.

## 10. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar wireframes do cartão patrocinado e da explicação de distribuição;
2. criar estados patrocinados para Lista e Mapa;
3. criar wireframes de gestão da campanha ativa;
4. criar wireframe do relatório agregado;
5. validar funcionalmente o conjunto completo de wireframes do Opportunity Boost.

Nenhum ato é iniciado automaticamente.
