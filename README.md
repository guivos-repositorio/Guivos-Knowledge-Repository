# Guivos Knowledge Repository (GKR)

O Guivos Knowledge Repository é a fonte oficial, versionada e governada do conhecimento da Guivos. Ele reúne fundamentos, arquiteturas, modelos, decisões, especificações e o histórico de evolução do ecossistema.

## Estado vigente proposto — patch 2.27.1

A autoridade transversal é o [Registro do Estado Atual](docs/project/current-state-register.md).

| Elemento | Estado resumido |
|---|---|
| Registro do Estado Atual | `GKR-STATE-001` **2.27.1** |
| Era | GE-2 — Knowledge |
| Marco | **M7.88** — saída consciente para fronteira externa validada |
| Última frente proposta | **UXA-101** |
| Patch documental | taxonomia global de planos + separação Organização/Guivos Business |
| Galeria visual | `active` 0.21.0; 118 SVGs |
| Matriz por SVG | `active` 0.17.0; 118 SVGs / 31 perfis |
| Validações funcionais vigentes | **118** |
| Pendentes de validação específica | **0** |
| Superfícies/estados/fronteiras | **53** |
| Transições documentais | **54** |
| IDs com referência visual | **42 de 53** |
| Responsabilidades sem SVG dedicado | 9 |
| Fronteiras sem tela | 2 |
| Engenharia de Produto | pausada antes de W0-01 |
| Resultados Empresariais canônicos | 0 |
| Próxima UXA | **UXA-102 não iniciada** |

A UXA-101 continua encerrando V4 no limite controlável pela Guivos. O patch 2.27.1 não cria nova UXA nem promove maturidade: sincroniza os planos `Pessoa: Free/Plus/Pro`, `Coletivo: Livre/Mobiliza/Impacta/Rede`, `Organização: Conecta/Eleva/Transforma` e registra `Guivos Business: Start/Growth/Scale/Enterprise` como produto especializado, sem preço ou entitlement novo.

Regra estrutural: **Organização Transforma ≠ Guivos Business Enterprise**.

## Navegação essencial

- [Registro do Estado Atual](docs/project/current-state-register.md)
- [Índice UXA-047 a UXA-101](docs/experience-architecture/uxa-047-101-index.md)
- [Arquitetura da Experiência](docs/experience-architecture/index.md)
- [UXA-101 — Saída Consciente para Fronteira Externa](docs/experience-architecture/uxa-101-conscious-external-boundary-validation.md)
- [UXA-100 — Planos, Cobrança e Pagamentos](docs/experience-architecture/uxa-100-plans-billing-payments-functional-program-and-initial-materialization.md)
- [Galeria Canônica de Planos](docs/journeys/screen-gallery-plans-billing.md)
- [Jornadas Integradas](docs/journeys/index.md)
- [Galeria Visual Integrada](docs/journeys/screen-gallery.md)
- [Registro Granular de Transições](docs/journeys/transition-registry.md)
- [Roadmap Arquitetural](docs/roadmap.md)
- [Índice de changelogs](docs/project/changelog-index.md)

## Regras de autoridade

- `GKR-STATE-001` prevalece sobre resumos e superfícies derivadas após integração do incremento correspondente.
- Materialização, validação, promoção e implementação são estados distintos.
- Uma versão visual reformulada exige revalidação quando altera comportamento; sincronização taxonômica sem mudança funcional preserva a validação declarada quando documentada pela auditoria.
- Publicação ou ativação não equivale a distribuição garantida.
- Relação comercial e plano pago não alteram relevância funcional.
- Plano representa capacidade/profundidade/complexidade atendida, não valor ou nível de evolução do participante.
- Oportunidade pública não é ocultada para vender plano.
- Fronteira externa não é tela da Guivos e validação até a fronteira não valida o sistema de terceiro.
- `BND-002` representa contratação/dimensionamento assistido quando necessário; não é sinônimo de Enterprise, Scale, Rede ou Transforma.
- Organização e Guivos Business são estruturas distintas.
- Estado canônico vigente prevalece sobre estado visual obsoleto.
- Nenhum pacote posterior, UXA ou etapa de Engenharia de Produto começa automaticamente.
- Alterações permanentes exigem branch, validação, pull request e decisão governada.

## Validação

Os controles oficiais incluem front matter, identificadores, links, navegação, whitespace, construção MkDocs em modo estrito, árvore rastreada limpa e sincronização semântica das superfícies globais.
