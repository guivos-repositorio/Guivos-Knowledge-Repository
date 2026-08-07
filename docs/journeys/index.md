---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.15.0
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
→ UXA-081 — galeria visual e auditoria de cobertura
→ UXA-082 — validação não aprovada e priorização por dependência
→ UXA-083 — reformulação da galeria e matriz individual dos 97 SVGs
→ UXA-084 — revalidação aprovada com ressalvas
→ UXA-085 — promoção controlada dos instrumentos visuais
→ UXA-086 — Visão Geral do Responsável materializada
→ UXA-087 — Visão Geral do Responsável reformulada e validada funcionalmente
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 5. Estado documental

| Camada | Estado | Referência |
|---|---|---|
| visão geral das Jornadas Integradas | `active` | UXA-075 |
| Pessoa, Coletivo e Organização | `draft` | incompletude explícita |
| handoffs e cenários | `active` | UXA-074; UXA-075 |
| catálogo integrado | `active` 0.12.0 | UXA-087 |
| registro de superfícies | `active` 0.5.0 | UXA-087 |
| registro de transições | `active` 0.4.0 | UXA-086; GKR-TRN-112 continua parcial |
| detalhamento do Coletivo | `active` 0.4.0 | UXA-087 |
| demais detalhamentos | `active` 0.2.0 | UXA-080 |
| galeria visual integrada | `active` 0.7.0 | UXA-087 |
| página de Coletivos | `active` 0.5.0 | UXA-087 |
| demais páginas visuais | `active` 0.3.0 | UXA-085 |
| matriz por SVG | `active` 0.5.0 | UXA-087 |
| registro de lacunas | `active` 0.12.0 | UXA-087 |
| protótipo, aplicação e motor | não iniciados | — |
| Engenharia de Produto | não iniciada | W0-01 |

## 6. Resultado da UXA-087

A UXA-087 valida funcionalmente `GKR-SURF-COL-002 — Visão Geral do Responsável` após reformular o mesmo SVG criado na UXA-086.

A validação confirma:

- representação e escopo de autoridade explícitos;
- momento operacional compreensível;
- atenção principal com prazo verificável;
- alternativa de adiamento e contestação sem penalidade;
- proteção de dados e ausência de acesso automático à jornada pessoal;
- retorno explícito ao contexto anterior;
- separação entre síntese e operação especializada.

Ela não:

- adiciona novo SVG;
- materializa a fila completa de solicitações;
- valida `GKR-TRN-112` ponta a ponta;
- promove a jornada do Coletivo;
- inicia protótipo, aplicação ou Engenharia de Produto.

## 7. Cobertura visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 98 |
| associações individuais | 98 |
| perfis de rastreabilidade | 24 |
| com validação funcional registrada | 88 |
| pendentes de validação específica | 10 |
| IDs com referência visual | 26 de 40 |
| responsabilidades sem SVG dedicado | 13 |
| fronteira sem tela por definição | 1 |

Os dez pendentes remanescentes pertencem exclusivamente à UXA-055.

## 8. Ressalvas

- perfis agregados não substituem análise exclusiva por estado;
- dez estados da UXA-055 permanecem sem validação;
- `GKR-TRN-112` permanece parcial porque seu destino operacional não existe;
- continuidades entre pacotes permanecem parciais ou não examinadas;
- uma superfície validada não equivale a jornada validada.

## 9. Prioridade de Coletivos

```text
Visão Geral do Responsável — validada
→ gestão completa de solicitações — ausente
→ Meus Coletivos — ausente
→ Central de Atualizações — ausente
→ Início do Participante — reformulação pendente
```

O avanço para a segunda superfície depende de autorização separada.

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

**UXA-088 — Materialização Controlada da Gestão de Solicitações do Responsável do Coletivo (`GKR-SURF-COL-003`)**, mediante autorização separada.

A UXA-088 não foi iniciada.
