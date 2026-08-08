# Guivos Knowledge Repository (GKR)

O Guivos Knowledge Repository é a fonte oficial, versionada e governada do conhecimento da Guivos. Ele reúne fundamentos, arquiteturas, modelos, decisões, especificações e o histórico de evolução do ecossistema.

## Estado vigente

A autoridade transversal é o [Registro do Estado Atual](docs/project/current-state-register.md).

| Elemento | Estado resumido |
|---|---|
| Registro do Estado Atual | `GKR-STATE-001` **2.28.0** |
| Era | GE-2 — Knowledge |
| Marco funcional | **M7.88** — saída consciente para fronteira externa validada |
| Última frente funcional | UXA-101 |
| Sincronização temática | validações recentes integradas em 2026-08-08 |
| Galeria visual | `active` 0.21.0; 118 SVGs |
| Matriz por SVG | `active` 0.17.0; 118 SVGs / 31 perfis |
| Validações funcionais vigentes | **118** |
| Pendentes de validação específica de SVG | **0** |
| Superfícies/estados/fronteiras | **53** |
| Transições documentais | **54** |
| IDs com referência visual | **42 de 53** |
| Responsabilidades sem SVG dedicado | 9 |
| Fronteiras sem tela | 2 |
| Engenharia de Produto | pausada antes de W0-01 |
| Resultados Empresariais canônicos | 0 |
| Próxima UXA | **UXA-102/V5 não iniciada** |

A UXA-101 continua sendo o último marco funcional: `TRN-205` é validada até `BND-001` e qualquer resultado posterior permanece sob autoridade externa.

A sincronização temática de 2026-08-08 integrou nomenclaturas, Neo4j como arquitetura de referência de grafo, rebaseline dos sete Produtos Especializados, governança de marca/naming/ativos digitais, gates de evidência da validação de mercado e o guardrail de propósito antes de incentivos.

## Atualização consolidada

- [Sincronização das Validações Recentes — 2026-08-08](docs/project/validated-updates-synchronization-2026-08-08.md)
- [Baseline Governada de Ressincronização — 2026-08-08](docs/project/repository-resynchronization-baseline-2026-08-08.md)
- [Guivos Go-to-Market, Growth & Capital](docs/go-to-market/index.md)
- [ADR-007 — Neo4j como Tecnologia Primária de Referência para Grafo](docs/adr/ADR-007-neo4j-primary-graph-reference.md)
- [Produtos Especializados — Política de Representação e Handoffs](docs/product-architecture/specialized-products-experience-and-handoff-policy.md)
- [Marca, Naming e Ativos Digitais](docs/governance-framework/brand-and-digital-assets-index.md)
- [VAL-009 — Estado de Execução e Gates de Evidência](docs/research/market-validation/VAL-009-status-de-execucao-e-gates-de-evidencia.md)
- [GEM-005-A1 — Propósito Antes do Incentivo](docs/economic-model/gem-005-a1-purpose-before-incentive-guardrail.md)

## Navegação essencial

- [Registro do Estado Atual](docs/project/current-state-register.md)
- [Índice UXA-047 a UXA-101](docs/experience-architecture/uxa-047-101-index.md)
- [Arquitetura da Experiência](docs/experience-architecture/index.md)
- [Arquitetura de Produtos](docs/product-architecture/index.md)
- [Jornadas Integradas](docs/journeys/index.md)
- [Galeria Visual Integrada](docs/journeys/screen-gallery.md)
- [Registro Granular de Transições](docs/journeys/transition-registry.md)
- [Guivos Economic Model](docs/economic-model/index.md)
- [Validação de Mercado](docs/research/market-validation/README.md)
- [Roadmap Arquitetural](docs/roadmap.md)
- [Índice de changelogs](docs/project/changelog-index.md)

## Regras de autoridade

- `GKR-STATE-001` prevalece sobre resumos e superfícies derivadas.
- A autoridade temática específica e mais recente prevalece dentro de seu domínio.
- Materialização, validação, promoção e implementação são estados distintos.
- Arquitetura de referência não é implantação.
- Publicação ou ativação não equivale a distribuição garantida.
- Relação comercial e plano pago não alteram relevância funcional.
- Oportunidade pública não é ocultada para vender plano.
- Fronteira externa não é tela da Guivos e validação até a fronteira não valida o sistema de terceiro.
- `BND-002` representa contratação/dimensionamento assistido quando o autoatendimento não for suficiente; não é plano Enterprise, Scale ou checkout autônomo.
- Organização e Guivos Business são objetos distintos; Organização usa Conecta · Eleva · Transforma, enquanto Guivos Business possui Start · Growth · Scale · Enterprise.
- Parceria Estratégica é relação corporativa da Guivos enquanto empresa; não é Organização, oportunidade ou quarto participante.
- Pontos, créditos ou recompensas não podem substituir evolução, valor legítimo ou autonomia como objetivo da experiência.
- Estado canônico vigente prevalece sobre estado visual ou nomenclatura obsoleta.
- Nenhum pacote posterior, UXA ou etapa de Engenharia de Produto começa automaticamente.
- Alterações permanentes exigem branch, validação, pull request e decisão governada.

## Limites atuais

Não estão autorizados por esta sincronização:

- UXA-102/V5;
- retomada da Engenharia de Produto;
- implementação/produção Neo4j;
- GraphRAG/GDS/Power BI tratados como implementados sem evidência;
- programa operacional de pontos ou créditos;
- resultado de mercado sem base reproduzível;
- registro marcário, domínio ou proteção territorial sem evidência;
- Fundação Guivos ou estrutura jurídica presumida;
- internacionalização operacional automática;
- cobrança real, gateway ou processo de terceiro após `BND-001`.

## Validação

Os controles oficiais incluem front matter, identificadores, links, navegação, whitespace, construção MkDocs em modo estrito, árvore rastreada limpa, sincronização semântica das superfícies globais e auditoria de nomenclaturas legadas conhecidas.
