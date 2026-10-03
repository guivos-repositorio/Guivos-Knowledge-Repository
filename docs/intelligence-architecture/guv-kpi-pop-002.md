---
id: GUV-KPI-POP-002
title: KPI Contract — Novas Pessoas
status: proposed
version: 0.1.0
owner: Guivos Intelligence Architecture
last_updated: 2026-09-12
normative: false
maturity: governed_pre_implementation_kpi_contract
depends_on:
  - GKR-INTELLIGENCE-KPI-CONTRACT-001
  - GKR-INTELLIGENCE-DASHBOARD-GUIVOS-KPI-REGISTRY-001
  - GKR-INTELLIGENCE-DASHBOARD-GUIVOS-001
---

# GUV-KPI-POP-002 — Novas Pessoas

```text
status: proposed
readiness: NOT_READY
contract_version: 0.1.0
```

## Contract record

**RESOLVED**

- `metric_id`: `GUV-KPI-POP-002`;
- `name`: Novas Pessoas;
- `question_answered`: quantas Pessoas elegíveis tiveram criação válida no período?;
- `family`: POP;
- `consumer_dashboard`: `GKR-INTELLIGENCE-DASHBOARD-GUIVOS-001`;
- `purpose`: compreender entrada agregada de Pessoas por período;
- `authorized_audience`: classes internas autorizadas, sem acesso individual padrão;
- `unit_of_analysis`: Pessoa;
- `unit`: pessoas/período;
- `directionality`: contextual;
- `granularity`: Pessoa no cálculo, agregado no disclosure padrão;
- `access_class`: Guivos interno autorizado / agregado;
- `aggregation_rule`: distinct count após elegibilidade;
- `drilldown_ceiling`: sem Pessoa individual por padrão;
- `evidence_nature`: CALCULADO a partir de registro operacional autorizado;
- `supported_claims`: quantidade de Pessoas que satisfazem a futura regra de criação válida no período;
- `prohibited_claims`: não equivale a Pessoas ativadas, ativas ou retidas;
- `confounders`: eventos retroativos, duplicidade, timezone e elegibilidade;
- `applicable_validations`: conceptual + data + temporal + privacy/disclosure;
- `semantic_visualization`: KPI card ou série temporal somente após fechamento temporal;
- `status`: proposed;
- `readiness`: NOT_READY.

**UNRESOLVED**

- `entity_population`, `formula`, `inclusions`, `exclusions`;
- `time_window`, `timezone`, `closing_rule`;
- `dimensions`, `filters`, `protection_threshold`, `export_rule`, `suppression_rule`;
- `quality_checks`, `null_handling`, `zero_handling`;
- `accountable_owner`, `calculation_owner`, `review_cadence`, `retention_rule`;
- `domain_contracts`, `serving_contract_ref`.

**SOURCE_PENDING**

- `source_of_truth`, `freshness_rule`, `provenance`, `source_version_rule`.

**NOT_APPLICABLE nesta versão**

- `numerator`, `denominator`, `comparison_baseline`, `change_log_ref` antes de operação.

## Blocking gates

```text
PERSON ELIGIBILITY / VALID CREATION EVENT
PERIOD / TIMEZONE / CLOSING
SOURCE + QUALITY
DISCLOSURE
OWNERS + DOMAIN CONTRACTS
SERVING
```

## Acceptance criteria

Antes de qualquer promoção, devem estar fechados elegibilidade, criação válida, período/timezone, source, quality, disclosure, owners, domain contracts e serving; a contagem distinta deve reconciliar com a fonte autorizada.

```text
GUV-KPI-POP-002
→ CONTRACT MATERIALIZED
→ proposed
→ NOT_READY
→ NO REAL DATA
→ NO REPLIT BUILD
```