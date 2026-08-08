---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.30.0
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
  - UXA-096
  - UXA-097
  - UXA-098
  - UXA-099
  - UXA-100
  - UXA-100-A1
  - UXA-100-A2
  - UXA-100-A3
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-GALLERY-PLANS-001
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
- [Planos, Comparação e Cobrança — Galeria Canônica](screen-gallery-plans-billing.md)
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
UXA-090 — cinco handoffs de solicitação validados ponta a ponta
→ UXA-091 — Meus Coletivos materializada
→ UXA-092 — Meus Coletivos e TRN-108 validados
→ UXA-093 — Central materializada
→ UXA-094 — Central e TRN-110 validadas
→ UXA-095 — Início do Participante materializado; TRN-111 parcial
→ UXA-096 — Central/Início revalidados e TRN-111 validada ponta a ponta
→ UXA-097 — primeira Tela Hoje materializada; PER-007 revalidada; TRN-007 validada ponta a ponta
→ UXA-098 — publicação, descoberta, Mapa, Lista e Detalhe validados como continuidade integrada
→ UXA-099 — dez estados residuais Opportunity Boost validados
→ UXA-100 / A1 — planos, comparação, cobrança, telas e jornadas materializados
→ UXA-100-A2 — 9/9 ativos auditados e aprovados funcionalmente; 6 reformulados
→ UXA-100-A3 — fragmentação mínima e promoção canônica de Planos
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 4. Estado documental

| Camada | Estado | Referência |
|---|---|---|
| visão geral das Jornadas Integradas | `active` 0.30.0 | UXA-100-A3 |
| Pessoa, Coletivo e Organização | `draft` | incompletude explícita preservada |
| Jornada da Pessoa | `draft` 0.14.0 | PER-301 a 304; TRN-401 a 405 |
| Jornada do Coletivo | `draft` 0.15.0 | COL-301 a 304; TRN-411 a 416 |
| Jornada da Organização | `draft` 0.7.0 | ORG-301 a 304; TRN-421 a 426 |
| catálogo integrado | `active` 0.25.0 | 118 SVGs canônicos |
| registro de superfícies | `active` 0.16.0 | 53 IDs |
| registro de transições | `active` 0.17.0 | 54 transições |
| galeria visual integrada | `active` 0.20.0 | 118 SVGs canônicos |
| galeria de Planos | `active` 0.3.0 | 9 SVGs canônicos |
| matriz por SVG | `active` 0.16.0 | 118 associações / 31 perfis |
| registro de lacunas | `active` | cobrança/processo comercial e outras continuidades preservadas |
| protótipo, aplicação e motor | não iniciados | — |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 5. Etapa transversal canônica de Planos

A UXA-100-A3 registra a mesma estrutura funcional nos três participantes:

```text
*-301 Planos e comparação
├── upgrade → *-302 revisão de contratação → *-304 resultado/recuperação → *-301
├── downgrade/cancelamento → *-303 gestão do ciclo → *-304 → *-301
└── Enterprise/Scale → BND-002 quando aplicável
```

A entrada em Planos continua legítima por dois caminhos:

1. **voluntário**, pela área de conta/administração, sem necessidade de atingir limite;
2. **contextual**, quando uma capacidade do plano é atingida, sempre preservando alternativas gratuitas ou operacionais aplicáveis.

A promoção não inventa IDs para superfícies de origem que ainda não estejam suficientemente definidas. Comparação incremental permanece estado de `*-301`, processamento de pagamento permanece transitório e `BND-002` é fronteira, não checkout.

## 6. Cobertura canônica após UXA-100-A3

| Indicador | Resultado |
|---|---:|
| SVGs canônicos existentes | **118** |
| associações individuais canônicas | **118** |
| perfis de rastreabilidade | **31** |
| com validação funcional vigente | **118** |
| pendentes de validação específica | **0** |
| superfícies/estados/fronteiras | **53** |
| transições documentais | **54** |
| IDs com referência visual | **42 de 53** |
| responsabilidades sem SVG dedicado | **9** |
| fronteiras sem tela por definição | **2** |

## 7. Maturidade das transições de Planos

- Pessoa: `TRN-401` a `405` — **localmente validadas**;
- Coletivo: `TRN-411` a `415` — **localmente validadas**; `TRN-416` — **parcial**;
- Organização: `TRN-421` a `425` — **localmente validadas**; `TRN-426` — **parcial**.

A maturidade preserva a diferença entre validação funcional documental e cobrança/processo comercial reais.

## 8. Continuidades anteriores preservadas

`TRN-203`, `TRN-204`, `TRN-210` e `TRN-211` permanecem integralmente validadas pela UXA-098. `TRN-007` permanece integralmente validada pela UXA-097. Oito handoffs permanecem integralmente validados no trecho governado de Coletivos: `TRN-105`, `106`, `107`, `108`, `109`, `110`, `111` e `112`.

## 9. Separações obrigatórias

- Planos canonicamente registrado não equivale a checkout implementado;
- promoção de SVG/ID não equivale a promoção da jornada inteira;
- pagar um plano não altera relevância orgânica, confiança, legitimidade, impacto ou evolução;
- limite comercial não apaga direitos essenciais ou alternativas gratuitas legítimas;
- sucesso e falha permanecem consequências diferentes, mesmo agrupados na família de resultado/recuperação;
- Enterprise/Scale termina em `BND-002` até processo comercial posterior ser materializado;
- validar `COM-005` não valida automaticamente `TRN-305`;
- validação documental não equivale a implementação técnica.

## 10. Estado da frente

A fragmentação e promoção canônica da UXA-100 está concluída documentalmente pela UXA-100-A3. Permanecem separadas a validação ponta a ponta de cobrança real, o processo comercial após `BND-002`, as entradas contextuais sem origem canônica própria e outras lacunas das jornadas. Nenhuma próxima UXA é iniciada automaticamente.