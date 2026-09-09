---
id: GKR-UX-PER002-DESIGN-AUTH-001
title: PER-002 — Autorização Governada de Design Low-Fidelity
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-09-09
normative: true
maturity: design_low_fidelity_authorized_pre_execution
depends_on:
  - GKR-UX-PER002-MAT-ELIGIBILITY-001
  - GKR-UX-HOME-MASTER-001
  - UXA-020
  - UXA-023
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-STATE-001
  - PER-001
  - PER-002
  - PER-003
  - PER-008
  - TRN-001
  - TRN-002
---

# PER-002 — Autorização Governada de Design Low-Fidelity

## 1. Finalidade

Esta autoridade registra a decisão governada explícita de liberar **Design low-fidelity funcional exclusivamente para `PER-002 — Entrada protegida`**, usando como boundary obrigatório `GKR-UX-PER002-MAT-ELIGIBILITY-001`.

Ela autoriza o início da materialização de Design; ela **não executa** a materialização neste documento e não promove qualquer maturidade funcional, técnica ou operacional.

```text
MATERIALIZATION ELIGIBILITY
→ PASS / CANONICALLY CONSOLIDATED

DESIGN HANDOFF BOUNDARY
→ GKR-UX-PER002-MAT-ELIGIBILITY-001 / FROZEN

DESIGN AUTHORIZATION
→ GRANTED

DESIGN EXECUTION
→ NOT_STARTED AT THIS DECISION RECORD
```

## 2. Decisão canônica

```text
PER-002 LOW-FIDELITY DESIGN AUTHORIZATION
→ GRANTED

AUTHORIZED TARGET
→ PER-002 — ENTRADA PROTEGIDA

AUTHORIZED NATURE
→ LOW-FIDELITY
→ FUNCTIONAL MATERIALIZATION
→ EXISTING RESPONSIBILITY ONLY

NEW SURFACE
→ NO

NEW PER-ID
→ NO

HISTORICAL VISUAL RESTORATION
→ NOT AUTHORIZED
```

A autorização existe porque a responsabilidade, os estados mínimos, entradas, saídas, controles, alternativas e handoff já estão funcionalmente definidos. Design não é autorizado a redescobrir ou redefinir a responsabilidade; é autorizado a **materializá-la visualmente em baixa fidelidade para inspeção**.

## 3. Autoridades de entrada obrigatórias

Design deve consumir, no mínimo:

1. `GKR-UX-PER002-MAT-ELIGIBILITY-001` — boundary funcional congelado;
2. `GKR-UX-HOME-MASTER-001` — fronteira pública e origem da Journey;
3. `UXA-020` — relação Home × entrada protegida × continuidade;
4. `UXA-023` — contrato funcional validado da entrada protegida;
5. registries vigentes de superfícies e transições da Pessoa.

Em caso de tensão entre aparência histórica e autoridade funcional corrente:

```text
CURRENT FUNCTIONAL AUTHORITY
→ PREVAILS

HISTORICAL WIREFRAME / SVG / PRODUCER
→ PROVENANCE ONLY
→ NOT VISUAL SOURCE OF TRUTH
```

## 4. Escopo autorizado

Design pode decidir **como** representar visualmente os estados/variantes necessários de `PER-002`, incluindo:

- quantidade de views necessárias;
- agrupamento ou separação de estados;
- progressive disclosure;
- hierarquia visual;
- composição de conteúdo e controles;
- comportamento responsivo low-fidelity;
- representação de estados condicionais;
- tratamento visual de erro, recuperação, retorno e interrupção;
- forma de tornar a condição de `HANDOFF READY` compreensível.

Essas decisões pertencem à autoridade visual de Design, desde que preservem o contrato funcional.

```text
FUNCTIONAL AUTHORITY
→ EXPERIENCE ARCHITECTURE / CURRENT TEXTUAL CANON

VISUAL AUTHORITY
→ DESIGN

VISUAL FREEDOM
→ WITHIN THE FROZEN FUNCTIONAL BOUNDARY
```

## 5. Cobertura mínima obrigatória

A primeira entrega low-fidelity deve tornar inspecionável, conforme o estado aplicável:

1. orientação protegida / pré-auth;
2. gate de autenticação quando necessário;
3. variante de sessão já autenticada;
4. continuação autenticada de `PER-002`;
5. acesso, recuperação, restrição ou falha;
6. voltar, interromper, não prosseguir e alternativa sem personalização material quando aplicável;
7. condição de handoff legítimo para `PER-003`.

Essa lista define **cobertura funcional**, não número obrigatório de telas.

## 6. Invariantes obrigatórios

A materialização deve preservar:

