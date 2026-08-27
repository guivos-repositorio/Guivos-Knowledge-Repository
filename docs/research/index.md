---
id: GKR-RES-000
title: Research
status: draft
version: 0.3.0
owner: Guivos Knowledge Repository
last_updated: 2026-08-26
---

# Research

## Definição

Research é o domínio do Guivos Knowledge Repository responsável por reduzir incertezas arquiteturais por meio da construção de entendimento compartilhado, rastreável e interdisciplinar sobre o domínio da Guivos.

Research não cria arquitetura nem substitui a responsabilidade decisória da GEA. Seu papel é produzir evidências, sínteses e modelos explicativos que permitam às arquiteturas da Guivos tomar decisões mais consistentes.

## Princípio central

> A pesquisa reduz incerteza. A arquitetura toma decisões.

## Missão

Construir, validar, preservar e evoluir entendimento compartilhado sobre o domínio da Guivos, utilizando o melhor conhecimento disponível como fundamento para decisões arquiteturais.

## Princípios

### Neutralidade arquitetural

Research não busca confirmar hipóteses previamente aceitas pela Guivos. Seu compromisso é produzir a melhor síntese possível das evidências disponíveis, mesmo quando isso exigir revisar ou rejeitar hipóteses existentes.

### Suficiência arquitetural

A pesquisa deve trabalhar no menor nível de abstração capaz de explicar adequadamente o domínio e apoiar decisões corretas, evitando abstrações universais sem necessidade arquitetural demonstrada.

### Compreensão antes da prescrição

Evidências e referências são meios. O objetivo é construir entendimento suficientemente sólido para explicar o fenômeno, orientar decisões e sustentar modelos arquiteturais.

### Separação de responsabilidades

Research produz conhecimento e recomendações. A arquitetura proprietária decide, consolida e governa a Canon.

## Escopo

O domínio Research pode produzir:

- Research Programs;
- Research Protocols;
- State-of-the-Art Reviews;
- Evidence Registries;
- Phenomena Catalogs;
- Meta-sínteses;
- Explanatory Models;
- Research Reports;
- Architectural Recommendations.

## Relação com a GEA

```mermaid
graph LR
    R[Research] -->|produz entendimento, evidências e sínteses| A[Architecture]
    A -->|toma decisões estruturais| M[Models]
    M --> P[Products and Engineering]
    P --> O[Observed Results]
    O --> R
```

## Limites

Research:

- não define a Canon diretamente;
- não cria novas camadas arquiteturais por conta própria;
- não substitui ADRs, AVs ou ownership arquitetural;
- não conduz investigações filosóficas sem impacto arquitetural concreto;
- não bloqueia a evolução da GEA sem dependência comprovada;
- não mede progresso apenas por volume de documentos ou referências.

## Critérios de maturidade de modelos

Um modelo produzido por Research somente será considerado suficientemente maduro quando demonstrar capacidade de:

1. explicar o fenômeno estudado;
2. orientar decisões arquiteturais;
3. sustentar previsões coerentes dentro dos limites declarados;
4. manter consistência em contextos distintos ou explicitar claramente seus limites de generalização.

## Programas ativos

### RP-001 — Ecosystem Research Program

O [RP-001 — Ecosystem Research Program](RP-001/index.md) investiga quais condições permanentes aparecem repetidamente em ecossistemas complexos capazes de gerar valor sustentável para seus participantes.

Seu objetivo principal é reduzir incertezas para o `BA-STR-002 — Business Outcomes`, preservando Evidence Registry, fenômenos, meta-síntese e recomendações arquiteturais.

### RP-002 — Possibilidades, Oportunidades, Supply e Evidência de Contribuição

O [RP-002 — Possibilidades, Oportunidades, Supply e Evidência de Contribuição](RP-002/index.md) investiga se, uma vez compreendido o Momento de uma Pessoa, existem no mundo caminhos e oportunidades concretas suficientemente relevantes para apoiar sua Journey e como a Guivos pode descobrir, governar, contextualizar e aprender com esse supply sem vender relevância ou fabricar transformação.

O programa consolida:

- Possibilidade × Oportunidade;
- Possibility Patterns e hipóteses contextuais;
- mecanismos;
- corpus real nos nove Domínios de Evolução;
- Direct e Enabling Supply;
- Supply Ecosystems;
- discovery, admission, provenance e freshness;
- Source Coverage e Possibility Gaps;
- papel de Organizações e Coletivos;
- Neutralidade Econômica da Relevância;
- Contribution Intelligence como hipótese;
- diferenciação competitiva da Guivos;
- protocolo de PMF;
- Field Kit e prontidão do piloto;
- registro explícito de claims provadas, convergidas, simuladas e ainda não validadas.

## Regra de maturidade entre programas

Os Research Programs podem produzir conclusões em níveis diferentes de maturidade.

Uma conclusão de Research não deve ser promovida à Canon apenas porque:

- parece conceitualmente correta;
- foi observada em simulação;
- possui exemplo real;
- apresenta forte coerência interna.

Sempre que possível, a promoção deverá preservar evidência, contraexemplos, limites e owner arquitetural responsável.
