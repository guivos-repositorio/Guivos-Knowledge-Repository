---
id: GKR-ARCHITECTURAL-MILESTONES-001
title: Architectural Milestones
status: active
version: 4.48.0
owner: Guivos
last_updated: 2026-07-24
depends_on:
  - GKR-STATE-001
related:
  - ROADMAP-11.50.0
  - GKR-REMEDIATION-002
  - GKR-R5-VALIDATION-001
  - M7.3.4
normative: false
---

# Architectural Milestones

## 1. Autoridade

Este registro apresenta os marcos arquiteturais vigentes em visão consolidada. Os documentos `architectural-milestones-*.md` preservam os snapshots e critérios detalhados de cada incremento. O estado transversal é governado pelo [Current State Register](current-state-register.md).

## 2. Linha de maturidade consolidada

| Faixa | Estado | Resultado principal |
|---|---|---|
| A0–A1 | Completed | fundação do GKR e macroestrutura institucional |
| M3–M4 | Completed | Foundation congelada, método fundamental e Knowledge Architecture estabelecidos |
| M5–M5.18 | Completed | consolidação progressiva da arquitetura funcional e publicação do Journey |
| M6.0–M6.10 | Completed | desenvolvimento e fechamento documental do Guivos Economic Model |
| M7.0–M7.1.5 | Completed | início da A2-R03, COR, validação externa e COEM concluídos |
| M7.2 | Completed | ciclo de decisões humanas iniciado; `COD-001` registrado |
| M7.3 | Completed | auditoria de estado e sequência concluída |
| M7.3.1 | Completed | precedência documental e Roadmap global reconciliados |
| M7.3.2 | Completed | controles centrais reconciliados |
| M7.3.3 | Completed | navegação oficial reconciliada |
| M7.3.4 | Completed neste PR | validação mecânica integral aprovada |

## 3. Marco vigente

### M7.3.4 — Repository Mechanical Validation Completed

**Critérios atendidos:**

- workflow reproduzível incorporado ao repositório;
- front matter YAML validado;
- IDs declarados validados como únicos;
- entradas do `mkdocs.yml` resolvidas;
- links e imagens Markdown locais resolvidos;
- `git diff --check` aprovado;
- `mkdocs build --strict` aprovado;
- árvore rastreada permaneceu limpa após os testes;
- zero achados Critical, Major ou Minor conhecidos abertos;
- R6 preservado como próximo incremento após integração e autorização explícita.

## 4. Estado das revisões A2

| Revisão | Estado |
|---|---|
| A2-R01 — Foundation Architecture Review | Completed — Frozen in A2-B3 |
| A2-R02 — Fundamental Model Review | Execution Ready — Operationally Paused |
| A2-R03 — Business Architecture Review | Active — Awaiting Governed Resumption |
| A2-R04 — Product Architecture Review | Planned |
| A2-R05 — Cross-Architecture Review | Planned |

A A2-R03 não foi cancelada. Sua execução será retomada somente pelo R6, começando pela decisão individual de `ECO-CAND-003`.

## 5. Próximo marco candidato

`M7.3.5 — Governed Architectural Work Resumed`, correspondente ao R6.

## 6. Regra de transição

Um marco somente muda de estado quando seus critérios estiverem demonstrados no GKR. Marcos históricos não determinam o ponto de retomada atual quando existir registro posterior aprovado.
