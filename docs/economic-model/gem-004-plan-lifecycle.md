---
id: GEM-004-PLAN-LIFECYCLE-001
title: Ciclo de Vida Conceitual dos Planos
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-004
---

# Ciclo de Vida Conceitual dos Planos

## 1. Objetivo

Definir estados e transições conceituais para ativação, trial, renovação, upgrade, downgrade, falha de pagamento, tolerância, cancelamento, expiração e encerramento, sem especificar sistema, cobrança ou contrato.

## 2. Estados

- `eligible`;
- `pending_activation`;
- `active_free`;
- `active_trial`;
- `active_paid`;
- `active_funded`;
- `change_scheduled`;
- `payment_issue`;
- `grace_period`;
- `paid_extensions_restricted`;
- `downgraded_to_free`;
- `cancelled`;
- `expired`;
- `suspended`;
- `terminated`.

## 3. Sequências de referência

### Ativação paga

```text
eligible
→ pending_activation
→ active_paid
```

### Trial

```text
eligible
→ active_trial
→ active_free | active_paid | cancelled
```

### Falha de pagamento

```text
active_paid
→ payment_issue
→ grace_period
→ paid_extensions_restricted
→ downgraded_to_free
```

### Cancelamento

```text
active_paid | active_funded
→ cancellation_requested
→ change_scheduled
→ downgraded_to_free | terminated
```

## 4. Ativação

A ativação futura deverá registrar:

- arquétipo;
- beneficiário;
- pagador ou financiador;
- capacidades incluídas;
- limites;
- início;
- renovação;
- dados e acessos;
- consentimento aplicável;
- canal de cancelamento.

## 5. Trial e acesso temporário

Deverão ser informados:

- capacidades;
- duração;
- data de encerramento;
- conversão automática ou não;
- condição futura de pagamento;
- forma de cancelamento;
- retorno ao gratuito;
- dados utilizados.

Conversão automática exigirá consentimento explícito, data conhecida, comunicação adequada e cancelamento simples.

## 6. Renovação

Deverá preservar:

- clareza sobre recorrência;
- período;
- alterações materiais;
- forma de cancelamento;
- responsabilidade do pagador;
- ausência de surpresa deliberada;
- registro da continuidade.

## 7. Upgrade

A transição deverá:

1. apresentar capacidades adicionais;
2. explicar limites e condições;
3. identificar renovação;
4. informar dados adicionais;
5. indicar início da vigência;
6. permitir revisão antes da confirmação;
7. evitar seleção automática indevida;
8. registrar consentimento;
9. permitir cancelamento;
10. não usar urgência artificial.

## 8. Downgrade

Deverá preservar:

- baseline gratuito;
- direitos sobre dados;
- exportação;
- correção;
- cancelamento;
- registros essenciais;
- evidências que não possam ser removidas legitimamente;
- informação sobre capacidades desativadas;
- transição proporcional.

O downgrade não poderá ser usado como punição.

## 9. Falha de pagamento e tolerância

Quando possível, a falha afetará primeiro ampliações pagas. Deverão permanecer:

- acesso gratuito;
- dados próprios;
- exportação;
- cancelamento;
- informação sobre a falha;
- suporte para correção;
- proteção contra exclusão imediata e irreversível.

## 10. Cancelamento

Deverá ser:

- acessível;
- compreensível;
- proporcional à contratação;
- confirmado;
- livre de obstáculos artificiais;
- separado de culpa, medo ou pressão;
- acompanhado de informação sobre o estado futuro.

## 11. Expiração e encerramento

Deverão definir:

- capacidades encerradas;
- dados preservados;
- acessos de terceiros removidos;
- período de retenção legítimo;
- retorno ao gratuito;
- possibilidade de exportação;
- forma de reativação futura;
- obrigações pendentes.

## 12. Suspensão

Poderá ocorrer por:

- fraude;
- incidente de segurança;
- uso incompatível;
- risco material;
- disputa;
- conflito de autoridade;
- ausência de elegibilidade;
- falha operacional crítica.

Suspensão deverá ser proporcional, informada e revisável quando possível.

## 13. Integridade das transições

1. estado anterior e novo estado serão rastreáveis;
2. direito essencial não será perdido silenciosamente;
3. dados não serão excluídos por simples falha de pagamento;
4. acesso de financiador será removido no término;
5. alteração não será retroativa sem base legítima;
6. erro de entitlement deverá ser corrigível;
7. transições deverão possuir evidência e contestação.

## 14. Fora do escopo

- eventos técnicos;
- ledger;
- billing;
- proration;
- calendário real;
- notificações de interface;
- integração de pagamento;
- implementação.
