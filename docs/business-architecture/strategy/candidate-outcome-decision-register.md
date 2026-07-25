---
id: BA-STR-002-CODR-001
title: Candidate Outcome Decision Register
status: active
version: 0.9.0
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
  - BA-STR-002-COD-SUB-005
  - COD-001
  - COD-002
  - COD-003
  - COD-004
  - COD-005
  - M7.7
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
Decision submissions awaiting human response: 0
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

A recomendação foi aceita porque:

1. experiência vivida é episódio de realização, não condição permanente autônoma do ecossistema;
2. o participante realiza valor em uso, enquanto a Guivos cria condições e facilita experiências;
3. valor vivido e avaliação retrospectiva podem divergir;
4. a formulação mistura acesso, escolha, conversão, experiência, percepção e potencial de evolução;
5. experiência não garante transformação causal nem efeito duradouro;
6. promover o candidato estruturaria o catálogo de Outcomes como sequência de jornada.

### Destino arquitetural preservado

Experiência permanece:

- unidade relevante da arquitetura da Jornada;
- momento possível de realização de valor;
- fonte de evidências para avaliação de Outcomes;
- referência para capacidades, experiências e métricas futuras;
- distinta de acesso, escolha, valor lembrado e transformação posterior.

### Efeitos autorizados

- aceitar `Reject`;
- alterar `ECO-CAND-004` para `Rejected`;
- preservar formulação, evidências e rastreabilidade;
- retirar o candidato do futuro catálogo de Outcomes;
- preservar experiência em sua camada arquitetural adequada.

### Efeitos não autorizados

- remover experiência da Guivos;
- alterar automaticamente o `PAS-001`;
- apagar o candidato ou suas evidências;
- criar código canônico;
- iniciar AQS-O01, Business Capabilities ou Product Engineering.

## 9. Matriz cumulativa de decisões

| Candidato | Recomendação da COEM | Decisão humana | Estado decisório |
|---|---|---|---|
| ECO-CAND-001 | Reformulate | Aceitar `Reformulate` | revisão candidata pendente de nova COEM |
| ECO-CAND-003 | Reformulate | Aceitar `Reformulate` | formulação combinada pendente de nova COEM |
| ECO-CAND-005 | Merge into ECO-CAND-003 | Aceitar `Merge into ECO-CAND-003` | `Merged`; alvo ECO-CAND-003 |
| ECO-CAND-002 | Reformulate | Aceitar `Reformulate` | revisão candidata pendente de nova COEM |
| ECO-CAND-004 | Reject | Aceitar `Reject` | `Rejected`; experiência preservada na Jornada |
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

## 10. Gate do incremento

| Critério | Resultado |
|---|---|
| manifestação humana explícita | Pass |
| recomendação original preservada | Pass |
| `COD-005` registrado | Pass |
| `ECO-CAND-004` alterado para `Rejected` | Pass |
| formulação e evidências preservadas | Pass |
| experiência preservada na Jornada | Pass |
| promoção canônica bloqueada | Pass |
| AQS-O01 não antecipado | Pass |
| Product Engineering preservado em pausa | Pass |

## 11. Próximo passo governado

Preparar e submeter `ECO-CAND-006 — Conexões relevantes e fortalecedoras` à sexta decisão humana individual sobre a recomendação `Reformulate`.
