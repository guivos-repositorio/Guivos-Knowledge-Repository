---
id: RP-002-PILOT-LINKAGE-KEY-DEC-001
title: Piloto — Decisão de Implementação do A5 Linkage Key
status: active
version: 1.0.0
owner: Guivos Research
last_updated: 2026-08-27
normative: false
parent: RP-002
maturity: implementation_target_approved_pre_configuration
related:
  - RP-002-PILOT-DOC-CLOSE-001
  - RP-002-PILOT-STACK-DEC-001
  - RP-002-PILOT-IDENTITY-VAULT-DEC-001
  - RP-002-PILOT-RESEARCH-BASE-DEC-001
  - RP-002-PILOT-OP-001
  - RP-002-PILOT-DATA-LAW-001
---

# Piloto — Decisão de Implementação do A5 Linkage Key

## 1. Finalidade

Este documento define o target documental do `A5 — Linkage Key` do `RP-002`.

A Linkage Key existe somente para permitir que a Guivos relacione, quando estritamente necessário, a identidade operacional mantida no Identity Vault ao pseudônimo usado na Research Base.

Ela não é uma terceira base de Research e não deve acumular conteúdo do episódio.

```text
A5 DOCUMENTATION TARGET
→ DECIDED

A5 OPERATIONAL CONFIGURATION
→ HOLD

PARTICIPANT 001
→ HOLD
```

## 2. Função única

A função permitida é:

```text
DIRECT IDENTITY RECORD
↔ participant_id
```

A Linkage Key deve conter o mínimo necessário para essa relação.

Campos-alvo mínimos:

- `participant_id`;
- referência mínima ao registro operacional correspondente no Identity Vault;
- status da ligação (`active`, `withdrawn`, `closed`), quando necessário;
- timestamp mínimo de criação/alteração, quando necessário à governança.

Não deve conter:

- síntese do Momento;
- Possibilidades;
- benchmark;
- evidências Guivos;
- notas de entrevista;
- follow-up rico;
- dados sensíveis;
- credenciais;
- senhas;
- conteúdo desnecessário do Identity Vault.

## 3. Separação material

```text
IDENTITY VAULT
→ identidade + operação mínima

LINKAGE KEY
→ ligação mínima

RESEARCH BASE
→ conteúdo pseudonimizado
```

Regras:

1. a Linkage Key não deve ficar dentro da Research Base;
2. a Research Base não deve possuir cópia da Linkage Key;
3. a Linkage Key não deve ser publicada no GKR;
4. exportações analíticas não devem incluir a Linkage Key;
5. acesso à Linkage Key deve ser mais restrito do que o acesso normal à Research Base.

## 4. Implementação-alvo

Para `N=1`, o target é manter a Linkage Key em boundary local criptografado separado e simples, evitando infraestrutura excessiva.

```text
STORAGE
→ local encrypted boundary

CLOUD SYNC
→ NO

DEFAULT ACCESS
→ Pilot Owner / Data Steward only

GENERAL RESEARCH ACCESS
→ NO
```

A implementação física poderá reutilizar o mecanismo criptográfico selecionado para o stack local, desde que o boundary seja materialmente separado e não seja automaticamente montado junto com a Research Base.

A configuração real permanece adiada pela fase de fechamento documental.

## 5. Política de acesso

Target:

```text
PILOT OWNER
→ ALLOWED

DATA STEWARD
→ ALLOWED

INTERVIEWER
→ NO BY DEFAULT

SUPPLY RESEARCHER / VERIFIER
→ NO

BENCHMARK BLINDER
→ NO

ANALYST
→ NO

AI TOOL
→ NO

SEARCH / WEB TOOL
→ NO
```

Exceções exigem necessidade documentada e revisão antes do acesso.

## 6. Regra de uso

A Linkage Key deve ser aberta somente quando houver necessidade operacional legítima, por exemplo:

- reconciliar contato com o `participant_id` correto;
- aplicar correção ou exclusão solicitada;
- registrar revogação;
- executar fechamento do episódio;
- localizar o conjunto pseudonimizado relacionado a um titular.

Ela não deve permanecer aberta durante análise normal do episódio.

## 7. Proibição de exposição externa

```text
OPENAI API
→ MUST NOT RECEIVE LINKAGE KEY

SEARCH / WEB
→ MUST NOT RECEIVE LINKAGE KEY

EMAIL ATTACHMENT
→ MUST NOT CONTAIN LINKAGE KEY

GKR
→ MUST NOT CONTAIN LINKAGE KEY
```

A Linkage Key é um artefato interno de reidentificação controlada.

## 8. Correção, revogação e exclusão

Quando houver correção ou revogação:

- atualizar somente o mínimo necessário;
- preservar consistência entre Identity Vault, Linkage Key e Research Base;
- não duplicar conteúdo para criar histórico informal;
- aplicar a política de retenção definida em A10;
- quando a ligação deixar de ser necessária e não houver fundamento para preservá-la, removê-la conforme o fluxo aprovado.

A execução real será verificada em A7.

## 9. Retenção

A Linkage Key deve ter retenção mais curta ou igual ao período em que a reidentificação seja realmente necessária.

A10 deverá congelar o prazo ou critério exato antes de dados reais.

```text
LINKAGE RETENTION
→ MINIMIZE
→ NO LONGER THAN NECESSARY
→ EXACT RULE PENDING A10
```

## 10. Backup

A6 deve decidir se a Linkage Key terá backup separado e sob quais condições.

Qualquer backup:

- deve permanecer criptografado;
- não pode ser agregado à Research Base;
- deve manter controle de acesso equivalente ou mais restrito;
- deve ser incluído no processo futuro de exclusão/recovery.

## 11. Teste futuro

Teste sintético futuro:

```text
T-LINKAGE-001
1. CREATE SYNTHETIC participant_id
2. CREATE SYNTHETIC MINIMUM LINK
3. CONFIRM RESEARCH BASE HAS NO DIRECT IDENTITY
4. CONFIRM LINKAGE KEY HAS NO RESEARCH DOSSIER
5. USE LINK TO LOCATE SYNTHETIC RESEARCH RECORD
6. UPDATE SYNTHETIC LINK STATUS
7. DELETE SYNTHETIC LINK
8. CONFIRM NO REAL PARTICIPANT DATA WAS USED
```

O teste permanece adiado até a fase operacional.

## 12. Subgates de A5

```text
A5-1 PURPOSE / MINIMUM SCHEMA
→ DOCUMENTED

A5-2 MATERIAL SEPARATION TARGET
→ DOCUMENTED

A5-3 ACCESS MODEL
→ DOCUMENTED

A5-4 REAL ENCRYPTED BOUNDARY
→ HOLD

A5-5 SYNTHETIC FUNCTIONAL TEST
→ HOLD

A5 OVERALL
→ OPERATIONAL HOLD
```

## 13. Estado final

```text
A5 DOCUMENTATION
→ TARGET CLOSED

A5 IMPLEMENTATION
→ DEFERRED

A5 OPERATIONAL STATUS
→ HOLD

A6 — BACKUP / RECOVERY DOCUMENTATION
→ NEXT

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```
