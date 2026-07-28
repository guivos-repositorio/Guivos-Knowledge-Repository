---
id: UXA-033
title: Validação Funcional Especializada e Reformulação da Referência do Mapa para Computador
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-27
parent: UXA-000
depends_on:
  - UXA-001
  - UXA-003-A1
  - UXA-004
  - UXA-005
  - UXA-009
  - UXA-011-A1
  - UXA-024
  - UXA-025
  - UXA-026
  - UXA-027
  - UXA-028
  - UXA-029
  - UXA-030
  - UXA-031
  - UXA-032
related:
  - UXA-002
  - UXA-006
  - UXA-007
  - UXA-010
  - UXA-012
  - UXA-020
  - UXA-022
  - UXA-023
normative: true
---

# Validação Funcional Especializada e Reformulação da Referência do Mapa para Computador

## 1. Finalidade

Este documento registra a validação funcional especializada da referência do Mapa de Oportunidades para computador e governa a reformulação da UXA-032.

A decisão permanece restrita à Arquitetura da Experiência. Ela não aprova tecnologia cartográfica, geocodificação, rotas, algoritmo de busca ou ordenação, cobertura de fontes de produção, identidade visual, pontos de quebra, responsividade, referência para tablet, protótipo navegável, conformidade técnica de acessibilidade, teste de usabilidade ou desenvolvimento.

## 2. Decisão humana registrada

Em 27/07/2026, o Fundador autorizou a validação funcional especializada da UXA-032 após a integração do marco M7.33.

A validação examinou:

- paridade entre os canais móvel e para computador;
- compreensão de que Mapa, Lista e filtros representam uma única consulta;
- consistência entre resumo e valores detalhados dos filtros;
- distribuição horizontal e prioridade dos painéis;
- comportamento de foco no Mapa ou na Lista;
- atualização territorial após movimentação cartográfica;
- sincronização da oportunidade selecionada;
- comparabilidade e explicabilidade dos cartões;
- continuidade para o Detalhe;
- localização opcional e região manual;
- estado sem resultados;
- operação sem mapa carregado;
- acessibilidade funcional e aderência à Fundação da Guivos.

## 3. Resultado da validação

A referência do Mapa de Oportunidades para computador é considerada **funcionalmente válida após reformulação**.

A versão inicial já estabelecia corretamente:

- Mapa como superfície recorrente;
- navegação `Hoje | Jornada | Explorar | Mapa | Eu`;
- contexto `Agindo como: Pessoa`;
- exploração geral sem personalização;
- localização desativada e posição não acessada;
- região manual distinta da posição pessoal;
- painel de filtros, campo territorial e Lista lado a lado;
- quantidade e atualização compartilhadas;
- oportunidade selecionada;
- separação entre razão funcional e relação comercial;
- continuidade para o Detalhe;
- estado zero com cobertura verificável;
- Lista operável sem mapa carregado.

Entretanto, sete riscos exigiram correção antes do fechamento funcional:

1. os filtros resumidos contradiziam os valores detalhados apresentados no mesmo painel;
2. `Ampliar Mapa` e `Ampliar Lista` não definiam mudança de foco, preservação de contexto ou retorno à visão dividida;
3. `Pesquisar nesta área` aparecia sem indicar que o Mapa havia sido movido e que a consulta anterior permanecia ativa;
4. a seleção não vinculava explicitamente o marcador, o cartão e o painel contextual pelo mesmo identificador;
5. os cartões secundários não apresentavam origem funcional, explicação e relação comercial com consistência suficiente;
6. o painel completo da oportunidade selecionada comprimia a área de comparação da Lista sem declarar que era recolhível;
7. o estado sem resultados repetia ações de recuperação no painel esquerdo, no centro do Mapa e no painel direito, criando competição de hierarquia.

## 4. Posição funcional preservada

A ordem vigente permanece:

