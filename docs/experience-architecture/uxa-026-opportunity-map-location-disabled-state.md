---
id: UXA-026
title: Wireframe Alternativo do Mapa de Oportunidades — Localização Desativada
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-26
parent: UXA-024
depends_on:
  - UXA-004
  - UXA-005
  - UXA-024
  - UXA-025
related:
  - UXA-002
  - UXA-010
  - UXA-012
normative: false
---

# Wireframe Alternativo do Mapa de Oportunidades — Localização Desativada

## 1. Finalidade

Este documento materializa o primeiro estado alternativo do Mapa de Oportunidades: uso territorial com a localização do dispositivo desativada.

O estado demonstra que a pessoa pode explorar oportunidades por cidade ou região informada manualmente, preservar busca e filtros, alternar entre Mapa e Lista e continuar sem conceder acesso à localização.

O wireframe não representa mapa real, design visual, tecnologia cartográfica, coordenadas, dados de produção ou implementação.

## 2. Posição na experiência

O estado permanece dentro da superfície recorrente do Mapa:

```text
Hoje | Jornada | Explorar | Mapa | Eu
```

Ele poderá ocorrer quando:

- a pessoa nunca concedeu localização;
- a permissão foi recusada ou retirada;
- o dispositivo não oferece localização;
- a pessoa prefere informar cidade ou região manualmente;
- o gate de personalização ainda não foi atendido;
- a exploração geral foi escolhida conscientemente.

A localização desativada não bloqueia o Mapa, a Lista, a busca ou o Detalhe de Oportunidade.

## 3. Artefato visual

![Wireframe alternativo do Mapa de Oportunidades com localização desativada](../assets/wireframes/uxa-026-opportunity-map-location-disabled-mobile.svg)

Arquivo vetorial:

`docs/assets/wireframes/uxa-026-opportunity-map-location-disabled-mobile.svg`

Dimensão de referência:

- canal: aplicativo móvel;
- largura: 390 pixels;
- altura: 844 pixels;
- estado: localização do dispositivo desativada, região manual selecionada e exploração geral sem personalização.

## 4. Hierarquia funcional

```text
nome da superfície e contexto de exploração
→ aviso de localização desativada
→ escolha manual de cidade ou região
→ pesquisa
→ Mapa ou Lista
→ filtros e resultados da região
→ área territorial sem marcador pessoal
→ legenda e controles
→ oportunidade geral selecionada
→ detalhe, salvamento e definição manual de origem
→ navegação recorrente
```

## 5. Contexto e linguagem

Quando o gate de personalização não estiver atendido, a superfície deverá declarar:

> **Exploração geral · sem personalização**

A interface não deverá utilizar expressões como:

- `para o seu momento`;
- `relacionada à sua transição`;
- `recomendada para você`;
- `perto de você`;
- qualquer afirmação de adequação pessoal.

A origem dos resultados deverá ser explicada por busca, região, categoria, período ou filtro explícito.

## 6. Localização desativada

O aviso deverá informar:

> **Localização desativada**

> Você pode escolher uma cidade ou região e continuar sem compartilhar sua posição.

A pessoa deverá poder:

- escolher ou alterar cidade ou região;
- continuar sem localização;
- ativar localização aproximada posteriormente;
- revisar privacidade antes de ativar;
- retirar uma permissão futura;
- utilizar origem manual para rota quando aplicável.

Ativar localização aproximada é uma ação opcional e secundária. A interface não deverá induzir consentimento por bloqueio, culpa, urgência ou perda artificial de funcionalidade.

## 7. Região manual

A região selecionada manualmente deverá permanecer visível e editável.

A alteração de região não poderá apagar silenciosamente:

- busca;
- filtros compatíveis;
- modo Mapa ou Lista;
- item salvo;
- preferências não territoriais.

Filtros estritamente dependentes de distância pessoal deverão ser desativados, reinterpretados ou substituídos por filtros de área, cidade, bairro ou raio a partir de um ponto informado.

## 8. Mapa sem marcador pessoal

O mapa não deverá mostrar:

- ponto de localização da pessoa;
- círculo de precisão;
- posição aproximada presumida;
- histórico de deslocamento;
- residência inferida;
- indicação de que a pessoa está em determinada área.

A área territorial poderá ser centralizada na região informada manualmente e exibir somente oportunidades, Organizações, Coletivos, eventos, atividades, pontos de apoio e locais autorizados.

## 9. Relação com a Lista

Mapa e Lista continuam representando a mesma descoberta.

A alternância deverá preservar:

- região manual;
- busca;
- filtros;
- quantidade de resultados;
- item selecionado;
- explicação da origem dos resultados.

A Lista constitui alternativa integral quando o mapa não estiver disponível, não carregar ou não for adequado à acessibilidade da pessoa.

## 10. Resultados e filtros

A superfície deverá informar que os resultados correspondem à região escolhida e aos filtros aplicados.

Exemplo:

> 8 resultados na região selecionada

A distância pessoal não deverá ser exibida quando não houver origem válida. O cartão poderá apresentar:

- cidade, bairro ou área;
- modalidade presencial, online ou híbrida;
- data, horário ou prazo;
- preço ou gratuidade;
- disponibilidade;
- acessibilidade;
- responsável ou fonte;
- relação comercial.

## 11. Oportunidade selecionada

O cartão ilustrado deverá utilizar linguagem geral, como:

> Resultado da busca nesta região

A ação `Por que está aqui?` poderá explicar:

- correspondência com a região manual;
- filtros aplicados;
- busca explícita;
- categoria selecionada;
- origem editorial ou institucional;
- relação comercial identificada.

Ela não deverá simular compreensão do Momento Atual.

## 12. Rota sem localização

Sem origem disponível, a interface não deverá executar rota automaticamente.

As alternativas serão:

- `Definir origem para rota`;
- `Usar endereço informado`;
- `Ativar localização aproximada`;
- `Copiar endereço`, quando permitido;
- `Ver área aproximada`, quando o endereço estiver protegido.

A escolha de origem não autoriza rastreamento contínuo nem retenção posterior.

## 13. Privacidade e autonomia

O estado preserva:

- exploração sem localização;
- exploração sem personalização;
- cidade ou região manual como alternativa real;
- ausência de marcador pessoal;
- ativação posterior consciente;
- continuidade pela Lista;
- proteção de endereços sensíveis;
- separação entre proximidade, relevância e publicidade.

## 14. Critérios de validação posterior

O wireframe deverá permitir verificar:

- se a pessoa entende que o Mapa continua disponível sem localização;
- se a região manual é encontrável e editável;
- se a ausência de marcador pessoal é clara;
- se ativar localização é opcional;
- se a linguagem deixa de afirmar relevância pessoal sem gate;
- se busca e filtros permanecem após alteração territorial;
- se Mapa e Lista continuam sincronizados;
- se a rota oferece origem manual sem contornar privacidade;
- se resultados gerais são distinguíveis de recomendações pessoais.

## 15. Limites

Este incremento não:

- valida o estado com usuários reais;
- cria localização técnica ou geocodificação;
- define fornecedor de mapas;
- cria rotas;
- define cidades ou oportunidades reais;
- conclui acessibilidade;
- cria referência para computador;
- cria protótipo navegável;
- inicia design visual ou Engenharia de Produto.

## 16. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. validar funcionalmente o estado de localização desativada;
2. criar o estado alternativo em Lista;
3. criar o estado sem resultados;
4. criar referência do Mapa para computador;
5. criar o wireframe gráfico do início protegido;
6. criar a referência móvel da Home;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
