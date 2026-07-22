---
id: GEM-009-MEASUREMENT-CONTRACT-001
title: Contrato Canônico de Métrica Econômica
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-22
parent: GEM-009
---

# Contrato Canônico de Métrica Econômica

## 1. Objetivo

Definir os campos mínimos para que uma métrica seja compreensível, reproduzível, governável e interpretada dentro de seus limites.

## 2. Contrato

```yaml
metric_id: string
name: string
question: string
family: string
type: input | activity | output | adoption | quality | outcome | impact | efficiency | sustainability | risk | guardrail
status: proposed | defined | source_pending | instrumentation_pending | baseline_pending | observed | validated | degraded | suspended | retired

definition:
  numerator: string | null
  denominator: string | null
  formula: string
  unit: string
  directionality: higher_better | lower_better | range_preferred | contextual | guardrail_only
  exclusions: [string]

scope:
  population: string
  unit_of_analysis: string
  segments: [string]
  time_window: string
  comparison_basis: string | null

evidence:
  nature: direct | declared | derived | estimated | proxy | modeled | externally_audited
  sources: [string]
  provenance_required: true
  freshness_rule: string
  quality_checks: [string]
  missing_data_treatment: string

governance:
  accountable_owner: string | null
  calculation_owner: string | null
  review_cadence: string | null
  access_class: string
  retention_rule: string | null
  change_log_required: true

interpretation:
  supported_claims: [string]
  prohibited_claims: [string]
  confounders: [string]
  uncertainty: string

thresholds:
  baseline_status: pending
  target_status: not_approved
  guardrail_status: not_approved

validation:
  conceptual: pending
  data: pending
  financial: pending
  accounting: pending
  legal_privacy_security: pending
```

## 3. Regras

- denominador, população, janela e exclusões não poderão ficar implícitos;
- alteração de fórmula ou fonte cria nova versão ou ruptura de série;
- dado ausente não será convertido em zero sem justificativa;
- métrica sem owner ou fonte não poderá ser tratada como operacional;
- thresholds permanecerão pendentes até baseline e aprovação formal;
- acesso deverá respeitar finalidade, minimização e necessidade legítima.

## 4. Não constitui

Dashboard, esquema de banco de dados, especificação de analytics, registro contábil, meta, SLA, orçamento ou autorização decisória.
