---
id: BA-STR-002-CODR-001
title: Candidate Outcome Decision Register
status: active
version: 0.20.0
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
  - M7.12.1
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
Human decisions recorded: 10
Decision submissions awaiting human response: 1
Current submission: BUS-CAND-003
Accepted Reformulate dispositions: 6
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

## 12. COD-009 — BUS-CAND-001

| Campo | Registro |
|---|---|
| Nome | Aderência permanente ao propósito |
| Recomendação | `Reject` |
| Decisão humana | Aceitar `Reject` |
| Autoridade | Fundador da Guivos |
| Data | 25/07/2026 |
| Estado anterior | `Under Validation` |
| Estado após a decisão | `Rejected` |
| Código canônico | não criado |
| AQS-O01 | não iniciado |

### Formulação originalmente avaliada

> A Guivos mantém decisões, investimentos, relações e evolução institucional coerentes com seu propósito e seus princípios permanentes.

### Destino arquitetural preservado

A rejeição atinge somente a classificação como Business Outcome autônomo. Aderência ao propósito permanece princípio constitucional permanente, obrigação de governança e accountability, critério de admissibilidade para decisões, investimentos, relações, capacidades, produtos e Outcomes, referência para prevenção e correção de *mission drift* e requisito transversal de coerência institucional.

A decisão não relativiza o propósito, não reduz a autoridade dos princípios permanentes e não trata desempenho, reputação, comunicação ou aderência declarada como prova suficiente de prática institucional.

## 13. COD-010 — BUS-CAND-002

| Campo | Registro |
|---|---|
| Nome | Relevância contínua das respostas |
| Recomendação | `Merge into BUS-CAND-003` |
| Decisão humana | Aceitar `Merge into BUS-CAND-003` |
| Autoridade | Fundador da Guivos |
| Data | 25/07/2026 |
| Estado anterior | `Under Validation` |
| Estado após a decisão | `Merged` |
| Alvo | `BUS-CAND-003` |
| Estado do alvo | `Under Validation` |
| Código canônico | não criado |
| AQS-O01 | não iniciado |

### Formulação originalmente avaliada

> As respostas organizadas pela Guivos permanecem relevantes diante da mudança de contextos, necessidades e prioridades dos participantes.

### Formulação combinada resultante

**Habilitação consistente e contextualmente relevante de valor legítimo**

> A Guivos sustenta condições para habilitar valor legítimo com consistência e relevância contextual, detectando mudanças materiais e ajustando proposições, capacidades e respostas de forma coerente, sem presumir controle unilateral sobre o valor realizado pelos participantes nem tratar personalização, satisfação pontual, disponibilidade técnica ou velocidade de resposta como prova suficiente.

A formulação permanece candidata. `BUS-CAND-003` conserva sua recomendação própria `Reformulate` e deverá retornar aos quatro testes da COEM antes de qualquer aprovação.

## 14. Submissão decisória atual — BUS-CAND-003

A submissão `BA-STR-002-COD-SUB-011` apresenta a recomendação própria `Reformulate` de `BUS-CAND-003`.

### Formulação originalmente avaliada

> A Guivos entrega valor legítimo com qualidade, segurança e continuidade suficientes para sustentar experiências relevantes.

### Formulação candidata revisada submetida

**Habilitação consistente e contextualmente relevante de valor legítimo**

> A Guivos sustenta condições para habilitar valor legítimo com consistência e relevância contextual, detectando mudanças materiais e ajustando proposições, capacidades e respostas de forma coerente, sem presumir controle unilateral sobre o valor realizado pelos participantes nem tratar personalização, satisfação pontual, disponibilidade técnica ou velocidade de resposta como prova suficiente.

### Fundamentação da recomendação

A formulação preserva a condição empresarial de habilitar valor legítimo, distingue habilitação de valor realizado por terceiros e incorpora a relevância contextual proveniente de `COD-010`. Qualidade, segurança, continuidade, inteligência e adaptação permanecem propriedades verificáveis ou capacidades sustentadoras.

### Alternativas

```text
A — Aceitar Reformulate
B — Rejeitar Reformulate, com fundamentação
C — Devolver para nova análise
```

A alternativa A é recomendada. Enquanto não houver manifestação explícita:

- `COD-011` não existe;
- decisões humanas permanecem em `10 de 18`;
- `BUS-CAND-003` permanece `Under Validation`;
- nenhuma alteração é executada no COR;
- nenhum código canônico é criado.

## 15. Matriz cumulativa de decisões

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
| BUS-CAND-001 | Reject | Aceitar `Reject` | `Rejected`; conteúdo preservado na Constituição e governança |
| BUS-CAND-002 | Merge into BUS-CAND-003 | Aceitar `Merge into BUS-CAND-003` | `Merged`; alvo BUS-CAND-003 |
| BUS-CAND-003 | Reformulate | — | submitted to human decision; awaiting response |
| BUS-CAND-004 | Reformulate | — | Pending human decision |
| BUS-CAND-005 | Reformulate | — | Pending human decision |
| BUS-CAND-006 | Reject | — | Pending human decision |
| BUS-CAND-007 | Reject | — | Pending human decision |
| BUS-CAND-008 | Reject | — | Pending human decision |
| BUS-CAND-009 | Reject | — | Pending human decision |
| BUS-CAND-010 | Merge into BUS-CAND-005 | — | Pending human decision |

## 16. Gate do incremento

| Critério | Resultado |
|---|---|
| submissão individual de BUS-CAND-003 criada | Pass |
| recomendação original preservada | Pass |
| linhagem de COD-010 preservada | Pass |
| evidências e limites explicitados | Pass |
| formulação candidata revisada registrada | Pass |
| alternativas humanas A, B e C registradas | Pass |
| decisão humana inferida automaticamente | Blocked |
| alteração automática do COR | Blocked |
| aprovação automática do candidato | Blocked |
| promoção canônica | Blocked |
| AQS-O01 não antecipado | Pass |
| Product Engineering preservado em pausa | Pass |

## 17. Próximo passo governado

Registrar a manifestação do Fundador sobre `BA-STR-002-COD-SUB-011`.

Se a alternativa A for escolhida, um incremento posterior deverá criar `COD-011`, preservar a linhagem completa, registrar a formulação combinada como formulação candidata revisada, manter `BUS-CAND-003` em `Under Validation` e exigir nova aplicação dos quatro testes da COEM.
