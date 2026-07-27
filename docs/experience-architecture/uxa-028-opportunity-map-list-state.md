---
id: UXA-028
title: Wireframe Alternativo do Mapa de Oportunidades — Visualização em Lista
status: active
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-27
parent: UXA-024
depends_on:
  - UXA-004
  - UXA-005
  - UXA-024
  - UXA-025
  - UXA-026
  - UXA-027
related:
  - UXA-002
  - UXA-007
  - UXA-010
  - UXA-012
  - UXA-020
  - UXA-023
  - UXA-029
normative: false
---

# Wireframe Alternativo do Mapa de Oportunidades — Visualização em Lista

## 1. Finalidade

Este documento materializa a visualização em Lista da mesma descoberta territorial governada pelo Mapa de Oportunidades.

A versão 0.2.0 incorpora a reformulação governada pela **UXA-029 — Validação Funcional Especializada e Reformulação da Visualização em Lista do Mapa**.

A Lista não é uma superfície inferior, uma mensagem de erro ou uma duplicação de `Explorar`. Ela é uma representação textual integral da consulta territorial ativa e preserva o contexto ao alternar entre Mapa e Lista.

O wireframe demonstra o estado com localização desativada, posição não acessada e região escolhida manualmente. A Lista também poderá operar quando houver localização aproximada ou exata temporária autorizada, respeitando os controles aplicáveis.

O artefato não representa design visual, tecnologia, dados reais, algoritmo de ordenação, implementação ou teste com usuários.

## 2. Posição na experiência

A Lista permanece dentro da superfície recorrente do Mapa:

```text
Hoje | Jornada | Explorar | Mapa | Eu
```

O item `Mapa` continua selecionado na navegação principal. A alternância interna ocorre entre:

```text
Mapa ↔ Lista
```

A Lista poderá ser escolhida pela pessoa ou apresentada como continuidade quando:

- a pessoa preferir leitura textual;
- o mapa não estiver disponível;
- houver baixa conectividade;
- recursos cartográficos apresentarem falha;
- o uso do mapa não for adequado à acessibilidade;
- a comparação entre oportunidades for mais útil em cartões;
- a localização estiver desativada;
- a região tiver sido informada manualmente.

## 3. Diferença entre Explorar e Lista do Mapa

`Explorar` organiza descoberta ampla por busca, categorias, temas, listas editoriais e filtros gerais.

A Lista do Mapa representa a mesma consulta territorial já aberta na superfície `Mapa`.

O wireframe reformulado declara:

> **LISTA TERRITORIAL DO MAPA · MESMA CONSULTA**

A Lista preserva:

- região ou área territorial ativa;
- busca;
- filtros;
- quantidade de resultados;
- ordenação;
- item selecionado;
- explicação de origem;
- condições conhecidas;
- retorno ao Mapa.

Mudar para a Lista não transporta a pessoa silenciosamente para `Explorar` nem reinicia a consulta.

## 4. Artefato visual reformulado

![Wireframe reformulado do Mapa de Oportunidades em visualização de Lista](../assets/wireframes/uxa-028-opportunity-map-list-mobile.svg)

Arquivo vetorial:

`docs/assets/wireframes/uxa-028-opportunity-map-list-mobile.svg`

Dimensão de referência:

- canal: aplicativo móvel;
- largura: 390 pixels;
- altura: 844 pixels;
- modo: Lista selecionada dentro da superfície Mapa;
- condição ilustrada: localização desativada, posição não acessada e região manual;
- resultado: funcionalmente válido após reformulação registrada em UXA-029.

## 5. Hierarquia funcional validada

```text
nome da superfície
→ declaração de Lista territorial do Mapa
→ contexto Agindo como
→ estado territorial e privacidade
→ região ativa e editável
→ pesquisa territorial
→ alternância Mapa ou Lista
→ total e identificação dos filtros ativos
→ quantidade e atualização dos resultados
→ ordenação explícita e explicável
→ cartões comparáveis
→ oportunidade selecionada preservada
→ explicação, relação comercial, salvamento e detalhe
→ retorno ao Mapa sem perda de contexto
→ Lista integral sem dependência do mapa carregado
→ navegação recorrente
```

