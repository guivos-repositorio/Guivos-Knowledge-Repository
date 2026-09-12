# Guivos Knowledge Repository

O GKR é a base oficial do conhecimento vigente da Guivos.

> **Git = histórico. GKR publicado = verdade atual.**

## Comece por aqui

- [Estado Atual do Repositório](project/current-state-register.md) — o que pode ser afirmado hoje;
- [Roadmap](roadmap.md) — sequência governada de evolução;
- [Auditoria Integral do Corpus](project/gkr-full-corpus-audit.md) — registro da auditoria integral concluída e dos gates finais;
- [Guia Oficial da Guivos](public/guia-oficial-da-guivos.md) — Public Canon vigente;
- [Glossário](glossary.md) — vocabulário transversal.

## Estado semântico sincronizado

A leitura de estado continua subordinada ao [Registro do Estado Atual](project/current-state-register.md). Esta superfície preserva somente os marcadores exigidos de sincronização global:

```text
GKR-STATE-001 3.34.1
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
HIGH-FIDELITY DESIGN DELIVERY → EXECUTED / GKR-UX-PER002-HIFI-DELIVERY-001 v0.1.0
HIGH-FIDELITY DESIGN VALIDATION → PASS / GKR-UX-PER002-HIFI-VALIDATION-001 v1.0.0
CURRENT HIGH-FIDELITY DESIGN REFERENCE → DELIVERY v0.1.0 + VALIDATION v1.0.0
INTERACTIVE PROTOTYPE ELIGIBILITY → PASS / GKR-UX-PER002-PROTOTYPE-ELIGIBILITY-001 v1.0.0
INTERACTIVE PROTOTYPE AUTHORIZATION → GRANTED / GKR-UX-PER002-PROTOTYPE-AUTH-001 v1.0.0
INTERACTIVE PROTOTYPE EXECUTION → EXECUTED / GKR-UX-PER002-PROTOTYPE-DELIVERY-001 v0.1.0
ORIGINAL PROTOTYPE VALIDATION → HISTORICAL PRE-REVIEW EVIDENCE / GKR-UX-PER002-PROTOTYPE-VALIDATION-001 v1.0.1 / SUPERSEDED
CODEX PROTOTYPE REVIEW → 2 P2 INTERACTION FINDINGS / REMEDIATED / THREADS RESOLVED
POST-REVIEW PROTOTYPE REVALIDATION → PASS / GKR-UX-PER002-PROTOTYPE-REVALIDATION-001 v1.0.0 / 16 OF 16 / 0 OPEN MATERIAL OR BLOCKING FINDINGS
CURRENT INTERACTIVE DESIGN REFERENCE → DELIVERY v0.1.0 + HISTORICAL VALIDATION v1.0.1 + REVALIDATION v1.0.0
FINAL INTERACTIVE CONCLUSION → POST-REVIEW REVALIDATION PASS
GIA-COG-001 → ACTIVE / NORMATIVE / CURRENT COGNITIVE REFERENCE ARCHITECTURE / v0.1.1
NEXT AUTOMATIC EXECUTION → NONE
SOURCE LOCK → NOT_CREATED / NOT_REQUIRED BY CURRENT EVIDENCE / NOT_AUTHORIZED BY INFERENCE
UXA-102 / V5 → NOT_STARTED
PRODUCT ENGINEERING → PAUSED BEFORE W0-01
```

## Como esta base é organizada

O MENU foi desenhado para descoberta por **assunto e função**, não para reproduzir cada arquivo do corpus.

```text
MENU PRINCIPAL
→ hubs e autoridades de entrada
→ baixa fragmentação
→ rotas compreensíveis por múltiplas equipes

CORPUS COMPLETO
→ autoridades temáticas
→ evidências
→ documentos de detalhe
→ proveniência necessária
```

Um documento pode permanecer vigente sem estar listado diretamente no MENU. A autoridade vem de seu estado, escopo e relações normativas — não de sua posição na navegação.

```text
NOT_IN_NAV
≠ PRIVATE
≠ DEPRECATED
≠ NON-AUTHORITATIVE
```

