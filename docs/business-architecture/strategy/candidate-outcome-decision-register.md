---
id: BA-STR-002-CODR-001
title: Candidate Outcome Decision Register
status: active
version: 0.7.0
owner: Guivos Business Architecture
last_updated: 2026-07-25
parent: BA-STR-002
depends_on:
  - BA-STR-002-COR-001
  - BA-STR-002-COEM-001
  - GKR-GOV-OUT-001
related:
  - BA-STR-002-EOVB-001
  - BA-STR-002-EOVB-006
  - RP-001-EVIDENCE
  - GKR-R6-RESUMPTION-001
  - BA-STR-002-COD-SUB-002
  - BA-STR-002-COD-SUB-003
  - BA-STR-002-COD-SUB-004
  - COD-001
  - COD-002
  - COD-003
  - COD-004
  - M7.6
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
5. a eventual formulação revisada ou alvo de fusão;
6. a mudança posterior de estado do candidato;
7. a futura consolidação na Canon.

Uma decisão registrada aqui não cria automaticamente um Outcome canônico. Reformulações permanecem candidatas e fusões somente alteram o COR quando a decisão humana e o incremento de registro autorizarem expressamente.

## 2. Estado formal

```text
Decision register: in progress — resumed by R6
Candidate dispositions in scope: 18
Human decisions recorded: 4
Decision submissions awaiting human response: 0
Accepted Reformulate dispositions: 3
Accepted Merge dispositions: 1
Accepted Reject dispositions: 0
Candidate state changes: 1
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
| Formulação revisada ou alvo | versão candidata ou destino da fusão, quando aplicável |
| Estado após a decisão | estado formal permitido no COR |
| Limites | efeitos expressamente não autorizados |
| Próximo gate | condição necessária antes do próximo ato de governança |

### Regras permanentes

- cada candidato recebe decisão individual;
- nenhuma decisão é inferida por contagem de testes, cobertura da COEM ou decisão tomada sobre outro candidato;
- uma recomendação `Reformulate` aceita não equivale a `Approved`;
- uma recomendação `Merge` aceita não aprova automaticamente o candidato-alvo;
- formulações revisadas ou combinadas devem ser reavaliadas pelos quatro testes da COEM;
- decisões `Merge` ou `Reject` somente alteram o COR quando o próprio registro decisório autorizar expressamente a mudança;
- candidatos fundidos permanecem rastreáveis e não são apagados;
- nenhum código `EO-###` ou `BO-###` nasce neste registro;
- AQS-O01 e consolidação canônica permanecem atos posteriores.

## 4. COD-001 — ECO-CAND-001

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

### Formulação candidata revisada

> Pessoas, Organizações e Coletivos formam e revisam uma compreensão contextual suficientemente fundamentada sobre sua situação, objetivos, necessidades, restrições e possibilidades, fortalecendo sua capacidade de realizar escolhas conscientes.

### Fundamentação e limites

A compreensão contextual possui relevância material e independência de produtos, mas pode operar predominantemente como condição de agência. A formulação revisada permanece `Under Validation`, deve retornar aos quatro testes e não recebe código canônico.

## 5. COD-002 — ECO-CAND-003

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

### Formulação candidata registrada em COD-002

> O ecossistema preserva condições reais, contextualmente adequadas e não coercitivas para que Pessoas, Organizações e Coletivos exerçam agência efetiva e situada ao definir, revisar, pausar, recusar ou renovar seus próprios próximos passos, individualmente ou em relações de co-agência.

### Fundamentação e limites

O núcleo de agência atende aos testes Essential, Decision e Replacement. A reformulação reconhece contexto, competência, pertencimento e co-agência. Ela não equivale a aprovação e foi posteriormente ampliada por `COD-003`, sem perder a rastreabilidade desta versão.

## 6. COD-003 — ECO-CAND-005

| Campo | Registro |
|---|---|
| Decisão | `COD-003` |
| Candidato | `ECO-CAND-005` |
| Nome provisório | Continuidade da evolução autodeterminada |
| Recomendação da COEM | `Merge into ECO-CAND-003` |
| Decisão humana | Aceitar `Merge into ECO-CAND-003` |
| Autoridade decisória | Fundador da Guivos |
| Data | 25/07/2026 |
| Estado após a decisão | `Merged` |
| Alvo | `ECO-CAND-003` |
| Estado do alvo | `Under Validation` |
| Código canônico | não criado |
| AQS-O01 | não iniciado |

### Formulação originalmente avaliada

> Participantes mantêm condições para reconhecer mudanças, aprender e iniciar novos ciclos de evolução coerentes com suas próprias escolhas.

### Formulação combinada resultante

