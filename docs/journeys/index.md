---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.16.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
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
  - UXA-082
  - UXA-083
  - UXA-084
  - UXA-085
  - UXA-086
  - UXA-087
  - UXA-088
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Jornadas Integradas

## 1. Finalidade

Esta seção reúne as jornadas da Pessoa, do Coletivo e da Organização para leitura contínua, comparação de perspectivas, inspeção visual, análise de handoffs e identificação de lacunas. Ela não substitui contratos, wireframes ou validações.

## 2. Instrumentos

- [Galeria Visual Integrada](screen-gallery.md)
- [Matriz de Rastreabilidade por SVG](screen-gallery-traceability-matrix.md)
- [Catálogo de Telas](screen-catalog.md)
- [Jornada da Pessoa](person.md)
- [Jornada do Coletivo](collective.md)
- [Jornada da Organização](organization.md)
- [Handoffs](handoffs.md)
- [Registro de Superfícies](surface-registry.md)
- [Registro de Transições](transition-registry.md)
- [Lacunas](gaps.md)

## 3. Sequência governada

```text
UXA-070 a UXA-075 — Jornadas Integradas estruturadas e promovidas seletivamente
→ UXA-076 a UXA-080 — registros granulares promovidos
→ UXA-081 a UXA-085 — galeria e matriz auditadas, reformuladas, revalidadas e promovidas
→ UXA-086 — COL-002 materializada
→ UXA-087 — COL-002 reformulada e validada
→ UXA-088 — COL-003 materializada em sete estados desktop
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 4. Estado documental

| Camada | Estado | Referência |
|---|---|---|
| visão geral das Jornadas Integradas | `active` 0.16.0 | UXA-088 |
| Pessoa, Coletivo e Organização | `draft` | incompletude explícita |
| catálogo integrado | `active` 0.13.0 | UXA-088 |
| registro de superfícies | `active` 0.6.0 | UXA-088 |
| registro de transições | `active` 0.5.0 | UXA-088 |
| detalhamento do Coletivo | `active` 0.5.0 | UXA-088 |
| galeria visual integrada | `active` 0.8.0 | UXA-088 |
| página de Coletivos | `active` 0.6.0 | UXA-088 |
| matriz por SVG | `active` 0.6.0 | UXA-088 |
| registro de lacunas | `active` 0.13.0 | UXA-088 |
| protótipo, aplicação e motor | não iniciados | — |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 5. Resultado da UXA-088

A UXA-088 materializa `GKR-SURF-COL-003 — gestão de solicitações` com sete SVGs desktop:

1. fila operacional;
2. detalhe comum;
3. análise protegida;
4. pedido de informação adicional;
5. confirmação de aprovação;
6. confirmação de recusa;
7. autoridade insuficiente.

O pacote cria evidência responsável para `TRN-105` a `109` e materializa o destino de `TRN-112`, mas não valida funcionalmente os sete estados nem os handoffs ponta a ponta.

## 6. Cobertura visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 105 |
| associações individuais | 105 |
| perfis de rastreabilidade | 25 |
| com validação funcional registrada | 88 |
| pendentes de validação específica | 17 |
| IDs com referência visual | 27 de 40 |
| responsabilidades sem SVG dedicado | 12 |
| fronteira sem tela por definição | 1 |

Os 17 pendentes são dez estados da UXA-055 e sete da UXA-088.

## 7. Prioridade de Coletivos

```text
Visão Geral do Responsável — validada
→ gestão de solicitações — materializada; validação pendente
→ Meus Coletivos — ausente
→ Central de Atualizações — ausente
→ Início do Participante — reformulação pendente
```

## 8. Regras preservadas

```text
materialização
≠ validação funcional
≠ transição ponta a ponta validada
≠ jornada completa
≠ implementação
```

A Jornada do Coletivo permanece `draft`.

## 9. Próxima transição possível

**UXA-089 — Validação Funcional da Gestão de Solicitações do Responsável do Coletivo**, mediante autorização separada.

A UXA-089 não foi iniciada.
