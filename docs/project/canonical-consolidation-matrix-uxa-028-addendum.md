---
id: GKR-CANON-MATRIX-UXA-028
title: Adendo à Matriz de Consolidação Canônica — Visualização em Lista do Mapa
status: active
version: 0.1.0
owner: Guivos
last_updated: 2026-07-27
depends_on:
  - GKR-STATE-001
  - UXA-024
  - UXA-025
  - UXA-026
  - UXA-027
  - UXA-028
related:
  - M7.29
normative: true
---

# Adendo à Matriz de Consolidação Canônica — Visualização em Lista do Mapa

## 1. Finalidade

Este adendo registra a consolidação canônica do primeiro wireframe alternativo da visualização em Lista dentro do Mapa de Oportunidades.

## 2. Decisão consolidada

| Dimensão | Decisão canônica |
|---|---|
| Natureza | Lista é representação integral da mesma consulta territorial do Mapa |
| Navegação | item `Mapa` permanece selecionado; alternância interna `Mapa ↔ Lista` |
| Relação com Explorar | não duplica nem substitui `Explorar`; preserva consulta territorial ativa |
| Contexto | região, busca, filtros, quantidade, ordenação e seleção devem permanecer |
| Localização desativada | Lista funciona com posição não acessada e região manual |
| Quantidade | consistente entre Mapa e Lista para a mesma consulta e atualização |
| Ordenação | explícita, revisável e não apresentada como personalização sem gate |
| Cartões | comparáveis, com condições, origem e relação comercial |
| Seleção | oportunidade selecionada permanece identificável ao trocar de modo |
| Explicabilidade | `Por que está aqui?` separa critérios funcionais de relação comercial |
| Salvamento | disponível sem ativar localização ou personalização |
| Detalhe | preserva origem, filtros, ordenação, posição e item selecionado |
| Retorno ao Mapa | não perde contexto nem altera consentimento |
| Resiliência | Lista é alternativa integral para acessibilidade, baixa conectividade e falha cartográfica |

## 3. Elementos materializados

A UXA-028 demonstra:

- `Exploração geral · sem personalização`;
- `Localização desativada · posição não acessada`;
- região informada manualmente;
- Lista selecionada dentro da superfície Mapa;
- pesquisa e filtros preservados;
- quantidade de resultados;
- ordenação explícita;
- cartões comparáveis;
- oportunidade selecionada;
- explicação de origem;
- relação comercial;
- salvamento;
- definição de origem;
- abertura do Detalhe;
- retorno ao Mapa sem perda de contexto.

## 4. Proteções preservadas

- Lista não cria personalização sem gate;
- ordenação não pode ocultar patrocínio;
- região manual não equivale a posição atual;
- salvamento não autoriza rastreamento;
- definir origem não autoriza histórico territorial;
- troca de modo não altera permissões;
- endereço protegido não pode ser contornado;
- dados ausentes não são completados por inferência.

## 5. Limites

Este adendo não valida a Lista com usuários reais, não define algoritmo de ordenação, tecnologia cartográfica, geocodificação, rotas, design visual, protótipo, acessibilidade técnica ou desenvolvimento.

## 6. Marco

A integração deste incremento estabelece o marco **M7.29 — Visualização em Lista do Mapa Criada**.
