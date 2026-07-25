---
id: BA-STR-002-CODR-001
title: Candidate Outcome Decision Register
status: active
version: 0.22.0
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
  - M7.13.1
normative: false
execution_status: in-progress
---

# BA-STR-002-CODR-001 — Candidate Outcome Decision Register

## 1. Autoridade e finalidade

Este registro preserva as decisões humanas individuais sobre as disposições recomendadas pela `BA-STR-002-COEM-001`.

Ele mantém separados:

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
Human decisions recorded: 11
Decision submissions awaiting human response: 1
Current submission: BUS-CAND-004
Accepted Reformulate dispositions: 7
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

### COD-001 — ECO-CAND-001

| Campo | Registro |
|---|---|
| Recomendação | `Reformulate` |
| Decisão humana | Aceitar `Reformulate` |
| Data | 24/07/2026 |
| Estado resultante | `Under Validation` |

> Pessoas, Organizações e Coletivos formam e revisam uma compreensão contextual suficientemente fundamentada sobre sua situação, objetivos, necessidades, restrições e possibilidades, fortalecendo sua capacidade de realizar escolhas conscientes.

### COD-002 — ECO-CAND-003

| Campo | Registro |
|---|---|
| Recomendação | `Reformulate` |
| Decisão humana | Aceitar `Reformulate` |
| Data | 24/07/2026 |
| Estado resultante | `Under Validation` |

> O ecossistema preserva condições reais, contextualmente adequadas e não coercitivas para que Pessoas, Organizações e Coletivos exerçam agência efetiva e situada ao definir, revisar, pausar, recusar ou renovar seus próprios próximos passos, individualmente ou em relações de co-agência.

### COD-003 — ECO-CAND-005

| Campo | Registro |
|---|---|
| Recomendação | `Merge into ECO-CAND-003` |
| Decisão humana | Aceitar `Merge into ECO-CAND-003` |
| Data | 25/07/2026 |
| Estado resultante | `Merged` |
| Alvo | `ECO-CAND-003` |

Continuidade adaptativa foi incorporada como dimensão temporal da agência efetiva e situada.

### COD-004 — ECO-CAND-002

| Campo | Registro |
|---|---|
| Recomendação | `Reformulate` |
| Decisão humana | Aceitar `Reformulate` |
| Data | 25/07/2026 |
| Estado resultante | `Under Validation` |

> Pessoas, Organizações e Coletivos dispõem de acesso real a possibilidades legítimas, compreensíveis e manejáveis, compatíveis com seu contexto, objetivos, restrições e fatores de conversão, preservando liberdade substantiva para compará-las e escolhê-las sem que a abundância de opções seja tratada como evidência de valor.

### COD-005 — ECO-CAND-004

| Campo | Registro |
|---|---|
| Recomendação | `Reject` |
| Decisão humana | Aceitar `Reject` |
| Data | 25/07/2026 |
| Estado resultante | `Rejected` |

Experiência permanece preservada na arquitetura da Jornada, como realização de valor em uso e fonte de evidências.

### COD-006 — ECO-CAND-006

| Campo | Registro |
|---|---|
| Recomendação | `Reformulate` |
| Decisão humana | Aceitar `Reformulate` |
| Data | 25/07/2026 |
| Estado resultante | `Under Validation` |

> O ecossistema sustenta condições para que Pessoas, Organizações e Coletivos estabeleçam e preservem relações voluntárias, diversas e reciprocamente construtivas, capazes de ampliar cooperação, acesso e valor recíproco sem restringir autonomia, excluir terceiros ou produzir dano material.

### COD-007 — ECO-CAND-007

| Campo | Registro |
|---|---|
| Recomendação | `Reformulate` |
| Decisão humana | Aceitar `Reformulate` |
| Data | 25/07/2026 |
| Estado resultante | `Under Validation` |

> Pessoas, Organizações e Coletivos, em diferentes culturas, crenças, países e contextos, dispõem de condições reais para participar do ecossistema de forma digna e efetiva, com capacidade de uso, respeito, voz e contestabilidade, mediante redução de barreiras materiais evitáveis e preservação de requisitos legítimos de elegibilidade, segurança e conformidade.

### COD-008 — ECO-CAND-008

| Campo | Registro |
|---|---|
| Recomendação | `Reformulate` |
| Decisão humana | Aceitar `Reformulate` |
| Data | 25/07/2026 |
| Estado resultante | `Under Validation` |

