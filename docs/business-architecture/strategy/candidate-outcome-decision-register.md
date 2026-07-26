---
id: BA-STR-002-CODR-001
title: Candidate Outcome Decision Register
status: active
version: 0.34.0
owner: Guivos Business Architecture
last_updated: 2026-07-26
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
  - BA-STR-002-COD-SUB-017
  - BA-STR-002-COD-SUB-018
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
  - COD-016
  - COD-017
  - COD-018
  - M7.20
normative: false
execution_status: completed
---

# BA-STR-002-CODR-001 — Candidate Outcome Decision Register

## 1. Autoridade e finalidade

Este registro preserva as decisões humanas individuais sobre as disposições recomendadas pela `BA-STR-002-COEM-001`.

Ele mantém separados:

1. formulação originalmente avaliada;
2. resultados dos quatro testes;
3. disposição recomendada;
4. decisão humana explícita;
5. formulação revisada, alvo de fusão ou destino arquitetural;
6. mudança de estado no Candidate Outcome Register;
7. futura consolidação na Canon.

Uma decisão registrada aqui não cria automaticamente um Outcome canônico. Reformulações permanecem candidatas; fusões e rejeições preservam rastreabilidade.

## 2. Estado formal

```text
Decision register: completed
Candidate dispositions in scope: 18
Human decisions recorded: 18
Decision submissions awaiting human response: 0
Accepted Reformulate dispositions: 9
Accepted Merge dispositions: 3
Accepted Reject dispositions: 6
Candidate state changes: 9
Under Validation: 9
Merged: 3
Rejected: 6
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
- formulações revisadas ou combinadas retornam aos quatro testes;
- candidatos fundidos ou rejeitados permanecem rastreáveis;
- nenhum código `EO-###` ou `BO-###` nasce neste registro;
- AQS-O01 e consolidação canônica permanecem atos posteriores.

## 4. Matriz cumulativa das decisões

| Código | Candidato | Recomendação aceita | Estado resultante | Destino ou situação |
|---|---|---|---|---|
| COD-001 | ECO-CAND-001 | Reformulate | Under Validation | compreensão contextual reformulada; nova avaliação pendente |
| COD-002 | ECO-CAND-003 | Reformulate | Under Validation | agência efetiva e situada; nova avaliação pendente |
| COD-003 | ECO-CAND-005 | Merge into ECO-CAND-003 | Merged | continuidade adaptativa incorporada à agência |
| COD-004 | ECO-CAND-002 | Reformulate | Under Validation | acesso real a possibilidades; nova avaliação pendente |
| COD-005 | ECO-CAND-004 | Reject | Rejected | experiência preservada na Arquitetura da Jornada |
| COD-006 | ECO-CAND-006 | Reformulate | Under Validation | saúde relacional reformulada; nova avaliação pendente |
| COD-007 | ECO-CAND-007 | Reformulate | Under Validation | participação inclusiva e digna; nova avaliação pendente |
| COD-008 | ECO-CAND-008 | Reformulate | Under Validation | participação protegida e contestável; nova avaliação pendente |
| COD-009 | BUS-CAND-001 | Reject | Rejected | aderência ao propósito preservada como autoridade constitucional e obrigação de governança |
| COD-010 | BUS-CAND-002 | Merge into BUS-CAND-003 | Merged | relevância contextual incorporada à habilitação de valor |
| COD-011 | BUS-CAND-003 | Reformulate | Under Validation | formulação combinada pendente de nova avaliação |
| COD-012 | BUS-CAND-004 | Reformulate | Under Validation | legitimidade institucional sustentada; nova avaliação pendente |
| COD-013 | BUS-CAND-005 | Reformulate | Under Validation | continuidade econômica sustentável; nova avaliação pendente |
| COD-014 | BUS-CAND-006 | Reject | Rejected | expansão responsável preservada como trajetória opcional |
| COD-015 | BUS-CAND-007 | Reject | Rejected | aprendizagem e adaptação preservadas como capacidades sustentadoras |
| COD-016 | BUS-CAND-008 | Reject | Rejected | governança de parceiros e alianças preservada como capacidade |
| COD-017 | BUS-CAND-009 | Reject | Rejected | coerência global e adequação contextual preservadas como princípio e critério governado |
| COD-018 | BUS-CAND-010 | Merge into BUS-CAND-005 | Merged | financiamento responsável da renovação incorporado à continuidade econômica sustentável |

