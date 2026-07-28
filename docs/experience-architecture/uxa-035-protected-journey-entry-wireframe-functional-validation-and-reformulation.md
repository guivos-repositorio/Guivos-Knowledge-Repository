---
id: UXA-035
title: Validação Funcional Especializada e Reformulação do Wireframe Móvel do Início Protegido
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-27
parent: UXA-034
depends_on:
  - UXA-001
  - UXA-003-A1
  - UXA-005
  - UXA-009
  - UXA-011
  - UXA-011-A1
  - UXA-020
  - UXA-021
  - UXA-023
  - UXA-034
related:
  - UXA-002
  - UXA-006
  - UXA-010
  - PAS-001-CV-VIEW-001
  - PAS-001-OBJ-VIEW-001
  - PAS-001-PP-VIEW-001
normative: false
---

# Validação Funcional Especializada e Reformulação do Wireframe Móvel do Início Protegido

## 1. Finalidade

Este documento registra a validação funcional especializada dos quatro estados móveis materializados pela UXA-034.

A validação verifica se a representação gráfica preserva o contrato funcional da UXA-023 sem transformar o início protegido em formulário obrigatório, sem confundir autenticação com autorização e sem antecipar persistência ou personalização antes da revisão da compreensão inicial.

## 2. Resultado

> **O wireframe móvel do início protegido é funcionalmente válido após reformulação.**

A estrutura em quatro estados permanece adequada como referência gráfica, desde que seja interpretada como conjunto de estados possíveis e retomáveis, não como sequência universal, rígida ou obrigatória.

## 3. Escopo avaliado

A validação examinou:

- transição consciente a partir da Home pública;
- linguagem sobre coleta, relato, dados de acesso e processamento;
- ordem entre explicação, autenticação, compartilhamento, revisão e autorização;
- pessoa já autenticada e pessoa que precisa acessar ou criar conta;
- modalidades de texto, voz, arquivo e perguntas opcionais;
- compartilhamento mínimo;
- pausa, saída, salvamento, retomada e exclusão;
- inventário do conteúdo recebido;
- autorizações específicas;
- recusa e continuidade sem processamento;
- persistência e personalização;
- acessibilidade textual e ausência de pressão.

## 4. Diagnóstico

### 4.1 Afirmações absolutas sobre ausência de coleta

As frases `Nenhuma informação pessoal foi coletada até aqui` e `Nenhuma coleta foi iniciada` poderiam ser interpretadas como afirmações sobre qualquer dado técnico, de sessão ou de acesso.

O contrato funcional precisa distinguir:

- conteúdo pessoal da jornada;
- dados necessários para acesso e proteção da conta;
- rascunho;
- processamento do relato;
- compreensão persistente;
- personalização.

A reformulação utiliza:

> **Nenhum relato pessoal da jornada foi solicitado ou recebido nesta etapa.**

> **Dados de acesso são tratados separadamente do conteúdo da jornada.**

### 4.2 Numeração e barra sugeriam formulário obrigatório

`1 DE 4`, `2 DE 4` e barras progressivas poderiam comunicar obrigação linear, embora a UXA-023 permita omissão, retomada e apresentação progressiva.

A reformulação substitui a contagem por estados nomeados:

- `ESTADO · EXPLICAÇÃO`;
- `ESTADO · ACESSO, QUANDO NECESSÁRIO`;
- `ESTADO · ESCOLHA E RASCUNHO`;
- `ESTADO · REVISÃO ANTES DO PROCESSAMENTO`.

Cada tela declara que a pessoa poderá pausar, voltar ou seguir por alternativa compatível.

### 4.3 Acesso parecia obrigatório para toda pessoa

O segundo estado não distinguia pessoa já autenticada de pessoa que precisa entrar, criar conta ou recuperar acesso.

A reformulação declara:

> **Esta etapa aparece somente quando o acesso protegido for necessário.**

Uma sessão válida poderá prosseguir sem reapresentar criação ou recuperação de conta, mantendo finalidade e controles visíveis.

### 4.4 Ação inicial possuía promessa e destino vagos

`Continuar com segurança` poderia soar como garantia ampla e não informava o próximo estado.

A ação passa a ser:

> **Ir para o acesso protegido**

Quando a pessoa já estiver autenticada, a ação correspondente poderá ser:

> **Continuar para escolher como compartilhar**

### 4.5 Modalidades equivalentes, mas texto favorecido

O terceiro estado apresentava quatro modalidades equivalentes, porém utilizava `Começar com uma frase` como ação principal geral.

A reformulação:

- não define modalidade principal antes da escolha;
- apresenta `Escolher esta forma` em cada alternativa;
- exibe explicação específica antes de voz ou arquivo;
- apresenta `Começar com pouco` somente após uma modalidade ser selecionada;
- permite combinar modalidades sem exigir combinação.

### 4.6 Pausa, saída, salvamento e exclusão não tinham efeitos suficientes

`Pausar` aparecia sem declarar se o conteúdo seria salvo. `Sair`, `Voltar` e `Continuar sem compartilhar agora` também poderiam produzir interpretações distintas.

A reformulação diferencia:

- `Sair sem iniciar relato`;
- `Pausar e manter rascunho`;
- `Sair sem salvar alterações`;
- `Salvar rascunho e sair`;
- `Excluir rascunho`;
- `Voltar à etapa anterior`;
- `Não autorizar processamento e voltar a explorar`.

A ação deverá informar o efeito antes da confirmação quando houver perda ou persistência.

### 4.7 Persistência era solicitada antes da compreensão ser conhecida

