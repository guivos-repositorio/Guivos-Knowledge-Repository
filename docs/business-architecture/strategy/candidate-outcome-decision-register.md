---
id: BA-STR-002-CODR-001
title: Candidate Outcome Decision Register
status: active
version: 0.2.0
owner: Guivos Business Architecture
last_updated: 2026-07-24
parent: BA-STR-002
depends_on:
  - BA-STR-002-COR-001
  - BA-STR-002-COEM-001
  - GKR-GOV-OUT-001
related:
  - BA-STR-002-EOVB-001
  - RP-001-EVIDENCE
  - GKR-R6-RESUMPTION-001
  - BA-STR-002-COD-SUB-002
  - M7.3.5
normative: false
execution_status: in-progress
---

# BA-STR-002-CODR-001 — Candidate Outcome Decision Register

## 1. Autoridade e finalidade

Este registro preserva as decisões humanas individuais sobre as disposições recomendadas pela `BA-STR-002-COEM-001`.

Ele mantém separados:

1. a formulação originalmente avaliada;
2. os resultados dos quatro testes da COEM;
3. a disposição recomendada pela matriz;
4. a decisão humana explícita;
5. a eventual formulação revisada;
6. a mudança posterior de estado do candidato;
7. a futura consolidação na Canon.

Uma decisão registrada aqui não cria automaticamente um Outcome canônico. Reformulações permanecem candidatas e devem retornar aos testes antes de qualquer recomendação `Approve`.

## 2. Estado formal

```text
Decision register: in progress — resumed by R6
Candidate dispositions in scope: 18
Human decisions recorded: 1
Decision submissions awaiting human response: 1
Current submission: ECO-CAND-003
Accepted Reformulate dispositions: 1
Accepted Merge dispositions: 0
Accepted Reject dispositions: 0
Candidate state changes: 0
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
| Decisão humana | aceitar, rejeitar ou devolver a recomendação para nova análise |
| Fundamentação | razão arquitetural da decisão |
| Formulação revisada | versão candidata, quando a decisão for `Reformulate` |
| Estado após a decisão | estado formal permitido no COR |
| Limites | efeitos expressamente não autorizados |
| Próximo gate | condição necessária antes do próximo ato de governança |

### Regras permanentes

- cada candidato recebe decisão individual;
- nenhuma decisão é inferida por contagem de testes, cobertura da COEM ou decisão tomada sobre outro candidato;
- uma recomendação `Reformulate` aceita não equivale a `Approved`;
- uma formulação revisada deve ser reavaliada pelos quatro testes da COEM;
- decisões `Merge` ou `Reject` somente alteram o COR quando o próprio registro decisório autorizar expressamente a mudança;
- nenhum código `EO-###` ou `BO-###` nasce neste registro;
- AQS-O01 e consolidação canônica permanecem atos posteriores.

## 4. COD-001 — ECO-CAND-001

### Registro da decisão

| Campo | Registro |
|---|---|
| Decisão | `COD-001` |
| Candidato | `ECO-CAND-001` |
| Nome provisório | Compreensão contextual suficiente |
| Recomendação da COEM | `Reformulate` |
| Decisão humana | Aceitar `Reformulate` |
| Autoridade decisória | Fundador da Guivos |
| Data | 24/07/2026 |
| Estado após a decisão | `Under Validation` |
| Código canônico | não criado |
| AQS-O01 | não iniciado |

### Formulação originalmente avaliada

> Pessoas, Organizações e Coletivos conseguem compreender seu Momento Atual, necessidades, objetivos, restrições e possibilidades com suficiência para decisões conscientes.

### Fundamentação consolidada

A compreensão contextual possui relevância material, independência de produtos e capacidade de orientar decisões estratégicas sobre explicabilidade, captura de contexto e apoio à decisão. Entretanto, as evidências não sustentam ainda sua promoção como Outcome autônomo.

A formulação original apresenta três insuficiências:

1. pode tratar compreensão como resultado autônomo quando ela opera predominantemente como condição de agência;
2. utiliza “suficiência” sem explicitar que o critério é contextual, revisável e apoiado por múltiplas evidências;
3. pode permitir que introspecção ou autodeclaração sejam interpretadas como prova única da condição.

