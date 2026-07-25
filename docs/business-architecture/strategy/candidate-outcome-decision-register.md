---
id: BA-STR-002-CODR-001
title: Candidate Outcome Decision Register
status: active
version: 0.26.0
owner: Guivos Business Architecture
last_updated: 2026-07-25
parent: BA-STR-002
depends_on:
  - BA-STR-002-COR-001
  - BA-STR-002-COEM-001
  - GKR-GOV-OUT-001
related:
  - BA-STR-002-EOVB-001
  - BA-STR-002-EOVB-002
  - BA-STR-002-EOVB-003
  - BA-STR-002-EOVB-004
  - BA-STR-002-EOVB-005
  - BA-STR-002-EOVB-006
  - RP-001-EVIDENCE
  - GKR-R6-RESUMPTION-001
  - BA-STR-002-COD-SUB-002
  - BA-STR-002-COD-SUB-003
  - BA-STR-002-COD-SUB-004
  - BA-STR-002-COD-SUB-005
  - BA-STR-002-COD-SUB-006
  - BA-STR-002-COD-SUB-007
  - BA-STR-002-COD-SUB-008
  - BA-STR-002-COD-SUB-009
  - BA-STR-002-COD-SUB-010
  - BA-STR-002-COD-SUB-011
  - BA-STR-002-COD-SUB-012
  - BA-STR-002-COD-SUB-013
  - BA-STR-002-COD-SUB-014
  - COD-001
  - COD-002
  - COD-003
  - COD-004
  - COD-005
  - COD-006
  - COD-007
  - COD-008
  - COD-009
  - COD-010
  - COD-011
  - COD-012
  - COD-013
  - M7.15.1
normative: false
execution_status: in-progress
---

# BA-STR-002-CODR-001 — Candidate Outcome Decision Register

## 1. Autoridade e finalidade

Este registro preserva as decisões humanas individuais sobre as disposições recomendadas pela `BA-STR-002-COEM-001`.

Mantém separados:

1. formulação originalmente avaliada;
2. resultados dos quatro testes da COEM;
3. disposição recomendada;
4. decisão humana explícita;
5. formulação revisada, alvo de fusão ou destino arquitetural;
6. mudança de estado no COR;
7. futura consolidação na Canon.

Uma decisão registrada aqui não cria automaticamente um Outcome canônico. Reformulações permanecem candidatas; fusões e rejeições preservam rastreabilidade.

## 2. Estado formal

```text
Decision register: in progress — resumed by R6
Candidate dispositions in scope: 18
Human decisions recorded: 13
Decision submissions awaiting human response: 1
Current submission: BUS-CAND-006
Accepted Reformulate dispositions: 9
Accepted Merge dispositions: 2
Accepted Reject dispositions: 2
Candidate state changes: 4
Approved Outcomes: 0
Canonical EO/BO codes: 0
AQS-O01: not started
Operational authorization: no
```

## 3. Regras permanentes

- cada candidato recebe decisão individual;
- nenhuma decisão é inferida por contagem de testes ou decisão de outro candidato;
- `Reformulate` aceito não equivale a `Approved`;
- `Merge` aceito não aprova automaticamente o alvo;
- `Reject` aceito preserva registro, formulação e evidências;
- formulações revisadas ou combinadas retornam aos quatro testes da COEM;
- candidatos fundidos ou rejeitados permanecem rastreáveis;
- nenhum código `EO-###` ou `BO-###` nasce neste registro;
- AQS-O01 e consolidação canônica permanecem atos posteriores.

## 4. Decisões registradas

| Decisão | Candidato | Disposição aceita | Estado resultante |
|---|---|---|---|
| `COD-001` | `ECO-CAND-001` | `Reformulate` | `Under Validation` |
| `COD-002` | `ECO-CAND-003` | `Reformulate` | `Under Validation` |
| `COD-003` | `ECO-CAND-005` | `Merge into ECO-CAND-003` | `Merged` |
| `COD-004` | `ECO-CAND-002` | `Reformulate` | `Under Validation` |
| `COD-005` | `ECO-CAND-004` | `Reject` | `Rejected` |
| `COD-006` | `ECO-CAND-006` | `Reformulate` | `Under Validation` |
| `COD-007` | `ECO-CAND-007` | `Reformulate` | `Under Validation` |
| `COD-008` | `ECO-CAND-008` | `Reformulate` | `Under Validation` |
| `COD-009` | `BUS-CAND-001` | `Reject` | `Rejected` |
| `COD-010` | `BUS-CAND-002` | `Merge into BUS-CAND-003` | `Merged` |
| `COD-011` | `BUS-CAND-003` | `Reformulate` | `Under Validation` |
| `COD-012` | `BUS-CAND-004` | `Reformulate` | `Under Validation` |
| `COD-013` | `BUS-CAND-005` | `Reformulate` | `Under Validation` |

