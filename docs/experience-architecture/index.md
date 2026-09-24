---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 1.24.4
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-24
related:
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-BUSINESS-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-UX-ORGCOL-AUTH-NAV-MAT-001
  - GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001
  - GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001
  - GKR-UX-ORGCOL-AUTH-HIFI-ELIGIBILITY-001
  - GKR-UX-ORGCOL-AUTH-HIFI-AUTH-001
  - GKR-UX-ORGCOL-AUTH-HIFI-EXEC-001
normative: false
---

# Arquitetura da Experiência da Guivos

## 1. Finalidade

Esta seção reúne somente as autoridades correntes necessárias para compreender, criar, prototipar e validar a experiência da Guivos.

```text
CURRENT MAIN
→ PRIMARY SOURCE OF TRUTH

HISTORICAL / CANDIDATE / SNAPSHOT / CHECKPOINT / CLOSED AUDIT
→ NOT DESIGN INPUT
→ NOT AI INPUT

GIT
→ PRESERVES HISTORY
```

## 2. Homes públicas — conjunto corrente

A fonte de entrada é o [Manifesto Canônico de Entrega para Design](public-homes-design-delivery-manifest.md).

Autoridades universais de Design:

- [Handoff Canônico](public-homes-design-handoff.md);
- [Prontidão de Produção de Design](public-homes-design-production-readiness-and-figma-contract.md);
- [Fluxo Operacional](public-homes-design-delivery-operational-flow.md);
- [Design Production Release](public-homes-design-production-release.md).

Autoridade condicional de IA:

- [Source Lock e Contrato de Consumo](public-homes-generative-source-lock-and-prompt-template.md) — somente quando a designer optar por usar IA ou ferramenta generativa.

Roteadores `00 — Leia Primeiro` — não normativos:

- [Pessoa](read-first/public-home-person-read-first.md);
- [Organizações e Coletivos](read-first/public-home-organizations-collectives-read-first.md);
- [Mall](read-first/public-home-mall-read-first.md);
- [Travel](read-first/public-home-travel-read-first.md);
- [Media](read-first/public-home-media-read-first.md);
- [Ads](read-first/public-home-ads-read-first.md);
- [Business](read-first/public-home-business-read-first.md);
- [Intelligence](read-first/public-home-intelligence-read-first.md).

Masters correntes:

- [Pessoa](public-home-master-document.md);
- [Organizações e Coletivos](public-home-organizations-collectives-master-document.md);
- [Mall](public-home-mall-master-document.md);
- [Travel](public-home-travel-master-document.md);
- [Media](public-home-media-master-document.md);
- [Ads](public-home-ads-master-document.md);
- [Business](public-home-business-master-document.md);
- [Intelligence](public-home-intelligence-master-document.md).

Os oito Masters incluem os quadros de consulta rápida dos 83 movimentos. Esses quadros resumem significado e função; não substituem os contratos detalhados.

## 3. Journey — continuidade após as Homes

Para prototipação que atravesse uma Home e entre em experiência autenticada, usar:

- [Jornadas Integradas](../journeys/index.md);
- [Jornada da Pessoa](../journeys/person.md);
- [Jornada do Coletivo](../journeys/collective.md);
- [Jornada da Organização](../journeys/organization.md);
- [Experiência Integrada do Guivos Business](../journeys/business.md);
- [Catálogo Integrado de Telas](../journeys/screen-catalog.md);
- [Registro de Superfícies e Estados](../journeys/surface-registry.md);
- [Registro de Transições](../journeys/transition-registry.md).

### 3.1 Contextos principais de experiência

Para leitura de Experience/Journey, usar quatro contextos principais:

```text
PESSOA
COLETIVO
ORGANIZAÇÃO
BUSINESS
```

A ontologia estrutural continua distinta:

```text
PESSOA / COLETIVO / ORGANIZAÇÃO
→ PARTICIPANTES E CONTEXTOS DE EXPERIÊNCIA

GUIVOS BUSINESS
→ PRODUTO ESPECIALIZADO B2B
→ CONTEXTO PRÓPRIO DE EXPERIÊNCIA
→ NÃO É PARTICIPANTE ESTRUTURAL
```

Não criar um quinto contexto chamado `Comercial`.

```text
COM-*
→ IDS LEGADOS DE ADS / OPPORTUNITY BOOST

BND-*
→ FRONTEIRAS DOCUMENTAIS

ADS / OPPORTUNITY BOOST / BND-*
→ RECORTES AUXILIARES
→ NÃO SUBSTITUEM BUSINESS
```

## 4. Organização e Coletivo autenticados

A cadeia corrente é:

```text
JOBS / AUTORIDADE
→ INFORMATION ARCHITECTURE
→ SURFACE MAP
→ STATE MAP
→ PRIORITY FLOWS
→ NAVIGATION MATERIALIZATION
→ LOW-FIDELITY DELIVERY
→ LOW-FIDELITY VALIDATION
→ HIGH-FIDELITY ELIGIBILITY
→ HIGH-FIDELITY AUTHORIZATION
→ HIGH-FIDELITY EXECUTION RELEASE
```

Essas autoridades governam significado, estados, transições e limites. Elas não impõem identidade visual final.

## 5. Fronteira Design × GKR

```text
GKR
→ significado
→ função
→ narrativa
→ atores e autoridade
→ estados e transições
→ evidência e limites

DESIGNER
→ tipografia
→ paleta
→ imagens
→ ilustração
→ grid
→ composição
→ componentes
→ motion
→ direção visual

AI
→ OPTIONAL / DESIGNER-CONTROLLED
```

## 6. Regra de consumo

Não carregar o corpus inteiro por padrão.

Para cada Home:

```text
4 UNIVERSAL DESIGN AUTHORITIES
+
HOME READ-FIRST
+
HOME MASTER
+
HOME-SPECIFIC CURRENT AUTHORITIES
+
OPTIONAL AI AUTHORITY ONLY WHEN AI IS USED
+
JOURNEY ONLY WHEN THE SOLUTION CROSSES INTO AUTHENTICATED EXPERIENCE
```

Qualquer arquivo fora desse conjunto só deve ser consultado quando uma dúvida concreta exigir autoridade adicional corrente.

## 7. Estado

```text
PUBLIC HOMES
→ READY FOR DESIGN

DESIGNER
→ CREATIVE AUTHOR

AI
→ OPTIONAL

SNAPSHOT REQUIREMENT
→ NONE

HISTORICAL RECONSTRUCTION
→ NOT REQUIRED

O/C HIGH-FIDELITY DESIGN
→ AUTHORIZATION GRANTED
→ EXECUTION RELEASE ISSUED
→ EXTERNAL DELIVERY NOT_RECEIVED

INTERACTIVE PROTOTYPE
→ NOT_AUTHORIZED

PRODUCT ENGINEERING
→ SEPARATE / NOT RELEASED BY THIS INDEX
```
