---
id: GKR-UXA-102-V5-EFFECT-CLASSIFICATION-001
title: UXA-102 / V5 — Classificação Candidata por Natureza de Efeito
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: false
maturity: v5_a_classification
depends_on:
  - UXA-102
  - GKR-UXA-102-V5-TRANSITION-INVENTORY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
---

# UXA-102 / V5 — Classificação Candidata por Natureza de Efeito

## 1. Finalidade

Esta classificação organiza as 76 transições para priorizar o exame de erros, retornos, interrupções, resultados indeterminados e repetição segura.

Ela **não altera a maturidade** registrada no Transition Registry.

## 2. Classes

| Código | Natureza |
|---|---|
| N | navegação/continuidade sem mutação material esperada |
| C | criação ou commit de objeto/estado persistente |
| M | mutação de objeto/estado existente ou efeito material |
| H | handoff entre responsabilidades, perspectivas ou autoridades |
| B | boundary para autoridade externa |
| F | efeito ou decisão financeira/comercial/entitlement |
| D | distribuição, disponibilidade ou projeção |

Uma transição pode possuir várias classes.

## 3. Priorização de stress test

| Prioridade | Regra | Quantidade |
|---|---|---:|
| P1 | contém C, M, B ou F; duplicidade/indeterminação pode produzir efeito material | 33 |
| P2 | handoff/distribuição sem efeito material direto classificado | 28 |
| P3 | navegação neutra | 15 |
| **Total** |  | **76** |

As classes não são mutuamente exclusivas. Ocorrências por classe:

| Classe | Ocorrências |
|---|---:|
| N | 40 |
| C | 8 |
| M | 17 |
| H | 57 |
| B | 3 |
| F | 18 |
| D | 4 |

## 4. Classificação candidata

