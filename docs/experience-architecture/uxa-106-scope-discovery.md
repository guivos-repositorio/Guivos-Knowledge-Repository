---
id: GKR-UXA-106-SCOPE-DISCOVERY-001
title: UXA-106 — Descoberta de Escopo
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-04
normative: false
maturity: scope_adjudicated
depends_on:
  - GKR-STATE-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
  - GKR-UXA-105-TRN001-MATURITY-EXAM-001
related:
  - UXA-105
  - GKR-UX-G2-COLLECTIVE-DISCOVERY-REQUEST-VALIDATION-001
  - GKR-UX-G3-ORGANIZATION-COLLECTIVE-RELATIONSHIP-VALIDATION-001
  - GKR-UX-G4-INTERNAL-OPPORTUNITY-PROCESS-VALIDATION-001
  - GKR-UX-G5-OPPORTUNITY-BOOST-VALIDATION-001
  - GKR-UXA-106-G2-SCOPE-AUTHORITY-001
---

# UXA-106 — Descoberta de Escopo

## 1. Estado deste artefato

Este documento abre a UXA-106 exclusivamente no estágio de descoberta de escopo.

```text
UXA-106
→ SCOPE DISCOVERY COMPLETE
→ SCOPE ADJUDICATED
→ AUTHORITY = GKR-UXA-106-G2-SCOPE-AUTHORITY-001

FUNCTIONAL EXAM
→ NOT_STARTED
→ NOT_AUTHORIZED

MATURITY EXAM
→ NOT_STARTED
→ NOT_AUTHORIZED

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```

Este artefato é não normativo. Ele não adjudica escopo, não altera transições, não promove maturidade e não autoriza Design, protótipo, implementação ou Product Engineering.

## 2. Base canônica consultada

UXA-105 concluiu o tratamento local de `TRN-001 — PER-001 → PER-002`, promovendo-a para `LOCALLY VALIDATED`.

Após esse fechamento, G1 permanece sem validação integral ponta a ponta, mas não possui lacuna local equivalente pendente que deva ser presumida como próxima UXA.

As lacunas documentais correntes estão concentradas em G2–G5.

## 3. Candidatos de escopo

### Candidato A — G2 / descoberta e solicitação de Coletivo

Estado corrente:

- `TRN-101` localmente validada;
- `TRN-102/103/104` permanecem `PARTIAL`;
- `TRN-114` permanece `CONTRACTED`;
- validação ponta a ponta e maturidade/materialização de `COL-003/004` permanecem abertas.

### Candidato B — G3 / Organização e relação O↔C

Estado corrente:

- `TRN-201` permanece `PARTIAL`;
- `TRN-202` está localmente validada;
- `TRN-206..209` permanecem `CONTRACTED`;
- autoridades bilaterais e validação ponta a ponta permanecem incompletas.

### Candidato C — G4 / processo interno de oportunidade

Estado corrente:

- `TRN-212` e `TRN-214` permanecem `CONTRACTED`;
- retornos `PER-204 → PER-203` e `ORG-008 → ORG-003` permanecem contextuais sem IDs dedicados;
- maturidade/materialização dos contratos de `PER-204/ORG-008` permanece aberta.

### Candidato D — G5 / Opportunity Boost

Estado corrente:

- `TRN-301/302/304/305/306` permanecem `PARTIAL`;
- `TRN-303` está localmente validada;
- integração ponta a ponta e operacionalização econômica permanecem abertas;
- nenhuma cobrança, mensuração ou deduplicação técnica pode ser inventada.

## 4. Convergência analítica

```text
CURRENT RESULT
→ SCOPE ADJUDICATED

G2
→ SELECTED
→ TRN-102 / TRN-103 / TRN-104

TRN-114
→ OUTSIDE ADJUDICATED SCOPE
→ REMAINS CONTRACTED

G3
G4
G5
→ OUTSIDE UXA-106 SCOPE
```

A convergência foi adjudicada humanamente em favor do núcleo G2 `TRN-102/103/104`. A autoridade normativa é `GKR-UXA-106-G2-SCOPE-AUTHORITY-001`.

## 5. Limites

Este artefato:

- não cria nova autoridade normativa;
- não altera `TRN-101..114`, `TRN-201..214` ou `TRN-301..306`;
- não cria novos `TRN-ID` ou `SURF-ID`;
- não promove maturidade;
- não presume validação integral ponta a ponta;
- não autoriza protótipo ou implementação;
- não libera Product Engineering;
- não interfere na frente O/C high-fidelity, cuja entrega externa permanece separada.

## 6. Próximo gate humano

```text
NEXT GOVERNED GATE
→ AUTHORIZE UXA-106 FUNCTIONAL EXAM

ADJUDICATED SCOPE
→ G2
→ TRN-102 / TRN-103 / TRN-104
```

O exame funcional permanece `NOT_STARTED / NOT_AUTHORIZED` até autorização humana própria.
