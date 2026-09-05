---
id: GKR-JOURNEY-SCREEN-GALLERY-PERSON-001
title: Pessoa — Fundação, Entrada, Compreensão e Recorrência
status: superseded
version: 0.7.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-05
parent: GKR-JOURNEY-SCREEN-GALLERY-001
related:
  - UXA-081
  - UXA-082
  - UXA-083
  - UXA-084
  - UXA-085
  - UXA-097
  - GKR-UX-D5-C1-001
  - GKR-UX-D5-C2-001
  - GKR-UX-D5-C3-001
  - GKR-UX-D5-C4B-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
maturity: historical_provenance_only
---

# Pessoa — Fundação, Entrada, Compreensão e Recorrência

> **F-016-A — desmaterialização física.** Os SVGs desta frente foram removidos do corpus vigente. Qualquer nome `.svg` remanescente neste documento é **proveniência histórica**, não arquivo disponível, não autoridade visual e não autorização de Design. O contrato funcional permanece governado pelo texto e pelas autoridades funcionais relacionadas.


[← Índice da galeria](screen-gallery.md) · [Matriz por SVG](screen-gallery-traceability-matrix.md) · [Próxima: Oportunidades e Organização →](screen-gallery-opportunities-organization.md)

## 1. Ordem funcional de inspeção

```text
Home pública
→ início protegido
→ expressão guiada
→ compreensão inicial
→ primeira Tela Hoje
→ Tela Hoje recorrente
├── Meus Objetivos
├── Meus Próximos Passos
└── Minha Evolução
```

A UXA-097 valida `GKR-TRN-007` entre a compreensão inicial e a primeira Tela Hoje. A D5-C3 valida localmente as três superfícies especializadas posteriores e a D5-C4B promove individualmente `TRN-008..013` para **integralmente validadas no limite documental**. Isso não promove a Jornada da Pessoa além de `draft`, porque outras transições da jornada permanecem parciais e a validação documental não equivale a implementação.

## 2. Home pública

**Cobertura:** 1 SVG · ID: `GKR-SURF-PER-001` · origem: `UXA-022` · validação: `UXA-021`

### `uxa-022-public-home-desktop.svg`


## 3. Início protegido

**Cobertura:** 4 SVGs · IDs: `GKR-SURF-PER-002`, `GKR-SURF-PER-003`, `GKR-SURF-PER-005` · origem: `UXA-034` · validação: `UXA-035`

### `uxa-034-protected-entry-access-mobile.svg`


### `uxa-034-protected-entry-explanation-mobile.svg`


### `uxa-034-protected-entry-sharing-mobile.svg`


### `uxa-034-protected-entry-review-mobile.svg`


## 4. Expressão Guiada do Momento Atual

**Cobertura:** 8 SVGs · ID: `GKR-SURF-PER-004` · origem: `UXA-068` · validação: `UXA-069`

### `uxa-068-guided-current-moment-orientation-mobile.svg`


### `uxa-068-guided-current-moment-text-draft-mobile.svg`


### `uxa-068-guided-current-moment-voice-preparation-mobile.svg`


### `uxa-068-guided-current-moment-voice-recording-mobile.svg`


### `uxa-068-guided-current-moment-voice-transcription-review-mobile.svg`


### `uxa-068-guided-current-moment-focus-separation-mobile.svg`


### `uxa-068-guided-current-moment-adaptive-clarification-mobile.svg`


### `uxa-068-guided-current-moment-structured-summary-mobile.svg`


## 5. Compreensão inicial

**Cobertura:** 5 SVGs · IDs: `GKR-SURF-PER-006`, `GKR-SURF-PER-007` · origem: `UXA-036` · validação: `UXA-037`; estado de decisão corrente revalidado por `UXA-097`

### `uxa-036-initial-understanding-processing-mobile.svg`


### `uxa-036-initial-understanding-presentation-mobile.svg`


### `uxa-036-initial-understanding-review-mobile.svg`


### `uxa-036-initial-understanding-decision-mobile.svg`


### `uxa-036-initial-understanding-insufficient-basis-mobile.svg`


## 6. Tela Hoje — primeira entrada

**Cobertura:** 1 SVG · ID: `GKR-SURF-PER-008` · origem e validação: `UXA-097` · entrada: `GKR-TRN-007` integralmente validada

### `uxa-097-first-today-after-initial-understanding-mobile.svg`


A primeira variante não presume avanço, mudança anterior, urgência ou preenchimento comercial. Sem autorização de personalização, os blocos pessoais são omitidos.

## 7. Tela Hoje — experiência recorrente

**Cobertura:** 1 SVG · ID: `GKR-SURF-PER-008` · origem: `UXA-006` · validação local: `UXA-010`; handoffs especializados `TRN-008/010/012` integralmente validados documentalmente por D5-C4B

### `uxa-006-hoje-mobile.svg`


## 8. Meus Objetivos — D5-C3 / D5-C4B

**Cobertura:** 1 SVG · ID: `GKR-SURF-PER-010` · materialização: `GKR-UX-D5-C2-001` · **validação/reformulação local: `GKR-UX-D5-C3-001`** · `TRN-008/009` **integralmente validadas documentalmente por D5-C4B**

### `d5-c2-person-objectives-mobile.svg`


O estado-base passa a explicitar estado funcional, prioridade declarada, progresso qualitativo, revisão e privacidade. Prioridade e progresso permanecem separados de valor humano.

## 9. Meus Próximos Passos — D5-C3 / D5-C4B

**Cobertura:** 1 SVG · ID: `GKR-SURF-PER-011` · materialização: `GKR-UX-D5-C2-001` · **validação/reformulação local: `GKR-UX-D5-C3-001`** · `TRN-010/011` **integralmente validadas documentalmente por D5-C4B**

### `d5-c2-person-next-steps-mobile.svg`


O estado-base distingue `PRONTO` de `PROPOSTO`, torna prontidão/dependência explícitas e usa ações compatíveis com cada estado. Não utiliza streak, obrigação ou urgência artificial.

## 10. Minha Evolução — D5-C3 / D5-C4B

**Cobertura:** 1 SVG · ID: `GKR-SURF-PER-012` · materialização: `GKR-UX-D5-C2-001` · **validação/reformulação local: `GKR-UX-D5-C3-001`** · `TRN-012/013` **integralmente validadas documentalmente por D5-C4B**

### `d5-c2-person-evolution-mobile.svg`


O estado-base explicita período, baseline, direção, natureza inferida da interpretação, confiança e incerteza, mantendo Área da jornada, Contexto Vivo e aspecto descritivo separados. Não utiliza score, radar, roda da vida, diagnóstico ou avaliação espiritual.

## 11. Limite

Esta página reúne **23 SVGs**. As superfícies possuem as maturidades locais indicadas por suas autoridades; D5-C4B valida integralmente `TRN-008..013` no limite documental e não transforma essa validação em implementação.

A Home e a Tela Hoje permanecem separadas. `TRN-007` e `TRN-008..013` estão integralmente validadas nos limites documentais aplicáveis, mas `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` continuam parciais; portanto a Jornada da Pessoa permanece `draft`.

O status `active` registra o instrumento de inspeção e não inicia protótipo ou Engenharia de Produto.

[← Índice da galeria](screen-gallery.md) · [Matriz por SVG](screen-gallery-traceability-matrix.md) · [Próxima: Oportunidades e Organização →](screen-gallery-opportunities-organization.md)