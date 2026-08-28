---
id: RP-002-PILOT-NOTICE-CONSENT-FLOW-DEC-001
title: Piloto — Decisão do Fluxo A2 Notice e Consentimento
status: active
version: 1.0.0
owner: Guivos Research
last_updated: 2026-08-27
normative: false
parent: RP-002
maturity: flow_target_approved_pre_execution
related:
  - RP-002-PILOT-DOC-CLOSE-001
  - RP-002-PILOT-NOTICE-CONSENT-001
  - RP-002-PILOT-RESEARCH-MAILBOX-DEC-001
  - RP-002-PILOT-DATA-LAW-001
  - RP-002-PILOT-CTRL-DEC-001
---

# Piloto — Decisão do Fluxo A2 Notice e Consentimento

## 1. Finalidade

Este documento define o fluxo-alvo documental de transparência e captura de consentimento para o primeiro Dry Run Real `N=1` do `RP-002`.

Ele não autoriza contato ou coleta com Pessoa real durante a fase documental.

```text
A2 DOCUMENTATION TARGET
→ DECIDED

A2 REAL FLOW
→ NOT EXECUTED

A2 OPERATIONAL STATUS
→ HOLD
```

## 2. Princípio

O fluxo deve produzir evidência simples de que a Pessoa recebeu uma versão identificável do Notice antes da coleta do núcleo de Research e manifestou decisão explícita.

```text
NO NOTICE
→ NO CONSENT

NO AFFIRMATIVE CONSENT
→ NO RESEARCH EPISODE

SILENCE / INACTION
→ NOT CONSENT
```

## 3. Canal-alvo

```text
SENDER
→ research@guivos.com

OPERATOR
→ Hostinger Mail

PURPOSE
→ research recruitment / notice / consent / scheduling / authorized follow-up
```

O canal de Research permanece separado dos canais de privacidade:

- `privacidade@guivos.com`;
- `privacy@guivos.com`.

## 4. Sequência documental

```text
1. MINIMUM RECRUITMENT CONTACT
2. ELIGIBILITY / 18+ MINIMUM GATE
3. SEND EXACT NOTICE VERSION
4. ALLOW QUESTIONS
5. REQUEST EXPLICIT AFFIRMATIVE MANIFESTATION
6. RECORD STATUS + VERSION + TIMESTAMP
7. IF GIVEN → MAY PROCEED ONLY AFTER ALL OTHER RELEASE GATES
8. IF NOT GIVEN → CLOSE WITHOUT RESEARCH EPISODE
9. IF WITHDRAWN → STOP NEW CONSENT-BASED PROCESSING AND TRIGGER RIGHTS/RETENTION FLOW
```

## 5. Notice versioning

Cada envio deve identificar a versão exata do Notice.

Target:

```text
NOTICE_ID
→ RP-002 participant notice

NOTICE_VERSION
→ explicit version string

SENT_AT
→ operational timestamp

CONSENT_STATUS
→ GIVEN / NOT_GIVEN / WITHDRAWN

CONSENT_AT
→ operational timestamp when applicable
```

O GKR armazena apenas o template/versionamento, nunca o registro individual da Pessoa.

## 6. Forma da manifestação

A manifestação deve ser afirmativa, específica ao Notice recebido e suficientemente inequívoca.

Fluxo-alvo por e-mail:

- a Pessoa recebe o Notice versionado;
- pode fazer perguntas antes de decidir;
- responde afirmativamente ao e-mail ou por mecanismo equivalente aprovado;
- a resposta deve demonstrar que a decisão se refere à versão enviada;
- ausência de resposta, reação ambígua ou continuidade da conversa não conta como consentimento.

A versão final da redação será congelada em A11 e revisada em A12.

## 7. Registro mínimo

No Identity Vault, quando o fluxo operacional for aberto, registrar somente:

- `participant_id`;
- `notice_version`;
- `notice_sent_at`;
- `consent_status`;
- `consent_at` quando aplicável;
- `withdrawn_at` quando aplicável;
- referência mínima suficiente à evidência original no canal de Research.

Não copiar o corpo inteiro da conversa para o Identity Vault por padrão.

## 8. Relação com a Research Base

A Research Base recebe apenas:

```text
participant_id
consent_state_required_for_episode_execution
```

Ela não recebe nome, endereço de e-mail ou thread de consentimento.

## 9. Perguntas antes do consentimento

Perguntas de esclarecimento podem ser respondidas sem iniciar o episódio de Research.

Se a Pessoa revelar conteúdo rico antes do consentimento:

- não transformar isso em dossiê;
- minimizar persistência;
- orientar que o episódio ainda não começou;
- excluir conteúdo desnecessário conforme a política aplicável.

## 10. Consentimento negado

```text
NOT_GIVEN
→ no penalty
→ no episode
→ no marketing reuse
→ recruitment data follows A10
```

A recusa não deve gerar perfil negativo nem tentativa persuasiva repetida.

## 11. Revogação

A revogação pode ser solicitada pelo canal de Research ou pelos canais oficiais de privacidade.

Fluxo:

```text
WITHDRAWAL RECEIVED
→ acknowledge
→ mark WITHDRAWN
→ stop new consent-based research processing
→ evaluate deletion / anonymization / lawful conservation
→ close follow-up unless another valid basis and necessity are documented
```

O processo de direitos já possui teste sintético próprio; A7 verificará o stack completo posteriormente.

## 12. Contato futuro

O consentimento do Dry Run não cobre newsletter, marketing, prospecção ou contato indefinido.

```text
GENERIC FUTURE CONTACT
→ OUTSIDE C1
→ separate purpose / authorization when applicable
```

## 13. Base legal

O núcleo voluntário do Dry Run permanece documentado com consentimento como hipótese candidata/selecionada para as operações comuns definidas na matriz do piloto, sujeito à revisão A12.

Operações auxiliares, atendimento de direitos, segurança e eventual conservação legal devem manter fundamento próprio quando aplicável.

Fonte legal de referência:

<https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm>

## 14. Teste futuro

```text
T-NOTICE-CONSENT-001
1. SYNTHETIC EXTERNAL ADDRESS
2. SEND FINAL NOTICE VERSION FROM research@guivos.com
3. RECEIVE AFFIRMATIVE SYNTHETIC REPLY
4. RECORD SYNTHETIC VERSION / STATUS / TIMESTAMP
5. VERIFY NO RICH RESEARCH DATA ENTERED IDENTITY RECORD
6. SIMULATE WITHDRAWAL
7. VERIFY STATUS UPDATE
8. CLEAN SYNTHETIC RECORDS
```

O teste não deve ser executado na fase documental atual.

## 15. Subgates de A2

```text
A2-1 CHANNEL
→ DOCUMENTED / A1 ALREADY PASS

A2-2 VERSIONING MODEL
→ DOCUMENTED

A2-3 AFFIRMATIVE CONSENT FLOW
→ DOCUMENTED

A2-4 WITHDRAWAL FLOW
→ DOCUMENTED

A2-5 FINAL NOTICE TEXT
→ DEPENDS ON A11

A2-6 REAL SYNTHETIC FLOW TEST
→ HOLD

A2 OVERALL
→ OPERATIONAL HOLD
```

## 16. Estado final

```text
A2 DOCUMENTATION
→ FLOW TARGET CLOSED

A2 IMPLEMENTATION / TEST
→ DEFERRED

A2 OPERATIONAL STATUS
→ HOLD

A11
→ FINAL DOCUMENTARY NOTICE MAY BE PRODUCED

PARTICIPANT 001
→ HOLD
```
