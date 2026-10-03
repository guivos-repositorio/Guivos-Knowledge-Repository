---
id: UXA-090
title: Validação Integrada Corrente dos Handoffs de Solicitação em Coletivos
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-21
parent: UXA-000
depends_on:
  - UXA-056
  - UXA-089
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-PER-105
  - GKR-SURF-COL-003
  - GKR-TRN-105
  - GKR-TRN-106
  - GKR-TRN-107
  - GKR-TRN-109
  - GKR-TRN-112
normative: false
---

# Validação Integrada Corrente dos Handoffs de Solicitação em Coletivos

## 1. Finalidade

Validar a continuidade bilateral entre a Pessoa e a operação do responsável do Coletivo sem coerção, perda de contexto, decisão duplicada ou sobrescrita silenciosa.

Este contrato governa:

- `TRN-105` — solicitação disponível para análise;
- `TRN-106` — pedido de informação adicional;
- `TRN-107` — resposta adicional;
- `TRN-109` — recusa;
- `TRN-112` — Visão Geral/Início do responsável → gestão de solicitações.

`TRN-108` possui validação posterior própria em `UXA-092`.

## 2. Identidade lógica

Uma solicitação mantém o mesmo identificador lógico enquanto atravessa as duas perspectivas.

Mudança de tela, fila, análise protegida, pedido de informação ou resultado não cria um novo pedido.

## 3. Estado canônico

Cada perspectiva deve refletir o mesmo estado canônico aplicável.

Se uma ação concorrente tornar a representação local obsoleta, a operação deve revalidar antes de produzir efeito material.

## 4. Autoridade

```text
PESSOA
→ autoridade sobre envio, resposta e cancelamento nos limites contratados

RESPONSÁVEL DO COLETIVO
→ autoridade sobre análise e decisão no escopo legitimamente concedido
```

Nenhuma perspectiva recebe autoridade da outra apenas porque a informação é visível.

## 5. Contratos das transições

### TRN-105

Disponibiliza a solicitação para análise sem criar aprovação, prioridade ou vínculo.

### TRN-106

Pedido de informação adicional preserva o mesmo propósito e não equivale a aprovação.

### TRN-107

Resposta adicional pertence à mesma solicitação e não duplica finalidade ou pedido.

### TRN-109

Recusa produz resultado explícito e proporcional, sem pontuação negativa automática ou exposição indevida.

### TRN-112

Abrir a gestão de solicitações a partir da visão geral não altera fila, solicitação ou decisão.

## 6. Idempotência

Repetir a mesma intenção não cria:

- duas solicitações;
- duas respostas equivalentes;
- duas decisões;
- dois vínculos;
- dois eventos lógicos do mesmo efeito.

O mecanismo técnico permanece fora deste contrato.

## 7. Estado

```text
TRN-105
TRN-106
TRN-107
TRN-109
TRN-112
→ INTEGRALLY VALIDATED WITHIN DOCUMENTARY AUTHORITY

TRN-108
→ GOVERNED BY UXA-092

IMPLEMENTATION
→ SEPARATE GATE
```
