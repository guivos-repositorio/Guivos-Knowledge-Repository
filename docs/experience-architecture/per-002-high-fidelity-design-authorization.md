---
id: GKR-UX-PER002-HIFI-AUTH-001
title: PER-002 — Autorização Governada de Design High-Fidelity
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-09
normative: true
maturity: high_fidelity_design_authorized_pre_execution
depends_on:
  - GKR-UX-PER002-HIFI-ELIGIBILITY-001
  - GKR-UX-PER002-DESIGN-VALIDATION-001
  - GKR-UX-PER002-DESIGN-DELIVERY-001
  - GKR-UX-PER002-MAT-ELIGIBILITY-001
related:
  - GKR-STATE-001
  - PER-002
  - PER-003
  - TRN-001
  - TRN-002
---

# PER-002 — Autorização Governada de Design High-Fidelity

## 1. Decisão

A elegibilidade pós-validação de `PER-002` foi adjudicada como `PASS` por `GKR-UX-PER002-HIFI-ELIGIBILITY-001 v1.0.0`.

Este ato registra a decisão explícita subsequente:

```text
PER-002 HIGH-FIDELITY DESIGN AUTHORIZATION
→ GRANTED

AUTHORIZED TARGET
→ PER-002 — ENTRADA PROTEGIDA

AUTHORIZED NATURE
→ HIGH-FIDELITY VISUAL REFINEMENT
→ EXISTING RESPONSIBILITY ONLY

HIGH-FIDELITY DESIGN EXECUTION
→ NOT_STARTED
```

A autorização concede permissão para um ato posterior de execução de Design high-fidelity. Ela não executa a entrega neste mesmo checkpoint.

## 2. Referência obrigatória de entrada

O refinamento high-fidelity deve partir de:

```text
CURRENT FUNCTIONALLY VALIDATED LOW-FIDELITY DESIGN REFERENCE
→ GKR-UX-PER002-DESIGN-DELIVERY-001 v0.1.0
+
→ GKR-UX-PER002-DESIGN-VALIDATION-001 v1.0.0

FUNCTIONAL BOUNDARY
→ GKR-UX-PER002-MAT-ELIGIBILITY-001 / FROZEN

HIGH-FIDELITY ELIGIBILITY
→ GKR-UX-PER002-HIFI-ELIGIBILITY-001 v1.0.0 / PASS
```

Em qualquer tensão:

```text
CURRENT FUNCTIONAL AUTHORITY
→ PREVAILS

VALIDATED LOW-FIDELITY REFERENCE
→ GUIDES VISUAL REFINEMENT
→ DOES NOT OVERRIDE FUNCTIONAL AUTHORITY

HISTORICAL REMOVED WIREFRAME / SVG
→ PROVENANCE ONLY
→ NOT CURRENT VISUAL SOURCE OF TRUTH
```

## 3. Escopo autorizado

Design high-fidelity pode refinar visualmente os estados e variantes já materializados de `PER-002`, incluindo:

- hierarquia visual;
- aplicação do sistema visual/brand system vigente;
- tipografia;
- cor;
- iconografia;
- spacing e grid;
- componentes de Design System existentes ou legitimamente aplicáveis;
- composição responsiva;
- estados de foco e feedback visual;
- tratamento visual de erro, recuperação, restrição, sessão e saída;
- refinamento de working copy em coordenação com UX Writing/Marca;
- affordances e clareza visual necessárias à inspeção de UI;
- consistência entre os quatro frames principais e as três variantes já validadas.

A composição pode ser refinada visualmente, mas a cobertura funcional validada deve permanecer íntegra.

## 4. Boundary funcional imutável neste ato

```text
AUTHENTICATION
→ INTERNAL GATE / STATE WITHIN PER-002

AUTHENTICATION COMPLETED
≠ PER-002 COMPLETED

LOGIN / ACCOUNT CREATION
≠ MATERIAL PROCESSING AUTHORIZATION

EXISTING-RELATIONSHIP LOGIN
→ RESUMPTIVE PATH
→ NOT FORCED INTO FIRST-ENTRY ONBOARDING

PER-003
→ DOWNSTREAM HANDOFF ONLY
→ NOT ABSORBED INTO PER-002

PER-008
→ DOWNSTREAM

NEW SURFACE / NEW PER-ID
→ NOT AUTHORIZED BY THIS ACT
```

High-fidelity não pode transformar decisão estética, componente, layout ou copy em nova arquitetura funcional sem novo ato governado específico.

## 5. Cobertura funcional a preservar

O refinamento deve continuar tornando inspecionáveis as sete áreas já validadas:

1. orientação protegida / pré-auth;
2. autenticação quando necessária;
3. sessão já autenticada;
4. continuação autenticada de `PER-002`;
5. recuperação / restrição / falha;
6. voltar / interromper / não prosseguir / alternativa aplicável;
7. condição de handoff legítimo para `PER-003`.

```text
HIGH-FIDELITY REFINEMENT
→ MAY CHANGE VISUAL TREATMENT
→ MUST PRESERVE VALIDATED FUNCTIONAL COVERAGE
```

## 6. Notas anti-regressão obrigatórias

### N1 — compreensão

O refinamento visual não pode transformar exposição em evidência de compreensão.

