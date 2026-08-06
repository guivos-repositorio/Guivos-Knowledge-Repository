---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.12.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-06
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
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-SECTION-CLARIFICATION-001
normative: false
---

# Jornadas Integradas

## 1. Finalidade

Esta seção reúne, por referência, as jornadas da Pessoa, do Coletivo e da Organização para permitir leitura contínua, comparação de perspectivas, inspeção visual, análise de handoffs e identificação de lacunas.

Ela não substitui contratos, wireframes, validações ou registros canônicos.

## 2. Como utilizar

1. abra a [Galeria Visual Integrada](screen-gallery.md);
2. percorra a rota canônica entre as cinco páginas;
3. consulte a [Matriz de Rastreabilidade por SVG](screen-gallery-traceability-matrix.md);
4. use o [Catálogo de Telas](screen-catalog.md) para visão agregada;
5. localize superfícies e transições por ID;
6. confira separadamente maturidade, materialização, validação e continuidade;
7. consulte as [Lacunas](gaps.md) sem tratá-las como fechadas.

## 3. Vistas disponíveis

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

## 4. Sequência governada

```text
UXA-070 a UXA-075 — seção integrada estruturada, reformulada, revalidada e promovida seletivamente
→ UXA-076 a UXA-080 — registros granulares estruturados, corrigidos, revalidados e promovidos
→ UXA-081 — galeria visual e auditoria de cobertura
→ UXA-082 — validação não aprovada e priorização por dependência
→ UXA-083 — reformulação da galeria e matriz individual dos 97 SVGs
→ UXA-084 — revalidação aprovada com ressalvas
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 5. Estado documental

| Camada | Estado | Referência |
|---|---|---|
| visão geral das Jornadas Integradas | `active` | UXA-075 |
| Pessoa, Coletivo e Organização | `draft` | incompletude explícita |
| handoffs e cenários | `active` | UXA-074; UXA-075 |
| catálogo integrado | `active` 0.9.0 | UXA-084 |
| registros de superfícies e transições | `active` 0.3.0 | UXA-080 |
| quatro detalhamentos granulares | `active` 0.2.0 | UXA-080 |
| galeria visual integrada | `draft` 0.4.0; aprovada com ressalvas | UXA-084 |
| cinco páginas visuais | `draft` 0.2.0; revalidadas como conjunto | UXA-084 |
| matriz por SVG | `draft` 0.2.0; aprovada com ressalvas | UXA-084 |
| registro de lacunas | `active` 0.9.0 | UXA-084 |
| protótipo, aplicação e motor | não iniciados | — |
| Engenharia de Produto | não iniciada | W0-01 |

## 6. Resultado da UXA-084

A revalidação aprovou com ressalvas:

- a ordem funcional da Pessoa;
- a separação entre Home e Tela Hoje;
- a rota anterior–índice–matriz–próxima página;
- as 97 associações individuais a 23 perfis;
- a sincronização dos resumos e versões.

A aprovação limita-se ao instrumento de inspeção e não valida jornadas ponta a ponta.

## 7. Cobertura visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 97 |
| associações individuais | 97 |
| perfis de rastreabilidade | 23 |
| com validação funcional registrada | 87 |
| pendentes de validação específica | 10 |
| IDs com referência visual | 25 de 40 |
| responsabilidades sem SVG dedicado | 14 |
| fronteira sem tela por definição | 1 |

## 8. Ressalvas

- perfis agregados não substituem análise exclusiva por estado;
- dez estados da UXA-055 permanecem sem validação;
- continuidades entre pacotes permanecem parciais ou não examinadas;
- galeria aprovada não equivale a jornada validada.

## 9. Prioridade futura de Coletivos

```text
Visão Geral do Responsável
→ gestão completa de solicitações
→ Meus Coletivos
→ Central de Atualizações
→ Início do Participante
```

Nenhuma materialização foi iniciada.

## 10. Regra de leitura

```text
visual existente
≠ decisão visual aprovada
≠ perfil de rastreabilidade suficiente para validar transição
≠ jornada completa
≠ implementação
```

Valores desconhecidos permanecem `indeterminado`, `ausente` ou `não examinado`.

## 11. Próxima transição possível

**UXA-085 — Promoção Controlada da Galeria Visual Integrada e Sincronização Pós-Revalidação**, mediante autorização separada.
