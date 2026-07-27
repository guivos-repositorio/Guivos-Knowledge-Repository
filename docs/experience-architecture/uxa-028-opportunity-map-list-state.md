---
id: UXA-028
title: Wireframe Alternativo do Mapa de Oportunidades — Visualização em Lista
status: draft
version: 0.1.0
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
normative: false
---

# Wireframe Alternativo do Mapa de Oportunidades — Visualização em Lista

## 1. Finalidade

Este documento materializa a visualização em Lista da mesma descoberta territorial governada pelo Mapa de Oportunidades.

A Lista não é uma superfície inferior, uma mensagem de erro ou uma duplicação de `Explorar`. Ela é uma representação textual integral da consulta territorial ativa e deverá preservar o contexto ao alternar entre Mapa e Lista.

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

A Lista do Mapa representa a mesma consulta territorial já aberta na superfície `Mapa` e preserva:

- região ou área territorial ativa;
- busca;
- filtros;
- quantidade de resultados;
- ordenação;
- item selecionado;
- explicação de origem;
- condições conhecidas;
- retorno ao Mapa.

Mudar para a Lista não deverá transportar a pessoa silenciosamente para `Explorar` nem reiniciar a consulta.

## 4. Artefato visual

![Wireframe alternativo do Mapa de Oportunidades em visualização de Lista](../assets/wireframes/uxa-028-opportunity-map-list-mobile.svg)

Arquivo vetorial:

`docs/assets/wireframes/uxa-028-opportunity-map-list-mobile.svg`

Dimensão de referência:

- canal: aplicativo móvel;
- largura: 390 pixels;
- altura: 844 pixels;
- modo: Lista selecionada dentro da superfície Mapa;
- condição ilustrada: localização desativada, posição não acessada e região manual.

## 5. Hierarquia funcional

```text
nome da superfície e contexto de exploração
→ estado territorial e privacidade
→ região ativa e editável
→ pesquisa
→ alternância Mapa ou Lista
→ filtros ativos
→ quantidade de resultados
→ ordenação explícita
→ cartões comparáveis
→ oportunidade selecionada preservada
→ explicação, relação comercial, salvamento e detalhe
→ retorno ao Mapa sem perda de contexto
→ navegação recorrente
```

A Lista deverá priorizar compreensão, comparação e continuidade, sem esconder por que os resultados aparecem.

## 6. Contexto territorial

Quando a localização estiver desativada, a Lista deverá preservar as declarações:

> **Localização desativada · posição não acessada**

> **Região informada manualmente · não é sua posição**

A região deverá permanecer visível e editável antes dos resultados.

Quando localização estiver autorizada, a interface deverá indicar precisão, finalidade e duração aplicáveis, sem tornar rastreamento contínuo requisito da Lista.

## 7. Pesquisa, filtros e atualização

A Lista deverá preservar a mesma busca e os mesmos filtros compatíveis do Mapa.

Ela deverá mostrar:

- termos pesquisados;
- filtros ativos identificáveis sem depender somente de cor;
- quantidade de filtros adicionais;
- ação para limpar filtros;
- quantidade de resultados;
- região à qual os resultados correspondem;
- ação para atualizar resultados quando a consulta territorial mudar.

A troca de modo não poderá apagar silenciosamente busca, filtros ou região.

## 8. Quantidade e ordenação

A quantidade de resultados deverá permanecer consistente entre Mapa e Lista para a mesma consulta e momento de atualização.

A ordenação deverá ser explícita e revisável. Poderá considerar:

- correspondência com busca e filtros;
- data ou prazo;
- disponibilidade;
- modalidade;
- acessibilidade;
- preço ou gratuidade;
- distância de uma origem válida, quando aplicável;
- critérios editoriais ou institucionais declarados.

Sem gate de personalização, a ordenação não poderá ser apresentada como `melhor para você`, `ideal para seu momento` ou equivalente.

Patrocínio não poderá elevar relevância funcional de forma oculta. Relação comercial deverá ser informada separadamente.

## 9. Cartões comparáveis

Cada cartão deverá apresentar informações suficientes para comparação antes do detalhe:

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

