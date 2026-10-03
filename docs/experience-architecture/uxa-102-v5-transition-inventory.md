---
id: GKR-UXA-102-V5-TRANSITION-INVENTORY-001
title: UXA-102 / V5 — Inventário Inicial de Transições
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: false
maturity: v5_a_inventory
depends_on:
  - UXA-102
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
---

# UXA-102 / V5 — Inventário Inicial de Transições

## 1. Finalidade

Este inventário materializa o primeiro passo de V5-A: comprovar quais transições existem antes de examinar falha, interrupção, retorno, resultado indeterminado e repetição segura.

Ele não altera a maturidade de nenhuma transição.

## 2. Resultado da reconciliação quantitativa

Foram encontrados **76 IDs únicos**, sem duplicidade.

| Família | Quantidade |
|---|---:|
| Jornada pessoal | 17 |
| Pessoa em Coletivos / operação do responsável | 14 |
| Organização / oportunidades / relações bilaterais | 16 |
| Opportunity Boost | 6 |
| Planos / cobrança / ciclo de vida | 23 |
| **Total** | **76** |

A baseline canônica anterior declarava 72 porque a contagem da Jornada pessoal permanecia em 13 apesar da existência de `TRN-014..017`. A correção mecânica passa a reconhecer 17 transições nessa família e 76 no total.

## 3. Inventário

