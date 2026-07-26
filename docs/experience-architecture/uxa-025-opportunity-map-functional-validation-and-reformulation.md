---
id: UXA-025
title: Validação Funcional e Reformulação do Mapa de Oportunidades
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-26
parent: UXA-000
depends_on:
  - UXA-001
  - UXA-004
  - UXA-005
  - UXA-009
  - UXA-011
  - UXA-012
  - UXA-024
related:
  - UXA-002
  - UXA-006
  - UXA-007
  - UXA-010
  - UXA-020
  - UXA-023
normative: true
---

# Validação Funcional e Reformulação do Mapa de Oportunidades

## 1. Finalidade

Este documento registra a primeira validação arquitetural funcional do **Mapa de Oportunidades**, governa a reformulação do wireframe móvel UXA-024 e define os contratos mínimos que deverão permanecer válidos em estados posteriores.

A validação responde:

> Como permitir descoberta territorial de oportunidades, Organizações, Coletivos, eventos e pontos de apoio sem reduzir relevância à proximidade, ocultar condições materiais, confundir Mapa e Lista ou expor localização pessoal indevidamente?

A análise é documental e estrutural. Ela não constitui teste de usabilidade com participantes, validação cartográfica, definição tecnológica, design visual ou autorização de desenvolvimento.

## 2. Decisão registrada

Em 26/07/2026, o Fundador autorizou a validação funcional da UXA-024 após a integração do primeiro wireframe gráfico móvel do Mapa de Oportunidades.

O resultado é:

> **Mapa de Oportunidades funcionalmente válido após reformulação.**

A aprovação permanece condicionada à incorporação dos ajustes descritos neste documento e não torna a navegação, os textos, os componentes ou a tecnologia definitivos.

## 3. Diagnóstico do wireframe inicial

O wireframe inicial já demonstrava:

- posição do Mapa como superfície própria da navegação recorrente;
- pesquisa por oportunidade, Organização ou região;
- alternância entre Mapa e Lista;
- filtros compactos;
- mapa esquemático sem geografia real;
- camadas territoriais;
- agrupamentos e pontos selecionáveis;
- localização aproximada declarada;
- cartão resumido com preço, distância, data, vagas, acessibilidade e origem;
- explicação resumida de relevância e relação comercial;
- ações para detalhe, salvamento e rota;
- navegação `Hoje | Jornada | Explorar | Mapa | Eu`.

Entretanto, quatro lacunas materiais impediam considerar a superfície plenamente validada:

1. o contexto de atuação era indicado, mas não utilizava a formulação explícita `Agindo como`;
2. a movimentação territorial não oferecia a ação visível `Pesquisar nesta região`;
3. o acesso a localização e privacidade era genérico e pouco encontrável;
4. a sincronização entre Mapa e Lista estava descrita no documento, mas precisava ser reforçada como contrato de estado compartilhado.

Também foram identificadas necessidades de precisão sobre camadas, rota, estados alternativos, conteúdo anterior ao gate e proteção de endereços sensíveis.

## 4. Critérios de validação

A superfície foi avaliada pelos seguintes critérios:

| Critério | Pergunta de validação |
|---|---|
| posição funcional | o Mapa é reconhecido como área recorrente própria, sem entrar entre Home e Tela Hoje? |
| contexto de atuação | a pessoa sabe se age em sua jornada, por uma Organização ou por um Coletivo? |
| descoberta | pesquisa, filtros, região e camadas permitem encontrar possibilidades sem catálogo infinito? |
| continuidade | Mapa, Lista, Explorar, Tela Hoje e Detalhe de Oportunidade preservam contexto compreensível? |
| relevância | proximidade, popularidade e patrocínio permanecem separados de adequação pessoal? |
| transparência | preço, origem, disponibilidade, acessibilidade e relação comercial aparecem antes da decisão? |
| autonomia | localização, raio, filtros, camadas e recomendações podem ser ajustados ou desativados? |
| privacidade | localização de participantes, residências e locais protegidos permanecem fora da exposição indevida? |
| acessibilidade | informação não depende somente de cor, gesto ou representação espacial? |
| estados | ausência, erro, baixa conectividade e permissão revogada possuem comportamento governado? |

## 5. Hierarquia funcional aprovada

A ordem funcional da superfície passa a ser:

```text
nome da superfície e contexto de atuação
→ pesquisa
→ alternância Mapa | Lista com estado compartilhado
→ filtros ativos e acesso aos filtros ampliados
→ região territorial e ação Pesquisar nesta região
→ camadas e controles de escala
→ localização, raio e privacidade
→ ponto ou agrupamento selecionado
→ cartão resumido da possibilidade
→ explicação de relevância e relação comercial
→ detalhe, salvamento ou rota contextual
→ navegação recorrente
```

