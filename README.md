# Guivos Knowledge Repository (GKR)

O **Guivos Knowledge Repository** é a fonte oficial, versionada e governada do conhecimento vigente da Guivos.

> **O Git preserva a história. O GKR publicado preserva a verdade atual.**

## Leitura obrigatória

Antes de usar qualquer documento isolado, consulte:

- [Estado Atual do Repositório](docs/project/current-state-register.md) — autoridade transversal sobre o que pode ser afirmado hoje;
- [Roadmap](docs/roadmap.md) — sequência governada de evolução;
- [Auditoria Integral do Corpus](docs/project/gkr-full-corpus-audit.md) — instrumento e registro da auditoria integral concluída;
- [Guia Oficial da Guivos](docs/public/index.md) — entrada para o Public Canon.

## Estado semântico sincronizado

A leitura de estado continua subordinada ao [Registro do Estado Atual](docs/project/current-state-register.md). Esta superfície preserva somente os marcadores exigidos de sincronização global:

```text
GKR-STATE-001 3.30.0
M7.88
ÚLTIMA UXA FUNCIONAL NUMERADA → UXA-101
PRÓXIMA UXA → UXA-102 / V5 → NOT_STARTED
LOTE O → DOCUMENTARY AUDIT COMPLETED / F-002 RESOLVED
LOTE P → FINAL COMPLETENESS AUDIT = PASS / COMPLETED
AUDITORIA INTEGRAL → COMPLETED / PASS / 23 OF 23
FINAL BASELINE → CAPTURED @ 15f4d69f63cd760718dce7903224673aac4f540a
Q → FUNCTIONAL DEFINITION = PASS / CANONICALLY CONSOLIDATED
Q MATERIALIZATION ELIGIBILITY → PASS / CANONICALLY CONSOLIDATED
FIRST AUTHENTICATED RESPONSIBILITY → AUTHENTICATED CONTINUATION OF PER-002 — ENTRADA PROTEGIDA
FIRST DISTINCT DOWNSTREAM SURFACE → PER-003 — ESCOLHA DE MODALIDADE
DESIGN HANDOFF BOUNDARY → GKR-UX-PER002-MAT-ELIGIBILITY-001 / FROZEN
PER-002 LOW-FIDELITY DESIGN AUTHORIZATION → GRANTED / GKR-UX-PER002-DESIGN-AUTH-001
PER-002 DESIGN DELIVERY → EXECUTED / GKR-UX-PER002-DESIGN-DELIVERY-001 v0.1.0
DESIGN DELIVERY COVERAGE → 4 PRIMARY FRAMES + 3 VARIANTS / 7 OF 7 AUTHORIZED AREAS
FUNCTIONAL VALIDATION → PASS / GKR-UX-PER002-DESIGN-VALIDATION-001 v1.0.0
CURRENT LOW-FIDELITY DESIGN REFERENCE → DELIVERY v0.1.0 + VALIDATION v1.0.0
HIGH-FIDELITY DESIGN ELIGIBILITY → PASS / GKR-UX-PER002-HIFI-ELIGIBILITY-001 v1.0.0
HIGH-FIDELITY DESIGN AUTHORIZATION → GRANTED / GKR-UX-PER002-HIFI-AUTH-001 v1.0.0
HIGH-FIDELITY DESIGN EXECUTION → NOT_STARTED
PRÓXIMO GATE → PER-002 HIGH-FIDELITY DESIGN EXECUTION / NO PROTOTYPE OR UXA-102 BY INFERENCE
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

- [Arquitetura da Experiência](docs/experience-architecture/index.md)
- [Jornadas Integradas](docs/journeys/index.md)
- [Home Principal / Pessoa](docs/experience-architecture/public-home-master-document.md)
- [Home de Organizações e Coletivos](docs/experience-architecture/public-home-organizations-collectives-master-document.md)
- [Homes dos Produtos Especializados](docs/experience-architecture/public-specialized-homes-reconciliation.md)
- [PER-002 — Elegibilidade de Materialização e Handoff para Design](docs/experience-architecture/per-002-materialization-eligibility-and-design-handoff-boundary.md)
- [PER-002 — Autorização Governada de Design Low-Fidelity](docs/experience-architecture/per-002-design-authorization.md)
- [PER-002 — Materialização Low-Fidelity Funcional de Design](docs/experience-architecture/per-002-low-fidelity-design-delivery.md)
- [PER-002 — Validação Funcional da Materialização Low-Fidelity](docs/experience-architecture/per-002-low-fidelity-functional-validation.md)
- [PER-002 — Elegibilidade Pós-Validação para Design High-Fidelity](docs/experience-architecture/per-002-high-fidelity-design-eligibility.md)
- [PER-002 — Autorização Governada de Design High-Fidelity](docs/experience-architecture/per-002-high-fidelity-design-authorization.md)

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
- [Painel de Conhecimento](docs/project/knowledge-board.md)
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
| Produto | Arquitetura de Produtos · Experience Architecture · Jornadas |
| UX / Design | Experience Architecture · Jornadas · PER-002 Handoff · Design Authorization · Design Delivery · Functional Validation · High-Fidelity Eligibility · High-Fidelity Authorization · Estado Atual |
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
DESIGN HANDOFF BOUNDARY ≠ DESIGN AUTHORIZATION
DESIGN AUTHORIZATION ≠ DESIGN DELIVERY ≠ FUNCTIONAL VALIDATION
DESIGN DELIVERY ≠ VISUAL MATURITY PROMOTION
FUNCTIONAL VALIDATION PASS ≠ HIGH-FIDELITY AUTHORIZATION
HIGH-FIDELITY ELIGIBILITY ≠ HIGH-FIDELITY AUTHORIZATION ≠ EXECUTION
HIGH-FIDELITY AUTHORIZATION ≠ HIGH-FIDELITY EXECUTION ≠ PROTOTYPE
```

Para qualquer afirmação de estado, prevalece o [Registro do Estado Atual](docs/project/current-state-register.md).