---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.22.0
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
→ UXA-093 — Central de Atualizações materializada
→ UXA-094 — Central validada e TRN-110 validada ponta a ponta
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 4. Estado documental

| Camada | Estado | Referência |
|---|---|---|
| visão geral das Jornadas Integradas | `active` 0.22.0 | UXA-094 |
| Pessoa, Coletivo e Organização | `draft` | incompletude explícita |
| Jornada da Pessoa | `draft` 0.7.0 | UXA-094 |
| Jornada do Coletivo | `draft` 0.10.0 | UXA-092 |
| handoffs e cenários | `active` | síntese atualizada até UXA-094 |
| catálogo integrado | `active` 0.18.0 | UXA-094 |
| registro de superfícies | `active` 0.11.0 | UXA-094 |
| detalhamento da Pessoa | `active` 0.6.0 | UXA-094 |
| registro de transições | `active` 0.11.0 | UXA-094 |
| galeria visual integrada | `active` 0.13.0 | UXA-094 |
| página de Coletivos | `active` 0.11.0 | UXA-094 |
| matriz por SVG | `active` 0.11.0 | UXA-094 |
| registro de lacunas | `active` 0.19.0 | UXA-094 |
| protótipo, aplicação e motor | não iniciados | — |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 5. Resultado da UXA-094

A UXA-094:

- reforma `PER-106` para adicionar entrada explícita e neutra para a Central;
- reforma `PER-107` para corrigir prioridade de segurança, fonte, preferências e taxonomia;
- revalida `PER-106` na versão corrente;
- valida `PER-107`;
- promove `TRN-110` a `integralmente validada`;
- mantém `TRN-111` ausente e `PER-108` sem materialização vigente;
- não cria ou remove SVG, superfície, transição ou ID;
- não promove qualquer jornada.

## 6. Cobertura visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 107 |
| associações individuais | 107 |
| perfis de rastreabilidade | 27 |
| com validação funcional vigente | **97** |
| pendentes de validação específica | **10** |
| IDs com referência visual | 29 de 40 |
| responsabilidades sem SVG dedicado | 10 |
| fronteira sem tela por definição | 1 |

Os dez pendentes remanescentes são exclusivamente os estados residuais da UXA-055.

## 7. Continuidade de Coletivos

```text
Visão Geral do Responsável — validada
→ TRN-112 — integralmente validada
→ gestão de solicitações — validada
↔ TRN-105/106/107/109 — integralmente validadas
→ TRN-108 — integralmente validada
→ Meus Coletivos — validado
→ TRN-110 — integralmente validada
→ Central de Atualizações — validada
→ TRN-111 — ausente
→ Início do Participante — reformulação/materialização pendente
```

A sequência completa de Coletivos continua `draft`; validar o trecho até a Central não comprova a jornada interna posterior.

## 8. Regras preservadas

- abertura da Central não altera vínculo nem leitura;
- estado `lido` não conclui ação substantiva;
- ações revalidam o estado canônico;
- repetição de abertura ou leitura não duplica efeito;
- segurança material precede ação comum;
- preferências não ocultam aviso essencial de segurança além do limite permitido;
- `PER-108` e áreas P1 não são presumidos como existentes;
- validação integral documental não equivale a implementação técnica.

## 9. Próxima transição possível

**UXA-095 — Materialização/Reformulação Controlada do Início do Participante (`GKR-SURF-PER-108`) e Refinamento de `GKR-TRN-111`**, mediante autorização separada.

A UXA-095 não foi iniciada.
