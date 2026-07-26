---
id: BA-STR-002-CODR-001
title: Candidate Outcome Decision Register
status: active
version: 0.30.0
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
  - BA-STR-002-COD-SUB-015
  - BA-STR-002-COD-SUB-016
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
  - COD-014
  - COD-015
  - M7.17.1
normative: false
execution_status: in-progress
---

# BA-STR-002-CODR-001 — Candidate Outcome Decision Register

## 1. Autoridade e finalidade

Este registro preserva as decisões humanas individuais sobre as disposições recomendadas pela `BA-STR-002-COEM-001` e aponta para os documentos de submissão e resolução que mantêm o detalhamento integral de cada ato.

Uma decisão registrada aqui não cria automaticamente um Outcome canônico. Reformulações permanecem candidatas; fusões e rejeições preservam formulação, evidências, histórico e destino arquitetural.

## 2. Estado formal

```text
Decision register: in progress — resumed by R6
Candidate dispositions in scope: 18
Human decisions recorded: 15
Decision submissions awaiting human response: 1
Current submission: BUS-CAND-008
Accepted Reformulate dispositions: 9
Accepted Merge dispositions: 2
Accepted Reject dispositions: 4
Candidate state changes: 6
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
- `Reject` aceito preserva registro, formulação, evidências e destino arquitetural;
- formulações revisadas ou combinadas retornam aos quatro testes da COEM;
- nenhum código `EO-###` ou `BO-###` nasce neste registro;
- AQS-O01 e consolidação canônica permanecem atos posteriores.

## 4. Decisões registradas

| Decisão | Candidato | Recomendação aceita | Estado resultante | Destino ou formulação preservada |
|---|---|---|---|---|
| `COD-001` | `ECO-CAND-001` | Reformulate | `Under Validation` | compreensão contextual suficientemente fundamentada |
| `COD-002` | `ECO-CAND-003` | Reformulate | `Under Validation` | agência efetiva e situada |
| `COD-003` | `ECO-CAND-005` | Merge into `ECO-CAND-003` | `Merged` | continuidade adaptativa incorporada ao alvo |
| `COD-004` | `ECO-CAND-002` | Reformulate | `Under Validation` | acesso real a possibilidades legítimas e manejáveis |
| `COD-005` | `ECO-CAND-004` | Reject | `Rejected` | experiência preservada na Jornada e como evidência |
| `COD-006` | `ECO-CAND-006` | Reformulate | `Under Validation` | saúde relacional no ecossistema |
| `COD-007` | `ECO-CAND-007` | Reformulate | `Under Validation` | participação inclusiva, digna e efetiva |
| `COD-008` | `ECO-CAND-008` | Reformulate | `Under Validation` | participação protegida, justa e contestável |
| `COD-009` | `BUS-CAND-001` | Reject | `Rejected` | propósito preservado como autoridade constitucional e obrigação de governança |
| `COD-010` | `BUS-CAND-002` | Merge into `BUS-CAND-003` | `Merged` | relevância contextual incorporada ao alvo |
| `COD-011` | `BUS-CAND-003` | Reformulate | `Under Validation` | habilitação consistente e contextualmente relevante de valor legítimo |
| `COD-012` | `BUS-CAND-004` | Reformulate | `Under Validation` | legitimidade institucional sustentada; confiança como avaliação associada |
| `COD-013` | `BUS-CAND-005` | Reformulate | `Under Validation` | continuidade econômica sustentável |
| `COD-014` | `BUS-CAND-006` | Reject | `Rejected` | expansão responsável preservada como trajetória estratégica opcional |
| `COD-015` | `BUS-CAND-007` | Reject | `Rejected` | aprendizado e adaptação preservados como capacidades sustentadoras |

O detalhamento das decisões permanece nos documentos de resolução correspondentes, preservando formulações originais, evidências, autoridade, data, limites e gates.

## 5. Matriz cumulativa de disposições

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
| BUS-CAND-006 | Reject | Aceitar `Reject` | `Rejected` |
| BUS-CAND-007 | Reject | Aceitar `Reject` | `Rejected` |
| BUS-CAND-008 | Reject | — | Pending human decision; `BA-STR-002-COD-SUB-016` aberto |
| BUS-CAND-009 | Reject | — | Pending human decision |
| BUS-CAND-010 | Merge into BUS-CAND-005 | — | Pending human decision |

## 6. Submissão humana vigente

`BA-STR-002-COD-SUB-016` submete `BUS-CAND-008 — Saúde das relações de parceria` à decisão humana sobre `Reject`.

A recomendação propõe retirar o candidato do futuro catálogo de Business Outcomes e preservar seu conteúdo na arquitetura de capacidades, governança de parceiros e critérios de portfólio. Ela não reduz a importância estratégica das parcerias, não exige internalização e não antecipa decisões legítimas de entrada, evolução, renovação, substituição ou saída.

## 7. Gate do incremento

| Critério | Resultado |
|---|---|
| submissão individual criada | Pass |
| recomendação original preservada | Pass |
| resultados `Partial / Pass / Pass / Fail` preservados | Pass |
| parceria separada de Outcome permanente | Pass |
| governança de parceiros preservada na arquitetura | Pass |
| `COD-016` não criado | Pass |
| COR inalterado | Pass |
| promoção canônica bloqueada | Pass |
| AQS-O01 não antecipado | Pass |
| Product Engineering preservado em pausa | Pass |

## 8. Próximo passo governado

Receber a manifestação do Fundador sobre `BA-STR-002-COD-SUB-016`. Nenhuma decisão posterior será registrada automaticamente.
