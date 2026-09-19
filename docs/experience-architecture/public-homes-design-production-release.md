---
id: GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
title: Homes Públicas — Autorização Governada de Design Production Release
status: active
version: 1.1.0
owner: Guivos
last_updated: 2026-09-19
normative: true
maturity: design_production_release_granted_document_source_v6_finalization
depends_on:
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V5-SNAPSHOT-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
related:
  - GKR-STATE-001
  - GKR-HOME-MASTERS-REMEDIATION-001
---

# Homes Públicas — Autorização Governada de Design Production Release

## 1. Finalidade

Esta autoridade preserva o ato humano que concedeu `DESIGN PRODUCTION RELEASE` para as oito Homes públicas e corrige o modelo operacional de consumo da documentação.

A autorização é para **trabalho externo de Design conduzido pela designer humana**, a partir das fontes governadas do GKR.

```text
GKR
→ SIGNIFICADO / FUNÇÃO / LIMITES / VERDADE / FONTES

DESIGNER
→ AUTORIA CRIATIVA
→ CRIAÇÃO MANUAL E CURADORIA DA ENTREGA NO FIGMA
→ DECISÃO VISUAL DENTRO DOS LIMITES SEMÂNTICOS

SISTEMAS DE IA
→ APOIO OPCIONAL
→ LEITURA / SÍNTESE / IDEAÇÃO / ALTERNATIVAS / COPY CANDIDATA / ASSETS CANDIDATOS
→ SEM AUTORIDADE CANÔNICA

GKR OU IA → MATERIALIZAÇÃO DIRETA DO ARQUIVO OFICIAL NO FIGMA
→ FORA DO FLUXO APROVADO
```

## 2. Decisão governada

```text
PUBLIC HOMES DESIGN PRODUCTION RELEASE
→ GRANTED

AUTHORIZED TARGETS
→ HOME PESSOA
→ HOME ORGANIZAÇÕES E COLETIVOS
→ HOME MALL
→ HOME TRAVEL
→ HOME MEDIA
→ HOME ADS
→ HOME BUSINESS
→ HOME INTELLIGENCE

HUMAN DESIGNER
→ PRIMARY CREATIVE EXECUTOR

AI SUPPORT
→ OPTIONAL / NON-AUTHORITATIVE

OFFICIAL FIGMA FILE
→ MANUALLY CREATED / CURATED BY DESIGNER

DIRECT AI-TO-FIGMA EXECUTION BY GKR WORKFLOW
→ NOT PART OF THE APPROVED PROCESS
```

## 3. Evidência histórica de entrada

O snapshot v5 permanece reproduzível e congelado:

```text
ORIGIN MAIN FOR SNAPSHOT
→ aa1b524c20f6707d007208222ba8581af097c38d

SNAPSHOT BRANCH
→ delivery/design-handoff-v5

SNAPSHOT COMMIT
→ f2e8375258fda4f37aea27a5e5ec5e83f5c1a66d

SNAPSHOT TREE
→ 67bacb135166e7f3e85bfb4c52602ba89a515a1e
```

O v5 não é reescrito. Sua hipótese operacional de Figma Make passa a ser **histórica e superada** para novas entregas.

## 4. Fonte operacional futura

A próxima emissão externa deverá ser v6 e trabalhar uma Home por vez com:

1. `00-COMUM`;
2. `00-LEIA-PRIMEIRO` da Home;
3. fontes específicas daquela Home;
4. esta autoridade de release;
5. matriz explícita das oito classes operacionais.

As classes permanecem: `CANONICAL`, `DESIGN_CREATIVE`, `CONTENT_CANDIDATE`, `DESIGN_HYPOTHESIS`, `PROTOTYPE_PLACEHOLDER`, `REAL_DATA_REQUIRED`, `OPEN_QUESTION` e `PROHIBITED_INFERENCE`.

## 5. Liberdade criativa preservada

Identidade visual, tipografia, paleta, imagens, composição, grid, iconografia, motion, aparência de componentes, linguagem gráfica, atmosfera e copy/tom não congelados permanecem sob autoria da designer.

Nenhum documento v6 deverá criar brand book visual implícito.

```text
DESIGN FREEDOM
≠ PRODUCT REDEFINITION
≠ FACTUAL INVENTION
≠ CLAIM WITHOUT EVIDENCE
```

## 6. Uso de sistemas de IA

A designer pode utilizar sistemas de IA quando isso ampliar qualidade ou velocidade, inclusive para estudar e sintetizar fontes, testar alternativas, propor `CONTENT_CANDIDATE`, gerar referências/assets candidatos e verificar consistência contra o Source Lock.

Toda saída de IA permanece proposta. A designer é responsável por selecionar, revisar, adaptar ou rejeitar.

```text
AI OUTPUT
→ CANDIDATE / ASSISTIVE

AI OUTPUT
≠ CANONICAL TRUTH
≠ DESIGN APPROVAL
≠ OFFICIAL FIGMA DELIVERY
```

## 7. Gate de direção e entrega final

```text
DOCUMENTARY SOURCE PACKAGE V6
↓
DESIGNER STUDY
↓
OPTIONAL AI ASSISTANCE
↓
MANUAL / HUMAN-CURATED DESIGN EXPLORATION
↓
HUMAN DIRECTION REVIEW
↓
DESIGNER FINALIZATION IN FIGMA
↓
FINAL HUMAN ACCEPTANCE
```

## 8. Limites explícitos

Este ato não autoriza Product Engineering, frontend/backend, publicação, deploy, nova arquitetura de produto, nova funcionalidade não governada, alteração de modelo econômico, Marketing/GTM, Research com participantes reais, claims não sustentados, promoção de `GKR-SURF-*`/`GKR-TRN-*`, `UXA-102/V5` ou high-fidelity da experiência autenticada O/C por inferência.

```text
PUBLIC HOME O/C DESIGN RELEASE
≠ O/C AUTHENTICATED HIGH-FIDELITY AUTHORIZATION
```

## 9. Estado corrente

```text
V5 SNAPSHOT
→ FROZEN / HISTORICAL FOR NEW EXECUTION

DESIGN PRODUCTION RELEASE
→ GRANTED

DOCUMENTARY SOURCE V6
→ UNDER FINALIZATION

EXTERNAL DESIGN EXECUTION
→ HOLD UNTIL V6 SNAPSHOT IS EMITTED AND VALIDATED

AI SUPPORT
→ OPTIONAL / NON-AUTHORITATIVE

DIRECT GKR/AI FIGMA MATERIALIZATION
→ OUT_OF_SCOPE

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED

UXA-102 / V5
→ NOT_STARTED
```

## 10. Próximo movimento legítimo

Concluir, revisar, validar e emitir o **pacote documental v6** para a designer e para sistemas de IA de apoio. Nenhum arquivo de Design precisa ser criado pelo GKR para satisfazer esse gate.
