---
id: GKR-INTELLIGENCE-DASHBOARD-GUIVOS-KPI-STATUS-RECONCILIATION-001
title: Dashboard Guivos — Reconciliação de Status de KPIs
status: active
version: 0.1.1
owner: Guivos Intelligence Architecture
last_updated: 2026-09-12
normative: false
maturity: governed_pre_implementation_status_adjudication_record
depends_on:
  - GKR-INTELLIGENCE-KPI-CONTRACT-001
  - GKR-INTELLIGENCE-DASHBOARD-GUIVOS-001
  - GKR-INTELLIGENCE-DASHBOARD-GUIVOS-KPI-REGISTRY-001
---

# Dashboard Guivos — Reconciliação de Status de KPIs

## Estado de absorção

A adjudicação deste documento foi absorvida por `GKR-INTELLIGENCE-DASHBOARD-GUIVOS-001 v0.1.4`. Este artefato permanece ativo apenas como registro de proveniência da decisão; ele não exerce mais papel de override sobre o Documento Mestre.

```text
ADJUDICATION
→ ABSORBED BY GKR-INTELLIGENCE-DASHBOARD-GUIVOS-001 v0.1.4

OVERRIDE ROLE
→ ENDED

CURRENT ROLE
→ HISTORICAL / GOVERNANCE PROVENANCE
```

A decisão preservada é:

```text
SEMANTICS INCOMPLETE → proposed
SEMANTICS CLOSED + SOURCE BLOCKED → source_pending
```

Para os IDs abaixo, blockers semânticos permanecem abertos; portanto o status governado absorvido pelo master é `proposed` e a readiness é `NOT_READY`.

| KPI | Blocker semântico | Status |
|---|---|---|
| `GUV-KPI-POP-001` | validade/elegibilidade e exclusões de Pessoa | `proposed` |
| `GUV-KPI-POP-002` | criação válida e regra temporal | `proposed` |
| `GUV-KPI-POP-007` | validade/elegibilidade de Organização | `proposed` |
| `GUV-KPI-POP-009` | validade/elegibilidade de Coletivo | `proposed` |
| `GUV-KPI-POP-011` | denominador e escopo aplicável | `proposed` |
| `GUV-KPI-OPP-001` | validade/elegibilidade da oportunidade | `proposed` |

```text
STATUS OF 6 KPI IDS
→ proposed

READINESS
→ NOT_READY

REAL DATA / SERVING / API / REPLIT BUILD
→ NOT AUTHORIZED
```

`POP-001` e `POP-002` possuem contract records v0.1.0. `POP-007`, `POP-009`, `POP-011` e `OPP-001` ainda exigem materialização individual futura.

Esta reconciliação não fecha fórmula, fonte, população, temporalidade, disclosure ou serving.