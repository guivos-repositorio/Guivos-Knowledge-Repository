---
id: GKR-HOME-MASTERS-REMEDIATION-001
title: Home Masters — Adjudicação de Remediação
status: active
version: 1.1.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-09-13
normative: true
maturity: closure_remediation_adjudication
related:
  - GKR-CHECKPOINT-HOME-MASTERS-PRIORITY-001
  - GKR-UX-SPECIALIZED-HOMES-RECONCILIATION-001
  - GKR-STATE-001
---

# Home Masters — Adjudicação de Remediação

## 1. Escopo

Este documento resolve somente lacunas de inventário, handoff e continuidade temporal identificadas na auditoria C1–C10. Não é Home Master, Product Master, Source Lock, Design ou implementação.

```text
HOME MASTER
→ CANONICAL SEMANTIC / FUNCTIONAL INPUT

HANDOFF AUTHORITY
≠ DESIGN RELEASE
≠ UI APPROVAL
≠ PROTOTYPE AUTHORIZATION
≠ IMPLEMENTATION RELEASE
```

Regra de não invenção: `TBD`, `NOT DEFINED` e `NOT AUTHORIZED` permanecem nesses estados até autoridade própria.

## 2. Inventário canônico da frente

A auditoria repo-wide reconhece exatamente oito Homes com Documento Mestre próprio:

| Home | ID mestre | Path |
|---|---|---|
| Home Pública Principal / Pessoa | `GKR-UX-HOME-MASTER-001` | `docs/experience-architecture/public-home-master-document.md` |
| Home Pública — Organizações e Coletivos | `GKR-UX-HOME-OC-MASTER-001` | `docs/experience-architecture/public-home-organizations-collectives-master-document.md` |
| Guivos Mall | `GKR-UX-HOME-MALL-MASTER-001` | `docs/experience-architecture/public-home-mall-master-document.md` |
| Guivos Travel | `GKR-UX-HOME-TRAVEL-MASTER-001` | `docs/experience-architecture/public-home-travel-master-document.md` |
| Guivos Media | `GKR-UX-HOME-MEDIA-MASTER-001` | `docs/experience-architecture/public-home-media-master-document.md` |
| Guivos Business | `GKR-UX-HOME-BUSINESS-MASTER-001` | `docs/experience-architecture/public-home-business-master-document.md` |
| Guivos Ads | `GKR-UX-HOME-ADS-MASTER-001` | `docs/experience-architecture/public-home-ads-master-document.md` |
| Guivos Intelligence | `GKR-UX-HOME-INTELLIGENCE-MASTER-001` | `docs/experience-architecture/public-home-intelligence-master-document.md` |

Limites:

```text
JOURNEY
→ EXPERIENCE LAYER
→ NOT A NINTH HOME

COMMUNITY
→ NO CURRENT DISTINCT HOME AUTHORITY PROVEN
→ NO MASTER CREATED BY INFERENCE

PUBLIC O/C HOME
≠ AUTHENTICATED O/C EXPERIENCE

PRODUCT MASTER
≠ HOME MASTER
```

A individualização dos oito Masters no `mkdocs.yml` já está comprovada e não exige alteração nesta remediação.

## 3. Mall e Travel

`GKR-UX-HOME-MALL-MASTER-001` e `GKR-UX-HOME-TRAVEL-MASTER-001` permanecem seus Masters canônicos. Seus `status: draft` são sinais históricos de maturidade conforme `GKR-UX-SPECIALIZED-HOMES-RECONCILIATION-001`, não estados correntes inferidos.

Ambos são suficientes como input documental de handoff quando consumidos com as regras deste documento. Nenhum artefato derivado pode inventar disponibilidade, parceiro, preço, regra comercial, personalização, fluxo interno ou materialização não autorizada.

## 4. Business

A frase histórica de `GKR-UX-HOME-BUSINESS-MASTER-001` segundo a qual o Master não é handoff para Design é normalizada para:

