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
7. consulte as [Lacunas](gaps.md) sem confundir superfície materializada com jornada concluída.

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
→ UXA-087 — Visão Geral do Responsável reformulada e validada funcionalmente
→ UXA-088 — Gestão de Solicitações do Responsável materializada em sete estados desktop
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 5. Estado documental

| Camada | Estado | Referência |
|---|---|---|
| visão geral das Jornadas Integradas | `active` 0.16.0 | UXA-088 |
| Pessoa, Coletivo e Organização | `draft` | incompletude explícita |
| handoffs e cenários | `active` | UXA-074; UXA-075 |
| catálogo integrado | `active` 0.13.0 | UXA-088 |
| registro de superfícies | `active` 0.6.0 | UXA-088 |
| registro de transições | `active` 0.5.0 | UXA-088; transições de solicitação continuam parciais |
| detalhamento do Coletivo | `active` 0.5.0 | UXA-088 |
| demais detalhamentos | `active` 0.2.0 | UXA-080 |
| galeria visual integrada | `active` 0.8.0 | UXA-088 |
| página de Coletivos | `active` 0.6.0 | UXA-088 |
| demais páginas visuais | `active` 0.3.0 | UXA-085 |
| matriz por SVG | `active` 0.6.0 | UXA-088 |
| registro de lacunas | `active` 0.13.0 | UXA-088 |
| protótipo, aplicação e motor | não iniciados | — |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 6. Resultado da UXA-088

A UXA-088 materializa `GKR-SURF-COL-003 — gestão de solicitações` em sete SVGs desktop:

1. fila operacional;
2. detalhe comum;
3. análise protegida;
4. pedido de informação adicional;
5. confirmação de aprovação;
6. confirmação de recusa;
7. autoridade insuficiente.

A materialização:

- cria evidência responsável para `GKR-TRN-105` a `GKR-TRN-109`;
- materializa o destino de `GKR-TRN-112`;
- preserva os efeitos na perspectiva da Pessoa já materializados em UXA-066 e validados por UXA-067;
- mantém cancelamento pela Pessoa e expiração como eventos distintos das decisões do responsável.

Ela não:

- valida funcionalmente os sete novos SVGs;
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
| com validação funcional registrada | 88 |
| pendentes de validação específica | 17 |
| IDs com referência visual | 27 de 40 |
| responsabilidades sem SVG dedicado | 12 |
| fronteira sem tela por definição | 1 |

Os 17 pendentes correspondem aos dez estados da UXA-055 e aos sete estados da UXA-088.

## 8. Ressalvas

- perfis agregados não substituem análise exclusiva por estado;
- dez estados da UXA-055 permanecem sem validação;
- sete estados da UXA-088 permanecem sem validação funcional específica;
- `GKR-TRN-105` a `GKR-TRN-109` e `GKR-TRN-112` permanecem parciais;
- `GKR-SURF-PER-106` continua ausente;
- continuidades entre pacotes permanecem parciais ou não examinadas;
- instrumento visual `active` não equivale a jornada validada.

## 9. Prioridade de Coletivos

```text
Visão Geral do Responsável — validada
→ gestão de solicitações — materializada; validação pendente
→ Meus Coletivos — ausente
→ Central de Atualizações — ausente
→ Início do Participante — reformulação pendente
```

O avanço a jusante depende primeiro do gate funcional da gestão de solicitações e de autorização separada.

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

**UXA-089 — Validação Funcional da Gestão de Solicitações do Responsável do Coletivo**, mediante autorização separada.

A UXA-089 não foi iniciada.
