---
id: GKR-CANON-MATRIX-UXA-029
title: Adendo à Matriz de Consolidação Canônica — Validação da Visualização em Lista do Mapa
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
  - UXA-029
related:
  - M7.30
normative: true
---

# Adendo à Matriz de Consolidação Canônica — Validação da Visualização em Lista do Mapa

## 1. Finalidade

Este adendo registra a consolidação canônica da validação funcional especializada da visualização em Lista do Mapa de Oportunidades.

## 2. Decisão consolidada

| Dimensão | Decisão canônica |
|---|---|
| Estado | funcionalmente válido após reformulação |
| Natureza | Lista é representação textual integral da mesma consulta territorial do Mapa |
| Navegação | item `Mapa` permanece selecionado; alternância interna `Mapa ↔ Lista` |
| Relação com Explorar | superfície declara `Lista territorial do Mapa · mesma consulta`; não duplica `Explorar` |
| Contexto | `Agindo como` permanece visível e não muda ao alternar modos |
| Localização | opcional; Lista funciona com posição não acessada e região manual |
| Pesquisa | busca territorial permanece vinculada à região ativa |
| Filtros | total consolidado e filtros aplicados devem ser revisáveis |
| Quantidade | consistente entre Mapa e Lista para a mesma consulta e atualização |
| Ordenação | explícita, explicável, revisável e separada de patrocínio |
| Cartões | estrutura mínima consistente; dados ausentes declarados sem inferência |
| Seleção | item selecionado permanece textual e estruturalmente identificável |
| Explicabilidade | todos os cartões oferecem justificativa funcional |
| Relação comercial | apresentada separadamente como sem patrocínio, parceria ou conteúdo patrocinado |
| Salvamento | disponível sem ativar localização, rastreamento ou personalização |
| Detalhe | preserva região, busca, filtros, ordenação, posição e seleção |
| Retorno ao Mapa | não perde contexto, não altera consentimento e não redefine localização |
| Resiliência | Lista funciona sem mapa carregado e constitui alternativa integral |

## 3. Riscos corrigidos

A validação corrigiu:

1. ausência de `Agindo como` no wireframe;
2. diferença visual insuficiente entre Lista do Mapa e `Explorar`;
3. total de filtros ativos ambíguo;
4. ordenação sem ação explicativa;
5. inconsistência de campos, incertezas e relações comerciais entre cartões.

## 4. Reformulações incorporadas

A UXA-028 passa a demonstrar:

- `Mapa de Oportunidades`;
- `LISTA TERRITORIAL DO MAPA · MESMA CONSULTA`;
- `Agindo como: Pessoa`;
- `Localização desativada · posição não acessada`;
- região manual distinta da posição pessoal;
- `Buscar nesta região`;
- `4 filtros ativos`;
- quantidade e atualização dos resultados;
- ordenação acompanhada de `Entender`;
- cartões comparáveis com acessibilidade confirmada, parcial ou não informada;
- `Selecionada · preservada do Mapa`;
- `Por que está aqui?` em todos os cartões;
- relação comercial separada;
- salvamento, origem e Detalhe;
- `Lista integral · funciona sem carregar o mapa`.

## 5. Proteções preservadas

- Lista não cria personalização sem gate;
- contexto de atuação não muda silenciosamente;
- região manual não equivale a posição atual;
- ordenação não oculta patrocínio;
- dado ausente não é completado por inferência;
- salvamento não autoriza rastreamento;
- definir origem não autoriza histórico territorial;
- troca de modo não altera permissões;
- endereços protegidos não são contornados;
- acessibilidade funcional não é confundida com conformidade técnica concluída.

## 6. Limites

Este adendo não define algoritmo de busca ou ordenação, tecnologia cartográfica, geocodificação, rotas, design visual, protótipo, acessibilidade técnica, teste com usuários ou desenvolvimento.

## 7. Marco

A integração deste incremento estabelece o marco **M7.30 — Visualização em Lista do Mapa Funcionalmente Validada e Reformulada**.
