---
id: GKR-CHANGELOG-0.97.0
title: Changelog 0.97.0 — R5 Mechanical Validation
status: active
version: 0.97.0
owner: Guivos
last_updated: 2026-07-24
related:
  - GKR-R5-VALIDATION-001
  - M7.3.4
  - GKR-REMEDIATION-002
---

# Changelog 0.97.0 — R5 Mechanical Validation

## Added

- `scripts/validate_gkr.py` para validação de front matter, IDs, navegação e links locais;
- workflow `GKR Mechanical Validation` no GitHub Actions;
- relatório `GKR-R5-VALIDATION-001`;
- Knowledge Board 11.50.0;
- Architectural Milestones 4.48.0 — M7.3.4;
- Canonical Consolidation Matrix 1.69.0 — R5.

## Validated

- sintaxe do `mkdocs.yml`;
- front matter YAML do corpus Markdown;
- unicidade dos IDs declarados;
- existência das entradas de navegação;
- links e imagens Markdown locais;
- `git diff --check`;
- `mkdocs build --strict`;
- ausência de alterações em arquivos rastreados após os testes.

## Result

```text
R5: PASS
Critical findings open: 0
Major findings open: 0
Known Minor findings open: 0
R6: eligible after merge and explicit authorization
```

## Preserved limits

- CODR permanece em 1 de 18 decisões;
- nenhum Outcome canônico foi criado;
- AQS-O01 e Business Capabilities não foram iniciados;
- Product Engineering permanece pausado antes do W0-01;
- Market Validation não foi executada automaticamente.
