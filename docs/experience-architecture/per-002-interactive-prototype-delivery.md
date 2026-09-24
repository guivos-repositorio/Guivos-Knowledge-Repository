---
id: GKR-UX-PER002-PROTOTYPE-DELIVERY-001
title: PER-002 — Protótipo Interativo Corrente
status: active
version: 1.0.0
owner: Design Guivos
last_updated: 2026-09-20
normative: false
maturity: current_interactive_design_reference
depends_on:
  - GKR-UX-PER002-MAT-ELIGIBILITY-001
  - GKR-UX-HOME-MASTER-001
  - UXA-020
  - UXA-023
related:
  - GKR-UX-PER002-PROTOTYPE-REVALIDATION-001
  - PER-002
  - PER-003
  - TRN-001
  - TRN-002
---

# PER-002 — Protótipo Interativo Corrente

## 1. Finalidade

Este documento descreve o **artefato interativo corrente de inspeção de Design** de `PER-002 — Entrada protegida`.

A sequência histórica de low-fidelity, high-fidelity, eligibility e autorizações que levou a este artefato pertence ao Git e não é necessária para consumir a referência atual.

## 2. Artefato

```text
ARTIFACT
→ docs/assets/prototypes/per-002-interactive-prototype.html

FORMAT
→ SELF-CONTAINED HTML / CSS / JAVASCRIPT

NATURE
→ DESIGN INSPECTION ARTIFACT
→ SIMULATED INTERACTION ONLY

CONTENT
→ SYNTHETIC / FICTIONAL / DESIGN-SAFE

NETWORK REQUESTS
→ NONE BY DESIGN

BACKEND
→ NONE

PERSISTENCE
→ NONE

ANALYTICS / TELEMETRY
→ NONE
```

O HTML/CSS/JavaScript é meio de prototipação, não decisão de stack de Product Engineering.

## 3. Cobertura

O protótipo representa `PER-002` como uma única responsabilidade com:

```text
4 PRIMARY FRAMES
+
3 VARIANTS
=
7 / 7 FUNCTIONAL COVERAGE AREAS
```

Cobertura:

1. orientação protegida / pré-auth;
2. autenticação quando necessária;
3. sessão já autenticada;
4. continuação autenticada / controles;
5. recuperação / restrição / falha;
6. voltar / interromper / não prosseguir / alternativa aplicável;
7. handoff legítimo para `PER-003`.

```text
7 COVERAGE AREAS
≠ 7 CANONICAL SURFACES
≠ 7 PER-IDs
```

## 4. Fluxo inspecionável

```text
PER-001 — HOME PÚBLICA
        ↓
PER-002 — ORIENTAÇÃO PROTEGIDA
        ↓
autenticação necessária?
   ├── sim → gate de acesso simulado
   └── não → sessão já autenticada simulada
        ↓
CONTINUAÇÃO / CONTROLES
        ↓
HANDOFF READY
        ↓
TRN-002
        ↓
PER-003 — boundary downstream
```

O protótipo não materializa o conteúdo interno de `PER-003`.

## 5. Guardrails preservados

```text
AUTHENTICATION
→ INTERNAL GATE

AUTHENTICATION COMPLETED
≠ PER-002 COMPLETED

LOGIN / ACCOUNT CREATION
≠ MATERIAL PROCESSING AUTHORIZATION

DISPLAYED / CLICKED
≠ UNDERSTOOD

PROTOTYPE CLICK
≠ REAL CONSENT
≠ REAL AUTHORIZATION
```

## 6. Autonomia

São inspecionáveis caminhos para:

- voltar;
- sair por agora;
- interromper;
- recuperar acesso;
- explorar sem personalização quando aplicável;
- continuar conscientemente.

## 7. Referência visual

A aparência deste protótipo é **referência local de Design de PER-002**, não sistema visual global da Guivos.

```text
LOCAL DESIGN DECISIONS
→ PER-002 ONLY

GLOBAL DESIGN SYSTEM
→ NOT CREATED BY THIS ARTIFACT

PUBLIC HOME VISUAL IDENTITY
→ NOT GOVERNED BY THIS ARTIFACT
```

A autoridade funcional prevalece sobre qualquer tratamento visual do protótipo.

## 8. Estado

```text
INTERACTIVE DESIGN REFERENCE
→ CURRENT

VALIDATION
→ GKR-UX-PER002-PROTOTYPE-REVALIDATION-001 v2.0.0
→ PASS

IMPLEMENTED PRODUCT
→ NO

REAL AUTHENTICATION / SESSION / DATA
→ NO

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ NOT RELEASED
```
