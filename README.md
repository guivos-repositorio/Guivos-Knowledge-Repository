# Guivos Knowledge Repository (GKR)

O Guivos Knowledge Repository é a fonte oficial, versionada e governada do conhecimento da Guivos.

## Estado vigente

A autoridade transversal é o [Registro do Estado Atual](docs/project/current-state-register.md).

| Elemento | Estado |
|---|---|
| GKR-STATE-001 | **2.34.0** |
| Era | GE-2 — Knowledge |
| marco funcional | **M7.88** |
| última UXA funcional numerada | **UXA-101** |
| frente não numerada mais recente | **D5-C3 — Objetivos, Próximos Passos e Evolução validados localmente** |
| próxima UXA | **UXA-102/V5 não iniciada** |
| SVGs | **121 — 121 validados / 0 pendentes** |
| associações | **121** |
| perfis | **34** |
| superfícies/estados/fronteiras | **57** |
| transições | **66** |
| Engenharia de Produto | pausada antes de W0-01 |
| programa P0–P9 | consolidado documentalmente após integração de P9 |

O Journey possui baseline canônico de **9 Domínios de Evolução**. D5-A e D5-B materializam esse eixo em superfícies existentes; D5-C1 contratou `PER-010..012` e `TRN-008..013`; D5-C2 materializou um estado-base low-fidelity para as três responsabilidades; D5-C3 valida e reforma localmente esses três SVGs sem promover os handoffs.

## Public Canon

O documento institucional público vigente é o [GOG-001 — Guia Oficial da Guivos 5.0.0](docs/public/guia-oficial-da-guivos.md).

A edição 5.0.0 foi reconciliada com as autoridades de participantes, planos, sete Produtos Especializados, grafo/Neo4j, incentivos, arquitetura institucional, privacidade e internacionalização. D5-C3 permanece autoridade interna de Experience Architecture e não declara disponibilidade pública de produto.

## Autoridades recentes

- [D5-C3 — Validação Funcional de Direção, Movimento e Evolução](docs/experience-architecture/d5-c3-direction-movement-evolution-functional-validation.md)
- [D5-C2 — Materialização Low-Fidelity de Direção, Movimento e Evolução](docs/experience-architecture/d5-c2-direction-movement-evolution-low-fidelity-wireframes.md)
- [D5-C1 — Contrato das Superfícies de Direção, Movimento e Evolução](docs/experience-architecture/d5-c1-direction-movement-evolution-surface-contract.md)
- [D5-B — Domínios de Evolução na Camada de Oportunidades](docs/experience-architecture/d5-b-evolution-domains-opportunities-layer.md)
- [D5-A — Domínios de Evolução na Jornada Inicial](docs/experience-architecture/d5-a-evolution-domains-guided-expression-initial-understanding-today.md)
- [PAS-001-DOMAIN-MODEL-001 — Modelo Canônico dos Domínios de Evolução do Guivos Journey](docs/product-architecture/pas-001-evolution-domains-model.md)
- [Guivos Journey — arquitetura pública e áreas de evolução](docs/product-architecture/journey.md)
- [Consolidação Global e Public Canon — P9](docs/project/p9-global-consolidation-and-public-canon-2026-08-08.md)
- [UXA-100-A4 — Origens Administrativas e Handoffs de Entrada em Planos](docs/experience-architecture/uxa-100-a4-plans-entry-origin-and-navigation-handoffs.md)
- [Matriz de Consolidação Canônica 3.0.0](docs/project/canonical-consolidation-matrix.md)
- [Go-to-Market, Growth & Capital](docs/go-to-market/index.md)
- [GTM-007 — Internacionalização e Programa Territorial](docs/go-to-market/gtm-007-internationalization-and-territorial-governance.md)
- [GTM-008 — Portugal: Gates de Prontidão, Piloto e Escala](docs/go-to-market/gtm-008-portugal-pilot-readiness-gates.md)
- [Arquitetura Institucional, Fundação Guivos e Jurídico](docs/governance-framework/institutional-and-legal-architecture-index.md)
- [Verdade Operacional, Privacidade e Superfícies Legais](docs/governance-framework/operational-privacy-and-legal-truth-index.md)
- [ADR-007 — Neo4j como Tecnologia Primária de Referência](docs/adr/ADR-007-neo4j-primary-graph-reference.md)
- [Produtos Especializados — Política de Handoffs](docs/product-architecture/specialized-products-experience-and-handoff-policy.md)
- [GEM-005-A1 — Propósito Antes do Incentivo](docs/economic-model/gem-005-a1-purpose-before-incentive-guardrail.md)

## Separações canônicas

