---
id: GKR-TRADEMARK-GRU-SCENARIO-PREFLIGHT-001
title: GRU Scenario Confirmation Preflight — Assinaturas Institucionais Guivos
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-10-03
normative: true
maturity: operational_preflight_confirmed
depends_on:
  - GKR-TRADEMARK-HUMAN-FILING-AUTHORIZATION-001
  - GKR-TRADEMARK-BRAZIL-SIGNATURE-FILING-AUTH-001
related:
  - GKR-TRADEMARK-FILING-SCOPE-001
---

# GRU Scenario Confirmation Preflight — Assinaturas Institucionais Guivos

## 1. Finalidade

Registrar a revalidação pública corrente do cenário de emissão de GRU para os quatro pedidos brasileiros das assinaturas institucionais da Guivos, sem declarar emissão, pagamento ou protocolo.

## 2. Baseline oficial revalidada

A Tabela de Retribuições vigente do INPI preserva, para pedido de registro de marca:

| Código | Serviço | Valor integral por classe | Valor com desconto elegível |
|---|---|---:|---:|
| 389 | pedido com especificação pré-aprovada | R$ 880,00 | R$ 440,00 |
| 394 | pedido com especificação de livre preenchimento | R$ 1.720,00 | R$ 860,00 |

Para quatro pedidos no código 389:

```text
SEM DESCONTO
→ 4 × R$ 880,00
→ R$ 3.520,00

COM DESCONTO DE 50%
→ 4 × R$ 440,00
→ R$ 1.760,00
```

## 3. Elegibilidade a desconto

O INPI prevê desconto de até 50% em serviços elegíveis para microempresas, MEI e empresas de pequeno porte, entre outros grupos previstos.

O GKR possui indicação pública secundária de porte `MICRO EMPRESA` para `GUIVOS LTDA`, mas o cenário com desconto somente será tratado como operacionalmente confirmado quando o cadastro/GRU do INPI reconhecer a elegibilidade no momento da emissão.

```text
PUBLIC INDICATION OF MICROEMPRESA
≠ DISCOUNT CONFIRMED IN GRU
```

## 4. Rota 389

A rota preferida permanece `389` somente se todos os itens necessários estiverem disponíveis na lista pré-aprovada do e-Marcas no momento da execução.

Para classe 42, a especificação-base autorizada permanece:

- Software como serviço [SaaS];
- Plataforma como serviço [PaaS].

AIaaS continua item condicional e somente pode ser incluído com evidência factual compatível.

Se qualquer item necessário não estiver disponível como pré-aprovado:

```text
389
→ NÃO PRESUMIR

REVALIDAR
→ ESPECIFICAÇÃO
→ CÓDIGO
→ CUSTO
→ AUTORIZAÇÃO SE O CENÁRIO MUDAR
```

## 5. Estado operacional

```text
PUBLIC PRICE BASELINE
→ CONFIRMED

PREFERRED ROUTE
→ 389 / CONDITIONAL ON PRE-APPROVED ITEMS

DISCOUNT SCENARIO
→ NOT YET CONFIRMED IN INPI SYSTEM

GRU_issued = false
GRU_paid = false
signature_filed = false
```

## 6. Próximo gate

O próximo gate permanece execução autenticada no sistema do INPI para:

1. confirmar titular/cadastro;
2. confirmar elegibilidade de desconto;
3. confirmar disponibilidade das especificações pré-aprovadas;
4. confirmar exclusão ou inclusão legítima de AIaaS;
5. somente então emitir as GRUs.

## 7. Não equivalências

```text
PUBLIC TARIFF VERIFIED
≠ GRU SCENARIO CONFIRMED

MICROEMPRESA INDICATION
≠ DISCOUNT APPLIED

CODE 389 PREFERRED
≠ CODE 389 EXECUTABLE WITHOUT ITEM CHECK

GRU SCENARIO CONFIRMED
≠ GRU PAID
```

## 8. Estado

```text
GRU SCENARIO PREFLIGHT
→ COMPLETE

PUBLIC BASELINE
→ CONFIRMED

OPERATIONAL SCENARIO
→ PENDING AUTHENTICATED INPI CHECK

NEXT GATE
→ AUTHENTICATED GRU ISSUANCE
```
