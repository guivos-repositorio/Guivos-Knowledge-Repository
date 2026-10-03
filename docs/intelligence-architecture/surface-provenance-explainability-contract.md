---
id: GKR-INTELLIGENCE-SURFACE-PROVENANCE-EXPLAINABILITY-001
title: Intelligence — Contrato Transversal de Proveniência e Explicabilidade por Superfície
status: active
version: 1.0.0
owner: Guivos Intelligence Architecture
last_updated: 2026-10-03
normative: true
maturity: semantic_cross_surface_contract
depends_on:
  - GPA-006
  - GKR-INTELLIGENCE-KPI-CONTRACT-001
  - GKR-INTELLIGENCE-DASHBOARD-KPI-001
related:
  - GAI-001
  - GAI-002
  - GPA-SPECIALIZED-JOURNEY-MATRIX-001
---

# Intelligence — Contrato Transversal de Proveniência e Explicabilidade por Superfície

## 1. Finalidade

Uniformizar o envelope semântico mínimo de proveniência e explicabilidade para superfícies que consumam outputs do Guivos Intelligence, sem definir implementação, mecanismo técnico de serving ou política operacional final.

Este ato fecha `SP-GAP-005` no nível contratual transversal.

## 2. Regra central

```text
INTELLIGENCE OUTPUT
→ MUST PRESERVE MEANING
→ MUST PRESERVE AUTHORITY
→ MUST PRESERVE PROVENANCE WHEN MATERIAL
→ MUST PRESERVE EXPLAINABILITY PROPORTIONAL TO IMPACT

SURFACE
≠ SOURCE OF TRUTH

OUTPUT
≠ RAW DATASET

OBSERVED
≠ CALCULATED
≠ INTERPRETED
≠ ESTIMATED
≠ PREDICTED
≠ SUGGESTED
```

## 3. Envelope mínimo por superfície

Quando material ao output exibido, a superfície consumidora deve conseguir preservar ou referenciar:

| Dimensão | Contrato mínimo |
|---|---|
| output | natureza do que está sendo entregue |
| source / source of truth | origem autorizada ou estado `SOURCE_PENDING` quando ainda não fechada |
| evidence nature | declarada, observada, operacional, calculada, inferida, predita, estimada, proxy ou equivalente governado |
| provenance | origem e cadeia relevante de transformação |
| authority | quem pode produzir, consumir, corrigir, contestar ou decidir |
| explanation | base, motivo e interpretação proporcional ao impacto |
| uncertainty | incerteza material, intervalo ou qualificação quando aplicável |
| limitation | o que o output não significa ou não permite concluir |
| version / time | versão, temporalidade ou regra de atualização quando material |
| serving context | consumidor/superfície e finalidade autorizada |

## 4. Profundidade proporcional

Nem toda superfície precisa expor todos os campos com a mesma profundidade visual.

```text
LOWER IMPACT
→ LIGHTWEIGHT EXPLANATION MAY BE SUFFICIENT

HIGHER IMPACT
→ STRONGER PROVENANCE + EXPLANATION + UNCERTAINTY + LIMITATION
```

A profundidade deve crescer conforme risco de interpretação, consequência, incerteza e distância entre observação e inferência.

## 5. Autoridade da superfície

A superfície anfitriã não se torna fonte de verdade apenas porque exibe um output do Intelligence.

```text
DASHBOARD / UI / REPORT / API / CHAT
→ CONSUMER
→ NOT AUTOMATIC SOURCE OF TRUTH
```

A autoridade final permanece com os contratos de domínio e com o participante/produto competente.

## 6. Separação entre personalizar e compartilhar

```text
AUTHORITY TO PERSONALIZE
≠ AUTHORITY TO SHARE
```

O fato de o Intelligence poder usar determinado contexto para servir legitimamente uma Pessoa não autoriza expor esse contexto a Organização, Business, Ads ou terceiro.

## 7. Silêncio legítimo

Ausência de evidência suficiente pode resultar em ausência legítima de insight, recomendação, previsão ou explicação conclusiva.

```text
INSUFFICIENT EVIDENCE
→ DO NOT FABRICATE CERTAINTY
```

## 8. Correção e contestabilidade

Quando material, a experiência deve preservar:

- possibilidade de corrigir fonte ou dado legitimamente corrigível;
- possibilidade de contestar interpretação ou output quando aplicável;
- distinção entre erro de dado, erro de cálculo, inferência e discordância legítima;
- reprocessamento/reconciliação somente dentro da autoridade aplicável.

## 9. Não inferências

Este contrato não define:

- modelo operacional de proveniência;
- storage de lineage;
- serving técnico;
- API;
- data contract físico;
- feature store;
- observabilidade;
- modelo ou fornecedor de IA;
- thresholds de confiança;
- UI final;
- implementação;
- Product Engineering.

## 10. Relação com KPI Contracts

KPIs permanecem subordinados a `GKR-INTELLIGENCE-KPI-CONTRACT-001`.

Este contrato transversal não substitui o KPI Contract Record; ele estabelece o envelope mínimo que qualquer superfície consumidora deve preservar quando o output exigir proveniência/explicabilidade.

## 11. Estado de SP-GAP-005

```text
SP-GAP-005
→ SEMANTIC CROSS-SURFACE CONTRACT CLOSED

OPERATIONAL PROVENANCE MODEL
→ STILL OPEN

OPERATIONAL EXPLAINABILITY CONTRACT
→ STILL OPEN

TECHNICAL SERVING
→ STILL OPEN

IMPLEMENTATION
→ NOT AUTHORIZED
```

## 12. Estado

```text
CROSS-SURFACE PROVENANCE / EXPLAINABILITY
→ CONTRACTED

NEW SURFACES
→ 0

NEW TRANSITIONS
→ 0

PRODUCT ENGINEERING
→ NOT RELEASED
```
