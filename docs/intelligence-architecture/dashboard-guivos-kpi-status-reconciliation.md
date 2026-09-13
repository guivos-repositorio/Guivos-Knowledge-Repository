---
id: GKR-INTELLIGENCE-DASHBOARD-GUIVOS-KPI-STATUS-RECONCILIATION-001
title: Dashboard Guivos — Reconciliação de Status de KPIs
status: active
version: 0.1.0
owner: Guivos Intelligence Architecture
last_updated: 2026-09-12
normative: false
maturity: governed_pre_implementation_status_adjudication
depends_on:
  - GKR-INTELLIGENCE-KPI-CONTRACT-001
  - GKR-INTELLIGENCE-DASHBOARD-GUIVOS-001
  - GKR-INTELLIGENCE-DASHBOARD-GUIVOS-KPI-REGISTRY-001
---

# Dashboard Guivos — Reconciliação de Status de KPIs

Este ato adjudica somente o campo `status` de seis KPIs. Pelo standard vigente:

```text
SEMANTICS INCOMPLETE → proposed
SEMANTICS CLOSED + SOURCE BLOCKED → source_pending
```

Para os IDs abaixo, blockers semânticos ainda permanecem abertos; portanto o status governado é `proposed` e a readiness é `NOT_READY`.

| KPI | Blocker semântico | Status |
|---|---|---|
| `GUV-KPI-POP-001` | validade/elegibilidade e exclusões de Pessoa | `proposed` |
| `GUV-KPI-POP-002` | criação válida e regra temporal | `proposed` |
| `GUV-KPI-POP-007` | validade/elegibilidade de Organização | `proposed` |
| `GUV-KPI-POP-009` | validade/elegibilidade de Coletivo | `proposed` |
| `GUV-KPI-POP-011` | denominador e escopo aplicável | `proposed` |
| `GUV-KPI-OPP-001` | validade/elegibilidade da oportunidade | `proposed` |

Para esses seis IDs e somente para `status`, esta adjudicação prevalece sobre as células `source_pending` de `GKR-INTELLIGENCE-DASHBOARD-GUIVOS-001 v0.1.3` até absorção formal por versão posterior do master.

```text
STATUS OVERRIDE → LIMITED TO 6 KPI IDS / STATUS FIELD
READINESS → NOT_READY
REAL DATA / SERVING / API / REPLIT BUILD → NOT AUTHORIZED
```

`POP-001` e `POP-002` já possuem contract records v0.1.0. `POP-007`, `POP-009`, `POP-011` e `OPP-001` ainda exigem materialização individual futura. Esta reconciliação não fecha fórmula, fonte, população, temporalidade, disclosure ou serving.