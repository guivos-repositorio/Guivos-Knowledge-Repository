---
id: GKR-UXA-104-SCOPE-DISCOVERY-001
title: UXA-104 — Descoberta de Escopo
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: false
maturity: scope_adjudicated
depends_on:
  - GKR-STATE-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
  - GKR-UX-G1-ENTRY-EXPRESSION-INVENTORY-VALIDATION-001
  - GKR-UXA-103-TRN005-MATURITY-EXAM-001
  - GKR-UXA-104-PER013014-SCOPE-AUTHORITY-001
related:
  - UXA-103
  - GKR-UX-PER003-MASTER-001
  - GKR-UX-PER005-MASTER-001
---

# UXA-104 — Descoberta de Escopo

## 1. Estado deste artefato

Este documento preserva a descoberta que antecedeu a adjudicação humana do escopo da UXA-104.

```text
UXA-104
→ SCOPE ADJUDICATED
→ FUNCTIONAL EXAM NOT_STARTED

SCOPE
→ ADJUDICATED
→ AUTHORITY = GKR-UXA-104-PER013014-SCOPE-AUTHORITY-001

FUNCTIONAL EXAM
→ NOT_STARTED

MATURITY PROMOTION
→ NONE

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```

A autoridade normativa de escopo é `GKR-UXA-104-PER013014-SCOPE-AUTHORITY-001`. Este artefato de descoberta permanece não normativo e não autoriza, por si só, exame funcional, Design, protótipo ou implementação.

## 2. Base canônica consultada

A UXA-103 encerrou especificamente o tratamento de `TRN-005 — PER-005 → PER-006`, promovendo essa transição para `LOCALLY VALIDATED`.

Após a reconciliação de `GKR-JOURNEY-GAPS-001`, a família G1 preserva como lacunas correntes:

- `TRN-001 — PER-001 → PER-002`: `PARTIAL`;
- `TRN-014 — PER-003 → PER-013`: `CONTRACTED`;
- `TRN-015 — PER-013 → PER-005`: `CONTRACTED`;
- `TRN-016 — PER-003 → PER-014`: `CONTRACTED`;
- `TRN-017 — PER-014 → PER-005`: `CONTRACTED`;
- `PER-013/014`: ainda não materializados como Masters canônicos correntes.

O Roadmap declara adicionalmente que as escolhas `FILE` e `OPTIONAL GUIDED QUESTIONS` de `PER-003` possuem continuidade downstream ainda não plenamente contratada/materializada.

## 3. Candidatos examinados

### Candidato A — continuidade Arquivo + Perguntas Opcionais em G1

Escopo potencial:

- `PER-013`;
- `PER-014`;
- `TRN-014..017`;
- continuidade consciente `PER-003 → PER-013/014 → PER-005`;
- revisão, remoção, retorno e autorização material antes de qualquer processamento;
- critérios verificáveis para eventual reexame posterior de maturidade.

Vantagem documental: fecha a bifurcação explícita ainda aberta em `PER-003`, permanecendo no mesmo domínio funcional imediato tratado por UXA-103 e sem depender de implementação técnica.

### Candidato B — TRN-001 / entrada pública → entrada protegida

Escopo potencial:

- `TRN-001 — PER-001 → PER-002`;
- continuidade entre pacotes;
- fronteira pública/protegida;
- autenticação como gate interno, sem autorização material implícita.

Este candidato permanece válido, porém é uma lacuna isolada de entrada e não resolve as duas rotas downstream explicitamente ainda incompletas em `PER-003`.

### Candidatos C–F — G2, G3, G4 e G5

Essas famílias permanecem abertas, mas já possuem validações específicas próprias e dependências adicionais de materialização ponta a ponta, superfícies bilaterais, processo interno de oportunidade ou operacionalização econômica.

Nenhuma delas é automaticamente promovida por esta descoberta.

## 4. Convergência analítica adjudicada

A convergência abaixo foi adjudicada humanamente como escopo da UXA-104:

```text
UXA-104 ADJUDICATED SCOPE
→ G1 / FILE + OPTIONAL GUIDED QUESTIONS CONTINUITY
→ PER-013 + PER-014
→ TRN-014..017

TRN-001
→ REMAINS OPEN
→ OUTSIDE THIS CANDIDATE SCOPE

G2–G5
→ REMAIN OPEN
→ OUTSIDE THIS CANDIDATE SCOPE
```

Motivo: `PER-003` já declara quatro escolhas válidas, mas somente Texto/Voz possuem continuidade materializada por `PER-004 → PER-005`. Arquivo e Perguntas Opcionais mantêm contratos de transição sem Masters canônicos próprios, constituindo a continuidade funcional mais diretamente adjacente à cadeia G1 já tratada.

Esta convergência foi adjudicada exclusivamente como limite de escopo; não constitui contrato funcional nem promoção de maturidade.

## 5. Limites

Este artefato:

- não cria `PER-013` ou `PER-014`;
- não altera `TRN-014..017`;
- não promove `TRN-001`;
- não abre G2–G5;
- não define upload, storage, parsing, OCR, IA, persistência ou mecanismo técnico;
- não define obrigatoriedade de perguntas;
- não autoriza processamento material;
- não libera Product Engineering.

## 6. Próximo gate humano

O escopo foi adjudicado e materializado por `GKR-UXA-104-PER013014-SCOPE-AUTHORITY-001`.

```text
NEXT GOVERNED GATE
→ AUTHORIZE UXA-104 FUNCTIONAL EXAM
```

O exame funcional permanece `NOT_STARTED` até autorização humana própria.
