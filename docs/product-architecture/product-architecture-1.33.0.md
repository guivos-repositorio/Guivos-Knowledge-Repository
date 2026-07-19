---
id: PRODUCT-ARCHITECTURE-OVERLAY-1.33.0
title: Product Architecture Effective State 1.33.0
status: active
version: 1.33.0
owner: Guivos
last_updated: 2026-07-19
normative: true
supersedes_partial:
  - PRODUCT-ARCHITECTURE-OVERLAY-1.32.0
related:
  - PAS-001
  - PAS-001-CAPABILITY-MAP-001
  - PAS-001-ENGINEERING-HANDOFF-001
  - PAS-001-CC-UIC-001
---

# Arquitetura de Produtos — Estado Efetivo 1.33.0

> Este overlay preserva o índice e o inventário histórico da Arquitetura de Produtos. Ele prevalece somente sobre versão efetiva, frente operacional, marco vigente e próximo ponto de retomada.

## Estado arquitetural

| Ativo | Estado efetivo |
|---|---|
| PAS-001 | Active 1.0.0 |
| Mapa Final | Active 1.0.1 |
| Engineering Handoff | Draft 0.2.0 efetivo |
| UIC-01 — Captura de Contexto | Draft 0.1.0 |
| Capacidades 01–09 | Functionally complete |
| Frente operacional | Product Engineering |
| Marco vigente | M5.12 |

## Novo ativo normativo

[`PAS-001-CC-UIC-001`](pas-001-captura-de-contexto-engineering-unit.md) traduz a Captura de Contexto para uma unidade técnica rastreável contendo:

- autoridade e decisões proibidas;
- agregados candidatos;
- invariantes iniciais;
- estados e transições;
- comandos e eventos;
- produtores e consumidores;
- persistência, busca e grafo;
- segurança, privacidade e Intelligence;
- observabilidade e testes;
- dependências, riscos e critérios de prontidão.

## Autoridades preservadas

Permanecem inalterados:

- PAS-001 1.0.0;
- Mapa Final 1.0.1;
- nove contratos finais;
- 54 extensões normativas;
- GLPA-001 1.1.1;
- GIA-000 1.3.0.

A UIC-01 é uma tradução técnica subordinada e não reabre a arquitetura funcional.

## Próximo ponto

> Aprofundar agregados, identidades e invariantes da Captura de Contexto para preparar `Domain model proposed`.

Prioridades:

1. confirmar o limite entre `CaptureRecord` e `CaptureSession`;
2. definir a identidade técnica da entrada original;
3. formalizar invariantes por comando;
4. classificar consistência, concorrência e reconstrução.
