---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.26.0
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
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 4. Estado documental

| Camada | Estado | Referência |
|---|---|---|
| visão geral das Jornadas Integradas | `active` 0.26.0 | UXA-098 |
| Pessoa, Coletivo e Organização | `draft` | incompletude explícita |
| Jornada da Pessoa | `draft` 0.11.0 | UXA-098 |
| Jornada do Coletivo | `draft` 0.12.0 | UXA-096 |
| Jornada da Organização | `draft` 0.4.0 | UXA-098 |
| handoffs e cenários | `active` | sínteses preservadas |
| catálogo integrado | `active` 0.21.0 | sem alteração visual em UXA-098 |
| registro de superfícies | `active` 0.14.0 | sem mudança de superfície em UXA-098 |
| detalhamento da Pessoa | `active` 0.9.0 | sem mudança em UXA-098 |
| registro de transições | `active` 0.15.0 | UXA-098 |
| galeria visual integrada | `active` 0.16.0 | sem alteração visual em UXA-098 |
| página da Pessoa | `active` 0.4.0 | sem alteração visual em UXA-098 |
| página de Coletivos | `active` 0.13.0 | UXA-096 |
| matriz por SVG | `active` 0.14.0 | sem alteração visual em UXA-098 |
| registro de lacunas | `active` 0.23.0 | UXA-098 |
| protótipo, aplicação e motor | não iniciados | — |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 5. Resultado da UXA-098

A UXA-098:

- não cria nem altera SVG;
- preserva as validações locais de `ORG-003`, `PER-201`, `PER-202` e `PER-203`;
- promove `TRN-203`, `TRN-204`, `TRN-210` e `TRN-211` a integralmente validadas;
- formaliza elegibilidade à descoberta sem garantia de exposição;
- formaliza Mapa e Lista como uma única consulta;
- formaliza Mapa/Lista → Detalhe com identidade e estado canônicos;
- separa o efeito externo posterior em `TRN-205`;
- preserva a separação entre inventário orgânico e patrocinado;
- não promove jornadas.

## 6. Cobertura visual preservada

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

## 7. Continuidade V2 validada

```text
ORG-003 — oportunidade aprovada e ativa
→ TRN-203 — elegibilidade à descoberta, sem exposição garantida
→ PER-201 — Mapa
↔ TRN-210 — mesma consulta
→ PER-202 — Lista

PER-201 → TRN-204 → PER-203
PER-202 → TRN-211 → PER-203
```

Estado canônico, identidade lógica, retorno, interrupção e idempotência prevalecem em toda a cadeia. `TRN-205` permanece separada para eventual efeito externo.

## 8. Continuidade de Coletivos preservada

Oito handoffs permanecem integralmente validados no trecho governado de Coletivos: `TRN-105`, `106`, `107`, `108`, `109`, `110`, `111` e `112`.

## 9. Regras preservadas

- publicação ativa não garante descoberta individual, distribuição ou posição;
- Mapa e Lista são modos da mesma consulta;
- abrir Detalhe não equivale a interesse, inscrição ou evolução;
- estado canônico prevalece sobre estado visual obsoleto;
- pagamento não altera relevância funcional;
- repetição não duplica oportunidade ou efeito lógico;
- validação integral documental não equivale a implementação técnica.

## 10. Próxima transição possível

Com `V2` encerrada, a próxima prioridade de validação registrada é `V3 — dez estados residuais UXA-055`. **UXA-099 não foi iniciada.**