A Lista prioriza compreensão, comparação e continuidade, sem esconder por que os resultados aparecem.

## 6. Contexto Agindo como

O contexto consolidado deverá permanecer visível:

> **Agindo como: Pessoa**

Quando outros contextos forem permitidos, a pessoa deverá poder revisar e alterar a atuação de forma consciente.

Trocar o modo Mapa ou Lista não altera o contexto de atuação.

## 7. Contexto territorial

Quando a localização estiver desativada, a Lista preservará as declarações:

> **Localização desativada · posição não acessada**

> **Região manual · não é sua posição**

A região permanecerá visível e editável antes dos resultados.

Quando localização estiver autorizada, a interface indicará precisão, finalidade e duração aplicáveis, sem tornar rastreamento contínuo requisito da Lista.

## 8. Pesquisa, filtros e atualização

A Lista preserva a mesma busca e os mesmos filtros compatíveis do Mapa.

O campo de pesquisa reformulado declara:

> **Buscar nesta região**

A superfície mostra:

- termos pesquisados;
- total consolidado de filtros ativos;
- filtros identificáveis sem depender somente de cor;
- quantidade de filtros adicionais;
- ação para limpar filtros;
- quantidade de resultados;
- região à qual os resultados correspondem;
- momento da última atualização;
- ação para atualizar resultados.

O exemplo declara:

> **4 filtros ativos**

A troca de modo não apaga silenciosamente busca, filtros ou região.

## 9. Quantidade e ordenação

A quantidade de resultados permanece consistente entre Mapa e Lista para a mesma consulta e momento de atualização.

A ordenação é explícita, revisável e acompanhada de ação explicativa:

> **Ordenado por: correspondência à busca e aos filtros**

> **Entender**

A explicação deverá informar os critérios aplicados e as limitações conhecidas.

A ordenação poderá considerar:

- correspondência com busca e filtros;
- data ou prazo;
- disponibilidade;
- modalidade;
- acessibilidade;
- preço ou gratuidade;
- distância de uma origem válida, quando aplicável;
- critérios editoriais ou institucionais declarados.

Sem gate de personalização, a ordenação não poderá ser apresentada como `melhor para você`, `ideal para seu momento` ou equivalente.

Patrocínio não poderá elevar relevância funcional de forma oculta. Relação comercial será informada separadamente.

## 10. Cartões comparáveis

Cada cartão apresenta uma estrutura mínima consistente:

- tipo de oportunidade;
- modalidade;
- cidade, bairro, região ou disponibilidade online;
- título;
- responsável ou fonte;
- data, horário ou prazo;
- preço ou gratuidade;
- vagas ou disponibilidade;
- acessibilidade conhecida;
- origem do resultado;
- relação comercial;
- ações disponíveis.

A ausência de informação é declarada como `não informada`, `não confirmada` ou `indisponível`, sem completar dados por inferência.

O wireframe reformulado demonstra:

- `Acessibilidade: confirmada`;
- `Acessibilidade: parcial`;
- `Acessibilidade: não informada`.

## 11. Oportunidade selecionada

A oportunidade selecionada no Mapa permanece identificada ao abrir a Lista.

O wireframe reformulado declara:

> **Selecionada · preservada do Mapa**

A seleção poderá ser demonstrada por:

- borda estrutural;
- rótulo textual;
- posição inicial na Lista, quando compatível com a ordenação;
- foco acessível;
- retorno ao mesmo cartão após fechar o Detalhe.

A seleção não altera relevância, não implica recomendação e não modifica a ordenação sem regra explícita.

## 12. Explicação e relação comercial

Cada oportunidade oferece `Por que está aqui?` ou explicação equivalente.

A explicação poderá incluir:

- correspondência com a região ativa;
- busca explícita;
- filtros aplicados;
- categoria ou modalidade;
- data e disponibilidade;
- origem editorial, institucional ou organizacional;
- critério de ordenação.

