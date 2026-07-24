---
id: GKR-REMEDIATION-002
title: Repository State and Navigation Remediation Plan
status: proposed
version: 0.1.0
owner: Guivos Knowledge Repository
last_updated: 2026-07-24
parent: GKR-AUD-002
depends_on:
  - GKR-AUD-002
  - GEA-AUDIT-001
related:
  - BA-STR-002-CODR-001
  - GEM-CLOSURE-REVIEW-001
normative: false
---

# GKR-REMEDIATION-002 — Repository State and Navigation Remediation Plan

## 1. Objetivo

Eliminar as não conformidades abertas pelo `GKR-AUD-002`, restabelecer uma única leitura do estado vigente e impedir que documentos históricos concorram com os overlays atuais.

## 2. Princípios de correção

- preservar integralmente o histórico;
- não apagar decisões ou versões anteriores;
- tornar explícita a precedência documental;
- reduzir duplicação de estado em superfícies globais;
- separar estado atual, histórico e backlog futuro;
- não alterar conteúdo arquitetural apenas para corrigir navegação;
- validar mecanicamente o resultado antes da integração final.

## 3. Estratégia de organização

### Superfície única de estado atual

Criar ou consolidar um `Current State Register` curto, responsável por declarar:

- era e marco vigentes;
- frente estratégica ativa;
- domínios concluídos, pausados e pendentes;
- próximo incremento autorizado;
- trilhas paralelas;
- documento de sequência global vigente.

README, Home, Roadmap, Board e GEA deverão consumir esse registro e evitar listas independentes extensas.

### Separação entre atual e histórico

| Classe | Tratamento |
|---|---|
| documento de estado vigente | `status: active` e referência explícita ao predecessor |
| overlay versionado anterior | preservado como histórico de estado |
| documento central desatualizado | atualizado ou classificado como `historical` com `superseded_by` |
| backlog superado | preservado em seção histórica, fora do próximo incremento |
| decisão de reordenamento executada | atualizar de `proposed` para estado executado ou histórico |

## 4. Incrementos de remediação

### R1 — Precedência e estado global

Corrigir:

- `README.md`;
- `docs/index.md`;
- `docs/enterprise-architecture/index.md`;
- registro de estado atual;
- regra de precedência entre documento central e overlay.

**Saída:** M7.2 e COD-001 visíveis nas entradas principais.

### R2 — Roadmap e backlog global

Reconciliar:

- `docs/roadmap.md`;
- backlog histórico do Journey;
- conclusão documental do Economic Model;
- A2-R03 como frente atual;
- sequência de Business Architecture;
- backlog dos seis produtos;
- Commercial Model e Go-to-Market;
- trilha paralela de Market Validation.

**Saída:** um backlog global rebaselined, sem itens concluídos apresentados como futuros.

### R3 — Controles centrais

Reconciliar:

- `docs/project/knowledge-board.md`;
- `docs/project/architectural-milestones.md`;
- `docs/project/canonical-consolidation-matrix.md`;
- referências de changelog e versões.

**Saída:** controles centrais sincronizados com overlays 11.45, 4.43, 1.64 e 0.92.

### R4 — Navegação

Atualizar `mkdocs.yml` para incluir:

- Candidate Outcome Decision Register;
- M7.2;
- Roadmap 11.45.0 e posterior;
- Knowledge Board 11.45.0 e posterior;
- Canonical Consolidation Matrix 1.64.0 e posterior;
- Changelog 0.92.0 e posterior;
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
- preservar a trilha de Market Validation como frente paralela.

## 5. Priorização

| Prioridade | Item | Motivo |
|---|---|---|
| P0 | precedência documental e entradas principais | elimina ambiguidade imediata |
| P0 | roadmap e backlog global | restabelece a rota oficial |
| P0 | navegação dos ativos vigentes | evita ativos órfãos |
| P1 | controles centrais | consolida governança e histórico |
| P1 | validação mecânica integral | comprova integridade da correção |
| P2 | redução estrutural de duplicação | previne recorrência de drift |

## 6. Limites

A remediação não:

- reabre o Economic Model sem condição material;
- altera o conteúdo de `COD-001`;
- toma decisões sobre outros Candidate Outcomes;
- inicia AQS-O01;
- especifica Mall ou outros produtos;
- cria Commercial Model ou Go-to-Market;
- retoma Product Engineering;
- executa Market Validation automaticamente.

## 7. Critério de conclusão

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

## 8. Próximo incremento proposto

Executar `R1 — Precedência e estado global` e `R2 — Roadmap e backlog global` em um PR isolado. A atualização deverá preservar documentos históricos e apresentar claramente a sequência Journey → Economic Model → Business Architecture → Product Portfolio → Commercial Model → Go-to-Market.
