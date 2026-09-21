---
id: GKR-UX-ORGCOL-AUTH-WIREFRAME-AUTH-001
title: Organizações e Coletivos — Autorização Governada de Wireframes Autenticados Low-Fidelity
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-18
normative: true
maturity: authenticated_low_fidelity_wireframes_authorization_consumed
depends_on:
  - GKR-UX-ORGCOL-AUTH-NAV-MAT-001
  - GKR-UX-ORGCOL-AUTH-NAV-MAT-ELIGIBILITY-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
related:
  - GKR-UX-ORGCOL-UX-STATE-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - UXA-014
  - UXA-019
---

# Organizações e Coletivos — Autorização Governada de Wireframes Autenticados Low-Fidelity

## 1. Finalidade

Esta autoridade registra a decisão humana explícita de liberar **wireframes autenticados low-fidelity de Organização e Coletivo**, usando como boundary obrigatório a Navigation Materialization canônica:

```text
GKR-UX-ORGCOL-AUTH-NAV-MAT-001
→ v1.0.0
→ ACTIVE
→ DEFINED / CANONICAL DOCUMENTARY
→ PRE-WIREFRAME
→ INTEGRATED INTO MAIN

HUMAN AUTHORIZATION
→ AUTHENTICATED LOW-FIDELITY WIREFRAMES
→ GRANTED
```

A autorização libera somente a materialização visual estrutural de baixa fidelidade necessária para tornar a experiência autenticada O/C inspecionável.

## 2. Decisão canônica

```text
O/C AUTHENTICATED LOW-FIDELITY WIREFRAME AUTHORIZATION
→ GRANTED

AUTHORIZED TARGETS
→ ORGANIZATION AUTHENTICATED EXPERIENCE
→ COLLECTIVE AUTHENTICATED EXPERIENCE

AUTHORIZED NATURE
→ LOW-FIDELITY
→ FUNCTIONAL / STRUCTURAL
→ PRE-UI
→ PRE-PROTOTYPE

CURRENT FUNCTIONAL BOUNDARY
→ GKR-UX-ORGCOL-AUTH-NAV-MAT-001 v1.0.0
```

Design pode decidir a composição low-fidelity necessária, mas não redefinir identidades, autoridade, surfaces, transitions ou lifecycle.

## 3. Autoridades obrigatórias

A entrega deve consumir cumulativamente:

1. `GKR-UX-ORGCOL-AUTH-JOBS-001`;
2. `GKR-UX-ORGCOL-AUTH-IA-001`;
3. `GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001`;
4. `GKR-UX-ORGCOL-AUTH-STATE-MAP-001`;
5. `GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001`;
6. `GKR-UX-ORGCOL-AUTH-NAV-MAT-ELIGIBILITY-001`;
7. `GKR-UX-ORGCOL-AUTH-NAV-MAT-001`;
8. Surface Registry e Transition Registry vigentes;
9. `UXA-019` apenas para Organização ↔ Coletivo.

## 4. Escopo autorizado

A materialização low-fidelity pode decidir:

- shell visual funcional;
- hierarquia aparente L0–L4;
- posição relativa de contexto, navegação, Momento, atenção e Próximos Passos;
- forma low-fidelity de alternar contexto;
- agrupamento visual dos domínios já canônicos;
- representação low-fidelity de destination-backed, state-resolved, shared-surface e contextual-only;
- tratamento low-fidelity de estados alternativos;
- affordances de retorno, interrupção e revalidação;
- acesso contextual a Planos e demais capacidades especializadas quando justificadas;
- comportamento estrutural mobile-first e adaptação desktop conceitual.

Essas decisões são **propostas de Design low-fidelity**, não UI final.

## 5. Cobertura mínima obrigatória

A primeira entrega deve tornar inspecionável, no mínimo:

### Organização

1. contexto ativo, unidade/papel e autoridade;
2. `ORG-001` como anchor;
3. Oportunidades e Programas;
4. Relações O↔C;
5. Responsabilidades e Evidências;
6. Organização e Autoridade como contexto, sem superfície inventada;
7. Planos como capacidade especializada/contextual;
8. Momento, atenção material e Próximos Passos;
9. estado regular;
10. estado de atenção/risco/obrigação;
11. autoridade insuficiente ou responsável ausente.

### Coletivo