```text
Página Inicial pública
→ início protegido da jornada
→ compreensão inicial revisável
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

A referência para computador não constitui etapa obrigatória, produto distinto ou catálogo separado.

O item `Mapa` permanece selecionado.

## 5. Gate de alinhamento à Fundação

### 5.1 Essência

A reformulação preserva orientação sem retirar autonomia. A pessoa mantém controle sobre consulta, território, filtros, foco e seleção.

### 5.2 Propósito

A tela ampla amplia compreensão e comparação sem aumentar coleta, inferência ou pressão para localização e personalização.

### 5.3 Missão Operacional

Região, busca, filtros, atualização, quantidade, seleção, cobertura e relação comercial permanecem visíveis e explicáveis.

### 5.4 Visão de Longo Prazo

A referência permite evolução para diferentes densidades territoriais e canais sem criar significados incompatíveis entre móvel e computador.

### 5.5 Constituição e Princípios Permanentes

São preservados:

- autonomia;
- dignidade;
- transparência;
- explicabilidade;
- privacidade;
- não manipulação;
- acessibilidade;
- reversibilidade;
- separação entre relevância funcional e interesse comercial.

Nenhuma falha material à Fundação foi identificada após a reformulação.

## 6. Consulta territorial única

A versão reformulada apresenta uma faixa compartilhada:

> **Consulta territorial ativa · mesma região, busca, filtros e atualização**

No estado com resultados, a faixa também informa:

> **8 resultados · atualizada agora**

No estado sem resultados:

> **0 resultados · cobertura verificada · atualizada agora**

A faixa não cria identificador técnico para a pessoa. Sua função é declarar que painel de filtros, Mapa, Lista e seleção pertencem ao mesmo estado.

A interface não poderá manter versões divergentes da consulta em painéis simultâneos.

## 7. Consistência dos filtros

Resumo, marcas de seleção e controles detalhados deverão apresentar valores semanticamente idênticos.

A referência reformulada utiliza:

- `Hoje e próximos 7 dias`;
- `Gratuitas e preço informado`;
- `Presencial e online`;
- `Acessibilidade confirmada ou informada`.

A interface não poderá resumir um filtro como `Hoje` enquanto o controle representar sete dias, nem declarar `Online` quando a modalidade também incluir presencial.

`Limpar filtros` continua sem apagar região ou busca.

## 8. Visão dividida e modos de foco

A disposição padrão é declarada como:

> **Visão dividida ativa**

As ações passam a ser:

- `Focar no Mapa`;
- `Focar na Lista`;
- `Voltar à visão dividida` nos estados concentrados.

Focar em um painel deverá preservar:

- contexto `Agindo como`;
- região;
- busca;
- filtros;
- quantidade;
- atualização;
- ordenação;
- seleção;
- estado de localização;
- cobertura;
- posição de leitura quando aplicável.

A mudança de foco não constitui nova consulta e não altera permissões.

## 9. Movimento do Mapa e atualização consciente

`Pesquisar nesta área` somente deverá aparecer quando:

- o campo cartográfico tiver sido movido materialmente;
- a área visível divergir da região que produziu os resultados atuais;
- a consulta anterior continuar ativa;
- a pessoa puder reconhecer que os resultados ainda não foram atualizados.

O estado pendente deverá declarar:

> **Área movida · resultados ainda correspondem à consulta anterior**

Antes do movimento, a referência informa:

> **Área atual · resultados atualizados**

Mover o Mapa não executa nova consulta silenciosamente.

## 10. Seleção sincronizada

A oportunidade selecionada deverá utilizar o mesmo vínculo textual nos três pontos:

- marcador territorial;
- cartão da Lista;
- painel contextual.

A referência utiliza:

> **Marcador 1 · selecionada**

A seleção deverá:

- permanecer reconhecível ao alternar foco;
- não alterar ordenação;
- não aumentar relevância;
- não modificar permissões;
- preservar retorno após o Detalhe;
- ser removida conscientemente quando aplicável.

## 11. Lista comparável e explicável

Cada cartão visível deverá apresentar, em forma compacta quando necessário:

- tipo;
- título;
- responsável;
- modalidade;
- região ou disponibilidade online;
- data ou prazo;
- preço;
- disponibilidade;
- acessibilidade;
- origem funcional;
- relação comercial;
- ação `Por que aparece aqui?`.

Dados ausentes serão declarados como não informados.

A ação genérica `Entender` é substituída por:

> **Entender ordenação**

A relação comercial deverá utilizar rótulo explícito, como:

- `Relação comercial: sem patrocínio`;
- `Relação comercial: parceria identificada`;
- `Relação comercial: conteúdo patrocinado`.

## 12. Painel contextual recolhível

O painel da oportunidade selecionada passa a ser declarado como:

> **Painel contextual recolhível**

Ele poderá ser aberto para apresentar condições resumidas e ações, mas não deverá eliminar a capacidade de comparar a Lista.

Ao recolher o painel:

- a seleção permanece ativa;
- o cartão selecionado continua reconhecível;
- o marcador permanece vinculado;
- a Lista recupera espaço;
- a consulta não é modificada.

O painel não substitui o Detalhe de Oportunidade.

## 13. Continuidade com o Detalhe

Ao abrir e retornar do Detalhe, permanecem:

- contexto `Agindo como`;
- região;
- busca;
- filtros;
- quantidade;
- atualização;
- ordenação;
- posição da Lista;
- oportunidade selecionada;
- modo de foco;
- estado de localização;
- origem da navegação.

Mudança real de disponibilidade deverá ser informada, não escondida por restauração artificial do estado anterior.

## 14. Estado sem resultados com hierarquia única

A recuperação principal fica concentrada no painel `Consulta e filtros`.

O centro do Mapa apresenta:

- diagnóstico;
- total zero;
- cobertura;
- declaração de preservação da consulta;
- ação `Revisar consulta preservada`;
- saída `Explorar sem alterar esta consulta`.

A Lista apresenta o mesmo total e orienta a utilização do painel de consulta, sem repetir todas as ações.

As ações independentes permanecem:

- `Ampliar região`;
- `Alterar período`;
- `Revisar filtros`;
- `Editar busca`;
- `Desfazer`, somente quando houver alteração anterior identificável.

A pessoa revisa valor atual e proposto antes de aplicar qualquer mudança.

## 15. Seleção anterior no estado zero

Quando uma alteração produzir zero resultados e houver seleção anterior, a Lista poderá apresentar:

> **Seleção anterior fora da consulta atual**

A oportunidade não integra o total zero.

A pessoa poderá abrir o Detalhe, remover a seleção, desfazer a alteração compatível ou manter a nova consulta.

## 16. Localização e privacidade

A referência continua declarando:

> **Localização desativada · posição não acessada**

> **Região manual · não é sua posição**

Mais espaço visual não autoriza:

- ativar localização;
- inferir residência;
- manter histórico territorial;
- rastrear movimentação;
- revelar localização de participantes;
- contornar endereço protegido;
- utilizar território para publicidade individualizada sem base aplicável.

## 17. Relação comercial e personalização

Sem gate de personalização, resultados e ordenação utilizam somente consulta explícita, região, filtros, período e cobertura.

Publicidade, comissão, patrocínio, popularidade ou proximidade isolada não poderão:

- alterar relevância funcional de forma oculta;
- preencher o estado zero;
- simular recomendação pessoal;
- modificar a seleção;
- alterar a consulta compartilhada.

## 18. Acessibilidade funcional e resiliência

A ordem funcional recomendada é:

```text
cabeçalho e contexto
→ consulta territorial ativa
→ pesquisa
→ filtros
→ Mapa
→ Lista
→ painel contextual da seleção
```

A superfície deverá permitir acesso direto a:

- consulta;
- filtros;
- Mapa;
- Lista;
- oportunidade selecionada.

Quantidade, atualização, localização, cobertura, foco e seleção deverão ser anunciáveis textualmente.

A Lista, o diagnóstico, os filtros e as ações essenciais continuam operáveis sem o mapa carregado.

A validação não conclui conformidade técnica de acessibilidade.

## 19. Paridade entre canais validada

A referência para computador poderá alterar disposição e densidade, mas não significado.

Deverão permanecer equivalentes entre móvel e computador:

- contexto;
- região;
- busca;
- filtros;
- quantidade;
- atualização;
- ordenação;
- seleção;
- explicabilidade;
- relação comercial;
- localização opcional;
- cobertura;
- continuidade para o Detalhe;
- estado sem resultados.

## 20. Reformulação da UXA-032

A UXA-032 passa a:

- versão 0.2.0;
- estado ativo;
- faixa compartilhada de consulta territorial;
- filtros semanticamente consistentes;
- visão dividida declarada;
- ações `Focar no Mapa` e `Focar na Lista`;
- regra `Voltar à visão dividida`;
- atualização territorial condicionada ao movimento;
- seleção vinculada como `Marcador 1`;
- cartões compactos comparáveis e explicáveis;
- `Entender ordenação` explícito;
- relação comercial rotulada;
- painel contextual recolhível;
- hierarquia única de recuperação no estado zero;
- ordem funcional e atalhos de acesso registrados.

## 21. Critérios de aceite atendidos

| Critério | Resultado |
|---|---|
| Mapa e Lista são percebidos como a mesma consulta | atendido após faixa compartilhada e visão dividida explícita |
| filtros não contradizem os controles | atendido após unificação dos valores |
| mudança de foco preserva contexto | atendido após contrato de foco e retorno |
| movimentação não atualiza silenciosamente | atendido após estado territorial pendente explícito |
| seleção é reconhecida nos três pontos | atendido após vínculo `Marcador 1` |
| cartões permitem comparação e explicação | atendido após campos e ações consistentes |
| painel selecionado não elimina a Lista | atendido após condição recolhível |
| estado zero possui hierarquia clara | atendido após concentração da recuperação |
| localização permanece opcional | atendido |
| relação comercial permanece separada | atendido |
| operação sem mapa carregado permanece possível | atendido |
| aderência à Fundação | atendido |

## 22. Limites da validação

Esta validação não:

- testa compreensão com usuários;
- define comportamento técnico de redimensionamento;
- cria pontos de quebra;
- cria referência para tablet;
- define componente, framework ou biblioteca;
- define tecnologia cartográfica;
- define algoritmo ou cobertura real;
- conclui design visual;
- cria protótipo navegável;
- conclui acessibilidade técnica;
- inicia Engenharia de Produto.

## 23. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar o wireframe gráfico do início protegido;
2. criar a referência móvel da Página Inicial pública;
3. validar a revisão da compreensão inicial;
4. validar a transição para a primeira Tela Hoje;
5. criar outros estados especializados do Mapa;
6. criar referência específica para tablet, caso priorizada;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
