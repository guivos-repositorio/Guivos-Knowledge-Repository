---
id: BA-STR-002-CODR-001
title: Candidate Outcome Decision Register
status: active
version: 0.16.0
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
  - COD-001
  - COD-002
  - COD-003
  - COD-004
  - COD-005
  - COD-006
  - COD-007
  - COD-008
  - M7.10.1
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
Human decisions recorded: 8
Decision submissions awaiting human response: 1
Current submission: BUS-CAND-001
Accepted Reformulate dispositions: 6
Accepted Merge dispositions: 1
Accepted Reject dispositions: 1
Candidate state changes: 2
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

## 4. COD-001 — ECO-CAND-001

| Campo | Registro |
|---|---|
| Recomendação | `Reformulate` |
| Decisão humana | Aceitar `Reformulate` |
| Autoridade | Fundador da Guivos |
| Data | 24/07/2026 |
| Estado após a decisão | `Under Validation` |

**Formulação original**

> Pessoas, Organizações e Coletivos conseguem compreender seu Momento Atual, necessidades, objetivos, restrições e possibilidades com suficiência para decisões conscientes.

**Formulação candidata revisada**

> Pessoas, Organizações e Coletivos formam e revisam uma compreensão contextual suficientemente fundamentada sobre sua situação, objetivos, necessidades, restrições e possibilidades, fortalecendo sua capacidade de realizar escolhas conscientes.

## 5. COD-002 — ECO-CAND-003

| Campo | Registro |
|---|---|
| Recomendação | `Reformulate` |
| Decisão humana | Aceitar `Reformulate` |
| Autoridade | Fundador da Guivos |
| Data | 24/07/2026 |
| Estado após a decisão | `Under Validation` |

**Formulação original**

> Participantes preservam liberdade de escolha e capacidade de definir, revisar ou recusar seus próprios próximos passos de evolução.

**Formulação candidata registrada**

> O ecossistema preserva condições reais, contextualmente adequadas e não coercitivas para que Pessoas, Organizações e Coletivos exerçam agência efetiva e situada ao definir, revisar, pausar, recusar ou renovar seus próprios próximos passos, individualmente ou em relações de co-agência.

## 6. COD-003 — ECO-CAND-005

| Campo | Registro |
|---|---|
| Recomendação | `Merge into ECO-CAND-003` |
| Decisão humana | Aceitar `Merge into ECO-CAND-003` |
| Autoridade | Fundador da Guivos |
| Data | 25/07/2026 |
| Estado após a decisão | `Merged` |
| Alvo | `ECO-CAND-003` |

**Formulação original**

> Participantes mantêm condições para reconhecer mudanças, aprender e iniciar novos ciclos de evolução coerentes com suas próprias escolhas.

**Formulação combinada resultante**

> O ecossistema preserva condições reais, contextualmente adequadas e não coercitivas para que Pessoas, Organizações e Coletivos exerçam agência efetiva e situada ao definir, revisar, pausar, recusar, abandonar ou renovar seus próprios próximos passos diante de mudanças, aprendizados e limites legítimos, individualmente ou em relações de co-agência.

## 7. COD-004 — ECO-CAND-002

| Campo | Registro |
|---|---|
| Recomendação | `Reformulate` |
| Decisão humana | Aceitar `Reformulate` |
| Autoridade | Fundador da Guivos |
| Data | 25/07/2026 |
| Estado após a decisão | `Under Validation` |

**Formulação original**

> Participantes encontram possibilidades legítimas, compreensíveis e relevantes para seu contexto, seus objetivos e seu momento de vida.

**Formulação candidata revisada**

> Pessoas, Organizações e Coletivos dispõem de acesso real a possibilidades legítimas, compreensíveis e manejáveis, compatíveis com seu contexto, objetivos, restrições e fatores de conversão, preservando liberdade substantiva para compará-las e escolhê-las sem que a abundância de opções seja tratada como evidência de valor.

## 8. COD-005 — ECO-CAND-004

