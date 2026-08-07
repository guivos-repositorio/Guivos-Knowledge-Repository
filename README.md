# Guivos Knowledge Repository (GKR)

O Guivos Knowledge Repository é a fonte oficial, versionada e governada do conhecimento da Guivos. Ele reúne fundamentos, arquiteturas, modelos, decisões, especificações e o histórico de evolução do ecossistema.

## Estado vigente proposto pela UXA-090

A autoridade transversal é o [Registro do Estado Atual](docs/project/current-state-register.md).

| Elemento | Estado resumido |
|---|---|
| Registro do Estado Atual | `GKR-STATE-001` 2.16.0 |
| Era | GE-2 — Knowledge |
| Marco | M7.77 — cinco handoffs de solicitação validados ponta a ponta; continuidade pós-aprovação parcial |
| Última frente proposta | UXA-090 |
| Galeria visual | `active` 0.9.0; 105 SVGs |
| Matriz por SVG | `active` 0.7.0; 105 SVGs / 25 perfis |
| Validações funcionais registradas | 95 |
| Pendentes de validação específica | 10 — exclusivamente UXA-055 |
| Handoffs integralmente validados pela UXA-090 | 5 |
| IDs com referência visual | 27 de 40 |
| Responsabilidades sem SVG dedicado | 12 |
| Engenharia de Produto | pausada antes de W0-01 |
| Resultados Empresariais canônicos | 0 |
| Próxima frente após eventual integração | UXA-091, não iniciada |

A UXA-090 valida integralmente `GKR-TRN-105`, `106`, `107`, `109` e `112`. `GKR-TRN-108` permanece parcial porque `PER-106 — Meus Coletivos` ainda não está materializada e a continuidade pós-aprovação exige refinamento. A validação não comprova produto implementado, operação comercial, demanda, receita ou viabilidade.

## Navegação essencial

- [Registro do Estado Atual](docs/project/current-state-register.md)
- [Índice UXA-047 a UXA-090](docs/experience-architecture/uxa-047-090-index.md)
- [Arquitetura da Experiência](docs/experience-architecture/index.md)
- [UXA-090 — Validação Integrada dos Handoffs de Solicitação](docs/experience-architecture/uxa-090-integrated-collective-request-handoffs-functional-validation.md)
- [Jornadas Integradas](docs/journeys/index.md)
- [Registro Granular de Transições](docs/journeys/transition-registry.md)
- [Roadmap Arquitetural](docs/roadmap.md)
- [Índice de changelogs](docs/project/changelog-index.md)
- [Índice dos adendos canônicos](docs/project/canonical-consolidation-addenda-index.md)

## Regras de autoridade

- `GKR-STATE-001` prevalece sobre resumos e superfícies derivadas.
- Conversas, PDFs e rascunhos externos não criam autoridade por declaração própria.
- Plano, recomendação e desenho não comprovam execução.
- Materialização não equivale a validação funcional.
- Validação de superfície não equivale a validação de transição ou jornada.
- Dois endpoints validados não validam automaticamente a ligação entre eles.
- Validação integral documental não equivale a implementação técnica.
- Estado obsoleto não pode sobrescrever estado canônico mais recente.
- Nenhum pacote posterior, UXA ou etapa de Engenharia de Produto começa automaticamente.
- Alterações permanentes exigem branch, validação, pull request e decisão governada.

## Validação

Os controles oficiais incluem front matter, identificadores, links, navegação, whitespace, construção MkDocs em modo estrito, árvore rastreada limpa e sincronização semântica das superfícies globais.
