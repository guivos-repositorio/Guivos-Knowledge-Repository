---
id: GKR-INTELLIGENCE-DASHBOARD-GUIVOS-KPI-REGISTRY-001
status: active
version: 0.1.5
owner: Guivos Intelligence Architecture
last_updated: 2026-09-12
normative: false
maturity: governed_pre_implementation_kpi_registry
depends_on:
  - GKR-INTELLIGENCE-KPI-CONTRACT-001
  - GKR-INTELLIGENCE-DASHBOARD-GUIVOS-001
related:
  - GKR-INTELLIGENCE-DASHBOARD-GUIVOS-KPI-STATUS-RECONCILIATION-001
---

# Dashboard Guivos — KPI Registry

| KPI | Contract record | Version | Status | Readiness |
|---|---|---:|---|---|
| `GUV-KPI-POP-001` | [`guv-kpi-pop-001.md`](guv-kpi-pop-001.md) | `0.1.0` | `proposed` | `NOT_READY` |
| `GUV-KPI-POP-002` | [`guv-kpi-pop-002.md`](guv-kpi-pop-002.md) | `0.1.0` | `proposed` | `NOT_READY` |

## Status canônico após absorção

`GKR-INTELLIGENCE-DASHBOARD-GUIVOS-001 v0.1.4` absorve a adjudicação anteriormente registrada em [`GKR-INTELLIGENCE-DASHBOARD-GUIVOS-KPI-STATUS-RECONCILIATION-001`](dashboard-guivos-kpi-status-reconciliation.md). O Documento Mestre volta a ser a autoridade direta para o campo `status` dos seis IDs abaixo.

| KPI | Status | Readiness | Record |
|---|---|---|---|
| `GUV-KPI-POP-001` | `proposed` | `NOT_READY` | materialized |
| `GUV-KPI-POP-002` | `proposed` | `NOT_READY` | materialized |
| `GUV-KPI-POP-007` | `proposed` | `NOT_READY` | not materialized |
| `GUV-KPI-POP-009` | `proposed` | `NOT_READY` | not materialized |
| `GUV-KPI-POP-011` | `proposed` | `NOT_READY` | not materialized |
| `GUV-KPI-OPP-001` | `proposed` | `NOT_READY` | not materialized |

```text
STATUS RECONCILIATION
→ ABSORBED INTO SPECIALIZED MASTER

REGISTRY
→ INDEX / TRACEABILITY
→ NOT SOURCE OF TRUTH

REAL DATA / SERVING / API / REPLIT BUILD
→ NOT AUTHORIZED
```

O documento de reconciliação permanece apenas como proveniência histórica da adjudicação. `POP-007`, `POP-009`, `POP-011` e `OPP-001` ainda exigem materialização individual futura.