## 5. Resolução da décima oitava decisão — COD-018

### Candidato

`BUS-CAND-010 — Capacidade de reinvestimento responsável`

### Formulação originalmente avaliada

> A Guivos mantém condições para reinvestir valor legitimamente capturado no fortalecimento de capacidades, conhecimento e valor entregue ao ecossistema.

### Resultado da Matriz de Avaliação

| Teste | Resultado | Fundamentação resumida |
|---|---|---|
| Essential | Partial | renovação pode depender de diferentes fontes e formas de financiamento; reinvestimento interno não é condição universal nem intrinsecamente responsável |
| Decision | Pass | incapacidade de financiar renovação ou alocação destrutiva exige revisão estratégica |
| Replacement | Pass | a necessidade de financiar renovação permanece mesmo com substituição dos meios atuais |
| Outcome Quality | Partial | o conceito descreve predominantemente condição financeira e mecanismo governado de alocação |

### Decisão humana

| Campo | Registro |
|---|---|
| Recomendação | `Merge into BUS-CAND-005` |
| Decisão humana | Aceitar `Merge into BUS-CAND-005` |
| Autoridade | Fundador da Guivos |
| Data | 26/07/2026 |
| Estado anterior | `Under Validation` |
| Estado resultante | `Merged` |
| Alvo | `BUS-CAND-005 — Continuidade econômica sustentável` |
| Estado do alvo | `Under Validation` |
| Código canônico | não criado |
| AQS-O01 | não iniciado |

### Conteúdo incorporado

A continuidade econômica sustentável passa a preservar explicitamente:

- opções legítimas de financiamento interno e externo;
- financiamento da renovação condicionado por adicionalidade e justificativa material;
- avaliação de riscos, obrigações protegidas, custo de oportunidade e alternativas;
- distinção entre reinvestimento proposto, aprovado, realizado e eficaz;
- avaliação anterior à alocação e aprendizado posterior à execução;
- bloqueio de retenção automática, sobreinvestimento e projetos de baixo valor legítimo;
- proibição de tratar maior gasto, retenção ou percentual reinvestido como prova automática de responsabilidade, continuidade ou eficácia.

A formulação candidata de `BUS-CAND-005` permanece em validação e deverá retornar aos quatro testes.

## 6. Efeitos autorizados por COD-018

- registrar a décima oitava decisão humana;
- alterar BUS-CAND-010 para `Merged`;
- identificar BUS-CAND-005 como alvo;
- preservar formulação, evidências e histórico do candidato fundido;
- incorporar requisitos de financiamento e alocação responsável ao contexto interpretativo do alvo;
- manter BUS-CAND-005 em `Under Validation`;
- concluir a fase de decisões humanas individuais.

## 7. Efeitos bloqueados

- aprovar ou canonicalizar BUS-CAND-005;
- criar código canônico `BO-###`;
- tornar reinvestimento obrigatório ou automático;
- exigir financiamento exclusivamente interno;
- usar gasto, retenção ou volume de investimento como prova de valor;
- iniciar AQS-O01, catálogos canônicos ou matriz de sustentação;
- iniciar Capacidades Empresariais, produtos, Modelo Comercial ou Entrada no Mercado;
- retomar Engenharia de Produto ou W0-01.

## 8. Gate de conclusão do registro

| Critério | Resultado |
|---|---|
| decisões individuais registradas | 18/18 — Pass |
| recomendações originais preservadas | Pass |
| decisões humanas explícitas | Pass |
| distribuição 9/3/6 registrada | Pass |
| candidatos fundidos e rejeitados rastreáveis | Pass |
| alvos das fusões identificados | Pass |
| candidatos reformulados mantidos em validação | Pass |
| promoção canônica bloqueada | Pass |
| AQS-O01 não antecipado | Pass |
| Engenharia de Produto preservada em pausa | Pass |

## 9. Próximo passo governado

Após integração deste incremento e nova autorização, reaplicar os quatro testes às formulações revisadas e combinadas, ajustar o AQS-O01 e preparar a futura consolidação governada dos catálogos canônicos.

A conclusão deste registro não autoriza automaticamente nenhuma dessas etapas.