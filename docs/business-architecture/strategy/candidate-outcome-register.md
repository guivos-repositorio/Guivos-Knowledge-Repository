---
id: BA-STR-002-COR-001
title: Candidate Outcome Register
status: active
version: 0.30.0
owner: Guivos Business Architecture
last_updated: 2026-07-26
parent: BA-STR-002
depends_on:
  - BA-FND-001
  - BA-STR-001
  - GKR-GOV-OUT-001
related:
  - BA-STR-002-EOVP-001
  - BA-STR-002-COEM-001
  - BA-STR-002-CODR-001
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
  - GEM-CLOSURE-REVIEW-001
  - M7.20
normative: false
---

# BA-STR-002-COR-001 — Candidate Outcome Register

## 1. Autoridade e finalidade

Este registro reúne as 18 hipóteses de Ecosystem Outcomes e Business Outcomes do `BA-STR-002`, preservando formulações, decisões, fusões, rejeições e destinos antes de qualquer promoção à Canon.

A validação externa, a cobertura inicial da Matriz de Avaliação e as 18 decisões humanas individuais estão concluídas. Formulações revisadas e combinadas continuam em validação e deverão retornar aos quatro testes.

## 2. Estado formal

```text
Candidates: 18
Ecosystem candidates: 8
Business candidates: 10
Under Validation: 9
Merged: 3
Rejected: 6
Approved Outcomes: 0
Canonical EO/BO codes: 0
External validation: completed
Initial COEM coverage: completed — 18 of 18
Human decisions: completed — 18 of 18
AQS-O01 practical validation: not started
Operational authorization: no
```

## 3. Convenção

| Estado | Regra |
|---|---|
| `Under Validation` | formulação ativa aguardando reaplicação dos testes ou consolidação posterior |
| `Merged` | conteúdo incorporado a outro candidato por decisão humana, com rastreabilidade preservada |
| `Rejected` | candidato retirado do futuro catálogo, mantendo conceito, evidências e destino arquitetural |

Nenhum estado deste registro equivale a aprovação canônica.

## 4. Candidate Ecosystem Outcomes

| Candidato | Formulação ou natureza preservada | Estado | Decisão e situação |
|---|---|---|---|
| ECO-CAND-001 — Compreensão contextual suficiente | Pessoas, Organizações e Coletivos formam e revisam compreensão contextual suficientemente fundamentada para escolhas conscientes. | Under Validation | `COD-001 — Reformulate`; independência em relação à agência ainda deve ser testada. |
| ECO-CAND-002 — Acesso real a possibilidades legítimas e manejáveis | Acesso real considera contexto, restrições, fatores de conversão, compreensão, comparação e liberdade de escolha; volume de opções não comprova valor. | Under Validation | `COD-004 — Reformulate`; nova avaliação pendente. |
| ECO-CAND-003 — Agência efetiva e situada | Condições reais e não coercitivas para definir, revisar, pausar, recusar, abandonar ou renovar próximos passos, individualmente ou em co-agência. | Under Validation | `COD-002 — Reformulate`; recebeu ECO-CAND-005 por `COD-003`; formulação combinada pendente de nova avaliação. |
| ECO-CAND-004 — Realização de experiências de valor | Experiência permanece unidade da Jornada, realização de valor em uso e fonte de evidências, não Outcome permanente autônomo. | Rejected | `COD-005 — Reject`; conteúdo preservado na Arquitetura da Jornada. |
| ECO-CAND-005 — Continuidade da evolução autodeterminada | Continuidade adaptativa como dimensão temporal da agência efetiva. | Merged | `COD-003 — Merge into ECO-CAND-003`. |
| ECO-CAND-006 — Saúde relacional no ecossistema | Relações voluntárias, diversas e reciprocamente construtivas que ampliam cooperação e valor sem restringir autonomia ou produzir dano material. | Under Validation | `COD-006 — Reformulate`; fronteiras com acesso, proteção e legitimidade ainda devem ser testadas. |
| ECO-CAND-007 — Participação inclusiva, digna e efetiva | Participação com capacidade de uso, respeito, voz e contestabilidade, mediante redução de barreiras evitáveis e preservação de requisitos legítimos. | Under Validation | `COD-007 — Reformulate`; nova avaliação pendente. |
| ECO-CAND-008 — Participação protegida, justa e contestável | Condições verificáveis de proteção, justiça, contestabilidade, reparação e autonomia; conformidade ou ausência de incidentes não constituem prova suficiente. | Under Validation | `COD-008 — Reformulate`; nova avaliação pendente. |

## 5. Candidate Business Outcomes

