---
id: UXA-029
title: Validação Funcional Especializada e Reformulação da Visualização em Lista do Mapa
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
related:
  - UXA-002
  - UXA-006
  - UXA-007
  - UXA-010
  - UXA-012
  - UXA-020
  - UXA-023
normative: true
---

# Validação Funcional Especializada e Reformulação da Visualização em Lista do Mapa

## 1. Finalidade

Este documento registra a validação funcional especializada da visualização em Lista do Mapa de Oportunidades e governa a reformulação da UXA-028.

A decisão permanece restrita à Arquitetura da Experiência. Ela não aprova algoritmo de ordenação, tecnologia cartográfica, geocodificação, rotas, design visual, protótipo navegável, acessibilidade técnica, teste de usabilidade ou desenvolvimento.

## 2. Decisão humana registrada

Em 27/07/2026, o Fundador autorizou a validação funcional especializada da UXA-028 após a integração do marco M7.29.

A validação examinou:

- clareza de que Mapa e Lista representam a mesma consulta;
- diferença entre Lista territorial do Mapa e `Explorar`;
- preservação de contexto `Agindo como`;
- preservação de região, busca, filtros, quantidade e ordenação;
- manutenção da oportunidade selecionada;
- comparação suficiente entre cartões;
- separação entre explicação funcional e relação comercial;
- salvamento e acesso ao Detalhe sem localização;
- retorno ao Mapa sem perda de contexto;
- funcionamento como alternativa integral para acessibilidade, baixa conectividade e falha cartográfica;
- aderência à Fundação da Guivos.

## 3. Resultado da validação

A visualização em Lista do Mapa é considerada **funcionalmente válida após reformulação**.

O wireframe inicial já estabelecia corretamente:

- Lista como modo interno da superfície `Mapa`;
- alternância `Mapa ↔ Lista`;
- localização desativada e posição não acessada;
- região manual;
- busca e filtros preservados;
- quantidade de resultados;
- ordenação explícita;
- oportunidade selecionada;
- salvamento, origem e Detalhe;
- retorno ao Mapa sem perda de contexto;
- Lista como alternativa integral.

Entretanto, cinco riscos exigiram correção antes do fechamento funcional:

1. o contexto `Agindo como` não aparecia no wireframe da Lista;
2. a diferença para `Explorar` dependia somente da navegação e não era declarada na superfície;
3. `Mais filtros · 2` não esclarecia o total consolidado de filtros ativos;
4. a ordenação era declarada, mas não possuía ação de explicação acessível;
5. os cartões secundários não apresentavam campos ausentes, explicação e relação comercial com consistência comparável.

## 4. Posição funcional preservada

A ordem vigente permanece:

