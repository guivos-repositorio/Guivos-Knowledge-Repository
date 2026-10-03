---
id: RP-002-PILOT-STACK-DEC-001
title: Piloto — Decisão da Arquitetura-Alvo do Primeiro Dry Run
status: active
version: 1.1.1
owner: Guivos Research
last_updated: 2026-09-04
normative: false
parent: RP-002
maturity: operational_target_partially_configured
related:
  - RP-002-PILOT-STACK-PROP-001
  - RP-002-PILOT-OP-001
  - RP-002-PILOT-DATA-LAW-001
  - RP-002-PILOT-PRIV-001
  - RP-002-PILOT-NOTICE-CONSENT-002
  - RP-002-PILOT-RESEARCH-MAILBOX-DEC-001
  - RP-002-PILOT-RESEARCH-MAILBOX-TEST-001
---

# Piloto — Decisão da Arquitetura-Alvo do Primeiro Dry Run

## 1. Finalidade

Este documento registra a decisão operacional sobre qual arquitetura orienta a preparação do primeiro Dry Run Real `N=1` do `RP-002` e mantém o estado reconciliado dos componentes já configurados.

A arquitetura-alvo permanece a **Option A — Local Privacy-First**.

O fechamento de um componente não aprova por inferência os demais nem libera Pessoa real.

## 2. Decisão

```text
TARGET ARCHITECTURE
→ OPTION A — LOCAL PRIVACY-FIRST

DECISION STATUS
→ APPROVED AS TARGET

OPERATIONAL STACK
→ PARTIALLY CONFIGURED / NOT YET APPROVED

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```

A decisão continua baseada em `RP-002-PILOT-STACK-PROP-001`.

## 3. Arquitetura-alvo reconciliada

```text
RECRUTAMENTO / OPERAÇÃO DE RESEARCH
→ research@guivos.com
→ Hostinger Mail
→ A1 RESEARCH MAILBOX = PASS

NOTICE / CONSENTIMENTO
→ versioned email trail
→ final flow ainda não congelado

IDENTITY VAULT
→ armazenamento local criptografado A
→ dedicado
→ sem cloud sync por padrão
→ ainda não configurado

RESEARCH BASE
→ armazenamento local criptografado B
→ materialmente separado do Identity Vault
→ pseudonimizado
→ sem identidade direta por padrão
→ ainda não configurado

LINKAGE KEY
→ separada da Research Base
→ acesso mais restrito
→ ainda não configurada

IA
→ OpenAI API dedicada à Guivos / RP-002
→ contexto mínimo pseudonimizado
→ sem identificadores diretos
→ configuração e controles ainda a verificar

SEARCH / WEB
→ pesquisa pública
→ queries minimizadas
→ sem identificadores diretos
→ operador/método final ainda a aprovar

PRIVACIDADE / DIREITOS
→ privacidade@guivos.com
→ privacy@guivos.com
→ Hostinger Mail
→ P2B = PASS
→ P2C = PASS
```

## 4. Razões da decisão

A Opção A permanece aprovada para `N=1` porque preserva:

1. minimização de dados;
2. separação material entre identidade e pesquisa;
3. menor superfície de operadores externos;
4. pseudonimização antes de IA e pesquisa externa;
5. possibilidade de correção e exclusão executáveis;
6. baixa dependência de infraestrutura definitiva de produto;
7. reversibilidade caso o método precise ser alterado;
8. aderência ao `RP-002-PILOT-OP-001`;
9. aderência ao `RP-002-PILOT-DATA-LAW-001`;
10. manutenção explícita dos blockers ainda não comprovados.

Para o primeiro Dry Run, a prioridade continua sendo provar o método com uma superfície de dados proporcional, rastreável e reversível.

## 5. Relação com o RP-002-PILOT-OP-001

A arquitetura operacional vigente exige:

```text
IDENTITY VAULT
+
RESEARCH BASE PSEUDONIMIZADA
+
LINKAGE KEY MAIS RESTRITA
```

Também permanecem as regras de:

- mínimo privilégio;
- ausência de identificadores diretos na Research Base por padrão;
- não uso do GKR como banco de participantes;
- gravação desligada por padrão;
- registro e aprovação de operadores antes de dados reais;
- `Participant 001` em `HOLD` até fechamento dos gates críticos.

## 6. Relação com P3 e P4

Estado preservado:

```text
P3-A — FINALIDADES
→ PASS DOCUMENTAL

P3-B — CATEGORIAS DE DADOS
→ PASS DOCUMENTAL

P3-C — DESTINATÁRIOS / OPERADORES REAIS
→ HOLD

P3-D — PRAZOS EXATOS DE RETENÇÃO
→ HOLD

P3
→ CONDITIONAL

P4
→ HOLD
```

O fechamento de A1 e P2C reduz blockers, mas `P3-C`, `P3-D` e `P4` dependem do conjunto efetivo do stack e da revisão final.

## 7. Estado dos componentes

### A1 — Mailbox de Research

```text
ADDRESS
→ research@guivos.com

OPERATOR
→ Hostinger Mail

PROVISIONING
→ PASS

END-TO-END TEST
→ PASS

FUNCTIONAL OWNER
→ PASS

FUNCTIONAL SEGREGATION
→ PASS

STATUS
→ PASS
```

Evidência:

- `RP-002-PILOT-RESEARCH-MAILBOX-DEC-001`;
- `RP-002-PILOT-RESEARCH-MAILBOX-TEST-001`.

### A2 — Fluxo de Notice e consentimento

```text
MODEL
→ VERSIONED EMAIL TRAIL

FINAL NOTICE VERSION
→ NOT FROZEN

REAL FLOW TEST
→ NOT DONE

STATUS
→ HOLD
```