O mapa gráfico não poderá dominar a leitura a ponto de ocultar pesquisa, filtros, localização, privacidade ou condições da oportunidade selecionada.

## 6. Reformulações aplicadas

### 6.1 Contexto de atuação explícito

O cabeçalho utilizará a formulação:

> **Agindo como: Minha jornada**

Quando a pessoa representar uma Organização ou atuar em um Coletivo, o nome do participante representado e o papel aplicável deverão permanecer visíveis.

A mudança de contexto deverá ser consciente, reversível e impedir que ações institucionais sejam executadas como ações pessoais ou vice-versa.

### 6.2 Mapa e Lista como uma única descoberta

`Mapa` e `Lista` não são catálogos independentes.

Ao alternar entre eles, deverão ser preservados, quando aplicável:

- texto pesquisado;
- região visualizada;
- filtros ativos;
- período;
- raio ou área;
- ordenação compatível;
- camadas selecionadas;
- item ou agrupamento selecionado;
- posição de retorno ao detalhe;
- distinção entre conteúdo geral e conteúdo personalizado.

A Lista deverá oferecer alternativa equivalente para pessoas que não possam ou não desejem interpretar uma representação espacial.

### 6.3 Pesquisa nesta região

Depois de movimentar, ampliar ou reduzir a área territorial, a interface deverá apresentar a ação:

> **Pesquisar nesta região**

A pesquisa não deverá ser disparada silenciosamente quando isso puder consumir localização, rede, processamento ou alterar substancialmente os resultados.

A pessoa deverá compreender se está vendo:

- resultados da posição atual;
- resultados da região movida manualmente;
- resultados de uma cidade informada;
- resultados de uma busca textual;
- resultados personalizados ou somente gerais.

### 6.4 Filtros progressivos

O primeiro nível poderá apresentar período, distância, gratuidade e quantidade de filtros adicionais ativos.

O conjunto ampliado poderá incluir categoria, data, horário, preço, subsídio, modalidade, disponibilidade, elegibilidade, acessibilidade, idioma, Organização, Coletivo, origem, patrocínio, confiança da fonte e vínculo com objetivo ou Próximo Passo.

Filtros deverão:

- mostrar quais estão ativos;
- permitir remoção individual;
- oferecer limpeza consciente;
- preservar ausência legítima de resultados;
- não esconder conteúdo pago por padrão comercial;
- não utilizar dados sensíveis sem base e autorização compatíveis.

### 6.5 Camadas territoriais

Camadas poderão representar oportunidades, Organizações, Coletivos, eventos, atividades, experiências públicas, pontos de apoio e locais salvos.

A distinção não dependerá somente de cor. Formas, rótulos, padrões, lista equivalente e descrição acessível deverão permitir interpretação alternativa.

A pessoa poderá ativar ou ocultar camadas sem alterar silenciosamente suas preferências permanentes.

### 6.6 Localização e privacidade

O estado principal continuará utilizando localização aproximada e declarará que a posição exata não está visível.

O acesso passará a ser identificado como:

> **Ajustar localização e privacidade**

A pessoa poderá escolher entre:

- localização exata temporária;
- localização aproximada;
- cidade informada;
- região selecionada;
- localização desativada.

Localização exata temporária exigirá finalidade, duração, indicador de uso e ação de encerramento. Revogação interromperá usos futuros e manterá alternativas manuais.

O Mapa não mostrará localização de participantes, residências, rotinas sensíveis ou pontos protegidos sem autorização aplicável.

### 6.7 Cartão da possibilidade selecionada

O cartão resumido continuará apresentando:

- tipo e modalidade;
- título;
- responsável e origem;
- distância ou região;
- data, prazo ou disponibilidade;
- preço, gratuidade ou faixa;
- vagas ou capacidade quando material;
- acessibilidade;
- razão resumida de relevância;
- relação comercial;
- ações contextuais.

O texto de explicação será padronizado como:

> **Por que estou vendo isto?**

Quando a base de personalização for insuficiente, a superfície deverá declarar que o item decorre de busca, filtro, região ou conteúdo geral, sem afirmar adequação ao Momento Atual.

O cartão não substitui o Detalhe de Oportunidade.

### 6.8 Rota e compartilhamento externo

A ação do cartão será apresentada como `Ver rota` quando deslocamento for material.

Antes de abrir serviço externo ou compartilhar localização, a interface deverá informar:

- executor da rota;
- destino;
- localização utilizada;
- dados transferidos;
- possibilidade de cancelar;
- alternativa de copiar endereço ou orientação sem compartilhamento automático.

Rotas não serão exibidas para oportunidades exclusivamente online.

## 7. Relação com a relevância pessoal

### 7.1 Antes do gate

Antes da compreensão inicial suficiente, revisável e autorizada, o Mapa poderá apresentar somente conteúdo:

