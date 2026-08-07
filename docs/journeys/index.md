---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.23.0
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
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 4. Estado documental

| Camada | Estado | Referência |
|---|---|---|
| visão geral das Jornadas Integradas | `active` 0.23.0 | UXA-095 |
| Pessoa, Coletivo e Organização | `draft` | incompletude explícita |
| Jornada da Pessoa | `draft` 0.8.0 | UXA-095 |
| Jornada do Coletivo | `draft` 0.11.0 | UXA-095 |
| handoffs e cenários | `active` | síntese atualizada até UXA-095 |
| catálogo integrado | `active` 0.19.0 | UXA-095 |
| registro de superfícies | `active` 0.12.0 | UXA-095 |
| detalhamento da Pessoa | `active` 0.7.0 | UXA-095 |
| registro de transições | `active` 0.12.0 | UXA-095 |
| galeria visual integrada | `active` 0.14.0 | UXA-095 |
| página de Coletivos | `active` 0.12.0 | UXA-095 |
| matriz por SVG | `active` 0.12.0 | UXA-095 |
| registro de lacunas | `active` 0.20.0 | UXA-095 |
| protótipo, aplicação e motor | não iniciados | — |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 5. Resultado da UXA-095

A UXA-095:

- adiciona 1 SVG móvel para `PER-108`;
- reforma 1 SVG existente de `PER-107` com entrada explícita para o Início;
- materializa `PER-108` sem validá-lo;
- torna `TRN-111` parcial, sem validação ponta a ponta;
- mantém `TRN-110` integralmente validada;
- não cria IDs nem promove jornadas.

## 6. Cobertura visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes | **108** |
| associações individuais | **108** |
| perfis de rastreabilidade | **28** |
| com validação funcional vigente | **96** |
| pendentes de validação específica | **12** |
| IDs com referência visual | **30 de 40** |
| responsabilidades sem SVG dedicado | **9** |
| fronteira sem tela por definição | 1 |

As pendências são 10 UXA-055 + PER-107 corrente reformulado + PER-108.

## 7. Continuidade de Coletivos

```text
Visão Geral do Responsável — validada
→ TRN-112 — integralmente validada
→ gestão de solicitações — validada
↔ TRN-105/106/107/109 — integralmente validadas
→ TRN-108 — integralmente validada
→ Meus Coletivos — validado
→ TRN-110 — integralmente validada
→ Central — contrato validado; SVG corrente pendente
→ TRN-111 — parcial
→ Início do Participante — materializado; validação pendente
```

A sequência completa continua `draft`.

## 8. Regras preservadas

- abertura de Central/Início não altera vínculo ou autoridade;
- leitura não conclui ação substantiva;
- presença em atividade não é inferida;
- vínculo, disponibilidade, função e autoridade são distintos;
- Início sintetiza e encaminha, não replica canais especializados;
- validação integral documental não equivale a implementação técnica.

## 9. Próxima transição possível

**UXA-096 — Validação Funcional do Início do Participante, Revalidação de PER-107 e Validação Integrada de GKR-TRN-111**, mediante autorização separada.

A UXA-096 não foi iniciada.
