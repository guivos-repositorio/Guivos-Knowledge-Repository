---
id: GKR-INTELLIGENCE-KPI-CONTRACT-001
title: KPI Contract Standard — Padrão Canônico de Contrato Analítico
status: active
version: 0.1.0
owner: Guivos Intelligence Architecture
last_updated: 2026-09-12
normative: false
maturity: governed_pre_implementation_kpi_contract_standard
depends_on:
  - GKR-INTELLIGENCE-DASHBOARD-KPI-001
  - GPA-006
  - GAI-001
  - GAI-002
  - GIA-COG-001
related:
  - GKR-INTELLIGENCE-DASHBOARD-GUIVOS-001
  - GKR-INTELLIGENCE-DASHBOARD-GUIVOS-KPI-REGISTRY-001
  - GEM-009-MEASUREMENT-CONTRACT-001
---

# KPI Contract Standard — Padrão Canônico de Contrato Analítico

## 1. Finalidade

Este documento operacionaliza o envelope de contrato de KPI definido por `GKR-INTELLIGENCE-DASHBOARD-KPI-001`.

Ele estabelece como um KPI deve ser especificado, classificado, versionado e entregue a uma camada downstream sem permitir que ferramentas de construção inventem significado, fórmula, população, origem, acesso ou interpretação.

```text
NOME DO KPI ≠ CONTRATO DO KPI
LINHA EM TABELA ≠ CONTRATO DO KPI
CONTRATO DOCUMENTADO ≠ DADO DISPONÍVEL ≠ BUILD AUTORIZADA
```

## 2. Posição documental

```text
MASTER GLOBAL
→ STANDARD DE CONTRATO
→ MASTER ESPECIALIZADO
→ REGISTRY ESPECIALIZADO
→ KPI CONTRACT RECORD
→ DATA / SERVING CONTRACT
→ SURFACE
```

Este standard não define schema físico, API, RBAC técnico, banco, Design System ou implementação.

## 3. KPI Contract Record

Cada KPI deve possuir um record identificável pelo `metric_id` estável. Nenhum campo obrigatório pode ser omitido silenciosamente.

### 3.1 Identidade e finalidade

- `metric_id`;
- `contract_version`;
- `name`;
- `question_answered`;
- `family`;
- `consumer_dashboard`;
- `purpose`;
- `authorized_audience`.

### 3.2 População, cálculo e temporalidade

- `entity_population`;
- `unit_of_analysis`;
- `formula`;
- `numerator`, quando aplicável;
- `denominator`, quando aplicável;
- `unit`;
- `directionality`, quando aplicável;
- `inclusions`, quando material;
- `exclusions`;
- `time_window`;
- `timezone`, para KPI temporal;
- `closing_rule`, quando aplicável;
- `comparison_baseline`, quando aplicável;
- `granularity`.

### 3.3 Dimensões e disclosure

- `dimensions`;
- `filters`;
- `access_class`;
- `aggregation_rule`;
- `protection_threshold`, quando aplicável;
- `drilldown_ceiling`;
- `export_rule`;
- `suppression_rule`, quando aplicável.

### 3.4 Origem, qualidade e proveniência

- `source_of_truth`;
- `evidence_nature`;
- `freshness_rule`;
- `quality_checks`;
- `null_handling`;
- `zero_handling`, quando zero for valor possível;
- `provenance`;
- `source_version_rule`, quando aplicável.

### 3.5 Governança e interpretação

- `accountable_owner`;
- `calculation_owner`;
- `review_cadence`;
- `retention_rule`;
- `supported_claims`;
- `prohibited_claims`;
- `confounders`, quando aplicável;
- `uncertainty`, quando material;
- `applicable_validations`;
- `domain_contracts`;
- `change_log_ref`, quando operacional.

### 3.6 Handoff e aceite

- `semantic_visualization`;
- `serving_contract_ref`;
- `acceptance_criteria`;
- `status`;
- `readiness`;
- `blocking_gates`.

## 4. Estados de campo

Todo campo ainda não fechado deve declarar seu estado. O vocabulário mínimo é:

```text
RESOLVED
→ valor semanticamente fechado

UNRESOLVED
→ significado ainda não adjudicado

SOURCE_PENDING
→ significado fechado, mas origem/data contract ainda bloqueado

BLOCKED_BY:<AUTHORITY_OR_CONTRACT>
→ depende de autoridade identificada

NOT_APPLICABLE
→ não se aplica; não pode mascarar desconhecimento
```

`UNRESOLVED` e `BLOCKED_BY` exigem entrada correspondente em `blocking_gates`.

## 5. Classificação de status

O vocabulário permanece:

```text
proposed
source_pending
defined
approved-equivalent
```

### `proposed`

Use quando qualquer elemento semântico material permanece `UNRESOLVED`, incluindo população, fórmula, validade, denominador, janela ou finalidade.

### `source_pending`

Use somente quando a definição lógica estiver suficientemente fechada e o bloqueio remanescente for de source/data contract/serving ou disponibilidade equivalente.

