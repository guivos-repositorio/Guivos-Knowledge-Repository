---
id: GKR-CANON-MATRIX-001
title: Matriz de Consolidação Canônica
status: active
version: 1.67.0
owner: Guivos
last_updated: 2026-07-24
depends_on:
  - GKR-STATE-001
related:
  - GKR-CANON-MATRIX-GKR-REMEDIATION-R3
  - GKR-REMEDIATION-002
  - M7.3.2
normative: false
---

# Matriz de Consolidação Canônica

## 1. Finalidade

Esta matriz central registra as decisões consolidadas de maior alcance e aponta para as autoridades e addenda que preservam o detalhamento. Ela não substitui documentos normativos de domínio, ADRs, validações, auditorias ou registros de decisão.

A versão anterior continha extensa duplicação de decisões já governadas em documentos especializados. Esse conteúdo permanece integralmente recuperável no histórico Git e nos addenda versionados.

## 2. Vocabulário de decisão

| Decisão | Significado |
|---|---|
| Manter | elemento permanece válido sem alteração estrutural |
| Refinar | elemento permanece, com precisão adicional |
| Unificar | elementos redundantes são consolidados sob uma autoridade |
| Remover | elemento deixa de integrar o estado canônico vigente |
| Historical only | elemento permanece apenas como evidência histórica |
| Pendente | decisão ainda depende de evidência ou autoridade competente |

## 3. Decisões estruturais vigentes

| Elemento | Decisão | Autoridade e situação |
|---|---|---|
| GKR como fonte oficial | Manter | ADR-001 e governança vigente |
| Foundation Architecture | Manter congelada | baseline A2-B3 |
| Guivos Journey | Manter | `PAS-001 1.0.0 active`; nove capacidades concluídas |
| versões anteriores do PAS-001 | Historical only | preservadas no Git, reconciliação, auditoria e publicação |
| Product Engineering | Manter pausado | antes do W0-01; execução 0% |
| Guivos Economic Model | Manter documentariamente concluído | `GEM-001` a `GEM-010`; validação real pendente |
| A2-R03 | Manter como frente arquitetural correta | temporariamente pausada pela remediação do GKR |
| COR, validação externa e COEM | Manter concluídos | 18/18 candidatos e 6/6 clusters avaliados |
| `COD-001` | Manter | `ECO-CAND-001` com `Reformulate` aceito e estado `Under Validation` |
| Outcomes canônicos | Pendente | nenhum código ou catálogo canônico criado |
| Business Capabilities | Pendente | dependem da conclusão governada do BA-STR-002 |
| Mall, Business, Intelligence, Ads, Media e Travel | Preservar para rebaseline | ordem histórica não constitui autorização de início |
| Commercial Model | Pendente | posterior ao rebaseline mínimo do portfólio |
| Go-to-Market | Pendente | posterior ao Commercial Model e aos gates de validação |
| Market Validation | Manter como trilha paralela | formulário e planilha ainda pendentes |
| Current State Register | Manter | autoridade do estado transversal vigente |
| Roadmap, Board, GEA, README e Home | Refinar como resumos | devem consumir o Current State Register |
| overlays anteriores | Historical only | preservam snapshots, não determinam o estado atual |

## 4. Decisões da remediação

| Não conformidade | Decisão | Estado |
|---|---|---|
| NC-MAJ-01 — Roadmap antigo | Refinar | corrigida em R2 |
| NC-MAJ-02 — Board antigo | Refinar | corrigida em R3 |
| NC-MAJ-03 — Milestones antigo | Refinar | corrigida em R3 |
| NC-MAJ-04 — Matrix antiga | Refinar | corrigida em R3 |
| NC-MAJ-05 — README e Home antigos | Refinar | corrigida em R1 |
| NC-MAJ-06 — navegação incompleta | Pendente | R4 |
| NC-MAJ-07 — precedência ausente | Refinar | corrigida em R1 |
| NC-MIN-01 — reordenamento ainda proposed | Refinar | corrigida em R3 |
| NC-MIN-02 — GEA anterior ao CODR | Refinar | corrigida em R1 |
| NC-MIN-03 — duplicação de estado | Refinar | corrigida progressivamente em R1–R3 |

## 5. Registro de addenda

Os addenda versionados preservam as decisões incrementais posteriores à antiga versão central 1.30.0. A navegação integral desses ativos será concluída em R4.

O addendum vigente deste incremento é `Canonical Consolidation Matrix 1.67.0 — R3 Central Controls`.

## 6. Próxima decisão de controle

Executar R4 para tornar Current State Register, CODR, auditoria, remediação, Roadmaps, Boards, Milestones, Matrices e Changelogs recentes acessíveis pela navegação oficial.

Nenhuma decisão adicional de Outcome é autorizada até o resultado `PASS` de R5.
