---
id: GKR-CANON-MATRIX-UXA-028
title: Adendo à Matriz de Consolidação Canônica — Visualização em Lista do Mapa
status: active
version: 0.2.0
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
  - UXA-029
  - M7.29
  - M7.30
normative: true
---

# Adendo à Matriz de Consolidação Canônica — Visualização em Lista do Mapa

## 1. Finalidade

Este adendo registra a consolidação canônica do primeiro wireframe alternativo da visualização em Lista dentro do Mapa de Oportunidades.

A versão 0.2.0 reconcilia o artefato com a validação funcional e a reformulação registradas em UXA-029. As decisões especializadas posteriores prevalecem em caso de conflito.

## 2. Decisão consolidada

| Dimensão | Decisão canônica |
|---|---|
| Natureza | Lista é representação integral da mesma consulta territorial do Mapa |
| Navegação | item `Mapa` permanece selecionado; alternância interna `Mapa ↔ Lista` |
| Relação com Explorar | não duplica nem substitui `Explorar`; declara sua natureza territorial |
| Contexto | `Agindo como`, região, busca, filtros, quantidade, ordenação e seleção permanecem |
| Localização desativada | Lista funciona com posição não acessada e região manual |
| Quantidade | consistente entre Mapa e Lista para a mesma consulta e atualização |
| Filtros | total consolidado e filtros aplicados são revisáveis |
| Ordenação | explícita, explicável, revisável e não apresentada como personalização sem gate |
| Cartões | comparáveis, com campos consistentes, incertezas, origem e relação comercial |
| Seleção | oportunidade selecionada permanece identificável ao trocar de modo |
| Explicabilidade | `Por que está aqui?` aparece em todos os cartões e separa critérios de comércio |
| Salvamento | disponível sem ativar localização ou personalização |
| Detalhe | preserva origem, filtros, ordenação, posição e item selecionado |
| Retorno ao Mapa | não perde contexto nem altera consentimento |
| Resiliência | Lista é alternativa integral e funciona sem mapa carregado |

## 3. Elementos materializados após reformulação

A UXA-028 demonstra:

- `Mapa de Oportunidades`;
- `LISTA TERRITORIAL DO MAPA · MESMA CONSULTA`;
- `Agindo como: Pessoa`;
- `Exploração geral · sem personalização`;
- `Localização desativada · posição não acessada`;
- região informada manualmente;
- Lista selecionada dentro da superfície Mapa;
- `Buscar nesta região`;
- `4 filtros ativos`;
- quantidade e atualização dos resultados;
- ordenação acompanhada de explicação;
- cartões comparáveis;
- dados ausentes declarados;
- oportunidade selecionada preservada;
- explicação de origem em todos os cartões;
- relação comercial separada;
- salvamento;
- definição de origem;
- abertura do Detalhe;
- retorno ao Mapa sem perda de contexto;
- `Lista integral · funciona sem carregar o mapa`.

## 4. Resultado da validação

A UXA-029 considera a visualização em Lista **funcionalmente válida após reformulação**.

O fechamento funcional não representa teste com usuários, conformidade técnica de acessibilidade, design ou implementação.

## 5. Proteções preservadas

- Lista não cria personalização sem gate;
- contexto de atuação não muda silenciosamente;
- ordenação não oculta patrocínio;
- região manual não equivale a posição atual;
- dado ausente não é completado por inferência;
- salvamento não autoriza rastreamento;
- definir origem não autoriza histórico territorial;
- troca de modo não altera permissões;
- endereço protegido não pode ser contornado.

## 6. Limites

Este adendo não define algoritmo de ordenação, tecnologia cartográfica, geocodificação, rotas, design visual, protótipo, acessibilidade técnica, testes com usuários ou desenvolvimento.

## 7. Marcos

- **M7.29 — Visualização em Lista do Mapa Criada**: origem histórica do wireframe;
- **M7.30 — Visualização em Lista do Mapa Funcionalmente Validada e Reformulada**: fechamento funcional governado pela UXA-029.
