---
id: BA-STR-002-CODR-001
title: Candidate Outcome Decision Register
status: active
version: 0.10.0
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
  - COD-001
  - COD-002
  - COD-003
  - COD-004
  - COD-005
  - M7.7.1
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

Uma decisão registrada aqui não cria automaticamente um Outcome canônico. Reformulações permanecem candidatas; fusões e rejeições preservam rastreabilidade e somente alteram o COR quando expressamente autorizadas.

## 2. Estado formal

```text
Decision register: in progress — resumed by R6
Candidate dispositions in scope: 18
Human decisions recorded: 5
Decision submissions awaiting human response: 1
Current submission: ECO-CAND-006
Accepted Reformulate dispositions: 3
Accepted Merge dispositions: 1
Accepted Reject dispositions: 1
Candidate state changes: 2
Approved Outcomes: 0
Canonical EO/BO codes: 0
AQS-O01: not started
Operational authorization: no
```

## 3. Protocolo decisório

| Campo | Regra |
|---|---|
| Identificador | código estável da decisão humana |
| Candidato | identificador preservado do COR |
| Recomendação da COEM | disposição emitida pela matriz, sem reinterpretação |
| Decisão humana | aceitar, rejeitar ou devolver para nova análise |
| Fundamentação | razão arquitetural da decisão |
| Formulação, alvo ou destino | versão candidata, destino de fusão ou camada preservada |
| Estado após a decisão | estado formal permitido no COR |
| Limites | efeitos expressamente não autorizados |
| Próximo gate | condição necessária antes do próximo ato |

### Regras permanentes

- cada candidato recebe decisão individual;
- nenhuma decisão é inferida por contagem de testes ou decisão de outro candidato;
- `Reformulate` aceito não equivale a `Approved`;
- `Merge` aceito não aprova automaticamente o alvo;
- `Reject` aceito preserva registro, formulação e evidências;
- formulações revisadas ou combinadas retornam aos quatro testes da COEM;
- candidatos fundidos ou rejeitados permanecem rastreáveis;
- nenhum código `EO-###` ou `BO-###` nasce neste registro;
- AQS-O01 e consolidação canônica permanecem posteriores.

## 4. COD-001 — ECO-CAND-001

| Campo | Registro |
|---|---|
| Decisão | `COD-001` |
| Candidato | `ECO-CAND-001` |
| Recomendação | `Reformulate` |
| Decisão humana | Aceitar `Reformulate` |
| Autoridade | Fundador da Guivos |
| Data | 24/07/2026 |
| Estado após a decisão | `Under Validation` |
| Código canônico | não criado |

### Formulação original

> Pessoas, Organizações e Coletivos conseguem compreender seu Momento Atual, necessidades, objetivos, restrições e possibilidades com suficiência para decisões conscientes.

### Formulação candidata revisada

> Pessoas, Organizações e Coletivos formam e revisam uma compreensão contextual suficientemente fundamentada sobre sua situação, objetivos, necessidades, restrições e possibilidades, fortalecendo sua capacidade de realizar escolhas conscientes.

A formulação permanece candidata e deverá retornar à COEM.

## 5. COD-002 — ECO-CAND-003

| Campo | Registro |
|---|---|
| Decisão | `COD-002` |
| Candidato | `ECO-CAND-003` |
| Recomendação | `Reformulate` |
| Decisão humana | Aceitar `Reformulate` |
| Autoridade | Fundador da Guivos |
| Data | 24/07/2026 |
| Estado após a decisão | `Under Validation` |
| Código canônico | não criado |

### Formulação original

> Participantes preservam liberdade de escolha e capacidade de definir, revisar ou recusar seus próprios próximos passos de evolução.

### Formulação candidata registrada

> O ecossistema preserva condições reais, contextualmente adequadas e não coercitivas para que Pessoas, Organizações e Coletivos exerçam agência efetiva e situada ao definir, revisar, pausar, recusar ou renovar seus próprios próximos passos, individualmente ou em relações de co-agência.

A formulação foi ampliada posteriormente por `COD-003`.

## 6. COD-003 — ECO-CAND-005

| Campo | Registro |
|---|---|
| Decisão | `COD-003` |
| Candidato | `ECO-CAND-005` |
| Recomendação | `Merge into ECO-CAND-003` |
| Decisão humana | Aceitar `Merge into ECO-CAND-003` |
| Autoridade | Fundador da Guivos |
| Data | 25/07/2026 |
| Estado após a decisão | `Merged` |
| Alvo | `ECO-CAND-003` |
| Estado do alvo | `Under Validation` |
| Código canônico | não criado |

### Formulação original

> Participantes mantêm condições para reconhecer mudanças, aprender e iniciar novos ciclos de evolução coerentes com suas próprias escolhas.

### Formulação combinada resultante

> O ecossistema preserva condições reais, contextualmente adequadas e não coercitivas para que Pessoas, Organizações e Coletivos exerçam agência efetiva e situada ao definir, revisar, pausar, recusar, abandonar ou renovar seus próprios próximos passos diante de mudanças, aprendizados e limites legítimos, individualmente ou em relações de co-agência.

A formulação combinada permanece `Under Validation`.

## 7. COD-004 — ECO-CAND-002

| Campo | Registro |
|---|---|
| Decisão | `COD-004` |
| Candidato | `ECO-CAND-002` |
| Recomendação | `Reformulate` |
| Decisão humana | Aceitar `Reformulate` |
| Autoridade | Fundador da Guivos |
| Data | 25/07/2026 |
| Estado após a decisão | `Under Validation` |
| Código canônico | não criado |

### Formulação original

