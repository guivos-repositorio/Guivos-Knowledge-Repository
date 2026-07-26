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
  - UXA-002
  - UXA-003-A1
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

Este adendo registra as decisões estruturais consolidadas pela primeira validação funcional e reformulação do Mapa de Oportunidades.

## 2. Decisões consolidadas

| Elemento | Decisão | Situação |
|---|---|---|
| Posição do Mapa | Manter como superfície recorrente própria | não entra entre Home e Tela Hoje |
| Navegação principal | Manter | Hoje, Jornada, Explorar, Mapa e Eu |
| Wireframe móvel | Validar após reformulação | UXA-024 0.2.0 governado por UXA-025 |
| Contexto de atuação | Tornar explícito | usar `Agindo como` e identificar participante representado |
| Mapa e Lista | Unificar como uma descoberta | busca, filtros, região e seleção permanecem compartilhados |
| Lista equivalente | Exigir | alternativa não espacial com conteúdo e controles compatíveis |
| Pesquisa territorial | Tornar consciente | apresentar `Pesquisar nesta região` após movimentação |
| Atualização automática | Limitar | não substituir resultados silenciosamente quando houver consumo ou mudança material |
| Filtros | Manter progressivos | ativos, removíveis e sem preenchimento artificial |
| Camadas | Manter ajustáveis | distinção não depende somente de cor |
| Localização aproximada | Manter como estado principal | posição exata não aparece |
| Localização e privacidade | Tornar encontráveis | acesso explícito `Ajustar localização e privacidade` |
| Localização exata | Permitir somente temporariamente | finalidade, duração, indicador e encerramento obrigatórios |
| Localização manual | Manter disponível | cidade ou região selecionada |
| Localização desativada | Manter disponível | exploração continua com alternativas manuais |
| Localização de participantes | Proibir exibição | Mapa mostra possibilidades e locais autorizados, não pessoas |
| Residências e locais sensíveis | Proteger | endereço exato depende de condição e autorização aplicáveis |
| Cartão selecionado | Manter resumido antes do detalhe | preço, origem, data, acessibilidade e relação comercial visíveis |
| Explicação de relevância | Padronizar | `Por que estou vendo isto?` |
| Conteúdo antes do gate | Limitar | geral, institucional, editorial, busca ou filtros explícitos |
| Proximidade | Não tratar como relevância suficiente | distância não substitui contexto e decisão |
| Patrocínio e comissão | Separar de relevância | relação comercial permanece identificada |
| Rota | Tornar contextual | usar `Ver rota` somente quando deslocamento for material |
| Serviço externo de rota | Exigir transparência | executor, destino, localização e dados antes da continuidade |
| Estados alternativos | Governar sem criar automaticamente | Lista, ausência, localização desativada, erro e baixa conectividade |
| Teste de usabilidade | Manter pendente | validação funcional não equivale a teste com participantes |
| Referência para computador | Manter pendente | ato posterior separado |
| Tecnologia cartográfica | Não definir | fornecedor, geocodificação e coordenadas permanecem fora |
| Protótipo, design e desenvolvimento | Não iniciar | dependem de autorizações próprias |

## 3. Resultado

O Mapa de Oportunidades passa de wireframe estrutural não validado para wireframe móvel funcionalmente validado e reformulado.

A validação confirma responsabilidade, hierarquia, autonomia, privacidade e continuidade. Ela não confirma usabilidade, desempenho, tecnologia, responsividade ou implementação.

## 4. Preservações

- Resultados Empresariais permanecem em 18 decisões, com 9 candidatos em validação, 3 fundidos e 6 rejeitados;
- Resultados canônicos permanecem em zero;
- Engenharia de Produto permanece pausada antes de W0-01;
- a Home pública continua sem coleta de relato pessoal;
- o início protegido continua separado da Home;
- a Tela Hoje continua como entrada recorrente após o gate;
- a exploração sem personalização continua disponível;
- estados alternativos e referência para computador continuam pendentes.
