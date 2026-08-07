# Guivos Knowledge Repository (GKR)

O Guivos Knowledge Repository é a fonte oficial, versionada e governada do conhecimento da Guivos. Ele reúne fundamentos, arquiteturas, modelos, decisões, especificações e o histórico de evolução do ecossistema.

## Estado vigente proposto pela UXA-088

A autoridade transversal é o [Registro do Estado Atual](docs/project/current-state-register.md).

| Elemento | Estado resumido |
|---|---|
| Registro do Estado Atual | `GKR-STATE-001` 2.14.0 |
| Era | GE-2 — Knowledge |
| Marco | M7.75 — gestão de solicitações do responsável materializada; validação funcional pendente |
| Última frente proposta | UXA-088 |
| Galeria visual | `active` 0.8.0; 105 SVGs |
| Matriz por SVG | `active` 0.6.0; 105 SVGs / 25 perfis |
| Validações funcionais registradas | 88 |
| Pendentes de validação específica | 17 — 10 UXA-055 + 7 UXA-088 |
| IDs com referência visual | 27 de 40 |
| Responsabilidades sem SVG dedicado | 12 |
| Engenharia de Produto | pausada antes de W0-01 |
| Resultados Empresariais canônicos | 0 |
| Próxima frente após eventual integração | UXA-089, não iniciada |

A UXA-088 materializa `GKR-SURF-COL-003` em sete estados desktop. Ela não valida funcionalmente a família, não valida os handoffs ponta a ponta e não comprova produto implementado, operação comercial, demanda, receita ou viabilidade.

## Navegação essencial

- [Registro do Estado Atual](docs/project/current-state-register.md)
- [Índice UXA-047 a UXA-088](docs/experience-architecture/uxa-047-088-index.md)
- [Arquitetura da Experiência](docs/experience-architecture/index.md)
- [UXA-088 — Gestão de Solicitações do Responsável](docs/experience-architecture/uxa-088-collective-request-management-low-fidelity-wireframes.md)
- [Jornadas Integradas](docs/journeys/index.md)
- [Galeria Visual Integrada](docs/journeys/screen-gallery.md)
- [Roadmap Arquitetural](docs/roadmap.md)
- [Índice de changelogs](docs/project/changelog-index.md)
- [Índice dos adendos canônicos](docs/project/canonical-consolidation-addenda-index.md)

## Regras de autoridade

- `GKR-STATE-001` prevalece sobre resumos e superfícies derivadas.
- Conversas, PDFs e rascunhos externos não criam autoridade por declaração própria.
- Plano, recomendação e desenho não comprovam execução.
- Materialização não equivale a validação funcional.
- Validação de superfície não equivale a validação de transição ou jornada.
- Nenhum pacote posterior, UXA ou etapa de Engenharia de Produto começa automaticamente.
- Alterações permanentes exigem branch, validação, pull request e decisão governada.

## Validação

Os controles oficiais incluem front matter, identificadores, links, navegação, whitespace, construção MkDocs em modo estrito, árvore rastreada limpa e sincronização semântica das superfícies globais.
