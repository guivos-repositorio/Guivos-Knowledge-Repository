---
id: GKR-CHANGELOG-1.52.0
title: Histórico de Alterações 1.52.0 — Validação da Visualização em Lista do Mapa
status: active
version: 1.52.0
owner: Guivos
last_updated: 2026-07-27
depends_on:
  - UXA-029
related:
  - UXA-028
  - GKR-CANON-MATRIX-UXA-029
  - M7.30
normative: false
---

# Histórico de Alterações 1.52.0 — Validação da Visualização em Lista do Mapa

## 1. Resumo

Este incremento valida funcionalmente a visualização em Lista do Mapa de Oportunidades e reformula a UXA-028 antes de qualquer avanço para novos estados, design, protótipo ou desenvolvimento.

## 2. Resultado

A Lista é considerada **funcionalmente válida após reformulação**.

## 3. Riscos corrigidos

- ausência do contexto `Agindo como`;
- diferença visual insuficiente entre Lista do Mapa e `Explorar`;
- total de filtros ativos ambíguo;
- ordenação sem explicação direta;
- inconsistência de campos, incertezas e relações comerciais nos cartões secundários.

## 4. Reformulação aplicada

A referência agora demonstra:

- `Mapa de Oportunidades`;
- `LISTA TERRITORIAL DO MAPA · MESMA CONSULTA`;
- `Agindo como: Pessoa`;
- localização desativada e posição não acessada;
- região manual distinta da posição pessoal;
- `Buscar nesta região`;
- `4 filtros ativos`;
- quantidade e atualização dos resultados;
- ordenação explicável;
- cartões com campos consistentes;
- dados ausentes explicitamente informados;
- seleção preservada do Mapa;
- explicação funcional em todos os cartões;
- relação comercial separada;
- Lista integral sem mapa carregado.

## 5. Artefatos criados ou atualizados

- `UXA-029 — Validação Funcional Especializada e Reformulação da Visualização em Lista do Mapa`;
- UXA-028 atualizada para versão 0.2.0;
- `docs/assets/wireframes/uxa-028-opportunity-map-list-mobile.svg` reformulado;
- `GKR-CANON-MATRIX-UXA-029`;
- este histórico 1.52.0;
- estado global, roadmap, painel, marcos, programa de wireframes, menu, README e páginas iniciais atualizados.

## 6. Marco

O incremento propõe **M7.30 — Visualização em Lista do Mapa Funcionalmente Validada e Reformulada**.

## 7. Limites preservados

Não foram iniciados estado sem resultados, referência do Mapa para computador, design visual, protótipo navegável, teste de usabilidade, acessibilidade técnica, algoritmo de ordenação, tecnologia cartográfica ou Engenharia de Produto.
