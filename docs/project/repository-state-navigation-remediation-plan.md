---
id: GKR-REMEDIATION-002
title: Repository State and Navigation Remediation Plan
status: active
version: 0.2.0
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
  - ROADMAP-11.47.0
normative: false
---

# GKR-REMEDIATION-002 — Repository State and Navigation Remediation Plan

## 1. Objetivo

Eliminar as não conformidades abertas pelo `GKR-AUD-002`, restabelecer uma única leitura do estado vigente e impedir que documentos históricos concorram com o estado atual.

## 2. Estado de execução

| Incremento | Estado | Resultado |
|---|---|---|
| R1 — Precedência e estado global | concluído neste incremento | `GKR-STATE-001`, README, Home e GEA reconciliados |
| R2 — Roadmap e backlog global | concluído neste incremento | Roadmap central reestruturado e backlog rebaselined |
| R3 — Controles centrais | próximo | Board, Milestones, Matrix e referências centrais |
| R4 — Navegação | pendente | `mkdocs.yml` e ativos recentes acessíveis |
| R5 — Validação mecânica | pendente | IDs, links, front matter, diff e build estrito |
| R6 — Retomada governada | bloqueado | retorno ao CODR após resultado `PASS` |

## 3. Princípios de correção

- preservar integralmente o histórico;
- não apagar decisões ou versões anteriores;
- manter precedência documental explícita;
- reduzir duplicação de estado em superfícies globais;
- separar estado atual, histórico e backlog futuro;
- não alterar conteúdo arquitetural apenas para corrigir navegação;
- validar mecanicamente o resultado antes da retomada da A2-R03.

## 4. Estratégia de organização

### 4.1 Superfície única de estado atual

O [GKR-STATE-001 — Current State Register](current-state-register.md) passa a declarar:

- era e marco vigentes;
- frente estratégica e frente de controle;
- domínios concluídos, pausados e pendentes;
- próximo incremento autorizado;
- trilhas paralelas;
- sequência global vigente.

README, Home, Roadmap, Board e GEA devem consumir esse registro e evitar estados independentes.

### 4.2 Separação entre atual e histórico

| Classe | Tratamento |
|---|---|
| autoridade normativa do domínio | preserva definição, decisão e conteúdo arquitetural |
| Current State Register | governa estado transversal e próximo incremento |
| documento central de navegação | resume e referencia o estado vigente |
| overlay versionado anterior | preserva snapshot histórico |
| backlog superado | permanece em histórico, fora do trabalho futuro |
| decisão de reordenamento executada | deve ser classificada como executada ou histórica em R3/R4 |

## 5. Incrementos de remediação

### R1 — Precedência e estado global — concluído

Executado:

- criação de `GKR-STATE-001`;
- reconciliação de `README.md`;
- reconciliação de `docs/index.md`;
- atualização de `GEA-000` para 1.9.0;
- regra de precedência documental explícita.

**Resultado:** entradas principais apresentam o mesmo estado e não criam rotas paralelas.

### R2 — Roadmap e backlog global — concluído

Executado:

- substituição do roadmap central desatualizado;
- registro de Journey como concluído;
- registro do Economic Model como documentariamente concluído;
- preservação da A2-R03 como sequência autorizada;
- detalhamento do ciclo Outcomes → Business Capabilities;
- preservação e rebaseline do backlog dos seis produtos;
- Commercial Model e Go-to-Market mantidos como ciclos posteriores;
- Market Validation preservada como trilha operacional paralela.

**Resultado:** itens concluídos não são mais apresentados como trabalho futuro.

### R3 — Controles centrais — próximo

Reconciliar:

- `docs/project/knowledge-board.md`;
- `docs/project/architectural-milestones.md`;
- `docs/project/canonical-consolidation-matrix.md`;
- referências de changelog e versões;
- estado da decisão de reordenamento Journey → Economic Model.

**Saída:** controles centrais sincronizados com `GKR-STATE-001` e com os overlays atuais.

### R4 — Navegação

Atualizar `mkdocs.yml` para incluir:

- Current State Register;
- Candidate Outcome Decision Register;
- marcos M7.2, M7.3 e posteriores;
- Roadmaps, Boards, Matrices e Changelogs recentes;
- auditoria e plano de remediação.

**Saída:** todos os ativos vigentes acessíveis pelo site oficial.

### R5 — Validação mecânica

Executar:

- validação de front matter;
- unicidade de IDs;
- resolução de links relativos;
- resolução de entradas de navegação;
- `git diff --check`;
- `mkdocs build --strict`;
- comparação da árvore remota com a árvore validada.

**Saída:** nenhuma não conformidade Critical ou Major aberta.

### R6 — Retomada governada

Após `PASS` da auditoria de correção:

- encerrar a pausa de reconciliação;
- retomar `BA-STR-002-CODR-001`;
- submeter `ECO-CAND-003` à decisão humana individual;
- preservar Market Validation como frente paralela.

## 6. Priorização remanescente

| Prioridade | Item | Motivo |
|---|---|---|
| P0 | controles centrais | elimina estados antigos ainda apresentados como oficiais |
| P0 | navegação dos ativos vigentes | evita autoridades órfãs |
| P0 | validação mecânica integral | comprova a integridade da correção |
| P1 | classificação de documentos históricos | reduz risco de novo drift |
| P2 | redução adicional de duplicação | previne recorrência no longo prazo |

## 7. Limites

A remediação não:

- reabre o Economic Model sem condição material;
- altera o conteúdo de `COD-001`;
- toma decisões sobre outros Candidate Outcomes;
- inicia AQS-O01;
- inicia Business Capabilities;
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
A2-R03 continuation gate: open
```

## 9. Próximo incremento

Executar `R3 — Controles centrais` em PR isolado. A integração deverá atualizar Board, Milestones, Matrix e referências centrais sem avançar para `ECO-CAND-003`.
