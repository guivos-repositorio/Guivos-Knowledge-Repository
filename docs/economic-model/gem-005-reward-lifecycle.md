---
id: GEM-005-REWARD-LIFECYCLE-001
title: Ciclo de Vida de Recompensas
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-005
---

# Ciclo de Vida de Recompensas

## 1. Objetivo

Definir estados e transições conceituais para elegibilidade, verificação, emissão, disponibilidade, reserva, resgate, expiração, reversão e disputa.

## 2. Fluxo principal

```text
candidate
→ eligible
→ pending_verification
→ approved
→ issued
→ available
→ reserved
→ redeemed
```

## 3. Estados alternativos

```text
rejected
cancelled
expired
reversed
disputed
suspended
```

## 4. Definições

### Candidate

Hipótese ou ocorrência registrada sem condição suficiente para criar direito.

### Eligible

Condições preliminares atendidas, ainda sem validação final.

### Pending verification

Evento aguarda evidência, confirmação ou análise.

### Approved

Autoridade competente confirmou o evento e autorizou emissão futura.

### Issued

Unidade ou direito foi criado no registro econômico correspondente.

### Available

Recompensa pode ser utilizada dentro das regras vigentes.

### Reserved

Saldo ou benefício está temporariamente indisponível durante processo de resgate.

### Redeemed

Benefício foi utilizado, entregue ou confirmado conforme regra aplicável.

### Rejected

Evento não atendeu aos critérios.

### Cancelled

Evento ou programa foi encerrado antes da constituição final do direito.

### Expired

Prazo previamente informado terminou.

### Reversed

Emissão ou resgate anterior foi cancelado por regra legítima e registrada.

### Disputed

Decisão está sob contestação.

### Suspended

Movimentação está temporariamente bloqueada por risco, incidente ou investigação.

## 5. Transições admissíveis

| Origem | Destino | Condição mínima |
|---|---|---|
| candidate | eligible | critérios preliminares atendidos |
| eligible | pending_verification | evidência requerida |
| eligible | approved | verificação simples suficiente |
| pending_verification | approved | evidência aceita |
| pending_verification | rejected | evidência insuficiente ou inválida |
| approved | issued | cobertura e autoridade confirmadas |
| issued | available | condição de disponibilidade atendida |
| available | reserved | resgate iniciado |
| reserved | redeemed | benefício confirmado |
| reserved | available | reserva liberada |
| available | expired | validade encerrada |
| issued/available | reversed | erro, duplicidade ou evento desfeito |
| qualquer material | disputed | contestação válida |
| qualquer ativo | suspended | risco ou incidente relevante |

## 6. Condições anteriores à emissão

Antes de `issued`, deverão existir:

- programa identificado;
- camada econômica correta;
- evento elegível;
- evidência suficiente;
- beneficiário;
- fonte de financiamento confirmada;
- responsabilidade econômica;
- regra de validade;
- regra de reversão;
- owner;
- trilha de decisão.

## 7. Registro mínimo de emissão

```yaml
reward_issue_id: string
program_id: string
reward_type: string
beneficiary_id: string
eligible_event_id: string
evidence_level: string
funding_source_id: string | null
economic_responsibility: string | null
quantity: number | null
monetary_value_defined: false
issued_at: datetime
available_at: datetime | null
expires_at: datetime | null
status: string
reversal_rule: string
owner: string
```

## 8. Reserva

A reserva deverá:

- impedir duplo uso;
- possuir prazo;
- indicar benefício;
- ser reversível em falha;
- não ser tratada como resgate concluído;
- liberar saldo quando a entrega não ocorrer;
- manter trilha de auditoria.

## 9. Resgate

O estado `redeemed` somente deverá ocorrer após confirmação proporcional da entrega ou utilização.

Dependendo do benefício futuro, a confirmação poderá vir de:

- participante;
- parceiro;
- sistema;
- documento;
- múltiplas fontes.

## 10. Expiração

A expiração deverá:

- possuir fundamento;
- ser informada antes da emissão;
- ser visível no saldo;
- ser comunicada de forma proporcional;
- preservar histórico;
- tratar indisponibilidade do benefício;
- permitir contestação de erro.

## 11. Reversão

Poderá ocorrer por:

- erro;
- duplicidade;
- fraude comprovada;
- cancelamento do evento gerador;
- devolução ou chargeback;
- evidência inválida;
- violação de regra previamente informada.

Não deverá ocorrer por decisão retroativa arbitrária ou por fato sem relação com a emissão.

## 12. Disputa

Durante disputa:

- saldo afetado poderá ser suspenso proporcionalmente;
- saldo não relacionado permanecerá disponível quando seguro;
- razão será informada;
- evidência poderá ser apresentada;
- revisão humana será aplicada quando necessária;
- resultado e autoridade serão registrados.

## 13. Encerramento de programa

Deverá tratar:

- novas emissões;
- eventos pendentes;
- saldos emitidos;
- reservas;
- resgates em curso;
- benefícios já adquiridos;
- expiração;
- comunicação;
- cobertura residual;
- histórico.

## 14. Fora do escopo

- prazos definitivos;
- arquitetura de ledger;
- consistência transacional técnica;
- APIs;
- interfaces;
- operação.
