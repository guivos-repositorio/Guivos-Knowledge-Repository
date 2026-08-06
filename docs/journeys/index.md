---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.10.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
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
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-SECTION-CLARIFICATION-001
normative: false
---

# Jornadas Integradas

## 1. Finalidade

Esta seção reúne, por referência, as jornadas da **Pessoa**, do **Coletivo** e da **Organização** para permitir leitura contínua, comparação de perspectivas, inspeção visual, análise de handoffs e identificação de lacunas.

Ela não substitui contratos, wireframes, validações ou registros canônicos. Em caso de divergência, prevalece o artefato de origem.

## 2. Como utilizar

1. consulte a [Galeria Visual Integrada de Telas](screen-gallery.md) para localizar os SVGs existentes;
2. não interprete a ordem atual da galeria como sequência funcional aprovada;
3. use o [Catálogo de telas](screen-catalog.md) para visão agregada;
4. percorra a vista do participante;
5. localize superfícies e transições por ID;
6. confira separadamente maturidade, materialização, validação e continuidade;
7. observe handoffs, retornos e interrupções;
8. consulte as [Lacunas](gaps.md) sem tratá-las como fechadas.

## 3. Vistas disponíveis

- [Galeria Visual Integrada de Telas](screen-gallery.md)
- [Catálogo de telas](screen-catalog.md)
- [Jornada da Pessoa](person.md)
- [Jornada do Coletivo](collective.md)
- [Jornada da Organização](organization.md)
- [Handoffs entre participantes](handoffs.md)
- [Cenários integrados](scenarios.md)
- [Registro Granular de Superfícies e Estados](surface-registry.md)
- [Registro Granular de Transições](transition-registry.md)
- [Lacunas e continuidades ausentes](gaps.md)

## 4. Sequência governada

```text
UXA-070 — programa funcional
→ UXA-071 — materialização da seção
→ UXA-072 — validação não aprovada
→ UXA-073 — reformulação e navegação
→ UXA-074 — revalidação aprovada com ressalvas
→ UXA-075 — promoção seletiva
→ UXA-076 — registros granulares em draft
→ UXA-077 — validação granular não aprovada
→ UXA-078 — correção dos cinco achados
→ UXA-079 — revalidação aprovada com ressalvas
→ UXA-080 — promoção dos instrumentos granulares
→ UXA-081 — galeria visual e auditoria de cobertura
→ UXA-082 — validação da galeria não aprovada e lacunas repriorizadas
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 5. Estado documental

| Camada | Estado | Referência |
|---|---|---|
| visão geral das Jornadas Integradas | `active` | UXA-075 |
| Pessoa, Coletivo e Organização | `draft` | incompletude explícita |
| handoffs e cenários | `active` | UXA-074; UXA-075 |
| catálogo integrado | `active` 0.7.0 | UXA-082 |
| registros de superfícies e transições | `active` 0.3.0 | UXA-080 |
| quatro detalhamentos granulares | `active` 0.2.0 | UXA-080 |
| galeria visual integrada | `draft` 0.2.0; não aprovada para promoção | UXA-082 |
| registro de lacunas | `active` 0.7.0 | UXA-082 |
| protótipo, aplicação e motor | não iniciados | — |
| Engenharia de Produto | não iniciada | W0-01 |

## 6. Auditoria visual confirmada

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 97 |
| com validação funcional registrada | 87 |
| pendentes de validação específica | 10 |
| IDs com referência visual direta ou agrupada | 25 de 40 |
| responsabilidades sem SVG dedicado | 14 |
| fronteira documental sem tela por definição | 1 |

A quantidade de SVGs não equivale à quantidade de superfícies. Estados alternativos e variações por dispositivo podem compartilhar a mesma responsabilidade granular.

## 7. Resultado da UXA-082

A galeria foi aprovada somente como inventário centralizado. Sua promoção foi bloqueada pelos seguintes achados:

- ordem funcional incorreta na página da Pessoa;
- Home pública e Tela Hoje agrupadas em um mesmo bloco;
- ausência de rota integrada de inspeção;
- rastreabilidade agrupada insuficiente por SVG;
- versões documentais divergentes.

A estrutura deverá ser reformulada e revalidada antes de promoção.

## 8. Prioridade futura de Coletivos

```text
Visão Geral do Responsável
→ gestão completa de solicitações
→ Meus Coletivos
→ Central de Atualizações
→ Início do Participante
```

Essa ordem respeita as dependências registradas e não inicia nenhuma materialização.

## 9. Dívidas de validação separadas

- compreensão inicial → Tela Hoje;
- publicação → mapa, lista e detalhe;
- dez estados residuais da UXA-055;
- efeito externo;
- erros, retornos e interrupções integrados.

## 10. Regra de leitura

```text
visual existente
≠ decisão visual aprovada
≠ transição integrada validada
≠ jornada completa
≠ implementação
```

Valores desconhecidos permanecem `indeterminado`, `ausente` ou `não examinado`.

## 11. Próxima transição possível

A próxima evolução documental possível é:

**UXA-083 — Reformulação Controlada da Galeria Visual Integrada e da Sequência de Inspeção.**

A UXA-083 não foi iniciada e dependerá de autorização separada.
