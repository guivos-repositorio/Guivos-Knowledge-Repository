---
id: PAS-001-CC-UIC-001-OVERLAY-0.4.0
title: Estado Efetivo da UIC-01 — Contratos Técnicos Propostos
status: active
version: 0.4.0
owner: Guivos
last_updated: 2026-07-19
parent: PAS-001-CC-UIC-001
normative: true
supersedes_partial:
  - PAS-001-CC-UIC-001@0.3.0
related:
  - PAS-001-CC-UIC-DOMAIN-001
  - PAS-001-CC-UIC-LIFECYCLE-001
  - PAS-001-CC-UIC-CONTRACTS-001
  - PAS-001-CC-UIC-SCHEMAS-001
  - PAS-001-ENGINEERING-HANDOFF-001
---

# PAS-001-CC-UIC-001 — Estado Efetivo 0.4.0

> **Estado efetivo:** `Draft 0.4.0 — Contracts technically proposed`.
>
> **Progresso de referência:** `80%`.

Este overlay preserva integralmente a UIC-base `0.1.0`, os estados efetivos `0.2.0` e `0.3.0`, o Modelo de Domínio e o Ciclo Técnico. Ele prevalece somente sobre maturidade contratual, gaps resolvidos, marco vigente e ponto de retomada.

## 1. Bases preservadas

- [`PAS-001-CC-UIC-001 0.1.0`](pas-001-captura-de-contexto-engineering-unit.md);
- blob protegido da base: `48988df33cc8047664c41248efd25a0d9ba1dac9`;
- [`PAS-001-CC-UIC-DOMAIN-001 0.1.0`](pas-001-captura-de-contexto-domain-model.md);
- blob do modelo de domínio: `3ac54d3fb6955d34c6f85672efa63df77e865627`;
- [`PAS-001-CC-UIC-LIFECYCLE-001 0.1.0`](pas-001-captura-de-contexto-technical-lifecycle.md);
- [`Estado Efetivo 0.3.0`](pas-001-captura-de-contexto-engineering-unit-0.3.0.md).

## 2. Autoridades especializadas incorporadas

O estado efetivo incorpora:

- [`PAS-001-CC-UIC-CONTRACTS-001`](pas-001-captura-de-contexto-technical-contracts.md);
- [`PAS-001-CC-UIC-SCHEMAS-001`](pas-001-captura-de-contexto-contract-schema-pack.md);
- estado: `Contracts technically proposed`;
- progresso: `80%`.

## 3. Decisões técnicas adicionadas

- envelope comum de comandos;
- envelope comum de respostas;
- 30 comandos versionados;
- envelope de eventos funcionais;
- envelope separado de eventos técnicos;
- 32 eventos funcionais versionados;
- contratos síncronos e assíncronos;
- contrato comum de consumidor;
- contrato com Contexto Vivo;
- contrato com Guivos Intelligence;
- contrato com Journey Experience;
- protocolo contratual de correção;
- protocolo contratual de revogação;
- contrato de reconstrução e replay;
- 16 dependências mínimas da Onda 0;
- catálogo estável de erros;
- idempotência por operação;
- política de compatibilidade;
- pacote de schemas e fixtures;
- 80 testes obrigatórios de contrato.

## 4. Gaps resolvidos acumulados

| Gap | Estado |
|---|---|
| UIC01-GAP-001 — limite entre CaptureRecord e CaptureSession | Resolved |
| UIC01-GAP-002 — identidade técnica da entrada original | Resolved |
| UIC01-GAP-004 — protocolo de transcrição e correção | Resolved |
| UIC01-GAP-005 — persistência temporária | Resolved |
| UIC01-GAP-006 — propagação técnica de revogação | Resolved |
| UIC01-GAP-007 — estratégia de reconstrução | Resolved |
| UIC01-GAP-009 — dependências mínimas da Onda 0 | Resolved |

## 5. Gaps ainda abertos

| Gap | Estado | Próxima decisão |
|---|---|---|
| UIC01-GAP-003 | Open | armazenamento multimodal |
| UIC01-GAP-008 | Open | busca e indexação sensível |
| UIC01-GAP-010 | Open | matriz técnica de guardrails |

## 6. Estado efetivo da UIC-01

| Dimensão | Estado |
|---|---|
| Fundação normativa | Concluída para esta etapa |
| Modelo de domínio | Proposed |
| Ciclo técnico | Defined |
| Contratos técnicos | Proposed |
| Schemas lógicos | Proposed |
| Prontidão para implementação | Não alcançada |
| Produção | Não autorizada |

## 7. Marco vigente

> `M5.15 — Capture Context Technical Contracts Proposed`

## 8. Próximo ponto

> Elevar a UIC-01 para `Technically ready for implementation — 100%`.

Prioridades:

1. matriz de armazenamento multimodal;
2. busca e indexação sensível;
3. matriz técnica dos guardrails;
4. requisitos não funcionais e SLOs iniciais;
5. threat model;
6. matriz de acesso;
7. estratégia final de testes e evidências;
8. critérios de readiness da Onda 0;
9. ADRs requeridos;
10. resolução de `UIC01-GAP-003`, `UIC01-GAP-008` e `UIC01-GAP-010`.

## 9. Limites preservados

A versão `0.4.0` não autoriza:

- implementação em produção;
- escolha definitiva de tecnologia;
- transformação de contratos lógicos em microsserviços obrigatórios;
- promoção de evento técnico a fato funcional;
- incorporação automática ao Contexto Vivo;
- exposição de conteúdo sensível por conveniência de transporte;
- encerramento dos gaps ainda abertos.
