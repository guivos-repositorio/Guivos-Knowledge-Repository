---
id: GKR-TRADEMARK-AUTHENTICATED-GRU-ISSUANCE-HANDOFF-001
title: Authenticated GRU Issuance — Handoff Operacional das Assinaturas Guivos
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-10-03
normative: true
maturity: execution_handoff_ready
depends_on:
  - GKR-TRADEMARK-HUMAN-FILING-AUTHORIZATION-001
  - GKR-TRADEMARK-GRU-SCENARIO-PREFLIGHT-001
  - GKR-TRADEMARK-BRAZIL-SIGNATURE-FILING-AUTH-001
related:
  - GKR-TRADEMARK-FILING-SCOPE-001
---

# Authenticated GRU Issuance — Handoff Operacional das Assinaturas Guivos

## 1. Finalidade

Preparar a execução autenticada no sistema do INPI para emissão das GRUs dos quatro pedidos já autorizados, sem declarar guia emitida antes da existência do número real de cada GRU.

## 2. Condição de execução

Esta etapa depende de sessão autenticada do titular ou procurador legitimamente autorizado no e-INPI/GRU.

```text
EXECUTION HANDOFF
→ READY

AUTHENTICATED INPI SESSION
→ REQUIRED

GRU_issued
→ false
```

## 3. Quatro emissões esperadas

| # | Sinal | Classe | Rota preferida | Classes na GRU | Estado |
|---:|---|---:|---|---:|---|
| 1 | `Possibility, lived.` | 35 | 389 | 1 | PENDING_AUTHENTICATED_ISSUANCE |
| 2 | `Possibility, lived.` | 42 | 389 | 1 | PENDING_AUTHENTICATED_ISSUANCE_WITH_ITEM_GATE |
| 3 | `Possibilidade, vivida.` | 35 | 389 | 1 | PENDING_AUTHENTICATED_ISSUANCE |
| 4 | `Possibilidade, vivida.` | 42 | 389 | 1 | PENDING_AUTHENTICATED_ISSUANCE_WITH_ITEM_GATE |

## 4. Checklist por emissão

Antes de gerar cada GRU, confirmar na sessão autenticada:

1. titular exibido como `GUIVOS LTDA`;
2. CNPJ correspondente ao titular já reconciliado no GKR;
3. tipo de serviço `Marcas`;
4. código `389`, somente se a especificação necessária estiver disponível como pré-aprovada;
5. total de classes = `1`;
6. elegibilidade ou não ao desconto exibida pelo sistema;
7. valor efetivo da guia;
8. número real da GRU gerada.

Para as classes 42, confirmar também:

9. SaaS disponível como item pré-aprovado;
10. PaaS disponível como item pré-aprovado;
11. AIaaS somente se houver evidência factual compatível; sem evidência, omitir.

## 5. Regra de rota

```text
SE ITENS NECESSÁRIOS ESTÃO DISPONÍVEIS COMO PRÉ-APROVADOS
→ USAR 389

SE ITEM NECESSÁRIO NÃO ESTÁ DISPONÍVEL
→ NÃO MIGRAR AUTOMATICAMENTE PARA 394
→ REVALIDAR ESCOPO + CUSTO
→ NOVA AUTORIZAÇÃO ANTES DE PAGAR
```

## 6. Regra financeira

Valores públicos revalidados para código 389:

```text
SEM DESCONTO
→ R$ 880,00 por classe

COM DESCONTO ELEGÍVEL DE 50%
→ R$ 440,00 por classe
```

O valor operacional somente se torna canônico quando exibido na GRU real.

```text
PUBLIC PRICE
≠ EXECUTED GRU VALUE
```

## 7. Pagamento

A emissão não equivale a pagamento.

```text
GRU_issued = true
≠ GRU_paid = true
```

Após emissão, preservar o número de cada GRU e somente registrar `GRU_paid=true` depois de evidência de pagamento efetivo.

## 8. Protocolo

O pedido no e-Marcas somente deve ser iniciado com a GRU correspondente já paga.

```text
GRU PAID
→ ENABLES FILING

GRU ISSUED
≠ APPLICATION FILED
```

## 9. Evidências mínimas a retornar ao GKR

Para cada uma das quatro guias:

- número da GRU;
- sinal correspondente;
- classe;
- código do serviço;
- valor emitido;
- desconto aplicado ou não;
- titular exibido;
- data de emissão;
- comprovante de pagamento, quando ocorrer.

## 10. Estado

```text
AUTHENTICATED GRU ISSUANCE HANDOFF
→ READY

GRU_issued = false
GRU_paid = false
signature_filed = false

NEXT MATERIAL EVENT
→ FIRST REAL GRU NUMBER RECEIVED
```