| ID | Família | Origem | Destino | Classe | Prioridade V5 | Maturidade corrente |
|---|---|---|---|---|---|---|
| GKR-TRN-001 | Pessoa | PER-001 | PER-002 | N,H | P2 | parcial |
| GKR-TRN-002 | Pessoa | PER-002 | PER-003 | N,H | P2 | localmente validada |
| GKR-TRN-003 | Pessoa | PER-003 | PER-004 | N,H | P2 | parcial |
| GKR-TRN-004 | Pessoa | PER-004 | PER-005 | N,H | P2 | parcial |
| GKR-TRN-005 | Pessoa | PER-005 | PER-006 | M,H | P1 | parcial |
| GKR-TRN-006 | Pessoa | PER-006 | PER-007 | N,H | P2 | localmente validada |
| GKR-TRN-014 | Pessoa | PER-003 | PER-013 | N,H | P2 | contratada |
| GKR-TRN-015 | Pessoa | PER-013 | PER-005 | N,H | P2 | contratada |
| GKR-TRN-016 | Pessoa | PER-003 | PER-014 | N,H | P2 | contratada |
| GKR-TRN-017 | Pessoa | PER-014 | PER-005 | N,H | P2 | contratada |
| GKR-TRN-007 | Pessoa | PER-007 | PER-008 | N,H | P2 | integralmente validada |
| GKR-TRN-008 | Pessoa | PER-008 | PER-010 | N | P3 | integralmente validada |
| GKR-TRN-009 | Pessoa | PER-010 | PER-008 | N | P3 | integralmente validada |
| GKR-TRN-010 | Pessoa | PER-008 | PER-011 | N | P3 | integralmente validada |
| GKR-TRN-011 | Pessoa | PER-011 | PER-008 | N | P3 | integralmente validada |
| GKR-TRN-012 | Pessoa | PER-008 | PER-012 | N | P3 | integralmente validada |
| GKR-TRN-013 | Pessoa | PER-012 | PER-008 | N | P3 | integralmente validada |
| GKR-TRN-101 | Pessoa/Coletivos | PER-101 | PER-102 | N | P3 | localmente validada |
| GKR-TRN-102 | Pessoa/Coletivos | PER-102 | PER-103 | N | P3 | parcial |
| GKR-TRN-103 | Pessoa/Coletivos | PER-103 | PER-104 | N,H | P2 | parcial |
| GKR-TRN-104 | Pessoa/Coletivos | PER-104 | PER-105 | C,H | P1 | parcial |
| GKR-TRN-105 | Pessoa/Coletivos | PER-105 | COL-003 | H | P2 | integralmente validada |
| GKR-TRN-106 | Pessoa/Coletivos | COL-003 | PER-105 | M,H | P1 | integralmente validada |
| GKR-TRN-107 | Pessoa/Coletivos | PER-105 | COL-003 | M,H | P1 | integralmente validada |
| GKR-TRN-108 | Pessoa/Coletivos | COL-003 | PER-106 | C,M,H | P1 | integralmente validada |
| GKR-TRN-109 | Pessoa/Coletivos | COL-003 | PER-105 | M,H | P1 | integralmente validada |
| GKR-TRN-110 | Pessoa/Coletivos | PER-106 | PER-107 | N | P3 | integralmente validada |
| GKR-TRN-111 | Pessoa/Coletivos | PER-107 | PER-108 | N | P3 | integralmente validada |
| GKR-TRN-112 | Pessoa/Coletivos | COL-002 | COL-003 | N | P3 | integralmente validada |
| GKR-TRN-113 | Pessoa/Coletivos | COL-004 | COL-005 | C,H | P1 | contratada |
| GKR-TRN-114 | Pessoa/Coletivos | COL-003 | COL-004 | N,H | P2 | contratada |
| GKR-TRN-201 | Organização/Oportunidades | ORG-001 | ORG-002 | N,H | P2 | parcial |
| GKR-TRN-202 | Organização/Oportunidades | ORG-002 | ORG-003 | N,H | P2 | localmente validada |
| GKR-TRN-203 | Organização/Oportunidades | ORG-003 | PER-201 | D,H | P2 | integralmente validada |
| GKR-TRN-204 | Organização/Oportunidades | PER-201 | PER-203 | N | P3 | integralmente validada |
| GKR-TRN-205 | Organização/Oportunidades | PER-203 | BND-001 | B,H | P1 | integralmente validada até a fronteira de autoridade Guivos |
| GKR-TRN-206 | Organização/Oportunidades | ORG-004 | COL-008 | C,H | P1 | contratada |
| GKR-TRN-207 | Organização/Oportunidades | COL-008 | ORG-005 | H | P2 | contratada |
| GKR-TRN-208 | Organização/Oportunidades | ORG-005 | ORG-006 | M,H | P1 | contratada |
| GKR-TRN-209 | Organização/Oportunidades | ORG-006 | ORG-006 | M | P1 | contratada |
| GKR-TRN-210 | Organização/Oportunidades | PER-201 | PER-202 | N | P3 | integralmente validada |
| GKR-TRN-211 | Organização/Oportunidades | PER-202 | PER-203 | N | P3 | integralmente validada |
| GKR-TRN-212 | Organização/Oportunidades | PER-203 | PER-204 | N,H | P2 | contratada |
| GKR-TRN-213 | Organização/Oportunidades | PER-204 | ORG-008 | C,H | P1 | contratada |
| GKR-TRN-214 | Organização/Oportunidades | ORG-003 | ORG-008 | N | P3 | contratada |
| GKR-TRN-215 | Organização/Oportunidades | ORG-008 | PER-204 | M,H | P1 | contratada |
| GKR-TRN-216 | Organização/Oportunidades | PER-204 | ORG-008 | M,H | P1 | contratada |
| GKR-TRN-301 | Opportunity Boost | COM-001 | COM-004 | M,F,H | P1 | parcial |
| GKR-TRN-302 | Opportunity Boost | COM-004 | COM-002 | D,H | P2 | parcial |
| GKR-TRN-303 | Opportunity Boost | COM-003 | COM-002 | N,H | P2 | localmente validada |
| GKR-TRN-304 | Opportunity Boost | COM-002 | PER-201 | D,H | P2 | parcial |
| GKR-TRN-305 | Opportunity Boost | COM-004 | COM-005 | M,H | P1 | parcial |
| GKR-TRN-306 | Opportunity Boost | COM-002 | PER-202 | D,H | P2 | parcial |
| GKR-TRN-401 | Planos | PER-301 | PER-302 | F,H | P1 | localmente validada |
| GKR-TRN-402 | Planos | PER-302 | PER-304 | C,M,F,H | P1 | localmente validada |
| GKR-TRN-403 | Planos | PER-301 | PER-303 | F,H | P1 | localmente validada |
| GKR-TRN-404 | Planos | PER-303 | PER-304 | M,F,H | P1 | localmente validada |
| GKR-TRN-405 | Planos | PER-304 | PER-301 | F,N | P1 | localmente validada |
| GKR-TRN-406 | Planos | PER-009 | PER-301 | N,H | P2 | contratada |
| GKR-TRN-407 | Planos | PER-301 | PER-009 | N,H | P2 | contratada |
| GKR-TRN-411 | Planos | COL-301 | COL-302 | F,H | P1 | localmente validada |
| GKR-TRN-412 | Planos | COL-302 | COL-304 | C,M,F,H | P1 | localmente validada |
| GKR-TRN-413 | Planos | COL-301 | COL-303 | F,H | P1 | localmente validada |
| GKR-TRN-414 | Planos | COL-303 | COL-304 | M,F,H | P1 | localmente validada |
| GKR-TRN-415 | Planos | COL-304 | COL-301 | F,N | P1 | localmente validada |
| GKR-TRN-416 | Planos | COL-301 | BND-002 | B,F,H | P1 | parcial |
| GKR-TRN-417 | Planos | COL-002 | COL-301 | N,H | P2 | integralmente validada |
| GKR-TRN-418 | Planos | COL-301 | COL-002 | N,H | P2 | integralmente validada |
| GKR-TRN-421 | Planos | ORG-301 | ORG-302 | F,H | P1 | localmente validada |
| GKR-TRN-422 | Planos | ORG-302 | ORG-304 | C,M,F,H | P1 | localmente validada |
| GKR-TRN-423 | Planos | ORG-301 | ORG-303 | F,H | P1 | localmente validada |
| GKR-TRN-424 | Planos | ORG-303 | ORG-304 | M,F,H | P1 | localmente validada |
| GKR-TRN-425 | Planos | ORG-304 | ORG-301 | F,N | P1 | localmente validada |
| GKR-TRN-426 | Planos | ORG-301 | BND-002 | B,F,H | P1 | parcial |
| GKR-TRN-427 | Planos | ORG-001 | ORG-301 | N,H | P2 | integralmente validada |
| GKR-TRN-428 | Planos | ORG-301 | ORG-001 | N,H | P2 | integralmente validada |

