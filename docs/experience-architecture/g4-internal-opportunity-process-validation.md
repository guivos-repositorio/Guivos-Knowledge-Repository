---
id: GKR-UX-G4-INTERNAL-OPPORTUNITY-PROCESS-VALIDATION-001
title: G4 — Validação do Processo Interno de Oportunidade
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: true
maturity: adjudicated_gap_validation
depends_on:
  - GKR-UXA-102-V5-AUTHORITY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-UX-PERSON-INTERNAL-OPPORTUNITY-APPLICATION-CONTRACT-001
  - GKR-UX-ORG-OPPORTUNITY-APPLICATIONS-CONTRACT-001
related:
  - GKR-UX-OPPORTUNITY-POST-SUBMIT-BILATERAL-CONTINUITY-001
  - GKR-UX-PUBLISHER-APPLICATION-CONTRACT-001
---

# G4 — Validação do Processo Interno de Oportunidade

## 1. Finalidade

Este ato aprofunda a família G4 registrada após a UXA-102/V5, com foco em:

- TRN-212 — PER-203 → PER-204;
- TRN-214 — ORG-003 → ORG-008.

O objetivo é decidir se as autoridades correntes sustentam promoção de maturidade ou somente refinamento das lacunas.

## 2. Resultado executivo

```text
TRN-212
→ CONTRACTED / UNCHANGED

TRN-214
→ CONTRACTED / UNCHANGED

DEDICATED RETURN IDS
→ NONE

MATURITY PROMOTIONS
→ 0
```

## 3. TRN-212 — PER-203 → PER-204

Estado preservado: **contracted**.

`TRN-212` formaliza a entrada consciente da Pessoa no processo interno de manifestação de interesse ou inscrição.

A autoridade corrente já exige que:

- a oportunidade suporte processo interno legítimo;
- a Pessoa escolha prosseguir conscientemente;
- finalidade, publicador e recorte autorizado de dados sejam preservados;
- entrar no processo não crie elegibilidade, seleção, participação ou resultado;
- retorno contextual a `PER-203` permaneça disponível quando legítimo;
- o retorno não receba ID próprio por mera simetria.

O contrato de `PER-204` permanece `draft / functional_contract_candidate`; portanto, não existe base para promover `TRN-212`.

## 4. TRN-214 — ORG-003 → ORG-008

Estado preservado: **contracted**.

`TRN-214` representa acesso institucional contextual da oportunidade ativa à gestão de manifestações/inscrições.

Esse handoff:

```text
ABRIR GESTÃO
≠ CRIAR OBJETO
≠ CONFIRMAR RECEBIMENTO
≠ ALTERAR ESTADO DA OPORTUNIDADE
```

`ORG-008` começa somente quando existe responsabilidade institucional própria sobre objetos bilaterais legitimamente recebidos.

O acesso contextual a partir de `ORG-003` não concede autoridade sobre a Pessoa, não amplia dados e não cria inscrição por navegação.

O contrato de `ORG-008` permanece `draft / functional_contract_candidate`; portanto, `TRN-214` permanece contratada.

## 5. Retornos contextuais

As autoridades correntes já registram:

```text
PER-204 → PER-203
ORG-008 → ORG-003
```

como retornos funcionais contextuais.

Eles não recebem novos `GKR-TRN-*` porque:

- não existe mudança de responsabilidade que exija identidade própria comprovada;
- retorno não cria nem altera objeto bilateral;
- navegação não equivale a ação material;
- simetria visual não é critério de adjudicação.

## 6. Falha, indeterminação e idempotência

Essas dimensões deixam de ser lacuna genérica em G4.

As autoridades correntes já cobrem:

- falha antes do envio;
- falha durante processamento;
- recebimento sem confirmação suficiente;
- estado indeterminado;
- retry sem criar objeto bilateral duplicado;
- revalidação antes de repetir efeito incerto;
- autoridade revogada;
- estado canônico acima de interface stale.

## 7. Relação com TRN-213/215/216

G4 não reabre as continuidades bilaterais já contratadas:

```text
TRN-213
→ PER-204 → ORG-008
→ ENVIO INICIAL CONSCIENTE

TRN-215
→ ORG-008 → PER-204
→ COMUNICAÇÃO / ATUALIZAÇÃO MATERIAL

TRN-216
→ PER-204 → ORG-008
→ RESPOSTA / ALTERAÇÃO MATERIAL PÓS-ENVIO
```

Essas transições preservam maturidade própria e não são promovidas por este ato.

## 8. O que continua aberto

### G4-A — TRN-212

Falta validação ponta a ponta da entrada consciente do Detalhe da Oportunidade para a responsabilidade interna `PER-204`.

### G4-B — TRN-214

Falta validação ponta a ponta do acesso institucional contextual `ORG-003 → ORG-008`.

### G4-C — maturidade das autoridades

`PER-204` e `ORG-008` possuem identidades adjudicadas, mas seus contratos funcionais de consumo ainda permanecem candidatos.

### G4-D — implementação

Persistência, confirmação técnica de recebimento, storage, locking, delivery e implementação permanecem fora deste ato.

## 9. Não inferências

```text
OPEN INTERNAL PROCESS
≠ APPLICATION CREATED

OPEN ORG-008
≠ RECEIPT CONFIRMED

RETURN
≠ NEW TRANSITION ID

SAME OBJECT
≠ SHARED UNRESTRICTED DATA

SUBMISSION
≠ ELIGIBILITY
≠ SELECTION
≠ PARTICIPATION
≠ RESULT
```

## 10. Guardrails

Este ato não:

- promove transição;
- cria retorno dedicado;
- cria nova superfície;
- cria novo `PER-ID` ou `ORG-ID`;
- cria score/ranking;
- define seleção automática;
- define persistência técnica;
- libera protótipo;
- libera Product Engineering.

## 11. Estado

```text
G4 VALIDATION
→ COMPLETE

TRN-212
TRN-214
→ CONTRACTED / UNCHANGED

MATURITY PROMOTIONS
→ 0

PRODUCT ENGINEERING
→ NOT RELEASED
```
