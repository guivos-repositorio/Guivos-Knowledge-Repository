---
id: RP-002-PILOT-DOC-CLOSE-001
title: Piloto — Decisão de Fechamento Documental antes da Implantação
status: active
version: 1.0.0
owner: Guivos Research
last_updated: 2026-08-27
normative: false
parent: RP-002
maturity: documentation_closure_phase_approved
related:
  - RP-002-PILOT-STACK-DEC-001
  - RP-002-PILOT-IDENTITY-VAULT-DEC-001
  - RP-002-PILOT-OP-001
  - RP-002-PILOT-DATA-LAW-001
  - RP-002-PILOT-OPS-REG-001
---

# Piloto — Decisão de Fechamento Documental antes da Implantação

## 1. Finalidade

Este documento registra a decisão de governança de concluir a documentação necessária do stack do primeiro Dry Run Real `N=1` do `RP-002` antes de avançar para novas implantações, configurações locais ou testes operacionais.

A decisão não desfaz componentes já comprovados, como `A1`, `P2B` e `P2C`. Ela altera apenas a ordem da preparação ainda pendente.

## 2. Decisão

```text
CURRENT PHASE
→ DOCUMENTATION CLOSURE

NEW OPERATIONAL IMPLEMENTATION
→ DEFERRED

REAL PARTICIPANT DATA
→ PROHIBITED

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```

Princípio:

> **Primeiro fechar o contrato documental do stack; depois implantar e provar operacionalmente o que foi documentado.**

## 3. Efeito sobre decisões anteriores

O `RP-002-PILOT-STACK-DEC-001` e o `RP-002-PILOT-IDENTITY-VAULT-DEC-001` permanecem válidos quanto à arquitetura, requisitos, gates e implementação-alvo já decididos.

Porém, qualquer cláusula anterior que determine que o **próximo ato imediato** seja instalação, configuração ou teste operacional fica temporariamente subordinada a esta decisão.

Isso significa:

```text
A3 TARGET DOCUMENTED
→ PRESERVED

A3 IMPLEMENTATION
→ DEFERRED

A3 OPERATIONAL STATUS
→ HOLD
```

Nenhum `HOLD` operacional deve ser convertido em `PASS` por fechamento documental.

## 4. Separação obrigatória de estados

A partir desta decisão, o GKR deve distinguir explicitamente:

```text
DOCUMENTED TARGET
→ requisito, arquitetura, fluxo, papéis e critérios definidos

IMPLEMENTED
→ componente realmente configurado

TESTED
→ comportamento verificado com evidência proporcional

OPERATIONALLY APPROVED
→ gate promovido após evidência
```

Logo:

```text
DOCUMENTATION CLOSED
≠ IMPLEMENTED

IMPLEMENTED
≠ TESTED

TESTED
≠ PARTICIPANT RELEASED
```

## 5. Escopo do fechamento documental

A fase documental deve fechar, na medida em que não dependa de evidência operacional:

1. `A2` — fluxo-alvo de Notice e consentimento;
2. `A3` — Identity Vault, já com target de implementação documentado;
3. `A4` — Research Base pseudonimizada;
4. `A5` — Linkage Key e política de ligação;
5. `A6` — backup e recovery;
6. `A8` — OpenAI API, escopo, minimização, controles e requisitos contratuais;
7. `A9` — Search/Web, método e minimização de queries;
8. `A10` — política e períodos de retenção a serem congelados antes de dados reais;
9. `A11` — Notice final compatível com o stack documentado;
10. `A12` — checklist e critérios da revisão jurídica/privacidade final.

`A7 — correction/deletion drill` permanece essencialmente operacional: sua lógica pode ser documentada, mas o gate só poderá fechar após execução sobre o stack implementado.

## 6. Ordem documental autorizada

A sequência documental passa a ser:

