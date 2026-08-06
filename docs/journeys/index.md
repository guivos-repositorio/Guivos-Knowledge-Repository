---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.9.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
related:
  - UXA-070
  - UXA-071
  - UXA-072
  - UXA-073
  - UXA-074
  - UXA-075
  - UXA-076
  - UXA-077
  - UXA-078
  - UXA-079
  - UXA-080
  - UXA-081
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-SECTION-CLARIFICATION-001
normative: false
---

# Jornadas Integradas

## 1. Finalidade

Esta seção reúne, por referência, as jornadas da **Pessoa**, do **Coletivo** e da **Organização** para permitir leitura contínua, comparação de perspectivas, inspeção visual, análise de handoffs e identificação de lacunas.

Ela não substitui contratos, wireframes, validações ou registros canônicos. Em caso de divergência, prevalece o artefato de origem.

## 2. Como utilizar

1. consulte a [Galeria Visual Integrada de Telas](screen-gallery.md) para comparar os SVGs existentes;
2. use o [Catálogo de telas](screen-catalog.md) para visão agregada;
3. percorra a vista do participante;
4. localize superfícies e transições por ID;
5. confira separadamente maturidade, materialização, validação e continuidade;
6. observe handoffs, retornos e interrupções;
7. consulte as [Lacunas](gaps.md) sem tratá-las como fechadas.

## 3. Vistas disponíveis

- [Galeria Visual Integrada de Telas](screen-gallery.md)
- [Catálogo de telas](screen-catalog.md)
- [Jornada da Pessoa](person.md)
- [Jornada do Coletivo](collective.md)
- [Jornada da Organização](organization.md)
- [Handoffs entre participantes](handoffs.md)
- [Cenários integrados](scenarios.md)
- [Registro Granular de Superfícies e Estados](surface-registry.md)
- [Registro Granular de Transições](transition-registry.md)
- [Lacunas e continuidades ausentes](gaps.md)

## 4. Sequência governada

```text
UXA-070 — programa funcional
→ UXA-071 — materialização da seção
→ UXA-072 — validação não aprovada
→ UXA-073 — reformulação e navegação
→ UXA-074 — revalidação aprovada com ressalvas
→ UXA-075 — promoção seletiva
→ UXA-076 — registros granulares em draft
→ UXA-077 — validação granular não aprovada
→ UXA-078 — correção dos cinco achados
→ UXA-079 — revalidação aprovada com ressalvas
→ UXA-080 — promoção dos instrumentos granulares
→ UXA-081 — galeria visual e auditoria de cobertura
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 5. Estado documental

| Camada | Estado | Referência |
|---|---|---|
| visão geral das Jornadas Integradas | `active` | UXA-075 |
| Pessoa, Coletivo e Organização | `draft` | incompletude explícita |
| handoffs, cenários e catálogo | `active` | UXA-074; UXA-075 |
| registros de superfícies e transições | `active` 0.3.0 | UXA-080 |
| quatro detalhamentos granulares | `active` 0.2.0 | UXA-080 |
| galeria visual integrada | `draft` 0.1.0 | UXA-081 |
| registro de lacunas | `active` | observacional |
| protótipo, aplicação e motor | não iniciados | — |
| Engenharia de Produto | não iniciada | W0-01 |

## 6. Auditoria visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 97 |
| com validação funcional registrada | 87 |
| pendentes de validação específica | 10 |
| IDs com referência visual direta ou agrupada | 25 de 40 |
| responsabilidades sem SVG dedicado | 14 |
| fronteira documental sem tela por definição | 1 |

A quantidade de SVGs não equivale à quantidade de superfícies. Estados alternativos e variações por dispositivo podem compartilhar a mesma responsabilidade granular.

## 7. Domínios preservados

### Coletivos

`GKR-SURF-PER-102` representa exclusivamente Resultados de Busca de Coletivos.

### Oportunidades

- `GKR-SURF-ORG-003` — estado institucional;
- `GKR-SURF-PER-201` — mapa;
- `GKR-SURF-PER-202` — lista;
- `GKR-SURF-PER-203` — detalhe;
- `GKR-SURF-BND-001` — fronteira externa.

### Opportunity Boost

Os dez estados da UXA-055 aparecem na galeria, mas permanecem sem validação funcional específica.

## 8. Regra de leitura

```text
visual existente
≠ decisão visual aprovada
≠ transição integrada validada
≠ jornada completa
≠ implementação
```

Valores desconhecidos permanecem `indeterminado`, `ausente` ou `não examinado`.

## 9. Próxima transição possível

A próxima evolução documental possível é:

**UXA-082 — Validação Funcional e Visual da Galeria Integrada e Priorização Governada das Lacunas.**

A UXA-082 não foi iniciada e dependerá de autorização separada.
