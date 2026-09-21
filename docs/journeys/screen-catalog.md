---
id: GKR-JOURNEY-SCREEN-CATALOG-001
title: Catálogo Integrado de Telas
status: active
version: 0.39.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-20
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
| Comercial | Opportunity Boost e superfícies patrocinadas |
| Fronteiras | transferência de autoridade para processos externos |

## 3. Autoridade granular

O inventário detalhado corrente está em:

- [Registro de Superfícies e Estados](surface-registry.md);
- [Registro de Transições](transition-registry.md);
- detalhes de [Pessoa](surface-registry-person-details.md);
- detalhes de [Coletivo](surface-registry-collective-details.md);
- detalhes de [Organização](surface-registry-organization-details.md);
- detalhes de [fronteiras comerciais](surface-registry-commercial-boundary-details.md).

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
