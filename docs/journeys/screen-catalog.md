---
id: GKR-JOURNEY-SCREEN-CATALOG-001
title: Catálogo Integrado de Telas
status: active
version: 0.40.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-21
related:
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001
  - GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001
normative: false
---

# Catálogo Integrado de Telas

## 1. Função

Este catálogo organiza as responsabilidades funcionais correntes que podem exigir expressão visual durante Design e prototipação.

Os contextos de experiência tratados como eixos principais são **Pessoa, Coletivo, Organização e Business**. Ads / Opportunity Boost e fronteiras aparecem somente quando necessários como capacidades, integrações ou limites transversais; não formam um contexto "Comercial".

```text
RESPONSIBILITY
≠ FINAL SCREEN COUNT
≠ FINAL COMPONENT COUNT
≠ IMPLEMENTATION
```

O número final de telas, estados visuais e componentes pertence à solução de Design, desde que preserve os contratos funcionais.

## 2. Famílias correntes

| Família | Papel |
|---|---|
| Pessoa — entrada e compreensão | entrada protegida, expressão, compreensão e Hoje |
| Pessoa — direção e evolução | Objetivos, Próximos Passos e Evolução |
| Pessoa — oportunidades | Mapa, Lista, Detalhe e saída consciente |
| Pessoa — Coletivos | descoberta, perfil, solicitação, participações e atualizações |
| Coletivo — responsável | visão geral, solicitações, participantes, comunicação e governança |
| Organização | visão geral, oportunidades e relações institucionais |
| Planos | comparação, contratação, gestão e recuperação nos participantes aplicáveis |
| Ads / Opportunity Boost | superfícies patrocinadas, gestão publicitária e controles relacionados |
| Business | Home, ofertas, Planos, configurador, contratação online e implementação/operação |
| Fronteiras | transferência de autoridade para processos externos |

## 3. Autoridade granular

O inventário detalhado corrente está em:

- [Registro de Superfícies e Estados](surface-registry.md);
- [Registro de Transições](transition-registry.md);
- detalhes de [Pessoa](surface-registry-person-details.md);
- detalhes de [Coletivo](surface-registry-collective-details.md);
- detalhes de [Organização](surface-registry-organization-details.md);
- detalhes de [Ads / Opportunity Boost e fronteiras documentais](surface-registry-ads-boundaries-details.md);
- [Experiência Integrada do Guivos Business](business.md) para continuidade própria de Business, sem criação automática de novos IDs de superfície.

## 4. Cobertura visual

```text
GKR VISUAL BASELINE
→ NONE IMPOSED

DESIGNER
→ CREATES VISUAL MATERIALIZATION

CURRENT FUNCTIONAL COVERAGE
→ REGISTRIES

HISTORICAL SVG INVENTORY
→ NOT INPUT
```

## 5. Separações obrigatórias

- Hoje não substitui Objetivos, Próximos Passos ou Evolução;
- Objetivos não é score de produtividade;
- Próximos Passos não é lista coercitiva de tarefas;
- Evolução não é ranking, nota humana ou “roda da vida”;
- abertura de Planos não inicia cobrança;
- Coletivo, Organização e Business preservam papéis distintos;
- fronteira externa não é tela Guivos nem valida processo de terceiro;
- relevância orgânica não é comprada por plano ou patrocínio;
- materialização visual não altera maturidade funcional por si só.

## 6. Estado

```text
CATALOG
→ CURRENT / FUNCTIONAL

VISUAL HISTORY
→ EXCLUDED

PROTOTYPING
→ USE CURRENT REGISTRIES

PRODUCT ENGINEERING
→ SEPARATE
```
