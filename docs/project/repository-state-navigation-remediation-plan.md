---
id: GKR-REMEDIATION-002
title: Repository State and Navigation Remediation Plan
status: active
version: 0.5.0
owner: Guivos Knowledge Repository
last_updated: 2026-07-24
parent: GKR-AUD-002
depends_on:
  - GKR-AUD-002
  - GEA-AUDIT-001
related:
  - GKR-STATE-001
  - BA-STR-002-CODR-001
  - GEM-CLOSURE-REVIEW-001
  - GKR-R5-VALIDATION-001
  - ROADMAP-11.50.0
normative: false
---

# GKR-REMEDIATION-002 — Repository State and Navigation Remediation Plan

## 1. Objetivo

Eliminar as não conformidades abertas pelo `GKR-AUD-002`, restabelecer uma única leitura do estado vigente e impedir que documentos históricos concorram com o estado atual.

## 2. Estado de execução

| Incremento | Estado | Resultado |
|---|---|---|
| R1 — Precedência e estado global | concluído | `GKR-STATE-001`, README, Home e GEA reconciliados |
| R2 — Roadmap e backlog global | concluído | Roadmap central reestruturado e backlog rebaselined |
| R3 — Controles centrais | concluído | Board, Milestones, Matrix e reordenamento sincronizados |
| R4 — Navegação | concluído | autoridades vigentes acessíveis e histórico subordinado |
| R5 — Validação mecânica | `PASS` neste PR | front matter, IDs, links, navegação, diff, build e árvore aprovados |
| R6 — Retomada governada | próximo após integração | retorno controlado ao CODR |

## 3. Situação das não conformidades

| ID | Estado após R5 |
|---|---|
| NC-MAJ-01 — Roadmap central desatualizado | corrigida e validada |
| NC-MAJ-02 — Knowledge Board central desatualizado | corrigida e validada |
| NC-MAJ-03 — Architectural Milestones central desatualizado | corrigida e validada |
| NC-MAJ-04 — Matriz Canônica central desatualizada | corrigida e validada |
| NC-MAJ-05 — README e Home desatualizados | corrigida e validada |
| NC-MAJ-06 — navegação incompleta | corrigida e validada |
| NC-MAJ-07 — precedência documental ausente | corrigida e validada |
| NC-MIN-01 — reordenamento ainda `proposed` | corrigida |
| NC-MIN-02 — GEA anterior ao CODR | corrigida |
| NC-MIN-03 — duplicação de estado | corrigida progressivamente |

```text
Critical findings open: 0
Major findings open: 0
Known Minor findings open: 0
Mechanical validation: PASS
```

## 4. Princípios preservados

- histórico integral preservado;
- decisões e versões anteriores não apagadas;
- precedência documental explícita;
- estado atual separado do histórico e do backlog futuro;
- conteúdo arquitetural não alterado apenas para corrigir navegação;
- retomada da A2-R03 condicionada ao R6.

## 5. Incrementos concluídos

### R1 — Precedência e estado global

- Current State Register criado;
- README, Home e GEA reconciliados;
- precedência documental explicitada.

### R2 — Roadmap e backlog global

- Journey registrado como concluído;
- Economic Model registrado como documentariamente concluído;
- A2-R03 preservada;
- ciclo Outcomes → Business Capabilities explicitado;
- portfólio, Commercial Model, Go-to-Market e Market Validation rebaselined.

### R3 — Controles centrais

- Knowledge Board, Milestones e Matrix atualizados;
- reordenamento Journey → Economic Model classificado como executado;
- versões e referências de controle reconciliadas.

### R4 — Navegação

- autoridades vigentes priorizadas no `mkdocs.yml`;
- CODR, auditoria, remediação e registros recentes expostos;
- histórico preservado fora do menu principal e disponível na pesquisa.

### R5 — Validação mecânica

- validador permanente criado;
- workflow GitHub Actions incorporado;
- front matter, IDs, links locais e navegação aprovados;
- `git diff --check` aprovado;
- `mkdocs build --strict` aprovado;
- árvore rastreada permaneceu limpa.

## 6. R6 — Retomada governada

Após integração deste PR e autorização explícita:

1. encerrar formalmente a pausa de remediação;
2. retomar `BA-STR-002-CODR-001`;
3. submeter `ECO-CAND-003` à decisão humana individual;
4. preservar Market Validation como frente paralela;
5. manter Product Engineering pausado antes do W0-01.

## 7. Limites

A remediação não:

- reabre o Economic Model sem condição material;
- altera o conteúdo de `COD-001`;
- toma decisões sobre outros Candidate Outcomes;
- inicia AQS-O01 ou Business Capabilities;
- especifica Mall ou outros produtos;
- cria Commercial Model ou Go-to-Market;
- retoma Product Engineering;
- executa Market Validation automaticamente.

## 8. Critério de conclusão

```text
Critical findings open: 0
Major findings open: 0
Minor findings: corrected or accepted with owner and due gate
State precedence: explicit
Global roadmap: current
Global board: current
Navigation: complete
IDs and links: valid
mkdocs build --strict: pass
A2-R03 continuation gate: eligible for R6
```

## 9. Próximo incremento

Executar R6 somente após a integração do PR do R5 e nova autorização explícita.
