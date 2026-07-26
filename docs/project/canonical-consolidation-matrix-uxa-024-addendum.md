---
id: GKR-CANON-MATRIX-UXA-024
title: Adendo da Matriz de Consolidação Canônica — Wireframe do Mapa de Oportunidades
status: active
version: 0.1.0
owner: Guivos
last_updated: 2026-07-26
parent: GKR-CANON-MATRIX-001
depends_on:
  - UXA-004
  - UXA-024
related:
  - UXA-002
  - UXA-003-A1
  - UXA-005
  - UXA-006
  - UXA-007
  - UXA-010
  - UXA-012
  - M7.25
normative: false
---

# Adendo da Matriz de Consolidação Canônica — Wireframe do Mapa de Oportunidades

## 1. Finalidade

Este adendo registra as decisões estruturais consolidadas pela criação do primeiro wireframe gráfico do Mapa de Oportunidades.

## 2. Decisões consolidadas

| Elemento | Decisão | Situação |
|---|---|---|
| Posição do Mapa | Manter como superfície recorrente própria | não entra entre Home e Tela Hoje |
| Navegação principal | Manter | Hoje, Jornada, Explorar, Mapa e Eu |
| Acesso pela Home | Permitir secundariamente | exploração geral por cidade ou região, sem personalização antes do gate |
| Acesso pela Tela Hoje | Limitar a recorte contextual | bloco `Perto de mim` com ação `Abrir no mapa` |
| Relação com Explorar | Sincronizar | lista, filtros, região e seleção representam a mesma descoberta |
| Wireframe móvel do Mapa | Criar | UXA-024 e arquivo vetorial de 390 por 844 pixels |
| Geografia do wireframe | Manter esquemática | não representa cidade, endereço ou coordenada real |
| Pesquisa | Incluir | oportunidade, Organização ou região |
| Filtros | Incluir progressivamente | período, distância, preço, gratuidade, modalidade, disponibilidade, acessibilidade e origem |
| Camadas | Permitir | oportunidades, Organizações, Coletivos, eventos, atividades, pontos de apoio e locais salvos |
| Cartão selecionado | Resumir antes do detalhe | preço, data, distância, vagas, acessibilidade, origem, relevância e relação comercial |
| Detalhe de Oportunidade | Manter especializado | cartão do mapa não substitui condições completas |
| Localização aproximada | Usar como estado principal | posição exata não aparece no wireframe |
| Localização exata | Permitir somente temporariamente | finalidade, duração e controle necessários |
| Localização manual | Manter disponível | cidade ou região selecionada |
| Localização desativada | Manter disponível | exploração territorial continua com alternativas manuais |
| Localização de participantes | Proibir exibição | Mapa mostra oportunidades e locais autorizados, não pessoas |
| Residências e locais sensíveis | Proteger | endereço exato depende de autorização aplicável |
| Rastreamento contínuo | Não exigir | localização não é condição universal de uso |
| Proximidade | Não tratar como relevância suficiente | distância não substitui contexto, elegibilidade ou decisão |
| Patrocínio | Separar de relevância | relação comercial permanece identificada |
| Conteúdo antes do gate | Limitar | geral, institucional, editorial ou resultante de busca explícita |
| Validação funcional do wireframe | Manter pendente | ato posterior separado |
| Estados alternativos | Manter pendentes | lista, ausência, erro, localização desativada e baixa conectividade |
| Referência para computador | Manter pendente | ato posterior separado |
| Tecnologia cartográfica | Não definir | fornecedor, geocodificação e rotas permanecem fora do incremento |
| Protótipo, design, testes e desenvolvimento | Não iniciar | dependem de autorizações próprias |

## 3. Resultado

O Mapa de Oportunidades passa de contrato funcional sem materialização própria para contrato funcional acompanhado de um wireframe móvel de baixa fidelidade.

A criação do wireframe não equivale a validação funcional, design visual, protótipo navegável ou implementação.

## 4. Preservações

- Resultados Empresariais permanecem em 18 decisões, com 9 candidatos em validação, 3 fundidos e 6 rejeitados;
- Resultados canônicos permanecem em zero;
- Engenharia de Produto permanece pausada antes de W0-01;
- a Home pública continua sem coleta de relato pessoal;
- o início protegido continua separado da Home;
- a Tela Hoje continua como entrada recorrente após o gate;
- a exploração sem personalização continua disponível.
