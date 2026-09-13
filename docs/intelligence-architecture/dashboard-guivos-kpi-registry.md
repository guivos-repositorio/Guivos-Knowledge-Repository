---
id: GKR-INTELLIGENCE-DASHBOARD-GUIVOS-KPI-REGISTRY-001
title: Dashboard Guivos — Registry de Contratos de KPI
status: active
version: 0.1.0
owner: Guivos Intelligence Architecture
last_updated: 2026-09-12
normative: false
maturity: governed_pre_implementation_kpi_registry
depends_on:
  - GKR-INTELLIGENCE-DASHBOARD-KPI-001
  - GKR-INTELLIGENCE-KPI-CONTRACT-001
  - GKR-INTELLIGENCE-DASHBOARD-GUIVOS-001
related:
  - GEM-009-MEASUREMENT-CONTRACT-001
---

# Dashboard Guivos — Registry de Contratos de KPI

## 1. Finalidade

Este documento é o registry governado dos contratos individuais de KPI do Dashboard Guivos.

Ele não substitui o master global nem o master especializado. Sua função é registrar quais KPI IDs já possuem contract record materializado, qual versão está vigente, qual é o estado semântico e quais blockers impedem avanço.

```text
MASTER GUIVOS
→ CATÁLOGO ANALÍTICO PRETENDIDO

KPI REGISTRY
→ CONTROLE DE CONTRATOS MATERIALIZADOS

KPI CONTRACT RECORD
→ SEMÂNTICA INDIVIDUAL DO KPI
```

## 2. Boundary

```text
REAL DATA
→ NOT AUTHORIZED

SERVING / API
→ NOT DEFINED HERE

REPLIT BUILD
→ NOT AUTHORIZED

STATUS UPGRADE
→ ONLY AFTER CONTRACT STANDARD GATES
```

## 3. Adjudicação inicial de status

A aplicação de `GKR-INTELLIGENCE-KPI-CONTRACT-001` revelou que os KPIs anteriormente classificados como `source_pending` ainda possuem elementos semânticos materiais não adjudicados.

Pelo algoritmo canônico:

```text
SEMANTICS INCOMPLETE
→ proposed

SEMANTICS CLOSED + SOURCE BLOCKED
→ source_pending
```

Portanto, nesta frente os seguintes itens devem permanecer/recuar para `proposed` até fechamento dos blockers semânticos:

| KPI | Bloqueio semântico material | Estado governado |
|---|---|---|
| `GUV-KPI-POP-001` | validade/exclusões da Pessoa | `proposed` |
| `GUV-KPI-POP-002` | criação válida + temporal contract | `proposed` |
| `GUV-KPI-POP-007` | validade/exclusões da Organização | `proposed` |
| `GUV-KPI-POP-009` | validade/exclusões do Coletivo | `proposed` |
| `GUV-KPI-POP-011` | denominador + escopo aplicável | `proposed` |
| `GUV-KPI-OPP-001` | validade da oportunidade | `proposed` |

Essa reclassificação é conservadora e não remove os KPI IDs do catálogo.

## 4. Wave A1 — contratos materializados

A primeira wave documental materializa quatro contratos fundacionais de contagem/crescimento de participantes.

| KPI | Contract record | Versão | Status | Readiness |
|---|---|---:|---|---|
| `GUV-KPI-POP-001` | `guv-kpi-pop-001.md` | 0.1.0 | proposed | NOT_READY |
| `GUV-KPI-POP-002` | `guv-kpi-pop-002.md` | 0.1.0 | proposed | NOT_READY |
| `GUV-KPI-POP-007` | `guv-kpi-pop-007.md` | 0.1.0 | proposed | NOT_READY |
| `GUV-KPI-POP-009` | `guv-kpi-pop-009.md` | 0.1.0 | proposed | NOT_READY |

## 5. Próximos itens do registry

```text
GUV-KPI-POP-011
→ CONTRACT RECORD NOT MATERIALIZED
→ proposed
→ denominator + applicable scope unresolved

GUV-KPI-OPP-001
→ CONTRACT RECORD NOT MATERIALIZED
→ proposed
→ opportunity validity unresolved
```

Os demais KPI IDs permanecem governados pelo catálogo do master especializado e só entram neste registry quando seu contract record for materializado.

## 6. Regras do registry

1. nenhum KPI pode ser promovido por inferência;
2. `source_pending` exige semântica fechada;
3. cada record deve seguir `GKR-INTELLIGENCE-KPI-CONTRACT-001`;
4. mudança material deve atualizar `contract_version`;
5. o registry deve apontar blockers de forma explícita;
6. `defined` não implica `READY_FOR_BUILD`;
7. nenhum record autoriza conexão a dados reais;
8. Replit não deve consumir item `proposed` como KPI canônico.

## 7. Estado final

```text
GKR-INTELLIGENCE-DASHBOARD-GUIVOS-KPI-REGISTRY-001
→ v0.1.0
→ ACTIVE
→ GOVERNED PRE-IMPLEMENTATION KPI REGISTRY

WAVE A1
→ 4 CONTRACT RECORDS MATERIALIZED
→ ALL proposed
→ ALL NOT_READY

SOURCE_PENDING RECONCILIATION
→ 6 ITEMS REQUIRE proposed UNTIL SEMANTIC BLOCKERS CLOSE

REAL DATA / SERVING / REPLIT BUILD
→ NOT AUTHORIZED
```