## Fundação e Marca

- [Fundamentos da Guivos](geb/index.md)
- [Fundamento Cristão](christian-foundation/index.md)
- [Framework de Evolução](evolution-framework/index.md)
- [Marca, Naming e Ativos Digitais](governance-framework/brand-and-digital-assets-index.md)
- [Marca, Fundador e Autoridade Pública](governance-framework/brand-public-authority-and-founder-role.md)

Preservação transversal:

```text
GUIVOS
≠ FUNDADOR

FALA PESSOAL
≠ POSICIONAMENTO INSTITUCIONAL
```

## Participantes

A Guivos reconhece três participantes estruturais:

```text
PESSOA
ORGANIZAÇÃO
COLETIVO
```

Entradas:

- [Pessoa](journeys/person.md)
- [Organização](journeys/organization.md)
- [Coletivo](journeys/collective.md)
- [Organizações e Coletivos — Estado Atual](experience-architecture/organizations-collectives-current-state.md)

```text
PARTICIPANTE ESTRUTURAL
≠ PRODUTO ESPECIALIZADO
```

## Produtos e Economia

- [Arquitetura de Produtos](product-architecture/index.md)
- [Modelo Econômico](economic-model/index.md)
- [Estratégia de Negócio](business-architecture/index.md)

```text
ORGANIZAÇÃO
≠ GUIVOS BUSINESS
≠ GUIVOS ADS
```

## Experiência e Journey

- [Arquitetura da Experiência](experience-architecture/index.md)
- [Jornadas Integradas](journeys/index.md)
- [Home Principal / Pessoa](experience-architecture/public-home-master-document.md)
- [Home de Organizações e Coletivos](experience-architecture/public-home-organizations-collectives-master-document.md)
- [Homes dos Produtos Especializados](experience-architecture/public-specialized-homes-reconciliation.md)
- [PER-002 — Elegibilidade de Materialização e Handoff para Design](experience-architecture/per-002-materialization-eligibility-and-design-handoff-boundary.md)
- [PER-002 — Autorização Governada de Design Low-Fidelity](experience-architecture/per-002-design-authorization.md)
- [PER-002 — Materialização Low-Fidelity Funcional de Design](experience-architecture/per-002-low-fidelity-design-delivery.md)
- [PER-002 — Validação Funcional da Materialização Low-Fidelity](experience-architecture/per-002-low-fidelity-functional-validation.md)
- [PER-002 — Elegibilidade Pós-Validação para Design High-Fidelity](experience-architecture/per-002-high-fidelity-design-eligibility.md)
- [PER-002 — Autorização Governada de Design High-Fidelity](experience-architecture/per-002-high-fidelity-design-authorization.md)
- [PER-002 — Entrega High-Fidelity de Design](experience-architecture/per-002-high-fidelity-design-delivery.md)
- [PER-002 — Validação Governada da Entrega High-Fidelity](experience-architecture/per-002-high-fidelity-design-validation.md)
- [PER-002 — Elegibilidade Pós-Validação para Protótipo Interativo](experience-architecture/per-002-interactive-prototype-eligibility.md)
- [PER-002 — Autorização Governada de Protótipo Interativo](experience-architecture/per-002-interactive-prototype-authorization.md)
- [PER-002 — Entrega do Protótipo Interativo](experience-architecture/per-002-interactive-prototype-delivery.md)
- [PER-002 — Validação Pré-Review do Protótipo Interativo — Evidência Histórica](experience-architecture/per-002-interactive-prototype-validation.md)
- [PER-002 — Revalidação Pós-Review do Protótipo Interativo](experience-architecture/per-002-interactive-prototype-post-review-revalidation.md)

A navegação do repositório não deve ser confundida com a arquitetura de informação de produto, Journey, experiência autenticada ou UI.

```text
REPOSITORY NAVIGATION
≠ PRODUCT INFORMATION ARCHITECTURE
≠ EXPERIENCE NAVIGATION
≠ UI NAVIGATION
```

## Research e Validação