## 5. Leituras principais

### 5.1 P1

P1 concentra transições nas quais retry, timeout ou retorno incorreto pode:

- criar objeto duplicado;
- aplicar mutação duas vezes;
- fabricar vínculo;
- repetir comunicação material;
- duplicar envio;
- repetir efeito comercial/financeiro;
- atravessar fronteira externa sem reconciliação;
- produzir inconsistência de entitlement.

P1 deve ser examinado primeiro.

### 5.2 P2

P2 concentra handoffs e projeções que podem não mutar o objeto fonte, mas podem:

- carregar contexto incorreto;
- usar autoridade vencida;
- apontar para destino obsoleto;
- perder retorno;
- expor informação indevida;
- apresentar estado stale.

### 5.3 P3

P3 concentra navegações neutras. Mesmo nelas, retorno e refresh não podem fabricar leitura, aceite, progresso, evolução ou efeito material.

## 6. Classificações que exigem revisão humana posterior

Esta matriz é candidata. Em especial, combinações envolvendo `C`, `M` e `D` devem ser confrontadas com contratos específicos antes da adjudicação.

Uma mudança de classificação durante V5 não cria nem remove transição; apenas melhora a análise do efeito.

## 7. Gate V5-A2

```text
76 TRANSITIONS
→ 76 CLASSIFIED

P1
→ 33

P2
→ 28

P3
→ 15

MATERIAL MATURITY CHANGES
→ 0

NEXT
→ V5-B1 / P1 STRESS TEST
```
