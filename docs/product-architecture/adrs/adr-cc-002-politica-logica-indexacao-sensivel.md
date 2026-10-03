---
id: ADR-CC-002
title: Política Lógica de Indexação Sensível
status: proposed
version: 0.1.0
owner: Guivos
last_updated: 2026-07-19
normative: true
related:
  - PAS-001-CC-UIC-STORAGE-INDEX-001
  - PAS-001-CC-UIC-GUARDRAILS-ACCESS-001
---

# ADR-CC-002 — Política Lógica de Indexação Sensível

## Status

`Proposed 0.1.0`.

## Contexto

A UIC-01 precisa localizar conteúdo, oportunidades de reconstrução, entradas relacionadas e derivados. Porém, índices podem replicar conteúdo sensível, misturar participantes, ignorar finalidade e sobreviver à revogação.

## Decisão

Toda entrada deverá adotar uma política explícita entre:

- `prohibited`;
- `metadata_only`;
- `protected`;
- `participant_private`;
- `purpose_scoped`;
- `temporary`.

A autorização será aplicada antes da recuperação material. Índice, cache, embedding e snippet não são sistema de registro nem autoridade funcional.

## Regras obrigatórias

1. escopo do participante precede filtros de conteúdo;
2. resultado não amplia finalidade;
3. snippet respeita sensibilidade e redaction;
4. interpretação preserva sua natureza;
5. conteúdo não confirmado não aparece como confirmado;
6. revogação remove ou bloqueia resultados imediatamente;
7. correção atualiza o índice por compensação;
8. embeddings possuem fonte, versão, modelo e finalidade;
9. logs de consulta não contêm conteúdo bruto;
10. entrada incompatível fica em quarentena.

## Consequências positivas

- busca compatível com privacidade e autoridade;
- revogação e correção rastreáveis;
- possibilidade de diferentes mecanismos físicos;
- isolamento explícito;
- redução do risco de reidentificação e exfiltração.

## Consequências negativas

- maior custo de política e filtragem;
- resultados podem ser incompletos durante convergência;
- reindexação será necessária após mudanças de contrato;
- embeddings exigem governança semelhante à fonte;
- métricas deverão evitar atributos identificáveis.

## Alternativas rejeitadas

### Indexar todo conteúdo por padrão

Rejeitada por violar minimização, finalidade e revogação.

### Autorizar após recuperar

Rejeitada porque a recuperação já constitui exposição técnica.

### Considerar embedding anonimizado

Rejeitada porque embeddings podem preservar informação sensível e permitir reidentificação.

## Falha segura

Na ausência de política, finalidade, fonte, versão ou escopo válido, o conteúdo não será indexado nem retornado.

## Evidências requeridas

- teste de isolamento entre participantes;
- teste de autorização pré-recuperação;
- teste de revogação;
- teste de correção;
- teste de snippet redigido;
- inventário de embeddings e derivados;
- prova de ausência de conteúdo bruto em logs.

## Decisões posteriores

Mecanismo lexical, vetorial, híbrido, formato do índice, engine e estratégia física de tenancy permanecem para ADR tecnológico.