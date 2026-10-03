---
id: GKR-P0-CLOSURE-001
title: Fechamento dos Controles Residuais do P0
status: draft
version: 0.1.0
owner: Guivos Enterprise Architecture
last_updated: 2026-08-05
depends_on:
  - GKR-AUD-ACCUMULATED-003
  - GKR-SOURCE-INTAKE-001
  - GKR-CLAIMS-TRACE-001
related:
  - GKR-EXT-SOURCE-PRESERVATION-001
  - GKR-INFO-CLASS-001
  - GKR-RUNBOOK-GH-CODEX-001
  - GKR-LINEAGE-GC-CON-001-001
  - GKR-VAL-OPS-AUD-001
normative: false
---

# Fechamento dos Controles Residuais do P0

## 1. Finalidade

Registrar o encerramento, no nível de intake e controle, das pendências residuais identificadas após a auditoria de conversas, rascunhos e fontes acumuladas.

Este fechamento não integra conteúdo temático, não altera a Canon e não inicia P2–P9.

## 2. Baseline preservada

| Elemento | Estado preservado |
|---|---|
| Registro do Estado Atual | `GKR-STATE-001` 1.99.0 |
| Marco | M7.72 |
| Última frente integrada | UXA-070 |
| UXA-071 | não iniciada |
| Engenharia de Produto | pausada antes de W0-01 |
| P1 | PR nº 163, separado |
| P0 | PR nº 164, draft |
| Outcomes empresariais | nenhum declarado |
| P2–P9 | não iniciados |

## 3. Controles encerrados

### 3.1 Armazenamento ou referência de fontes históricas

**Decisão:** encerrada por `GKR-EXT-SOURCE-PRESERVATION-001`.

O GKR possui visibilidade pública e adotará o padrão `reference_only` para fontes externas.

Conteúdo integral permanecerá em ambiente controlado quando necessário. A publicação integral será exceção sujeita a titularidade, classificação pública, linhagem resolvida, revisão e autorização.

### 3.2 Classificação de sigilo

**Decisão:** encerrada por `GKR-INFO-CLASS-001`.

Foram estabelecidas quatro classes:

- `public`;
- `internal`;
- `confidential`;
- `restricted`.

Conteúdo interno somente poderá aparecer como síntese sanitizada. Conteúdo confidencial será limitado a metadados mínimos. Conteúdo restrito não poderá ser publicado no Git.

### 3.3 GitHub CLI, autenticação, Codex e workspace

**Decisão:** encerrada por `GKR-RUNBOOK-GH-CODEX-001`.

O procedimento operacional foi separado da arquitetura e passa a possuir:

- verificações de ambiente;
- persistência do `gh` por imagem ou bootstrap;
- autenticação sem exposição de tokens;
- divisão de responsabilidades entre conector GitHub e workspace Codex;
- validação antes do PR;
- recuperação de falhas comuns;
- proibição de merge sem autorização explícita.

## 4. Pendências que não bloqueiam o fechamento do P0

### 4.1 Hashes físicos de fontes externas

O cálculo de hashes permanece condicionado ao recebimento dos arquivos em ambiente controlado.

A falta de hash não altera as decisões de autoridade já registradas e não autoriza publicação dos PDFs.

### 4.2 Evidência operacional VAL

Permanece roteada ao P4.

Nenhuma base, KPI, dashboard preenchido ou decisão poderá ser afirmado sem o pacote de evidência definido em `GKR-VAL-OPS-AUD-001`.

### 4.3 Inventário de marcas, domínios e ativos

Permanece roteado ao P3 e ao P7.

O inventário deverá ser mantido em ambiente confidencial ou restrito, com publicação apenas de sínteses autorizadas.

### 4.4 Varredura de “Guivos Marketplace”

Permanece roteada ao P9 ou a pacote editorial próprio.

A autoridade arquitetural já está resolvida: Guivos Mall é o nome vigente e Marketplace é histórico.

### 4.5 Fontes temáticas futuras

Neo4j, Fundação, internacionalização, Guivos.ai, integrações e demais hipóteses permanecem nos pacotes correspondentes. Nenhuma análise temática é autorizada por este fechamento.

## 5. Critério de conclusão do P0

O P0 é considerado concluído no nível de **intake, autoridade, proveniência e controles de publicação** quando:

1. fontes e alegações relevantes estão catalogadas;
2. colisões de autoridade possuem disposição;
3. conteúdo externo não pode ser promovido automaticamente;
4. fontes sensíveis possuem regra de tratamento;
5. operações GitHub/Codex estão separadas da arquitetura;
6. pendências temáticas estão roteadas;
7. estado global permanece inalterado;
8. gates mecânicos do PR estão aprovados;
9. o PR permanece sujeito a revisão e autorização de merge.

## 6. Resultado

| Dimensão | Resultado |
|---|---|
| Intake acumulado | concluído no nível do P0 |
| Trava de autoridade | ativa |
| Linhagem `GC-CON-001` | conflitante e bloqueada |
| Preservação de fontes | `reference_only` no GKR público |
| Classificação de informação | definida |
| Runbook GitHub/Codex | definido |
| Promoção canônica | nenhuma |
| Mudança de marco | nenhuma |
| Início de pacote posterior | nenhum |
| Merge automático | proibido |

## 7. Próxima decisão governada

Após revisão do PR nº 164, a próxima ação possível será uma decisão explícita entre:

1. solicitar correções adicionais no P0;
2. marcar o PR como pronto para revisão;
3. autorizar o merge do P0;
4. manter o PR em draft enquanto o P1 é tratado separadamente.

Nenhuma dessas ações é executada automaticamente por este documento.
