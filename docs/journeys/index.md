---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.32.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-08
related:
  - UXA-070
  - UXA-080
  - UXA-085
  - UXA-090
  - UXA-097
  - UXA-098
  - UXA-099
  - UXA-100
  - UXA-100-A3
  - UXA-101
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Jornadas Integradas

## 1. Finalidade

Esta seção reúne as jornadas da Pessoa, do Coletivo e da Organização para leitura contínua, comparação de perspectivas, inspeção visual, análise de handoffs e identificação de lacunas. Ela não substitui contratos, wireframes, validações ou registros canônicos.

## 2. Vistas disponíveis

- [Galeria Visual Integrada de Telas](screen-gallery.md)
- [Planos, Comparação e Cobrança — Galeria Canônica](screen-gallery-plans-billing.md)
- [Matriz de Rastreabilidade Visual por SVG](screen-gallery-traceability-matrix.md)
- [Catálogo de Telas](screen-catalog.md)
- [Jornada da Pessoa](person.md)
- [Jornada do Coletivo](collective.md)
- [Jornada da Organização](organization.md)
- [Handoffs entre participantes](handoffs.md)
- [Cenários integrados](scenarios.md)
- [Registro Granular de Superfícies e Estados](surface-registry.md)
- [Registro Granular de Transições](transition-registry.md)
- [Lacunas e Continuidades Ausentes](gaps.md)

## 3. Sequência governada recente

```text
UXA-097 — compreensão inicial → primeira Tela Hoje
→ UXA-098 — publicação → descoberta → Mapa/Lista → Detalhe
→ UXA-099 — dez estados residuais Opportunity Boost
→ UXA-100/A1/A2/A3 — Planos materializados, validados e promovidos
→ UXA-101 — Detalhe → revisão consciente → BND-001
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 4. Estado documental proposto

| Camada | Estado | Referência |
|---|---|---|
| visão geral das Jornadas Integradas | `active` 0.32.0 | reconciliação de nomenclatura 2026-08-08 |
| Pessoa, Coletivo e Organização | `draft` | incompletude explícita preservada |
| Jornada da Pessoa | `draft` 0.15.0 | UXA-101 |
| Jornada do Coletivo | `draft` 0.16.0 | taxonomia Livre/Mobiliza/Impacta/Rede |
| Jornada da Organização | `draft` 0.9.0 | taxonomia Conecta/Eleva/Transforma |
| catálogo integrado | `active` 0.26.0 | 118 SVGs canônicos |
| registro de superfícies | `active` 0.17.0 | 53 IDs |
| registro de transições | `active` 0.18.0 | 54 transições |
| galeria visual integrada | `active` 0.21.0 | 118 SVGs canônicos |
| galeria de Planos | `active` 0.3.0 | 9 SVGs canônicos |
| matriz por SVG | `active` 0.17.0 | 118 associações / 31 perfis |
| registro de lacunas | `active` 0.27.0 | V4 encerrada; V5 pendente |
| protótipo, aplicação e motor | não iniciados | — |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 5. Continuidade de oportunidades após UXA-101

```text
ORG-003 → TRN-203 → PER-201
PER-201 ↔ TRN-210 ↔ PER-202
PER-201/PER-202 → TRN-204/211 → PER-203
PER-203 → revisão consciente no mesmo estado → TRN-205 → BND-001
```

- UXA-098 valida `TRN-203`, `204`, `210` e `211`;
- UXA-101 valida `TRN-205` até a fronteira de autoridade da Guivos;
- `BND-001` não possui tela Guivos;
- qualquer resultado posterior pertence ao terceiro até reconciliação autorizada e comprovada.

## 6. Etapa transversal de Planos preservada

```text
*-301 Planos e comparação
├── upgrade → *-302 revisão → *-304 resultado/recuperação → *-301
├── downgrade/cancelamento → *-303 → *-304 → *-301
└── quando autoatendimento não for suficiente → BND-002
```

A nomenclatura vigente é:

- Pessoa: `Free · Plus · Pro`;
- Coletivo: `Livre · Mobiliza · Impacta · Rede`;
- Organização: `Conecta · Eleva · Transforma`;
- Guivos Business: `Start · Growth · Scale · Enterprise`, como Produto Especializado separado.

`BND-002` é fronteira genérica de contratação/dimensionamento assistido e não plano. As transições internas continuam localmente validadas; `TRN-416/426` permanecem parciais. Cobrança real e processo posterior a `BND-002` continuam fora do escopo.

## 7. Cobertura canônica

| Indicador | Resultado |
|---|---:|
| SVGs canônicos | **118** |
| associações | **118** |
| perfis | **31** |
| validações vigentes | **118** |
| pendentes | **0** |
| superfícies/estados/fronteiras | **53** |
| transições | **54** |
| IDs com referência visual | **42 de 53** |
| responsabilidades sem SVG dedicado | **9** |
| fronteiras sem tela | **2** |

## 8. Separações obrigatórias

- Planos canonicamente registrado não equivale a checkout implementado;
- Organização ≠ Guivos Business;
- Organização Transforma ≠ Guivos Business Enterprise;
- `BND-002` ≠ Enterprise ou Scale;
- revisão de saída em `PER-203` não cria tela nova;
- validação até `BND-001` não valida sistema de terceiro;
- pagar um plano ou patrocínio não altera relevância funcional;
- `COM-005` validado não promove automaticamente `TRN-305`;
- validação documental não equivale a implementação técnica.

## 9. Estado da frente

V1, V2, V3 e V4 estão encerradas nos limites declarados. V5 não foi iniciada. Pessoa, Coletivo e Organização permanecem `draft`, e Engenharia de Produto permanece pausada.