```text
Pessoa · Coletivo · Organização = participantes
Journey · Mall · Travel · Business · Media · Intelligence · Ads = Produtos Especializados
Organização ≠ Guivos Business
Guivos Mall = nome canônico
Neo4j = tecnologia de referência ≠ produção
Fundação Guivos = conceito ≠ entidade constituída
Portugal = T1_candidate ≠ mercado ativo
aceite contratual ≠ consentimento LGPD ≠ preferência
PER-010..012 validados localmente ≠ continuidade integrada ≠ produto implementado
TRN-008..013 contratadas ≠ continuidade validada
Domínio de Evolução ≠ identidade ≠ score ≠ diagnóstico ≠ prova de evolução
Domínio de Evolução ≠ dimensão estrutural do Contexto Vivo ≠ aspecto descritivo da mudança
```

## Planos

- Pessoa: Free · Plus · Pro;
- Coletivo: Livre · Mobiliza · Impacta · Rede;
- Organização: Conecta · Eleva · Transforma;
- Guivos Business: Start · Growth · Scale · Enterprise.

Plano não representa mérito, prestígio ou nível de evolução.

A origem voluntária de Planos está formalizada por `PER-009 ↔ PER-301`, `COL-002 ↔ COL-301` e `ORG-001 ↔ ORG-301`. A origem da Pessoa ainda não possui SVG dedicado; navegar para Planos não equivale a contratar ou iniciar cobrança.

## Jornada pessoal especializada após D5-C3

A Experience Architecture reconhece:

```text
PER-008 — Hoje
├── TRN-008 → PER-010 — Meus Objetivos → TRN-009 → PER-008
├── TRN-010 → PER-011 — Meus Próximos Passos → TRN-011 → PER-008
└── TRN-012 → PER-012 — Minha Evolução → TRN-013 → PER-008
```

`PER-010..012` possuem um SVG low-fidelity cada e estão **funcionalmente validados localmente pela D5-C3**. As seis transições permanecem `contratadas`; portanto, retorno visual para Hoje não equivale a continuidade integrada validada.

## Domínios de Evolução do Guivos Journey

O baseline canônico inicial do Journey é:

1. Saúde e Bem-estar;
2. Trabalho, Carreira e Estudos;
3. Vida Financeira;
4. Empreendedorismo e Projetos;
5. Relacionamentos e Vida Social;
6. Espiritualidade, Propósito e Valores;
7. Viagens, Lazer, Cultura e Novas Experiências;
8. Causas, Voluntariado e Contribuição;
9. Organização e Equilíbrio da Vida.

`Ainda estou descobrindo` é estado transversal legítimo de exploração, não um décimo domínio. Uma jornada pode envolver vários domínios simultaneamente. A interpretação de cada domínio muda conforme o participante seja Pessoa, Coletivo ou Organização.

A autoridade normativa detalhada, incluindo subáreas, exemplos, relação com as nove capacidades do Journey, uso pela Intelligence, sensibilidade e guardrails, é o [PAS-001-DOMAIN-MODEL-001](docs/product-architecture/pas-001-evolution-domains-model.md).

## Limites atuais

Não estão autorizados ou comprovados apenas pela consolidação documental:

- UXA-102/V5;
- retomada da Engenharia de Produto;
- promoção automática de `TRN-008..013` a continuidade validada;
- implementação/produção Neo4j, GraphRAG ou GDS;
- classificação operacional por IA dos Domínios de Evolução;
- ontologia física de grafo para os Domínios de Evolução;
- PMF ou resultados de pesquisa sem base reproduzível;
- programa operacional de pontos/créditos;
- registro marcário/domínio sem evidência;
- Fundação Guivos juridicamente constituída;
- controles de privacidade/Termos presumidos como operacionais;
- piloto ou mercado ativo em Portugal;
- Porto ou segundo país europeu sem novo gate;
- cobrança real/gateway;
- processo posterior a `BND-002`;
- resultados de terceiros após `BND-001`.

## Navegação

- [Home documental](docs/index.md)
- [Estado Atual](docs/project/current-state-register.md)
- [Roadmap](docs/roadmap.md)
- [Guia Oficial](docs/public/guia-oficial-da-guivos.md)
- [Arquitetura de Produtos](docs/product-architecture/index.md)
- [Guivos Journey](docs/product-architecture/journey.md)
- [Arquitetura da Experiência](docs/experience-architecture/index.md)
- [Jornadas](docs/journeys/index.md)
- [Modelo Econômico](docs/economic-model/index.md)
- [Validação de Mercado](docs/research/market-validation/README.md)
- [Changelogs](docs/project/changelog-index.md)

Alterações permanentes exigem branch, validação, pull request e decisão governada.