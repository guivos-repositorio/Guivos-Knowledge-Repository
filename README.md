# Guivos Knowledge Repository (GKR)

O Guivos Knowledge Repository é a fonte oficial, versionada e governada do conhecimento da Guivos. Ele reúne fundamentos, arquiteturas, modelos, decisões, especificações e o histórico de evolução do ecossistema.

## Estado vigente proposto pela UXA-094

A autoridade transversal é o [Registro do Estado Atual](docs/project/current-state-register.md).

| Elemento | Estado resumido |
|---|---|
| Registro do Estado Atual | `GKR-STATE-001` 2.20.0 |
| Era | GE-2 — Knowledge |
| Marco | M7.81 — Central de Atualizações e TRN-110 validadas |
| Última frente proposta | UXA-094 |
| Galeria visual | `active` 0.13.0; 107 SVGs |
| Matriz por SVG | `active` 0.11.0; 107 SVGs / 27 perfis |
| Validações funcionais vigentes | **97** |
| Pendentes de validação específica | **10, exclusivamente UXA-055** |
| Handoffs integralmente validados em Coletivos | **7** |
| IDs com referência visual | 29 de 40 |
| Responsabilidades sem SVG dedicado | 10 |
| Engenharia de Produto | pausada antes de W0-01 |
| Resultados Empresariais canônicos | 0 |
| Próxima frente após eventual integração | UXA-095, não iniciada |

A UXA-094 reforma os SVGs correntes de `PER-106 — Meus Coletivos` e `PER-107 — Central de Atualizações`, valida a Central e fecha `GKR-TRN-110` como continuidade integralmente validada. `GKR-TRN-111` permanece ausente porque `PER-108 — Início do Participante` ainda não possui materialização vigente.

## Navegação essencial

- [Registro do Estado Atual](docs/project/current-state-register.md)
- [Índice UXA-047 a UXA-094](docs/experience-architecture/uxa-047-094-index.md)
- [Arquitetura da Experiência](docs/experience-architecture/index.md)
- [UXA-094 — Validação da Central e TRN-110](docs/experience-architecture/uxa-094-collective-updates-center-functional-validation-and-trn110-revalidation.md)
- [Jornadas Integradas](docs/journeys/index.md)
- [Galeria Visual Integrada](docs/journeys/screen-gallery.md)
- [Registro Granular de Transições](docs/journeys/transition-registry.md)
- [Roadmap Arquitetural](docs/roadmap.md)
- [Índice de changelogs](docs/project/changelog-index.md)

## Regras de autoridade

- `GKR-STATE-001` prevalece sobre resumos e superfícies derivadas.
- Materialização não equivale a validação funcional.
- Uma versão visual reformulada exige revalidação.
- Dois endpoints materializados não validam automaticamente a ligação.
- Estado `lido` não equivale a consentimento, concordância, presença ou ação concluída.
- Ações substantivas revalidam o estado canônico antes do efeito.
- Repetição de abertura/leitura não pode duplicar efeito lógico.
- Validação integral documental não equivale a implementação técnica.
- Nenhum pacote posterior, UXA ou etapa de Engenharia de Produto começa automaticamente.
- Alterações permanentes exigem branch, validação, pull request e decisão governada.

## Validação

Os controles oficiais incluem front matter, identificadores, links, navegação, whitespace, construção MkDocs em modo estrito, árvore rastreada limpa e sincronização semântica das superfícies globais.
