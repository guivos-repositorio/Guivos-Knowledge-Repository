---
id: ROADMAP-OVERLAY-11.14.0
title: Roadmap Arquitetural — Estado Efetivo 11.14.0
status: active
version: 11.14.0
owner: Guivos
last_updated: 2026-07-19
supersedes_partial:
  - ROADMAP-OVERLAY-11.13.0
related:
  - PAS-001-ENGINEERING-HANDOFF-001
  - PAS-001-CC-UIC-001
  - PAS-001-CC-UIC-DOMAIN-001
  - M5.13
---

# Roadmap Arquitetural — Estado Efetivo 11.14.0

> O Roadmap-base permanece preservado. Este overlay prevalece sobre estado corrente, marco vigente, backlog prioritário e ponto de retomada.

## Estado atual

| Frente | Estado |
|---|---|
| Arquitetura funcional do Journey | Publicada e funcionalmente concluída |
| Engineering Handoff | Draft 0.2.0 efetivo |
| UIC-01 — Captura de Contexto | Draft 0.2.0 efetivo |
| Estado técnico da UIC-01 | Domain model proposed |
| Progresso de referência | 40% |
| Marco vigente | M5.13 — Capture Context Domain Model Proposed |
| Frente operacional | Product Engineering |

## Entregas concluídas nesta versão

- criação da primeira Unidade de Implementação de Capacidade;
- definição de autoridade e decisões proibidas;
- confirmação de `CaptureRecord` como Aggregate Root;
- confirmação de `CaptureSession` como entidade interna;
- definição da identidade permanente de `CaptureInput`;
- classificação de entidades e objetos de valor;
- formalização de invariantes estruturais e por comando;
- definição de consistência imediata e eventual;
- definição de concorrência otimista e idempotência;
- proposta de reconstrução;
- diagramas de agregados, entidades, comandos, ciclo, correção e revogação;
- resolução de `UIC01-GAP-001` e `UIC01-GAP-002`.

## Backlog prioritário

### P0 — Ciclo técnico da UIC-01

1. definir máquinas de estado independentes;
2. concluir matriz de transições;
3. definir precondições por transição;
4. formalizar compensações;
5. definir timeouts e expirações;
6. detalhar pausas e retomadas;
7. tratar falhas parciais;
8. concluir testes de transição;
9. elevar a unidade para `Lifecycle technically defined — 60%`.

### P1 — Contratos técnicos derivados

- catálogo versionado de comandos;
- catálogo versionado de eventos;
- política de persistência temporária;
- protocolo completo de revogação;
- contratos mínimos da Onda 0.

### P2 — Decisões tecnológicas

Permanecem posteriores ao domínio e deverão ser registradas por ADRs comparativos.

## Próximo marco candidato

> `M5.14 — Capture Context Technical Lifecycle Defined`

Condição: UIC-01 em `Lifecycle technically defined — 60%`, com máquinas de estado, transições, compensações, falhas e testes de ciclo concluídos.

## Ponto exato de retomada

> Definir tecnicamente o ciclo de vida da UIC-01.
