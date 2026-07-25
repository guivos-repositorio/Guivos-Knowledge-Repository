---
id: GKR-REMEDIATION-002
title: Repository State and Navigation Remediation Plan
status: active
version: 0.4.0
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
  - ROADMAP-11.49.0
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
| R4 — Navegação | concluído neste incremento | autoridades vigentes e registros recentes acessíveis no site oficial |
| R5 — Validação mecânica | próximo | IDs, links, front matter, diff e build estrito |
| R6 — Retomada governada | bloqueado | retorno ao CODR após resultado `PASS` |

## 3. Situação das não conformidades

| ID | Estado após R4 |
|---|---|
| NC-MAJ-01 — Roadmap central desatualizado | corrigida em R2 |
| NC-MAJ-02 — Knowledge Board central desatualizado | corrigida em R3 |
| NC-MAJ-03 — Architectural Milestones central desatualizado | corrigida em R3 |
| NC-MAJ-04 — Matriz Canônica central desatualizada | corrigida em R3 |
| NC-MAJ-05 — README e Home desatualizados | corrigida em R1 |
| NC-MAJ-06 — navegação incompleta | corrigida documentalmente em R4; confirmação mecânica pendente em R5 |
| NC-MAJ-07 — precedência documental ausente | corrigida em R1 |
| NC-MIN-01 — reordenamento ainda `proposed` | corrigida em R3 |
| NC-MIN-02 — GEA anterior ao CODR | corrigida em R1 |
| NC-MIN-03 — duplicação de estado | corrigida progressivamente em R1–R4 |

Não há achado Critical ou Major conhecido após R4. R5 deverá confirmar ou reabrir achados com base em evidência mecânica.

## 4. Princípios de correção

- preservar integralmente o histórico;
- não apagar decisões ou versões anteriores;
- manter precedência documental explícita;
- reduzir duplicação de estado em superfícies globais;
- separar estado atual, histórico e backlog futuro;
- não alterar conteúdo arquitetural apenas para corrigir navegação;
- validar mecanicamente o resultado antes da retomada da A2-R03.

## 5. Estratégia de organização

### 5.1 Superfície única de estado atual

O [GKR-STATE-001 — Current State Register](current-state-register.md) declara era, marco, frente estratégica, frente de controle, domínios concluídos, pausas, trilhas paralelas e próximo incremento.

README, Home, Roadmap, Board, GEA e navegação devem consumir esse registro e evitar estados independentes.

### 5.2 Separação entre atual e histórico

| Classe | Tratamento |
|---|---|
| autoridade normativa do domínio | preserva definição, decisão e conteúdo arquitetural |
| Current State Register | governa estado transversal e próximo incremento |
| menu oficial | prioriza autoridades vigentes e registros recentes |
| documento fora do menu | permanece construído, pesquisável e acessível por link |
| overlay versionado anterior | preserva snapshot histórico |
| backlog superado | permanece em histórico, fora do trabalho futuro |
| decisão executada | classificada como executada e subordinada ao estado atual |

## 6. Incrementos concluídos

### R1 — Precedência e estado global

- criação do Current State Register;
- reconciliação de README e Home;
- atualização da GEA;
- regra de precedência explícita.

### R2 — Roadmap e backlog global

- Journey registrado como concluído;
- Economic Model registrado como documentariamente concluído;
- A2-R03 preservada;
- ciclo Outcomes → Business Capabilities explicitado;
- backlog dos seis produtos rebaselined;
- Commercial Model, Go-to-Market e Market Validation preservados.

### R3 — Controles centrais

- Knowledge Board central atualizado;
- Architectural Milestones central atualizado;
- Matriz de Consolidação Canônica central atualizada;
- reordenamento Journey → Economic Model classificado como `executed`;
- referências de controle e changelog registradas.

### R4 — Navegação

- Current State Register e controles centrais incluídos no menu;
- Candidate Outcome Decision Register incluído;
- auditoria e plano de remediação incluídos;
- autoridades principais de Journey, Economic Model e Business Architecture priorizadas;
- últimos Boards, Milestones, Matrices e Changelogs incluídos;
- documentos históricos mantidos no build e na pesquisa por `not_in_nav`;
- menu reduzido para evitar concorrência entre versões antigas e estado atual.

## 7. Incrementos remanescentes

### R5 — Validação mecânica

Executar:

- validação de front matter;
- unicidade de IDs;
- resolução de links relativos;
- resolução de entradas de navegação;
- validação da política `not_in_nav`;
- `git diff --check`;
- `mkdocs build --strict`;
- comparação da árvore remota com a árvore validada.

**Saída:** parecer `PASS` ou bloqueio documentado.

### R6 — Retomada governada

Após `PASS`:

- encerrar a pausa de reconciliação;
- retomar `BA-STR-002-CODR-001`;
- submeter `ECO-CAND-003` à decisão humana individual;
- preservar Market Validation como frente paralela.

## 8. Limites

A remediação não:

- reabre o Economic Model sem condição material;
- altera o conteúdo de `COD-001`;
- toma decisões sobre outros Candidate Outcomes;
- inicia AQS-O01 ou Business Capabilities;
- especifica Mall ou outros produtos;
- cria Commercial Model ou Go-to-Market;
- retoma Product Engineering;
- executa Market Validation automaticamente.

## 9. Critério de conclusão

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
A2-R03 continuation gate: open
```

## 10. Próximo incremento proposto

Executar `R5 — Validação mecânica` em PR isolado. R6 continuará bloqueado até parecer `PASS`.