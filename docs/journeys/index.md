---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.17.0
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
  - UXA-089
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
7. consulte as [Lacunas](gaps.md) sem confundir superfície validada com jornada concluída.

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
→ UXA-081 a UXA-085 — galeria e matriz auditadas, reformuladas, revalidadas e promovidas
→ UXA-086 — Visão Geral do Responsável materializada
→ UXA-087 — Visão Geral do Responsável reformulada e validada funcionalmente
→ UXA-088 — Gestão de Solicitações do Responsável materializada em sete estados desktop
→ UXA-089 — Gestão de Solicitações reformulada e validada funcionalmente
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 5. Estado documental

| Camada | Estado | Referência |
|---|---|---|
| visão geral das Jornadas Integradas | `active` 0.17.0 | UXA-089 |
| Pessoa, Coletivo e Organização | `draft` | incompletude explícita |
| handoffs e cenários | `active` | UXA-074; UXA-075 |
| catálogo integrado | `active` 0.14.0 | UXA-089 |
| registro de superfícies | `active` 0.7.0 | UXA-089 |
| registro de transições | `active` 0.6.0 | UXA-089; transições de solicitação continuam parciais |
| detalhamento do Coletivo | `active` 0.6.0 | UXA-089 |
| demais detalhamentos | `active` 0.2.0 | UXA-080 |
| galeria visual integrada | `active` 0.9.0 | UXA-089 |
| página de Coletivos | `active` 0.7.0 | UXA-089 |
| demais páginas visuais | `active` 0.3.0 | UXA-085 |
| matriz por SVG | `active` 0.7.0 | UXA-089 |
| registro de lacunas | `active` 0.14.0 | UXA-089 |
| protótipo, aplicação e motor | não iniciados | — |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 6. Resultado da UXA-089

A UXA-089 valida `GKR-SURF-COL-003 — gestão de solicitações` após reformulação controlada de seis dos sete SVGs desktop da família.

A validação consolida:

- referência temporal distinguindo estimativa e prazo de resposta;
- critérios de decisão previamente apresentados à Pessoa;
- acessibilidade separada de elegibilidade e tratada para acomodação;
- autoridade verificada por escopo, nunca criada por confirmação;
- aprovação e recusa com fundamento e consequência compreensíveis;
- autoridade insuficiente sem autoelevação de permissão.

Ela não:

- valida `GKR-TRN-105` a `GKR-TRN-109` ou `GKR-TRN-112` ponta a ponta;
- materializa `GKR-SURF-PER-106`;
- promove a jornada do Coletivo;
- inicia protótipo, aplicação ou Engenharia de Produto.

## 7. Cobertura visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 105 |
| associações individuais | 105 |
| perfis de rastreabilidade | 25 |
| com validação funcional registrada | 95 |
| pendentes de validação específica | 10 |
| IDs com referência visual | 27 de 40 |
| responsabilidades sem SVG dedicado | 12 |
| fronteira sem tela por definição | 1 |

Os dez pendentes remanescentes correspondem exclusivamente aos estados da UXA-055.

## 8. Ressalvas

- perfis agregados não substituem análise exclusiva por estado;
- dez estados da UXA-055 permanecem sem validação;
- `GKR-TRN-105` a `GKR-TRN-109` e `GKR-TRN-112` permanecem parciais;
- `GKR-SURF-PER-106` continua ausente;
- continuidades entre pacotes permanecem parciais ou não examinadas;
- instrumento visual `active` e superfície validada não equivalem a jornada validada.

## 9. Prioridade de Coletivos

```text
Visão Geral do Responsável — validada
→ gestão de solicitações — validada no escopo da superfície
→ handoffs bilaterais de solicitação — validação integrada pendente
→ Meus Coletivos — ausente
→ Central de Atualizações — ausente
→ Início do Participante — reformulação pendente
```

O avanço a jusante depende de ato governado separado.

## 10. Regra de leitura

```text
visual existente
≠ validação funcional automática
≠ transição ponta a ponta validada
≠ jornada completa
≠ implementação
```

Valores desconhecidos permanecem `indeterminado`, `ausente` ou `não examinado`.

## 11. Próxima transição possível

**UXA-090 — Validação Integrada dos Handoffs Bilaterais de Solicitação em Coletivos**, mediante autorização separada.

A UXA-090 não foi iniciada.
