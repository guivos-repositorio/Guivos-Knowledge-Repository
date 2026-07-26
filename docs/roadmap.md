---
id: ROADMAP-11.82.0
title: Roadmap Arquitetural — COD-017 Registrado
status: active
version: 11.82.0
owner: Guivos
last_updated: 2026-07-25
supersedes_partial:
  - ROADMAP-11.81.0
related:
  - GKR-STATE-001
  - GKR-R6-RESUMPTION-001
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - BA-STR-002-COD-SUB-017
  - COD-017
  - M7.19
---

# Roadmap Arquitetural — COD-017 Registrado

## 1. Autoridade

Este documento governa a sequência global de evolução arquitetural do GKR. O estado transversal vigente é declarado pelo [Current State Register](project/current-state-register.md).

## 2. Estado atual

| Elemento | Estado |
|---|---|
| Era | `GE-2 — Knowledge` |
| Marco | `M7.19` |
| Remediação R1–R5 | concluída; `PASS` |
| R6 | concluído |
| A2-R03 | ativa em execução |
| BA-STR-002 | ativo |
| COR | 10 `Under Validation`; 2 `Merged`; 6 `Rejected` |
| CODR | `17 de 18` decisões; 0 submissões abertas |
| Reformulate aceitos | 9 |
| Merge aceitos | 2 |
| Reject aceitos | 6 |
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

- COR: 18 registros rastreáveis;
- validação externa: 6 de 6 lotes;
- COEM: 18 de 18 candidatos e 6 de 6 clusters;
- decisões humanas: 17 de 18;
- submissões abertas: 0;
- `ECO-CAND-005`: `Merged into ECO-CAND-003`;
- `BUS-CAND-002`: `Merged into BUS-CAND-003`;
- `ECO-CAND-004`, `BUS-CAND-001`, `BUS-CAND-006`, `BUS-CAND-007`, `BUS-CAND-008` e `BUS-CAND-009`: `Rejected`;
- `BUS-CAND-003`, `BUS-CAND-004` e `BUS-CAND-005`: `Reformulate` aceitos;
- Outcomes canônicos: 0.

## 5. Resultado de COD-017

A recomendação `Reject` foi aceita para `BUS-CAND-009 — Coerência global com adequação contextual`.

A decisão retirou o candidato do futuro catálogo de Business Outcomes e preservou **coerência global com adequação contextual** como princípio arquitetural e critério governado para internacionalização, localização, desenho de capacidades e avaliação de mudanças.

A decisão não impõe padronização global, não proíbe adaptação local, não exige internacionalização e não considera tradução, presença local ou variação nominal de produto como prova suficiente de adequação legítima.

## 6. Sequência restante de BA-STR-002

1. submeter `BUS-CAND-010` à decisão humana sobre `Merge into BUS-CAND-005`;
2. reavaliar formulações reformuladas e combinadas pelos quatro testes;
3. aplicar e ajustar o `AQS-O01`;
4. consolidar os catálogos de Ecosystem Outcomes e Business Outcomes;
5. construir a matriz canônica de sustentação.

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

Após integração deste incremento, preparar e submeter `BUS-CAND-010 — Capacidade de reinvestimento responsável` à décima oitava decisão humana individual sobre a recomendação `Merge into BUS-CAND-005`.