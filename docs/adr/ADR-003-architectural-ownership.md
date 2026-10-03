---
id: ADR-003
title: Architectural Ownership
status: accepted
version: 1.0.0
owner: Guivos Enterprise Architecture
last_updated: 2026-06-28
---

# ADR-003 — Architectural Ownership

## Contexto

A Guivos Enterprise Architecture reúne arquiteturas interdependentes. Sem uma regra explícita de propriedade, um mesmo conceito, modelo, capacidade ou decisão poderia ser definido em mais de um local, gerando duplicidade, conflito e perda de rastreabilidade.

## Decisão

Todo conceito, modelo, capacidade, ativo arquitetural ou decisão canônica da Guivos deve possuir uma única arquitetura proprietária responsável por sua definição, evolução e governança.

As demais arquiteturas podem utilizar, referenciar e depender desse ativo, mas não podem redefini-lo.

## Regras

1. Cada ativo canônico deve declarar sua arquitetura proprietária.
2. Alterações em um ativo devem ocorrer no contexto de sua arquitetura proprietária.
3. Arquiteturas consumidoras devem referenciar a definição oficial.
4. Quando a propriedade não estiver clara, o ativo permanece fora da Canon até decisão formal.
5. Mudanças com impacto transversal devem registrar dependências e, quando necessário, um ADR específico.

## Matriz inicial de propriedade

| Conceito ou ativo | Arquitetura proprietária |
|---|---|
| Essência, propósito, missão, visão e princípios institucionais | Foundation Architecture |
| Participante, jornada, oportunidade, experiência e evidência de evolução | Ecosystem Architecture |
| Produto e portfólio de produtos | Product Architecture |
| Capacidade de negócio, Business Outcome, cadeia de valor e modelo operacional | Business Architecture |
| Dados, analytics, inteligência e modelos de IA | Data & Intelligence Architecture |
| Aplicações, APIs, infraestrutura, segurança e implementação técnica | Technology Architecture |
| ADRs, políticas, riscos e conformidade arquitetural | Governance Architecture |
| Knowledge Units, ciclo de vida e preservação do conhecimento | Knowledge Architecture |

A propriedade formal do conceito institucional de valor será avaliada em revisão futura da Foundation Architecture.

## Consequências positivas

- reduz duplicidade conceitual;
- melhora consistência entre arquiteturas;
- facilita análise de impacto;
- aumenta rastreabilidade;
- define responsabilidade clara pela evolução dos ativos;
- prepara a GEA para futura representação em grafo de conhecimento.

## Consequências e custos

- exige referências explícitas entre arquiteturas;
- pode demandar ADR para transferir propriedade de um ativo;
- requer revisão de documentos antigos que redefinam conceitos externos ao seu domínio.

## Alternativas rejeitadas

### Propriedade compartilhada

Rejeitada por aumentar ambiguidade e dificultar a resolução de conflitos.

### Definições locais em cada arquitetura

Rejeitada por criar versões concorrentes do mesmo conceito.

## Estado

Decisão aceita e aplicável a todos os ativos futuros da GEA.