### A3 — Identity Vault

```text
ARCHITECTURE
→ APPROVED AS TARGET

ENCRYPTED STORAGE
→ NOT CONFIGURED

PERMISSIONS
→ NOT VERIFIED

BACKUP
→ NOT TESTED

STATUS
→ HOLD
```

### A4 — Research Base

```text
ARCHITECTURE
→ APPROVED AS TARGET

SEPARATE ENCRYPTED STORAGE
→ NOT CONFIGURED

PSEUDONYMIZATION FLOW
→ NOT TESTED IN REAL STACK

STATUS
→ HOLD
```

### A5 — Linkage Key

```text
SEPARATION REQUIREMENT
→ APPROVED

REAL IMPLEMENTATION
→ NOT CONFIGURED

STATUS
→ HOLD
```

### A6 — Backup / recovery

```text
ENCRYPTED BACKUP
→ REQUIRED

RECOVERY TEST
→ NOT DONE

STATUS
→ HOLD
```

### A7 — Correction / deletion drill

O drill sintético anterior prova a lógica do processo, mas não prova o stack operacional ainda incompleto.

```text
SYNTHETIC LOGIC
→ PASS

TARGET STACK DRILL
→ NOT EXECUTED

STATUS
→ HOLD
```

### A8 — OpenAI API

```text
TARGET
→ DEDICATED GUIVOS / RP-002 API PROJECT

DIRECT IDENTIFIERS
→ PROHIBITED BY DEFAULT

ACCOUNT / PROJECT
→ NOT VERIFIED

DATA CONTROLS
→ NOT VERIFIED

DPA STATUS
→ NOT RECORDED FOR OPERATIONAL APPROVAL

STATUS
→ HOLD
```

Esta decisão não presume elegibilidade a Zero Data Retention.

### A9 — Search / Web

```text
METHOD
→ MINIMIZED PUBLIC SEARCH

DIRECT IDENTIFIERS IN QUERY
→ NO

FINAL OPERATOR / METHOD RECORD
→ PENDING

STATUS
→ HOLD
```

### A10 — Retenção

```text
EXACT PERIODS
→ NOT FROZEN

STATUS
→ HOLD
```

### A11 — Notice final

```text
STACK DISCLOSURE
→ MUST MATCH REAL CONFIGURATION

FINAL VERSION
→ NOT FROZEN

STATUS
→ HOLD
```

### A12 — Revisão jurídica / privacidade final

```text
FINAL REVIEW
→ NOT COMPLETED

STATUS
→ HOLD
```

## 8. Opção B

A arquitetura baseada em Google Workspace Business permanece alternativa futura de colaboração e escala.

```text
OPTION B — GOOGLE WORKSPACE BUSINESS
→ SCALE OPTION
→ NOT SELECTED FOR PARTICIPANT 001
→ NOT REJECTED FOR FUTURE SCALE
→ NOT APPROVED FOR CURRENT PILOT DATA
```

A existência de Google Drive conectado não equivale a tenant empresarial aprovado para tratamento de participantes.

## 9. O que já está fechado

```text
STACK ARCHITECTURE CHOICE
→ CLOSED

SELECTED TARGET
→ OPTION A — LOCAL PRIVACY-FIRST

A1 — RESEARCH MAILBOX
→ PASS

P2B — PRIVACY CHANNEL
→ PASS

P2C — RIGHTS PROCESS SYNTHETIC TEST
→ PASS
```

## 10. O que permanece vedado inferir

```text
TARGET APPROVED
≠ FULL STACK CONFIGURED

A1 PASS
≠ P3-C PASS

P2C PASS
≠ FINAL LEGAL REVIEW PASS

PARTIAL STACK
≠ PARTICIPANT RELEASED
```

## 11. Ordem operacional autorizada

A preparação do stack permanece nesta sequência material:

```text
1. mailbox dedicada de Research → COMPLETED / A1 PASS
2. recebimento, resposta, owner e segregação → COMPLETED / A1 PASS
3. configurar Identity Vault local criptografado
4. configurar Research Base local criptografada e separada
5. configurar separação da linkage key
6. configurar e testar backup criptografado
7. repetir correction + deletion drill no stack-alvo
8. configurar projeto OpenAI API dedicado
9. registrar controles aplicáveis da API / DPA
10. aprovar método/operador de Search/Web
11. congelar prazos exatos de retenção
12. atualizar e congelar Notice correspondente ao stack real
13. P2C → COMPLETED / PASS
14. realizar revisão jurídica/privacidade final
15. reavaliar P3-C / P3-D / P4
16. somente então avaliar Participant 001
```

A ordem pode ser paralelizada apenas quando isso não cria dependência circular nem promove gates sem evidência.

## 12. Próximo ato material

Com `A1` encerrado, o próximo blocker material passa a ser:

```text
A3 — IDENTITY VAULT
→ CONFIGURAR ARMAZENAMENTO LOCAL CRIPTOGRAFADO
→ VERIFICAR PERMISSÕES
→ PRESERVAR SEM CLOUD SYNC POR PADRÃO
```

Até a continuidade do stack:

```text
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

## 13. Estado final desta decisão

```text
RP-002-PILOT-STACK-PROP-001
→ PROPOSAL PRESERVED

RP-002-PILOT-STACK-DEC-001
→ APPROVED TARGET DECISION / PARTIALLY CONFIGURED

TARGET ARCHITECTURE
→ OPTION A — LOCAL PRIVACY-FIRST

A1 — RESEARCH MAILBOX
→ PASS

OPERATIONAL STACK READINESS
→ HOLD

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```
