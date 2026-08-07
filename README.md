# Guivos Knowledge Repository (GKR)

O Guivos Knowledge Repository é a fonte oficial, versionada e governada do conhecimento da Guivos. Ele reúne fundamentos, arquiteturas, modelos, decisões, especificações e o histórico de evolução do ecossistema.

## Estado vigente proposto pela UXA-093

A autoridade transversal é o [Registro do Estado Atual](docs/project/current-state-register.md).

| Elemento | Estado resumido |
|---|---|
| Registro do Estado Atual | `GKR-STATE-001` 2.19.0 |
| Era | GE-2 — Knowledge |
| Marco | M7.80 — Central de Atualizações materializada; validação funcional e TRN-110 abertas |
| Última frente proposta | UXA-093 |
| Galeria visual | `active` 0.12.0; 107 SVGs |
| Matriz por SVG | `active` 0.10.0; 107 SVGs / 27 perfis |
| Validações funcionais vigentes | 96 |
| Pendentes de validação específica | 11: 10 UXA-055 + PER-107 |
| Handoffs integralmente validados no fluxo de solicitação | 6 |
| IDs com referência visual | 29 de 40 |
| Responsabilidades sem SVG dedicado | 10 |
| Engenharia de Produto | pausada antes de W0-01 |
| Resultados Empresariais canônicos | 0 |
| Próxima frente após eventual integração | UXA-094, não iniciada |

A UXA-093 materializa `GKR-SURF-PER-107 — Central de Atualizações` em um novo SVG móvel P0A, sem alterar ativos previamente validados. `GKR-TRN-110` continua parcial mesmo com ambos os endpoints materializados; `GKR-TRN-111` permanece ausente porque `PER-108 — Início do Participante` ainda não possui materialização vigente. Materialização documental não comprova produto implementado, operação comercial, demanda, receita ou viabilidade.

## Navegação essencial

- [Registro do Estado Atual](docs/project/current-state-register.md)
- [Índice UXA-047 a UXA-093](docs/experience-architecture/uxa-047-093-index.md)
- [Arquitetura da Experiência](docs/experience-architecture/index.md)
- [UXA-093 — Materialização da Central de Atualizações](docs/experience-architecture/uxa-093-collective-updates-center-materialization.md)
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
- Estado `lido` não equivale a consentimento, concordância ou ação concluída.
- Validação integral documental não equivale a implementação técnica.
- Nenhum pacote posterior, UXA ou etapa de Engenharia de Produto começa automaticamente.
- Alterações permanentes exigem branch, validação, pull request e decisão governada.

## Validação

Os controles oficiais incluem front matter, identificadores, links, navegação, whitespace, construção MkDocs em modo estrito, árvore rastreada limpa e sincronização semântica das superfícies globais.
