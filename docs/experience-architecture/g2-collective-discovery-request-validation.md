---
id: GKR-UX-G2-COLLECTIVE-DISCOVERY-REQUEST-VALIDATION-001
title: G2 — Validação de Descoberta e Solicitação de Coletivo
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: true
maturity: adjudicated_gap_validation
depends_on:
  - GKR-UXA-102-V5-AUTHORITY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-UX-PER101-MASTER-001
  - GKR-UX-PER102-MASTER-001
  - GKR-UX-PER103-MASTER-001
  - GKR-UX-PER104-MASTER-001
  - GKR-UX-PER105-MASTER-001
  - UXA-056
related:
  - GKR-UX-COL-REQUEST-MANAGEMENT-MASTER-001
  - GKR-UX-COL-PARTICIPANTS-LINKS-MASTER-001
  - UXA-089
---

# G2 — Validação de Descoberta e Solicitação de Coletivo

## 1. Finalidade

Este ato aprofunda a família G2 registrada após a UXA-102/V5:

```text
TRN-101
TRN-102
TRN-103
TRN-104
TRN-114
```

O objetivo é verificar se as autoridades correntes sustentam promoção de maturidade ou apenas refinamento de lacunas.

## 2. Resultado executivo

```text
TRN-101
→ LOCALLY VALIDATED / UNCHANGED

TRN-102
→ PARTIAL / UNCHANGED

TRN-103
→ PARTIAL / UNCHANGED

TRN-104
→ PARTIAL / UNCHANGED

TRN-114
→ CONTRACTED / UNCHANGED

MATURITY PROMOTIONS
→ 0
```

A ausência de promoção é uma decisão adjudicada, não falta de análise.

## 3. TRN-101 — PER-101 → PER-102

Estado preservado: **localmente validada**.

Os Masters correntes já definem:

- busca e exploração em `PER-101`;
- critérios revisáveis;
- ausência de vínculo por simples descoberta;
- handoff para resultados;
- preservação de contexto necessário;
- responsabilidade de carregamento/erro/ausência em `PER-102`.

`PER-101` e `PER-102` afirmam explicitamente que `TRN-101` permanece localmente validada.

Nenhuma promoção adicional é cabível.

## 4. TRN-102 — PER-102 → PER-103

Estado preservado: **partial**.

`PER-102` e `PER-103` já governam:

- seleção consciente de resultado;
- identidade lógica do Coletivo;
- contexto mínimo para retorno;
- não criação de vínculo;
- proteção de contexto pessoal;
- retorno sem mutação;
- falha técnica sem fabricar inexistência do Coletivo.

Porém, ambos preservam expressamente:

```text
TRN-102
→ PARTIAL
```

Logo, este ato não pode promover a transição sem contrariar a autoridade de superfície vigente.

## 5. TRN-103 — PER-103 → PER-104

Estado preservado: **partial**.

A continuidade já distingue corretamente:

```text
ABRIR REVISÃO
≠ ENVIAR SOLICITAÇÃO
```

`PER-103` exige avanço consciente e `PER-104` governa revisão, regras, dados, permissões, cancelamento e confirmação.

Entretanto, os dois Masters preservam explicitamente `TRN-103` como partial.

A lacuna é, portanto, de validação ponta a ponta da continuidade, não de semântica básica ausente.

## 6. TRN-104 — PER-104 → PER-105

Estado preservado: **partial**.

A fonte corrente já cobre:

- revisão antes da confirmação;
- cancelamento antes do envio;
- confirmação afirmativa;
- envio ≠ aprovação;
- confirmação em processamento;
- não apresentar sucesso antes de confirmação legítima;
- estado material incerto → revalidação antes de repetir;
- mesma solicitação lógica em `PER-105`;
- consulta de `PER-105` sem alterar fila, prioridade, decisão ou vínculo.

Mesmo assim, `PER-104` e `PER-105` declaram explicitamente:

```text
TRN-104
→ PARTIAL
```

Portanto, este ato preserva a maturidade.

## 7. TRN-114 — COL-003 → COL-004

Estado preservado: **contracted**.

A finalidade está semanticamente definida:

```text
SOLICITAÇÃO APROVADA
→ MESMO VÍNCULO
→ NOVA RESPONSABILIDADE OPERACIONAL
```

O handoff não deve:

- repetir aprovação;
- criar novo vínculo por navegação;
- tratar interface otimista como persistência técnica;
- confundir aprovação com vínculo técnico confirmado;
- duplicar o efeito de `TRN-108`.

Porém, os Masters de `COL-003` e `COL-004` permanecem:

```text
status: draft
maturity: functional_contract_candidate
```

e registram `TRN-114` como contratada.

Logo, não há base para promoção.

## 8. O que G2 efetivamente fecha

G2 fecha a dúvida sobre **falha/retorno/idempotência** como lacuna genérica.

Essas dimensões já possuem cobertura suficiente no corpus corrente:

- erro ≠ ausência legítima de resultado;
- seleção ≠ vínculo;
- abrir revisão ≠ enviar;
- envio ≠ aprovação;
- aprovação ≠ clique posterior;
- retry ≠ solicitação duplicada;
- resultado indeterminado exige reconsulta;
- retorno não altera fila, prioridade ou vínculo;
- estado canônico prevalece sobre interface stale.

## 9. O que continua aberto

### G2-A — TRN-102

Falta validação ponta a ponta entre resultado selecionado e Perfil Público, apesar de origem/destino já estarem semanticamente governados.

### G2-B — TRN-103

Falta validação ponta a ponta do handoff Perfil Público → Revisão e Solicitação.

### G2-C — TRN-104

Falta fechamento ponta a ponta do envio confirmado até o estado pendente, apesar de processamento/indeterminação/idempotência já estarem governados localmente.

### G2-D — TRN-114

Falta maturidade própria de `COL-003/004` e comprovação de persistência/materialização técnica do mesmo vínculo.

## 10. Não inferências

```text
SEMANTIC COVERAGE
≠ LOCAL VALIDATION AUTOMATIC

LOCAL CONTRACT
≠ END-TO-END VALIDATION

APPROVAL
≠ TECHNICAL LINK PERSISTENCE

PUBLIC PROFILE
≠ PARTICIPATION

REQUEST SENT
≠ APPROVED

OPEN LINK MANAGEMENT
≠ NEW LINK
```

## 11. Guardrails

Este ato não:

- promove nenhuma transição;
- cria nova superfície;
- cria nova transição;
- cria convite genérico Coletivo → Pessoa;
- cria inclusão unilateral;
- cria score/ranking;
- implementa fila;
- implementa persistência de vínculo;
- libera protótipo;
- libera Product Engineering.

## 12. Estado

```text
G2 VALIDATION
→ COMPLETE

MATURITY PROMOTIONS
→ 0

TRN-101
→ LOCALLY VALIDATED

TRN-102/103/104
→ PARTIAL

TRN-114
→ CONTRACTED

PRODUCT ENGINEERING
→ NOT RELEASED
```
