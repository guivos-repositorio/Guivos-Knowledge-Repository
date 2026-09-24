---
id: GKR-UX-PER002-MAT-ELIGIBILITY-001
title: PER-002 — Boundary Funcional Corrente
status: active
version: 2.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-20
normative: true
maturity: current_functional_boundary
depends_on:
  - GKR-UX-HOME-MASTER-001
  - UXA-020
  - UXA-023
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-UX-PER002-PROTOTYPE-DELIVERY-001
  - GKR-UX-PER002-PROTOTYPE-REVALIDATION-001
  - PER-001
  - PER-002
  - PER-003
  - PER-008
  - TRN-001
  - TRN-002
---

# PER-002 — Boundary Funcional Corrente

## 1. Finalidade

Esta autoridade define o **boundary funcional corrente** de `PER-002 — Entrada protegida`, primeira responsabilidade autenticada da Jornada da Pessoa após a Home pública.

Ela substitui a necessidade de reconstruir eligibility, autorizações de Design e estágios intermediários de fidelidade para compreender o que `PER-002` significa hoje.

```text
PER-001 — HOME PÚBLICA
→ decisão consciente de iniciar
→ PER-002 — ENTRADA PROTEGIDA
→ TRN-002
→ PER-003 — ESCOLHA DE MODALIDADE
```

## 2. Responsabilidade

`PER-002` é **uma única responsabilidade**, mesmo quando Design usa estados ou variantes visualmente distintos.

Ela deve permitir que a Pessoa:

1. compreenda que está saindo do ambiente público e entrando em contexto protegido;
2. encontre autenticação quando necessária;
3. prossiga corretamente quando a sessão já estiver autenticada;
4. compreenda finalidades e controles aplicáveis antes de processamento material;
5. encontre recuperação, restrição ou falha sem coerção;
6. volte, interrompa ou não prossiga;
7. alcance `PER-003` somente por handoff legítimo.

## 3. Estados funcionais internos

```text
PER-002
├── orientação protegida / pré-auth
├── autenticação quando necessária
├── sessão já autenticada
├── continuação autenticada / controles
├── recuperação / restrição / falha
├── alternativas de saída / interrupção
└── handoff ready
    ↓
  TRN-002
    ↓
  PER-003
```

Esses estados não criam novos `PER-ID`.

## 4. Autenticação

```text
AUTHENTICATION
→ INTERNAL GATE / STATE WITHIN PER-002

AUTHENTICATION COMPLETED
≠ PER-002 COMPLETED

LOGIN / ACCOUNT CREATION
≠ MATERIAL PROCESSING AUTHORIZATION
```

Uma sessão já autenticada pode satisfazer o gate de autenticação sem eliminar responsabilidades restantes de orientação, finalidade, privacidade, controles ou handoff.

## 5. Primeira entrada × relação existente

```text
NOVA ENTRADA
HOME
→ PER-002
→ PER-003
→ continuidade da Journey

RELAÇÃO EXISTENTE
HOME
→ LOGIN
→ AUTHENTICATION
→ RETOMADA DO ESTADO LEGÍTIMO
```

A rota de login de relação existente é resumptiva e não força onboarding de primeira entrada.

## 6. Invariantes

```text
DISPLAYED
≠ UNDERSTOOD

CLICKED
≠ UNDERSTOOD

AUTHENTICATED
≠ UNDERSTOOD

GENERIC PURPOSE EXPLANATION
≠ FUTURE PROCESSING AUTHORIZATION

PROTOTYPE INTERACTION
≠ REAL CONSENT
≠ REAL DATA AUTHORIZATION
```

Cada uso material futuro continua dependente de finalidade, disclosure, controle e autoridade aplicáveis.

## 7. Autonomia e reversibilidade

A experiência deve preservar, quando aplicável:

- voltar;
- interromper;
- não prosseguir;
- recuperar acesso;
- sair;
- explorar sem personalização;
- retomar estado legítimo.

Nenhuma alternativa pode ser subordinada por coerção visual ou dark pattern.

## 8. Dados e tecnologia

Este boundary não escolhe nem prova:

- e-mail, telefone, username, senha, passkey ou biometria;
- provedor de identidade;
- backend;
- sessão real;
- storage;
- API;
- persistência;
- telemetria;
- analytics;
- arquitetura técnica de autorização.

## 9. Estado corrente

```text
PER-002 FUNCTIONAL BOUNDARY
→ CURRENT / FROZEN

CURRENT INTERACTIVE DESIGN REFERENCE
→ GKR-UX-PER002-PROTOTYPE-DELIVERY-001 v1.0.0

CURRENT VALIDATION
→ GKR-UX-PER002-PROTOTYPE-REVALIDATION-001 v2.0.0
→ PASS

TRN-001
→ PARTIAL / UNCHANGED

TRN-002
→ LOCALLY VALIDATED / UNCHANGED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```