- geral;
- institucional;
- editorial;
- resultante de busca explícita;
- resultante de filtros definidos pela própria pessoa;
- relacionado à cidade ou região selecionada sem afirmar relevância pessoal.

### 7.2 Depois do gate

Depois do gate, a Guivos poderá explicar relações com objetivo, Próximo Passo, preferência, disponibilidade, elegibilidade conhecida e localização autorizada.

A pessoa poderá:

- revisar informações utilizadas;
- corrigir seu momento;
- remover uma informação da justificativa;
- ocultar categoria, Organização ou Coletivo;
- reduzir uso de localização;
- continuar sem recomendações pessoais;
- declarar que a possibilidade não faz sentido.

Proximidade, popularidade, patrocínio, comissão ou posição comercial não constituem relevância suficiente.

## 8. Estados funcionais governados

| Estado | Comportamento obrigatório |
|---|---|
| localização desativada | permite cidade ou região manual e explica o que deixa de funcionar |
| localização aproximada | mostra área e raio sem posição exata |
| localização exata temporária | mostra finalidade, duração, uso ativo e encerramento |
| região sem resultados | não preenche artificialmente; oferece ampliar área, período ou filtros |
| carregamento | preserva estrutura, busca, filtros e região anterior |
| baixa conectividade | reduz camadas, informa atualização limitada e preserva lista disponível quando possível |
| item indisponível | explica mudança, fonte e data quando conhecidas |
| endereço protegido | mostra área aproximada e condição legítima para revelar detalhes |
| permissão revogada | interrompe uso futuro e oferece alternativas manuais |
| erro de fonte | identifica falha e não apresenta dado como confirmado |
| mudança de região | oferece `Pesquisar nesta região` antes de substituir resultados |
| Lista ativa | preserva estado compartilhado e oferece conteúdo equivalente ao mapa |
| contexto institucional | identifica Organização, unidade, papel e escopo de autoridade |
| contexto coletivo | identifica Coletivo, papel e limites de representação |

Estados alternativos poderão receber wireframes próprios em atos posteriores. Esta validação governa o comportamento, mas não os cria automaticamente.

## 9. Gate de alinhamento à Fundação

### 9.1 Essência

O Mapa reduz distância entre o Momento Atual e possibilidades concretas no território, sem transformar proximidade em finalidade.

### 9.2 Propósito

A superfície amplia acesso a oportunidades, experiências, apoio, Organizações e Coletivos mantendo compreensão e decisão com a pessoa.

### 9.3 Missão Operacional

Pesquisa, filtros, contexto, condições e privacidade deverão permitir uma decisão informada sobre onde olhar e qual possibilidade conhecer.

### 9.4 Visão de Longo Prazo

O contrato deverá funcionar em diferentes países, culturas, densidades territoriais, condições de conectividade e regimes de localização, sem depender de um fornecedor cartográfico específico.

### 9.5 Constituição e Princípios Permanentes

A reformulação preserva evolução como finalidade, oportunidade como meio, autonomia, contexto, transparência, acessibilidade, validade global, experiência no mundo real e separação entre relevância funcional e interesse comercial.

## 10. Resultado da validação

A UXA-024 é considerada funcionalmente válida após a reformulação porque:

- ocupa posição recorrente própria;
- torna o contexto de atuação explícito;
- trata Mapa e Lista como uma descoberta única;
- preserva pesquisa, filtros, região e seleção;
- oferece pesquisa consciente na região movimentada;
- distingue localização aproximada, exata temporária, manual e desativada;
- torna localização e privacidade encontráveis;
- preserva preço, origem, acessibilidade e relação comercial;
- explica por que um item aparece;
- mantém detalhe especializado antes de decisão material;
- impede exposição de participantes e locais sensíveis;
- separa proximidade e patrocínio de relevância;
- mantém conteúdo anterior ao gate sem personalização simulada;
- preserva alternativas em baixa conectividade e ausência de resultados.

## 11. Limites

Esta validação não autoriza:

- escolha de fornecedor ou tecnologia de mapas;
- geocodificação, rotas, rastreamento ou coordenadas reais;
- coleta contínua de localização;
- textos finais de interface;
- identidade visual, cores, tipografia ou iconografia;
- protótipo navegável;
- teste de usabilidade;
- referência para computador;
- criação automática de estados alternativos;
- Engenharia de Produto.

## 12. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar estados alternativos do Mapa, começando por Lista, ausência de resultados ou localização desativada;
2. criar referência do Mapa para computador;
3. criar o wireframe gráfico do início protegido da jornada;
4. criar a referência móvel da Página Inicial pública;
5. validar a revisão da compreensão inicial;
6. validar a transição específica para a primeira Tela Hoje;
7. retomar independentemente a reaplicação dos quatro testes dos Resultados Empresariais.

Nenhum ato posterior é iniciado automaticamente.
