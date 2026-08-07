---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.14.0
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
→ UXA-086 — Visão Geral do Responsável materializada
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 5. Estado documental

| Camada | Estado | Referência |
|---|---|---|
| visão geral das Jornadas Integradas | `active` | UXA-075 |
| Pessoa, Coletivo e Organização | `draft` | incompletude explícita |
| handoffs e cenários | `active` | UXA-074; UXA-075 |
| catálogo integrado | `active` 0.11.0 | UXA-086 |
| registro de superfícies | `active` 0.4.0 | UXA-086 |
| registro de transições | `active` 0.4.0 | UXA-086 |
| detalhamento do Coletivo | `active` 0.3.0 | UXA-086 |
| demais detalhamentos | `active` 0.2.0 | UXA-080 |
| galeria visual integrada | `active` 0.6.0 | UXA-086 |
| página de Coletivos | `active` 0.4.0 | UXA-086 |
| demais páginas visuais | `active` 0.3.0 | UXA-085 |
| matriz por SVG | `active` 0.4.0 | UXA-086 |
| registro de lacunas | `active` 0.11.0 | UXA-086 |
| protótipo, aplicação e motor | não iniciados | — |
| Engenharia de Produto | não iniciada | W0-01 |

## 6. Resultado da UXA-086

A UXA-086 materializa exclusivamente `GKR-SURF-COL-002 — Visão Geral do Responsável` em um wireframe desktop de baixa fidelidade.

A materialização:

- cria 1 novo SVG;
- torna explícitos papel, autoridade e escopo do responsável;
- apresenta sínteses de momento, atenção principal, vínculos, comunicação, proteção e governança;
- cria ponto de entrada documental para solicitações.

Ela não:

- valida funcionalmente o novo SVG;
- materializa a fila completa de solicitações;
- valida `GKR-TRN-112`;
- promove a jornada do Coletivo;
- inicia protótipo, aplicação ou Engenharia de Produto.

## 7. Cobertura visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 98 |
| associações individuais | 98 |
| perfis de rastreabilidade | 24 |
| com validação funcional registrada | 87 |
| pendentes de validação específica | 11 |
| IDs com referência visual | 26 de 40 |
| responsabilidades sem SVG dedicado | 13 |
| fronteira sem tela por definição | 1 |

## 8. Ressalvas

- perfis agregados não substituem análise exclusiva por estado;
- dez estados da UXA-055 permanecem sem validação;
- a UXA-086 também permanece sem validação funcional específica;
- continuidades entre pacotes permanecem parciais ou não examinadas;
- instrumento visual `active` não equivale a jornada validada.

## 9. Prioridade de Coletivos

```text
Visão Geral do Responsável — materializada; validação pendente
→ gestão completa de solicitações — ausente
→ Meus Coletivos — ausente
→ Central de Atualizações — ausente
→ Início do Participante — reformulação pendente
```

O avanço para a segunda superfície depende da validação e de autorização separada.

## 10. Regra de leitura

```text
visual existente
≠ decisão visual aprovada
≠ validação funcional
≠ transição ponta a ponta validada
≠ jornada completa
≠ implementação
```

Valores desconhecidos permanecem `indeterminado`, `ausente` ou `não examinado`.

## 11. Próxima transição possível

**UXA-087 — Validação Funcional da Visão Geral do Responsável do Coletivo**, mediante autorização separada.

A UXA-087 não foi iniciada.