| Candidato | Formulação ou natureza preservada | Estado | Decisão e situação |
|---|---|---|---|
| BUS-CAND-001 — Aderência permanente ao propósito | Permanece princípio constitucional, obrigação de governança e critério de admissibilidade contra desvio de missão. | Rejected | `COD-009 — Reject`; retirado do futuro catálogo de Business Outcomes. |
| BUS-CAND-002 — Relevância contínua das respostas | Relevância contextual contínua incorporada à habilitação consistente de valor legítimo. | Merged | `COD-010 — Merge into BUS-CAND-003`. |
| BUS-CAND-003 — Habilitação consistente e contextualmente relevante de valor legítimo | A Guivos sustenta condições para habilitar valor legítimo, detectando mudanças e ajustando proposições, capacidades e respostas sem presumir controle unilateral sobre valor vivido. | Under Validation | `COD-011 — Reformulate`; recebeu BUS-CAND-002; formulação combinada pendente de nova avaliação. |
| BUS-CAND-004 — Legitimidade institucional sustentada | Legitimidade sustentada por conduta, governança, transparência, contestabilidade e reparação verificáveis, sem tratar reputação ou confiança declarada como prova suficiente. | Under Validation | `COD-012 — Reformulate`; nova avaliação pendente. |
| BUS-CAND-005 — Continuidade econômica sustentável | A Guivos sustenta condições econômicas para cumprir obrigações e preservar valor essencial em múltiplos horizontes, mantendo opções legítimas de financiamento, alocação e renovação. | Under Validation | `COD-013 — Reformulate`; recebeu BUS-CAND-010 por `COD-018`; formulação combinada pendente de nova avaliação. |
| BUS-CAND-006 — Crescimento responsável e resiliente | Expansão responsável permanece trajetória estratégica opcional, condicionada à capacidade, adicionalidade e não degradação. | Rejected | `COD-014 — Reject`; resiliência e adaptação preservadas como propriedades ou capacidades sustentadoras. |
| BUS-CAND-007 — Aprendizado e adaptação institucionais | Aprendizagem permanece capacidade sustentadora multinível de percepção, interpretação, absorção, memória, contestação, renovação e adaptação. | Rejected | `COD-015 — Reject`; dados, inteligência artificial ou reuniões não comprovam aprendizagem por si. |
| BUS-CAND-008 — Saúde das relações de parceria | Governança de parceiros, alianças, dependências, controles, riscos e critérios de portfólio permanecem capacidades e decisões governadas. | Rejected | `COD-016 — Reject`; importância estratégica das parcerias preservada. |
| BUS-CAND-009 — Coerência global com adequação contextual | Permanece princípio arquitetural e critério governado para internacionalização, localização, desenho de capacidades e avaliação de mudanças. | Rejected | `COD-017 — Reject`; não impõe padronização global nem proíbe adaptação local. |
| BUS-CAND-010 — Capacidade de reinvestimento responsável | Capacidade governada de financiar renovação e preservar opções de investimento, sujeita a adicionalidade, riscos, obrigações, alternativas e avaliação de eficácia. | Merged | `COD-018 — Merge into BUS-CAND-005`; retenção, gasto ou percentual reinvestido não comprovam responsabilidade ou valor futuro. |

## 6. Formulação combinada de continuidade econômica sustentável

A formulação candidata de `BUS-CAND-005` permanece:

> A Guivos sustenta condições econômicas suficientes para cumprir obrigações e preservar valor essencial em múltiplos horizontes, mantendo opções legítimas de financiamento, alocação e renovação sem presumir permanência absoluta nem tratar receita, margem, caixa, disponibilidade operacional ou crescimento isolados como prova suficiente.

A incorporação de `BUS-CAND-010` acrescenta requisitos interpretativos, sem criar sub-Outcome:

- financiamento interno e externo permanecem alternativas legítimas;
- renovação somente deve ser financiada quando houver justificativa e adicionalidade material;
- riscos, obrigações protegidas, custo de oportunidade e alternativas de uso devem ser avaliados;
- reinvestimento proposto, aprovado, realizado e eficaz são estados distintos;
- avaliação anterior à alocação e aprendizado posterior à execução são necessários;
- retenção automática, sobreinvestimento e projetos de baixo valor legítimo devem ser evitados;
- maior gasto ou maior percentual reinvestido não comprovam continuidade, responsabilidade ou eficácia.

## 7. Sobreposições e decisões consolidadas

| Cluster | Estado após as decisões humanas |
|---|---|
| agência e evolução | ECO-CAND-005 fundido em ECO-CAND-003; formulações ativas exigem nova avaliação. |
| oportunidade e experiência | ECO-CAND-004 rejeitado; experiência preservada na Jornada; ECO-CAND-002 permanece em validação. |
| confiança e inclusão | ECO-CAND-006, ECO-CAND-007, ECO-CAND-008 e BUS-CAND-004 permanecem reformulados e aguardam nova avaliação. |
| valor e continuidade | BUS-CAND-002 fundido em BUS-CAND-003; BUS-CAND-010 fundido em BUS-CAND-005; BUS-CAND-003 e BUS-CAND-005 permanecem em validação. |
| crescimento, aprendizagem, parceria e adaptação global | BUS-CAND-006 a BUS-CAND-009 rejeitados como Outcomes, com conteúdos preservados em estratégia, princípios e capacidades futuras. |

## 8. Pendências para os próximos ciclos

Antes de qualquer promoção canônica deverão existir:

1. reaplicação dos quatro testes às nove formulações ativas, incluindo as formulações combinadas;
2. aplicação e ajuste prático do AQS-O01;
3. decisão formal sobre catálogos e códigos canônicos;
4. matriz de sustentação entre Ecosystem Outcomes e Business Outcomes;
5. clareza suficiente para iniciar a Arquitetura de Capacidades Empresariais.

## 9. Gate do incremento

| Critério | Resultado |
|---|---|
| decisões humanas individuais | 18/18 — Pass |
| `COD-018` registrado | Pass |
| `BUS-CAND-010` alterado para `Merged` | Pass |
| alvo `BUS-CAND-005` identificado | Pass |
| alvo mantido em `Under Validation` | Pass |
| formulação e evidências preservadas | Pass |
| reinvestimento automático bloqueado | Pass |
| distribuição 9/3/6 registrada | Pass |
| promoção automática bloqueada | Pass |
| Outcomes canônicos definidos | Not started |

## 10. Próximo passo governado

Após integração deste incremento e nova autorização, reaplicar os quatro testes às formulações revisadas e combinadas, ajustar o AQS-O01 e preparar a futura consolidação governada dos catálogos.