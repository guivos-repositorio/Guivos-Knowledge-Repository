---
id: GKR-UX-PER002-PROTOTYPE-ELIGIBILITY-001
title: PER-002 — Elegibilidade Pós-Validação para Protótipo Interativo
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-09
normative: true
maturity: interactive_prototype_eligibility_pass_pre_authorization
depends_on:
  - GKR-UX-PER002-HIFI-VALIDATION-001
  - GKR-UX-PER002-HIFI-DELIVERY-001
  - GKR-UX-PER002-HIFI-AUTH-001
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

# PER-002 — Elegibilidade Pós-Validação para Protótipo Interativo

## 1. Finalidade

Esta autoridade adjudica somente se, após a validação `PASS` da entrega high-fidelity de `PER-002`, existe base suficiente para submeter um **protótipo interativo de Design** a uma decisão separada de autorização.

Ela não autoriza nem executa protótipo, Source Lock, UXA-102/V5, Product Engineering, implementação ou produção.

## 2. Evidência de entrada

```text
PER-002 FUNCTIONAL BOUNDARY
→ FROZEN

LOW-FIDELITY DELIVERY
→ EXECUTED / VALIDATED PASS

HIGH-FIDELITY ELIGIBILITY
→ PASS

HIGH-FIDELITY AUTHORIZATION
→ GRANTED

HIGH-FIDELITY DELIVERY
→ GKR-UX-PER002-HIFI-DELIVERY-001 v0.1.0
→ EXECUTED

HIGH-FIDELITY VALIDATION
→ GKR-UX-PER002-HIFI-VALIDATION-001 v1.0.0
→ PASS
→ 15 / 15 CRITERIA PASS
→ MATERIAL FINDINGS = 0
→ BLOCKING FINDINGS = 0
→ REFORMULATION REQUIRED = NO
```

## 3. Pergunta de elegibilidade

> O boundary funcional e a referência high-fidelity já estão suficientemente definidos e validados para permitir uma **decisão separada de autorização de protótipo interativo de `PER-002`**, sem usar prototipação para redescobrir a arquitetura ou presumir implementação?

Resultado:

```text
INTERACTIVE PROTOTYPE ELIGIBILITY
→ PASS
```

## 4. Razões do PASS

O estágio é elegível porque:

1. `PER-002` possui responsabilidade funcional congelada;
2. os quatro frames e três variantes cobrem 7/7 áreas requeridas;
3. autenticação permanece gate interno;
4. N1 e N2 passaram pela validação high-fidelity;
5. autonomia, retorno, interrupção e saída permanecem explicitamente representados;
6. `PER-003` permanece somente como handoff;
7. a direção visual high-fidelity está suficientemente especificada para tornar comportamento de interface inspecionável sem redefinir arquitetura;
8. responsividade e acessibilidade possuem requisitos de especificação explícitos;
9. não existem findings materiais ou bloqueadores abertos;
10. nenhuma reformulação high-fidelity é necessária antes de uma eventual prototipação;
11. a aparência histórica removida não é necessária;
12. existe uma referência high-fidelity corrente validada para controlar regressão durante uma eventual interação simulada.

## 5. Referência obrigatória para qualquer decisão futura

```text
CURRENT FUNCTIONALLY VALIDATED HIGH-FIDELITY DESIGN REFERENCE
→ GKR-UX-PER002-HIFI-DELIVERY-001 v0.1.0
+
→ GKR-UX-PER002-HIFI-VALIDATION-001 v1.0.0

FUNCTIONAL BOUNDARY
→ GKR-UX-PER002-MAT-ELIGIBILITY-001 / FROZEN

CURRENT FUNCTIONAL AUTHORITY
→ PREVAILS
```

## 6. Natureza de um eventual protótipo autorizado

Se houver autorização separada, o protótipo poderá tornar interativamente inspecionáveis somente os estados e transições de Design já especificados para `PER-002`.

Poderá simular, conforme necessário:

- avanço entre os quatro frames;
- entrada e criação de conta como modos de acesso, sem escolher tecnologia real;
- sessão já autenticada;
- recuperação/restrição/falha;
- voltar, sair, interromper e explorar sem personalização;
- revisão de privacidade/controles;
- condição de `HANDOFF READY`;
- handoff para `PER-003` sem materializar o conteúdo interno de `PER-003`.

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
```

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
→ NOT WARRANTED BY THIS ELIGIBILITY
```

Um futuro protótipo não poderá usar interatividade para criar nova responsabilidade funcional ou esconder um desvio arquitetural.

## 8. N1 e N2 permanecem obrigatórias

### N1

```text
DISPLAYED
≠ UNDERSTOOD

CLICKED
≠ UNDERSTOOD

COMPLETED INTERACTION
≠ UNDERSTOOD
```