### Formulações empresariais vigentes registradas

#### BUS-CAND-003 — Habilitação consistente e contextualmente relevante de valor legítimo

> A Guivos sustenta condições para habilitar valor legítimo com consistência e relevância contextual, detectando mudanças materiais e ajustando proposições, capacidades e respostas de forma coerente, sem presumir controle unilateral sobre o valor realizado pelos participantes nem tratar personalização, satisfação pontual, disponibilidade técnica ou velocidade de resposta como prova suficiente.

#### BUS-CAND-004 — Legitimidade institucional sustentada

> A legitimidade institucional da Guivos é sustentada perante participantes e stakeholders por conduta coerente, governança responsável, transparência, contestabilidade e reparação verificáveis, sem presumir controle unilateral sobre avaliações socialmente conferidas nem tratar reputação, conformidade, satisfação, confiança declarada ou longevidade das relações como prova suficiente.

#### BUS-CAND-005 — Continuidade econômica sustentável

> A Guivos sustenta condições econômicas suficientes para cumprir obrigações e preservar valor essencial em múltiplos horizontes, mantendo opções legítimas de financiamento, alocação e renovação sem presumir permanência absoluta nem tratar receita, margem, caixa, disponibilidade operacional ou crescimento isolados como prova suficiente.

## 5. Matriz cumulativa de decisões

| Candidato | Recomendação da COEM | Decisão humana | Estado decisório |
|---|---|---|---|
| ECO-CAND-001 | Reformulate | Aceitar `Reformulate` | nova COEM pendente |
| ECO-CAND-003 | Reformulate | Aceitar `Reformulate` | formulação combinada pendente de nova COEM |
| ECO-CAND-005 | Merge into ECO-CAND-003 | Aceitar `Merge into ECO-CAND-003` | `Merged` |
| ECO-CAND-002 | Reformulate | Aceitar `Reformulate` | nova COEM pendente |
| ECO-CAND-004 | Reject | Aceitar `Reject` | `Rejected` |
| ECO-CAND-006 | Reformulate | Aceitar `Reformulate` | nova COEM pendente |
| ECO-CAND-007 | Reformulate | Aceitar `Reformulate` | nova COEM pendente |
| ECO-CAND-008 | Reformulate | Aceitar `Reformulate` | nova COEM pendente |
| BUS-CAND-001 | Reject | Aceitar `Reject` | `Rejected` |
| BUS-CAND-002 | Merge into BUS-CAND-003 | Aceitar `Merge into BUS-CAND-003` | `Merged` |
| BUS-CAND-003 | Reformulate | Aceitar `Reformulate` | nova COEM pendente |
| BUS-CAND-004 | Reformulate | Aceitar `Reformulate` | nova COEM pendente |
| BUS-CAND-005 | Reformulate | Aceitar `Reformulate` | nova COEM pendente |
| BUS-CAND-006 | Reject | — | Pending human decision; `BA-STR-002-COD-SUB-014` aberto |
| BUS-CAND-007 | Reject | — | Pending human decision |
| BUS-CAND-008 | Reject | — | Pending human decision |
| BUS-CAND-009 | Reject | — | Pending human decision |
| BUS-CAND-010 | Merge into BUS-CAND-005 | — | Pending human decision |

## 6. Submissão humana vigente

`BA-STR-002-COD-SUB-014` submete `BUS-CAND-006 — Crescimento responsável e resiliente` à decisão humana sobre `Reject`.

A recomendação propõe retirar crescimento do futuro catálogo de Business Outcomes, preservando expansão responsável como trajetória estratégica opcional, condicionada à capacidade demonstrada, adicionalidade e não degradação.

A recomendação não proíbe crescimento, não rejeita a importância de ampliar alcance e valor e não altera `BUS-CAND-006` antes da manifestação humana.

## 7. Gate do incremento

| Critério | Resultado |
|---|---|
| submissão individual criada | Pass |
| recomendação original preservada | Pass |
| quatro testes preservados | Pass |
| crescimento separado de Outcome permanente | Pass |
| expansão responsável preservada como trajetória opcional | Pass |
| resiliência preservada como propriedade ou capacidade sustentadora | Pass |
| `COD-014` não criado | Pass |
| COR inalterado | Pass |
| promoção canônica bloqueada | Pass |
| AQS-O01 não antecipado | Pass |
| Product Engineering preservado em pausa | Pass |

## 8. Próximo passo governado

Receber a manifestação do Fundador sobre `BA-STR-002-COD-SUB-014`. Nenhuma decisão posterior será registrada automaticamente.
