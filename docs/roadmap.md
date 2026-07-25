---
id: ROADMAP-11.69.0
title: Roadmap Arquitetural — BUS-CAND-003 Submetido
status: active
version: 11.69.0
owner: Guivos
last_updated: 2026-07-25
supersedes_partial:
  - ROADMAP-11.68.0
related:
  - GKR-STATE-001
  - GKR-R6-RESUMPTION-001
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - BA-STR-002-COD-SUB-011
  - COD-010
  - M7.12.1
---

# Roadmap Arquitetural — BUS-CAND-003 Submetido

## 1. Autoridade

Este documento governa a sequência global de evolução arquitetural do GKR. O estado transversal vigente é declarado pelo [Current State Register](project/current-state-register.md).

## 2. Estado atual

| Elemento | Estado |
|---|---|
| Era | `GE-2 — Knowledge` |
| Marco | `M7.12.1` |
| Remediação R1–R5 | concluída; `PASS` |
| R6 | concluído |
| A2-R03 | ativa em execução |
| BA-STR-002 | ativo |
| COR | 14 `Under Validation`; 2 `Merged`; 2 `Rejected` |
| CODR | `10 de 18` decisões; 1 submissão aberta |
| Submissão vigente | `BUS-CAND-003 — Reformulate` |
| COD-001 a COD-010 | registrados |
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
- decisões humanas: 10 de 18;
- décima primeira submissão aberta para `BUS-CAND-003`;
- `ECO-CAND-005` e `BUS-CAND-002`: `Merged`;
- `ECO-CAND-004` e `BUS-CAND-001`: `Rejected`;
- formulações revisadas e combinadas permanecem sujeitas a nova COEM;
- Outcomes canônicos: 0.

## 5. Submissão de BUS-CAND-003

A COEM recomenda `Reformulate` para **Habilitação consistente e contextualmente relevante de valor legítimo**.

Formulação originalmente avaliada:

> A Guivos entrega valor legítimo com qualidade, segurança e continuidade suficientes para sustentar experiências relevantes.

Formulação candidata revisada submetida:

> A Guivos sustenta condições para habilitar valor legítimo com consistência e relevância contextual, detectando mudanças materiais e ajustando proposições, capacidades e respostas de forma coerente, sem presumir controle unilateral sobre o valor realizado pelos participantes nem tratar personalização, satisfação pontual, disponibilidade técnica ou velocidade de resposta como prova suficiente.

A reformulação não foi decidida. `BUS-CAND-003` permanece `Under Validation`, e a formulação deverá retornar aos quatro testes da COEM se aceita.

## 6. Sequência restante de BA-STR-002

1. receber a decisão humana sobre `BUS-CAND-003`;
2. concluir as sete decisões posteriores;
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

Receber a manifestação do Fundador sobre `BA-STR-002-COD-SUB-011`. Nenhuma reformulação será registrada como decisão antes dessa manifestação explícita.
