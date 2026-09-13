---
id: GKR-INTELLIGENCE-DASHBOARD-GUIVOS-KPI-REGISTRY-001
status: active
version: 0.1.4
owner: Guivos Intelligence Architecture
last_updated: 2026-09-12
normative: false
maturity: governed_pre_implementation_kpi_registry
depends_on:
  - GKR-INTELLIGENCE-KPI-CONTRACT-001
  - GKR-INTELLIGENCE-DASHBOARD-GUIVOS-001
  - GKR-INTELLIGENCE-DASHBOARD-GUIVOS-KPI-STATUS-RECONCILIATION-001
---

# Dashboard Guivos — KPI Registry

| KPI | Contract record | Version | Status | Readiness |
|---|---|---:|---|---|
| `GUV-KPI-POP-001` | [`guv-kpi-pop-001.md`](guv-kpi-pop-001.md) | `0.1.0` | `proposed` | `NOT_READY` |
| `GUV-KPI-POP-002` | [`guv-kpi-pop-002.md`](guv-kpi-pop-002.md) | `0.1.0` | `proposed` | `NOT_READY` |

## Status reconciliation

[`GKR-INTELLIGENCE-DASHBOARD-GUIVOS-KPI-STATUS-RECONCILIATION-001`](dashboard-guivos-kpi-status-reconciliation.md) adjudica o campo `status` dos seis IDs abaixo:

| KPI | Status | Record |
|---|---|---|
| `GUV-KPI-POP-001` | `proposed` | materialized |
| `GUV-KPI-POP-002` | `proposed` | materialized |
| `GUV-KPI-POP-007` | `proposed` | not materialized |
| `GUV-KPI-POP-009` | `proposed` | not materialized |
| `GUV-KPI-POP-011` | `proposed` | not materialized |
| `GUV-KPI-OPP-001` | `proposed` | not materialized |

```text
STATUS RECONCILIATION → ADJUDICATED
ALL 6 → proposed / NOT_READY
REAL DATA / SERVING / API / REPLIT BUILD → NOT AUTHORIZED
```

Até absorção formal por versão posterior do master, a reconciliação prevalece somente sobre o campo `status` desses seis IDs.