```text
D1. RECONCILIAR A2 / NOTICE + CONSENT FLOW
D2. A3 TARGET → ALREADY DOCUMENTED
D3. DOCUMENTAR A4 — RESEARCH BASE
D4. DOCUMENTAR A5 — LINKAGE KEY
D5. DOCUMENTAR A6 — BACKUP / RECOVERY
D6. DOCUMENTAR A8 — OPENAI API
D7. DOCUMENTAR A9 — SEARCH / WEB
D8. CONGELAR A10 — RETENTION POLICY
D9. RECONCILIAR E CONGELAR A11 — FINAL NOTICE
D10. DOCUMENTAR A12 — FINAL LEGAL / PRIVACY REVIEW CHECKLIST
D11. EXECUTAR DOCUMENTATION CONSISTENCY REVIEW
D12. SOMENTE DEPOIS ABRIR IMPLEMENTATION PHASE
```

A ordem pode ser ajustada quando houver dependência documental explícita, mas não deve antecipar implantação operacional.

## 7. O que fica proibido nesta fase

Até o encerramento formal da fase documental, não realizar como parte desta frente:

- instalação de VeraCrypt para o piloto;
- criação de `identity-vault.hc` real;
- criação de Research Base real;
- criação de Linkage Key real;
- configuração de backup real;
- execução de `T-IDENTITY-001`;
- correction/deletion drill no stack-alvo;
- configuração de projeto de API para uso com participante;
- inserção de qualquer dado real de participante em ferramentas do stack;
- promoção de gates operacionais sem evidência.

Esta vedação não impede pesquisa técnica/documental nem atualização de decisões-alvo.

## 8. Estado reconciliado

```text
A1 — RESEARCH MAILBOX
→ PASS

A2 — NOTICE / CONSENT FLOW
→ DOCUMENTATION TO RECONCILE
→ OPERATIONAL HOLD

A3 — IDENTITY VAULT
→ IMPLEMENTATION TARGET DOCUMENTED
→ OPERATIONAL HOLD

A4 — RESEARCH BASE
→ DOCUMENTATION PENDING
→ OPERATIONAL HOLD

A5 — LINKAGE KEY
→ DOCUMENTATION PENDING
→ OPERATIONAL HOLD

A6 — BACKUP / RECOVERY
→ DOCUMENTATION PENDING
→ OPERATIONAL HOLD

A7 — CORRECTION / DELETION DRILL
→ OPERATIONAL HOLD

A8 — OPENAI API
→ DOCUMENTATION PENDING
→ OPERATIONAL HOLD

A9 — SEARCH / WEB
→ DOCUMENTATION PENDING
→ OPERATIONAL HOLD

A10 — RETENTION
→ DOCUMENTATION PENDING
→ OPERATIONAL HOLD

A11 — FINAL NOTICE
→ DOCUMENTATION PENDING
→ OPERATIONAL HOLD

A12 — FINAL LEGAL / PRIVACY REVIEW
→ DOCUMENTATION PENDING
→ OPERATIONAL HOLD
```

## 9. Gates superiores preservados

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

O fechamento documental poderá reduzir incerteza e preparar a revisão desses gates, mas não os promove automaticamente.

## 10. Critério para encerrar a fase documental

A fase somente poderá ser declarada `DOCUMENTATION CLOSED` quando:

- todos os documentos D1–D10 existirem ou estiverem reconciliados;
- não houver contradição material entre stack, notice, retenção, operadores e papéis;
- cada componente distinguir target documental de evidência operacional;
- os operadores externos propostos estiverem registrados com escopo e limitações;
- a política de retenção estiver suficientemente definida para o Notice;
- o checklist de revisão final estiver pronto;
- nenhum documento induzir interpretação de que Pessoa real já está liberada.

## 11. Próximo ato autorizado

O próximo ato material passa a ser exclusivamente documental:

```text
NEXT
→ DOCUMENT A4 — PSEUDONYMIZED RESEARCH BASE TARGET

DO NOT
→ INSTALL
→ CONFIGURE
→ TEST REAL STACK
→ USE REAL PARTICIPANT DATA
```

Após A4, a sequência continua pelos itens documentais desta decisão.