### Formulação candidata revisada

> Pessoas, Organizações e Coletivos formam e revisam uma compreensão contextual suficientemente fundamentada sobre sua situação, objetivos, necessidades, restrições e possibilidades, fortalecendo sua capacidade de realizar escolhas conscientes.

### Efeitos autorizados

- aceitar formalmente a disposição `Reformulate`;
- preservar a formulação original para rastreabilidade;
- registrar a formulação revisada como nova versão candidata;
- manter `ECO-CAND-001` em `Under Validation`;
- submeter a formulação revisada aos quatro testes da COEM em incremento posterior;
- reavaliar a fronteira com `ECO-CAND-003` antes de qualquer aprovação.

### Efeitos não autorizados

- promover `ECO-CAND-001` a `Approved`;
- criar código canônico `EO-###`;
- tratar a compreensão contextual como Outcome independente já demonstrado;
- incorporar automaticamente o candidato a `ECO-CAND-003`;
- iniciar AQS-O01, catálogo canônico ou `BA-CAP-001`;
- retomar Product Engineering ou autorizar W0-01.

### Evidências e rastreabilidade

- `RP1-EV-001` e `RP1-EV-002`: compreensão reflexiva e *sensemaking* como mecanismos que informam ação;
- `RP1-EV-003`: bloqueio de introspecção ou autorrelato como prova suficiente;
- `BA-STR-002-EOVB-001`: dependência funcional entre compreensão contextual, agência e continuidade adaptativa;
- `BA-STR-002-COEM-001`: Essential `Partial`, Decision `Pass`, Replacement `Pass` e Outcome Quality `Partial`.

### Gate de reentrada na COEM

A formulação revisada somente poderá receber nova disposição após:

1. reaplicação explícita dos quatro testes;
2. verificação de independência em relação a `ECO-CAND-003`;
3. definição de evidências possíveis que não dependam de autodeclaração isolada;
4. confirmação de que a formulação descreve condição permanente do ecossistema e não processo de captura ou interpretação de contexto.

## 5. Submissão decisória atual — ECO-CAND-003

A submissão `BA-STR-002-COD-SUB-002` apresenta a recomendação `Reformulate`, a formulação candidata **Agência efetiva e situada** e três alternativas para manifestação do Fundador.

```text
A — Aceitar Reformulate
B — Rejeitar Reformulate, com fundamentação
C — Devolver para nova análise
```

Enquanto não houver manifestação explícita:

- `COD-002` não existe;
- decisões humanas permanecem em `1 de 18`;
- `ECO-CAND-003` permanece `Under Validation`;
- nenhuma mudança é executada no COR;
- nenhum código canônico é criado.

## 6. Matriz cumulativa de decisões

| Candidato | Recomendação da COEM | Decisão humana | Estado decisório |
|---|---|---|---|
| ECO-CAND-001 | Reformulate | Aceitar `Reformulate` | decisão registrada; revisão candidata pendente de nova COEM |
| ECO-CAND-003 | Reformulate | — | submitted to human decision; awaiting response |
| ECO-CAND-005 | Merge into ECO-CAND-003 | — | Pending human decision |
| ECO-CAND-002 | Reformulate | — | Pending human decision |
| ECO-CAND-004 | Reject | — | Pending human decision |
| ECO-CAND-006 | Reformulate | — | Pending human decision |
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

## 7. Gate do R6

| Critério | Resultado |
|---|---|
| remediação R1–R5 integrada | Pass |
| parecer mecânico | Pass |
| pausa da A2-R03 encerrada | Pass |
| CODR retomado | Pass |
| submissão individual de ECO-CAND-003 criada | Pass |
| decisão humana inferida automaticamente | Blocked |
| mudança automática de estado | Blocked |
| promoção canônica | Blocked |
| Product Engineering preservado em pausa | Pass |

## 8. Próximo passo governado

Registrar a manifestação do Fundador sobre `BA-STR-002-COD-SUB-002`.

Se a alternativa A for escolhida, o próximo incremento deverá criar `COD-002`, preservar `ECO-CAND-003` em `Under Validation` e registrar a formulação revisada para reentrada futura na COEM.
