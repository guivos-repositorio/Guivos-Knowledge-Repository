---
id: ROADMAP-11.58.0
title: Roadmap Arquitetural — COD-005 Registrado
status: active
version: 11.58.0
owner: Guivos
last_updated: 2026-07-25
supersedes_partial:
  - ROADMAP-11.57.0
related:
  - GKR-STATE-001
  - GKR-R6-RESUMPTION-001
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - BA-STR-002-COD-SUB-005
  - COD-005
  - M7.7
---

# Roadmap Arquitetural — COD-005 Registrado

## 1. Autoridade

Este documento governa a sequência global de evolução arquitetural do GKR. O estado transversal vigente é declarado pelo [Current State Register](project/current-state-register.md).

Roadmaps anteriores permanecem no histórico e não substituem esta sequência.

## 2. Estado atual

| Elemento | Estado |
|---|---|
| Era | `GE-2 — Knowledge` |
| Marco | `M7.7` |
| Remediação R1–R5 | concluída; `PASS` |
| R6 | concluído |
| A2-R03 | ativa em execução |
| BA-STR-002 | ativo |
| COR | 16 `Under Validation`; 1 `Merged`; 1 `Rejected` |
| CODR | `5 de 18` decisões; 0 submissões abertas |
| COD-001 | `Reformulate` aceito para ECO-CAND-001 |
| COD-002 | `Reformulate` aceito para ECO-CAND-003 |
| COD-003 | `Merge into ECO-CAND-003` aceito para ECO-CAND-005 |
| COD-004 | `Reformulate` aceito para ECO-CAND-002 |
| COD-005 | `Reject` aceito para ECO-CAND-004 |
| Outcomes canônicos | `0` |
| Product Engineering | pausado antes do `W0-01` |

## 3. Sequência já executada

### 3.1 Guivos Journey

Concluído funcionalmente e publicado em `PAS-001 1.0.0 active`, com nove capacidades concluídas e implementação pausada.

### 3.2 Guivos Economic Model

Arquitetura documental inicial concluída em `GEM-001` a `GEM-010`. Parâmetros reais e validações especializadas permanecem pendentes.

### 3.3 Remediação e retomada

```text
R1 — precedência e estado global — concluído
→ R2 — roadmap e backlog — concluído
→ R3 — controles centrais — concluído
→ R4 — navegação — concluído
→ R5 — validação mecânica — PASS
→ R6 — retomada governada — concluído
```

## 4. Business Outcomes — frente ativa

Estado:

- COR: 18 registros rastreáveis;
- validação externa: 6 de 6 lotes;
- COEM: 18 de 18 candidatos e 6 de 6 clusters;
- decisões humanas: 5 de 18;
- `ECO-CAND-005`: `Merged into ECO-CAND-003`;
- `ECO-CAND-002`: `Reformulate` aceito e pendente de nova COEM;
- `ECO-CAND-004`: `Rejected` por `COD-005`;
- experiência preservada na Jornada e como fonte de evidências;
- Outcomes canônicos: 0.

## 5. Resultado de COD-005

A recomendação `Reject` foi aceita para `ECO-CAND-004 — Realização de experiências de valor`.

A rejeição não remove experiência da Guivos. Ela impede somente que um episódio de jornada seja promovido como Outcome permanente independente.

O conceito permanece como:

- unidade da arquitetura da Jornada;
- realização de valor em uso;
- fonte de evidências para Outcomes;
- referência para capacidades e métricas futuras.

## 6. Sequência restante de BA-STR-002

1. submeter `ECO-CAND-006` à decisão humana sobre `Reformulate`;
2. concluir as doze decisões posteriores;
3. reavaliar formulações reformuladas e combinadas pelos quatro testes;
4. aplicar e ajustar o `AQS-O01`;
5. consolidar os catálogos de Ecosystem Outcomes e Business Outcomes;
6. construir a matriz canônica de sustentação.

## 7. Business Capabilities

Após a conclusão governada dos Outcomes:

1. desenvolver `BA-CAP-001 — Core Business Capabilities`;
2. desenvolver `BA-CAP-002 — Capability Map`;
3. confirmar dependências, ownership e fronteiras;
4. rebaselinear o portfólio especializado.

## 8. Portfólio e frentes posteriores

A ordem histórica de referência permanece:

1. Guivos Mall;
2. Guivos Business;
3. Guivos Intelligence;
4. Guivos Ads;
5. Guivos Media;
6. Guivos Travel;
7. Commercial Model;
8. Go-to-Market.

Essa ordem não autoriza início. Product Engineering somente poderá ser retomado por decisão explícita posterior.

## 9. Market Validation

Permanece como trilha operacional paralela e pode avançar por incremento próprio, sem alterar automaticamente Outcomes ou Economic Model.

## 10. Próximo ponto exato

Preparar e submeter `ECO-CAND-006 — Conexões relevantes e fortalecedoras` à sexta decisão humana individual. Nenhuma reformulação será registrada antes da manifestação explícita do Fundador.
