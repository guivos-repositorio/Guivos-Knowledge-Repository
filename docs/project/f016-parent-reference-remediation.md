---
id: GKR-F016-PARENT-REF-REM-001
title: Remediação das referências parent residuais de F-016
status: active
version: 1.0.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-09-11
normative: false
maturity: remediation_record_partial_automation_blocked
related:
  - GKR-FULL-CORPUS-AUDIT-001
---

# Remediação das referências `parent` residuais de F-016

## 1. Finalidade

Registrar a adjudicação de `F-016-PARENT-REF-REM-01` sobre as referências `parent:` que permanecem em consumidores/validadores correntes depois da remoção física dos produtores visuais legados de F-016.

Este registro não cria nova autoridade de produto, Experience Architecture, Design ou implementação. Ele documenta exclusivamente a classificação das arestas residuais e os limites da remediação executável no checkpoint.

## 2. Checkpoint reconciliado

```text
PR #363
→ OPEN / DRAFT
→ MERGED = FALSE
→ MERGEABLE = TRUE

BASE / MAIN
→ b5acfaffc57afd2714c44dbe53ecf3faba76fe9e
→ UNCHANGED

HEAD DE ENTRADA
→ e0aea7ff5f2e424f70c273f2f8c80f399ce12e20

SEMANTIC #901
→ SUCCESS

MECHANICAL #1157
→ SUCCESS
```

O commit `e0aea7ff...` apenas reconciliou o caminho de `UXA-052` no índice e não alterou a adjudicação de F-016.

## 3. Adjudicação

As 19 arestas abaixo preservam genealogia documental real entre um produtor visual posteriormente removido e o artefato consumidor/validador que permaneceu no corpus.

Elas são classificadas como:

```text
HISTORICAL PROVENANCE
→ YES

CURRENT STRUCTURAL DEPENDENCY
→ NO

CURRENT VISUAL AUTHORITY
→ NO

DESIGN AUTHORIZATION
→ NO

REMATERIALIZATION AUTHORIZATION
→ NO
```

A permanência textual de `parent:` nesses 19 casos não deve ser lida como reintrodução do produtor removido, restauração de materialização visual ou dependência estrutural corrente.

## 4. Allowlist fechada das 19 arestas

| Consumidor preservado | `parent:` histórico removido | Classificação |
|---|---|---|
| UXA-026 | UXA-024 | proveniência histórica F-016 |
| UXA-028 | UXA-024 | proveniência histórica F-016 |
| UXA-030 | UXA-024 | proveniência histórica F-016 |
| UXA-032 | UXA-024 | proveniência histórica F-016 |
| UXA-035 | UXA-034 | proveniência histórica F-016 |
| UXA-037 | UXA-036 | proveniência histórica F-016 |
| UXA-041 | UXA-040 | proveniência histórica F-016 |
| UXA-043 | UXA-042 | proveniência histórica F-016 |
| UXA-045 | UXA-044 | proveniência histórica F-016 |
| UXA-047 | UXA-046 | proveniência histórica F-016 |
| UXA-049 | UXA-048 | proveniência histórica F-016 |
| UXA-052 | UXA-051 | proveniência histórica F-016 |
| UXA-054 | UXA-053 | proveniência histórica F-016 |
| UXA-061 | UXA-060 | proveniência histórica F-016 |
| UXA-063 | UXA-005 | proveniência histórica F-016 |
| UXA-065 | UXA-005 | proveniência histórica F-016 |
| UXA-067 | UXA-005 | proveniência histórica F-016 |
| UXA-069 | UXA-068 | proveniência histórica F-016 |
| UXA-099 | UXA-055 | proveniência histórica F-016 |

Regra fechada:

```text
PARENT → REMOVED F-016 PRODUCER
→ ALLOWED ONLY FOR THE 19 PAIRS ABOVE
→ HISTORICAL PROVENANCE ONLY

ANY OTHER PARENT → REMOVED F-016 PRODUCER
→ NOT ADJUDICATED
→ MUST FAIL GOVERNED REVIEW
```

## 5. Relação com as dependências vigentes

As dependências funcionais correntes permanecem expressas pelos campos e contratos vigentes, especialmente `depends_on`, `related` e pelas autoridades funcionais preservadas.

```text
HISTORICAL parent
≠ depends_on
≠ related authority
≠ current visual producer
≠ implementation dependency
```

Nenhum novo `parent` foi inventado e nenhuma autoridade corrente foi promovida para substituir artificialmente os produtores removidos.

## 6. Guard automático — estado do checkpoint

Foi tentada a persistência de uma allowlist fechada em `scripts/validate_semantic_state.py`, destinada a:

1. aceitar somente os 19 pares adjudicados;
2. tratar esses pares exclusivamente como proveniência histórica;
3. falhar qualquer nova aresta `parent:` para produtor removido fora da allowlist;
4. provar que os 19 pares esperados não foram silenciosamente alterados.

As duas formas de escrita disponibilizadas pelo conector para o arquivo de código foram bloqueadas pelas configurações de segurança antes de qualquer commit ou alteração de branch.

Portanto:

```text
SEMANTIC ADJUDICATION
→ COMPLETED

CORPUS RECORD
→ PERSISTED BY THIS REMEDIATION RECORD

AUTOMATED PARENT-EDGE GUARD
→ NOT PERSISTED
→ BLOCKED BY CONNECTOR SECURITY

CLAIM OF FULL AUTOMATED CLOSURE
→ NOT ALLOWED
```

Esse bloqueio não deve ser contornado por uma escrita menos governada.

## 7. Limites preservados

Esta remediação não autoriza:

- reintrodução de qualquer produtor visual removido em F-016;
- reintrodução de SVGs;
- Design;
- nova materialização;
- `UXA-102 / V5`;
- Product Engineering;
- implementação, operação ou produção;
- dados reais;
- merge da PR #363;
- alteração de `main`.

## 8. Estado final desta etapa

```text
F-016-PARENT-REF-REM-01
→ SEMANTIC ADJUDICATION COMPLETED
→ 19 / 19 EDGES CLASSIFIED
→ HISTORICAL PROVENANCE ONLY

AUTOMATED GUARD
→ BLOCKED / NOT PERSISTED

FOLLOW-UP REQUIRED
→ F-016-PARENT-REF-GUARD-01
→ persist exact closed allowlist in semantic validation when a governed code-write path is available
```

Até esse follow-up, nenhuma nova aresta `parent:` para produtor removido deve ser aceita por inferência.