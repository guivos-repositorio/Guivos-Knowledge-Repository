---
id: UXA-037
title: Validação Funcional Especializada e Reformulação do Wireframe Móvel da Compreensão Inicial
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-28
parent: UXA-036
depends_on:
  - UXA-001
  - UXA-003-A1
  - UXA-005
  - UXA-009
  - UXA-011
  - UXA-011-A1
  - UXA-020
  - UXA-023
  - UXA-034
  - UXA-035
  - UXA-036
related:
  - UXA-002
  - UXA-006
  - UXA-010
  - PAS-001-CV-VIEW-001
  - PAS-001-OBJ-VIEW-001
  - PAS-001-PP-VIEW-001
normative: false
---

# Validação Funcional Especializada e Reformulação do Wireframe Móvel da Compreensão Inicial

## 1. Finalidade

Este documento valida funcionalmente a referência móvel criada pela UXA-036 e registra as reformulações necessárias para que processamento, hipótese, revisão, decisões e base insuficiente preservem autonomia, explicabilidade e separação de finalidades.

A pergunta de validação é:

> **A pessoa compreende o que está sendo processado, consegue interromper com efeito conhecido, revisar cada afirmação como hipótese e decidir separadamente sobre persistência e personalização sem escolhas implícitas ou pressão para aceitar a leitura da Guivos?**

## 2. Resultado

O conjunto é considerado **funcionalmente válido após reformulação**.

A validação não aprova design visual, textos jurídicos, modelo de IA, segurança, armazenamento, persistência, personalização, acessibilidade técnica, protótipo, teste com usuários ou desenvolvimento.

## 3. Escopo examinado

Foram examinados:

1. processamento visível e interrompível;
2. apresentação da compreensão como hipótese;
3. separação entre Momento Atual, avanço e possibilidade de Próximo Passo;
4. origem, natureza, confiança, lacunas e desconhecidos;
5. revisão por afirmação;
6. preservação do relato original;
7. retirada de autorização e exclusão;
8. decisões sobre persistência e personalização;
9. continuidade sem personalização;
10. transição para a Tela Hoje;
11. base autorizada insuficiente.

## 4. Lacunas identificadas

### 4.1 Saída ambígua durante o processamento

O rótulo `Sair` não informava se o processamento continuaria, seria interrompido ou teria resultado parcial descartado.

### 4.2 Efeito da interrupção pouco visível

O efeito de `Interromper processamento` estava descrito no contrato, mas não suficientemente demonstrado na superfície gráfica.

### 4.3 Naturezas diferentes aplicadas à mesma frase

A apresentação associava `Confirmado por você` e `Inferido · confiança moderada` ao mesmo bloco textual, sem indicar qual trecho pertencia a cada natureza.

### 4.4 Revisão aparentemente pré-selecionada

O preenchimento escuro de `Faz sentido` podia ser interpretado como resposta escolhida por padrão, contrariando voluntariedade e confirmação explícita.

### 4.5 Ausência de afirmação mantida em aberto

A pessoa podia confirmar, rejeitar ou corrigir, mas não havia alternativa explícita para não decidir naquele momento.

### 4.6 Retirada de autorização sem escopo

`Retirar autorização de uso` não identificava conteúdo afetado, finalidade retirada, efeito sobre derivados ou possibilidade de manter o relato original.

### 4.7 Decisões exclusivas representadas como caixas de seleção

Persistência e personalização utilizavam caixas quadradas, embora cada grupo exija uma única escolha mutuamente exclusiva.

### 4.8 Confirmação disponível sem escolhas concluídas

A ação para confirmar e entrar na Tela Hoje parecia ativa mesmo com todas as alternativas desmarcadas.

### 4.9 Base insuficiente sem estado gráfico

O contrato governava ausência de base, mas o conjunto não materializava a situação necessária para validar ausência de hipótese artificial e ausência de pressão para compartilhar mais.

## 5. Reformulação aprovada

### 5.1 Processamento

O estado reformulado deverá:

- remover saída ambígua;
- declarar `Processamento temporário em andamento`;
- mostrar etapas por estado textual, sem percentual de evolução humana;
- apresentar `Interromper e descartar resultado parcial`;
- explicar que revisar conteúdos interrompe e descarta o resultado parcial;
- oferecer `Interromper e explorar sem personalização`;
- preservar os conteúdos de origem somente conforme controles anteriores;
- não prometer continuidade silenciosa em segundo plano.

### 5.2 Afirmações com identidade própria

Cada afirmação material deverá possuir:

- identificador visível de referência;
- texto próprio;
- natureza própria;
- origem própria;
- confiança somente quando houver inferência;
- finalidade e possibilidade de revisão.

Uma frase não poderá receber simultaneamente rótulos de `confirmado` e `inferido` sem separação explícita dos trechos.

### 5.3 Revisão sem resposta padrão

Todas as respostas começam desmarcadas.

Cada afirmação poderá receber uma das respostas:

- `Confirmar esta afirmação`;
- `Confirmar parcialmente`;
- `Não representa meu momento`;
- `Está incorreta`;
- `Manter em aberto`;
- `Não usar esta interpretação`.

