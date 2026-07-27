---
id: GKR-CANON-MATRIX-UXA-027
title: Adendo à Matriz de Consolidação Canônica — Validação do Estado do Mapa sem Localização
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
related:
  - M7.28
normative: true
---

# Adendo à Matriz de Consolidação Canônica — Validação do Estado do Mapa sem Localização

## 1. Finalidade

Este adendo registra a consolidação canônica da validação funcional especializada do estado do Mapa de Oportunidades com localização desativada.

## 2. Decisão consolidada

| Dimensão | Decisão canônica |
|---|---|
| Estado | funcionalmente válido após reformulação |
| Superfície | condição operacional do Mapa recorrente, não nova etapa da jornada |
| Localização | opcional; posição não acessada deve ser declarada quando verdadeiro |
| Região manual | visível, editável e explicitamente distinta da posição pessoal |
| Personalização | linguagem geral sem gate; nenhuma adequação ao Momento Atual |
| Mapa e Lista | mesma descoberta, com preservação de região, busca, filtros e seleção |
| Marcador pessoal | ausente; nenhuma posição presumida ou residência inferida |
| Distância | omitida sem origem válida |
| Salvamento | disponível sem ativar localização ou personalização |
| Rota | exige origem específica; não inicia automaticamente |
| Ativação posterior | localização aproximada permanece opcional, explicada e revogável |
| Endereço protegido | não pode ser contornado por rota ou origem manual |

## 3. Reformulações incorporadas

A UXA-026 passa a demonstrar:

- `Posição não acessada`;
- `Região informada manualmente · não é sua posição`;
- mapa sem posição ou marcador pessoal;
- `Salvar`;
- `Definir origem`;
- `Ver detalhes`;
- ativação de localização aproximada explicitamente opcional.

## 4. Proteções preservadas

- recusa de localização não bloqueia funções essenciais;
- região manual não é tratada como residência ou posição atual;
- salvamento não autoriza rastreamento;
- origem para rota não autoriza histórico territorial;
- ausência de gate impede linguagem personalizada;
- publicidade e proximidade não definem relevância;
- residências e locais sensíveis permanecem protegidos.

## 5. Limites

Este adendo não define tecnologia cartográfica, geocodificação, coordenadas, rotas, design visual, protótipo, testes com usuários ou desenvolvimento.

## 6. Marco

A integração deste incremento estabelece o marco **M7.28 — Estado do Mapa sem Localização Funcionalmente Validado e Reformulado**.