> O ecossistema preserva condições reais, contextualmente adequadas e não coercitivas para que Pessoas, Organizações e Coletivos exerçam agência efetiva e situada ao definir, revisar, pausar, recusar, abandonar ou renovar seus próprios próximos passos diante de mudanças, aprendizados e limites legítimos, individualmente ou em relações de co-agência.

### Efeitos e limites

A decisão alterou `ECO-CAND-005` para `Merged`, preservou sua rastreabilidade e manteve `ECO-CAND-003` em `Under Validation`. Não criou código canônico, não iniciou AQS-O01 e não autorizou Business Capabilities ou Product Engineering.

## 7. COD-004 — ECO-CAND-002

| Campo | Registro |
|---|---|
| Decisão | `COD-004` |
| Candidato | `ECO-CAND-002` |
| Nome provisório original | Acesso a possibilidades relevantes |
| Nome provisório revisado | Acesso real a possibilidades legítimas e manejáveis |
| Recomendação da COEM | `Reformulate` |
| Decisão humana | Aceitar `Reformulate` |
| Autoridade decisória | Fundador da Guivos |
| Data | 25/07/2026 |
| Estado após a decisão | `Under Validation` |
| Código canônico | não criado |
| AQS-O01 | não iniciado |

### Formulação originalmente avaliada

> Participantes encontram possibilidades legítimas, compreensíveis e relevantes para seu contexto, seus objetivos e seu momento de vida.

### Fundamentação consolidada

A formulação original atende aos testes Essential, Decision e Replacement, mas falha parcialmente em Outcome Quality por sugerir descoberta ou disponibilidade nominal de alternativas.

A reformulação foi aceita porque:

1. acesso real depende de restrições e fatores de conversão;
2. disponibilidade não equivale a capacidade de compreender, comparar e escolher;
3. abundância de opções pode aumentar complexidade e reduzir escolha;
4. acesso não garante experiência, benefício ou transformação posterior;
5. a condição deve permanecer independente de catálogo, recomendação, marketplace, canal ou tecnologia.

### Formulação candidata revisada

> Pessoas, Organizações e Coletivos dispõem de acesso real a possibilidades legítimas, compreensíveis e manejáveis, compatíveis com seu contexto, objetivos, restrições e fatores de conversão, preservando liberdade substantiva para compará-las e escolhê-las sem que a abundância de opções seja tratada como evidência de valor.

### Efeitos autorizados

- aceitar formalmente a disposição `Reformulate`;
- preservar a formulação original para rastreabilidade;
- registrar a formulação revisada como versão candidata;
- manter `ECO-CAND-002` em `Under Validation`;
- reaplicar os quatro testes da COEM antes de qualquer aprovação.

### Efeitos não autorizados

- promover `ECO-CAND-002` a `Approved`;
- criar código canônico `EO-###`;
- tratar volume de ofertas, exposição ou recomendação como prova suficiente;
- prometer escolha, experiência, benefício ou transformação posterior;
- iniciar AQS-O01, Business Capabilities ou Product Engineering.

### Gate de reentrada na COEM

A formulação revisada somente poderá receber nova disposição após:

1. reaplicação explícita dos quatro testes;
2. definição de sinais de acesso real que não dependam de volume de opções;
3. verificação de restrições e fatores de conversão para Pessoas, Organizações e Coletivos;
4. separação entre acesso, escolha, experiência e valor realizado;
5. confirmação de independência de produto, canal e tecnologia.

## 8. Matriz cumulativa de decisões

| Candidato | Recomendação da COEM | Decisão humana | Estado decisório |
|---|---|---|---|
| ECO-CAND-001 | Reformulate | Aceitar `Reformulate` | decisão registrada; revisão candidata pendente de nova COEM |
| ECO-CAND-003 | Reformulate | Aceitar `Reformulate` | decisão registrada; formulação combinada pendente de nova COEM |
| ECO-CAND-005 | Merge into ECO-CAND-003 | Aceitar `Merge into ECO-CAND-003` | `Merged`; alvo ECO-CAND-003; rastreabilidade preservada |
| ECO-CAND-002 | Reformulate | Aceitar `Reformulate` | decisão registrada; revisão candidata pendente de nova COEM |
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

## 9. Gate do incremento

| Critério | Resultado |
|---|---|
| manifestação humana explícita | Pass |
| recomendação original preservada | Pass |
| `COD-004` registrado | Pass |
| formulação original preservada | Pass |
| formulação candidata revisada registrada | Pass |
| candidato mantido em `Under Validation` | Pass |
| promoção canônica bloqueada | Pass |
| AQS-O01 não antecipado | Pass |
| Product Engineering preservado em pausa | Pass |

## 10. Próximo passo governado

Preparar e submeter `ECO-CAND-004 — Realização de experiências de valor` à quinta decisão humana individual sobre a recomendação `Reject`.

As formulações revisadas e combinadas permanecem candidatas, sem códigos canônicos, até reentrada formal na COEM.
