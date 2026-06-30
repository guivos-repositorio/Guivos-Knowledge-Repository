# Guivos Knowledge Repository (GKR)

Repositório oficial de conhecimento, arquitetura e decisões da Guivos.

O GKR é a fonte única da verdade para a Guivos Enterprise Architecture (GEA). Ele centraliza fundamentos, modelos, produtos, decisões arquiteturais, glossário, diagramas, governança, pesquisa e publicações derivadas em Markdown, com histórico versionado por Git.

## Status atual

- **Baseline vigente:** M1 — Research Foundation Complete
- **Estado do baseline:** Frozen
- **Fase atual:** M2 — Validation & Refinement
- **Checkpoint ativo:** M2.0 — Architectural Evolution Hypothesis
- **Objetivo imediato:** avaliar o GMM por meio da concepção experimental do GKS, sem promoção à Canon

Consulte:

- [Baseline M1](docs/project/BASELINE-M1.md)
- [Checkpoint M2.0](docs/project/CHECKPOINT-M2.0.md)

## Princípio central

Nenhum conhecimento validado da Guivos deve existir apenas em conversas, apresentações, PDFs, DOCXs ou arquivos isolados.

Toda decisão aprovada deve ser incorporada ao GKR.

> Toda evolução do GKR deve preservar a rastreabilidade entre evidências, modelos explicativos, decisões arquiteturais e implementações.

> Propor, experimentar, observar, avaliar e somente então consolidar.

## Relação entre GEA, GKR e GEB

- **GEA — Guivos Enterprise Architecture:** conjunto integrado das arquiteturas oficiais da Guivos.
- **GKR — Guivos Knowledge Repository:** sistema oficial onde conhecimento, pesquisa, arquitetura e decisões são documentados, versionados e publicados.
- **GEB — Guivos Ecosystem Blueprint:** blueprint principal da Ecosystem Architecture.

## Arquiteturas oficiais

A GEA é composta pelas seguintes arquiteturas:

- Foundation Architecture;
- Ecosystem Architecture;
- Product Architecture;
- Business Architecture;
- Data & Intelligence Architecture;
- Technology Architecture;
- Governance Architecture;
- Knowledge Architecture.

## Hipóteses estruturantes em validação

O `Guivos Meta-Model — GMM` e o `Guivos Knowledge System — GKS` permanecem fora da Canon. O GMM será avaliado por meio do uso do GKS como domínio piloto, conforme os critérios do Checkpoint M2.0.

## Estrutura atual

- `docs/research/` — domínio Research, programas, protocolos, sínteses e recomendações.
- `docs/enterprise-architecture/` — visão geral da GEA.
- `docs/geb/` — Guivos Ecosystem Blueprint.
- `docs/product-architecture/` — arquitetura oficial de produtos.
- `docs/business-architecture/` — arquitetura de negócio da Guivos.
- `docs/governance-framework/` — métodos de governança do GKR.
- `docs/validation/` — validações arquiteturais.
- `docs/adr/` — Architecture Decision Records.
- `docs/glossary.md` — glossário canônico.
- `docs/project/` — baselines, checkpoints, painéis, matriz de consolidação e governança do projeto.
- `docs/roadmap.md` — roadmap arquitetural.
- `docs/assets/` — ativos de publicação.
- `exports/` — publicações derivadas.

## Pipeline de publicação

O fluxo oficial de publicação é:

```text
GitHub -> Markdown -> Mermaid -> Site -> PDF
```

O Markdown versionado no GitHub é a fonte oficial. Site, PDF, apresentações e demais materiais são publicações derivadas.
