---
id: UXA-024
title: Wireframe de Baixa Fidelidade do Mapa de Oportunidades
status: draft
version: 0.2.0
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
  - UXA-025
normative: false
---

# Wireframe de Baixa Fidelidade do Mapa de Oportunidades

## 1. Finalidade

Este documento materializa a referência gráfica móvel do Mapa de Oportunidades como superfície própria da navegação recorrente da Guivos.

A versão 0.2.0 incorpora a **Validação Funcional e Reformulação do Mapa de Oportunidades**, registrada em UXA-025.

O wireframe verifica hierarquia, busca, alternância sincronizada entre Mapa e Lista, filtros, camadas, localização, pesquisa regional, seleção de um ponto, cartão resumido, privacidade territorial e continuidade para o Detalhe de Oportunidade.

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
- pelo Detalhe de Oportunidade;
- por um local salvo, Organização, Coletivo, atividade ou evento.

## 3. Artefato visual reformulado

![Wireframe reformulado de baixa fidelidade do Mapa de Oportunidades](../assets/wireframes/uxa-024-opportunity-map-mobile.svg)

Arquivo vetorial:

`docs/assets/wireframes/uxa-024-opportunity-map-mobile.svg`

Dimensão de referência:

- canal: aplicativo móvel;
- largura: 390 pixels;
- altura: 844 pixels;
- estado principal: pessoa autenticada, contexto pessoal ativo e localização aproximada autorizada.

## 4. Resultado da validação funcional

A superfície foi considerada funcionalmente válida após reformulação porque:

- ocupa posição recorrente própria;
- apresenta `Agindo como: Minha jornada` de forma explícita;
- trata Mapa e Lista como uma descoberta única;
- preserva pesquisa, filtros, região e seleção;
- oferece `Pesquisar nesta região` após mudança territorial;
- distingue localização aproximada, exata temporária, manual e desativada;
- torna localização e privacidade encontráveis;
- preserva preço, origem, acessibilidade e relação comercial;
- explica por que um item aparece;
- mantém o Detalhe de Oportunidade como superfície especializada;
- protege localização de participantes e endereços sensíveis;
- separa proximidade e patrocínio de relevância funcional;
- mantém conteúdo anterior ao gate sem personalização simulada.

A autoridade da validação é UXA-025.

## 5. Hierarquia aprovada

A ordem funcional do estado principal é:

```text
nome da superfície e contexto de atuação
→ pesquisa
→ Mapa | Lista com estado compartilhado
→ filtros ativos
→ região territorial e Pesquisar nesta região
→ camadas e escala
→ localização, raio e privacidade
→ ponto ou agrupamento selecionado
→ cartão resumido
→ explicação de relevância e relação comercial
→ detalhe, salvamento ou rota
→ navegação recorrente
```

### 5.1 Contexto e pesquisa

O cabeçalho apresenta:

- nome da superfície;
- formulação `Agindo como`;
- participante representado, quando aplicável;
- pesquisa por oportunidade, Organização ou região;
- acesso consciente à mudança de contexto.

A interface deverá impedir que uma ação institucional seja executada como ação pessoal ou vice-versa.

### 5.2 Alternância entre Mapa e Lista

A superfície permite alternar entre:

```text
Mapa
↔ Lista
```

A alternância preservará, quando aplicável:

- texto pesquisado;
- região;
- filtros;
- período;
- raio;
- camadas;
- item selecionado;
- posição de retorno ao detalhe;
- distinção entre conteúdo geral e personalizado.

A Lista funciona como alternativa equivalente à representação espacial.

### 5.3 Filtros essenciais

O estado principal apresenta filtros compactos de:

- período;
- distância;
- gratuidade;
- quantidade de filtros adicionais ativos.

O conjunto ampliado poderá incluir categoria, data, horário, preço, subsídio, modalidade, disponibilidade, elegibilidade, acessibilidade, idioma, Organização, Coletivo, origem, patrocínio, confiança da fonte e vínculo com objetivo ou Próximo Passo.

### 5.4 Pesquisa territorial

Depois de movimentar, ampliar ou reduzir a área, a interface oferece:

> **Pesquisar nesta região**

A pessoa deverá compreender se os resultados decorrem da posição atual, região movida, cidade informada, busca textual, filtro explícito ou personalização autorizada.

### 5.5 Área e camadas territoriais

O mapa esquemático poderá apresentar:

- oportunidades;
- Organizações;
- Coletivos;
- eventos e atividades;
- experiências públicas;
- pontos de apoio;
- locais salvos.

Agrupamentos numéricos poderão representar vários itens em uma mesma área. Formas, rótulos e Lista equivalente deverão impedir dependência exclusiva de cor.