| Campo | Registro |
|---|---|
| Recomendação | `Reject` |
| Decisão humana | Aceitar `Reject` |
| Autoridade | Fundador da Guivos |
| Data | 25/07/2026 |
| Estado após a decisão | `Rejected` |

**Formulação original preservada**

> Participantes conseguem converter oportunidades escolhidas em experiências vividas que produzem valor percebido e potencial de evolução.

Experiência permanece na arquitetura da Jornada, como realização de valor em uso, fonte de evidências e referência para capacidades e métricas futuras.

## 9. COD-006 — ECO-CAND-006

| Campo | Registro |
|---|---|
| Nome original | Conexões relevantes e fortalecedoras |
| Nome revisado | Saúde relacional no ecossistema |
| Recomendação | `Reformulate` |
| Decisão humana | Aceitar `Reformulate` |
| Autoridade | Fundador da Guivos |
| Data | 25/07/2026 |
| Estado após a decisão | `Under Validation` |
| Código canônico | não criado |
| AQS-O01 | não iniciado |

### Formulação originalmente avaliada

> Participantes formam e preservam relações relevantes que ampliam cooperação, acesso a oportunidades e geração recíproca de valor.

### Formulação candidata revisada

> O ecossistema sustenta condições para que Pessoas, Organizações e Coletivos estabeleçam e preservem relações voluntárias, diversas e reciprocamente construtivas, capazes de ampliar cooperação, acesso e valor recíproco sem restringir autonomia, excluir terceiros ou produzir dano material.

A formulação permanece `Under Validation` e deverá retornar aos quatro testes da COEM.

## 10. COD-007 — ECO-CAND-007

| Campo | Registro |
|---|---|
| Nome original | Participação inclusiva e digna |
| Nome revisado | Participação inclusiva, digna e efetiva |
| Recomendação | `Reformulate` |
| Decisão humana | Aceitar `Reformulate` |
| Autoridade | Fundador da Guivos |
| Data | 25/07/2026 |
| Estado após a decisão | `Under Validation` |
| Código canônico | não criado |
| AQS-O01 | não iniciado |

### Formulação originalmente avaliada

> Participantes de diferentes culturas, crenças, países e contextos conseguem participar do ecossistema com dignidade, acolhimento e acesso a valor essencial.

### Formulação candidata revisada

> Pessoas, Organizações e Coletivos, em diferentes culturas, crenças, países e contextos, dispõem de condições reais para participar do ecossistema de forma digna e efetiva, com capacidade de uso, respeito, voz e contestabilidade, mediante redução de barreiras materiais evitáveis e preservação de requisitos legítimos de elegibilidade, segurança e conformidade.

Cadastro, tradução, presença global ou representação nominal não comprovam inclusão. A formulação permanece `Under Validation` e deverá retornar aos quatro testes da COEM.

## 11. COD-008 — ECO-CAND-008

| Campo | Registro |
|---|---|
| Nome original | Participação confiável e protegida |
| Nome revisado | Participação protegida, justa e contestável |
| Recomendação | `Reformulate` |
| Decisão humana | Aceitar `Reformulate` |
| Autoridade | Fundador da Guivos |
| Data | 25/07/2026 |
| Estado após a decisão | `Under Validation` |
| Código canônico | não criado |
| AQS-O01 | não iniciado |

### Formulação originalmente avaliada

> Participantes interagem em condições de transparência, segurança, privacidade, justiça, contestabilidade e respeito à sua autonomia.

### Formulação candidata revisada

> Pessoas, Organizações e Coletivos participam do ecossistema em condições verificáveis de proteção, justiça e contestabilidade, com vulnerabilidades evitáveis reduzidas, possibilidade efetiva de compreender e questionar decisões, obter reparação diante de danos ou falhas e preservar sua autonomia, sem que conformidade, ausência de incidentes ou confiança declarada sejam tratadas como prova suficiente.

Privacidade, segurança, transparência e autonomia permanecem guardrails verificáveis. Proteção absoluta é impossível; conformidade, ausência de incidentes ou confiança declarada não constituem evidência suficiente. A formulação deverá retornar aos quatro testes da COEM.

## 12. Submissão decisória atual — BUS-CAND-001

