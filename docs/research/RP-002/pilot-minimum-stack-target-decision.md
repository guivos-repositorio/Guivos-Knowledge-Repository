---
id: RP-002-PILOT-STACK-DEC-001
title: Piloto — Decisão da Arquitetura-Alvo do Primeiro Dry Run
status: active
version: 1.0.0
owner: Guivos Research
last_updated: 2026-08-27
normative: false
parent: RP-002
maturity: operational_target_approved_pre_configuration
related:
  - RP-002-PILOT-STACK-PROP-001
  - RP-002-PILOT-OP-001
  - RP-002-PILOT-DATA-LAW-001
  - RP-002-PILOT-PRIV-001
  - RP-002-PILOT-NOTICE-CONSENT-001
---

# Piloto — Decisão da Arquitetura-Alvo do Primeiro Dry Run

## 1. Finalidade

Este documento registra a decisão operacional sobre qual arquitetura deverá orientar a preparação do primeiro Dry Run Real `N=1` do `RP-002`.

Ele fecha somente a decisão de **arquitetura-alvo**.

Não configura ferramentas, não aprova operadores por inferência e não libera a entrada de Pessoa real.

## 2. Decisão

Fica aprovada como arquitetura-alvo do primeiro Dry Run Real do `RP-002`:

```text
TARGET ARCHITECTURE
→ OPTION A — LOCAL PRIVACY-FIRST

DECISION STATUS
→ APPROVED AS TARGET

OPERATIONAL STACK
→ NOT YET APPROVED

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```

A decisão adota a recomendação materializada em `RP-002-PILOT-STACK-PROP-001`.

A aprovação é deliberadamente restrita à arquitetura-alvo.

Ela não converte qualquer componente candidato em `PASS`.

## 3. Arquitetura-alvo aprovada

```text
RECRUTAMENTO / NOTICE / CONSENTIMENTO
→ mailbox dedicada de Research sob @guivos.com
→ Hostinger Mail como operador candidato já conhecido
→ endereço final ainda a provisionar e testar

IDENTITY VAULT
→ armazenamento local criptografado A
→ dedicado
→ sem cloud sync por padrão

RESEARCH BASE
→ armazenamento local criptografado B
→ materialmente separado do Identity Vault
→ pseudonimizado
→ sem identidade direta por padrão

LINKAGE KEY
→ separada da Research Base
→ acesso mais restrito

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
```

## 4. Razões da decisão

A Opção A é aprovada para `N=1` porque é a arquitetura que melhor preserva, no estágio atual:

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

Para o primeiro Dry Run, a prioridade não é escalabilidade tecnológica.

A prioridade é provar o método com uma superfície de dados proporcional, rastreável e reversível.

## 5. Relação com o RP-002-PILOT-OP-001

A decisão é compatível com a arquitetura operacional já vigente, que exige:

```text
IDENTITY VAULT
+
RESEARCH BASE PSEUDONIMIZADA
+
LINKAGE KEY MAIS RESTRITA
```

Também preserva as regras de:

- mínimo privilégio;
- ausência de identificadores diretos na Research Base por padrão;
- não uso do GKR como banco de participantes;
- gravação desligada por padrão;
- registro e aprovação de operadores antes de dados reais;
- `Participant 001` em `HOLD` até fechamento dos gates críticos.

## 6. Relação com P3 e P4

Esta decisão não altera automaticamente os gates jurídicos e de privacidade.

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

A arquitetura escolhida reduz ambiguidade sobre o desenho pretendido, mas `P3-C`, `P3-D` e `P4` dependem de fatos operacionais que ainda precisam ser materialmente comprovados.

## 7. Componentes que permanecem não aprovados

### A1 — Mailbox de Research

```text
TARGET
→ HOSTINGER MAIL / @guivos.com

ADDRESS
→ TBD

PROVISIONING
→ NOT DONE

END-TO-END TEST
→ NOT DONE

STATUS
→ HOLD
```

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

O drill sintético anterior prova a lógica do processo, mas não prova o stack operacional ainda inexistente.

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

A arquitetura baseada em Google Workspace Business permanece registrada como alternativa futura de colaboração e escala.

Estado:

```text
OPTION B — GOOGLE WORKSPACE BUSINESS
→ SCALE OPTION
→ NOT SELECTED FOR PARTICIPANT 001
→ NOT REJECTED FOR FUTURE SCALE
→ NOT APPROVED FOR CURRENT PILOT DATA
```

A existência de Google Drive conectado não equivale a tenant empresarial aprovado para tratamento de participantes.

## 9. O que esta decisão fecha

```text
STACK ARCHITECTURE CHOICE
→ CLOSED

SELECTED TARGET
→ OPTION A — LOCAL PRIVACY-FIRST
```

Portanto, não é necessário continuar comparando arquiteturas antes de iniciar a configuração material do stack do `Participant 001`.

## 10. O que esta decisão não fecha

Permanece vedado inferir:

```text
TARGET APPROVED
≠ TOOL CONFIGURED

TARGET APPROVED
≠ OPERATOR APPROVED

TARGET APPROVED
≠ DPA VERIFIED

TARGET APPROVED
≠ RETENTION APPROVED

TARGET APPROVED
≠ LEGAL BASIS FINALIZED

TARGET APPROVED
≠ PARTICIPANT RELEASED
```

## 11. Ordem operacional autorizada

A preparação do stack deve seguir esta sequência:

```text
1. provisionar mailbox dedicada de Research
2. testar recebimento, resposta e owner funcional
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
13. concluir P2C
14. realizar revisão jurídica/privacidade final
15. reavaliar P3-C / P3-D / P4
16. somente então avaliar Participant 001
```

A ordem pode ser paralelizada apenas quando isso não cria dependência circular nem promove gates sem evidência.

## 12. Próximo ato material

O próximo blocker operacional passa a ser:

```text
A1 — RESEARCH MAILBOX
→ DECIDIR ENDEREÇO
→ PROVISIONAR
→ TESTAR END-TO-END
→ REGISTRAR OWNER FUNCIONAL
```

Até esse ato ser materialmente comprovado:

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
→ APPROVED TARGET DECISION

TARGET ARCHITECTURE
→ OPTION A — LOCAL PRIVACY-FIRST

OPERATIONAL STACK READINESS
→ HOLD

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```
