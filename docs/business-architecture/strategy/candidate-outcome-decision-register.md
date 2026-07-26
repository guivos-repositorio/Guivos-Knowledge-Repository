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
2. resultados dos quatro testes da COEM;
3. disposição recomendada;
4. decisão humana explícita;
5. formulação revisada, alvo de fusão ou destino arquitetural;
6. mudança de estado no COR;
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

> A Guivos sustenta condições para habilitar valor legítimo com consistência e relevância contextual, detectando mudanças materiais e ajustando proposições, capacidades e respostas de forma coerente, sem presumir controle unilateral sobre o valor realizado pelos participantes nem tratar personalização, satisfação pontual, disponibilidade técnica ou velocidade de resposta como prova suficiente.

### COD-012 — BUS-CAND-004

| Campo | Registro |
|---|---|
| Nome | Legitimidade institucional sustentada |
| Recomendação | `Reformulate` |
| Decisão humana | Aceitar `Reformulate` |
| Autoridade | Fundador da Guivos |
| Data | 25/07/2026 |
| Estado anterior | `Under Validation` |
| Estado resultante | `Under Validation` |
| Código canônico | não criado |
| AQS-O01 | não iniciado |

#### Formulação originalmente avaliada

> A Guivos preserva confiança e legitimidade suficientes para manter relações voluntárias, transparentes e duradouras no ecossistema.

#### Formulação candidata revisada

> A legitimidade institucional da Guivos é sustentada perante participantes e stakeholders por conduta coerente, governança responsável, transparência, contestabilidade e reparação verificáveis, sem presumir controle unilateral sobre avaliações socialmente conferidas nem tratar reputação, conformidade, satisfação, confiança declarada ou longevidade das relações como prova suficiente.

Confiança institucional permanece avaliação relacional associada. A decisão não cria novo candidato ou Outcome para confiança, mantém `BUS-CAND-004` em `Under Validation` e exige nova aplicação dos quatro testes da COEM.

### COD-013 — BUS-CAND-005

| Campo | Registro |
|---|---|
| Nome | Continuidade econômica sustentável |
| Recomendação | `Reformulate` |
| Decisão humana | Aceitar `Reformulate` |
| Autoridade | Fundador da Guivos |
| Data | 25/07/2026 |
| Estado anterior | `Under Validation` |
| Estado resultante | `Under Validation` |
| Código canônico | não criado |
| AQS-O01 | não iniciado |

#### Formulação originalmente avaliada

> A Guivos mantém recursos, capacidade e equilíbrio econômico suficientes para cumprir obrigações e preservar o valor essencial ao longo do tempo.

#### Formulação candidata revisada

> A Guivos sustenta condições econômicas suficientes para cumprir obrigações e preservar valor essencial em múltiplos horizontes, mantendo opções legítimas de financiamento, alocação e renovação sem presumir permanência absoluta nem tratar receita, margem, caixa, disponibilidade operacional ou crescimento isolados como prova suficiente.

Continuidade operacional, resiliência, equilíbrio financeiro, reservas, financiamento e alocação permanecem dimensões ou capacidades sustentadoras. `BUS-CAND-010` foi posteriormente fundido neste candidato por `COD-018`; a formulação combinada permanece em `Under Validation` e exige nova aplicação dos quatro testes.

### COD-014 — BUS-CAND-006

| Campo | Registro |
|---|---|
| Nome | Crescimento responsável e resiliente |
| Recomendação | `Reject` |
| Decisão humana | Aceitar `Reject` |
| Autoridade | Fundador da Guivos |
| Data | 25/07/2026 |
| Estado anterior | `Under Validation` |
| Estado resultante | `Rejected` |
| Código canônico | não criado |
| AQS-O01 | não iniciado |

A rejeição alcança somente a candidatura de crescimento como Outcome permanente. **Expansão responsável** permanece trajetória estratégica opcional, condicionada à capacidade demonstrada, adicionalidade e critérios de não degradação. Resiliência e adaptação legítima permanecem propriedades de continuidade ou capacidades sustentadoras.

### COD-015 — BUS-CAND-007

| Campo | Registro |
|---|---|
| Nome | Aprendizado e adaptação institucionais |
| Recomendação | `Reject` |
| Decisão humana | Aceitar `Reject` |
| Autoridade | Fundador da Guivos |
| Data | 25/07/2026 |
| Estado anterior | `Under Validation` |
| Estado resultante | `Rejected` |
| Código canônico | não criado |
| AQS-O01 | não iniciado |

A rejeição alcança somente a candidatura de aprendizado institucional como Outcome permanente. Aprendizado e adaptação permanecem capacidades sustentadoras multinível, incluindo sensing, interpretação, absorção, memória, contestação, renovação e adaptação. Coleta de dados, analytics, IA, reuniões ou retrospectivas não constituem prova suficiente de aprendizagem institucional.