```text
DISPLAYED
≠ UNDERSTOOD

SCROLLED
≠ UNDERSTOOD

TIME ON SCREEN
≠ UNDERSTOOD

AUTHENTICATED
≠ UNDERSTOOD
```

Qualquer representação de “compreendido”, “pronto” ou equivalente deve depender de um estado/ação coerente com o contrato vigente e não de inferência silenciosa de UI.

### N2 — finalidades

```text
GENERIC PURPOSE EXPLANATION
≠ FUTURE PROCESSING AUTHORIZATION

EACH MATERIAL USE
→ APPLICABLE PURPOSE DISCLOSURE
→ APPLICABLE CONTROL / AUTHORIZATION
→ BEFORE CORRESPONDING MATERIAL PROCESSING
```

A etapa high-fidelity não pode ampliar autorização de dados, coleta ou processamento por copy, checkbox, padrão visual ou conveniência de interface.

## 7. Autonomia, reversibilidade e não coerção

Devem permanecer perceptíveis e acionáveis, conforme o estado aplicável:

- voltar;
- interromper;
- não prosseguir;
- recuperar acesso;
- compreender por que autenticação é necessária;
- distinguir autenticação de autorização de processamento;
- acessar alternativa sem personalização material quando aplicável;
- prosseguir para `PER-003` somente depois de condição legítima de handoff.

```text
HIGH-FIDELITY
≠ DARK PATTERN AUTHORIZATION
≠ COERCION AUTHORIZATION
≠ DEFAULT CONSENT AUTHORIZATION
```

## 8. Source Lock

A autorização high-fidelity **não cria nem exige Source Lock por inferência**.

```text
SOURCE LOCK
→ NOT_CREATED
→ NOT_AUTHORIZED BY INFERENCE

HIGH-FIDELITY AUTHORIZATION
≠ SOURCE LOCK AUTHORIZATION
```

Se um Source Lock visual se tornar necessário por finalidade concreta de congelamento, seu propósito, escopo e autoridade deverão ser adjudicados separadamente.

## 9. Protótipo

```text
INTERACTIVE PROTOTYPE
→ NOT_AUTHORIZED
→ NOT_STARTED
→ REQUIRES SEPARATE GOVERNED GATE

HIGH-FIDELITY DESIGN
≠ INTERACTIVE PROTOTYPE
```

A autorização não libera comportamento executável, fluxo clicável final, tecnologia de autenticação, backend, sessão real ou integração.

## 10. UXA-102/V5 e Product Engineering

```text
UXA-102 / V5
→ NOT_STARTED
→ UNCHANGED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01
→ UNCHANGED

HIGH-FIDELITY DESIGN AUTHORIZATION
≠ UXA-102 RELEASE
≠ PRODUCT ENGINEERING RELEASE
```

## 11. Transições

```text
TRN-001
→ PARTIAL / UNCHANGED

TRN-002
→ LOCALLY VALIDATED / UNCHANGED

HIGH-FIDELITY DESIGN AUTHORIZATION
≠ TRANSITION MATURITY PROMOTION
```

Nenhuma transição recebe promoção por refinamento visual.

## 12. Evidência histórica

```text
UXA-034
→ HISTORICAL PRODUCER REMOVED
→ FUNCTIONAL / DOCUMENTARY PROVENANCE MAY INFORM
→ MUST NOT BE RESTORED OR COPIED AS CURRENT VISUAL BASELINE

UXA-035
→ ANTI-REGRESSION / FUNCTIONAL EVIDENCE MAY INFORM VALIDATION
→ DOES NOT DEFINE CURRENT APPEARANCE
```

Os SVGs removidos continuam removidos.

## 13. Limites explícitos

Este ato não autoriza:

- nova superfície ou novo `PER-ID`;
- expansão funcional de `PER-002`;
- materialização detalhada de `PER-003`;
- materialização de `PER-008`;
- Design das Homes;
- protótipo interativo;
- Source Lock visual;
- UXA-102/V5;
- Product Engineering;
- implementação;
- produção;
- operação;
- alteração de `TRN-001` ou `TRN-002`;
- merge da PR #363.

## 14. Estado após a autorização

```text
HIGH-FIDELITY DESIGN ELIGIBILITY
→ PASS

HIGH-FIDELITY DESIGN AUTHORIZATION
→ GRANTED

HIGH-FIDELITY DESIGN EXECUTION
→ NOT_STARTED

INTERACTIVE PROTOTYPE
→ NOT_AUTHORIZED

SOURCE LOCK
→ NOT_CREATED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01
```

## 15. Próximo gate

O próximo movimento legítimo é uma execução separada de Design:

```text
PER-002 HIGH-FIDELITY DESIGN EXECUTION
→ AUTHORIZED
→ NOT_STARTED

MUST CONSUME
→ VALIDATED LOW-FIDELITY REFERENCE
→ FROZEN FUNCTIONAL BOUNDARY
→ N1 / N2
→ CURRENT BRAND / DESIGN AUTHORITIES APPLICABLE

DO NOT
→ CREATE PROTOTYPE
→ CREATE SOURCE LOCK BY INFERENCE
→ START UXA-102/V5
→ EXPAND TO PER-003
→ RESUME PRODUCT ENGINEERING
→ IMPLEMENT
→ MERGE PR #363
```

A execução posterior deverá produzir sua própria entrega e permanecer sujeita a validação governada antes de qualquer promoção adicional.