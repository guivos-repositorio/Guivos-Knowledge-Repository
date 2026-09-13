---
id: GKR-INTELLIGENCE-DASHBOARD-GUIVOS-KPI-REGISTRY-001
title: Dashboard Guivos — Registry de Contratos de KPI
status: active
version: 0.1.1
owner: Guivos Intelligence Architecture
last_updated: 2026-09-12
normative: false
maturity: governed_pre_implementation_kpi_registry
depends_on:
  - GKR-INTELLIGENCE-KPI-CONTRACT-001
  - GKR-INTELLIGENCE-DASHBOARD-GUIVOS-001
---

# Dashboard Guivos — Registry de Contratos de KPI

Este registry registra somente contratos efetivamente materializados.

| KPI | Contract record | Status | Readiness |
|---|---|---|---|
| `GUV-KPI-POP-001` | `guv-kpi-pop-001.md` | proposed | NOT_READY |
| `GUV-KPI-POP-002` | `guv-kpi-pop-002.md` | proposed | NOT_READY |

A aplicação de `GKR-INTELLIGENCE-KPI-CONTRACT-001` também identifica blockers semânticos nos itens antes marcados `source_pending`: `POP-001`, `POP-002`, `POP-007`, `POP-009`, `POP-011` e `OPP-001`. Até fechamento desses blockers, nenhum deve ser tratado como build-ready.

```text
POP-007 / POP-009
→ CONTRACT RECORD NOT MATERIALIZED

REAL DATA / SERVING / REPLIT BUILD
→ NOT AUTHORIZED
```