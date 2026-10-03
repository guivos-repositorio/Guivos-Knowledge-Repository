---
id: ROADMAP-OVERLAY-11.15.0
title: Roadmap Arquitetural — Estado Efetivo 11.15.0
status: active
version: 11.15.0
owner: Guivos
last_updated: 2026-07-19
supersedes_partial:
  - ROADMAP-OVERLAY-11.14.0
related:
  - PAS-001-ENGINEERING-HANDOFF-001
  - PAS-001-CC-UIC-001
  - PAS-001-CC-UIC-LIFECYCLE-001
  - M5.14
---

# Roadmap Arquitetural — Estado Efetivo 11.15.0

> O Roadmap-base permanece preservado. Este overlay prevalece sobre estado corrente, marco vigente, backlog prioritário e ponto de retomada.

## Estado atual

| Frente | Estado |
|---|---|
| Arquitetura funcional do Journey | Publicada e concluída |
| Engineering Handoff | Draft 0.3.0 efetivo |
| UIC-01 — Captura de Contexto | Draft 0.3.0 |
| Estado técnico da UIC-01 | Lifecycle technically defined |
| Progresso | 60% |
| Marco vigente | M5.14 — Capture Context Technical Lifecycle Defined |
| Frente operacional | Product Engineering |

## Entrega concluída

- 13 máquinas de estado independentes;
- snapshot composto do registro;
- matriz material de transições da sessão;
- estados de canal, entrada e derivados;
- guardas por comando;
- pausa, retomada e continuidade entre canais;
- timeouts, expirações e encerramentos;
- falhas parciais, retries e compensações;
- sincronização entre estados funcionais e técnicos;
- protocolo de transcrição e correção;
- política de persistência temporária;
- 60 testes de ciclo;
- resolução de `UIC01-GAP-004` e `UIC01-GAP-005`.

## Progressão técnica

| Etapa | Estado | Progresso |
|---|---|---:|
| Fundação normativa | Normative sources mapped | 20% |
| Modelo de domínio | Domain model proposed | 40% |
| Ciclo técnico | Lifecycle technically defined | 60% |
| Contratos técnicos | Contracts technically proposed | 80% |
| Prontidão técnica | Technically ready for implementation | 100% |

## Backlog prioritário

### P0 — Contratos técnicos da UIC-01

1. catálogo versionado de comandos;
2. catálogo versionado de eventos;
3. schemas mínimos;
4. contratos síncronos e assíncronos;
5. contratos de consumidores;
6. protocolo entre contextos para correção e revogação;
7. erros funcionais e técnicos;
8. compatibilidade e versionamento;
9. idempotência por operação;
10. testes de contrato.

### P1 — Gaps do próximo ciclo

- `UIC01-GAP-006 — propagação técnica de revogação`;
- `UIC01-GAP-007 — estratégia de reconstrução`;
- `UIC01-GAP-009 — dependências mínimas da Onda 0`.

### P2 — Decisões tecnológicas

Permanecem posteriores aos contratos e deverão ser registradas por ADRs comparativos.

## Próximo marco candidato

> `M5.15 — Capture Context Technical Contracts Proposed`

Condição: UIC-01 em `Contracts technically proposed — 80%`, com catálogos, schemas, compatibilidade, erros, integrações e testes de contrato suficientemente definidos.

## Ponto exato de retomada

> Elaborar contratos técnicos da Captura de Contexto.