```text
SEMANTICS INCOMPLETE → proposed
SEMANTICS CLOSED + SOURCE BLOCKED → source_pending
```

`source_pending` não pode mascarar fórmula, população, validade, denominador ou janela ainda não adjudicados.

### `defined`

Use quando o contrato mínimo transversal estiver documentalmente preenchido e as autoridades de domínio necessárias ao significado estiverem satisfeitas.

`defined ≠ READY_FOR_BUILD`.

### `approved-equivalent`

Exige referência explícita a autoridade especializada que forneça estado equivalente aceito; não reduz gates transversais.

## 6. Status e readiness

`status` representa maturidade semântica/documental. `readiness` representa elegibilidade downstream no momento.

Vocabulário inicial de readiness:

```text
NOT_READY
READY_FOR_MOCK
READY_FOR_SERVING_INTEGRATION
READY_FOR_BUILD
```

Regras:

```text
proposed → NOT_READY
source_pending → NOT_READY
defined / approved-equivalent → ainda dependem de gates downstream
```

`READY_FOR_BUILD` exige, no mínimo: contrato semântico aceito, domain contracts satisfeitos, serving contract válido, access/disclosure fechado, freshness/quality fechados, null/zero/no-data fechados, filtros/drill-down/export fechados, dados classificados como mock ou real e autorização de Design/build.

## 7. Composição

```text
GLOBAL KPI CONTRACT MINIMUM
+ SPECIALIZED DASHBOARD CONTEXT
+ DOMAIN CONTRACTS
+ ACCESS / PRIVACY / DISCLOSURE
+ DATA / SERVING CONTRACT
= DOWNSTREAM-ELIGIBLE CONTRACT PACKAGE
```

Em conflito, o registry deve registrar o bloqueio; não deve escolher silenciosamente uma interpretação. KPIs econômicos devem compor com `GEM-009-MEASUREMENT-CONTRACT-001` e demais autoridades econômicas aplicáveis.

## 8. Registry especializado

Cada dashboard pode manter registry próprio para:

- listar KPI IDs do escopo;
- registrar versão do contrato;
- registrar `status` e `readiness`;
- apontar blockers;
- apontar o record individual correspondente;
- organizar waves documentais sem tratá-las como release de software.

```text
REGISTRY ≠ SOURCE OF TRUTH DE DOMÍNIO
REGISTRY ≠ IMPLEMENTAÇÃO
```

## 9. Forma documental

O record pode ser materializado em Markdown estruturado, YAML documental ou formato equivalente governado. Isso não define payload de produção.

Exemplo estrutural:

```yaml
metric_id: GUV-KPI-XXX-000
contract_version: 0.1.0
status: proposed
readiness: NOT_READY
name: "..."
entity_population:
  state: UNRESOLVED
  blocker: "..."
formula:
  state: UNRESOLVED
  blocker: "..."
source_of_truth:
  state: SOURCE_PENDING
  blocker: "..."
blocking_gates:
  - "..."
```

## 10. Versionamento

Mudança material em significado, população, fórmula, denominador, janela, unidade, access/disclosure, source-of-truth sem equivalência comprovada ou claims suportados exige nova versão do contrato.

```text
SAME metric_id → SAME ANALYTICAL MEANING
MATERIAL SEMANTIC BREAK → VERSION CHANGE
```

Séries historicamente incompatíveis não devem ser unidas como se fossem a mesma métrica.

## 11. Guardrails downstream

Replit ou outra superfície não deve:

- redefinir fórmula no componente visual;
- preencher `UNRESOLVED` por inferência;
- promover `proposed` ou `source_pending` a KPI canônico implementado;
- converter ausência/supressão/atraso em zero;
- ampliar acesso por filtro, drill-down ou exportação;
- consumir contrato sem registrar sua versão.

## 12. Definition of Ready do contrato

Antes de promover para `defined`:

```text
[ ] finalidade fechada
[ ] população/unidade de análise fechadas
[ ] fórmula fechada
[ ] numerador/denominador fechados quando aplicáveis
[ ] inclusões/exclusões fechadas
[ ] temporalidade fechada
[ ] dimensões/filtros fechados
[ ] access/disclosure/drill-down/export fechados
[ ] source of truth definida
[ ] freshness e quality definidos
[ ] null/zero definidos
[ ] proveniência definida
[ ] claims e validações definidos
[ ] domain contracts satisfeitos
[ ] blockers semânticos = 0
```

Antes de `READY_FOR_BUILD`, aplicar também os gates do master global e do master especializado.

## 13. Estado final

```text
GKR-INTELLIGENCE-KPI-CONTRACT-001
→ v0.1.0
→ ACTIVE
→ GOVERNED PRE-IMPLEMENTATION KPI CONTRACT STANDARD

REAL DATA / API / BACKEND / TECHNICAL RBAC
→ NOT AUTHORIZED

REPLIT BUILD
→ NOT AUTHORIZED

NEXT GOVERNED APPLICATION
→ DASHBOARD GUIVOS KPI REGISTRY + INDIVIDUAL CONTRACT RECORDS
```