A ausência de uma informação deverá ser indicada como não informada, não confirmada ou indisponível, sem completar dados por inferência.

## 10. Oportunidade selecionada

A oportunidade selecionada no Mapa deverá permanecer identificada ao abrir a Lista.

A seleção poderá ser demonstrada por:

- borda estrutural;
- rótulo textual `Selecionada`;
- posição inicial na Lista, quando compatível com a ordenação;
- foco acessível;
- retorno ao mesmo cartão após fechar o Detalhe.

A seleção não altera relevância, não implica recomendação e não modifica a ordenação sem regra explícita.

## 11. Explicação e relação comercial

Cada oportunidade deverá oferecer `Por que está aqui?` ou explicação equivalente.

A explicação poderá incluir:

- correspondência com a região ativa;
- busca explícita;
- filtros aplicados;
- categoria ou modalidade;
- data e disponibilidade;
- origem editorial, institucional ou organizacional;
- critério de ordenação;
- relação comercial identificada.

Ela não deverá simular conhecimento do Momento Atual quando o gate não estiver atendido.

Relação comercial deverá ser apresentada de forma separada, com exemplos como:

- `Sem patrocínio`;
- `Parceria identificada`;
- `Conteúdo patrocinado`, quando aplicável.

## 12. Salvamento e Detalhe

Salvar deverá permanecer disponível na Lista independentemente de localização.

O salvamento não autoriza:

- ativar localização;
- personalizar recomendações;
- registrar deslocamento;
- criar histórico territorial;
- contornar preferências de privacidade.

`Ver detalhes` deverá abrir o Detalhe de Oportunidade preservando:

- origem da navegação;
- região ativa;
- busca e filtros;
- ordenação;
- posição da Lista;
- item selecionado;
- condições conhecidas.

Ao retornar, a pessoa deverá reencontrar o mesmo contexto.

## 13. Origem para rota

Quando a localização estiver desativada, a Lista poderá apresentar `Definir origem`.

A ação deverá solicitar origem específica e não poderá iniciar rastreamento contínuo, criar histórico territorial ou presumir residência.

Endereços protegidos permanecerão limitados à área permitida ou à condição de liberação aplicável.

## 14. Retorno ao Mapa

Ao retornar ao Mapa, deverão permanecer:

- região ou área territorial;
- busca;
- filtros;
- ordenação compatível;
- quantidade de resultados;
- item selecionado;
- posição ou foco correspondente, quando possível;
- explicação da origem dos resultados.

A troca não deverá executar nova personalização, alterar consentimento ou redefinir localização.

## 15. Acessibilidade e resiliência

A Lista constitui alternativa integral para:

- leitores de tela;
- navegação por teclado ou controles assistivos;
- pessoas que preferem conteúdo textual;
- baixa conectividade;
- indisponibilidade do fornecedor cartográfico;
- falha de carregamento do mapa;
- dispositivos com desempenho limitado.

A Lista não poderá depender de mapa carregado para apresentar oportunidades já disponíveis na consulta.

Estados de carregamento, atualização, ausência de resultados e erro de fonte deverão ser textuais e recuperáveis.

## 16. Privacidade e autonomia

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

## 17. Critérios de validação posterior

A validação funcional especializada deverá verificar:

- se a pessoa entende que Lista e Mapa representam a mesma consulta;
- se a diferença entre Lista do Mapa e `Explorar` é clara;
- se região, busca e filtros permanecem intactos;
- se quantidade e ordenação são compreensíveis;
- se o item selecionado é reencontrado;
- se os cartões permitem comparação suficiente;
- se relevância e relação comercial estão separadas;
- se salvar e abrir detalhes não exigem localização;
- se retornar ao Mapa preserva o contexto;
- se a Lista funciona como alternativa integral em acessibilidade e falhas cartográficas.

## 18. Limites

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

## 19. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. validar funcionalmente a visualização em Lista;
2. criar o estado sem resultados;
3. criar referência do Mapa para computador;
4. criar o wireframe gráfico do início protegido da jornada;
5. criar a referência móvel da Página Inicial pública;
6. validar a revisão da compreensão inicial;
7. validar a transição para a primeira Tela Hoje;
8. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
