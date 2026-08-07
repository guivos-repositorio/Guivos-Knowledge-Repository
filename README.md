# Guivos Knowledge Repository (GKR)

O Guivos Knowledge Repository é a fonte oficial, versionada e governada do conhecimento da Guivos. Ele reúne fundamentos, arquiteturas, modelos, decisões, especificações e o histórico de evolução do ecossistema.

## Estado vigente proposto pela UXA-092

A autoridade transversal é o [Registro do Estado Atual](docs/project/current-state-register.md).

| Elemento | Estado resumido |
|---|---|
| Registro do Estado Atual | `GKR-STATE-001` 2.18.0 |
| Era | GE-2 — Knowledge |
| Marco | M7.79 — Meus Coletivos e continuidade pós-aprovação validadas; Central de Atualizações ausente |
| Última frente proposta | UXA-092 |
| Galeria visual | `active` 0.11.0; 106 SVGs |
| Matriz por SVG | `active` 0.9.0; 106 SVGs / 26 perfis |
| Validações funcionais vigentes | 96 |
| Pendentes de validação específica | 10, exclusivamente UXA-055 |
| Handoffs integralmente validados no fluxo de solicitação | 6 |
| IDs com referência visual | 28 de 40 |
| Responsabilidades sem SVG dedicado | 11 |
| Engenharia de Produto | pausada antes de W0-01 |
| Resultados Empresariais canônicos | 0 |
| Próxima frente após eventual integração | UXA-093, não iniciada |

A UXA-092 reformula e valida `GKR-SURF-PER-106 — Meus Coletivos`, revalida o estado aprovado corrente de `PER-105` e promove `GKR-TRN-108` a integralmente validada. `GKR-TRN-110` continua parcial porque `PER-107 — Central de Atualizações` permanece ausente. A validação documental não comprova produto implementado, operação comercial, demanda, receita ou viabilidade.

## Navegação essencial

- [Registro do Estado Atual](docs/project/current-state-register.md)
- [Índice UXA-047 a UXA-092](docs/experience-architecture/uxa-047-092-index.md)
- [Arquitetura da Experiência](docs/experience-architecture/index.md)
- [UXA-092 — Validação de Meus Coletivos e continuidade pós-aprovação](docs/experience-architecture/uxa-092-my-collectives-functional-validation-and-post-approval-continuity-revalidation.md)
- [Jornadas Integradas](docs/journeys/index.md)
- [Galeria Visual Integrada](docs/journeys/screen-gallery.md)
- [Registro Granular de Transições](docs/journeys/transition-registry.md)
- [Roadmap Arquitetural](docs/roadmap.md)
- [Índice de changelogs](docs/project/changelog-index.md)
- [Índice dos adendos canônicos](docs/project/canonical-consolidation-addenda-index.md)

## Regras de autoridade

- `GKR-STATE-001` prevalece sobre resumos e superfícies derivadas.
- Conversas, PDFs e rascunhos externos não criam autoridade por declaração própria.
- Plano, recomendação e desenho não comprovam execução.
- Materialização não equivale a validação funcional.
- Uma versão visual reformulada exige revalidação.
- Validação de superfície não equivale a validação de transição ou jornada.
- Dois endpoints materializados não validam automaticamente a ligação entre eles.
- Validação integral documental não equivale a implementação técnica.
- Nenhum pacote posterior, UXA ou etapa de Engenharia de Produto começa automaticamente.
- Alterações permanentes exigem branch, validação, pull request e decisão governada.

## Validação

Os controles oficiais incluem front matter, identificadores, links, navegação, whitespace, construção MkDocs em modo estrito, árvore rastreada limpa e sincronização semântica das superfícies globais.
