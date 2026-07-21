---
id: GEM-003-REVENUE-EVENT-MODEL-001
title: Modelo de Eventos Econômicos de Receita
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-003
---

# Modelo de Eventos Econômicos de Receita

## 1. Objetivo

Definir eventos conceituais necessários para rastrear o ciclo econômico sem criar modelo contábil, fiscal, comercial ou técnico.

## 2. Sequência de referência

```text
entitlement
→ billing eligibility
→ billing
→ payment
→ settlement
→ recognition dependency
→ continuation, cancellation, dispute or reversal
```

A sequência poderá variar por família e não presume reconhecimento de receita.

## 3. Eventos

### Entitlement

Criação, alteração, suspensão ou encerramento do direito de acesso, recebimento ou utilização.

### Billing eligibility

Confirmação de que condições conceituais mínimas para futura cobrança foram atendidas.

### Billing

Geração de obrigação econômica ou documento de cobrança futuro.

### Payment

Transferência financeira ou confirmação de pagamento. Pagamento não prova entrega, realização, reconhecimento ou ausência de contestação.

### Settlement

Distribuição de valores entre Guivos, parceiros, fornecedores, profissionais, plataformas, causas ou outros recebedores legítimos.

### Recognition dependency

Conjunto de condições que deverá ser analisado futuramente para reconhecimento econômico ou contábil.

### Renewal

Continuidade de relação recorrente após período definido.

### Cancellation

Encerramento de relação recorrente ou de obrigação futura.

### Expiration

Término de direito, crédito, benefício ou capacidade contratada.

### Refund

Devolução total ou parcial de valor pago.

### Reversal

Anulação de evento econômico anterior.

### Chargeback ou dispute

Contestação iniciada por pagador, instituição financeira ou outro ator legítimo.

### Adjustment

Correção de quantidade, período, elegibilidade, responsabilidade ou valor futuro.

### Suspension

Bloqueio temporário de mecanismo por risco, fraude, falha, disputa, segurança ou governança.

### Termination

Encerramento definitivo da relação econômica ou do mecanismo.

## 4. Estados conceituais

- `not_eligible`;
- `eligible`;
- `pending`;
- `authorized`;
- `paid`;
- `partially_settled`;
- `settled`;
- `disputed`;
- `refunded`;
- `reversed`;
- `cancelled`;
- `expired`;
- `suspended`;
- `terminated`.

Esses estados não constituem especificação de software.

## 5. Regras de integridade

1. entitlement não equivale a cobrança;
2. cobrança não equivale a pagamento;
3. pagamento não equivale a receita reconhecida;
4. settlement deve separar receita, repasse e recurso vinculado;
5. reversão deve preservar rastreabilidade;
6. disputa não poderá ser ocultada;
7. cancelamento não poderá ser dificultado artificialmente;
8. refund deverá considerar valor recebido, valor repassado e responsabilidade;
9. evento econômico não poderá alterar evidência de valor;
10. falhas e exceções deverão ser registradas.

## 6. Evidências mínimas futuras

- evento originador;
- ator responsável;
- contraprestação;
- direito criado;
- período ou unidade;
- status;
- recebedores;
- repasses;
- contestação;
- correções e reversões;
- relação com fluxo de valor.

## 7. Fora do escopo

- plano de contas;
- regra fiscal;
- emissão de documento;
- gateway;
- adquirente;
- conciliação bancária;
- ledger técnico;
- reconhecimento conforme norma contábil;
- implementação.