### COD-016 — BUS-CAND-008

| Campo | Registro |
|---|---|
| Nome | Saúde das relações de parceria |
| Recomendação | `Reject` |
| Decisão humana | Aceitar `Reject` |
| Autoridade | Fundador da Guivos |
| Data | 25/07/2026 |
| Estado anterior | `Under Validation` |
| Estado resultante | `Rejected` |
| Código canônico | não criado |
| AQS-O01 | não iniciado |

A rejeição alcança somente a candidatura de saúde das relações de parceria como Outcome permanente. Governança de parceiros, gestão de alianças, dependências externas, confiança, controles, riscos relacionais e de desempenho e critérios de portfólio permanecem capacidades e dimensões governadas. A decisão não reduz a importância estratégica das parcerias e não exige internalização.

### COD-017 — BUS-CAND-009

| Campo | Registro |
|---|---|
| Nome | Coerência global com adequação contextual |
| Recomendação | `Reject` |
| Decisão humana | Aceitar `Reject` |
| Autoridade | Fundador da Guivos |
| Data | 25/07/2026 |
| Estado anterior | `Under Validation` |
| Estado resultante | `Rejected` |
| Código canônico | não criado |
| AQS-O01 | não iniciado |

A rejeição alcança somente a candidatura de coerência global com adequação contextual como Outcome permanente. O conteúdo permanece como princípio arquitetural e critério governado para internacionalização, localização, desenho de capacidades e avaliação de mudanças. A decisão não impõe padronização global, não proíbe adaptação local e não exige internacionalização.

### COD-018 — BUS-CAND-010

| Campo | Registro |
|---|---|
| Nome | Capacidade de reinvestimento responsável |
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

#### Formulação originalmente avaliada

> A Guivos mantém condições para reinvestir valor legitimamente capturado no fortalecimento de capacidades, conhecimento e valor entregue ao ecossistema.

#### Resultado da COEM preservado

| Teste | Resultado | Fundamentação resumida |
|---|---|---|
| Essential | Partial | renovação pode depender de diferentes fontes e formas de financiamento; reinvestimento interno não é condição universal nem intrinsecamente responsável |
| Decision | Pass | incapacidade de financiar renovação ou alocação destrutiva exige revisão estratégica |
| Replacement | Pass | a necessidade de financiar renovação permanece mesmo com substituição dos meios atuais |
| Outcome Quality | Partial | o conceito descreve predominantemente condição financeira e mecanismo governado de alocação |

#### Conteúdo incorporado ao alvo

- opções legítimas de financiamento interno e externo;
- financiamento da renovação condicionado por adicionalidade e justificativa material;
- avaliação de riscos, obrigações protegidas, custo de oportunidade e alternativas;
- distinção entre reinvestimento proposto, aprovado, realizado e eficaz;
- avaliação anterior à alocação e aprendizado posterior à execução;
- bloqueio de retenção automática, sobreinvestimento e projetos de baixo valor legítimo;
- proibição de tratar maior gasto, retenção ou percentual reinvestido como prova automática de responsabilidade, continuidade ou eficácia.

A fusão não aprova `BUS-CAND-005`. Sua formulação combinada permanece em `Under Validation` e deverá retornar aos quatro testes da COEM.

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
| BUS-CAND-004 | Reformulate | Aceitar `Reformulate` | nova COEM pendente |
| BUS-CAND-005 | Reformulate | Aceitar `Reformulate` | formulação combinada pendente de nova COEM |
| BUS-CAND-006 | Reject | Aceitar `Reject` | `Rejected` |
| BUS-CAND-007 | Reject | Aceitar `Reject` | `Rejected` |
| BUS-CAND-008 | Reject | Aceitar `Reject` | `Rejected` |
| BUS-CAND-009 | Reject | Aceitar `Reject` | `Rejected` |
| BUS-CAND-010 | Merge into BUS-CAND-005 | Aceitar `Merge into BUS-CAND-005` | `Merged` |

## 6. Gate de conclusão

| Critério | Resultado |
|---|---|
| manifestação humana explícita para cada candidato | 18/18 — Pass |
| recomendações originais preservadas | Pass |
| `COD-018` registrado | Pass |
| `BUS-CAND-010` alterado para `Merged` | Pass |
| alvo `BUS-CAND-005` identificado e mantido em validação | Pass |
| formulações e evidências preservadas | Pass |
| distribuição 9/3/6 registrada | Pass |
| promoção canônica bloqueada | Pass |
| AQS-O01 não antecipado | Pass |
| Product Engineering preservado em pausa | Pass |

## 7. Próximo passo governado

Após integração deste incremento e nova autorização, reaplicar os quatro testes às formulações revisadas e combinadas, ajustar o AQS-O01 e preparar a futura consolidação governada dos catálogos.

A conclusão deste registro não inicia automaticamente nenhuma dessas etapas.