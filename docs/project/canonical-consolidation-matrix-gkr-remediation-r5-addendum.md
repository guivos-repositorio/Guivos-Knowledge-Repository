---
id: GKR-CANON-MATRIX-GKR-REMEDIATION-R5
title: Canonical Consolidation Matrix 1.69.0 — R5 Mechanical Validation
status: active
version: 1.69.0
owner: Guivos
last_updated: 2026-07-24
related:
  - GKR-STATE-001
  - GKR-REMEDIATION-002
  - GKR-R5-VALIDATION-001
  - M7.3.4
---

# Canonical Consolidation Matrix 1.69.0

| Elemento | Decisão neste incremento | Situação |
|---|---|---|
| validador mecânico | manter como controle permanente | `scripts/validate_gkr.py` |
| workflow de validação | manter | executa em pull requests e manualmente |
| front matter | validar integralmente | PASS |
| IDs declarados | exigir unicidade | PASS |
| navegação MkDocs | validar contra arquivos reais | PASS |
| links Markdown locais | exigir resolução | PASS |
| `git diff --check` | exigir aprovação | PASS |
| `mkdocs build --strict` | exigir aprovação | PASS |
| árvore rastreada | exigir ausência de mutações pelos testes | PASS |
| remediação R1–R5 | consolidar | concluída no PR do R5 |
| R6 | liberar somente após merge e autorização explícita | pendente |
| A2-R03 | preservar | ainda não retomada |
| Product Engineering | manter pausado | W0-01 em 0% |

O `PASS` mecânico não substitui validação arquitetural, empírica, jurídica, financeira, operacional ou de produção.
