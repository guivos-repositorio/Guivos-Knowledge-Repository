---
id: GKR-F016-PARENT-REF-REM-001
title: Remediação das referências parent residuais de F-016
status: active
version: 1.0.1
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-09-11
normative: false
maturity: remediation_record_guard_persisted
related:
  - GKR-FULL-CORPUS-AUDIT-001
---

# Remediação das referências `parent` residuais de F-016

## 1. Finalidade

Registrar a adjudicação de `F-016-PARENT-REF-REM-01` sobre as referências `parent:` que permanecem em consumidores/validadores correntes depois da remoção física dos produtores visuais legados de F-016 e registrar o guard automático posterior `F-016-PARENT-REF-GUARD-01`.

Este registro não cria nova autoridade de produto, Experience Architecture, Design ou implementação. Ele documenta exclusivamente a classificação das arestas residuais, sua proteção automática e os limites desta remediação.

## 2. Checkpoint reconciliado

```text
PR #363
→ OPEN / DRAFT
→ MERGED = FALSE
→ MERGEABLE = TRUE

BASE / MAIN
→ b5acfaffc57afd2714c44dbe53ecf3faba76fe9e
→ UNCHANGED

HEAD DE ENTRADA DA REMEDIAÇÃO
→ e0aea7ff5f2e424f70c273f2f8c80f399ce12e20

SEMANTIC #901
→ SUCCESS

MECHANICAL #1157
→ SUCCESS
```

O commit `e0aea7ff...` apenas reconciliou o caminho de `UXA-052` no índice e não alterou a adjudicação de F-016.

A adjudicação foi inicialmente persistida no commit:

```text
85a028723c86fe28da967068b076ed0e273ab96e
→ GKR: record F-016 historical parent adjudication

Semantic #902
→ SUCCESS

Mechanical #1158
→ SUCCESS
```

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
→ MUST FAIL SEMANTIC VALIDATION
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

## 6. Guard automático

`F-016-PARENT-REF-GUARD-01` foi persistido em:

```text
ffdbd4ab3bdb31fa84ab20f5acc8171d9f0cdcca
→ GKR: guard F-016 historical parent references
```

O guard em `scripts/validate_semantic_state.py` mantém uma allowlist fechada com os mesmos 19 pares adjudicados e executa duas provas complementares:

1. cada consumidor histórico esperado deve continuar presente e manter exatamente o `parent` adjudicado;
2. qualquer `parent:` corrente que aponte para um produtor removido por F-016 deve pertencer exatamente à allowlist; caso contrário, a validação semântica falha.

A saída de sucesso também publica a quantidade esperada:

```text
f016_historical_parent_edges=19
```

Portanto:

```text
SEMANTIC ADJUDICATION
→ COMPLETED

CORPUS RECORD
→ PERSISTED

AUTOMATED PARENT-EDGE GUARD
→ PERSISTED

CLOSED ALLOWLIST
→ 19 / 19

NEW UNADJUDICATED parent → REMOVED F-016 PRODUCER
→ SEMANTIC FAILURE
```

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
→ COMPLETED
→ 19 / 19 EDGES CLASSIFIED
→ HISTORICAL PROVENANCE ONLY

F-016-PARENT-REF-GUARD-01
→ EXECUTED
→ EXACT CLOSED ALLOWLIST PERSISTED

STRUCTURAL CURRENT DEPENDENCY TO REMOVED PRODUCERS
→ NOT CREATED

HISTORICAL GENEALOGY
→ PRESERVED

NEXT AUTOMATIC EXECUTION
→ NONE
```

A conclusão desta etapa não resolve por inferência thread de review, não declara Codex final limpo e não autoriza merge da PR #363.