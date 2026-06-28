# Guivos Knowledge Repository (GKR)

Repositório oficial de conhecimento, arquitetura e decisões da Guivos.

O GKR é a fonte única da verdade para a Guivos Enterprise Architecture (GEA). Ele centraliza fundamentos, modelos, produtos, decisões arquiteturais, glossário, diagramas, governança e publicações derivadas em Markdown, com histórico versionado por Git.

## Princípio central

Nenhum conhecimento validado da Guivos deve existir apenas em conversas, apresentações, PDFs, DOCXs ou arquivos isolados.

Toda decisão aprovada deve ser incorporada ao GKR.

## Relação entre GEA, GKR e GEB

- **GEA — Guivos Enterprise Architecture:** conjunto integrado das arquiteturas oficiais da Guivos.
- **GKR — Guivos Knowledge Repository:** repositório oficial onde a GEA é documentada, versionada e publicada.
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

## Estrutura atual

- `docs/enterprise-architecture/` — visão geral da GEA.
- `docs/geb/` — Guivos Ecosystem Blueprint.
- `docs/product-architecture/` — arquitetura oficial de produtos.
- `docs/business-architecture/` — arquitetura de negócio da Guivos.
- `docs/adr/` — Architecture Decision Records.
- `docs/glossary.md` — glossário canônico.
- `docs/project/` — painéis, matriz de consolidação e governança do projeto.
- `docs/roadmap.md` — roadmap arquitetural.
- `docs/assets/` — ativos de publicação.
- `exports/` — publicações derivadas.

## Pipeline de publicação

O fluxo oficial de publicação é:

```text
GitHub -> Markdown -> Mermaid -> Site -> PDF
```

O Markdown versionado no GitHub é a fonte oficial. Site, PDF, apresentações e demais materiais são publicações derivadas.
