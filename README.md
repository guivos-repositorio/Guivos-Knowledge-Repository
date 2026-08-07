# Guivos Knowledge Repository (GKR)

O Guivos Knowledge Repository é a fonte oficial, versionada e governada do conhecimento da Guivos. Ele reúne fundamentos, arquiteturas, modelos, decisões, especificações e o histórico de evolução do ecossistema.

## Estado vigente proposto pela UXA-098

A autoridade transversal é o [Registro do Estado Atual](docs/project/current-state-register.md).

| Elemento | Estado resumido |
|---|---|
| Registro do Estado Atual | `GKR-STATE-001` 2.24.0 |
| Era | GE-2 — Knowledge |
| Marco | M7.85 — publicação, descoberta, Mapa/Lista/Detalhe validados |
| Última frente proposta | UXA-098 |
| Galeria visual | `active` 0.16.0; 109 SVGs |
| Matriz por SVG | `active` 0.14.0; 109 SVGs / 28 perfis |
| Validações funcionais vigentes | **99** |
| Pendentes de validação específica | **10, exclusivamente UXA-055** |
| TRN-203 / 204 / 210 / 211 | **integralmente validadas** |
| TRN-007 | **integralmente validada** |
| Handoffs integralmente validados em Coletivos | **8** |
| IDs com referência visual | 30 de 40 |
| Responsabilidades sem SVG dedicado | 9 |
| Engenharia de Produto | pausada antes de W0-01 |
| Resultados Empresariais canônicos | 0 |
| Próxima prioridade registrada | V3 — dez estados residuais UXA-055; UXA-099 não iniciada |

A UXA-098 valida como conjunto a continuidade `ORG-003 → PER-201 ↔ PER-202 → PER-203`, incluindo as rotas diretas Mapa → Detalhe. Ativação torna a oportunidade elegível à descoberta, mas não garante distribuição, posição, relevância ou recomendação. Nenhum SVG foi criado ou alterado.

## Navegação essencial

- [Registro do Estado Atual](docs/project/current-state-register.md)
- [Índice UXA-047 a UXA-098](docs/experience-architecture/uxa-047-098-index.md)
- [Arquitetura da Experiência](docs/experience-architecture/index.md)
- [UXA-098 — Publicação → Descoberta/Mapa/Lista/Detalhe](docs/experience-architecture/uxa-098-publication-discovery-map-list-detail-integrated-validation.md)
- [Jornadas Integradas](docs/journeys/index.md)
- [Galeria Visual Integrada](docs/journeys/screen-gallery.md)
- [Registro Granular de Transições](docs/journeys/transition-registry.md)
- [Roadmap Arquitetural](docs/roadmap.md)
- [Índice de changelogs](docs/project/changelog-index.md)

## Regras de autoridade

- `GKR-STATE-001` prevalece sobre resumos e superfícies derivadas.
- Materialização não equivale a validação funcional por padrão.
- Uma versão visual reformulada exige revalidação.
- Publicação ou ativação não equivale a distribuição garantida.
- Relação comercial não altera relevância funcional.
- Estado canônico vigente prevalece sobre estado visual obsoleto.
- Abrir Detalhe não equivale a interesse, inscrição ou evolução.
- Validação integral documental não equivale a implementação técnica.
- Nenhum pacote posterior, UXA ou etapa de Engenharia de Produto começa automaticamente.
- Alterações permanentes exigem branch, validação, pull request e decisão governada.

## Validação

Os controles oficiais incluem front matter, identificadores, links, navegação, whitespace, construção MkDocs em modo estrito, árvore rastreada limpa e sincronização semântica das superfícies globais.