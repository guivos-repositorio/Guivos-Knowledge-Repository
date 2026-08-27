---
id: RP-002-PILOT-RESEARCH-MAILBOX-TEST-001
title: Piloto — Evidência do T-RESEARCH-001 da Mailbox de Research
status: active
version: 0.1.0
owner: Guivos Research
last_updated: 2026-08-27
normative: false
parent: RP-002
maturity: operational_test_in_progress
related:
  - RP-002-PILOT-RESEARCH-MAILBOX-DEC-001
  - RP-002-PILOT-STACK-DEC-001
  - RP-002-PILOT-OP-001
---

# Piloto — Evidência do T-RESEARCH-001 da Mailbox de Research

## 1. Finalidade

Este artefato registra a execução controlada do teste sintético `T-RESEARCH-001` da mailbox institucional de Research definida para o primeiro Dry Run Real `N=1` do `RP-002`.

O teste existe para produzir evidência material sobre:

- provisionamento funcional da mailbox;
- recebimento externo;
- resposta externa;
- operação pela função Guivos Research;
- segregação funcional mínima.

Este documento não libera participante real e não altera por inferência qualquer gate jurídico, de privacidade ou de dados.

## 2. Mailbox sob teste

```text
ADDRESS
→ research@guivos.com

FUNCTION
→ Guivos Research / RP-002

TARGET OPERATOR
→ Hostinger Mail

TEST ID
→ T-RESEARCH-001
```

O endereço foi previamente aprovado por `RP-002-PILOT-RESEARCH-MAILBOX-DEC-001`.

## 3. Fato operacional informado

Em 2026-08-27 foi informado que:

```text
research@guivos.com
→ CREATED
```

Esse fato é registrado como evidência operacional declarada de provisionamento.

Entretanto, o padrão de evidência do piloto exige separar:

```text
DECLARED CREATED
≠
END-TO-END VERIFIED
```

Portanto, a criação declarada não promove sozinha `A1` para `PASS`.

## 4. Verificação no operador conectado

Foi consultada a integração autenticada disponível do Hostinger Mail por meio da descoberta da conta corrente.

Resultado observado:

```text
MAILBOXES ENUMERATED BY CURRENT API CONNECTION
→ privacidade@guivos.com

research@guivos.com
→ NOT ENUMERATED BY CURRENT CONNECTION
```

Interpretação controlada:

- isso não prova inexistência de `research@guivos.com`;
- isso prova apenas que a conexão atual do operador não oferece visibilidade independente dessa nova mailbox;
- a evidência do usuário sobre criação permanece válida como informação declarada;
- a comprovação operacional deve ser concluída pelo fluxo ponta a ponta.

Nenhum identificador interno de recurso, token ou credencial do operador é registrado neste artefato.

## 5. Envio externo executado

Foi enviado um e-mail sintético de origem externa para:

```text
TO
→ research@guivos.com

SUBJECT
→ T-RESEARCH-001 — teste controlado de recebimento

TEST ID
→ T-RESEARCH-001

SENT AT
→ 2026-08-27T23:39:41Z
```

Conteúdo material do teste:

- identifica explicitamente o teste sintético;
- informa que o objetivo é verificar recebimento da mailbox;
- declara que nenhum dado de participante real está envolvido.

Nenhum dado pessoal de participante foi usado.

## 6. Estado de entrega observado

O sistema externo aceitou o envio e registrou a mensagem como enviada.

Em verificações posteriores imediatas:

```text
BOUNCE ASSOCIATED WITH research@guivos.com
→ NOT OBSERVED
```

Isso constitui evidência positiva de que não houve rejeição imediata conhecida pelo remetente.

Mas a ausência de bounce não equivale a comprovação de recebimento na mailbox.

Logo:

```text
EXTERNAL SEND
→ EXECUTED

IMMEDIATE REJECTION
→ NOT OBSERVED

INBOX RECEIPT
→ NOT YET INDEPENDENTLY CONFIRMED
```

## 7. Separação de evidências antigas

Existe evidência histórica de falha de entrega relativa a outro teste e a outra mailbox de privacidade.

Essa evidência:

```text
→ NÃO pertence ao T-RESEARCH-001
→ NÃO deve ser usada para inferir falha de research@guivos.com
```

O `T-RESEARCH-001` deve ser avaliado somente por suas próprias evidências.

## 8. Estado dos gates A1

### A1-1 — Address Decision

```text
PASS
```

Base:

- `research@guivos.com` já aprovado como endereço primário.

### A1-2 — Provisioning

Evidência atual:

- criação informada como concluída;
- a conexão atual do Hostinger Mail ainda não enumera essa mailbox;
- teste externo já iniciado.

Estado:

```text
PARTIAL / VERIFICATION PENDING
```

Não promover para `PASS` até existir evidência funcional suficiente de operação da caixa.

### A1-3 — Inbound

Evidência atual:

- mensagem externa enviada;
- nenhuma rejeição imediata observada;
- recebimento dentro da mailbox ainda não confirmado.

Estado:

```text
IN PROGRESS
```

### A1-4 — Outbound / Reply

Critério ainda não executado:

- responder ao `T-RESEARCH-001` a partir de `research@guivos.com`;
- confirmar que a resposta chega ao remetente externo.

Estado:

```text
HOLD
```

### A1-5 — Functional Owner

A operação real pela função Guivos Research ainda precisa ser comprovada sem expor credenciais.

Estado:

```text
HOLD
```

### A1-6 — Functional Segregation

A segregação em relação aos canais de Privacy ainda precisa ser comprovada operacionalmente.

Estado:

```text
HOLD
```

## 9. Próximo passo exato do T-RESEARCH-001

A mensagem já foi enviada.

O próximo ato material é:

```text
1. CONFIRMAR QUE T-RESEARCH-001 CHEGOU A research@guivos.com
2. RESPONDER PELA PRÓPRIA research@guivos.com
3. MANTER O MESMO THREAD / SUBJECT QUANDO POSSÍVEL
4. CONFIRMAR A RESPOSTA NO REMETENTE EXTERNO
```

A resposta pode ser mínima e sintética, por exemplo:

```text
T-RESEARCH-001 — recebimento confirmado.
Resposta sintética para validação de outbound.
Nenhum dado de participante real envolvido.
```

## 10. Critério de fechamento

O teste somente poderá ser fechado como `PASS` quando houver evidência suficiente do ciclo:

```text
EXTERNAL SENDER
→ research@guivos.com
→ INBOUND CONFIRMED
→ ACCESS BY GUIVOS RESEARCH
→ REPLY FROM research@guivos.com
→ EXTERNAL SENDER RECEIVES REPLY
```

Depois disso, avaliar separadamente:

- owner funcional;
- segregação funcional;
- necessidade de qualquer ajuste no operador conectado.

## 11. Gates preservados

Este teste não altera automaticamente:

```text
P2C
→ HOLD

P3-C
→ HOLD

P3-D
→ HOLD

P4
→ HOLD

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```

## 12. Estado atual

```text
T-RESEARCH-001
→ IN PROGRESS

A1-1 ADDRESS DECISION
→ PASS

A1-2 PROVISIONING
→ PARTIAL / VERIFICATION PENDING

A1-3 INBOUND
→ IN PROGRESS

A1-4 OUTBOUND / REPLY
→ HOLD

A1-5 FUNCTIONAL OWNER
→ HOLD

A1-6 SEGREGATION
→ HOLD

A1 OVERALL
→ PARTIAL / HOLD

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```
