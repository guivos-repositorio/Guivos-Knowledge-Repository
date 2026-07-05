---
id: ADR-006
title: Guivos Knowledge Architecture as a First-Class Architecture
status: approved
date: 2026-07-04
owner: Guivos
supersedes: null
related:
  - A2-METHOD-001
  - A2-R02-FMEM-001
  - GEF-001
---

# ADR-006 — Guivos Knowledge Architecture as a First-Class Architecture

## Contexto

Durante a evolução do Guivos Knowledge Repository, o GKR deixou de exercer apenas a função de armazenar e publicar documentação arquitetural.

Com a Foundation congelada, o Guia Oficial consolidado, a Intelligence Architecture estruturada e a A2-R02 preparada para execução, tornou-se evidente que a Guivos precisa governar não apenas arquiteturas e produtos, mas também o processo pelo qual conhecimento institucional é descoberto, validado, consolidado, preservado e evoluído.

A partir desse ponto, o conhecimento institucional passa a ser reconhecido como ativo estratégico permanente da Guivos.

## Decisão

A Guivos reconhece oficialmente a **Guivos Knowledge Architecture (GKA)** como uma arquitetura de primeira classe dentro da Guivos Enterprise Architecture.

A GKA será responsável por definir como o conhecimento institucional da Guivos é:

- descoberto;
- estruturado;
- validado;
- consolidado;
- promovido à Canon;
- governado;
- revisado;
- evoluído;
- utilizado para fundamentar arquiteturas, capacidades, produtos e implementações.

A GKA não determina o que é verdadeiro. Ela governa o processo pelo qual o conhecimento institucional é descoberto, validado, consolidado e evoluído.

## Princípio institucional

> Nenhuma arquitetura permanente deverá existir sem conhecimento consolidado que a sustente, e nenhum conhecimento consolidado deverá existir sem evidências rastreáveis que o fundamentem.

## Relação entre realidade, conhecimento e arquitetura

A partir desta decisão, o fluxo institucional de fundamentação da Guivos passa a ser:

```text
Realidade observada
  -> Evidências
  -> Conhecimento consolidado
  -> Canon
  -> Arquiteturas
  -> Capacidades
  -> Produtos
  -> Implementações
  -> Novas evidências
```

A arquitetura deixa de ser ponto de partida e passa a ser consequência de conhecimento consolidado.

## Responsabilidades da GKA

A GKA deverá governar:

- métodos de descoberta;
- princípios de produção de conhecimento;
- modelos de evidência;
- protocolos de pesquisa e análise;
- critérios de validação;
- critérios de promoção à Canon;
- ciclo de vida do conhecimento;
- revisão de conhecimento consolidado;
- rastreabilidade entre evidências, Canon e arquiteturas.

## Não responsabilidades

A GKA não deverá:

- substituir a Foundation;
- substituir a Guivos Enterprise Architecture;
- substituir a Intelligence Architecture;
- criar produtos;
- definir implementação técnica;
- decidir a verdade por autoridade;
- promover hipóteses diretamente à Canon;
- tratar a Canon como verdade absoluta e imutável.

## Canon

A Canon passa a ser entendida como o conjunto oficial de conhecimentos institucionais atualmente mais confiáveis para fundamentar decisões permanentes da Guivos, derivados de evidências rastreáveis e aprovados pelos processos da GKA.

A Canon é estável, mas revisável quando evidências consistentes demonstrarem que deixou de representar adequadamente a realidade observada.

## Consequências

Toda arquitetura permanente deverá demonstrar:

1. de qual conhecimento consolidado deriva;
2. quais evidências sustentam esse conhecimento;
3. como esse conhecimento foi promovido à Canon;
4. quais limites, incertezas ou dependências permanecem.

Essa decisão inaugura a segunda grande era do GKR, orientada à descoberta, validação, consolidação e evolução sistemática do conhecimento institucional.

## Estratégia de implementação

Esta ADR autoriza a existência da GKA.

A criação dos documentos internos da GKA ocorrerá em etapa posterior, preservando a sequência:

```text
Decisão
  -> Marco institucional
  -> Reconhecimento arquitetural
  -> Documentos estruturantes
```

## Estado

A decisão está aprovada.

A GKA está reconhecida como arquitetura de primeira classe, mas sua documentação interna ainda será criada em uma versão posterior do GKR.