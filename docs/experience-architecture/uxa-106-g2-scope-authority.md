---
id: GKR-UXA-106-G2-SCOPE-AUTHORITY-001
title: UXA-106 — Autoridade de Escopo — Continuidade de Descoberta e Solicitação de Coletivo
status: active
version: 1.0.2
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-04
normative: true
maturity: scope_adjudicated
depends_on:
  - GKR-STATE-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
  - GKR-UX-G2-COLLECTIVE-DISCOVERY-REQUEST-VALIDATION-001
  - GKR-UXA-106-SCOPE-DISCOVERY-001
related:
  - UXA-106
  - GKR-UX-PER102-MASTER-001
  - GKR-UX-PER103-MASTER-001
  - GKR-UX-PER104-MASTER-001
  - GKR-UX-PER105-MASTER-001
---

# UXA-106 — Autoridade de Escopo — Continuidade de Descoberta e Solicitação de Coletivo

## 1. Autoridade

Este documento materializa a adjudicação humana do escopo da UXA-106.

```text
GKR-UXA-106-G2-SCOPE-AUTHORITY-001
→ ACTIVE
→ NORMATIVE
→ SCOPE ADJUDICATED
```

## 2. Escopo adjudicado

A UXA-106 examinará exclusivamente a continuidade funcional G2 entre resultado de descoberta, Perfil Público do Coletivo, revisão/solicitação e estado pendente:

- `TRN-102 — PER-102 → PER-103`;
- `TRN-103 — PER-103 → PER-104`;
- `TRN-104 — PER-104 → PER-105`;
- preservação da mesma intenção e do mesmo Coletivo ao longo da continuidade;
- seleção consciente sem criação de vínculo;
- abertura de revisão sem envio implícito;
- confirmação afirmativa antes do envio;
- envio diferente de aprovação;
- tratamento de falha, indeterminação, retry e retorno;
- ausência de duplicação lógica de solicitação;
- critérios verificáveis para eventual exame posterior de maturidade.

A UXA-106 não presume que as três transições devam receber a mesma conclusão de maturidade. Cada transição deverá ser examinada individualmente.

## 3. Fundamentação da escolha

G2 foi selecionado porque:

1. `PER-102/103/104/105` já possuem responsabilidades funcionais correntes;
2. `GKR-UX-G2-COLLECTIVE-DISCOVERY-REQUEST-VALIDATION-001` já eliminou falha, retorno e idempotência como lacunas genéricas;
3. `TRN-102/103/104` permanecem `PARTIAL` especificamente por falta de validação ponta a ponta das continuidades;
4. o escopo pode ser examinado documentalmente sem depender da entrega externa O/C high-fidelity;
5. o escopo não depende de checkout, billing, pricing ou operacionalização econômica;
6. o escopo não exige criar nova superfície ou nova transição.

## 4. Fora do escopo

Permanecem fora da UXA-106:

- `TRN-101`, já `LOCALLY VALIDATED`;
- `TRN-114 — COL-003 → COL-004`, que permanece `CONTRACTED`;
- promoção ou materialização de `COL-003/004`;
- persistência técnica de vínculo;
- fila técnica;
- aprovação do Coletivo;
- entrada efetiva em vínculo/participação;
- G3 — Organização e relação O↔C;
- G4 — processo interno de oportunidade;
- G5 — Opportunity Boost;
- Design high-fidelity;
- protótipo;
- implementação;
- Product Engineering;
- promoção automática de maturidade.

## 5. Efeito da adjudicação

A adjudicação:

- cria autoridade normativa somente para o limite do exame;
- não altera `TRN-102/103/104`, que permanecem `PARTIAL`;
- não altera `TRN-114`, que permanece `CONTRACTED`;
- não inicia exame funcional automaticamente;
- não autoriza maturity exam;
- não autoriza implementação.

## 6. Próximo gate

```text
UXA-106
→ SCOPE ADJUDICATED
→ ADJUDICATED SCOPE = TRN-102 / TRN-103 / TRN-104

FUNCTIONAL EXAM
→ COMPLETE

FUNCTIONAL CONTRACT
→ ADJUDICATED / NORMATIVE

MATURITY EXAM
→ NOT_STARTED
→ NOT_AUTHORIZED

NEXT GOVERNED GATE
→ MATURITY EXAM AUTHORIZATION
```