- [Research](research/index.md)
- [Validação de Mercado](research/market-validation/README.md)
- [Pesquisa do Ecossistema](research/RP-001/index.md)
- [Possibilidades, Oportunidades e Supply](research/RP-002/index.md)

```text
MÉTODO DEFINIDO
≠ INSTRUMENTO APLICADO
≠ BASE VÁLIDA
≠ KPI CALCULADO
≠ PMF
```

## Dados, Intelligence e Tecnologia

- [Arquitetura Corporativa](enterprise-architecture/index.md)
- [Intelligence e IA](intelligence-architecture/index.md)
- [Neo4j como Tecnologia Primária de Referência](adr/ADR-007-neo4j-primary-graph-reference.md)

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

## Jurídico, Privacidade e Institucional

- [Arquitetura Institucional e Jurídica](governance-framework/institutional-and-legal-architecture-index.md)
- [Privacidade e Verdade Operacional](governance-framework/operational-privacy-and-legal-truth-index.md)
- [Fundação Guivos — Conceito e Estado Jurídico](governance-framework/fundacao-guivos-institutional-concept-and-legal-status.md)
- [Proteção Marcária — Autorização de Filing](governance-framework/trademark-brazil-signature-filing-authorization-package.md)

```text
CONCEITO INSTITUCIONAL
≠ ENTIDADE CONSTITUÍDA

CLEAR
≠ REGISTRO

FILE
≠ FILING AUTHORIZED
```

## GTM e Internacionalização

- [Go-to-Market](go-to-market/index.md)
- [Internacionalização e Governança Territorial](go-to-market/gtm-007-internationalization-and-territorial-governance.md)
- [Piloto Portugal — Gates de Prontidão](go-to-market/gtm-008-portugal-pilot-readiness-gates.md)
- [Operações Internacionais e Cross-Border](governance-framework/international-operations-and-cross-border-readiness.md)

```text
ESTRATÉGIA INTERNACIONAL
≠ AUTORIZAÇÃO TERRITORIAL
≠ OPERAÇÃO REAL
```

## Governança do GKR

- [Auditoria Integral do Corpus](project/gkr-full-corpus-audit.md)
- [Framework de Auditoria Arquitetural](governance-framework/architectural-audit-framework.md)
- [Consolidação do Conhecimento Arquitetural](governance-framework/architectural-knowledge-consolidation-pipeline.md)
- [GKR como Fonte Única da Verdade](adr/ADR-001-gkr-as-source-of-truth.md)
- [Arquitetura de Conhecimento da Guivos](adr/ADR-006-guivos-knowledge-architecture.md)

## Rotas por equipe

As rotas abaixo são **atalhos de consumo**. Elas não criam cópias, autoridades paralelas ou versões específicas por área.

