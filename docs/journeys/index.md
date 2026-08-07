---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.27.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - UXA-070
  - UXA-080
  - UXA-085
  - UXA-086
  - UXA-087
  - UXA-088
  - UXA-089
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
  - UXA-094
  - UXA-095
  - UXA-096
  - UXA-097
  - UXA-098
  - UXA-099
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Jornadas Integradas

## 1. Finalidade

Esta seção reúne, por referência, as jornadas da Pessoa, do Coletivo e da Organização para permitir leitura contínua, comparação de perspectivas, inspeção visual, análise de handoffs e identificação de lacunas. Ela não substitui contratos, wireframes, validações ou registros canônicos.

## 2. Vistas disponíveis

- [Galeria Visual Integrada de Telas](screen-gallery.md)
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
UXA-090 — cinco handoffs de solicitação validados ponta a ponta
→ UXA-091 — Meus Coletivos materializada
→ UXA-092 — Meus Coletivos e TRN-108 validados
→ UXA-093 — Central materializada
→ UXA-094 — Central e TRN-110 validadas
→ UXA-095 — Início do Participante materializado; TRN-111 parcial
→ UXA-096 — Central/Início revalidados e TRN-111 validada ponta a ponta
→ UXA-097 — primeira Tela Hoje materializada; PER-007 revalidada; TRN-007 validada ponta a ponta
→ UXA-098 — publicação, descoberta, Mapa, Lista e Detalhe validados como continuidade integrada
→ UXA-099 — dez estados residuais Opportunity Boost validados
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 4. Estado documental

| Camada | Estado | Referência |
|---|---|---|
| visão geral das Jornadas Integradas | `active` 0.27.0 | UXA-099 |
| Pessoa, Coletivo e Organização | `draft` | incompletude explícita |
| Jornada da Pessoa | `draft` 0.11.0 | sem alteração em UXA-099 |
| Jornada do Coletivo | `draft` 0.12.0 | sem alteração em UXA-099 |
| Jornada da Organização | `draft` 0.4.0 | sem alteração em UXA-099 |
| handoffs e cenários | `active` | sínteses preservadas |
| catálogo integrado | `active` 0.22.0 | UXA-099 |
| registro de superfícies | `active` 0.15.0 | UXA-099 |
| detalhamento da Pessoa | `active` 0.9.0 | sem alteração em UXA-099 |
| registro de transições | `active` 0.16.0 | UXA-099; sem promoção de TRN-305 |
| galeria visual integrada | `active` 0.17.0 | UXA-099 |
| página da Pessoa | `active` 0.4.0 | sem alteração em UXA-099 |
| página de Coletivos | `active` 0.13.0 | sem alteração em UXA-099 |
| Opportunity Boost — Operação, Relatórios e Resíduos | `active` 0.4.0 | UXA-099 |
| matriz por SVG | `active` 0.15.0 | UXA-099 |
| registro de lacunas | `active` 0.24.0 | UXA-099 |
| protótipo, aplicação e motor | não iniciados | — |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 5. Resultado da UXA-099

A UXA-099:

- valida os dez SVGs residuais da UXA-055;
- aprova oito sem alteração e reforma dois;
- preserva 109 SVGs, 109 associações e 28 perfis;
- eleva validações funcionais vigentes de 99 para **109**;
- reduz pendências específicas de 10 para **0**;
- valida `COM-005` no escopo dos dez estados;
- preserva `TRN-305` como parcial;
- consolida erro ≠ zero, baixa oferta orgânica, pausa protetiva em falha material, reversibilidade, separação denúncia/contestação e idempotência;
- não promove jornadas.

## 6. Cobertura visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes | **109** |
| associações individuais | **109** |
| perfis de rastreabilidade | **28** |
| com validação funcional vigente | **109** |
| pendentes de validação específica | **0** |
| IDs com referência visual | **30 de 40** |
| responsabilidades sem SVG dedicado | **9** |
| fronteira sem tela por definição | 1 |

## 7. Continuidades anteriores preservadas

`TRN-203`, `TRN-204`, `TRN-210` e `TRN-211` permanecem integralmente validadas pela UXA-098. `TRN-007` permanece integralmente validada pela UXA-097. Oito handoffs permanecem integralmente validados no trecho governado de Coletivos: `TRN-105`, `106`, `107`, `108`, `109`, `110`, `111` e `112`.

## 8. Separações obrigatórias

- validar `COM-005` não valida automaticamente `TRN-305`;
- estados residuais publicitários não alteram catálogo, busca ou ordenação orgânicos;
- mudança material não confirmada não autoriza entrega futura por inércia;
- denúncia, contestação e preferência permanecem fluxos diferentes;
- repetir a mesma intenção não duplica efeito lógico;
- validação documental não equivale a implementação técnica.

## 9. Próxima transição possível

Com `V3` encerrada, a próxima prioridade de validação registrada é `V4 — efeito externo de oportunidades`, associada a `TRN-205`. **UXA-100 não foi iniciada.**
