---
id: RP-002-PILOT-RESEARCH-MAILBOX-TEST-001
title: Piloto — Evidência do T-RESEARCH-001 da Mailbox de Research
status: active
version: 1.0.0
owner: Guivos Research
last_updated: 2026-08-27
normative: false
parent: RP-002
maturity: operational_evidence_verified_partial
related:
  - RP-002-PILOT-RESEARCH-MAILBOX-DEC-001
  - RP-002-PILOT-STACK-DEC-001
  - RP-002-PILOT-OP-001
---

# Piloto — Evidência do T-RESEARCH-001 da Mailbox de Research

## 1. Finalidade

Este artefato registra a execução controlada e o resultado observado do teste sintético `T-RESEARCH-001` da mailbox institucional de Research definida para o primeiro Dry Run Real `N=1` do `RP-002`.

O teste não utilizou dados pessoais reais de participante e não libera, isoladamente, participante real ou qualquer gate jurídico, de privacidade ou de dados.

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

## 3. Fato operacional inicial

Em 2026-08-27 foi informado que `research@guivos.com` havia sido criada.

A conexão autenticada do Hostinger Mail disponível nesta sessão enumerava apenas a mailbox `privacidade@guivos.com`. Isso não demonstrava inexistência da mailbox de Research; apenas impedia comprovação direta pelo escopo daquela conexão.

Por isso, a validação foi concluída pelo fluxo externo ponta a ponta.

Nenhum identificador interno de recurso, token, senha ou credencial é registrado neste artefato.

## 4. Envio externo

Foi enviado um e-mail sintético de origem externa para `research@guivos.com` com assunto:

```text
T-RESEARCH-001 — teste controlado de recebimento
```

O conteúdo declarou explicitamente tratar-se de teste sintético e que nenhum dado de participante real estava envolvido.

O remetente externo registrou o envio e não observou rejeição imediata associada à mailbox.

## 5. Resultado observado

### 5.1 Provisionamento funcional

Posteriormente foram recebidas no remetente externo respostas provenientes da própria `research@guivos.com`, dentro da thread do `T-RESEARCH-001`.

Isso demonstra que a mailbox estava funcionalmente provisionada para o ciclo testado.

```text
A1-2 PROVISIONING
→ PASS
```

### 5.2 Recebimento externo

As respostas emitidas pela própria mailbox dentro da thread do teste demonstram que a mensagem externa original foi recebida e operacionalmente acessada.

```text
A1-3 INBOUND
→ PASS
```

### 5.3 Resposta externa

O Gmail usado como remetente externo recebeu duas respostas provenientes de `research@guivos.com` na thread do `T-RESEARCH-001`.

```text
A1-4 OUTBOUND / REPLY
→ PASS
```

## 6. Gates que permanecem abertos

### A1-5 — Functional Owner

O critério vigente exige comprovar que a função `Guivos Research / Pilot Owner` é quem consegue operar a mailbox, sem exposição de credenciais.

A evidência ponta a ponta comprova operação da mailbox, mas não identifica de forma suficiente a função operacional responsável.

```text
A1-5 FUNCTIONAL OWNER
→ HOLD
```

### A1-6 — Functional Segregation

O critério vigente exige comprovar cumulativamente que:

- a mailbox não redireciona por padrão para caixa pessoal incompatível;
- a finalidade de Research permanece distinguível dos canais de Privacy;
- não há uso de marketing ou vendas no teste.

O teste comprova uso exclusivamente sintético de Research e endereços funcionais distintos, mas não comprova ainda a ausência de redirecionamento padrão incompatível.

```text
A1-6 FUNCTIONAL SEGREGATION
→ HOLD
```

## 7. Estado de A1 após o T-RESEARCH-001

```text
A1-1 ADDRESS DECISION
→ PASS

A1-2 PROVISIONING
→ PASS

A1-3 INBOUND
→ PASS

A1-4 OUTBOUND / REPLY
→ PASS

A1-5 FUNCTIONAL OWNER
→ HOLD

A1-6 FUNCTIONAL SEGREGATION
→ HOLD

A1 OVERALL
→ PARTIAL / HOLD
```

## 8. Limites da evidência

Este resultado:

- comprova a operação básica ponta a ponta da mailbox de Research;
- não comprova por inferência owner funcional;
- não comprova por inferência segregação funcional completa;
- não promove `P3-C`, `P3-D` ou `P4`;
- não libera Participante 001;
- não libera o Dry Run Real.

## 9. Próximo ato material

Fechar `A1` exige somente os dois subgates restantes:

```text
A1-5 FUNCTIONAL OWNER
→ PROVAR

A1-6 FUNCTIONAL SEGREGATION
→ PROVAR
```

Até esse fechamento:

```text
PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```
