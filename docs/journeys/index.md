---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.24.0
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
UXA-090 — cinco handoffs validados ponta a ponta
→ UXA-091 — Meus Coletivos materializada
→ UXA-092 — Meus Coletivos e TRN-108 validados
→ UXA-093 — Central materializada
→ UXA-094 — Central e TRN-110 validadas
→ UXA-095 — Início do Participante materializado; TRN-111 parcial
→ UXA-096 — Central/Início revalidados e TRN-111 validada ponta a ponta
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 4. Estado documental

| Camada | Estado | Referência |
|---|---|---|
| visão geral das Jornadas Integradas | `active` 0.24.0 | UXA-096 |
| Pessoa, Coletivo e Organização | `draft` | incompletude explícita |
| Jornada da Pessoa | `draft` 0.9.0 | UXA-096 |
| Jornada do Coletivo | `draft` 0.12.0 | UXA-096 |
| handoffs e cenários | `active` | síntese atualizada até UXA-096 |
| catálogo integrado | `active` 0.20.0 | UXA-096 |
| registro de superfícies | `active` 0.13.0 | UXA-096 |
| detalhamento da Pessoa | `active` 0.8.0 | UXA-096 |
| registro de transições | `active` 0.13.0 | UXA-096 |
| galeria visual integrada | `active` 0.15.0 | UXA-096 |
| página de Coletivos | `active` 0.13.0 | UXA-096 |
| matriz por SVG | `active` 0.13.0 | UXA-096 |
| registro de lacunas | `active` 0.21.0 | UXA-096 |
| protótipo, aplicação e motor | não iniciados | — |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 5. Resultado da UXA-096

A UXA-096:

- reforma 2 SVGs existentes, sem criar ativos;
- revalida `PER-107` corrente;
- valida `PER-108`;
- promove `TRN-111` a integralmente validada;
- preserva `TRN-110` integralmente validada;
- não cria IDs nem promove jornadas.

## 6. Cobertura visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes | **108** |
| associações individuais | **108** |
| perfis de rastreabilidade | **28** |
| com validação funcional vigente | **98** |
| pendentes de validação específica | **10** |
| IDs com referência visual | **30 de 40** |
| responsabilidades sem SVG dedicado | **9** |
| fronteira sem tela por definição | 1 |

As dez pendências remanescentes são exclusivamente os estados residuais UXA-055.

## 7. Continuidade de Coletivos

```text
Visão Geral do Responsável — validada
→ TRN-112 — integralmente validada
→ gestão de solicitações — validada
↔ TRN-105/106/107/109 — integralmente validadas
→ TRN-108 — integralmente validada
→ Meus Coletivos — validado
→ TRN-110 — integralmente validada
→ Central — validada
→ TRN-111 — integralmente validada
→ Início do Participante — validado
```

A sequência específica está fechada até o Início no escopo documental, mas a Jornada da Pessoa e a Jornada do Coletivo completas continuam `draft`.

## 8. Regras preservadas

- abertura de Central/Início não altera vínculo ou autoridade;
- evento histórico não concede acesso interno;
- leitura não conclui ação substantiva;
- presença em atividade não é inferida;
- vínculo, disponibilidade, função e autoridade são distintos;
- Início sintetiza e encaminha, não replica canais especializados;
- estado canônico prevalece sobre estado visual obsoleto;
- repetição não duplica efeito lógico;
- validação integral documental não equivale a implementação técnica.

## 9. Próxima transição possível

A próxima priorização deverá partir das lacunas remanescentes. **UXA-097 não foi iniciada.**