> Participantes encontram possibilidades legítimas, compreensíveis e relevantes para seu contexto, seus objetivos e seu momento de vida.

### Formulação candidata revisada

> Pessoas, Organizações e Coletivos dispõem de acesso real a possibilidades legítimas, compreensíveis e manejáveis, compatíveis com seu contexto, objetivos, restrições e fatores de conversão, preservando liberdade substantiva para compará-las e escolhê-las sem que a abundância de opções seja tratada como evidência de valor.

A formulação permanece `Under Validation` e deverá retornar à COEM.

## 8. COD-005 — ECO-CAND-004

| Campo | Registro |
|---|---|
| Decisão | `COD-005` |
| Candidato | `ECO-CAND-004` |
| Nome provisório | Realização de experiências de valor |
| Recomendação | `Reject` |
| Decisão humana | Aceitar `Reject` |
| Autoridade | Fundador da Guivos |
| Data | 25/07/2026 |
| Estado após a decisão | `Rejected` |
| Código canônico | não criado |
| AQS-O01 | não iniciado |

### Formulação originalmente avaliada

> Participantes conseguem converter oportunidades escolhidas em experiências vividas que produzem valor percebido e potencial de evolução.

### Fundamentação consolidada

A recomendação foi aceita porque experiência vivida é episódio de realização, não condição permanente autônoma do ecossistema. A decisão preserva experiência na arquitetura da Jornada, como realização de valor em uso, fonte de evidências e referência para capacidades e métricas futuras.

## 9. Submissão decisória atual — ECO-CAND-006

A submissão `BA-STR-002-COD-SUB-006` apresenta a recomendação `Reformulate`.

### Formulação originalmente avaliada

> Participantes formam e preservam relações relevantes que ampliam cooperação, acesso a oportunidades e geração recíproca de valor.

### Formulação candidata proposta

**Saúde relacional no ecossistema**

> O ecossistema sustenta condições para que Pessoas, Organizações e Coletivos estabeleçam e preservem relações voluntárias, diversas e reciprocamente construtivas, capazes de ampliar cooperação, acesso e valor recíproco sem restringir autonomia, excluir terceiros ou produzir dano material.

### Fundamentação da recomendação

A formulação original pressupõe benefício e agrega relação, mecanismo e efeito. A evidência exige diversidade estrutural, reciprocidade, voluntariedade, autonomia e limites contra exclusão ou dano material. Quantidade, densidade, intensidade ou coesão das conexões não constituem prova suficiente de saúde relacional.

### Alternativas

```text
A — Aceitar Reformulate
B — Rejeitar Reformulate, com fundamentação
C — Devolver para nova análise
```

A alternativa A é recomendada. Enquanto não houver manifestação explícita:

- `COD-006` não existe;
- decisões humanas permanecem em `5 de 18`;
- `ECO-CAND-006` permanece `Under Validation`;
- nenhuma alteração é executada no COR;
- nenhum código canônico é criado.

## 10. Matriz cumulativa de decisões

| Candidato | Recomendação da COEM | Decisão humana | Estado decisório |
|---|---|---|---|
| ECO-CAND-001 | Reformulate | Aceitar `Reformulate` | revisão candidata pendente de nova COEM |
| ECO-CAND-003 | Reformulate | Aceitar `Reformulate` | formulação combinada pendente de nova COEM |
| ECO-CAND-005 | Merge into ECO-CAND-003 | Aceitar `Merge into ECO-CAND-003` | `Merged`; alvo ECO-CAND-003 |
| ECO-CAND-002 | Reformulate | Aceitar `Reformulate` | revisão candidata pendente de nova COEM |
| ECO-CAND-004 | Reject | Aceitar `Reject` | `Rejected`; experiência preservada na Jornada |
| ECO-CAND-006 | Reformulate | — | submitted to human decision; awaiting response |
| ECO-CAND-007 | Reformulate | — | Pending human decision |
| ECO-CAND-008 | Reformulate | — | Pending human decision |
| BUS-CAND-001 | Reject | — | Pending human decision |
| BUS-CAND-002 | Merge into BUS-CAND-003 | — | Pending human decision |
| BUS-CAND-003 | Reformulate | — | Pending human decision |
| BUS-CAND-004 | Reformulate | — | Pending human decision |
| BUS-CAND-005 | Reformulate | — | Pending human decision |
| BUS-CAND-006 | Reject | — | Pending human decision |
| BUS-CAND-007 | Reject | — | Pending human decision |
| BUS-CAND-008 | Reject | — | Pending human decision |
| BUS-CAND-009 | Reject | — | Pending human decision |
| BUS-CAND-010 | Merge into BUS-CAND-005 | — | Pending human decision |

## 11. Gate do incremento

| Critério | Resultado |
|---|---|
| submissão individual de ECO-CAND-006 criada | Pass |
| recomendação original preservada | Pass |
| evidências e contraevidências explicitadas | Pass |
| formulação candidata proposta | Pass |
| alternativas humanas A, B e C registradas | Pass |
| decisão humana inferida automaticamente | Blocked |
| alteração automática do COR | Blocked |
| promoção canônica | Blocked |
| AQS-O01 não antecipado | Pass |
| Product Engineering preservado em pausa | Pass |

## 12. Próximo passo governado

Registrar a manifestação do Fundador sobre `BA-STR-002-COD-SUB-006`.

Se a alternativa A for escolhida, um incremento posterior deverá criar `COD-006`, preservar a formulação original, registrar a formulação candidata de saúde relacional, manter `ECO-CAND-006` em `Under Validation` e exigir nova aplicação dos quatro testes da COEM.
