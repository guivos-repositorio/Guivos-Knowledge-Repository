---
id: GKR-UX-G5-OPPORTUNITY-BOOST-VALIDATION-001
title: G5 — Validação do Opportunity Boost
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: true
maturity: adjudicated_gap_validation
depends_on:
  - GKR-UXA-102-V5-AUTHORITY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - UXA-038
  - UXA-047
  - UXA-099
related:
  - UXA-043
  - UXA-045
  - GEM-007-A1
  - GEM-010-A2
---

# G5 — Validação do Opportunity Boost

## 1. Finalidade

Este ato aprofunda a família G5 registrada após a UXA-102/V5:

- TRN-301
- TRN-302
- TRN-303
- TRN-304
- TRN-305
- TRN-306

O objetivo é distinguir o que já está semanticamente governado do que continua dependente de integração/economia/implementação.

## 2. Resultado executivo

```text
TRN-301
→ PARTIAL / UNCHANGED

TRN-302
→ PARTIAL / UNCHANGED

TRN-303
→ LOCALLY VALIDATED / UNCHANGED

TRN-304
TRN-305
TRN-306
→ PARTIAL / UNCHANGED

MATURITY PROMOTIONS
→ 0
```

## 3. Princípios preservados

```text
PAID DISTRIBUTION
≠ ORGANIC RELEVANCE

PAID POSITION
≠ ORGANIC RANKING

IMPRESSION / CLICK
≠ IMPACT

PAUSE
≠ FINAL BILLING RULE

CANCEL
≠ ERASE VALID PAST EVENTS

RETRY
≠ DUPLICATE IMPRESSION / EVENT / SPEND / PREFERENCE
```

## 4. TRN-301 — COM-001 → COM-004

Estado preservado: **partial**.

A criação/configuração da campanha já possui contrato funcional para objetivo, orçamento, duração, limite diário, transparência, pausa e encerramento.

Porém, o próprio corpus separa experiência funcional de:

- oferta pública;
- checkout;
- cobrança;
- política financeira final;
- regras finais de saldo;
- implementação.

Logo, as regras econômicas e a integração ponta a ponta continuam abertas.

## 5. TRN-302 — COM-004 → COM-002

Estado preservado: **partial**.

A projeção patrocinada precisa permanecer identificada e separada da experiência orgânica.

Os contratos correntes já exigem:

- primeiro resultado orgânico preservado;
- publicidade identificada;
- contagens orgânicas e patrocinadas separadas;
- baixa oferta orgânica reduzindo publicidade;
- ocultação/desativação sem perda do catálogo orgânico.

Apesar disso, a integração campanha → projeção patrocinada nas superfícies correntes permanece parcial.

## 6. TRN-303 — COM-003 → COM-002

Estado preservado: **locally validated**.

O Registry já registra continuidade transversal localmente validada. Este ato não amplia sua maturidade.

## 7. TRN-304 — COM-002 → PER-201

Estado preservado: **partial**.

A continuidade entre projeção patrocinada e Mapa orgânico permanece parcial.

Regras correntes:

- seleção patrocinada não cria correspondência orgânica;
- marcador patrocinado não encobre oportunidade orgânica;
- publicidade não altera ordenação orgânica;
- desativar publicidade preserva Mapa/Lista/catálogo orgânico.

Isso ainda não fecha a integração ponta a ponta.

## 8. TRN-305 — COM-004 → COM-005

Estado preservado: **partial**.

`COM-005` possui contrato funcional de estados residuais validado por UXA-099, incluindo:

- erro técnico patrocinado;
- falha de atualização;
- inventário patrocinado indisponível;
- baixa oferta orgânica;
- preferência de mostrar menos;
- desativação de patrocinados;
- pausa protetiva;
- idempotência funcional.

Mas UXA-099 afirma explicitamente que isso **não promove TRN-305**. A ligação origem → estado residual continua sem validação ponta a ponta.

## 9. TRN-306 — COM-002 → PER-202

Estado preservado: **partial**.

O retorno patrocinado → Lista orgânica deve preservar consulta, filtros, região, seleção e catálogo orgânico sem fabricar resultado pago como orgânico.

A semântica está coberta, mas a ligação permanece parcial.

## 10. Falha, indeterminação, retry e reconciliação

Essas dimensões deixam de ser lacuna genérica de G5.

As autoridades correntes já exigem:

- pausa protetiva diante de informação material possivelmente desatualizada;
- nenhum novo gasto futuro presumido durante incerteza;
- estado indeterminado quando não houver confirmação suficiente;
- retry sem duplicar impressão, evento, gasto ou preferência;
- preservação do último estado confirmado;
- reconciliação posterior de eventos válidos;
- separação entre orçamento total, reservado, utilizado e saldo.

## 11. O que continua aberto

### G5-A — TRN-301

Regras econômicas finais, entitlement e integração ponta a ponta de criação/configuração de campanha.

### G5-B — TRN-302

Integração ponta a ponta campanha → projeção patrocinada.

### G5-C — TRN-304

Integração patrocinado → Mapa orgânico.

### G5-D — TRN-305

Ligação ponta a ponta campanha → estado residual.

### G5-E — TRN-306

Retorno patrocinado → Lista orgânica.

### G5-F — economia/operacionalização

Checkout, faturamento, cobrança, política final de saldo, antifraude técnico, mensuração operacional e implementação continuam fora deste ato.

## 12. Não inferências

```text
BUDGET
≠ GUARANTEED DELIVERY

PAID EXPOSURE
≠ ORGANIC MATCH

PAUSE
≠ REFUND RULE

CANCEL
≠ AUTOMATIC REFUND

METRIC
≠ HUMAN IMPACT

FUNCTIONAL IDEMPOTENCY
≠ TECHNICAL DEDUP IMPLEMENTATION
```

## 13. Guardrails

Este ato não:

- promove nenhuma transição;
- cria superfície;
- cria transição;
- define checkout;
- define faturamento;
- define cobrança real;
- define antifraude técnico;
- define algoritmo de entrega;
- define perfil publicitário individual;
- define deduplicação técnica;
- libera protótipo;
- libera Product Engineering.

## 14. Estado

```text
G5 VALIDATION
→ COMPLETE

TRN-301/302/304/305/306
→ PARTIAL / UNCHANGED

TRN-303
→ LOCALLY VALIDATED / UNCHANGED

MATURITY PROMOTIONS
→ 0

PRODUCT ENGINEERING
→ NOT RELEASED
```