O quarto estado oferecia `Manter compreensão persistente` antes de a compreensão inicial existir e ser revisada.

Isso antecipava o gate.

A reformulação permite, nesta etapa, somente autorizar o uso de conteúdos revisados para **preparar uma compreensão inicial temporária e revisável**.

Persistência da compreensão e personalização futura permanecem bloqueadas até a apresentação e revisão da própria compreensão.

### 4.8 A recusa não esclarecia a ausência de processamento

`Continuar sem personalização` poderia ser interpretado como recusa apenas da personalização, mantendo o processamento do relato.

A reformulação apresenta duas escolhas distintas:

- `Autorizar somente os itens marcados para preparar a compreensão inicial`;
- `Não autorizar processamento e voltar a explorar`.

A ausência de autorização não poderá iniciar compreensão, persistência ou personalização.

## 5. Reformulação do estado de explicação

O primeiro estado deverá demonstrar:

- que a Home pública foi deixada;
- que nenhum relato pessoal da jornada foi solicitado ou recebido;
- que gravação, upload, transcrição e análise não começaram;
- que dados técnicos ou de acesso, quando necessários, possuem finalidade separada;
- que a pessoa poderá conhecer o processo, voltar ou explorar sem personalização;
- que os quatro artefatos são estados possíveis, não etapas obrigatórias universais.

A ação principal possui destino explícito.

## 6. Reformulação do acesso

O estado de acesso deverá:

- aparecer somente quando necessário;
- reconhecer sessão válida quando aplicável;
- oferecer entrar, criar conta e recuperar acesso;
- não revelar existência de conta;
- separar dados de acesso do conteúdo da jornada;
- afirmar que autenticação não autoriza relato, processamento, persistência ou personalização;
- permitir retorno à explicação ou à exploração geral.

## 7. Reformulação da escolha e do rascunho

O estado deverá:

- manter texto, voz, arquivo e perguntas opcionais em paridade;
- apresentar finalidade atual;
- permitir iniciar com pouco;
- explicar voz e arquivo antes da ativação;
- declarar quando um rascunho existe;
- declarar se o rascunho está salvo apenas no dispositivo, associado à conta ou ainda não persistido, conforme implementação futura;
- separar pausa, salvamento, saída e exclusão;
- permitir seguir sem compartilhar e sem iniciar processamento.

## 8. Reformulação da revisão e autorização

O estado deverá distinguir:

- conteúdo original;
- resposta opcional;
- gravação;
- transcrição;
- arquivo;
- extração proposta;
- conteúdo removido;
- finalidade aplicável.

As autorizações deverão iniciar desmarcadas e responder:

- qual item será usado;
- para qual finalidade;
- qual resultado intermediário será produzido;
- o que ocorrerá se a pessoa não autorizar.

Nesta etapa, a única finalidade material ilustrada é preparar uma compreensão inicial temporária e revisável.

Persistência e personalização permanecem bloqueadas.

## 9. Estados funcionais resultantes

```text
Home pública
→ explicação do ambiente protegido
→ acesso, somente quando necessário
→ escolha de modalidade
→ rascunho mínimo e progressivo
→ revisão do conteúdo recebido
→ autorização específica para preparar compreensão inicial
→ processamento visível e interrompível
→ compreensão inicial apresentada
→ revisão da compreensão
→ decisão sobre persistência e personalização
```

A pessoa poderá pausar, voltar, excluir ou retornar à exploração geral nos pontos compatíveis.

## 10. Proteções confirmadas

- nenhum relato é solicitado antes da explicação;
- dados de acesso não são tratados como conteúdo da jornada;
- autenticação não autoriza processamento;
- acesso não é reapresentado quando desnecessário;
- modalidades permanecem equivalentes;
- voz e arquivo exigem explicação anterior;
- compartilhamento mínimo é legítimo;
- pausa, salvamento, saída e exclusão possuem efeitos distintos;
- revisão antecede processamento;
- autorizações são específicas e inicialmente desmarcadas;
- recusa não inicia processamento;
- persistência não é solicitada antes da compreensão inicial;
- personalização permanece bloqueada até o gate;
- exploração sem personalização continua disponível;
- informações de terceiros não são exigidas;
- a interface não utiliza culpa, urgência ou promessa absoluta de segurança.

## 11. Critérios atendidos

A reformulação permite compreender:

- que a pessoa saiu da Home pública;
- que nenhum relato pessoal começou;
- que dados de acesso são uma categoria separada;
- que o conjunto não é formulário linear obrigatório;
- quando autenticação é necessária;
- quais modalidades estão disponíveis;
- que pouco conteúdo é suficiente para começar;
- o efeito de pausar, salvar, sair e excluir;
- o inventário do que foi recebido;
- a finalidade de cada autorização;
- que recusar impede processamento;
- que a compreensão será revisada antes de persistência ou personalização.

## 12. Limites

Esta validação não:

- define textos jurídicos finais;
- conclui política de privacidade;
- define provedor de identidade;
- implementa autenticação ou segurança;
- define armazenamento local ou remoto;
- implementa voz, transcrição, arquivo ou extração;
- define modelo de IA;
- cria compreensão inicial gráfica;
- cria referência para computador ou tablet;
- cria protótipo navegável;
- executa teste com usuários;
- conclui acessibilidade técnica;
- inicia Engenharia de Produto.

## 13. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar a referência móvel da Página Inicial pública;
2. materializar a revisão da compreensão inicial;
3. validar a transição para a primeira Tela Hoje;
4. criar estados especializados de texto, voz e arquivos;
5. criar referência do início protegido para computador;
6. criar estados de processamento, pausa, falha e retomada;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