A pessoa poderá aplicar a revisão com afirmações mantidas em aberto, desde que o resumo declare quais partes não foram confirmadas e impeça seu uso como fato.

### 5.4 Escopo de correção e retirada

A interface deverá distinguir:

- corrigir somente a interpretação;
- editar o conteúdo de origem;
- retirar autorização de uma finalidade específica;
- excluir conteúdo de origem e derivados;
- remover somente uma interpretação;
- recalcular a hipótese sem o item afetado.

Antes de aplicar uma alteração, a superfície mostrará conteúdo afetado, finalidade, derivados e resultado esperado.

### 5.5 Persistência e personalização

Cada grupo utilizará escolha única, representada por controles circulares ou rótulo equivalente.

Nenhuma alternativa será selecionada por padrão.

A ação de continuidade permanecerá indisponível até existir:

1. uma escolha sobre persistência;
2. uma escolha independente sobre personalização;
3. uma combinação funcionalmente compatível.

Se `Excluir esta compreensão` for escolhido, personalização ficará indisponível e a continuidade ocorrerá sem personalização.

Se `Usar somente nesta sessão` for escolhido, a personalização poderá valer somente para a sessão e finalidade apresentadas.

### 5.6 Continuidade sem personalização

A saída direta será apresentada como escolha com consequência explícita, por exemplo:

> **Usar somente nesta sessão e continuar sem personalização.**

Nenhuma ação deverá escolher silenciosamente persistência ou exclusão.

### 5.7 Base insuficiente

Um quinto estado gráfico passa a integrar a referência.

Ele deverá declarar:

> **Ainda não há base autorizada suficiente para preparar uma compreensão com segurança.**

A superfície mostrará:

- o que foi considerado;
- o que permanece desconhecido;
- ausência de hipótese pessoal;
- ausência de Próximo Passo pessoal;
- alternativas para revisar, compartilhar algo adicional voluntariamente, continuar sem personalização ou encerrar;
- ausência de urgência, culpa ou bloqueio.

## 6. Critérios funcionais confirmados

Após a reformulação, o conjunto demonstra que:

- somente conteúdos revisados e autorizados entram no processamento;
- interrupção possui efeito explícito e não deixa tarefa oculta;
- processamento não equivale a persistência ou personalização;
- compreensão é hipótese, não diagnóstico;
- afirmações confirmadas e inferidas são distinguíveis;
- confiança não equivale a certeza;
- Momento Atual, avanço e Próximo Passo permanecem separados;
- ausência de evidência não é preenchida artificialmente;
- revisão não possui resposta padrão;
- confirmação parcial não transforma inferência rejeitada em fato;
- uma afirmação pode permanecer em aberto;
- relato original e interpretação derivada permanecem separados;
- correção, retirada de autorização e exclusão possuem escopos diferentes;
- persistência e personalização são escolhas únicas e independentes;
- combinações incompatíveis são bloqueadas;
- continuidade sem personalização é legítima e possui consequência conhecida;
- base insuficiente não gera pressão para compartilhar mais;
- a Tela Hoje recebe somente a condição explicitamente escolhida.

## 7. Estado dos cinco artefatos

A referência reformulada passa a conter:

1. `uxa-036-initial-understanding-processing-mobile.svg`;
2. `uxa-036-initial-understanding-presentation-mobile.svg`;
3. `uxa-036-initial-understanding-review-mobile.svg`;
4. `uxa-036-initial-understanding-decision-mobile.svg`;
5. `uxa-036-initial-understanding-insufficient-basis-mobile.svg`.

Todos permanecem em baixa fidelidade, com dimensão de referência de 390 × 844 pixels.

## 8. Proteções preservadas

- autenticação não autoriza processamento;
- conteúdo não autorizado permanece fora do processamento;
- raciocínio interno detalhado não é exposto;
- inferências sensíveis automáticas não são autorizadas;
- engajamento não é apresentado como evolução;
- persistência não autoriza personalização;
- personalização não cria nova finalidade;
- publicidade não recebe autorização por consequência;
- exclusão destrutiva exige confirmação futura;
- continuar sem personalização permanece disponível;
- nenhuma decisão é premiada, pressionada ou apresentada como moralmente superior.

## 9. Limites

Esta validação não:

- define modelo ou fornecedor de IA;
- define política jurídica ou de retenção final;
- implementa segurança, autenticação ou armazenamento;
- implementa processamento, persistência ou personalização;
- define inferências sensíveis permitidas;
- cria diagnóstico psicológico, médico, financeiro ou profissional;
- cria referência para computador ou tablet;
- conclui textos finais ou identidade visual;
- cria protótipo navegável;
- executa teste com usuários;
- conclui acessibilidade técnica;
- inicia Engenharia de Produto.

## 10. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar a referência móvel da Página Inicial pública;
2. validar a transição da compreensão para a primeira Tela Hoje;
3. criar estados especializados de processamento, pausa, falha e retomada;
4. criar referência do início protegido e da compreensão para computador;
5. criar estados especializados de texto, voz e arquivos;
6. criar referência para tablet, caso priorizada;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