A submissão `BA-STR-002-COD-SUB-009` apresenta a recomendação `Reject`.

### Formulação originalmente avaliada

> A Guivos mantém decisões, investimentos, relações e evolução institucional coerentes com seu propósito e seus princípios permanentes.

### Destino arquitetural proposto

Retirar o candidato do futuro catálogo de Business Outcomes e preservar aderência ao propósito como princípio constitucional, obrigação de governança, critério de admissibilidade e referência para prevenção e correção de *mission drift*.

### Fundamentação da recomendação

A aderência ao propósito é indispensável, porém sua ausência representa violação constitucional e de governança. Tratar o dever como Outcome empresarial criaria circularidade entre o propósito e a medição de aderência a ele próprio.

### Alternativas

```text
A — Aceitar Reject
B — Rejeitar Reject, com fundamentação
C — Devolver para nova análise
```

A alternativa A é recomendada. Enquanto não houver manifestação explícita:

- `COD-009` não existe;
- decisões humanas permanecem em `8 de 18`;
- `BUS-CAND-001` permanece `Under Validation`;
- nenhuma alteração é executada no COR;
- nenhum código canônico é criado.

## 13. Matriz cumulativa de decisões

| Candidato | Recomendação da COEM | Decisão humana | Estado decisório |
|---|---|---|---|
| ECO-CAND-001 | Reformulate | Aceitar `Reformulate` | revisão candidata pendente de nova COEM |
| ECO-CAND-003 | Reformulate | Aceitar `Reformulate` | formulação combinada pendente de nova COEM |
| ECO-CAND-005 | Merge into ECO-CAND-003 | Aceitar `Merge into ECO-CAND-003` | `Merged`; alvo ECO-CAND-003 |
| ECO-CAND-002 | Reformulate | Aceitar `Reformulate` | revisão candidata pendente de nova COEM |
| ECO-CAND-004 | Reject | Aceitar `Reject` | `Rejected`; experiência preservada na Jornada |
| ECO-CAND-006 | Reformulate | Aceitar `Reformulate` | revisão candidata pendente de nova COEM |
| ECO-CAND-007 | Reformulate | Aceitar `Reformulate` | revisão candidata pendente de nova COEM |
| ECO-CAND-008 | Reformulate | Aceitar `Reformulate` | revisão candidata pendente de nova COEM |
| BUS-CAND-001 | Reject | — | submitted to human decision; awaiting response |
| BUS-CAND-002 | Merge into BUS-CAND-003 | — | Pending human decision |
| BUS-CAND-003 | Reformulate | — | Pending human decision |
| BUS-CAND-004 | Reformulate | — | Pending human decision |
| BUS-CAND-005 | Reformulate | — | Pending human decision |
| BUS-CAND-006 | Reject | — | Pending human decision |
| BUS-CAND-007 | Reject | — | Pending human decision |
| BUS-CAND-008 | Reject | — | Pending human decision |
| BUS-CAND-009 | Reject | — | Pending human decision |
| BUS-CAND-010 | Merge into BUS-CAND-005 | — | Pending human decision |

## 14. Gate do incremento

| Critério | Resultado |
|---|---|
| submissão individual de BUS-CAND-001 criada | Pass |
| recomendação original preservada | Pass |
| evidências e contraevidências explicitadas | Pass |
| destino arquitetural proposto | Pass |
| alternativas humanas A, B e C registradas | Pass |
| decisão humana inferida automaticamente | Blocked |
| alteração automática do COR | Blocked |
| redução da autoridade do propósito | Blocked |
| promoção canônica | Blocked |
| AQS-O01 não antecipado | Pass |
| Product Engineering preservado em pausa | Pass |

## 15. Próximo passo governado

Registrar a manifestação do Fundador sobre `BA-STR-002-COD-SUB-009`.

Se a alternativa A for escolhida, um incremento posterior deverá criar `COD-009`, preservar formulação e evidências, mover `BUS-CAND-001` para `Rejected`, retirar a candidatura do futuro catálogo de Business Outcomes e manter aderência ao propósito como autoridade constitucional e obrigação de governança.
