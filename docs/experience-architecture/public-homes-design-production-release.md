---
id: GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
title: Homes Públicas — Registro do Design Production Release v5 e Suspensão para Nova Emissão
status: active
version: 1.1.0
owner: Guivos
last_updated: 2026-09-19
normative: true
maturity: v5_release_historical_new_execution_suspended_for_source_readiness
depends_on:
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V5-SNAPSHOT-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-SOURCE-READINESS-REMEDIATION-001
related:
  - GKR-STATE-001
  - GKR-HOME-MASTERS-REMEDIATION-001
---

# Homes Públicas — Registro do Design Production Release v5 e Suspensão para Nova Emissão

## 1. Finalidade

Esta autoridade preserva o ato humano de `DESIGN PRODUCTION RELEASE = GRANTED` que foi concedido ao snapshot v5 e registra a decisão posterior de retornar à prontidão documental antes de qualquer nova execução externa de Design.

O ato anterior não é apagado. Seu efeito operacional fica limitado ao contexto histórico do v5.

```text
V5 RELEASE
→ HISTORICALLY GRANTED

CURRENT NEW EXECUTION
→ SUSPENDED

REASON
→ MATERIAL SOURCE-READINESS REMEDIATION

NEW EXTERNAL PACKAGE
→ REQUIRED BEFORE NEW DESIGN START
```

## 2. Decisão humana posterior

A Guivos definiu que:

- a designer humana é a executora criativa principal;
- a criação deve ocorrer manualmente com total liberdade estética dentro dos contratos do GKR;
- sistemas de IA podem ser usados opcionalmente como apoio;
- Figma Make não é etapa obrigatória;
- o GKR/ChatGPT não deve produzir arquivos de Design como etapa de prontidão;
- os documentos mestres e demais autoridades devem ser levados a `100% SOURCE READY` antes do trabalho externo.

Consequentemente:

```text
DESIGN PRODUCTION RELEASE v5
→ DOES NOT AUTHORIZE A NEW EXECUTION AFTER MATERIAL SOURCE CHANGE

FIGMA MAKE / GENERATIVE EXPLORATION
→ NOT A REQUIRED GATE

FIGMA EXECUTION BY GKR / CHATGPT
→ STOPPED

DESIGNER MANUAL CREATION
→ TARGET OPERATING MODEL

AI
→ OPTIONAL SUPPORT
```

## 3. Evidência histórica preservada

```text
ORIGIN MAIN FOR V5
→ aa1b524c20f6707d007208222ba8581af097c38d

SNAPSHOT BRANCH
→ delivery/design-handoff-v5

SNAPSHOT COMMIT
→ f2e8375258fda4f37aea27a5e5ec5e83f5c1a66d

SNAPSHOT TREE
→ 67bacb135166e7f3e85bfb4c52602ba89a515a1e

PACKAGE
→ 34 FILES
→ 26 CANONICAL SOURCES
→ 8 PER-HOME LEIA-PRIMEIRO / SOURCE LOCK GUIDES

CANONICAL BLOB PRESERVATION
→ 26 / 26 EXACT MATCH
→ MISMATCHES = 0
```

O snapshot v5 permanece congelado e não será reescrito.

## 4. Motivo da nova remediação

A auditoria posterior identificou acoplamento operacional indevido a Figma Make e prototipação generativa nas autoridades comuns e nos oito `LEIA-PRIMEIRO`.

Essa mudança é material porque altera o modo de consumo do pacote externo.

```text
V5
→ HISTORICAL / FROZEN

CURRENT AUTHORITIES
→ UNDER TOOL-AGNOSTIC REMEDIATION

8 HOMES
→ REQUIRE SOURCE_READY AUDIT

NEW SNAPSHOT
→ ONLY AFTER REMEDIATION + VALIDATION + HUMAN GATE
```

## 5. Regra para a designer

A designer deverá receber documentação que permita compreender sem inferência:

- papel da Home;
- tese;
- narrativa;
- navegação;
- estados;
- fronteiras;
- prova;
- dados;
- conteúdo;
- proteções;
- questões abertas;
- liberdades criativas;
- inferências proibidas.

O GKR não deve impor antes da criação:

- tipografia;
- paleta;
- imagem;
- composição;
- grid;
- motion;
- identidade visual;
- linguagem gráfica;
- direção de arte.

## 6. Regra para IA

Se a designer optar por usar IA:

1. usar o mesmo pacote governado;
2. respeitar o Source Lock;
3. não carregar múltiplas Homes indiscriminadamente;
4. não preencher lacuna factual ou semântica;
5. classificar hipótese, placeholder e conteúdo candidato;
6. submeter qualquer saída à decisão humana.

## 7. Artefato experimental de Figma

A execução `GKR-UX-HOME-PERSON-DESIGN-EXEC-001` foi encerrada como `SUPERSEDED / NOT PLANNED`.

Qualquer arquivo externo criado durante essa tentativa:

```text
→ NON-CANONICAL
→ NOT A BASELINE
→ NOT A REQUIRED REFERENCE
→ NOT PART OF THE SOURCE PACKAGE
→ MUST NOT CONSTRAIN THE DESIGNER
```

## 8. Limites preservados

Esta remediação não autoriza:

- Product Engineering;
- frontend/backend;
- publicação;
- deploy;
- nova arquitetura de produto;
- nova funcionalidade não governada;
- alteração de modelo econômico;
- Marketing/GTM;
- Research com participantes reais;
- claims não sustentados;
- promoção de `GKR-SURF-*` / `GKR-TRN-*`;
- `UXA-102/V5`;
- high-fidelity autenticado O/C por inferência.

```text
PUBLIC HOME SOURCE READINESS
≠ O/C AUTHENTICATED HIGH-FIDELITY AUTHORIZATION
```

## 9. Novo gate

Antes de nova entrega externa:

```text
COMMON AUTHORITIES
→ TOOL-AGNOSTIC

8 / 8 HOMES
→ SOURCE_READY

MATERIAL DOCUMENT GAPS
→ 0

SEMANTIC CONFLICTS
→ 0

NEW SOURCE PACKAGE
→ REPRODUCIBLE

SEMANTIC + MECHANICAL VALIDATION
→ PASS

INDEPENDENT REVIEW
→ NO MATERIAL FINDING

HUMAN RELEASE
→ REQUIRED
```

## 10. Estado

```text
V5 SNAPSHOT
→ HISTORICAL / FROZEN

V5 DESIGN PRODUCTION RELEASE
→ HISTORICALLY GRANTED

CURRENT EXTERNAL DESIGN START
→ SUSPENDED PENDING SOURCE-READINESS REMEDIATION

FIGMA EXECUTION BY GKR
→ STOPPED

DESIGNER MANUAL CREATION
→ TARGET MODEL

AI SUPPORT
→ OPTIONAL / TOOL-AGNOSTIC

NEW SNAPSHOT
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED

UXA-102 / V5
→ NOT_STARTED
```

## 11. Próximo movimento legítimo

Auditar e completar os documentos das oito Homes, uma por vez, contra `GKR-UX-HOMES-DESIGN-SOURCE-READINESS-REMEDIATION-001`.

Somente depois do fechamento de `8 / 8 SOURCE_READY` poderá ser proposta nova emissão externa.