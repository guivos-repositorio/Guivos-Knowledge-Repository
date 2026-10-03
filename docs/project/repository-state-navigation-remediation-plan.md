---
id: GKR-REMEDIATION-002
title: Repository State and Navigation Remediation Plan
status: completed
version: 1.0.0
owner: Guivos Knowledge Repository
last_updated: 2026-07-24
parent: GKR-AUD-002
depends_on:
  - GKR-AUD-002
  - GEA-AUDIT-001
related:
  - GKR-STATE-001
  - GKR-R5-VALIDATION-001
  - GKR-R6-RESUMPTION-001
  - BA-STR-002-CODR-001
  - ROADMAP-11.51.0
normative: false
---

# GKR-REMEDIATION-002 — Repository State and Navigation Remediation Plan

## 1. Objetivo

Eliminar as não conformidades abertas pelo `GKR-AUD-002`, restabelecer uma única leitura do estado vigente e devolver a prioridade ao trabalho arquitetural governado.

## 2. Resultado final

| Incremento | Estado | Resultado |
|---|---|---|
| R1 — Precedência e estado global | concluído | Current State Register, README, Home e GEA reconciliados |
| R2 — Roadmap e backlog global | concluído | sequência e backlog rebaselined |
| R3 — Controles centrais | concluído | Board, Milestones, Matrix e reordenamento sincronizados |
| R4 — Navegação | concluído | autoridades vigentes acessíveis e histórico subordinado |
| R5 — Validação mecânica | `PASS` | front matter, IDs, links, navegação, diff, build e árvore aprovados |
| R6 — Retomada governada | concluído | A2-R03 e CODR retomados; ECO-CAND-003 submetido à decisão humana |

## 3. Não conformidades

```text
Critical findings open: 0
Major findings open: 0
Known Minor findings open: 0
Mechanical validation: PASS
Repository remediation: COMPLETE
```

As não conformidades `NC-MAJ-01` a `NC-MAJ-07` e `NC-MIN-01` a `NC-MIN-03` foram corrigidas conforme seus incrementos e validadas pelos controles aplicáveis.

## 4. Ativos permanentes resultantes

- `GKR-STATE-001` como autoridade transversal;
- precedência documental explícita;
- Roadmap global reconciliado;
- controles centrais concisos e atuais;
- navegação governada do MkDocs;
- histórico preservado fora do menu principal;
- `scripts/validate_gkr.py`;
- workflow `GKR Mechanical Validation`;
- relatório `GKR-R5-VALIDATION-001`;
- registro `GKR-R6-RESUMPTION-001`.

## 5. Retomada arquitetural

O R6 encerrou formalmente a pausa da remediação e retomou:

- `A2-R03 — Business Architecture Review`;
- `BA-STR-002 — Business Outcomes`;
- `BA-STR-002-CODR-001`.

A submissão `BA-STR-002-COD-SUB-002` apresenta `ECO-CAND-003` ao Fundador. Essa submissão não constitui decisão e não cria `COD-002`.

## 6. Limites preservados

A conclusão da remediação não:

- reabre o Economic Model sem condição material;
- aprova Candidate Outcomes automaticamente;
- inicia AQS-O01 ou Business Capabilities;
- especifica produtos, Commercial Model ou Go-to-Market;
- retoma Product Engineering;
- executa Market Validation automaticamente.

## 7. Critério de conclusão

```text
State precedence: explicit
Global roadmap: current
Global board: current
Navigation: complete
IDs and links: valid
mkdocs build --strict: pass
A2-R03: active
CODR: resumed
Human decision inference: blocked
```

## 8. Encerramento

Este plano está concluído. Novos trabalhos devem seguir o Roadmap e o Current State Register, sem reabrir a remediação salvo surgimento de nova não conformidade material.
