---
id: GKR-CANON-MATRIX-UXA-024
title: Adendo da Matriz de Consolidação Canônica — Wireframe do Mapa de Oportunidades
status: active
version: 0.2.0
owner: Guivos
last_updated: 2026-07-26
parent: GKR-CANON-MATRIX-001
depends_on:
  - UXA-004
  - UXA-024
related:
  - GKR-CANON-MATRIX-UXA-025
  - UXA-002
  - UXA-003-A1
  - UXA-005
  - UXA-006
  - UXA-007
  - UXA-010
  - UXA-012
  - UXA-025
  - M7.25
  - M7.26
normative: false
---

# Adendo da Matriz de Consolidação Canônica — Wireframe do Mapa de Oportunidades

## 1. Finalidade

Este adendo registra as decisões estruturais consolidadas pela criação do primeiro wireframe gráfico do Mapa de Oportunidades.

A validação funcional posterior está registrada em UXA-025 e no adendo GKR-CANON-MATRIX-UXA-025. As decisões abaixo foram reconciliadas com essa evolução.

## 2. Decisões consolidadas

| Elemento | Decisão | Situação |
|---|---|---|
| Posição do Mapa | Manter como superfície recorrente própria | não entra entre Home e Tela Hoje |
| Navegação principal | Manter | Hoje, Jornada, Explorar, Mapa e Eu |
| Acesso pela Home | Permitir secundariamente | exploração geral por cidade ou região, sem personalização antes do gate |
| Acesso pela Tela Hoje | Limitar a recorte contextual | bloco `Perto de mim` com ação `Abrir no mapa` |
| Relação com Explorar | Sincronizar | lista, filtros, região e seleção representam a mesma descoberta |
| Wireframe móvel do Mapa | Manter reformulado | UXA-024 0.2.0 e arquivo vetorial de 390 por 844 pixels |
| Geografia do wireframe | Manter esquemática | não representa cidade, endereço ou coordenada real |
| Pesquisa | Incluir | oportunidade, Organização ou região |
| Filtros | Tornar ativos e removíveis | período, distância, preço, gratuidade e outras dimensões |
| Resultados da área | Tornar visíveis | quantidade relacionada à região e aos filtros |
| Movimento territorial | Tornar consciente | ação `Pesquisar nesta área` |
| Camadas | Permitir | oportunidades, Organizações, Coletivos, eventos, atividades, pontos de apoio e locais salvos |
| Legenda | Exigir | formas e texto distinguem tipos sem dependência exclusiva de cor |
| Cartão selecionado | Resumir antes do detalhe | preço, data, distância, vagas, acessibilidade, origem, relevância e relação comercial |
| Detalhe de Oportunidade | Manter especializado | cartão do mapa não substitui condições completas |
| Localização aproximada | Usar como estado principal | posição exata não aparece no wireframe |
| Localização exata | Permitir somente temporariamente | finalidade, duração e controle necessários |
| Localização manual | Manter disponível | cidade ou região selecionada |
| Localização desativada | Manter disponível | exploração territorial continua com alternativas manuais |
| Localização de participantes | Proibir exibição | Mapa mostra oportunidades e locais autorizados, não pessoas |
| Residências e locais sensíveis | Proteger | endereço exato depende de condição aplicável |
| Rastreamento contínuo | Não exigir | localização não é condição universal de uso |
| Rota | Tornar contextual | não revela endereço protegido nem local sensível |
| Proximidade | Não tratar como relevância suficiente | distância não substitui contexto, elegibilidade ou decisão |
| Patrocínio | Separar de relevância | relação comercial permanece identificada |
| Conteúdo antes do gate | Limitar | geral, institucional, editorial ou resultante de busca explícita |
| Validação funcional do wireframe | Concluir após reformulação | UXA-025; marco M7.26 |
| Estados alternativos | Governar funcionalmente e manter wireframes pendentes | lista, ausência, erro, localização desativada e baixa conectividade |
| Referência para computador | Manter pendente | ato posterior separado |
| Tecnologia cartográfica | Não definir | fornecedor, geocodificação e rotas permanecem fora do incremento |
| Protótipo, design, testes e desenvolvimento | Não iniciar | dependem de autorizações próprias |

## 3. Resultado

O Mapa de Oportunidades possui contrato funcional, wireframe móvel reformulado e validação funcional registrada.

A validação não equivale a design visual, protótipo navegável, teste de usabilidade ou implementação.

## 4. Preservações

- Resultados Empresariais permanecem em 18 decisões, com 9 candidatos em validação, 3 fundidos e 6 rejeitados;
- Resultados canônicos permanecem em zero;
- Engenharia de Produto permanece pausada antes de W0-01;
- a Home pública continua sem coleta de relato pessoal;
- o início protegido continua separado da Home;
- a Tela Hoje continua como entrada recorrente após o gate;
- a exploração sem personalização continua disponível.