| ID | Família | Origem | Destino | Maturidade corrente | Classe V5 | Exame V5 |
|---|---|---|---|---|---|---|
| GKR-TRN-001 | Jornada pessoal | PER-001 | PER-002 | parcial | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-002 | Jornada pessoal | PER-002 | PER-003 | localmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-003 | Jornada pessoal | PER-003 | PER-004 | parcial | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-004 | Jornada pessoal | PER-004 | PER-005 | parcial | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-005 | Jornada pessoal | PER-005 | PER-006 | parcial | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-006 | Jornada pessoal | PER-006 | PER-007 | localmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-014 | Jornada pessoal | PER-003 | PER-013 | contratada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-015 | Jornada pessoal | PER-013 | PER-005 | contratada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-016 | Jornada pessoal | PER-003 | PER-014 | contratada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-017 | Jornada pessoal | PER-014 | PER-005 | contratada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-007 | Jornada pessoal | PER-007 | PER-008 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-008 | Jornada pessoal | PER-008 | PER-010 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-009 | Jornada pessoal | PER-010 | PER-008 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-010 | Jornada pessoal | PER-008 | PER-011 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-011 | Jornada pessoal | PER-011 | PER-008 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-012 | Jornada pessoal | PER-008 | PER-012 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-013 | Jornada pessoal | PER-012 | PER-008 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-101 | Pessoa em Coletivos / operação do responsável | PER-101 | PER-102 | localmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-102 | Pessoa em Coletivos / operação do responsável | PER-102 | PER-103 | parcial | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-103 | Pessoa em Coletivos / operação do responsável | PER-103 | PER-104 | parcial | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-104 | Pessoa em Coletivos / operação do responsável | PER-104 | PER-105 | parcial | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-105 | Pessoa em Coletivos / operação do responsável | PER-105 | COL-003 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-106 | Pessoa em Coletivos / operação do responsável | COL-003 | PER-105 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-107 | Pessoa em Coletivos / operação do responsável | PER-105 | COL-003 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-108 | Pessoa em Coletivos / operação do responsável | COL-003 | PER-106 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-109 | Pessoa em Coletivos / operação do responsável | COL-003 | PER-105 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-110 | Pessoa em Coletivos / operação do responsável | PER-106 | PER-107 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-111 | Pessoa em Coletivos / operação do responsável | PER-107 | PER-108 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-112 | Pessoa em Coletivos / operação do responsável | COL-002 | COL-003 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-113 | Pessoa em Coletivos / operação do responsável | COL-004 | COL-005 | contratada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-114 | Pessoa em Coletivos / operação do responsável | COL-003 | COL-004 | contratada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-201 | Organização / oportunidades / relações bilaterais | ORG-001 | ORG-002 | parcial | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-202 | Organização / oportunidades / relações bilaterais | ORG-002 | ORG-003 | localmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-203 | Organização / oportunidades / relações bilaterais | ORG-003 | PER-201 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-204 | Organização / oportunidades / relações bilaterais | PER-201 | PER-203 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-205 | Organização / oportunidades / relações bilaterais | PER-203 | BND-001 | integralmente validada até a fronteira de autoridade Guivos | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-206 | Organização / oportunidades / relações bilaterais | ORG-004 | COL-008 | contratada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-207 | Organização / oportunidades / relações bilaterais | COL-008 | ORG-005 | contratada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-208 | Organização / oportunidades / relações bilaterais | ORG-005 | ORG-006 | contratada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-209 | Organização / oportunidades / relações bilaterais | ORG-006 | ORG-006 | contratada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-210 | Organização / oportunidades / relações bilaterais | PER-201 | PER-202 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-211 | Organização / oportunidades / relações bilaterais | PER-202 | PER-203 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-212 | Organização / oportunidades / relações bilaterais | PER-203 | PER-204 | contratada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-213 | Organização / oportunidades / relações bilaterais | PER-204 | ORG-008 | contratada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-214 | Organização / oportunidades / relações bilaterais | ORG-003 | ORG-008 | contratada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-215 | Organização / oportunidades / relações bilaterais | ORG-008 | PER-204 | contratada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-216 | Organização / oportunidades / relações bilaterais | PER-204 | ORG-008 | contratada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-301 | Opportunity Boost | COM-001 | COM-004 | parcial | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-302 | Opportunity Boost | COM-004 | COM-002 | parcial | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-303 | Opportunity Boost | COM-003 | COM-002 | localmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-304 | Opportunity Boost | COM-002 | PER-201 | parcial | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-305 | Opportunity Boost | COM-004 | COM-005 | parcial | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-306 | Opportunity Boost | COM-002 | PER-202 | parcial | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-401 | Planos / cobrança / ciclo de vida | PER-301 | PER-302 | localmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-402 | Planos / cobrança / ciclo de vida | PER-302 | PER-304 | localmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-403 | Planos / cobrança / ciclo de vida | PER-301 | PER-303 | localmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-404 | Planos / cobrança / ciclo de vida | PER-303 | PER-304 | localmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-405 | Planos / cobrança / ciclo de vida | PER-304 | PER-301 | localmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-406 | Planos / cobrança / ciclo de vida | PER-009 | PER-301 | contratada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-407 | Planos / cobrança / ciclo de vida | PER-301 | PER-009 | contratada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-411 | Planos / cobrança / ciclo de vida | COL-301 | COL-302 | localmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-412 | Planos / cobrança / ciclo de vida | COL-302 | COL-304 | localmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-413 | Planos / cobrança / ciclo de vida | COL-301 | COL-303 | localmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-414 | Planos / cobrança / ciclo de vida | COL-303 | COL-304 | localmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-415 | Planos / cobrança / ciclo de vida | COL-304 | COL-301 | localmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-416 | Planos / cobrança / ciclo de vida | COL-301 | BND-002 | parcial | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-417 | Planos / cobrança / ciclo de vida | COL-002 | COL-301 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-418 | Planos / cobrança / ciclo de vida | COL-301 | COL-002 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-421 | Planos / cobrança / ciclo de vida | ORG-301 | ORG-302 | localmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-422 | Planos / cobrança / ciclo de vida | ORG-302 | ORG-304 | localmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-423 | Planos / cobrança / ciclo de vida | ORG-301 | ORG-303 | localmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-424 | Planos / cobrança / ciclo de vida | ORG-303 | ORG-304 | localmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-425 | Planos / cobrança / ciclo de vida | ORG-304 | ORG-301 | localmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-426 | Planos / cobrança / ciclo de vida | ORG-301 | BND-002 | parcial | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-427 | Planos / cobrança / ciclo de vida | ORG-001 | ORG-301 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |
| GKR-TRN-428 | Planos / cobrança / ciclo de vida | ORG-301 | ORG-001 | integralmente validada | TO_CLASSIFY | TO_EXAMINE |

## 4. Leitura do estado

`TO_CLASSIFY` significa que a natureza do efeito ainda será classificada no próprio V5-A.

`TO_EXAMINE` significa que a transição ainda não foi submetida ao exame transversal de:

- interrupção voluntária;
- falha conhecida;
- resultado indeterminado;
- retorno/retomada;
- repetição segura/idempotência.

Esses marcadores não são novos estados do Transition Registry.

## 5. Gate V5-A1

```text
TRANSITION IDS
→ 76 UNIQUE

DUPLICATES
→ 0

BASELINE COUNT
→ RECONCILED

V5 EFFECT CLASSIFICATION
→ PENDING

V5 FAILURE/RETURN EXAM
→ PENDING
```

O próximo passo é classificar as 76 transições por natureza do efeito antes de testar cenários de falha.
