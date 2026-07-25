---
id: BA-STR-002-COD-SUB-009
title: Human Decision Resolution — BUS-CAND-001
status: decision-recorded
version: 0.2.0
owner: Guivos Business Architecture
last_updated: 2026-07-25
parent: BA-STR-002-CODR-001
depends_on:
  - BA-STR-002-COR-001
  - BA-STR-002-COEM-001
  - BA-STR-002-EOVB-006
  - GKR-GOV-OUT-001
related:
  - RP-001-EVIDENCE
  - COD-008
  - COD-009
  - M7.11
normative: false
---

# Human Decision Resolution — BUS-CAND-001

## 1. Finalidade

Registrar a nona decisão humana individual do Candidate Outcome Decision Register para `BUS-CAND-001 — Aderência permanente ao propósito`.

O Fundador da Guivos manifestou explicitamente:

```text
A — Aceitar Reject
```

A decisão é registrada como `COD-009`.

## 2. Formulação originalmente avaliada

> A Guivos mantém decisões, investimentos, relações e evolução institucional coerentes com seu propósito e seus princípios permanentes.

## 3. Resultado da COEM

| Teste | Resultado | Síntese |
|---|---|---|
| Essential | Partial | aderência ao propósito é indispensável à legitimidade institucional, mas sua ausência representa violação constitucional e de governança, não falta de resultado empresarial autônomo |
| Decision | Pass | sinais persistentes de *mission drift* exigem revisão estratégica, accountability e correção de autoridade, portfólio, investimentos e relações |
| Replacement | Pass | a obrigação permanece válida após substituição de produtos, estruturas e tecnologias |
| Outcome Quality | Fail | a formulação descreve orientação superior, conformidade constitucional e dever permanente de governança; promovê-la a Outcome criaria circularidade |
| Disposição recomendada | `Reject` | retirar a candidatura do futuro catálogo de Business Outcomes e preservar o conteúdo em sua camada constitucional e de governança |

## 4. Decisão humana registrada

| Campo | Registro |
|---|---|
| Código da decisão | `COD-009` |
| Candidato | `BUS-CAND-001` |
| Recomendação | `Reject` |
| Decisão humana | Aceitar `Reject` |
| Autoridade | Fundador da Guivos |
| Data | 25/07/2026 |
| Estado anterior | `Under Validation` |
| Estado resultante | `Rejected` |
| Código canônico | não criado |
| AQS-O01 | não iniciado |

## 5. Destino arquitetural preservado

A rejeição atinge exclusivamente a classificação como Business Outcome autônomo. **Aderência permanente ao propósito** permanece como:

- princípio constitucional permanente;
- obrigação de governança e accountability;
- critério de admissibilidade para decisões, investimentos, relações, capacidades, produtos e Outcomes;
- referência para identificação, prevenção e correção de *mission drift*;
- requisito transversal de coerência institucional.

A decisão não relativiza o propósito, não reduz a autoridade dos princípios permanentes e não transforma desempenho, reputação, comunicação ou aderência declarada em prova de prática institucional.

## 6. Efeitos no Candidate Outcome Register

`BUS-CAND-001` passa de `Under Validation` para `Rejected`.

A distribuição resultante do COR é:

```text
Under Validation: 15
Merged: 1
Rejected: 2
Approved Outcomes: 0
Canonical EO/BO codes: 0
```

A formulação original, as evidências, a recomendação e o destino arquitetural permanecem rastreáveis.

## 7. Limites da decisão

`COD-009` não:

- rejeita ou relativiza o propósito da Guivos;
- remove a obrigação de prevenir e corrigir *mission drift*;
- transforma a aderência em métrica única ou prova declaratória;
- aprova outro candidato;
- cria código `BO-###`;
- inicia AQS-O01, Business Capabilities, produtos ou Product Engineering.

## 8. Gate da resolução

| Critério | Resultado |
|---|---|
| manifestação humana explícita | Pass |
| recomendação original preservada | Pass |
| `COD-009` registrado | Pass |
| formulação e evidências preservadas | Pass |
| `BUS-CAND-001` movido para `Rejected` | Pass |
| destino constitucional e de governança preservado | Pass |
| autoridade do propósito preservada | Pass |
| promoção canônica bloqueada | Pass |
| AQS-O01 não antecipado | Pass |
| Product Engineering preservado em pausa | Pass |

## 9. Próximo passo governado

Preparar e submeter `BUS-CAND-002 — Relevância contínua das respostas` à décima decisão humana individual sobre a recomendação `Merge into BUS-CAND-003`.