| Equipe / necessidade | Comece por |
|---|---|
| Liderança / estratégia | [Estado Atual](project/current-state-register.md) · [Roadmap](roadmap.md) · [Estratégia de Negócio](business-architecture/index.md) · [Modelo Econômico](economic-model/index.md) |
| Marketing / marca | [Marca e Ativos Digitais](governance-framework/brand-and-digital-assets-index.md) · [Guia Oficial](public/guia-oficial-da-guivos.md) · [GTM](go-to-market/index.md) |
| Publicidade / Ads | [Produtos](product-architecture/index.md) · [Economia](economic-model/index.md) · [GTM](go-to-market/index.md) |
| Comercial | [Estratégia de Negócio](business-architecture/index.md) · [Produtos](product-architecture/index.md) · [Economia](economic-model/index.md) · [GTM](go-to-market/index.md) |
| Produto | [Produtos](product-architecture/index.md) · [Experience Architecture](experience-architecture/index.md) · [Jornadas](journeys/index.md) |
| UX / Design | [Experience Architecture](experience-architecture/index.md) · [Jornadas](journeys/index.md) · [PER-002 Handoff](experience-architecture/per-002-materialization-eligibility-and-design-handoff-boundary.md) · [Design Authorization](experience-architecture/per-002-design-authorization.md) · [Design Delivery](experience-architecture/per-002-low-fidelity-design-delivery.md) · [Functional Validation](experience-architecture/per-002-low-fidelity-functional-validation.md) · [High-Fidelity Eligibility](experience-architecture/per-002-high-fidelity-design-eligibility.md) · [High-Fidelity Authorization](experience-architecture/per-002-high-fidelity-design-authorization.md) · [High-Fidelity Delivery](experience-architecture/per-002-high-fidelity-design-delivery.md) · [High-Fidelity Validation](experience-architecture/per-002-high-fidelity-design-validation.md) · [Prototype Eligibility](experience-architecture/per-002-interactive-prototype-eligibility.md) · [Prototype Authorization](experience-architecture/per-002-interactive-prototype-authorization.md) · [Prototype Delivery](experience-architecture/per-002-interactive-prototype-delivery.md) · [Historical Prototype Validation](experience-architecture/per-002-interactive-prototype-validation.md) · [Post-Review Prototype Revalidation](experience-architecture/per-002-interactive-prototype-post-review-revalidation.md) · [Estado Atual](project/current-state-register.md) |
| Desenvolvimento | [Produtos](product-architecture/index.md) · [Experience Architecture](experience-architecture/index.md) · [Arquitetura Corporativa](enterprise-architecture/index.md) |
| Dados / Intelligence | [Intelligence](intelligence-architecture/index.md) · [Arquitetura Corporativa](enterprise-architecture/index.md) · [Research](research/index.md) |
| Research | [Research](research/index.md) · [RP-001](research/RP-001/index.md) · [RP-002](research/RP-002/index.md) · [Privacidade](governance-framework/operational-privacy-and-legal-truth-index.md) |
| Jurídico / privacidade | [Arquitetura Institucional e Jurídica](governance-framework/institutional-and-legal-architecture-index.md) · [Verdade Operacional](governance-framework/operational-privacy-and-legal-truth-index.md) |
| Internacionalização / operação | [GTM](go-to-market/index.md) · [Internacionalização](go-to-market/gtm-007-internationalization-and-territorial-governance.md) · [Cross-Border](governance-framework/international-operations-and-cross-border-readiness.md) |

## Regra de maturidade

A navegação não concede maturidade nem autorização de execução.

```text
DOCUMENTED
≠ IMPLEMENTED
≠ TESTED
≠ OPERATIONALLY APPROVED

HOME DOCUMENTADA
≠ HOME IMPLEMENTADA

SOURCE LOCK
≠ AUTORIZAÇÃO AUTOMÁTICA DE DESIGN

ACTIVE / NORMATIVE REFERENCE ARCHITECTURE
≠ IMPLEMENTATION AUTHORIZATION

DESIGN HANDOFF BOUNDARY
≠ DESIGN AUTHORIZATION

DESIGN AUTHORIZATION
≠ DESIGN DELIVERY
≠ FUNCTIONAL VALIDATION

DESIGN DELIVERY
≠ VISUAL MATURITY PROMOTION

FUNCTIONAL VALIDATION PASS
≠ HIGH-FIDELITY AUTHORIZATION

HIGH-FIDELITY ELIGIBILITY
≠ HIGH-FIDELITY AUTHORIZATION
≠ EXECUTION

HIGH-FIDELITY AUTHORIZATION
≠ HIGH-FIDELITY EXECUTION
≠ PROTOTYPE

HIGH-FIDELITY DELIVERY
≠ HIGH-FIDELITY VALIDATION

HIGH-FIDELITY VALIDATION PASS
≠ PROTOTYPE AUTHORIZATION

PROTOTYPE ELIGIBILITY
≠ PROTOTYPE AUTHORIZATION
≠ PROTOTYPE EXECUTION

PROTOTYPE AUTHORIZATION
≠ PROTOTYPE EXECUTION
≠ PROTOTYPE VALIDATION

PROTOTYPE VALIDATION PRE-REVIEW
≠ CURRENT POST-REVIEW CONCLUSION

AUDITORIA DOCUMENTAL
≠ EVIDÊNCIA OPERACIONAL
```

Para qualquer afirmação de estado, prevalece o [Registro do Estado Atual](project/current-state-register.md).