### 5.6 Controles territoriais

A superfície oferece controles para:

- visualizar e ajustar camadas;
- aumentar ou reduzir escala;
- reposicionar a visualização;
- pesquisar na região movida;
- alterar raio;
- usar localização exata temporária, aproximada, cidade informada ou região selecionada;
- desativar localização;
- ajustar localização e privacidade.

## 6. Oportunidade selecionada

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
- ações para abrir detalhes, salvar ou ver rota.

A explicação será apresentada como:

> **Por que estou vendo isto?**

O cartão não substitui o Detalhe de Oportunidade. Condições completas, elegibilidade, riscos, cancelamento, composição de preço e autoridade permanecem na superfície especializada.

## 7. Relevância e exploração

### 7.1 Antes do gate de personalização

A superfície poderá apresentar conteúdo geral, institucional, editorial ou resultante de busca e filtros explícitos.

Ela não deverá afirmar que um item é adequado ao Momento Atual da pessoa.

### 7.2 Depois do gate de personalização

A Guivos poderá explicar relevância com base em objetivo, Próximo Passo, preferência, localização autorizada, disponibilidade e elegibilidade conhecida.

A pessoa poderá revisar informações utilizadas, corrigir seu momento, ocultar categorias, reduzir uso de localização, declarar que o item não faz sentido e continuar sem recomendações pessoais.

Proximidade geográfica, popularidade, patrocínio ou comissão não constituem relevância suficiente.

## 8. Privacidade territorial

O Mapa não deverá:

- mostrar localização de participantes;
- revelar residência ou local sensível de membros;
- expor endereço protegido antes da autorização aplicável;
- exigir rastreamento contínuo;
- manter localização exata sem finalidade e prazo;
- utilizar histórico sensível para publicidade;
- presumir interesse apenas por proximidade.

O estado principal utiliza localização aproximada, declara que a posição exata não está visível e oferece `Ajustar localização e privacidade`.

Localização exata temporária exigirá finalidade, duração, indicador de uso e ação de encerramento.

## 9. Rota e serviço externo

A ação do cartão será `Ver rota` quando deslocamento for material.

Antes de abrir serviço externo ou compartilhar localização, a interface deverá informar executor, destino, localização utilizada, dados transferidos, possibilidade de cancelar e alternativa manual.

O Mapa não apresentará rota para oportunidades exclusivamente online.

## 10. Estados funcionais mínimos

| Estado | Comportamento esperado |
|---|---|
| localização desativada | permite cidade ou região manual e explica limitações |
| localização aproximada | mostra área e raio sem posição exata |
| localização exata temporária | apresenta finalidade, duração e controle de encerramento |
| região sem resultados | não preenche artificialmente; oferece ampliar raio, período ou filtros |
| carregamento | mantém estrutura, pesquisa, filtros e região anterior |
| baixa conectividade | reduz camadas e informa atualização limitada |
| item indisponível | preserva razão e data da mudança quando possível |
| endereço protegido | mostra área aproximada e condição para revelar detalhes |
| permissão revogada | interrompe uso futuro e mantém alternativas manuais |
| erro de fonte | identifica falha sem apresentar dado como confiável |
| mudança de região | oferece `Pesquisar nesta região` antes de substituir resultados |
| Lista ativa | preserva estado compartilhado e conteúdo equivalente |
| contexto institucional | identifica Organização, unidade, papel e autoridade |
| contexto coletivo | identifica Coletivo, papel e limites de representação |

## 11. Relação com a Tela Hoje

A Tela Hoje poderá mostrar somente um recorte compacto denominado `Perto de mim`.

Esse bloco poderá apresentar um ou poucos itens com utilidade material e oferecer `Abrir no mapa`.

A Tela Hoje não incorpora o mapa completo e não se transforma em catálogo territorial.

## 12. Relação com Explorar

`Explorar` organiza descoberta por busca, lista, categorias e filtros.

`Mapa` organiza a mesma descoberta pela dimensão territorial.

```text
Explorar em lista
↔ visualizar no Mapa
↔ abrir Detalhe de Oportunidade
```

Mudanças de filtro, região e seleção permanecerão compreensíveis ao alternar entre as superfícies.

## 13. Limites

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

## 14. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar estados alternativos do Mapa, começando por Lista, ausência de resultados ou localização desativada;
2. criar referência do Mapa para computador;
3. criar o wireframe gráfico do início protegido da jornada;
4. criar a referência móvel da Página Inicial pública;
5. validar a revisão da compreensão inicial;
6. validar a transição específica para a primeira Tela Hoje;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
