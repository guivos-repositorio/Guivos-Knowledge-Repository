---
id: GEM-010-FINANCIAL-MODEL-CONTRACT-001
title: Contrato Canônico do Modelo Financeiro
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-22
parent: GEM-010
---

# Contrato Canônico do Modelo Financeiro

```yaml
model_id: string
version: string
status: conceptual | parameter_pending | calibrated | reviewed | approved_for_planning | superseded
as_of_date: date
horizon: string
granularity: monthly | quarterly | annual
currency: string
price_basis: nominal | real
consolidation_scope: [string]
scenarios: [conservative, base, expansive, stress]
assumptions:
  registry_required: true
  evidence_class_required: true
  missing_value: TBD
outputs:
  - operating_drivers
  - revenue_and_costs
  - contribution_and_result
  - cash_and_working_capital
  - unit_economics
  - funding_need
controls:
  reconciliation_required: true
  sensitivity_required: true
  change_log_required: true
  independent_review_required: true
approvals:
  planning: pending
  financial: pending
  accounting_tax_legal: pending
```

Nenhum output poderá circular sem versão, data-base, cenário, unidade, moeda, fonte e disclaimer de incerteza.

