---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.13.0
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
→ UXA-085 — promoção controlada dos instrumentos visuais
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 5. Estado documental

| Camada | Estado | Referência |
|---|---|---|
| visão geral das Jornadas Integradas | `active` | UXA-075 |
| Pessoa, Coletivo e Organização | `draft` | incompletude explícita |
| handoffs e cenários | `active` | UXA-074; UXA-075 |
| catálogo integrado | `active` 0.10.0 | UXA-085 |
| registros de superfícies e transições | `active` 0.3.0 | UXA-080 |
| quatro detalhamentos granulares | `active` 0.2.0 | UXA-080 |
| galeria visual integrada | `active` 0.5.0; ressalvas preservadas | UXA-085 |
| cinco páginas visuais | `active` 0.3.0; instrumentos de inspeção | UXA-085 |
| matriz por SVG | `active` 0.3.0; ressalvas preservadas | UXA-085 |
| registro de lacunas | `active` 0.10.0 | UXA-085 |
| protótipo, aplicação e motor | não iniciados | — |
| Engenharia de Produto | não iniciada | W0-01 |

## 6. Resultado da UXA-085

A UXA-085 promove somente a galeria, suas cinco páginas integrantes e a matriz por SVG como instrumentos documentais vigentes no escopo aprovado pela UXA-084.

A promoção não:

- valida jornadas ponta a ponta;
- altera os 97 SVGs;
- reclassifica superfícies ou transições;
- fecha lacunas;
- valida os dez estados residuais da UXA-055;
- inicia protótipo, aplicação ou Engenharia de Produto.

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
- instrumento visual `active` não equivale a jornada validada.

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

**UXA-086 — Materialização Controlada da Visão Geral do Responsável do Coletivo**, mediante autorização separada.

A UXA-086 não foi iniciada.
