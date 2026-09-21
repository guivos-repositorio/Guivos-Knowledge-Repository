# Guivos Knowledge Repository (GKR)

O **Guivos Knowledge Repository** é a fonte oficial, versionada e governada do conhecimento vigente da Guivos.

> **O Git preserva a história. O GKR publicado preserva a verdade atual.**

## Leitura obrigatória

Antes de usar qualquer documento isolado, consulte:

- [Estado Atual do Repositório](docs/project/current-state-register.md) — autoridade transversal sobre o que pode ser afirmado hoje;
- [Roadmap](docs/roadmap.md) — sequência governada de evolução;
- [Auditoria Integral do Corpus](docs/project/gkr-full-corpus-audit.md) — instrumento e registro da auditoria integral concluída;
- [Guia Oficial da Guivos](docs/public/guia-oficial-da-guivos.md) — Public Canon vigente.

## Estado semântico sincronizado

A leitura de estado continua subordinada ao [Registro do Estado Atual](docs/project/current-state-register.md). Esta superfície preserva somente os marcadores exigidos de sincronização global:

```text
GKR-STATE-001
→ 3.50.11 / CURRENT

ERA
→ GE-2 — KNOWLEDGE

MARCO FUNCIONAL
→ M7.88

ÚLTIMA UXA FUNCIONAL NUMERADA
→ UXA-101

GIA-COG-001
→ v0.1.1 / ACTIVE / NORMATIVE
→ CURRENT COGNITIVE REFERENCE ARCHITECTURE

PER-002
→ FUNCTIONAL BOUNDARY = GKR-UX-PER002-MAT-ELIGIBILITY-001 v2.0.0 / CURRENT
→ INTERACTIVE DESIGN REFERENCE = GKR-UX-PER002-PROTOTYPE-DELIVERY-001 v1.0.0
→ VALIDATION = GKR-UX-PER002-PROTOTYPE-REVALIDATION-001 v2.0.0 / PASS / 16 OF 16

O/C AUTHENTICATED EXPERIENCE
→ SURFACE MAP = CANONICAL
→ STATE MAP = CANONICAL
→ PRIORITY FLOWS = CANONICAL
→ NAVIGATION MATERIALIZATION = CANONICAL
→ LOW-FIDELITY DELIVERY + VALIDATION = CURRENT / PASS
→ HIGH-FIDELITY ELIGIBILITY = PASS
→ HIGH-FIDELITY DESIGN AUTHORIZATION = GRANTED
→ HIGH-FIDELITY EXECUTION = NOT_STARTED
→ INTERACTIVE PROTOTYPE = NOT_AUTHORIZED

PUBLIC HOMES
→ CANONICAL SOURCE = CURRENT MAIN + GKR-UX-HOMES-DESIGN-DELIVERY-001 v7.0.13
→ DESIGN PRODUCTION READINESS = GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001 v1.3.7 / PASS
→ DESIGN PRODUCTION RELEASE = GRANTED / v1.3.1
→ 8 OF 8 HOMES CURRENT
→ DESIGNER = CREATIVE AUTHOR
→ AI = OPTIONAL / DESIGNER-CONTROLLED
→ SNAPSHOT = NOT REQUIRED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```

## Como navegar

O MENU principal é uma **superfície de descoberta**, não um inventário completo do corpus.

```text
MENU
→ orienta por assunto e função
→ aponta para hubs e autoridades de entrada

CORPUS
→ preserva autoridades, evidências e documentos de detalhe
→ continua acessível por hubs, links internos, busca e Git
```

A ausência de um documento específico no MENU não reduz sua autoridade nem implica remoção do corpus.

```text
NOT_IN_NAV
≠ PRIVATE
≠ DEPRECATED
≠ NON-AUTHORITATIVE

DOCUMENTED
≠ IMPLEMENTED
≠ TESTED
≠ OPERATIONALLY APPROVED
```

## Domínios principais

### Fundação e Marca

- [Fundamentos da Guivos](docs/geb/index.md)
- [Fundamento Cristão](docs/christian-foundation/index.md)
- [Framework de Evolução](docs/evolution-framework/index.md)
- [Marca, Naming e Ativos Digitais](docs/governance-framework/brand-and-digital-assets-index.md)
- [Marca, Fundador e Autoridade Pública](docs/governance-framework/brand-public-authority-and-founder-role.md)

```text
GUIVOS
≠ FUNDADOR

FALA PESSOAL
≠ POSICIONAMENTO INSTITUCIONAL
```

### Participantes

O ecossistema preserva três participantes estruturais:

```text
PESSOA
ORGANIZAÇÃO
COLETIVO
```

Entradas:

- [Pessoa](docs/journeys/person.md)
- [Organização](docs/journeys/organization.md)
- [Coletivo](docs/journeys/collective.md)
- [Organizações e Coletivos — Estado Atual](docs/experience-architecture/organizations-collectives-current-state.md)
- [O/C — Atores, Autoridades e Jobs](docs/experience-architecture/organizations-collectives-authenticated-actors-authorities-and-jobs.md)
- [O/C — Arquitetura da Informação](docs/experience-architecture/organizations-collectives-authenticated-information-architecture.md)
- [O/C — Mapa de Superfícies Autenticadas](docs/experience-architecture/organizations-collectives-authenticated-surface-map.md)
- [O/C — Mapa de Estados Autenticados](docs/experience-architecture/organizations-collectives-authenticated-state-map.md)
- [O/C — Fluxos Prioritários Autenticados](docs/experience-architecture/organizations-collectives-authenticated-priority-flows.md)

### Produtos e Economia

- [Arquitetura de Produtos](docs/product-architecture/index.md)
- [Modelo Econômico](docs/economic-model/index.md)
- [Estratégia de Negócio](docs/business-architecture/index.md)

```text
PARTICIPANTE
≠ PRODUTO ESPECIALIZADO

ORGANIZAÇÃO
≠ GUIVOS BUSINESS
≠ GUIVOS ADS
```

### Experiência e Journey

Contextos principais de experiência:

```text
PESSOA
COLETIVO
ORGANIZAÇÃO
BUSINESS
```

- [Arquitetura da Experiência](docs/experience-architecture/index.md)
- [Jornadas Integradas](docs/journeys/index.md)
- [Jornada da Pessoa](docs/journeys/person.md)
- [Jornada do Coletivo](docs/journeys/collective.md)
- [Jornada da Organização](docs/journeys/organization.md)
- [Guivos Business — Experiência Integrada](docs/journeys/business.md)
- [Home Principal / Pessoa](docs/experience-architecture/public-home-master-document.md)
- [Home de Organizações e Coletivos](docs/experience-architecture/public-home-organizations-collectives-master-document.md)
- [Homes Públicas — Manifesto Corrente de Entrega](docs/experience-architecture/public-homes-design-delivery-manifest.md)
- [PER-002 — Boundary Funcional Corrente](docs/experience-architecture/per-002-materialization-eligibility-and-design-handoff-boundary.md)
- [PER-002 — Protótipo Interativo Corrente](docs/experience-architecture/per-002-interactive-prototype-delivery.md)
- [PER-002 — Validação Corrente do Protótipo Interativo](docs/experience-architecture/per-002-interactive-prototype-post-review-revalidation.md)
- [O/C — Autorização Governada de Wireframes Low-Fidelity](docs/experience-architecture/organizations-collectives-authenticated-wireframe-authorization.md)
- [O/C — Entrega de Wireframes Autenticados Low-Fidelity](docs/experience-architecture/organizations-collectives-authenticated-low-fidelity-wireframe-delivery.md)
- [O/C — Validação Funcional dos Wireframes Autenticados Low-Fidelity](docs/experience-architecture/organizations-collectives-authenticated-low-fidelity-functional-validation.md)
- [O/C — Elegibilidade Pós-Validação para Design High-Fidelity](docs/experience-architecture/organizations-collectives-authenticated-high-fidelity-eligibility.md)
- [O/C — Autorização de Design High-Fidelity](docs/experience-architecture/organizations-collectives-authenticated-high-fidelity-authorization.md)

### Research e Validação

- [Research](docs/research/index.md)
- [Validação de Mercado](docs/research/market-validation/README.md)
- [Pesquisa do Ecossistema](docs/research/RP-001/index.md)
- [Possibilidades, Oportunidades e Supply](docs/research/RP-002/index.md)

```text
MÉTODO DEFINIDO
≠ EVIDÊNCIA REAL
≠ PMF
```

### Dados, Intelligence e Tecnologia

- [Arquitetura Corporativa](docs/enterprise-architecture/index.md)
- [Intelligence e IA](docs/intelligence-architecture/index.md)
- [Neo4j como Tecnologia Primária de Referência](docs/adr/ADR-007-neo4j-primary-graph-reference.md)

```text
REFERENCE_SELECTED
≠ POC
≠ PROVISIONED
≠ INTEGRATED
≠ PRODUCTION

ACTIVE / NORMATIVE REFERENCE ARCHITECTURE
≠ IMPLEMENTATION
≠ OPERATION
≠ PRODUCTION
```

### Jurídico, Privacidade e Institucional

- [Arquitetura Institucional e Jurídica](docs/governance-framework/institutional-and-legal-architecture-index.md)
- [Privacidade e Verdade Operacional](docs/governance-framework/operational-privacy-and-legal-truth-index.md)
- [Fundação Guivos — Conceito e Estado Jurídico](docs/governance-framework/fundacao-guivos-institutional-concept-and-legal-status.md)
- [Proteção Marcária — Autorização de Filing](docs/governance-framework/trademark-brazil-signature-filing-authorization-package.md)

### GTM e Internacionalização

