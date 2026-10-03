---
id: GKR-UXA-104-PER013014-SCOPE-AUTHORITY-001
title: UXA-104 — Autoridade de Escopo — Arquivo e Perguntas Opcionais
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: true
maturity: scope_adjudicated
depends_on:
  - GKR-STATE-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
  - GKR-UX-G1-ENTRY-EXPRESSION-INVENTORY-VALIDATION-001
related:
  - UXA-104
  - GKR-UX-PER003-MASTER-001
  - GKR-UX-PER005-MASTER-001
---

# UXA-104 — Autoridade de Escopo — Arquivo e Perguntas Opcionais

## 1. Autoridade

Este documento materializa a adjudicação humana do escopo da UXA-104.

```text
GKR-UXA-104-PER013014-SCOPE-AUTHORITY-001
→ ACTIVE
→ NORMATIVE
→ SCOPE ADJUDICATED
```

## 2. Escopo adjudicado

A UXA-104 examinará exclusivamente a continuidade G1 das escolhas **Arquivo** e **Perguntas Opcionais** a partir de `PER-003`, abrangendo:

- responsabilidade funcional candidata `PER-013` para captura/revisão de Arquivo;
- responsabilidade funcional candidata `PER-014` para Perguntas Opcionais;
- `TRN-014 — PER-003 → PER-013`;
- `TRN-015 — PER-013 → PER-005`;
- `TRN-016 — PER-003 → PER-014`;
- `TRN-017 — PER-014 → PER-005`;
- revisão consciente antes de continuidade;
- remoção/retorno quando aplicáveis;
- voluntariedade das perguntas;
- ausência de autorização material implícita;
- critérios verificáveis para eventual reexame posterior de maturidade.

## 3. Fora do escopo

Permanecem fora da UXA-104:

- `TRN-001`;
- `TRN-005`, já tratado por UXA-103;
- G2, G3, G4 e G5;
- implementação de upload, storage, parsing, OCR ou IA;
- persistência técnica;
- mecanismos físicos de idempotência;
- Design high-fidelity;
- protótipo;
- Product Engineering;
- promoção automática de maturidade.

## 4. Efeito da adjudicação

A adjudicação:

- cria autoridade normativa apenas para o **limite do exame**;
- não materializa por si só `PER-013` ou `PER-014` como Masters;
- não altera o estado de `TRN-014..017`, que permanecem `CONTRACTED`;
- não inicia o exame funcional automaticamente;
- não autoriza implementação.

## 5. Próximo gate

```text
UXA-104
→ SCOPE ADJUDICATED

FUNCTIONAL EXAM
→ NOT_STARTED

NEXT GOVERNED GATE
→ FUNCTIONAL EXAM AUTHORIZATION
```
