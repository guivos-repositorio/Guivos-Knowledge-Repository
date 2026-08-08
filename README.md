# Guivos Knowledge Repository (GKR)

O Guivos Knowledge Repository é a fonte oficial, versionada e governada do conhecimento da Guivos. Ele reúne fundamentos, arquiteturas, modelos, decisões, especificações e o histórico de evolução do ecossistema.

## Estado vigente proposto pela UXA-099

A autoridade transversal é o [Registro do Estado Atual](docs/project/current-state-register.md).

| Elemento | Estado resumido |
|---|---|
| Registro do Estado Atual | `GKR-STATE-001` 2.25.0 |
| Era | GE-2 — Knowledge |
| Marco | M7.86 — dez estados residuais Opportunity Boost validados |
| Última frente proposta | UXA-099 |
| Galeria visual | `active` 0.17.0; 109 SVGs |
| Matriz por SVG | `active` 0.15.0; 109 SVGs / 28 perfis |
| Validações funcionais vigentes | **109** |
| Pendentes de validação específica | **0** |
| COM-005 | **validado funcionalmente pela UXA-099** |
| TRN-305 | parcial; integração ponta a ponta não promovida |
| TRN-203 / 204 / 210 / 211 | **integralmente validadas** |
| TRN-007 | **integralmente validada** |
| Handoffs integralmente validados em Coletivos | **8** |
| IDs com referência visual | 30 de 40 |
| Responsabilidades sem SVG dedicado | 9 |
| Engenharia de Produto | pausada antes de W0-01 |
| Resultados Empresariais canônicos | 0 |
| Próxima prioridade registrada | V4 — efeito externo de oportunidades; UXA-100 não iniciada |

A UXA-099 encerra as dez pendências específicas da UXA-055. Oito SVGs são aprovados sem alteração e dois são reformulados: falha de atualização material do anunciante e revisão/reversão de preferências. A repetição da mesma intenção é consolidada como idempotente sem definir implementação técnica.

## Navegação essencial

- [Registro do Estado Atual](docs/project/current-state-register.md)
- [Índice UXA-047 a UXA-099](docs/experience-architecture/uxa-047-099-index.md)
- [Arquitetura da Experiência](docs/experience-architecture/index.md)
- [UXA-099 — Estados Residuais do Opportunity Boost](docs/experience-architecture/uxa-099-opportunity-boost-residual-states-functional-validation-and-reformulation.md)
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
- Preferência negativa prevalece sobre entrega contratada.
- Abrir Detalhe não equivale a interesse, inscrição ou evolução.
- Validação integral documental não equivale a implementação técnica.
- Nenhum pacote posterior, UXA ou etapa de Engenharia de Produto começa automaticamente.
- Alterações permanentes exigem branch, validação, pull request e decisão governada.

## Validação

Os controles oficiais incluem front matter, identificadores, links, navegação, whitespace, construção MkDocs em modo estrito, árvore rastreada limpa e sincronização semântica das superfícies globais.