```text
AUTHENTICATION
→ INTERNAL GATE / STATE WITHIN PER-002

AUTHENTICATION COMPLETED
≠ PER-002 COMPLETED

LOGIN / ACCOUNT CREATION
≠ MATERIAL PROCESSING AUTHORIZATION

PER-003
→ DOWNSTREAM HANDOFF DESTINATION
→ NOT ABSORBED INTO PER-002

PER-008 / TELA HOJE
→ DOWNSTREAM
→ NOT FIRST AUTHENTICATED RESPONSIBILITY

EXISTING-RELATIONSHIP LOGIN
→ RESUMPTIVE PATH
→ NOT FORCED INTO FIRST-ENTRY ONBOARDING
```

Também permanecem obrigatórios autonomia, reversibilidade, clareza de finalidade, privacidade proporcional, não coerção, ausência de coleta automática e separação entre autenticação e autorização de processamento material.

## 7. Limites explícitos da autorização

Esta decisão **não autoriza**:

- materialização detalhada de `PER-003 — Escolha de modalidade`;
- materialização de `PER-008 — Tela Hoje` sob Q;
- nova superfície ou novo `PER-ID`;
- `UXA-102/V5`;
- restauração de `UXA-034` ou dos SVGs removidos;
- criação automática de Source Lock visual;
- high-fidelity UI;
- protótipo interativo;
- implementação;
- Product Engineering;
- produção;
- operação;
- alteração da maturidade de `TRN-001` ou `TRN-002`;
- materialização das Homes públicas, de O/C ou dos Produtos Especializados;
- merge da PR #363.

```text
PER-002 LOW-FIDELITY DESIGN AUTHORIZED
≠ ALL DESIGN AUTHORIZED
≠ HOME DESIGN AUTHORIZED
≠ PROTOTYPE AUTHORIZED
≠ IMPLEMENTATION AUTHORIZED
```

## 8. Tratamento da evidência histórica

Os produtores e SVGs removidos por `F-016/F-016-A` não devem ser restaurados como baseline visual.

```text
UXA-034
→ HISTORICAL PRODUCER REMOVED
→ MAY INFORM PROVENANCE
→ MUST NOT GOVERN CURRENT VISUAL SOLUTION

UXA-035
→ FUNCTIONAL / ANTI-REGRESSION EVIDENCE MAY INFORM VALIDATION
→ DOES NOT DEFINE CURRENT APPEARANCE

OLD FOUR-STATE PACKAGE
→ MAY INFORM FUNCTIONAL RISKS
→ MUST NOT BE COPIED AS A WHOLE
```

Design deve partir das autoridades funcionais correntes e pode chegar a uma composição visual diferente da história, desde que preserve os invariantes autorizados.

## 9. Maturidade preservada

```text
TRN-001
→ PARTIAL / UNCHANGED

TRN-002
→ LOCALLY VALIDATED / UNCHANGED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01

PMF
→ NOT VALIDATED
```

A autorização de Design não é evidência de uso, teste, compreensão real, acessibilidade validada, comportamento real ou prontidão de engenharia.

## 10. Gate após a entrega

Uma entrega low-fidelity futura não será automaticamente aprovada por existir.

```text
DESIGN AUTHORIZATION
→ GRANTED

DESIGN DELIVERY
→ FUTURE EXECUTION

DESIGN DELIVERY
≠ FUNCTIONAL VALIDATION
≠ TRANSITION MATURITY PROMOTION
≠ PROTOTYPE AUTHORIZATION
≠ ENGINEERING HANDOFF
```

Após a materialização, deverá ocorrer uma **validação funcional governada** contra `GKR-UX-PER002-MAT-ELIGIBILITY-001`, `UXA-020`, `UXA-023` e registries vigentes antes de qualquer promoção ou expansão de escopo.

## 11. Próximo ato governado

```text
NEXT
→ EXECUTE LOW-FIDELITY FUNCTIONAL DESIGN MATERIALIZATION OF PER-002
→ CONSUME GKR-UX-PER002-MAT-ELIGIBILITY-001 AS FROZEN BOUNDARY
→ PRESERVE DESIGN AUTHORITY OVER VISUAL FORM
→ PRESERVE EXPERIENCE ARCHITECTURE AUTHORITY OVER FUNCTIONAL CONTRACT

DO NOT
→ START UXA-102/V5
→ MATERIALIZE PER-003 BEYOND HANDOFF
→ RESTORE HISTORICAL PRODUCERS
→ CREATE HIGH-FIDELITY UI / PROTOTYPE
→ RESUME PRODUCT ENGINEERING
→ IMPLEMENT
→ MERGE PR #363
```

Esta decisão conclui o gate de autorização; a execução de Design é o próximo ato e permanece separada deste registro.