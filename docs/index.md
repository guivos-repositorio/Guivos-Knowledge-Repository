# Guivos Knowledge Repository

O GKR é a fonte oficial, versionada e governada do conhecimento da Guivos.

## Estado vigente

A declaração transversal oficial está no [Registro do Estado Atual](project/current-state-register.md).

| Dimensão | Situação |
|---|---|
| Registro | `GKR-STATE-001` **2.28.0** |
| Era | GE-2 — Knowledge |
| Marco funcional | **M7.88** — saída consciente para fronteira externa validada |
| Última frente funcional | UXA-101 |
| Sincronização temática | validações recentes integradas em 2026-08-08 |
| Galeria visual | `active` 0.21.0; **118 SVGs** |
| Matriz por SVG | `active` 0.17.0; **118 associações e 31 perfis** |
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

A sincronização temática não criou nova UXA nem alterou as contagens funcionais. Ela integra autoridades de nomenclatura, arquitetura de grafo, Produtos Especializados, marca/naming/ativos digitais, evidência de validação de mercado, propósito antes de incentivos, arquitetura institucional/jurídica e verdade operacional/privacidade.

## Atualização consolidada de 2026-08-08

O registro auditável está em [Sincronização das Validações Recentes](project/validated-updates-synchronization-2026-08-08.md).

A atualização incorporou:

- **P1.1 — nomenclaturas legadas:** reconciliação e gate permanente;
- **P2 — grafo:** Neo4j como tecnologia primária de referência, sem afirmar implantação;
- **P8 — Produtos Especializados:** Journey, Mall, Travel, Business, Media, Intelligence e Ads rebaselineados contra as jornadas;
- **P3 — marca/naming/ativos:** governança e modelo de evidência, sem presumir registros ou domínio controlado;
- **P4 — validação de mercado:** gates E0–E7 para separar método, aplicação, base, métricas e decisão;
- **GEM-005-A1:** propósito e evolução prevalecem sobre pontos, créditos e acumulação artificial;
- **P5 — arquitetura institucional/jurídica:** conceito Fundação Guivos, separação entre entidades e gates F0–F9, sem presumir constituição ou operação;
- **P6 — verdade operacional/privacidade:** tratamento, consentimentos, superfícies legais e registros operacionais separados por evidência.

A [Baseline Governada de Ressincronização](project/repository-resynchronization-baseline-2026-08-08.md) preserva o snapshot histórico que classificava P5, P6, P7 e P9 como abertos naquele momento. O estado corrente deve ser lido em conjunto com integrações posteriores e com `GKR-STATE-001`.

## P5 — Arquitetura institucional, Fundação Guivos e jurídico

O P5 integrado está organizado em [Arquitetura Institucional, Fundação Guivos e Jurídico](governance-framework/institutional-and-legal-architecture-index.md).

A regra é preservar estados distintos:

`conceito ≠ forma jurídica ≠ ato constitutivo ≠ registro ≠ infraestrutura operacional ≠ operação real`.

`Fundação Guivos` é tratada neste estágio como conceito institucional social e nome de trabalho. A forma jurídica permanece `unresolved`; registro, CNPJ, governança formal e operação própria não são presumidos.

## P6 — Verdade operacional, privacidade e superfícies legais

O P6 integrado está organizado em [Verdade Operacional, Privacidade, Consentimentos e Superfícies Legais](governance-framework/operational-privacy-and-legal-truth-index.md).

O P6 estabelece três separações essenciais:

- **tratamento de dados:** princípio/desenho ≠ atividade mapeada ≠ base jurídica revisada ≠ implementação ≠ operação evidenciada;
- **manifestação do usuário:** aceite contratual ≠ consentimento LGPD ≠ preferência voluntária;
- **superfícies legais:** draft ≠ revisão jurídica ≠ aprovação ≠ publicação ≠ registro operacional.

O GKR não promove Termos, Política/Aviso de Privacidade, consentimentos, inventário de cookies/SDKs, Encarregado, fluxo de direitos ou processo de incidentes a estado operacional sem evidência específica.

## P7 — Internacionalização e programa territorial

O P7 proposto reconcilia internacionalização com o GTM e está organizado em:

- [Governança de Internacionalização e Programa Territorial](go-to-market/gtm-007-internationalization-and-territorial-governance.md);
- [Portugal — Gates de Prontidão, Piloto e Escala](go-to-market/gtm-008-portugal-pilot-readiness-gates.md);
- [Prontidão Operacional Internacional e Cross-Border](governance-framework/international-operations-and-cross-border-readiness.md).

A sequência continua **Belo Horizonte → São Paulo → Portugal**, com Lisboa como base inicial candidata e Porto posterior mediante gate.

Estado territorial governado de Portugal: `T1_candidate`. Operação, entidade local, equipe, contratos, IVA, pagamentos, suporte e piloto permanecem não evidenciados.

