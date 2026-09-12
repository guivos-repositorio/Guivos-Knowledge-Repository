---
id: GKR-UX-PER002-PROTOTYPE-AUTH-001
title: PER-002 — Autorização Governada de Protótipo Interativo
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-09-09
normative: true
maturity: interactive_prototype_authorized_pre_execution
depends_on:
  - GKR-UX-PER002-PROTOTYPE-ELIGIBILITY-001
  - GKR-UX-PER002-HIFI-VALIDATION-001
  - GKR-UX-PER002-HIFI-DELIVERY-001
  - GKR-UX-PER002-MAT-ELIGIBILITY-001
  - UXA-020
  - UXA-023
related:
  - GKR-STATE-001
  - PER-002
  - PER-003
  - TRN-001
  - TRN-002
---

# PER-002 — Autorização Governada de Protótipo Interativo

## 1. Finalidade

Esta autoridade registra a decisão explícita sobre a execução de um **protótipo interativo de Design de `PER-002 — Entrada protegida`** após a elegibilidade pós-validação ter concluído `PASS`.

Ela autoriza somente uma execução posterior e separada do protótipo dentro do boundary funcional já congelado e da referência high-fidelity validada.

Ela não executa o protótipo neste mesmo ato e não autoriza Source Lock, UXA-102/V5, Product Engineering, implementação, backend, dados reais, produção, operação ou merge da PR #363.

## 2. Evidência de entrada

```text
PER-002 FUNCTIONAL BOUNDARY
→ GKR-UX-PER002-MAT-ELIGIBILITY-001
→ FROZEN

LOW-FIDELITY
→ AUTHORIZED
→ EXECUTED
→ VALIDATED / PASS

HIGH-FIDELITY
→ ELIGIBILITY PASS
→ AUTHORIZED
→ EXECUTED
→ VALIDATED / PASS

CURRENT FUNCTIONALLY VALIDATED HIGH-FIDELITY DESIGN REFERENCE
→ GKR-UX-PER002-HIFI-DELIVERY-001 v0.1.0
+
→ GKR-UX-PER002-HIFI-VALIDATION-001 v1.0.0

INTERACTIVE PROTOTYPE ELIGIBILITY
→ GKR-UX-PER002-PROTOTYPE-ELIGIBILITY-001 v1.0.0
→ PASS
```

A elegibilidade comprovou que o protótipo pode tornar interativamente inspecionáveis estados já especificados sem redescobrir a arquitetura e sem presumir implementação.

## 3. Decisão

```text
PER-002 INTERACTIVE PROTOTYPE AUTHORIZATION
→ GRANTED

AUTHORIZED TARGET
→ PER-002 — ENTRADA PROTEGIDA

AUTHORIZED NATURE
→ INTERACTIVE DESIGN INSPECTION ARTIFACT
→ SIMULATED INTERACTION ONLY
→ EXISTING RESPONSIBILITY ONLY

INTERACTIVE PROTOTYPE EXECUTION
→ NOT_STARTED
```

A autorização encerra somente o gate decisório.

```text
AUTHORIZATION
≠ EXECUTION
≠ VALIDATION
≠ IMPLEMENTATION
≠ PRODUCTION
```

## 4. Referência obrigatória de execução

Qualquer execução autorizada deverá consumir conjuntamente:

1. `GKR-UX-PER002-PROTOTYPE-ELIGIBILITY-001 v1.0.0`;
2. `GKR-UX-PER002-HIFI-DELIVERY-001 v0.1.0`;
3. `GKR-UX-PER002-HIFI-VALIDATION-001 v1.0.0`;
4. `GKR-UX-PER002-MAT-ELIGIBILITY-001`;
5. `UXA-020`;
6. `UXA-023`;
7. os registries correntes de superfícies e transições da Pessoa.

```text
CURRENT FUNCTIONAL AUTHORITY
→ PREVAILS

VALIDATED HIGH-FIDELITY REFERENCE
→ VISUAL / INTERACTION INPUT
→ NOT FUNCTIONAL AUTHORITY REPLACEMENT
```

## 5. Escopo interativo autorizado

O protótipo poderá tornar inspecionáveis somente os estados e ações já especificados para `PER-002`.

Pode simular:

- avanço entre os quatro frames high-fidelity;
- entrada e criação de conta como modos de acesso, sem escolher tecnologia real;
- sessão já autenticada;
- recuperação, restrição e falha;
- voltar;
- sair;
- interromper;
- explorar sem personalização, quando aplicável;
- revisão de privacidade e controles;
- condição `HANDOFF READY`;
- handoff para `PER-003` sem materializar o conteúdo interno de `PER-003`.

A composição validada permanece:

```text
PER-002
├─ FRAME 01 — ORIENTAÇÃO PROTEGIDA / PRÉ-AUTH
├─ FRAME 02 — GATE DE ACESSO
│  ├─ VARIANTE A — SESSÃO JÁ AUTENTICADA
│  └─ VARIANTE B — RECUPERAÇÃO / RESTRIÇÃO / FALHA
├─ FRAME 03 — CONTINUAÇÃO AUTENTICADA / CONTROLES
├─ VARIANTE C — SAIR / INTERROMPER / EXPLORAR SEM PERSONALIZAÇÃO
└─ FRAME 04 — HANDOFF READY
                 ↓
               TRN-002
                 ↓
               PER-003
```

```text
4 PRIMARY FRAMES + 3 VARIANTS
→ 7 / 7 AUTHORIZED COVERAGE AREAS

7 COVERAGE AREAS
≠ 7 NEW SCREENS
≠ 7 NEW SURFACES
```

## 6. Natureza simulada obrigatória

```text
PROTOTYPE
→ DESIGN INSPECTION ARTIFACT
→ SIMULATED INTERACTION ONLY

PROTOTYPE
≠ IMPLEMENTED PRODUCT
≠ REAL AUTHENTICATION
≠ REAL SESSION
≠ REAL PERSISTENCE
≠ REAL DATA PROCESSING
≠ BACKEND
≠ PRODUCTION UI
```

A prototipação não poderá ser usada para escolher ou afirmar como implementados:

- e-mail, telefone ou username;
- senha, passkey ou biometria;
- provedor social/externo;
- IdP;
- backend;
- modelo de sessão;
- storage;
- API;
- política técnica de recuperação;
- arquitetura de autorização;
- telemetria;
- analytics;
- infraestrutura.

Slots funcionais podem ser representados apenas como simulação de Design.

## 7. Boundary funcional imutável

```text
AUTHENTICATION
→ INTERNAL GATE / STATE WITHIN PER-002

AUTHENTICATION COMPLETED
≠ PER-002 COMPLETED

LOGIN / ACCOUNT CREATION
≠ MATERIAL PROCESSING AUTHORIZATION

EXISTING-RELATIONSHIP LOGIN
→ RESUMPTIVE PATH

PER-003
→ DOWNSTREAM HANDOFF ONLY

PER-008
→ DOWNSTREAM

NEW SURFACE / NEW PER-ID
→ NOT AUTHORIZED
```

Interatividade não pode criar nova responsabilidade funcional, nova superfície canônica ou novo `PER-ID`.

## 8. N1 — compreensão não inferida

A execução deve preservar:

```text
DISPLAYED
≠ UNDERSTOOD

CLICKED
≠ UNDERSTOOD

COMPLETED INTERACTION
≠ UNDERSTOOD
```

Nenhum clique, avanço, scroll, tempo de tela ou conclusão simulada poderá ser representado como prova de compreensão humana.

## 9. N2 — finalidade e processamento

A execução deve preservar:

```text
GENERIC PURPOSE EXPLANATION
≠ FUTURE PROCESSING AUTHORIZATION

PROTOTYPE CLICK
≠ REAL CONSENT
≠ REAL DATA AUTHORIZATION
```

O protótipo não poderá representar autorização real de processamento nem produzir uma experiência de consentimento omnibus.

Cada uso material futuro continua sujeito a finalidade, disclosure, controles e autorização aplicáveis antes do processamento correspondente.

## 10. Autonomia, reversibilidade e ausência de coerção

Devem permanecer interativamente disponíveis, quando aplicável ao estado:

- voltar;
- não prosseguir;
- sair;
- interromper;
- recuperar acesso;
- explorar sem personalização;
- continuar somente depois das condições legítimas do boundary.

```text
PROTOTYPE AUTHORIZATION
≠ DARK PATTERN AUTHORIZATION
```

A execução não pode:

- ocultar saída legítima;
- criar urgência artificial;
- pré-selecionar autorização;
- usar disabled state para coagir continuidade;
- transformar autenticação em consentimento;
- penalizar visualmente a recusa legítima.

## 11. Dados

```text
PROTOTYPE CONTENT
→ SYNTHETIC / FICTIONAL / DESIGN-SAFE

REAL PERSONAL DATA
→ NOT REQUIRED
→ NOT AUTHORIZED

REAL CREDENTIALS
→ NOT AUTHORIZED
```

Nenhum dado real de participante é necessário ou autorizado por este ato.

## 12. Acessibilidade

O protótipo deverá preservar os requisitos de especificação da referência high-fidelity, incluindo:

- ordem semântica coerente;
- navegação por teclado quando a ferramenta permitir;
- foco visível;
- labels persistentes;
- estados não comunicados somente por cor;
- alternativas e saída alcançáveis;
- ausência de dependência exclusiva de hover;
- comportamento previsível de erro e recuperação.

```text
PROTOTYPE ACCESSIBILITY INSPECTION
≠ PRODUCTION ACCESSIBILITY CERTIFICATION
```

A existência do protótipo não comprova WCAG operacional nem acessibilidade de produção.

## 13. Responsividade

A execução poderá representar mobile, tablet e desktop conforme a referência high-fidelity, desde que preserve:

```text
SEMANTIC ORDER
→ UNCHANGED

RIGHTS / ALTERNATIVES
→ UNCHANGED

FUNCTIONAL BOUNDARY
→ UNCHANGED
```

Mudança de viewport não autoriza mudança de responsabilidade.

## 14. `PER-003` permanece apenas handoff

O protótipo pode demonstrar que `PER-003` é o próximo destino legítimo, mas não pode materializar internamente suas modalidades ou estados.

```text
SHOW HANDOFF TO PER-003
≠ DESIGN PER-003
≠ PROTOTYPE PER-003
```

Se a ferramenta exigir um destino clicável, deverá usar apenas uma parada/placeholder de boundary claramente identificada como fora do escopo de `PER-002`.

## 15. Source Lock

```text
SOURCE LOCK
→ NOT_CREATED
→ NOT_REQUIRED BY CURRENT EVIDENCE
→ NOT_AUTHORIZED BY THIS ACT
```

A autorização de protótipo não cria Source Lock por inferência.

## 16. UXA-102/V5 e Product Engineering

```text
UXA-102 / V5
→ NOT_STARTED
→ UNCHANGED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01
→ UNCHANGED

PROTOTYPE AUTHORIZATION
≠ UXA-102 RELEASE
≠ PRODUCT ENGINEERING RELEASE
```

## 17. Transições

```text
TRN-001
→ PARTIAL / UNCHANGED

TRN-002
→ LOCALLY VALIDATED / UNCHANGED

PROTOTYPE AUTHORIZATION
≠ TRANSITION MATURITY PROMOTION
```

A execução de uma simulação clicável também não poderá promover essas maturidades por si só.

## 18. Testes com pessoas

Este ato não autoriza Research ou teste com participantes reais.

```text
DESIGN PROTOTYPE EXECUTION
≠ HUMAN-SUBJECT TEST AUTHORIZATION
≠ FIELD RESEARCH RELEASE
```

Qualquer uso com participantes reais dependerá de autoridade própria, finalidade definida e gates aplicáveis.

## 19. O que esta autorização não autoriza

Este ato não autoriza:

- executar qualquer coisa além do protótipo de Design de `PER-002`;
- criar Source Lock;
- materializar `PER-003` além do handoff;
- materializar `PER-008`;
- criar nova superfície ou novo `PER-ID`;
- alterar a arquitetura funcional;
- Design das Homes;
- UXA-102/V5;
- Product Engineering;
- implementação;
- backend;
- autenticação real;
- sessão real;
- persistência real;
- dados reais;
- analytics real;
- telemetria real;
- produção;
- operação;
- testes com participantes reais;
- PMF;
- merge da PR #363.

## 20. Estado após a decisão

```text
INTERACTIVE PROTOTYPE ELIGIBILITY
→ PASS

INTERACTIVE PROTOTYPE AUTHORIZATION
→ GRANTED
→ GKR-UX-PER002-PROTOTYPE-AUTH-001 v1.0.0

INTERACTIVE PROTOTYPE EXECUTION
→ AUTHORIZED
→ NOT_STARTED

SOURCE LOCK
→ NOT_CREATED
→ NOT_AUTHORIZED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01

IMPLEMENTATION / PRODUCTION
→ NOT_AUTHORIZED
```

## 21. Próximo ato legítimo

```text
NEXT
→ PER-002 INTERACTIVE PROTOTYPE EXECUTION

MUST CONSUME
→ GKR-UX-PER002-PROTOTYPE-AUTH-001
→ GKR-UX-PER002-PROTOTYPE-ELIGIBILITY-001
→ VALIDATED HIGH-FIDELITY REFERENCE
→ FROZEN FUNCTIONAL BOUNDARY
→ N1 / N2

DO NOT
→ CREATE SOURCE LOCK BY INFERENCE
→ START UXA-102/V5
→ EXPAND TO PER-003
→ RESUME PRODUCT ENGINEERING
→ IMPLEMENT
→ USE REAL DATA
→ TEST WITH REAL PARTICIPANTS
→ MERGE PR #363
```

A execução do protótipo, se realizada, deverá ocorrer em ato separado e permanecer um artefato de Design simulado até validação posterior específica.