```text
Página Inicial pública
→ início protegido da jornada
→ compreensão inicial revisável
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

A Lista não constitui nova etapa da jornada. Ela é um modo interno da superfície recorrente do Mapa.

O item `Mapa` permanece selecionado na navegação principal.

## 5. Gate de alinhamento à Fundação

### 5.1 Essência

A reformulação reduz ambiguidade e amplia a capacidade de compreender, comparar e decidir conscientemente.

### 5.2 Propósito

A Lista mantém oportunidades acessíveis sem exigir leitura cartográfica, localização do dispositivo ou personalização.

### 5.3 Missão Operacional

Busca, filtros, condições, relações comerciais, incertezas e transições permanecem verificáveis e controláveis.

### 5.4 Visão de Longo Prazo

A mesma consulta poderá evoluir para múltiplos canais sem criar experiências contraditórias ou dependentes de um fornecedor cartográfico.

### 5.5 Constituição e Princípios Permanentes

São preservados:

- autonomia;
- dignidade;
- privacidade;
- transparência;
- explicabilidade;
- não manipulação;
- acessibilidade como alternativa real;
- separação entre relevância e interesse comercial.

Nenhuma falha material à Fundação foi identificada após a reformulação.

## 6. Natureza da Lista validada

A Lista é uma representação textual integral da mesma consulta territorial do Mapa.

Ela não é:

- uma duplicação de `Explorar`;
- um erro do mapa;
- uma versão reduzida;
- uma tela de contingência sem paridade;
- uma nova origem de personalização.

A superfície reformulada declara:

> **LISTA TERRITORIAL DO MAPA · MESMA CONSULTA**

## 7. Contexto Agindo como

O contexto consolidado passa a ser demonstrado:

> **Agindo como: Pessoa**

A alternância entre Mapa e Lista não poderá alterar silenciosamente:

- pessoa, Organização ou Coletivo em atuação;
- permissões aplicáveis;
- origem da consulta;
- regras de apresentação.

A ação `Alterar` deverá permitir revisão consciente do contexto quando outros papéis estiverem disponíveis.

## 8. Diferença validada entre Lista e Explorar

`Explorar` continua organizando descoberta ampla por temas, categorias, busca, listas editoriais e filtros gerais.

A Lista do Mapa mantém a consulta territorial ativa.

A diferença deverá ser compreensível por:

- título e subtítulo da superfície;
- item `Mapa` selecionado;
- alternância interna `Mapa ↔ Lista`;
- região territorial visível;
- preservação da consulta;
- retorno ao Mapa.

A pessoa não poderá ser redirecionada silenciosamente para `Explorar` ao selecionar Lista.

## 9. Estado territorial e privacidade

O exemplo permanece com:

> **Localização desativada · posição não acessada**

> **Região manual · não é sua posição**

A Lista continua funcional sem localização do dispositivo.

Localização aproximada ou exata temporária, quando autorizada, deverá manter finalidade, precisão, duração e retirada compreensíveis.

A alternância de modo não cria nova autorização territorial.

## 10. Pesquisa e região

A pesquisa reformulada declara:

> **Buscar nesta região**

A linguagem evita confundir busca territorial com troca automática de região.

A alteração de região deverá preservar filtros compatíveis e tornar incompatibilidades visíveis antes de remover condições.

## 11. Filtros ativos

O estado inicial apresentava filtros individuais e `Mais filtros · 2`, mas não consolidava o total.

A reformulação declara:

> **4 filtros ativos**

O total deverá corresponder aos filtros efetivamente aplicados, incluindo filtros ocultos em agrupamentos.

A pessoa poderá:

- revisar filtros;
- remover filtros individualmente;
- limpar todos;
- entender quais filtros deixaram de ser compatíveis após mudança territorial;
- retornar ao Mapa com o mesmo conjunto aplicável.

## 12. Quantidade, atualização e consistência

A quantidade de resultados deverá ser consistente entre Mapa e Lista para a mesma consulta e versão de dados.

A superfície reformulada demonstra:

> **8 resultados · região selecionada**

> **Atualizados há instantes · Atualizar**

Quando houver diferença temporária entre modos, a interface deverá explicar atualização, carregamento, indisponibilidade ou alteração de fonte.

## 13. Ordenação explicável

A ordenação inicial era visível, mas não oferecia explicação direta.

A reformulação declara:

> **Ordenado por: correspondência à busca e aos filtros**

> **Entender**

A explicação deverá informar:

- critérios utilizados;
- critérios não utilizados;
- ausência ou presença de personalização;
- influência de data, disponibilidade ou distância;
- limitações e dados ausentes;
- separação entre ordenação funcional e patrocínio.

Sem gate, a ordenação não poderá afirmar adequação ao Momento Atual.

## 14. Comparação entre cartões

Os cartões passam a demonstrar uma estrutura mínima consistente:

- tipo;
- modalidade;
- região ou disponibilidade online;
- título;
- responsável;
- data ou prazo;
- preço;
- disponibilidade;
- acessibilidade;
- explicação;
- relação comercial;
- ações.

A ausência de dados deverá ser explícita.

O wireframe demonstra:

- `Acessibilidade: confirmada`;
- `Acessibilidade: parcial`;
- `Acessibilidade: não informada`.

`Não informada` não significa ausência de acessibilidade. Significa somente que a informação não foi fornecida ou confirmada.

## 15. Oportunidade selecionada

A seleção passa a declarar:

> **Selecionada · preservada do Mapa**

A identificação textual reduz dependência exclusiva de borda, cor ou posição.

Ao alternar modos ou retornar do Detalhe, a pessoa deverá reencontrar o item, sua posição aproximada e o contexto aplicável.

A seleção não altera relevância nem ordenação.

## 16. Explicação funcional e relação comercial

Todos os cartões deverão oferecer explicação equivalente a `Por que está aqui?`.

A relação comercial será apresentada separadamente:

- `Relação comercial: sem patrocínio`;
- `Relação comercial: parceria identificada`;
- `Relação comercial: conteúdo patrocinado`.

Conteúdo patrocinado não poderá receber posição superior por regra oculta.

Quando patrocínio influenciar uma área publicitária separada, essa natureza deverá ser identificada e não confundida com relevância funcional.

## 17. Salvamento e Detalhe sem localização

Salvar e abrir detalhes permanecem disponíveis quando a localização estiver desativada.

Salvar não autoriza:

- localização;
- rastreamento;
- personalização;
- retenção territorial;
- inferência de residência.

O Detalhe preservará região, busca, filtros, ordenação, posição e seleção.

## 18. Origem para rota

`Definir origem` permanece ação específica e separada.

A origem poderá ser informada sem ativar rastreamento contínuo ou histórico territorial.

Endereço protegido não poderá ser revelado ou contornado pela Lista.

## 19. Retorno ao Mapa

Mapa e Lista preservam, quando aplicável:

- contexto `Agindo como`;
- região;
- busca;
- filtros;
- quantidade;
- ordenação compatível;
- item selecionado;
- posição ou foco correspondente;
- explicação da origem.

A troca de modo não altera consentimento, localização ou personalização.

## 20. Acessibilidade e resiliência

A reformulação declara:

> **Lista integral · funciona sem carregar o mapa**

A Lista não poderá depender de renderização cartográfica para apresentar dados já disponíveis.

Ela constitui alternativa integral para:

- leitores de tela;
- controles assistivos;
- preferência por conteúdo textual;
- baixa conectividade;
- falha do mapa;
- indisponibilidade do fornecedor;
- dispositivos com desempenho limitado.

Esta decisão é funcional. A conformidade técnica de acessibilidade permanece posterior.

## 21. Estados e transições validados

| Estado ou transição | Decisão funcional |
|---|---|
| abrir Lista pelo Mapa | preservar consulta e seleção |
| abrir Lista sem localização | manter região manual e posição não acessada |
| alternar para Mapa | preservar contexto e permissões |
| alterar região | preservar filtros compatíveis e explicar incompatibilidades |
| alterar ordenação | manter critérios compreensíveis e revisáveis |
| dado ausente | declarar ausência sem inferência |
| mapa indisponível | manter Lista integral |
| baixa conectividade | priorizar conteúdo textual recuperável |
| abrir Detalhe | preservar origem e posição da Lista |
| retornar do Detalhe | reencontrar item e contexto |
| salvar | não ativar localização ou personalização |
| conteúdo patrocinado | identificar relação comercial separadamente |

## 22. Reformulação aplicada ao wireframe

A UXA-028 reformulada demonstra:

- `Mapa de Oportunidades`;
- `LISTA TERRITORIAL DO MAPA · MESMA CONSULTA`;
- `Agindo como: Pessoa`;
- exploração sem personalização;
- localização desativada e posição não acessada;
- região manual distinta da posição;
- `Buscar nesta região`;
- `4 filtros ativos`;
- quantidade e atualização dos resultados;
- ordenação explicável;
- cartões com campos consistentes;
- dados ausentes declarados;
- item selecionado preservado;
- explicação funcional em todos os cartões;
- relação comercial separada;
- salvamento, origem e Detalhe;
- Lista integral sem mapa carregado;
- item `Mapa` preservado na navegação.

## 23. Resultado final

Após a reformulação, a Lista atende ao contrato funcional porque:

- pertence claramente ao Mapa;
- não duplica `Explorar`;
- preserva contexto e consulta;
- permite comparação consistente;
- torna filtros e ordenação compreensíveis;
- explicita incertezas;
- separa relevância e publicidade;
- funciona sem localização;
- funciona sem mapa carregado;
- mantém continuidade para Detalhe e retorno;
- não inicia design ou implementação.

## 24. Limites

Esta validação não:

- aprova textos finais de interface;
- define algoritmo de busca ou ordenação;
- define tecnologia ou fornecedor de mapas;
- cria coordenadas, geocodificação ou rotas;
- conclui acessibilidade técnica;
- cria versão para computador;
- cria protótipo navegável;
- executa teste de usabilidade;
- inicia Engenharia de Produto.

## 25. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar o estado sem resultados;
2. criar referência do Mapa para computador;
3. criar o wireframe gráfico do início protegido da jornada;
4. criar a referência móvel da Página Inicial pública;
5. validar a revisão da compreensão inicial;
6. validar a transição para a primeira Tela Hoje;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
