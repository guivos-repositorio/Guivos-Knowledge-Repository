---
id: PAS-001-CC-UIC-001-OVERLAY-0.2.0
title: Estado Efetivo da UIC-01 — Modelo de Domínio Proposto
status: active
version: 0.2.0
owner: Guivos
last_updated: 2026-07-19
parent: PAS-001-CC-UIC-001
normative: true
supersedes_partial:
  - PAS-001-CC-UIC-001@0.1.0
related:
  - PAS-001-CC-UIC-DOMAIN-001
  - PAS-001-ENGINEERING-HANDOFF-001
  - PAS-001-CC-LIFECYCLE-001
  - PAS-001-CC-EVENT-INTEGRATION-001
  - PAS-001-CC-CONTRACT-001
---

# PAS-001-CC-UIC-001 — Estado Efetivo 0.2.0

> **Estado efetivo:** `Draft 0.2.0 — Domain model proposed`.
>
> **Progresso de referência:** `40%`.

Este overlay preserva integralmente a UIC-base `0.1.0` e prevalece somente sobre o estado técnico, a classificação dos agregados, as identidades, as invariantes confirmadas, os gaps resolvidos, o marco vigente e o ponto de retomada.

## 1. Base preservada

Permanece inalterada:

- [`PAS-001-CC-UIC-001 0.1.0`](pas-001-captura-de-contexto-engineering-unit.md);
- blob protegido: `48988df33cc8047664c41248efd25a0d9ba1dac9`;
- autoridade funcional: `PAS-001-CC-CONTRACT-001 1.0.0`;
- ciclo de vida: `PAS-001-CC-LIFECYCLE-001 1.0.0`;
- eventos e integrações: `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0`.

## 2. Autoridade especializada incorporada

O estado efetivo incorpora:

- [`PAS-001-CC-UIC-DOMAIN-001 — Modelo de Domínio da Captura de Contexto`](pas-001-captura-de-contexto-domain-model.md);
- versão: `Draft 0.1.0`;
- estado: `Domain model proposed`.

## 3. Decisões efetivamente concluídas

| Decisão | Resultado |
|---|---|
| Raiz principal | `CaptureRecord` confirmado como Aggregate Root |
| Sessão | `CaptureSession` confirmada como entidade interna com identidade própria |
| Cardinalidade | Um registro contém uma ou mais sessões relacionadas |
| Entrada original | `CaptureInput` possui identidade permanente independente da mídia |
| Conteúdo multimodal | Referenciado fora do agregado por referência protegida |
| Transcrição | Entidade derivada versionada |
| Interpretação | Entidade derivada, incerta e contestável |
| Síntese | Entidade versionada apresentada ao participante |
| Confirmação | Evidência delimitada sobre versão e escopo |
| Autorização | Agregado auxiliar por finalidade e temporalidade |
| Revogação | Processo explícito de propagação |
| Consistência | Limites imediatos e eventuais definidos |
| Concorrência | Controle otimista e conflitos materiais definidos |
| Reconstrução | Modelo inicial proposto |

## 4. Gaps resolvidos

| Gap | Estado | Evidência |
|---|---|---|
| `UIC01-GAP-001` — limite entre registro e sessão | `Resolved` | Seções 7104–7106 e 7112–7114 do modelo de domínio |
| `UIC01-GAP-002` — identidade da entrada original | `Resolved` | Seções 7107–7108, 7111 e 7117 do modelo de domínio |

Os demais gaps permanecem abertos.

## 5. Estado efetivo por dimensão

| Dimensão | Estado |
|---|---|
| Fontes normativas | Mapeadas |
| Responsabilidade técnica | Definida |
| Decisões proibidas | Definidas |
| Modelo de domínio | Proposto |
| Raiz do agregado | Confirmada |
| Entidades e objetos de valor | Classificados |
| Identidades | Definidas |
| Invariantes estruturais | Confirmadas |
| Invariantes por comando | Mapeadas |
| Consistência | Definida |
| Concorrência | Definida |
| Idempotência | Definida |
| Reconstrução | Proposta |
| Ciclo técnico detalhado | Próximo incremento |
| Contratos técnicos completos | Pendente |
| Segurança e privacidade finais | Pendente |
| Estado técnico | `Domain model proposed` |

## 6. Marco vigente

> `M5.13 — Capture Context Domain Model Proposed`

O marco reconhece o fechamento do modelo de domínio inicial. Ele não representa prontidão para implementação.

## 7. Próximo incremento

> **`Lifecycle technically defined — 60%`.**

O próximo ciclo deverá concluir:

- máquinas de estado independentes;
- matriz completa de transições;
- precondições e invariantes por transição;
- compensações;
- timeouts e expirações;
- pausas e retomadas;
- falhas parciais;
- testes de transição.

## 8. Limites preservados

O estado `0.2.0` não autoriza:

- implementação em produção;
- escolha definitiva de tecnologia;
- transformação do agregado em microsserviço;
- incorporação automática ao Contexto Vivo;
- confirmação por IA;
- encerramento de gaps sem evidência;
- redução dos direitos do participante.
