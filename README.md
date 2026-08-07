# Guivos Knowledge Repository (GKR)

O Guivos Knowledge Repository é a fonte oficial, versionada e governada do conhecimento da Guivos. Ele reúne fundamentos, arquiteturas, modelos, decisões, especificações e o histórico de evolução do ecossistema.

## Estado vigente proposto pela UXA-095

A autoridade transversal é o [Registro do Estado Atual](docs/project/current-state-register.md).

| Elemento | Estado resumido |
|---|---|
| Registro do Estado Atual | `GKR-STATE-001` 2.21.0 |
| Era | GE-2 — Knowledge |
| Marco | M7.82 — Início do Participante materializado; TRN-111 parcial |
| Última frente proposta | UXA-095 |
| Galeria visual | `active` 0.14.0; 108 SVGs |
| Matriz por SVG | `active` 0.12.0; 108 SVGs / 28 perfis |
| Validações funcionais vigentes | **96** |
| Pendentes de validação específica | **12: 10 UXA-055 + PER-107 corrente + PER-108** |
| Handoffs integralmente validados em Coletivos | **7** |
| IDs com referência visual | 30 de 40 |
| Responsabilidades sem SVG dedicado | 9 |
| Engenharia de Produto | pausada antes de W0-01 |
| Resultados Empresariais canônicos | 0 |
| Próxima frente após eventual integração | UXA-096, não iniciada |

A UXA-095 materializa `PER-108 — Início do Participante` e reforma minimamente `PER-107 — Central de Atualizações` para tornar `GKR-TRN-111` observável. A ligação passa a parcial; nenhuma validação da nova superfície, do SVG reformulado ou do handoff é inferida.

## Navegação essencial

- [Registro do Estado Atual](docs/project/current-state-register.md)
- [Índice UXA-047 a UXA-095](docs/experience-architecture/uxa-047-095-index.md)
- [Arquitetura da Experiência](docs/experience-architecture/index.md)
- [UXA-095 — Início do Participante e TRN-111](docs/experience-architecture/uxa-095-participant-home-materialization-and-trn111-refinement.md)
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
- Vínculo, disponibilidade, função, presença e autoridade são estados distintos.
- Estado `lido` não equivale a consentimento, concordância, presença ou ação concluída.
- Validação integral documental não equivale a implementação técnica.
- Nenhum pacote posterior, UXA ou etapa de Engenharia de Produto começa automaticamente.
- Alterações permanentes exigem branch, validação, pull request e decisão governada.

## Validação

Os controles oficiais incluem front matter, identificadores, links, navegação, whitespace, construção MkDocs em modo estrito, árvore rastreada limpa e sincronização semântica das superfícies globais.
