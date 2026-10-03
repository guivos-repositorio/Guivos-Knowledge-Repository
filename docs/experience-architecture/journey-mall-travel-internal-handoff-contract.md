---
id: GKR-UX-JOURNEY-MALL-TRAVEL-HANDOFF-CONTRACT-001
title: Journey → Mall / Travel — Contrato Canônico de Handoff Interno
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: true
maturity: contracted_internal_handoff
depends_on:
  - GPA-SPECIALIZED-EXPERIENCE-POLICY-001
  - GPA-SPECIALIZED-JOURNEY-MATRIX-001
  - GPA-002
  - GPA-003
related:
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
---

# Journey → Mall / Travel — Contrato Canônico de Handoff Interno

## 1. Finalidade

Fechar semanticamente os gaps `SP-GAP-001` e `SP-GAP-002` por meio de contratos explícitos de handoff interno entre Guivos Journey e Guivos Mall/Travel.

Este ato não cria superfície, transição granular, checkout, reserva, pagamento, pedido, carrinho ou implementação.

## 2. Regra comum

Journey → Mall e Journey → Travel são handoffs internos de nível 3 quando a responsabilidade dominante muda entre Produtos Especializados ainda sob autoridade Guivos.

```text
PRODUCT REFERENCE INSIDE JOURNEY
≠ JOURNEY → MALL HANDOFF

TRAVEL-RELATED OPPORTUNITY INSIDE JOURNEY
≠ JOURNEY → TRAVEL HANDOFF

HANDOFF
→ REQUIRES REAL CHANGE OF DOMINANT RESPONSIBILITY
```

`BND-001` não se aplica enquanto a autoridade permanecer na Guivos.

## 3. Journey → Mall

| Campo | Contrato |
|---|---|
| origem | responsabilidade Journey em que item, serviço ou oferta é apresentado sem autoridade transacional presumida |
| destino | Guivos Mall, quando o contexto passa a ser comércio, item, pedido, compra, assinatura ou outra relação transacional sob responsabilidade Mall |
| trigger | ação afirmativa e consciente da Pessoa para entrar no contexto especializado do Mall |
| identidade | preservar apenas a referência lógica necessária ao item/serviço/oferta e ao contexto legitimamente aplicável |
| contexto | somente o contexto necessário para continuidade da intenção; recomendação no Journey não prova transação |
| dados | somente dados necessários, autorizados e compatíveis com finalidade; nenhum compartilhamento irrestrito |
| autoridade | Journey deixa de ser autoridade transacional; Mall passa a responder pela decisão especializada dentro de seu escopo |
| consequência | mudança explícita da responsabilidade dominante para Mall; nenhum checkout, estoque, pedido ou pagamento é criado por este contrato |
| retorno | retorno neutro ao contexto Journey de origem quando materializado, sem presumir compra, abandono, conversão ou sucesso |
| recuperação | reconciliar estado canônico; indisponibilidade/falha não gera compra; repetição não duplica efeito material quando houver implementação |
| transparência | a mudança para contexto comercial deve ser perceptível antes de qualquer consequência transacional |
| maturidade | contratado; não materializado como `SURF/TRN` dedicado |

## 4. Journey → Travel

| Campo | Contrato |
|---|---|
| origem | responsabilidade Journey em que possibilidade, oportunidade ou contexto relacionado a viagem é apresentado sem autoridade operacional de Travel presumida |
| destino | Guivos Travel, quando o contexto passa a planejamento, experiência, roteiro, reserva ou operação de viagem sob responsabilidade Travel |
| trigger | ação afirmativa e consciente da Pessoa para entrar no contexto especializado do Travel |
| identidade | preservar apenas a referência lógica necessária à possibilidade/experiência/viagem e ao contexto legitimamente aplicável |
| contexto | somente o contexto necessário para continuidade da intenção; oportunidade relacionada a viagem não é, por si só, superfície Travel |
| dados | somente dados necessários, autorizados e compatíveis com finalidade; nenhum compartilhamento irrestrito |
| autoridade | Journey deixa de responder pela decisão especializada de viagem; Travel passa a responder dentro de seu escopo |
| consequência | mudança explícita da responsabilidade dominante para Travel; nenhuma reserva, emissão, pagamento ou operação externa é criada por este contrato |
| retorno | retorno neutro ao contexto Journey de origem quando materializado, sem presumir reserva, compra, conclusão ou sucesso |
| recuperação | reconciliar estado canônico; indisponibilidade/falha não gera reserva; repetição não duplica efeito material quando houver implementação |
| transparência | a mudança para contexto Travel deve ser perceptível antes de qualquer consequência especializada |
| maturidade | contratado; não materializado como `SURF/TRN` dedicado |

## 5. Interno × externo

Enquanto Mall ou Travel permanecerem sob autoridade Guivos:

```text
JOURNEY → MALL
→ INTERNAL HANDOFF

JOURNEY → TRAVEL
→ INTERNAL HANDOFF

BND-001
→ NOT APPLICABLE
```

Uma eventual execução por terceiro fora da autoridade Guivos poderá exigir fronteira própria somente quando autoridade específica futura a definir.

## 6. Dados e autoridade

O handoff interno não autoriza compartilhamento irrestrito entre produtos.

Aplicam-se:

- finalidade;
- minimização;
- autorização quando necessária;
- proveniência;
- separação de autoridade;
- revalidação do estado canônico;
- preservação apenas do contexto ainda autorizado.

## 7. Não inferências

```text
JOURNEY SHOWS PRODUCT
≠ MALL TRANSACTION

JOURNEY SHOWS TRAVEL POSSIBILITY
≠ TRAVEL BOOKING

INTERNAL HANDOFF CONTRACT
≠ NEW SCREEN
≠ NEW TRN-ID
≠ CHECKOUT
≠ PAYMENT
≠ RESERVATION
≠ IMPLEMENTATION
```

## 8. Materialização futura

Nova superfície ou transição granular somente deverá ser criada quando uma necessidade real de navegação, dados, consequência, recuperação ou autoridade exigir materialização própria.

Até esse momento:

```text
SP-GAP-001
→ SEMANTIC CONTRACT CLOSED
→ MATERIALIZATION NOT CREATED

SP-GAP-002
→ SEMANTIC CONTRACT CLOSED
→ MATERIALIZATION NOT CREATED
```

## 9. Estado

```text
JOURNEY → MALL
→ CONTRACTED INTERNAL HANDOFF

JOURNEY → TRAVEL
→ CONTRACTED INTERNAL HANDOFF

NEW SURFACES
→ 0

NEW TRANSITIONS
→ 0

PRODUCT ENGINEERING
→ NOT RELEASED
```
