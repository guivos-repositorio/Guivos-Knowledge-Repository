---
id: GKR-BASELINE-M1
title: Baseline M1 — Research Foundation Complete
status: frozen
version: 1.0.0
owner: Guivos Knowledge Repository
last_updated: 2026-06-30
---

# Baseline M1 — Research Foundation Complete

## Finalidade

Registrar o primeiro baseline institucional do Guivos Knowledge Repository e estabelecer a referência oficial para a evolução posterior da Guivos Enterprise Architecture.

O Baseline M1 não declara que todo o conteúdo da Guivos está concluído. Ele congela o estado considerado suficientemente coerente para encerrar a fase de construção dos fundamentos e iniciar a fase de validação, refinamento e aplicação.

## Estado

- **Baseline:** M1
- **Nome:** Research Foundation Complete
- **Estado:** Frozen
- **Data:** 30/06/2026
- **Fase seguinte:** M2 — Validation & Refinement

## Escopo incluído

### Foundation Architecture

Estado: `stable`

- Essência;
- Propósito;
- Missão Operacional;
- Visão de Longo Prazo;
- Constituição;
- Princípios Permanentes.

### Ecosystem Architecture / GEB

Estado: `validated`

- KU-FM-001 — Fenômeno da Evolução;
- KU-FM-002 — Modelo Fundamental da Jornada;
- KU-FM-003 — Quatro Naturezas Fundamentais.

Os modelos de Participante, Oportunidade, Experiência, Relacionamentos e Conhecimento do Ecossistema permanecem em evolução.

### Guivos Enterprise Architecture

Estado: `stable` em sua macroestrutura.

Inclui:

- arquiteturas oficiais;
- responsabilidades arquiteturais;
- ownership;
- ordem de dependências;
- governança documental;
- roadmap arquitetural.

### Product Architecture

Estado: `stable` na estrutura superior.

Inclui:

- Guivos Journey;
- Guivos Marketplace, com nome comercial ainda provisório;
- Guivos Travel;
- Guivos Business;
- Guivos Media;
- Guivos Intelligence;
- Guivos Ads.

### Business Architecture

Estado: `validated` em Foundations e Strategy inicial.

Inclui:

- BA-FND-001 — Business Architecture Foundations;
- BA-STR-001 — Business Transformation Model;
- BA-STR-002 — Business Outcomes, ainda em `draft`;
- Outcome Governance Method;
- estruturas previstas para COR, External Validation, COEM e AQS-O01.

### Research

Estado: `stable` em sua estrutura metodológica.

Inclui:

- Research Domain;
- RP-001 — Ecosystem Research Program;
- Research Protocol;
- critérios de qualidade das fontes;
- níveis de evidência;
- Estado da Arte como etapa oficial;
- Evidence Registry;
- Meta-síntese como produto de integração;
- EPC como etapa anterior ao COR;
- Architectural Recommendations.

### RP-001 — Ciclo 1

Estado: `conceptual checkpoint`.

O Ciclo 1 produziu uma síntese preliminar interdisciplinar envolvendo:

1. Systems Thinking;
2. Complex Adaptive Systems;
3. Network Science;
4. Ecologia;
5. Organizational Theory;
6. Service-Dominant Logic;
7. Knowledge Management;
8. Institutional Economics.

Essa síntese foi consolidada na MS-001 em estado `draft`. As evidências bibliográficas ainda deverão ser registradas e auditadas no Evidence Registry antes de qualquer promoção à Canon.

## Ativos explicitamente fora da Canon

Permanecem como hipóteses, possibilidades futuras ou artefatos ainda não validados:

- Sistema Humano de Evolução;
- transformação como fenômeno fundamental;
- mudança de estado como unidade mínima;
- Worldview como elemento autônomo;
- Knowledge-Centric Enterprise;
- Modelo Explicativo Integrado — MEI;
- Enterprise Theory;
- Research Question Map;
- Knowledge Objects;
- Grafo de Conhecimento Arquitetural;
- Knowledge Twin;
- Expected Behaviors;
- Roadmap Epistemológico;
- pipeline de maturidade do conhecimento;
- catálogo definitivo de invariantes.

## Princípio de governança do baseline

> Toda evolução do GKR deve preservar a rastreabilidade entre evidências, modelos explicativos, decisões arquiteturais e implementações.

## Política de mudança

| Classe de mudança | Exemplo | Exigência mínima |
|---|---|---|
| Correção documental | ortografia, link ou formatação | revisão editorial |
| Refinamento conceitual | maior precisão sem alterar a decisão | justificativa registrada |
| Mudança arquitetural | alteração de modelo, ownership ou dependência | ADR |
| Mudança estrutural | Foundation, macroestrutura da GEA ou Research Protocol | ADR e revisão arquitetural |

## Critérios de encerramento do M1

O baseline foi estabelecido porque a fase atingiu:

1. **Consistência:** ausência de conflitos estruturais relevantes conhecidos;
2. **Rastreabilidade:** decisões críticas principais registradas no GKR;
3. **Reprodutibilidade:** outro arquiteto pode compreender o estado atual e continuar o trabalho;
4. **Validabilidade:** hipóteses centrais possuem caminho explícito para futura validação.

## Transição para M2

```mermaid
graph LR
    M1[M1 — Research Foundation Complete] --> M2[M2 — Validation & Refinement]
    M2 --> EV[Evidence Validation]
    EV --> MS[MS-001 Refinement]
    MS --> EPC[Ecosystem Phenomena Catalog]
    EPC --> AR[Architectural Recommendations]
    AR --> COR[Candidate Outcome Register]
```

## Objetivos da Fase M2

- registrar e auditar as fontes do RP-001;
- refinar a MS-001 com evidências rastreáveis;
- testar os mecanismos explicativos candidatos;
- construir o EPC;
- produzir recomendações arquiteturais;
- derivar candidatos a Ecosystem Outcomes;
- iniciar validações empíricas e casos de aplicação.

## Regra histórica

O Baseline M1 deve permanecer como referência histórica. Mudanças futuras não apagam este estado; elas originam novas versões, decisões ou baselines.