```text
BUSINESS MASTER
→ CANONICAL DOCUMENTARY HANDOFF INPUT

HANDOFF
≠ DESIGN AUTHORIZATION
```

A indicação histórica de `SOURCE LOCK → PRÓXIMA ETAPA` não cria gate automático atual. Qualquer Source Lock permanece autoridade separada e depende de ato governado próprio.

A referência histórica de que a Home do Guivos Intelligence ainda não precisava existir foi superada: a Home Intelligence possui Master próprio e Home Source Lock vigente. Business não absorve essa autoridade.

## 5. Intelligence

A afirmação histórica de `GKR-UX-HOME-INTELLIGENCE-MASTER-001` de que o Home Source Lock ainda não havia sido criado está superada.

```text
GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001 v1.0.0
→ ACTIVE / NORMATIVE

MASTER
→ NARRATIVE / SEMANTIC / FUNCTIONAL AUTHORITY

HOME SOURCE LOCK
→ SOURCE PACKAGE / INVARIANT FREEZE WITHIN ITS SCOPE

MASTER
≠ SOURCE LOCK

MASTER + SOURCE LOCK
≠ DESIGN RELEASE
≠ IMPLEMENTATION RELEASE
```

`COMPREENDER ≠ DECIDIR` permanece obrigatório.

## 6. Demais Homes

Nenhuma remediação estrutural adicional é necessária para Pessoa, O/C, Media ou Ads. Snapshots temporais não substituem `GKR-STATE-001` como fonte do estado executivo corrente.

Media e Ads já possuem linguagem suficiente de handoff, aceite e limites. Pessoa e O/C permanecem sem gap arquitetural provado.

## 7. Estado C1–C10 após esta remediação documental

```text
C1 — REPO-WIDE INVENTORY
→ PASS

C2 — MASTER / ID / PATH / VERSION / STATUS / MATURITY
→ PASS FOR DOCUMENTARY CLOSURE SCOPE

C3 — PUBLIC × AUTHENTICATED × OTHER SURFACES
→ PASS

C4 — INDIVIDUALIZATION IN MENU
→ PASS

C5 — HANDOFF SUFFICIENCY
→ PASS FOR DOCUMENTARY CLOSURE SCOPE

C6 — NEW MASTER ONLY IF PROVEN
→ PASS

C7 — AUTHORITY PRECEDENCE
→ PASS

C8 — SEMANTIC + MECHANICAL ON EXACT FINAL HEAD
→ PENDING

C9 — INDEPENDENT GOVERNED REVIEW ON EXACT FINAL HEAD
→ PENDING

C10 — ZERO IMPLEMENTATION INFERENCE
→ PASS
```

Esta adjudicação prevalece somente para o inventário de fechamento, o significado de handoff e os estados temporais explicitamente normalizados acima. Ela não altera a arquitetura semântica dos Masters.

## 8. Estado governado e gates restantes

Base física no início desta remediação:

```text
MAIN
→ 830b3f204a9e8e74aa65f73fb1fc68f5f228fade
```

A PR #365 permanece frente independente em HOLD. No início desta remediação, seu HEAD continuava `3a946a2c2ae840d6ac6f5dba91242479d46db2e5`, divergindo do `main` acima com `ahead_by = 29` e `behind_by = 61`.

O fechamento formal continua condicionado a:

```text
SEMANTIC VALIDATION ON EXACT FINAL HEAD
→ REQUIRED

MECHANICAL VALIDATION ON EXACT FINAL HEAD
→ REQUIRED

INDEPENDENT GOVERNED REVIEW ON EXACT FINAL HEAD
→ REQUIRED

UNTIL CLEAN
→ HOME MASTERS FRONT NOT FORMALLY CLOSED
→ PR #365 REMAINS HOLD
→ DESIGN NOT RELEASED
→ PRODUCT ENGINEERING NOT RELEASED
```
