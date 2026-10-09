---
id: GKR-UXA-107-TRN201-MATURITY-EXAM-001
title: UXA-107 — TRN-201 — Exame de Maturidade da Continuidade ORG-001 → ORG-002
status: active
version: 1.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-09
normative: true
maturity: maturity_promotion_materialized
depends_on:
  - GKR-UXA-107-TRN201-SCOPE-EXAM-001
  - GKR-UXA-107-TRN201-FUNCTIONAL-EXAM-001
  - GKR-UX-G3-ORGANIZATION-COLLECTIVE-RELATIONSHIP-VALIDATION-001
  - GKR-UXA-102-V5-AUTHORITY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-JOURNEY-GAPS-001
  - GKR-STATE-001
  - GKR-TRN-201
---

# UXA-107 — TRN-201 — Exame de Maturidade da Continuidade ORG-001 → ORG-002

## 1. Finalidade

Este documento executa exclusivamente o Maturity Exam autorizado da UXA-107 sobre:

```text
TRN-201
→ ORG-001 — Visão Geral da Organização
→ ORG-002 — Cadastro de Oportunidade / Programa
```

O escopo e o contrato funcional correspondente já estão `ADJUDICATED / NORMATIVE`.

Este exame não promove maturidade. Ele verifica a elegibilidade documental de `TRN-201` para eventual promoção por gate humano separado.

## 2. Baseline de maturidade

```text
TRN-201
→ BASELINE = PARTIAL

MATURITY PROMOTIONS
→ 0
```

A razão local registrada antes do exame era:

> **ligação com visão institucional**

A autoridade G3 também havia preservado `TRN-201` em `PARTIAL` porque a continuidade ponta a ponta entre a Visão Geral institucional e o Cadastro de Oportunidade/Programa ainda não havia sido validada como conjunto.

## 3. Critério do Registry

A leitura de maturidade distingue:

```text
FUNCTIONALLY SUFFICIENT
≠ AUTOMATIC MATURITY PROMOTION

LOCALLY VALIDATED
≠ INTEGRALLY VALIDATED

DOCUMENTARY VALIDATION
≠ IMPLEMENTATION
```

O exame pergunta se permanece alguma lacuna funcional **local** conhecida que obrigue `TRN-201` a continuar em `PARTIAL`.

## 4. Evidência corrente

O contrato funcional adjudicado pela UXA-107 fecha documentalmente, dentro do recorte `ORG-001 → ORG-002`:

1. preservação da mesma Organização/unidade/contexto;
2. ação consciente para iniciar ou retomar o cadastro;
3. revalidação de autoridade quando material;
4. abertura de ORG-002 sem criação automática de rascunho, envio, publicação ou ativação;
5. retorno e abandono antes de efeito material sem fabricar falha ou rollback;
6. indisponibilidade e resultado indeterminado sem fabricar sucesso;
7. retry/reabertura sem duplicação do efeito lógico;
8. separação entre cadastro em ORG-002 e oportunidade aprovada/ativa em ORG-003;
9. preservação de TRN-202 fora deste recorte;
10. ausência de inferência por analogia para relações O↔C.

A autoridade transversal UXA-102/V5 permanece aplicável a estado canônico, resultado indeterminado, retry após reconciliação, retorno, interrupção, idempotência funcional e revalidação de autoridade.

## 5. Leitura de maturidade de TRN-201

A razão local anteriormente registrada — **ligação com visão institucional** — foi precisamente o objeto do Scope Exam e do Functional Exam da UXA-107.

A continuidade `ORG-001 → ORG-002` foi examinada de forma autônoma, e o contrato funcional foi adjudicado normativamente sem necessidade de nova regra funcional.

Não permanece lacuna funcional local conhecida que, por si só, exija manter `TRN-201` em `PARTIAL`.

```text
TRN-201
→ CURRENT = LOCALLY VALIDATED
→ ADJUDICATED ELIGIBILITY = LOCALLY VALIDATED
→ PROMOTION MATERIALIZED
→ INTEGRALLY VALIDATED NOT SUPPORTED
```

## 6. Limite da evidência

A evidência disponível sustenta maturidade **local** de `TRN-201`.

Ela não comprova:

- implementação real;
- persistência técnica;
- telemetria ou observabilidade;
- testes end-to-end em produto;
- mecanismo técnico específico de idempotência;
- publicação, aprovação ou ativação em ORG-003;
- promoção adicional de TRN-202;
- TRN-203;
- TRN-206..209;
- relação bilateral Organização ↔ Coletivo;
- cadeia G3 integralmente validada;
- qualquer estado além de `LOCALLY VALIDATED`.

`LOCALLY VALIDATED` permanece uma maturidade documental local, não comprovação de implementação ou integração técnica.

## 7. Adjudicação humana e materialização

Os achados de maturidade foram adjudicados humanamente e a promoção autorizada foi materializada.

```text
HUMAN MATURITY ADJUDICATION
→ COMPLETE

TRN-201
→ ADJUDICATED ELIGIBILITY = LOCALLY VALIDATED
→ CURRENT = LOCALLY VALIDATED

PROMOTION MATERIALIZATION
→ COMPLETE
```

## 8. Resultado do exame

```text
UXA-107 MATURITY EXAM
→ COMPLETE

MATURITY FINDINGS
→ ADJUDICATED

TRN-201
→ CURRENT = LOCALLY VALIDATED
→ FUNCTIONALLY SUFFICIENT / ADJUDICATED
→ ADJUDICATED ELIGIBILITY = LOCALLY VALIDATED

INTEGRALLY VALIDATED
→ NOT SUPPORTED

PROMOTION MATERIALIZATION
→ COMPLETE

MATURITY PROMOTIONS MATERIALIZED
→ 1
→ PARTIAL → LOCALLY VALIDATED

TRANSITION REGISTRY
→ UPDATED / TRN-201 = LOCALLY VALIDATED

G3 INTEGRALLY VALIDATED
→ NOT CLAIMED

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```

## 9. Não inferências

Este ato:

- promove `TRN-201` exclusivamente de `PARTIAL` para `LOCALLY VALIDATED` conforme gate humano autorizado;
- altera o Transition Registry exclusivamente para refletir essa promoção adjudicada;
- não promove `TRN-202`;
- não altera `TRN-206..209`;
- não declara G3 integralmente validada;
- não cria implementação, persistência ou teste técnico;
- não libera Design, protótipo ou Product Engineering.

## 10. Próximo gate

A promoção adjudicada foi materializada no Transition Registry e nas autoridades sincronizadas.

```text
TRN-201
→ OPERATIVE MATURITY = LOCALLY VALIDATED

MATURITY PROMOTIONS MATERIALIZED
→ 1
```

`INTEGRALLY VALIDATED` permanece não suportado. Qualquer avanço adicional exige novo exame e gate próprio.