Interação em protótipo não poderá ser tratada como evidência real de compreensão.

### N2

```text
GENERIC PURPOSE EXPLANATION
≠ FUTURE PROCESSING AUTHORIZATION

PROTOTYPE CLICK
≠ REAL CONSENT
≠ REAL DATA AUTHORIZATION
```

Nenhuma simulação poderá ser interpretada como autorização real de processamento.

## 9. Autonomia e não coerção

Se autorizado futuramente, o protótipo deverá manter testáveis:

- voltar;
- não prosseguir;
- sair;
- interromper;
- recuperar acesso;
- explorar sem personalização quando aplicável;
- continuar somente depois das condições legítimas do boundary.

```text
PROTOTYPE ELIGIBILITY
≠ DARK PATTERN AUTHORIZATION
```

## 10. Acessibilidade

Um eventual protótipo deverá preservar os requisitos da referência high-fidelity, mas sua existência não provará conformidade operacional.

```text
PROTOTYPE ACCESSIBILITY INSPECTION
≠ PRODUCTION ACCESSIBILITY CERTIFICATION
```

## 11. Tecnologia e autenticação

A elegibilidade não escolhe:

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

Slots funcionais podem ser simulados sem se tornarem decisões técnicas.

## 12. Dados e processamento

Um protótipo futuro deverá usar conteúdo sintético/fictício de Design.

```text
REAL PERSONAL DATA
→ NOT REQUIRED
→ NOT AUTHORIZED BY THIS ELIGIBILITY

PROTOTYPE CONTENT
→ SYNTHETIC / DESIGN-SAFE
```

Esta adjudicação não libera coleta, processamento ou persistência de dados reais.

## 13. Source Lock

```text
SOURCE LOCK
→ NOT_CREATED
→ NOT_REQUIRED BY CURRENT EVIDENCE
→ NOT_AUTHORIZED BY INFERENCE
```

A referência high-fidelity validada já oferece rastreabilidade suficiente para um gate de autorização de protótipo. Source Lock só deverá ser proposto se surgir finalidade concreta de congelamento que não esteja atendida pela cadeia atual.

## 14. UXA-102/V5 e Product Engineering

```text
UXA-102 / V5
→ NOT_STARTED
→ UNCHANGED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01
→ UNCHANGED

PROTOTYPE ELIGIBILITY
≠ UXA-102 RELEASE
≠ PRODUCT ENGINEERING RELEASE
```

## 15. Transições

```text
TRN-001
→ PARTIAL / UNCHANGED

TRN-002
→ LOCALLY VALIDATED / UNCHANGED

PROTOTYPE ELIGIBILITY
≠ TRANSITION MATURITY PROMOTION
```

Uma simulação clicável futura não promove maturidade funcional por si só.

## 16. Estado de autorização

```text
INTERACTIVE PROTOTYPE ELIGIBILITY
→ PASS

INTERACTIVE PROTOTYPE AUTHORIZATION
→ NOT_GRANTED
→ REQUIRES SEPARATE EXPLICIT GOVERNED ACT

INTERACTIVE PROTOTYPE EXECUTION
→ NOT_STARTED

SOURCE LOCK
→ NOT_CREATED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01
```

## 17. O que esta autoridade não autoriza

Este `PASS` não autoriza:

- criar protótipo;
- criar Source Lock;
- materializar `PER-003` além do handoff;
- materializar `PER-008`;
- criar nova superfície ou novo `PER-ID`;
- Design das Homes;
- UXA-102/V5;
- Product Engineering;
- implementação;
- backend;
- autenticação real;
- dados reais;
- produção;
- operação;
- testes com participantes reais;
- merge da PR #363.

## 18. Resultado final

```text
POST-HIGH-FIDELITY NEXT-STAGE ELIGIBILITY
→ PASS

NEXT ELIGIBLE STAGE
→ EXPLICIT PER-002 INTERACTIVE PROTOTYPE AUTHORIZATION DECISION

CURRENT HIGH-FIDELITY DESIGN REFERENCE
→ DELIVERY v0.1.0 + VALIDATION v1.0.0

PROTOTYPE AUTHORIZATION
→ NOT_GRANTED

PROTOTYPE EXECUTION
→ NOT_STARTED

DO NOT YET
→ CREATE PROTOTYPE
→ CREATE SOURCE LOCK BY INFERENCE
→ START UXA-102/V5
→ RESUME PRODUCT ENGINEERING
→ IMPLEMENT
→ MERGE PR #363
```

Esta autoridade abre somente a possibilidade de uma decisão separada de autorização de protótipo interativo de `PER-002`.