Ela não simula conhecimento do Momento Atual quando o gate não estiver atendido.

A relação comercial é apresentada em campo separado, com exemplos:

- `Relação comercial: sem patrocínio`;
- `Relação comercial: parceria identificada`;
- `Relação comercial: conteúdo patrocinado`.

A presença de relação comercial não modifica silenciosamente a posição do cartão.

## 13. Salvamento e Detalhe

Salvar permanece disponível na Lista independentemente de localização.

O salvamento não autoriza:

- ativar localização;
- personalizar recomendações;
- registrar deslocamento;
- criar histórico territorial;
- contornar preferências de privacidade.

`Ver detalhes` abre o Detalhe de Oportunidade preservando:

- origem da navegação;
- região ativa;
- busca e filtros;
- ordenação;
- posição da Lista;
- item selecionado;
- condições conhecidas.

Ao retornar, a pessoa reencontra o mesmo contexto.

## 14. Origem para rota

Quando a localização estiver desativada, a Lista poderá apresentar `Definir origem`.

A ação solicita origem específica e não inicia rastreamento contínuo, histórico territorial ou presunção de residência.

Endereços protegidos permanecem limitados à área permitida ou à condição de liberação aplicável.

## 15. Retorno ao Mapa

Ao retornar ao Mapa, permanecem:

- região ou área territorial;
- busca;
- filtros;
- ordenação compatível;
- quantidade de resultados;
- item selecionado;
- posição ou foco correspondente, quando possível;
- explicação da origem dos resultados.

A troca não executa nova personalização, não altera consentimento e não redefine localização.

## 16. Acessibilidade e resiliência

A Lista constitui alternativa integral para:

- leitores de tela;
- navegação por teclado ou controles assistivos;
- pessoas que preferem conteúdo textual;
- baixa conectividade;
- indisponibilidade do fornecedor cartográfico;
- falha de carregamento do mapa;
- dispositivos com desempenho limitado.

O wireframe reformulado declara:

> **Lista integral · funciona sem carregar o mapa**

A Lista não depende de mapa carregado para apresentar oportunidades já disponíveis na consulta.

Estados de carregamento, atualização, ausência de resultados e erro de fonte serão textuais e recuperáveis.

## 17. Privacidade e autonomia

A Lista preserva:

- localização opcional;
- posição não acessada quando verdadeiro;
- região manual distinta da posição pessoal;
- exploração sem personalização;
- explicação de critérios;
- comparação sem pressão comercial;
- salvamento sem consentimento territorial;
- retorno ao Mapa sem alteração silenciosa;
- proteção de endereços sensíveis;
- separação entre proximidade, relevância e publicidade.

## 18. Resultado da validação

A validação funcional especializada está registrada em UXA-029.

A visualização em Lista é considerada **funcionalmente válida após reformulação** porque:

- identifica que pertence ao Mapa e representa a mesma consulta;
- distingue-se visualmente de `Explorar`;
- preserva contexto `Agindo como`;
- mantém região, busca, filtros, quantidade e seleção;
- explicita o total de filtros ativos;
- torna atualização e ordenação compreensíveis;
- padroniza campos comparáveis;
- declara dados ausentes sem inferência;
- separa explicação funcional de relação comercial;
- mantém salvamento e Detalhe sem localização;
- retorna ao Mapa sem perda de contexto;
- funciona sem dependência do mapa carregado;
- não inicia design ou implementação.

## 19. Limites

Este incremento não:

- valida a Lista com usuários reais;
- define algoritmo de busca ou ordenação;
- cria dados de produção;
- conclui acessibilidade técnica;
- define tecnologia cartográfica;
- cria geocodificação ou rotas;
- cria referência para computador;
- cria protótipo navegável;
- inicia design visual;
- inicia Engenharia de Produto.

## 20. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar o estado sem resultados;
2. criar referência do Mapa para computador;
3. criar o wireframe gráfico do início protegido da jornada;
4. criar a referência móvel da Página Inicial pública;
5. validar a revisão da compreensão inicial;
6. validar a transição para a primeira Tela Hoje;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
