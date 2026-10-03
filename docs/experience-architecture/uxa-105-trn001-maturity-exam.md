---
id: GKR-UXA-105-TRN001-MATURITY-EXAM-001
title: UXA-105 — TRN-001 — Exame Específico de Maturidade
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: false
maturity: maturity_exam_complete_candidate
depends_on:
  - GKR-UXA-105-TRN001-SCOPE-EXAM-001
  - GKR-UXA-105-TRN001-FUNCTIONAL-EXAM-001
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-PER002-MASTER-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-UX-G1-ENTRY-EXPRESSION-INVENTORY-VALIDATION-001
  - GKR-JOURNEY-GAPS-001
  - GKR-STATE-001
---

# UXA-105 — TRN-001 — Exame Específico de Maturidade

## 1. Finalidade

Este documento executa o exame específico de maturidade autorizado da UXA-105 exclusivamente sobre:

```text
TRN-001
→ PER-001 — HOME PÚBLICA
→ PER-002 — ENTRADA PROTEGIDA
```

O exame avalia se a evidência documental corrente sustenta mudança de maturidade de `PARTIAL` para `LOCALLY VALIDATED`.

Este documento **não adjudica nem materializa promoção de maturidade**. Qualquer promoção exige gate humano próprio posterior.

## 2. Estado de entrada

O Transition Registry registra:

```text
GKR-TRN-001
→ PER-001 → PER-002
→ PARTIAL
→ lacuna: continuidade entre pacotes
```

A UXA-105 já possui:

```text
SCOPE
→ ADJUDICATED / NORMATIVE

FUNCTIONAL EXAM
→ COMPLETE

FUNCTIONAL CONTRACT
→ ADJUDICATED / NORMATIVE

TRN-001
→ FUNCTIONALLY SUFFICIENT / ADJUDICATED
→ MATURITY PARTIAL / UNCHANGED
```

## 3. Critério do Registry

O Registry distingue:

- **integralmente validada** — origem, destino, autoridade, dados, efeito, retorno, interrupção e concorrência examinados como ligação ponta a ponta dentro do limite declarado;
- **localmente validada** — examinada dentro do pacote indicado sem comprovação ponta a ponta;
- **parcial** — cobertura incompleta ou ligação ainda não validada como conjunto.

O exame deve verificar se a lacuna que justificava `PARTIAL` continua materialmente aberta após a adjudicação funcional da UXA-105.

## 4. Evidência por dimensão

| Dimensão | Evidência corrente | Resultado do exame |
|---|---|---|
| origem | `PER-001` é Home pública; `Iniciar Jornada` é ação voluntária distinta de explorar a Home | FECHADA |
| destino | `PER-002` é a primeira responsabilidade protegida e explica finalidade, proteção, alternativas e controles | FECHADA |
| gatilho | a mudança ocorre por ação consciente de iniciar a Journey | FECHADA |
| autoridade | entrada protegida não equivale a consentimento genérico, processamento, personalização ou conclusão de autenticação | FECHADA |
| dados | `TRN-001` não exige transferência de relato material; dados técnicos de navegação/acesso não são conteúdo da Journey | FECHADA |
| efeito | o efeito funcional é exclusivamente o handoff de contexto público → protegido | FECHADA |
| primeira entrada × retomada | `Iniciar Jornada` e Login possuem responsabilidades distintas | FECHADA |
| retorno | voltar para a Home é legítimo e não produz efeito material | FECHADA |
| interrupção / não prosseguimento | interrupção e não prosseguimento não equivalem a falha ou recusa global | FECHADA |
| falha / indisponibilidade | tentativa, falha conhecida e estado indeterminado são distintos; ausência de acesso não autoriza fallback material | FECHADA LOCALMENTE |
| retry / reentrada | retry revalida o contexto e não presume autorização material | FECHADA NO LIMITE FUNCIONAL |
| concorrência / duplicação lógica | repetir a tentativa não deve criar efeito material duplicado; `TRN-001` não gera processamento/autorização por si | FECHADA NO LIMITE FUNCIONAL |
| acessibilidade | significado público → protegido deve sobreviver sem dependência exclusiva de cor, motion, hover ou mídia rica | FECHADA |
| continuidade G1 ponta a ponta | a cadeia completa contém transições com maturidades distintas e não foi reexaminada integralmente como uma única cadeia | NÃO COMPROVADA INTEGRALMENTE |
| implementação técnica | roteamento, sessão, autenticação técnica, persistência e comportamento em produção não foram comprovados | NÃO COMPROVADA |

## 5. Lacuna histórica

A lacuna registrada para `TRN-001` era:

> continuidade entre pacotes.

A adjudicação funcional da UXA-105 passou a examinar explicitamente, como um único pacote documental:

- origem pública;
- destino protegido;
- ação consciente;
- mudança de contexto;
- autoridade;
- dados;
- efeito;
- retorno;
- interrupção;
- falha e indeterminação;
- retry;
- duplicação lógica;
- fronteira com autenticação e downstream.

Não permanece lacuna funcional local conhecida que, por si só, exija manter `TRN-001` em `PARTIAL`.

## 6. Limite da evidência

A cobertura é suficiente para exame **local**, porém não sustenta `INTEGRALLY VALIDATED`.

Razões:

1. o exame está circunscrito ao pacote `PER-001 → PER-002`;
2. não comprova roteamento ou autenticação técnica em execução;
3. não comprova persistência ou sessão real;
4. não valida a cadeia G1 completa como unidade ponta a ponta;
5. não converte validação documental em evidência operacional.

```text
LOCAL FUNCTIONAL CLOSURE
≠ END-TO-END IMPLEMENTATION PROOF

TRN-001 LOCALLY VALIDATED
≠ G1 INTEGRALLY VALIDATED
```

## 7. Conclusão do exame

A conclusão analítica é:

```text
UXA-105 MATURITY EXAM
→ COMPLETE

TRN-001 CURRENT
→ PARTIAL / UNCHANGED

CANDIDATE ELIGIBILITY
→ LOCALLY VALIDATED

INTEGRALLY VALIDATED
→ NOT SUPPORTED BY CURRENT EVIDENCE

MATURITY PROMOTIONS
→ 0

HUMAN MATURITY ADJUDICATION
→ PENDING
```

Conclusão:

> **A evidência corrente sustenta elegibilidade candidata para promover `TRN-001` de `PARTIAL` para `LOCALLY VALIDATED`, mas não sustenta `INTEGRALLY VALIDATED`.**

## 8. Efeito sobre G1

Mesmo se a promoção local vier a ser adjudicada em gate posterior:

```text
TRN-001
→ LOCALLY VALIDATED

G1 COMPLETE CHAIN
→ NOT AUTOMATICALLY INTEGRALLY VALIDATED
```

A maturidade de cada transição permanece individual. A promoção local de `TRN-001` não equivale a uma nova adjudicação ponta a ponta da família G1.

## 9. Limites

Este exame:

- não altera o Transition Registry;
- não altera `GKR-JOURNEY-GAPS-001`;
- não promove `TRN-001`;
- não altera `TRN-002..017`;
- não comprova implementação;
- não libera Product Engineering;
- não autoriza Design, protótipo ou execução técnica;
- não declara G1 integralmente validada.

## 10. Próximo gate

```text
MATURITY EXAM
→ COMPLETE

CANDIDATE ELIGIBILITY
→ PARTIAL → LOCALLY VALIDATED

NEXT GOVERNED GATE
→ AUTHORIZE UXA-105 MATURITY ADJUDICATION
```

Somente a adjudicação humana posterior poderá autorizar a promoção material no Transition Registry e nas autoridades de estado.
