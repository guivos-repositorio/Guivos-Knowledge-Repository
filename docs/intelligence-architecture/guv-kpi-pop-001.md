---
id: GUV-KPI-POP-001
title: KPI Contract — Pessoas cadastradas
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

# GUV-KPI-POP-001 — Pessoas cadastradas

## Contract state

```text
status: proposed
readiness: NOT_READY
contract_version: 0.1.0
```

## Identidade e finalidade

| Campo | Estado | Valor |
|---|---|---|
| metric_id | RESOLVED | `GUV-KPI-POP-001` |
| name | RESOLVED | Pessoas cadastradas |
| question_answered | RESOLVED | Quantas Pessoas válidas existem no universo corrente elegível do Dashboard Guivos? |
| family | RESOLVED | POP |
| consumer_dashboard | RESOLVED | `GKR-INTELLIGENCE-DASHBOARD-GUIVOS-001` |
| purpose | RESOLVED | compreender tamanho agregado da população de Pessoas elegível para leitura interna autorizada |
| authorized_audience | RESOLVED | classes internas autorizadas conforme master especializado; não implica acesso individual |

## População, cálculo e temporalidade

| Campo | Estado | Valor |
|---|---|---|
| entity_population | UNRESOLVED | critérios de Pessoa válida/elegível ainda não adjudicados |
| unit_of_analysis | RESOLVED | Pessoa |
| formula | UNRESOLVED | candidato: contagem distinta de Pessoas válidas; depende da regra de validade |
| numerator | NOT_APPLICABLE | métrica de contagem |
| denominator | NOT_APPLICABLE | métrica de contagem |
| unit | RESOLVED | pessoas |
| directionality | RESOLVED | contextual; maior não significa melhor |
| inclusions | UNRESOLVED | depende da regra de elegibilidade |
| exclusions | UNRESOLVED | testes, duplicidades, estados inválidos e demais exclusões precisam de autoridade explícita |
| time_window | UNRESOLVED | leitura corrente requer regra de referência/as_of |
| timezone | UNRESOLVED | necessária se a referência temporal depender de fechamento operacional |
| closing_rule | UNRESOLVED | não adjudicada |
| comparison_baseline | NOT_APPLICABLE | contrato base não define comparação |
| granularity | RESOLVED | Pessoa para cálculo; apenas agregado para disclosure padrão |

## Dimensões e disclosure

| Campo | Estado | Valor |
|---|---|---|
| dimensions | UNRESOLVED | somente dimensões autorizadas pelo master e por contratos de disclosure |
| filters | UNRESOLVED | filtros específicos do KPI ainda não fechados |
| access_class | RESOLVED | Guivos interno autorizado / leitura agregada |
| aggregation_rule | RESOLVED | distinct count sobre população elegível após regras de validade |
| protection_threshold | UNRESOLVED | exigido para segmentos quando aplicável |
| drilldown_ceiling | RESOLVED | agregado/segmento autorizado; Pessoa individual não é drill-down padrão |
| export_rule | UNRESOLVED | não autorizada por este contrato |
| suppression_rule | UNRESOLVED | depende de política de disclosure |

## Origem, qualidade e proveniência

| Campo | Estado | Valor |
|---|---|---|
| source_of_truth | SOURCE_PENDING | participant/Pessoa source ainda não adjudicada |
| evidence_nature | RESOLVED | CALCULADO a partir de registros operacionais autorizados |
| freshness_rule | SOURCE_PENDING | depende do source/data contract |
| quality_checks | UNRESOLVED | ao menos unicidade, validade e completude de identificador deverão ser fechadas |
| null_handling | UNRESOLVED | depende de elegibilidade/validade |
| zero_handling | UNRESOLVED | zero só pode ser exibido quando ausência real for distinguível de indisponibilidade |
| provenance | SOURCE_PENDING | source + transformação ainda não materializados |
| source_version_rule | SOURCE_PENDING | depende da fonte |

## Governança e interpretação

| Campo | Estado | Valor |
|---|---|---|
| accountable_owner | UNRESOLVED | responsável semântico ainda não designado |
| calculation_owner | UNRESOLVED | responsável pelo cálculo ainda não designado |
| review_cadence | UNRESOLVED | não adjudicada |
| retention_rule | UNRESOLVED | depende dos contratos de dados aplicáveis |
| supported_claims | RESOLVED | quantidade agregada de Pessoas que satisfazem a futura regra de validade na referência |
| prohibited_claims | RESOLVED | não representa Pessoas ativas, engajadas, retidas, impactadas ou evoluídas |
| confounders | RESOLVED | duplicidade, registros de teste, estados inválidos, regras de exclusão e mudanças de elegibilidade |
| uncertainty | RESOLVED | deve ser qualificada enquanto source/quality não estiverem fechados |
| applicable_validations | RESOLVED | conceptual + data + privacy/disclosure |
| domain_contracts | UNRESOLVED | autoridades de Pessoa/participante e privacidade aplicáveis devem ser apontadas antes de promoção |
| change_log_ref | NOT_APPLICABLE | obrigatório quando operacional |

## Handoff e aceite

| Campo | Estado | Valor |
|---|---|---|
| semantic_visualization | RESOLVED | KPI card agregado com `as_of`/freshness quando disponível |
| serving_contract_ref | UNRESOLVED | não existe contrato de serving autorizado nesta versão |
| acceptance_criteria | RESOLVED | validade/elegibilidade, source, temporalidade, quality, disclosure e owners fechados; reconciliação de distinct count comprovada |
| status | RESOLVED | proposed |
| readiness | RESOLVED | NOT_READY |
| blocking_gates | RESOLVED | validade/exclusões; source; temporalidade; quality; disclosure; owners; domain contracts; serving |

## Estado final

```text
GUV-KPI-POP-001
→ CONTRACT MATERIALIZED
→ proposed
→ NOT_READY
→ NO REAL DATA
→ NO REPLIT BUILD
```