# Guivos Knowledge Repository (GKR)

O Guivos Knowledge Repository representa a Guivos em seu estado de maturidade institucional, reunindo sua visão, fundamentos, arquiteturas, modelos, princípios, decisões e patrimônio intelectual em sua capacidade máxima.

O GKR não descreve apenas o estágio atual da implementação. Ele preserva a arquitetura permanente e a arquitetura de referência da organização, enquanto programas e entregas materializam essa visão progressivamente.

## Status atual

- **Baseline vigente:** M1 — Research Foundation Complete
- **Estado do baseline:** Frozen
- **Marco concluído:** A1 — Institutional Architecture Complete
- **Fase ativa:** A2 — Functional Architecture Discovery
- **Entregável ativo:** GCCM-001 — Guivos Core Capability Model
- **Estado do GCCM:** Discovery — nenhuma Core Capability canônica nesta versão
- **Modelo institucional vigente:** GEA-PLM-001 — Permanence Layer Model

Consulte:

- [Architectural Milestones](docs/project/architectural-milestones.md)
- [GCCM-001 — Guivos Core Capability Model](docs/reference-architecture/gccm-001.md)
- [Baseline M1](docs/project/BASELINE-M1.md)
- [Checkpoint M2.0](docs/project/CHECKPOINT-M2.0.md)
- [Permanence Layer Model](docs/enterprise-architecture/permanence-layer-model.md)

## Foco atual

A fase A2 busca descobrir, a partir das evidências já existentes no GKR, o conjunto mínimo e suficiente de capacidades institucionais permanentes da Guivos.

O GCCM não será produzido por brainstorming isolado. O processo deverá:

1. extrair evidências dos ativos existentes;
2. agrupar responsabilidades e verbos semanticamente relacionados;
3. formular capacidades candidatas;
4. aplicar critérios de admissão, destruição, irredutibilidade e cobertura da missão;
5. consolidar somente o que estiver suficientemente demonstrado.

## Princípios centrais

> A Guivos é concebida em sua capacidade máxima. A implementação realiza progressivamente essa visão.

> Todo conteúdo canônico do GKR deve representar a Guivos em seu estado de maturidade institucional, e não apenas seu estágio atual de implementação.

> Quanto maior a permanência de um ativo, menor deve ser sua velocidade de mudança e maior deve ser o rigor aplicado à sua evolução.

> Toda evolução do GKR deve preservar a rastreabilidade entre evidências, modelos explicativos, decisões arquiteturais e implementações.

## Camadas de permanência

| Camada | Horizonte | Finalidade |
|---|---|---|
| Permanent Architecture | Décadas | Preservar identidade, princípios, modelos fundamentais e macroestrutura institucional |
| Reference Architecture | Anos | Definir a melhor forma conhecida de materializar a visão |
| Enterprise Programs | Meses e ciclos plurianuais | Coordenar programas estratégicos que realizam a arquitetura |
| Enterprise Delivery | Dias, semanas e releases | Executar código, infraestrutura, releases e operações |

As camadas superiores orientam as inferiores. Restrições temporárias de implementação não redefinem automaticamente a visão institucional.

## Relação entre GEA, GKR, GEB e GCCM

- **GEA — Guivos Enterprise Architecture:** conjunto integrado das arquiteturas oficiais da Guivos e proprietária do Permanence Layer Model.
- **GKR — Guivos Knowledge Repository:** representação canônica da Guivos em seu estado de maturidade e fonte oficial de suas justificativas arquiteturais.
- **GEB — Guivos Ecosystem Blueprint:** blueprint principal da Ecosystem Architecture.
- **GCCM — Guivos Core Capability Model:** modelo em descoberta que definirá as capacidades institucionais permanentes e reutilizáveis da Guivos.

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

O `Guivos Meta-Model — GMM`, o `Guivos Knowledge System — GKS`, o `Knowledge Validation Framework — GKVF` e os `Knowledge Validation Standards — KVS` permanecem fora da Canon. A fase A2 não promove nenhum desses ativos automaticamente.

## Estrutura atual

- `docs/research/` — domínio Research, programas, protocolos, sínteses e recomendações.
- `docs/enterprise-architecture/` — visão geral da GEA e modelo de camadas de permanência.
- `docs/reference-architecture/` — modelos e arquiteturas de referência, iniciando pelo GCCM.
- `docs/geb/` — Guivos Ecosystem Blueprint.
- `docs/product-architecture/` — arquitetura oficial de produtos.
- `docs/business-architecture/` — arquitetura de negócio da Guivos.
- `docs/governance-framework/` — métodos de governança do GKR.
- `docs/validation/` — validações arquiteturais.
- `docs/adr/` — Architecture Decision Records.
- `docs/glossary.md` — glossário canônico.
- `docs/project/` — baselines, checkpoints, marcos, painéis e governança do projeto.
- `docs/roadmap.md` — roadmap arquitetural.
- `docs/assets/` — ativos de publicação.
- `exports/` — publicações derivadas.

## Pipeline de publicação

O fluxo oficial de publicação é:

```text
GitHub -> Markdown -> Mermaid -> Site -> PDF
```

O Markdown versionado no GitHub é a fonte oficial. Site, PDF, apresentações e demais materiais são publicações derivadas.