O P7 também registra a decisão mútua de adequação Brasil–União Europeia em proteção de dados vigente em 2026, sem tratá-la como permissão irrestrita de compartilhamento ou como prova de conformidade operacional.

## Go-to-Market, Growth & Capital

A baseline de lançamento, expansão geográfica, aquisição, vendas, captação de Coletivos e Organizações, Guivos Business, Parcerias Estratégicas, metas, receita e valuation está organizada em [Guivos Go-to-Market, Growth & Capital](go-to-market/index.md).

Metas e projeções permanecem classificadas como `candidate_target` ou `scenario` onde aplicável. Run-rate projetado não é receita realizada, pipeline não é faturamento e valuation interno não é oferta nem laudo independente.

## Autoridades temáticas recentes

- [ADR-007 — Neo4j como Tecnologia Primária de Referência para Grafo](adr/ADR-007-neo4j-primary-graph-reference.md)
- [Arquitetura de Referência de Grafo e Inteligência](enterprise-architecture/graph-intelligence-reference-architecture.md)
- [Política de Representação e Handoffs entre Produtos Especializados](product-architecture/specialized-products-experience-and-handoff-policy.md)
- [Matriz de Integração entre Produtos Especializados e Jornadas](product-architecture/specialized-products-journey-integration-matrix.md)
- [Marca, Naming e Ativos Digitais](governance-framework/brand-and-digital-assets-index.md)
- [Arquitetura Institucional e Jurídica](governance-framework/institutional-and-legal-architecture-index.md)
- [Verdade Operacional, Privacidade e Superfícies Legais](governance-framework/operational-privacy-and-legal-truth-index.md)
- [Governança de Internacionalização e Programa Territorial](go-to-market/gtm-007-internationalization-and-territorial-governance.md)
- [Portugal — Gates de Prontidão, Piloto e Escala](go-to-market/gtm-008-portugal-pilot-readiness-gates.md)
- [Prontidão Operacional Internacional e Cross-Border](governance-framework/international-operations-and-cross-border-readiness.md)
- [VAL-009 — Estado de Execução e Gates de Evidência](research/market-validation/VAL-009-status-de-execucao-e-gates-de-evidencia.md)
- [VAL-010 — Contrato de Intake e Registro de Rodadas](research/market-validation/VAL-010-contrato-de-intake-e-registro-de-rodadas.md)
- [GEM-005-A1 — Propósito Antes do Incentivo](economic-model/gem-005-a1-purpose-before-incentive-guardrail.md)

## Acesso rápido

- [Registro do Estado Atual](project/current-state-register.md)
- [Sincronização das Validações Recentes](project/validated-updates-synchronization-2026-08-08.md)
- [Baseline de Ressincronização](project/repository-resynchronization-baseline-2026-08-08.md)
- [Arquitetura Institucional, Fundação Guivos e Jurídico](governance-framework/institutional-and-legal-architecture-index.md)
- [Verdade Operacional, Privacidade e Superfícies Legais](governance-framework/operational-privacy-and-legal-truth-index.md)
- [Prontidão Operacional Internacional e Cross-Border](governance-framework/international-operations-and-cross-border-readiness.md)
- [Go-to-Market, Growth & Capital](go-to-market/index.md)
- [Arquitetura de Produtos](product-architecture/index.md)
- [Arquitetura da Experiência](experience-architecture/index.md)
- [Índice UXA-047 a UXA-101](experience-architecture/uxa-047-101-index.md)
- [Galeria Visual Integrada](journeys/screen-gallery.md)
- [Matriz de Rastreabilidade Visual por SVG](journeys/screen-gallery-traceability-matrix.md)
- [Registro Granular de Transições](journeys/transition-registry.md)
- [Jornadas Integradas](journeys/index.md)
- [Lacunas](journeys/gaps.md)
- [Guivos Economic Model](economic-model/index.md)
- [Validação de Mercado](research/market-validation/README.md)
- [Roadmap Arquitetural](roadmap.md)
- [Índice de changelogs](project/changelog-index.md)

## Limites preservados

Esta superfície não autoriza **UXA-102/V5**, Engenharia de Produto, cobrança real, gateway, programa operacional de pontos/créditos, implantação de Neo4j, dados pessoais em produção no grafo, registro marcário presumido, resultado de pesquisa não evidenciado, Fundação Guivos juridicamente constituída, Política de Privacidade/Termos presumidos, consentimento presumido, internacionalização operacional, entidade/filial portuguesa, IVA/OSS, PSP europeu, equipe local, piloto em Lisboa, expansão para Porto ou qualquer processo de terceiro após `BND-001`.

`TRN-304`, `TRN-305`, `TRN-306`, `TRN-416` e `TRN-426` permanecem parciais. Pessoa, Coletivo e Organização permanecem jornadas `draft`.

Em caso de divergência, prevalecem `GKR-STATE-001` e a autoridade temática específica mais recente.
