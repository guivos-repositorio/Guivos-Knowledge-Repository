---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.25.0
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
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 4. Estado documental

| Camada | Estado | Referência |
|---|---|---|
| visão geral das Jornadas Integradas | `active` 0.25.0 | UXA-097 |
| Pessoa, Coletivo e Organização | `draft` | incompletude explícita |
| Jornada da Pessoa | `draft` 0.10.0 | UXA-097 |
| Jornada do Coletivo | `draft` 0.12.0 | UXA-096 |
| handoffs e cenários | `active` | sínteses preservadas; TRN-007 no registro granular |
| catálogo integrado | `active` 0.21.0 | UXA-097 |
| registro de superfícies | `active` 0.14.0 | UXA-097 |
| detalhamento da Pessoa | `active` 0.9.0 | UXA-097 |
| registro de transições | `active` 0.14.0 | UXA-097 |
| galeria visual integrada | `active` 0.16.0 | UXA-097 |
| página da Pessoa | `active` 0.4.0 | UXA-097 |
| página de Coletivos | `active` 0.13.0 | UXA-096 |
| matriz por SVG | `active` 0.14.0 | UXA-097 |
| registro de lacunas | `active` 0.22.0 | UXA-097 |
| protótipo, aplicação e motor | não iniciados | — |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 5. Resultado da UXA-097

A UXA-097:

- cria 1 SVG para a primeira variante de `PER-008`;
- reforma 1 SVG existente do estado de decisão de `PER-007`;
- revalida a variante corrente de `PER-007`;
- valida a primeira variante de `PER-008`;
- promove `TRN-007` a integralmente validada;
- preserva a Tela Hoje recorrente sem alteração;
- não cria IDs nem promove jornadas.

## 6. Cobertura visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes | **109** |
| associações individuais | **109** |
| perfis de rastreabilidade | **28** |
| com validação funcional vigente | **99** |
| pendentes de validação específica | **10** |
| IDs com referência visual | **30 de 40** |
| responsabilidades sem SVG dedicado | **9** |
| fronteira sem tela por definição | 1 |

As dez pendências remanescentes são exclusivamente os estados residuais UXA-055.

## 7. Continuidade pessoal fechada pela UXA-097

```text
PER-007 — compreensão inicial revisável
→ escolhas compatíveis e explícitas
→ TRN-007 — integralmente validada
→ PER-008 — primeira Tela Hoje validada
→ Tela Hoje recorrente preservada como variante separada
```

A Jornada da Pessoa permanece `draft` porque `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` continuam parciais.

## 8. Continuidade de Coletivos preservada

Oito handoffs permanecem integralmente validados no trecho governado de Coletivos: `TRN-105`, `106`, `107`, `108`, `109`, `110`, `111` e `112`.

## 9. Regras preservadas

- concluir a compreensão inicial não constitui avanço humano;
- personalização não é condição para acessar Hoje;
- primeira Hoje não fabrica mudança anterior, urgência ou conteúdo comercial;
- estado canônico prevalece sobre estado visual obsoleto;
- repetição não duplica efeito lógico;
- abertura de Central/Início não altera vínculo ou autoridade;
- evento histórico não concede acesso interno;
- validação integral documental não equivale a implementação técnica.

## 10. Próxima transição possível

Com `V1` fechado, a próxima prioridade de validação registrada é `V2 — publicação → descoberta/mapa/lista/detalhe`. **UXA-098 não foi iniciada.**