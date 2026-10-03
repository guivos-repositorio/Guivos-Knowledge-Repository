---
id: GKR-UXA-104-SCOPE-DISCOVERY-001
title: UXA-104 — Descoberta de Escopo
status: candidate
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: false
maturity: scope_candidate_not_adjudicated
depends_on:
  - GKR-STATE-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
  - GKR-UX-G1-ENTRY-EXPRESSION-INVENTORY-VALIDATION-001
  - GKR-UXA-103-TRN005-MATURITY-EXAM-001
related:
  - UXA-103
  - GKR-UX-PER003-MASTER-001
  - GKR-UX-PER005-MASTER-001
---

# UXA-104 — Descoberta de Escopo

## 1. Estado deste artefato

Este documento registra somente a descoberta de escopo candidata para a próxima frente numerada.

```text
UXA-104
→ NEXT
→ NOT_STARTED
→ NOT AUTHORIZED

SCOPE
→ CANDIDATE ONLY
→ NOT ADJUDICATED

FUNCTIONAL EXAM
→ NOT_STARTED

MATURITY PROMOTION
→ NONE

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```

A existência deste artefato não inicia UXA-104, não cria autoridade normativa e não autoriza exame funcional, Design, protótipo ou implementação.

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

## 4. Convergência analítica candidata

A evidência corrente converge, sem adjudicação, para:

```text
UXA-104 CANDIDATE SCOPE
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

Esta convergência não equivale a adjudicação de escopo.

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

O próximo gate é exclusivamente a adjudicação humana da seguinte conclusão candidata:

```text
ADJUDICATE UXA-104 SCOPE?
→ PER-013 / PER-014
→ TRN-014..017
→ G1 FILE + OPTIONAL GUIDED QUESTIONS CONTINUITY
```

Somente após essa adjudicação poderá existir uma autoridade normativa de escopo e, em gate posterior, um exame funcional.
