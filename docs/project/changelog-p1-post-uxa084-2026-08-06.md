---
id: GKR-CHANGELOG-P1-POST-UXA084-001
title: Registro da Reconstrução do P1 após UXA-084
status: draft
version: 1.0.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-06
depends_on:
  - GKR-P1-REBASELINE-001
  - GKR-STATE-001
related:
  - GKR-SEMANTIC-SYNC-001
  - GKR-UXA-047-084-INDEX-001
normative: false
---

# Registro da Reconstrução do P1 após UXA-084

## Baseline

- `main`: `795008499867de1820cd28b1dcef8db2e89da2f1`;
- `GKR-STATE-001`: 2.10.0;
- marco: M7.72;
- última frente integrada: UXA-084;
- P0: integrado pelo PR nº 181.

## Alterações

- README ressincronizado;
- Home do MkDocs ressincronizada;
- sequência UXA-047 a UXA-084 indexada;
- índice de changelogs reconstruído;
- índice dos adendos canônicos reconstruído;
- política semântica atualizada para derivação dinâmica;
- validador semântico reconstruído;
- workflow de validação semântica criado;
- rebaseline do P1 registrado.

## Correções de desvio

- removida a dependência fixa de “UXA-071 não iniciada”;
- impedida a integração direta do snapshot do PR nº 163;
- preservada a árvore atual do MkDocs;
- corrigidas as superfícies que ainda apresentavam estado anterior à UXA-084;
- restaurada a descobribilidade das UXA-047 a UXA-084.

## Estado preservado

- nenhuma mudança em `GKR-STATE-001`;
- galeria visual permanece `draft` 0.4.0;
- matriz por SVG permanece `draft` 0.2.0;
- ressalvas da UXA-084 permanecem abertas;
- UXA-085 não iniciada;
- Engenharia de Produto pausada antes de W0-01;
- nenhum Resultado Empresarial canônico;
- P2–P9 não iniciados.

## Validação requerida

O registro somente poderá ser considerado integrado após aprovação dos workflows mecânico e semântico no head exato do pull request e decisão governada de merge.
