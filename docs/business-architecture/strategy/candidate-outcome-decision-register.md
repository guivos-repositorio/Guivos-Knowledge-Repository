---
id: BA-STR-002-CODR-001
title: Candidate Outcome Decision Register
status: active
version: 0.3.0
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
  - COD-001
  - COD-002
  - M7.4
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
Human decisions recorded: 2
Decision submissions awaiting human response: 0
Accepted Reformulate dispositions: 2
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

### Gate de reentrada na COEM

A formulação revisada somente poderá receber nova disposição após:

1. reaplicação explícita dos quatro testes;
2. verificação de independência em relação a `ECO-CAND-003`;
3. definição de evidências possíveis que não dependam de autodeclaração isolada;
4. confirmação de que a formulação descreve condição permanente do ecossistema e não processo de captura ou interpretação de contexto.

## 5. COD-002 — ECO-CAND-003

### Registro da decisão

| Campo | Registro |
|---|---|
| Decisão | `COD-002` |
| Candidato | `ECO-CAND-003` |
| Nome provisório original | Agência sobre próximos passos |
| Nome provisório revisado | Agência efetiva e situada |
| Recomendação da COEM | `Reformulate` |
| Decisão humana | Aceitar `Reformulate` |
| Autoridade decisória | Fundador da Guivos |
| Data | 24/07/2026 |
| Estado após a decisão | `Under Validation` |
| Código canônico | não criado |
| AQS-O01 | não iniciado |

### Formulação originalmente avaliada

> Participantes preservam liberdade de escolha e capacidade de definir, revisar ou recusar seus próprios próximos passos de evolução.

### Fundamentação consolidada

O núcleo de agência atende aos testes Essential, Decision e Replacement e possui a implicação estratégica mais autônoma do cluster formado por `ECO-CAND-001`, `ECO-CAND-003` e `ECO-CAND-005`.

A reformulação foi aceita porque:

1. liberdade formal de escolha não comprova agência efetiva;
2. agência depende de condições contextuais, competência, pertencimento e relações de co-agência;
3. a condição deve ser descrita no nível do ecossistema, e não apenas como habilidade individual;
4. autonomia não equivale a adesão, engajamento ou conclusão de tarefas;
5. continuidade adaptativa deve aparecer como possibilidade de revisar, pausar, recusar ou renovar caminhos.

### Formulação candidata revisada

> O ecossistema preserva condições reais, contextualmente adequadas e não coercitivas para que Pessoas, Organizações e Coletivos exerçam agência efetiva e situada ao definir, revisar, pausar, recusar ou renovar seus próprios próximos passos, individualmente ou em relações de co-agência.

### Efeitos autorizados

- aceitar formalmente a disposição `Reformulate`;
- preservar a formulação original para rastreabilidade;
- registrar a formulação revisada como nova versão candidata;
- manter `ECO-CAND-003` em `Under Validation`;
- reaplicar os quatro testes da COEM antes de qualquer recomendação `Approve`;
- revisar posteriormente as fronteiras com `ECO-CAND-001` e `ECO-CAND-005`.

### Efeitos não autorizados

- promover `ECO-CAND-003` a `Approved`;
- criar código canônico `EO-###`;
- executar automaticamente a fusão de `ECO-CAND-005`;
- incorporar automaticamente `ECO-CAND-001`;
- usar voz, consentimento formal, quantidade de opções ou engajamento como prova suficiente de agência;
- iniciar AQS-O01, Business Capabilities ou Product Engineering.

### Gate de reentrada na COEM

A formulação revisada somente poderá receber nova disposição após:

1. reaplicação explícita dos quatro testes;
2. definição de evidências de condições reais e não coercitivas de escolha, revisão, pausa, recusa e renovação;
3. verificação de que a formulação não depende de produto, tecnologia, jornada ou métrica de engajamento;
4. revisão das fronteiras com compreensão contextual e continuidade adaptativa;
5. confirmação de observabilidade por múltiplos sinais, sem autodeclaração isolada.

## 6. Matriz cumulativa de decisões

| Candidato | Recomendação da COEM | Decisão humana | Estado decisório |
|---|---|---|---|
| ECO-CAND-001 | Reformulate | Aceitar `Reformulate` | decisão registrada; revisão candidata pendente de nova COEM |
| ECO-CAND-003 | Reformulate | Aceitar `Reformulate` | decisão registrada; revisão candidata pendente de nova COEM |
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

## 7. Gate do incremento

| Critério | Resultado |
|---|---|
| manifestação humana explícita | Pass |
| recomendação original preservada | Pass |
| fundamentação rastreável | Pass |
| formulação revisada registrada | Pass |
| estado `Under Validation` preservado | Pass |
| mudança automática de estado bloqueada | Pass |
| promoção canônica bloqueada | Pass |
| AQS-O01 não antecipado | Pass |
| Product Engineering preservado em pausa | Pass |

## 8. Próximo passo governado

Submeter `ECO-CAND-005 — Continuidade da evolução autodeterminada` à decisão humana individual sobre a recomendação `Merge into ECO-CAND-003`.

As formulações revisadas de `ECO-CAND-001` e `ECO-CAND-003` permanecem registradas, mas não retornam à COEM neste incremento e não recebem códigos canônicos.