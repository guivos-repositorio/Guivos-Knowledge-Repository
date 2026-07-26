---
id: UXA-024
title: Wireframe de Baixa Fidelidade do Mapa de Oportunidades
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-26
parent: UXA-005
depends_on:
  - UXA-001
  - UXA-002
  - UXA-003
  - UXA-003-A1
  - UXA-004
  - UXA-005
  - UXA-007
  - UXA-010
  - UXA-012
related:
  - UXA-020
  - UXA-022
normative: false
---

# Wireframe de Baixa Fidelidade do Mapa de Oportunidades

## 1. Finalidade

Este documento materializa a primeira referência gráfica do Mapa de Oportunidades como superfície própria da navegação recorrente da Guivos.

O wireframe verifica hierarquia, busca, alternância entre mapa e lista, filtros, camadas, localização, seleção de um ponto, cartão resumido, privacidade territorial e continuidade para o detalhe da oportunidade.

Ele não representa mapa real, design visual, tecnologia cartográfica, dados de produção ou implementação.

## 2. Posição na experiência

O Mapa não entra entre a Página Inicial pública e a Tela Hoje.

```text
Página Inicial pública
→ início protegido da jornada
→ compreensão inicial revisável
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

A superfície também poderá ser acessada:

- pela exploração geral da Home, sem personalização;
- pela área Explorar;
- pelo bloco contextual `Perto de mim` da Tela Hoje;
- pelo detalhe de uma oportunidade;
- por um local salvo, Organização, Coletivo, atividade ou evento.

## 3. Artefato visual

![Wireframe de baixa fidelidade do Mapa de Oportunidades](../assets/wireframes/uxa-024-opportunity-map-mobile.svg)

Arquivo vetorial:

`docs/assets/wireframes/uxa-024-opportunity-map-mobile.svg`

Dimensão de referência:

- canal: aplicativo móvel;
- largura: 390 pixels;
- altura: 844 pixels;
- estado principal: pessoa autenticada, contexto pessoal ativo e localização aproximada autorizada.

## 4. Hierarquia da superfície

### 4.1 Contexto e pesquisa

O cabeçalho apresenta:

- nome completo da superfície;
- contexto de atuação atual;
- pesquisa por oportunidade, Organização ou região;
- acesso à alteração do contexto quando aplicável.

O contexto institucional ou coletivo deverá permanecer explícito quando a pessoa estiver agindo em nome de outro participante.

### 4.2 Alternância entre mapa e lista

A superfície permite alternar entre:

```text
Mapa
↔ Lista
```

A alternância não cria dois catálogos independentes. Busca, filtros, região e seleção deverão permanecer sincronizados quando aplicável.

### 4.3 Filtros essenciais

O estado principal apresenta filtros compactos de:

- período;
- distância;
- gratuidade;
- filtros adicionais ativos.

O conjunto ampliado poderá incluir categoria, data, horário, preço, modalidade, disponibilidade, elegibilidade, acessibilidade, idioma, Organização, Coletivo, origem, patrocínio, confiança da fonte e vínculo com objetivo ou Próximo Passo.

### 4.4 Área territorial

O mapa esquemático apresenta camadas de:

- oportunidades;
- Organizações;
- Coletivos;
- eventos e atividades;
- experiências públicas;
- pontos de apoio;
- locais salvos.

Agrupamentos numéricos poderão representar vários itens em uma mesma área. Formas diferentes poderão distinguir categorias, mas cor nunca deverá ser o único meio de identificação.

### 4.5 Controles territoriais

A superfície oferece controles para:

- visualizar camadas;
- aumentar ou reduzir escala;
- reposicionar a visualização;
- pesquisar nesta região;
- alterar raio;
- usar localização exata temporária, aproximada, cidade informada ou região selecionada;
- desativar localização.

## 5. Oportunidade selecionada

Ao selecionar um ponto, a pessoa recebe um cartão resumido com:

- tipo e modalidade;
- título;
- Organização, Coletivo ou fonte responsável;
- distância ou região;
- data, prazo ou disponibilidade;
- preço, gratuidade ou faixa;
- vagas ou capacidade quando material;
- acessibilidade;
- razão resumida de relevância;
- relação comercial ou ausência de patrocínio;
- ações para abrir detalhes, salvar ou criar rota.

O cartão não substitui o Detalhe de Oportunidade. Condições completas, elegibilidade, riscos, política de cancelamento, composição de preço e autoridade permanecem na superfície especializada.

## 6. Relevância e exploração

### 6.1 Antes do gate de personalização

A superfície poderá apresentar conteúdo geral, institucional, editorial ou resultante de busca explícita.

Ela não deverá afirmar que um item é adequado ao Momento Atual da pessoa.

### 6.2 Depois do gate de personalização

A Guivos poderá explicar relevância com base em objetivo, Próximo Passo, preferência, localização autorizada, disponibilidade e elegibilidade conhecida.

A pessoa deverá poder abrir `Por que aparece aqui?`, alterar filtros, ocultar categorias, reduzir o uso de localização e continuar sem recomendações pessoais.

Proximidade geográfica, popularidade, patrocínio ou comissão não constituem relevância suficiente.

## 7. Privacidade territorial

O Mapa não deverá:

- mostrar localização de participantes;
- revelar residência ou local sensível de membros;
- expor endereço protegido antes da autorização aplicável;
- exigir rastreamento contínuo;
- manter localização exata sem finalidade e prazo;
- utilizar histórico sensível para publicidade;
- presumir interesse apenas por proximidade.

O estado principal do wireframe utiliza localização aproximada e declara que a posição exata não está visível.

## 8. Estados funcionais mínimos

| Estado | Comportamento esperado |
|---|---|
| localização desativada | permite cidade ou região manual e explica limitações |
| localização aproximada | mostra área e raio sem posição exata |
| localização exata temporária | apresenta finalidade, duração e controle de encerramento |
| região sem resultados | não preenche artificialmente; oferece ampliar raio, período ou filtros |
| carregamento | mantém estrutura e estado dos filtros visíveis |
| baixa conectividade | reduz camadas e informa atualização limitada |
| item indisponível | preserva razão e data da mudança quando possível |
| endereço protegido | mostra área aproximada e condição para revelar detalhes |
| permissão revogada | interrompe uso futuro e mantém alternativas manuais |
| erro de fonte | identifica falha sem apresentar dado como confiável |

## 9. Relação com a Tela Hoje

A Tela Hoje poderá mostrar apenas um recorte compacto denominado `Perto de mim`.

Esse bloco poderá apresentar um ou poucos itens com utilidade material e oferecer a ação `Abrir no mapa`.

A Tela Hoje não incorpora o mapa completo e não se transforma em catálogo territorial.

## 10. Relação com Explorar

`Explorar` organiza descoberta por busca, lista, categorias e filtros.

`Mapa` organiza a mesma descoberta pela dimensão territorial.

```text
Explorar em lista
↔ visualizar no Mapa
↔ abrir Detalhe de Oportunidade
```

Mudanças de filtro ou região deverão permanecer compreensíveis ao alternar entre as duas superfícies.

## 11. Critérios de validação posterior

O wireframe deverá permitir verificar:

- se o Mapa é reconhecido como área própria da navegação recorrente;
- se mapa e lista parecem partes da mesma descoberta;
- se localização aproximada e exata são distinguíveis;
- se filtros essenciais são compreendidos sem excesso de densidade;
- se um ponto selecionado apresenta contexto suficiente antes do detalhe;
- se preço, origem, acessibilidade e relação comercial permanecem visíveis;
- se a pessoa entende por que um item aparece;
- se ausência de resultados não gera preenchimento artificial;
- se controles de privacidade são encontráveis;
- se a navegação para Explorar, Tela Hoje e Detalhe de Oportunidade é coerente.

## 12. Limites

Este incremento não:

- define fornecedor ou tecnologia de mapas;
- cria geocodificação, rotas ou rastreamento;
- define coordenadas, cidades ou oportunidades reais;
- define ícones, cores ou tipografia finais;
- conclui responsividade para computador ou tablet;
- cria textos finais de interface;
- cria protótipo navegável;
- executa teste de usabilidade;
- inicia Engenharia de Produto.

## 13. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. validar funcionalmente o wireframe do Mapa de Oportunidades;
2. criar estados alternativos do Mapa, como lista, ausência de resultados e localização desativada;
3. criar referência do Mapa para computador;
4. criar o wireframe gráfico do início protegido da jornada;
5. criar a referência móvel da Página Inicial pública;
6. validar a revisão da compreensão inicial;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