- [Go-to-Market](docs/go-to-market/index.md)
- [Internacionalização e Governança Territorial](docs/go-to-market/gtm-007-internationalization-and-territorial-governance.md)
- [Piloto Portugal — Gates de Prontidão](docs/go-to-market/gtm-008-portugal-pilot-readiness-gates.md)
- [Operações Internacionais e Cross-Border](docs/governance-framework/international-operations-and-cross-border-readiness.md)

```text
ESTRATÉGIA INTERNACIONAL
≠ AUTORIZAÇÃO TERRITORIAL
≠ OPERAÇÃO INTERNACIONAL COMPROVADA
```

### Governança do GKR

- [Auditoria Integral do Corpus](docs/project/gkr-full-corpus-audit.md)
- [Framework de Auditoria Arquitetural](docs/governance-framework/architectural-audit-framework.md)
- [Consolidação do Conhecimento Arquitetural](docs/governance-framework/architectural-knowledge-consolidation-pipeline.md)
- [GKR como Fonte Única da Verdade](docs/adr/ADR-001-gkr-as-source-of-truth.md)
- [Arquitetura de Conhecimento da Guivos](docs/adr/ADR-006-guivos-knowledge-architecture.md)

## Rotas por equipe

As equipes não recebem cópias próprias de autoridades. Elas entram no mesmo corpus por rotas diferentes:

| Necessidade | Entradas recomendadas |
|---|---|
| Liderança / estratégia | Estado Atual · Roadmap · Estratégia de Negócio · Modelo Econômico |
| Marketing / marca | Marca e Ativos Digitais · Guia Oficial · Go-to-Market |
| Publicidade / Ads | Arquitetura de Produtos · Modelo Econômico · Go-to-Market |
| Comercial | Estratégia de Negócio · Produtos · Economia · GTM |

> **Leitura:** a lente documental **Comercial** organiza estratégia, produtos, economia e GTM no repositório. Ela não representa o produto **Guivos Business**, não é tipo de participante e não substitui Pessoa, Coletivo, Organização ou Business como contextos de experiência.
| Produto | Arquitetura de Produtos · Experience Architecture · Jornadas |
| UX / Design | Experience Architecture · Jornadas · PER-002 Handoff · Design Authorization · Design Delivery · Functional Validation · High-Fidelity Eligibility · High-Fidelity Authorization · High-Fidelity Delivery · High-Fidelity Validation · Prototype Eligibility · Prototype Authorization · Prototype Delivery · Post-Review Prototype Revalidation · Estado Atual |
| Desenvolvimento | Produtos · Experience Architecture · Arquitetura Corporativa |
| Dados / Intelligence | Intelligence · Arquitetura Corporativa · Research |
| Research | Research · RP-001 · RP-002 · Privacidade |
| Jurídico / privacidade | Arquitetura Institucional e Jurídica · Verdade Operacional |
| Internacionalização / operação | GTM · Internacionalização · Cross-Border Readiness |

## Guardrail de maturidade

Nenhuma rota de navegação promove o estado de uma frente.

```text
DOCUMENTADO ≠ IMPLEMENTADO ≠ TESTADO ≠ APROVADO OPERACIONALMENTE
HOME DOCUMENTADA ≠ HOME IMPLEMENTADA
SOURCE LOCK ≠ AUTORIZAÇÃO AUTOMÁTICA DE DESIGN
AUDITORIA DOCUMENTAL ≠ EVIDÊNCIA OPERACIONAL
ACTIVE / NORMATIVE REFERENCE ARCHITECTURE ≠ IMPLEMENTATION AUTHORIZATION
DESIGN HANDOFF BOUNDARY ≠ DESIGN AUTHORIZATION
DESIGN AUTHORIZATION ≠ DESIGN DELIVERY ≠ FUNCTIONAL VALIDATION
DESIGN DELIVERY ≠ VISUAL MATURITY PROMOTION
FUNCTIONAL VALIDATION PASS ≠ HIGH-FIDELITY AUTHORIZATION
HIGH-FIDELITY ELIGIBILITY ≠ HIGH-FIDELITY AUTHORIZATION ≠ EXECUTION
HIGH-FIDELITY AUTHORIZATION ≠ HIGH-FIDELITY EXECUTION ≠ PROTOTYPE
HIGH-FIDELITY DELIVERY ≠ HIGH-FIDELITY VALIDATION
HIGH-FIDELITY VALIDATION PASS ≠ PROTOTYPE AUTHORIZATION
PROTOTYPE ELIGIBILITY ≠ PROTOTYPE AUTHORIZATION ≠ PROTOTYPE EXECUTION
PROTOTYPE AUTHORIZATION ≠ PROTOTYPE EXECUTION ≠ PROTOTYPE VALIDATION
PROTOTYPE VALIDATION PRE-REVIEW ≠ CURRENT POST-REVIEW CONCLUSION
O/C SURFACE MAP + STATE MAP + PRIORITY FLOWS DEFINED ≠ MATERIALIZED NAVIGATION ≠ WIREFRAME ≠ UI ≠ IMPLEMENTATION
```

Para qualquer afirmação de estado, prevalece o [Registro do Estado Atual](docs/project/current-state-register.md).