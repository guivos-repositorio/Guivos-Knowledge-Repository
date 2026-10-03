---
id: GKR-TRADEMARK-HUMAN-FILING-AUTHORIZATION-001
title: Human Filing Authorization — Assinaturas Institucionais Guivos — Brasil
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-10-03
normative: true
maturity: filing_authorized
depends_on:
  - GKR-TRADEMARK-BRAZIL-SIGNATURE-FILING-AUTH-001
  - GKR-TRADEMARK-SIGNATURE-FILING-DECISION-001
  - GKR-TRADEMARK-FILING-PREFLIGHT-001
related:
  - GKR-TRADEMARK-FILING-SCOPE-001
---

# Human Filing Authorization — Assinaturas Institucionais Guivos — Brasil

## 1. Finalidade

Registrar a autorização humana explícita para avançar do estado `READY_FOR_AUTHORIZATION` para a execução operacional de depósito das assinaturas institucionais da Guivos no Brasil.

Esta autorização cobre o avanço para protocolo e a assunção do gasto correspondente dentro da rota autorizada, mas a execução do pagamento permanece condicionada à confirmação prévia do cenário financeiro aplicável no sistema e do respectivo teto. Ela não declara GRU emitida, GRU paga, pedido depositado ou registro concedido.

## 2. Pedidos autorizados

| Pedido | Sinal | Classe | Apresentação | Estado |
|---:|---|---:|---|---|
| 1 | `Possibility, lived.` | 35 | Nominativa | AUTHORIZED_TO_FILE |
| 2 | `Possibility, lived.` | 42 | Nominativa | AUTHORIZED_TO_FILE_WITH_ITEM_GATE |
| 3 | `Possibilidade, vivida.` | 35 | Nominativa | AUTHORIZED_TO_FILE |
| 4 | `Possibilidade, vivida.` | 42 | Nominativa | AUTHORIZED_TO_FILE_WITH_ITEM_GATE |

## 3. Gate AIaaS

Para as classes 42:

```text
CLASSE 42
→ AUTHORIZED TO FILE

AIaaS
→ INCLUDE ONLY IF EVIDENCE OF EFFECTIVE COMPATIBLE ACTIVITY EXISTS
→ OTHERWISE OMIT
```

A ausência de evidência para AIaaS não cancela nem adia automaticamente o depósito da classe 42 com os itens já sustentados de SaaS/PaaS.

## 4. Estado de execução

```text
authorization_package_prepared = true
filing_authorized = true
GRU_issued = false
GRU_paid = false
signature_filed = false
signature_registered = false
```

## 5. Próximos atos operacionais

1. confirmar titularidade/cadastro vigente no e-INPI;
2. confirmar especificações finais de classe 35 e 42;
3. aplicar o gate AIaaS às classes 42;
4. confirmar no sistema o cenário financeiro efetivo e o teto aplicável;
5. emitir as GRUs correspondentes;
6. pagar as GRUs;
7. protocolar os quatro pedidos;
8. arquivar comprovantes e números de processo;
9. reconciliar o GKR com a evidência registral.

Cada ato externo deve ser registrado somente após evidência de execução.

## 6. Não equivalências

```text
FILING AUTHORIZED
≠ GRU ISSUED

GRU ISSUED
≠ GRU PAID

GRU PAID
≠ APPLICATION FILED

APPLICATION FILED
≠ REGISTRATION GRANTED
```

## 7. Limites

Esta autorização não:

- amplia o escopo para classes 9, 39, 41, 43 ou 45;
- autoriza lockup `GUIVOS + assinatura`;
- autoriza AIaaS sem evidência factual compatível;
- declara gasto executado antes do pagamento;
- declara protocolo antes da evidência do INPI;
- declara registro concedido.

## 8. Estado

```text
HUMAN FILING AUTHORIZATION
→ GRANTED

FOUR SIGNATURE APPLICATIONS
→ AUTHORIZED TO FILE

AIaaS
→ CONDITIONAL ITEM GATE PRESERVED

NEXT EXECUTION GATE
→ GRU SCENARIO CONFIRMATION + ISSUANCE
```
