---
id: GKR-CANON-MATRIX-UXA-025
title: Adendo da Matriz de Consolidação Canônica — Validação do Mapa de Oportunidades
status: active
version: 0.1.0
owner: Guivos
last_updated: 2026-07-26
parent: GKR-CANON-MATRIX-001
depends_on:
  - UXA-004
  - UXA-024
  - UXA-025
related:
  - GKR-CANON-MATRIX-UXA-024
  - UXA-002
  - UXA-005
  - UXA-006
  - UXA-007
  - UXA-010
  - UXA-012
  - M7.26
normative: false
---

# Adendo da Matriz de Consolidação Canônica — Validação do Mapa de Oportunidades

## 1. Finalidade

Este adendo registra as decisões consolidadas pela primeira validação funcional e reformulação do Mapa de Oportunidades.

## 2. Decisões consolidadas

| Elemento | Decisão | Situação |
|---|---|---|
| Mapa de Oportunidades | Validar funcionalmente após reformulação | UXA-024 reformulada e UXA-025 ativa |
| Posição do Mapa | Manter como superfície recorrente própria | fora da sequência obrigatória entre Home e Tela Hoje |
| Contexto de atuação | Tornar explícito | utilizar `Agindo como` e identificar participante representado |
| Mapa e Lista | Unificar como uma descoberta | preservar busca, filtros, região, resultados e seleção |
| Filtros ativos | Tornar distinguíveis | marca textual, valor aplicado e remoção encontrável |
| Quantidade de resultados | Exigir | relacionar área visível e filtros vigentes |
| Movimento territorial | Tornar consciente | oferecer `Pesquisar nesta área` |
| Limpeza de filtros | Permitir sem perda silenciosa | preservar busca e região |
| Camadas territoriais | Manter configuráveis | não confundir com filtros de negócio |
| Legenda | Exigir | forma e texto complementam a diferenciação |
| Localização aproximada | Manter como estado principal | posição exata não aparece |
| Localização exata | Limitar temporalmente | finalidade, duração e encerramento necessários |
| Localização manual ou desativada | Manter como alternativa real | exploração continua disponível |
| Controle de privacidade | Tornar encontrável | disponível no bloco de localização |
| Localização de participantes | Proibir | Mapa mostra oportunidades e locais autorizados, não pessoas |
| Residências e locais sensíveis | Proteger | endereço exato depende de condição aplicável |
| Rota | Tornar contextual | somente quando endereço puder ser utilizado com segurança |
| Endereço protegido | Impedir contorno por rota | usar área aproximada ou condições de acesso |
| Cartão selecionado | Manter resumido | não substitui Detalhe de Oportunidade |
| Relação comercial | Tornar explícita | patrocínio ou comissão não alteram prioridade |
| Relevância antes do gate | Proibir personalização material | somente conteúdo geral ou busca explícita |
| Relevância após o gate | Explicar e tornar corrigível | objetivo, Próximo Passo, preferência e localização autorizada |
| Ausência de resultados | Preservar legitimamente | não preencher artificialmente |
| Mapa indisponível | Oferecer Lista equivalente | preservar busca, filtros e região conhecida |
| Estados alternativos gráficos | Manter pendentes | contrato validado; wireframes separados |
| Referência para computador | Manter pendente | ato posterior separado |
| Tecnologia, design, protótipo e desenvolvimento | Não iniciar | dependem de autorizações próprias |

## 3. Resultado

O Mapa de Oportunidades passa de wireframe estrutural pendente de avaliação para superfície **funcionalmente validada após reformulação**.

A validação não equivale a teste de usabilidade, design visual, tecnologia cartográfica ou implementação.

## 4. Preservações

- Resultados Empresariais permanecem em 18 decisões, com 9 candidatos em validação, 3 fundidos e 6 rejeitados;
- Resultados canônicos permanecem em zero;
- Engenharia de Produto permanece pausada antes de W0-01;
- a Home pública continua sem coleta de relato pessoal;
- o início protegido continua separado da Home;
- a Tela Hoje continua como entrada recorrente após o gate;
- exploração sem personalização e sem localização continua disponível.
