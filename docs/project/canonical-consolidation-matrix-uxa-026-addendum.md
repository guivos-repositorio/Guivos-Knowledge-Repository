---
id: GKR-CANON-MATRIX-UXA-026
title: Adendo da Matriz de Consolidação Canônica — Mapa com Localização Desativada
status: active
version: 0.1.0
owner: Guivos
last_updated: 2026-07-26
parent: GKR-CANON-MATRIX-001
depends_on:
  - UXA-024
  - UXA-025
  - UXA-026
related:
  - UXA-005
  - M7.27
normative: false
---

# Adendo da Matriz de Consolidação Canônica — Mapa com Localização Desativada

## 1. Finalidade

Este adendo consolida as decisões materializadas pelo primeiro estado alternativo gráfico do Mapa de Oportunidades.

## 2. Decisões consolidadas

| Elemento | Decisão | Situação |
|---|---|---|
| Localização do dispositivo | Manter opcional | Mapa e Lista continuam disponíveis sem permissão |
| Região manual | Exigir como alternativa real | cidade ou região permanece visível e editável |
| Contexto sem gate | Manter geral | nenhuma adequação ao Momento Atual é afirmada |
| Linguagem personalizada | Remover | resultados decorrem de busca, região e filtros explícitos |
| Marcador pessoal | Proibir | nenhuma posição real, aproximada ou presumida é exibida |
| Mapa territorial | Manter disponível | centralizado na região informada manualmente |
| Lista | Manter como alternativa integral | preserva região, busca, filtros e seleção |
| Filtros dependentes de distância pessoal | Refinar | substituir por área, cidade, bairro ou origem informada |
| Ativação de localização aproximada | Manter opcional e secundária | exige decisão consciente e revisão de privacidade |
| Continuidade sem localização | Manter | busca, filtros, detalhe e salvamento não são bloqueados |
| Rota | Exigir origem válida | origem poderá ser informada manualmente sem rastreamento contínuo |
| Endereço protegido | Manter protegido | rota não contorna condição territorial |
| Publicidade e relevância | Manter separadas | patrocínio não transforma resultado geral em recomendação |
| Artefato móvel | Criar | UXA-026 e SVG de 390 por 844 pixels |
| Validação funcional especializada | Manter pendente | ato posterior separado |
| Design, protótipo e desenvolvimento | Não iniciar | dependem de autorização própria |

## 3. Resultado

A localização deixa de ser interpretada como requisito implícito do Mapa. A pessoa pode explorar territorialmente por região manual, sem compartilhar posição e sem perder acesso às funções essenciais.

## 4. Preservações

- o Mapa permanece fora da sequência obrigatória entre Home e Tela Hoje;
- Resultados Empresariais permanecem em 18 decisões e zero Resultados canônicos;
- Engenharia de Produto permanece pausada antes de W0-01;
- a exploração sem personalização continua disponível;
- tecnologia cartográfica, design e implementação não são iniciados.