> Pessoas, Organizações e Coletivos participam do ecossistema em condições verificáveis de proteção, justiça e contestabilidade, com vulnerabilidades evitáveis reduzidas, possibilidade efetiva de compreender e questionar decisões, obter reparação diante de danos ou falhas e preservar sua autonomia, sem que conformidade, ausência de incidentes ou confiança declarada sejam tratadas como prova suficiente.

### COD-009 — BUS-CAND-001

| Campo | Registro |
|---|---|
| Recomendação | `Reject` |
| Decisão humana | Aceitar `Reject` |
| Data | 25/07/2026 |
| Estado resultante | `Rejected` |

Aderência ao propósito permanece autoridade constitucional, obrigação de governança, critério de admissibilidade e referência contra *mission drift*.

### COD-010 — BUS-CAND-002

| Campo | Registro |
|---|---|
| Recomendação | `Merge into BUS-CAND-003` |
| Decisão humana | Aceitar `Merge into BUS-CAND-003` |
| Data | 25/07/2026 |
| Estado resultante | `Merged` |
| Alvo | `BUS-CAND-003` |

Relevância contextual foi incorporada à formulação candidata de `BUS-CAND-003`.

### COD-011 — BUS-CAND-003

| Campo | Registro |
|---|---|
| Nome | Habilitação consistente e contextualmente relevante de valor legítimo |
| Recomendação | `Reformulate` |
| Decisão humana | Aceitar `Reformulate` |
| Autoridade | Fundador da Guivos |
| Data | 25/07/2026 |
| Estado anterior | `Under Validation` |
| Estado resultante | `Under Validation` |
| Código canônico | não criado |
| AQS-O01 | não iniciado |

#### Formulação originalmente avaliada

> A Guivos entrega valor legítimo com qualidade, segurança e continuidade suficientes para sustentar experiências relevantes.

#### Formulação candidata revisada

> A Guivos sustenta condições para habilitar valor legítimo com consistência e relevância contextual, detectando mudanças materiais e ajustando proposições, capacidades e respostas de forma coerente, sem presumir controle unilateral sobre o valor realizado pelos participantes nem tratar personalização, satisfação pontual, disponibilidade técnica ou velocidade de resposta como prova suficiente.

A formulação incorpora `BUS-CAND-002` por `COD-010`, permanece candidata e deverá retornar aos quatro testes da COEM.

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
| BUS-CAND-004 | Reformulate | — | Pending human decision; `BA-STR-002-COD-SUB-012` aberto |
| BUS-CAND-005 | Reformulate | — | Pending human decision |
| BUS-CAND-006 | Reject | — | Pending human decision |
| BUS-CAND-007 | Reject | — | Pending human decision |
| BUS-CAND-008 | Reject | — | Pending human decision |
| BUS-CAND-009 | Reject | — | Pending human decision |
| BUS-CAND-010 | Merge into BUS-CAND-005 | — | Pending human decision |

## 6. Submissão humana vigente

`BA-STR-002-COD-SUB-012` submete `BUS-CAND-004` à decisão humana sobre `Reformulate`.

A formulação candidata proposta é **Legitimidade institucional sustentada**:

> A legitimidade institucional da Guivos é sustentada perante participantes e stakeholders por conduta coerente, governança responsável, transparência, contestabilidade e reparação verificáveis, sem presumir controle unilateral sobre avaliações socialmente conferidas nem tratar reputação, conformidade, satisfação, confiança declarada ou longevidade das relações como prova suficiente.

Confiança institucional permanece avaliação relacional associada. `COD-012` não existe, o COR não foi alterado e nenhuma alternativa foi inferida como decisão.

## 7. Gate do incremento

| Critério | Resultado |
|---|---|
| submissão individual criada | Pass |
| recomendação original preservada | Pass |
| confiança e legitimidade separadas conceitualmente | Pass |
| formulação candidata revisada proposta | Pass |
| confiança preservada sem novo candidato automático | Pass |
| `COD-012` não criado | Pass |
| COR inalterado | Pass |
| promoção canônica bloqueada | Pass |
| AQS-O01 não antecipado | Pass |
| Product Engineering preservado em pausa | Pass |

## 8. Próximo passo governado

Receber a manifestação do Fundador sobre `BA-STR-002-COD-SUB-012`. Nenhuma decisão posterior será registrada automaticamente.
