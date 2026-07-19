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
  - M5.12
---

# Roadmap Arquitetural — Estado Efetivo 11.14.0

> O Roadmap-base permanece preservado. Este overlay prevalece sobre estado corrente, marco vigente, backlog prioritário e ponto de retomada.

## Estado atual

| Frente | Estado |
|---|---|
| Arquitetura funcional do Journey | Publicada e funcionalmente concluída |
| Engineering Handoff | Draft 0.2.0 efetivo |
| UIC-01 — Captura de Contexto | Draft 0.1.0 |
| Estado técnico da UIC-01 | Normative sources mapped |
| Marco vigente | M5.12 — Capture Context Engineering Unit Defined |
| Frente operacional | Product Engineering |

## Entrega concluída nesta versão

- criação da primeira Unidade de Implementação de Capacidade;
- definição de autoridade e decisões proibidas;
- proposta de agregados e invariantes;
- catálogo inicial de comandos e eventos;
- delimitação de produtores e consumidores;
- classificação de persistência, busca e grafo;
- incorporação de segurança, privacidade, observabilidade e testes;
- mapeamento de dependências da Onda 0;
- registro de riscos e lacunas.

## Backlog prioritário

### P0 — Domain model da UIC-01

1. resolver `UIC01-GAP-001`;
2. resolver `UIC01-GAP-002`;
3. confirmar raiz e limites de agregados;
4. definir identidades e chaves;
5. formalizar invariantes por comando;
6. classificar consistência e concorrência;
7. definir estratégia inicial de reconstrução.

### P1 — Contratos técnicos derivados

- catálogo versionado de comandos;
- catálogo versionado de eventos;
- política de persistência temporária;
- protocolo de revogação;
- contratos mínimos da Onda 0.

### P2 — Decisões tecnológicas

Permanecem posteriores ao domínio e deverão ser registradas por ADRs comparativos.

## Próximo marco candidato

> `M5.13 — Capture Context Domain Model Proposed`

Condição: UIC-01 em `Domain model proposed`, com agregados, identidades e invariantes suficientemente definidos para revisão técnica.

## Ponto exato de retomada

> Aprofundar agregados, identidades e invariantes da Captura de Contexto.