1. contexto ativo, papel e governança;
2. `COL-002` como anchor;
3. Atividades e Oportunidades;
4. Participação;
5. Governança e Proteção;
6. Relações O↔C;
7. Aprendizados e Evidências como contextual-only;
8. Planos como capacidade especializada/contextual;
9. estado regular;
10. estado de participação/governança/proteção que exija atenção;
11. autoridade insuficiente ou responsável ausente.

### Compartilhado

1. troca explícita de contexto;
2. revalidação de autoridade;
3. informação protegida;
4. contestação;
5. indisponibilidade técnica;
6. contexto expirado;
7. retorno sem mutação silenciosa;
8. busca/notificação como mecanismo de acesso, não domínio.

## 6. Invariantes obrigatórios

```text
VISIBLE
≠ AUTHORIZED

NAVIGABLE
≠ EFFECTIVE

CLICK
≠ CONFIRMATION

RETURN
≠ AUTOMATIC UNDO

CONTEXT SWITCH
≠ AUTHORITY TRANSFER

NAVIGATION PATH
≠ GKR-TRN

WIREFRAME NODE
≠ NEW GKR-SURF
```

Também permanecem obrigatórios:

- `ORG-001` e `COL-002` como anchors;
- O↔O e C↔C continuam gaps;
- `ORG-004..006` e `COL-008` continuam restritos a O↔C;
- `COL-003 → COL-004` continua sem novo transition ID;
- Planos não vira eixo principal;
- Intelligence não vira autoridade decisória;
- nenhum produto especializado ganha destaque estrutural por razões comerciais;
- contexto pessoal protegido não é exposto a O/C por navegação.

## 7. Tratamento dos artefatos históricos

`UXA-015..018` e SVGs removidos permanecem somente proveniência histórica.

```text
HISTORICAL WIREFRAMES
→ MAY INFORM RISKS / COVERAGE
→ MUST NOT GOVERN CURRENT VISUAL SOLUTION
→ MUST NOT BE RESTORED AS BASELINE
```

A nova entrega deve partir das autoridades atuais e pode chegar a composição diferente.

## 8. Limites explícitos

Esta autorização **não autoriza**:

- high-fidelity UI;
- identidade visual final;
- Design System global;
- copy final;
- protótipo interativo;
- pesquisa com participantes reais;
- implementação;
- URL/rotas técnicas;
- RBAC técnico;
- novo `GKR-SURF-*`;
- novo `GKR-TRN-*`;
- promoção de maturidade de transition;
- O↔O ou C↔C por analogia;
- `UXA-102/V5`;
- Product Engineering;
- produção.

```text
LOW-FIDELITY WIREFRAME AUTHORIZATION
≠ FUNCTIONAL VALIDATION
≠ HIGH-FIDELITY AUTHORIZATION
≠ PROTOTYPE AUTHORIZATION
≠ ENGINEERING RELEASE
```

## 9. Forma de entrega autorizada

A primeira entrega pode usar representação monoespaçada estrutural, conforme precedente governado de `PER-002`.

```text
ASCII / MONOSPACED LOW-FIDELITY
→ VALID DELIVERY FORM

SVG / FIGMA / PNG
→ NOT REQUIRED FOR THIS FIRST DELIVERY

PHYSICAL SVG COUNT
→ MAY REMAIN 0
```

Isso não reduz o requisito de hierarquia visual inspecionável.

## 10. Gate após a entrega

Uma entrega não será considerada validada por existir.

```text
AUTHORIZATION
→ GRANTED

LOW-FIDELITY DELIVERY
→ MAY EXECUTE

FUNCTIONAL VALIDATION
→ SEPARATE GOVERNED ACT

CANONICAL VISUAL REFERENCE
→ ONLY AFTER VALIDATION
```

A validação deverá confrontar a entrega com Navigation Materialization, State Map, Priority Flows, registries e estados absorvidos de UXA-015..018.

## 11. Estado governado

```text
GKR-UX-ORGCOL-AUTH-WIREFRAME-AUTH-001
→ v1.0.0
→ ACTIVE / NORMATIVE

LOW-FIDELITY WIREFRAME AUTHORIZATION
→ GRANTED

LOW-FIDELITY DELIVERY
→ AUTHORIZED TO EXECUTE

FUNCTIONAL VALIDATION
→ NOT YET PERFORMED

HIGH-FIDELITY UI
→ NOT AUTHORIZED

PROTOTYPE
→ NOT AUTHORIZED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01 / NOT RELEASED
```
