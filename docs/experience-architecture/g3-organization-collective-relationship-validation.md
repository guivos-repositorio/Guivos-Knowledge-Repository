---
id: GKR-UX-G3-ORGANIZATION-COLLECTIVE-RELATIONSHIP-VALIDATION-001
title: G3 — Validação de Organização e Relação Organização–Coletivo
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: true
maturity: adjudicated_gap_validation
depends_on:
  - GKR-UXA-102-V5-AUTHORITY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - UXA-019
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
related:
  - GKR-UX-ORG-OPPORTUNITY-REGISTRATION-MASTER-001
  - GKR-UX-ORG-ACTIVE-OPPORTUNITY-MASTER-001
  - GKR-UX-ORG-COL-RELATIONSHIP-MASTER-001
  - GKR-UX-COL-ORG-RELATIONSHIP-MASTER-001
---

# G3 — Validação de Organização e Relação Organização–Coletivo

## 1. Finalidade

Este ato aprofunda a família G3 registrada após a UXA-102/V5:

- TRN-201
- TRN-202
- TRN-206
- TRN-207
- TRN-208
- TRN-209

O objetivo é verificar se as autoridades correntes sustentam promoção de maturidade ou somente refinamento das lacunas.

## 2. Resultado executivo

```text
TRN-201
→ PARTIAL / UNCHANGED

TRN-202
→ LOCALLY VALIDATED / UNCHANGED

TRN-206..209
→ CONTRACTED / UNCHANGED

MATURITY PROMOTIONS
→ 0
```

A ausência de promoção é uma decisão adjudicada.

## 3. TRN-201 — ORG-001 → ORG-002

Estado preservado: **partial**.

A Visão Geral da Organização já governa contexto, autoridade, atenção e continuidade legítima. O Cadastro de Oportunidade/Programa governa criação, revisão, rascunho, envio, cancelamento, falha, indeterminação e retry.

Entretanto, a continuidade `ORG-001 → ORG-002` permanece registrada como ligação parcial e o próprio Master de cadastro preserva sua maturidade.

## 4. TRN-202 — ORG-002 → ORG-003

Estado preservado: **locally validated**.

As autoridades correntes distinguem:

```text
CADASTRO / ENVIO
≠ APROVAÇÃO
≠ ATIVAÇÃO
```

`ORG-002` trata envio, processamento, falha, indeterminação e retry. `ORG-003` governa o estado institucional aprovado/ativo.

O Transition Registry já registra `TRN-202` como localmente validada, e os Masters preservam essa maturidade sem autorizar promoção adicional.

## 5. TRN-206..209 — relação Organização ↔ Coletivo

Estados preservados: **contracted**.

O conjunto corrente de autoridades define um único objeto bilateral com identidade lógica, finalidade, escopo, versão material, autoridades, compromissos, dados, recursos, histórico material, proteção e lifecycle.

```text
ORG-004
↓ TRN-206
COL-008
↓ TRN-207
ORG-005
↓ TRN-208
ORG-006
↓ TRN-209
ORG-006
```

### TRN-206

Disponibiliza ao Coletivo autorizado o mesmo objeto/proposta bilateral.

```text
RECEBER / VISUALIZAR
≠ APROVAR
≠ NEGOCIAR
≠ ATIVAR
```

### TRN-207

Mantém o mesmo objeto bilateral do Coletivo para a avaliação/negociação da Organização. Não transfere autoridade entre participantes.

### TRN-208

Só pode representar continuidade para relação ativa quando as autoridades legítimas aprovaram o mesmo escopo e as condições governadas de ativação estão satisfeitas.

```text
NEGOCIAÇÃO
≠ RELAÇÃO ATIVA
```

### TRN-209

Preserva o mesmo objeto durante revisão, alteração e continuidade.

```text
ALTERAÇÃO MATERIAL PENDENTE
≠ NOVO ESCOPO VIGENTE
```

A versão anterior permanece efetiva até nova aprovação legítima.

## 6. Concorrência, versão e idempotência

As autoridades correntes já cobrem:

- revalidar versão antes de ação material;
- revalidar autoridade após mudança de contexto;
- não aceitar alteração baseada em versão stale;
- reconsultar estado canônico após falha/indeterminação;
- impedir duplicidade por retry;
- não converter navegação/retorno em ativação ou alteração.

Portanto, concorrência, retry, retorno e estado indeterminado deixam de ser lacuna genérica de G3.

## 7. O que continua aberto

### G3-A — TRN-201

Falta validação ponta a ponta entre Visão Geral institucional e Cadastro de Oportunidade/Programa.

### G3-B — TRN-206

Falta validação ponta a ponta do handoff Organização → perspectiva do Coletivo.

### G3-C — TRN-207

Falta validação ponta a ponta do handoff Coletivo → avaliação/negociação da Organização.

### G3-D — TRN-208

Falta comprovação ponta a ponta do efeito negociação → relação ativa.

### G3-E — TRN-209

Falta validação dedicada de revisão/alteração/continuidade do mesmo objeto em estado ativo.

Além disso, os Masters especializados `ORG-004..006 / COL-008` permanecem contratos candidatos.

## 8. Não inferências

```text
LIFECYCLE DEFINED
≠ END-TO-END VALIDATED

BILATERAL APPROVAL
≠ TECHNICAL ACTIVATION CONFIRMED

NEGOTIATION
≠ ACTIVE RELATION

PENDING MATERIAL CHANGE
≠ CURRENT EFFECTIVE SCOPE

NAVIGATION
≠ AUTHORITY TRANSFER

RETRY
≠ DUPLICATE EFFECT
```

## 9. Guardrails

Este ato não:

- promove nenhuma transição;
- cria superfície;
- cria transição;
- cria relação Organização–Organização por analogia;
- cria relação Coletivo–Coletivo por analogia;
- cria score/ranking;
- define persistência técnica;
- define locking/versioning técnico;
- libera protótipo;
- libera Product Engineering.

## 10. Estado

```text
G3 VALIDATION
→ COMPLETE

MATURITY PROMOTIONS
→ 0

TRN-201
→ PARTIAL

TRN-202
→ LOCALLY VALIDATED

TRN-206..209
→ CONTRACTED

PRODUCT ENGINEERING
→ NOT RELEASED
```
