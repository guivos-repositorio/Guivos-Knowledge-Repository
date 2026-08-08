---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.29.0
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
- [Planos, Comparação e Cobrança — Galeria Candidata](screen-gallery-plans-billing.md)
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
→ UXA-100 / UXA-100-A1 — planos, comparação, cobrança e telas dedicadas materializados como candidatos
→ UXA-100-A2 — 9/9 ativos de Planos auditados e aprovados funcionalmente como candidatos; 6 reformulados
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 4. Estado documental

| Camada | Estado | Referência |
|---|---|---|
| visão geral das Jornadas Integradas | `active` 0.29.0 | UXA-100-A2 |
| Pessoa, Coletivo e Organização | `draft` | incompletude explícita |
| Jornada da Pessoa | `draft` 0.13.0 | Planos aprovado funcionalmente como candidato |
| Jornada do Coletivo | `draft` 0.14.0 | Planos aprovado funcionalmente como candidato |
| Jornada da Organização | `draft` 0.6.0 | Planos aprovado funcionalmente como candidato |
| handoffs e cenários | `active` | sínteses preservadas |
| catálogo integrado | `active`; conjunto candidato separado | 109 SVGs canônicos + 9 candidatos aprovados funcionalmente |
| registro de superfícies | `active` 0.15.0 | sem IDs de Planos ainda |
| detalhamento da Pessoa | `active` 0.9.0 | sem alteração canônica |
| registro de transições | `active` 0.16.0 | sem transições de Planos ainda |
| galeria visual integrada | `active`; apêndice candidato separado | 109 canônicos + 9 candidatos |
| galeria candidata de Planos | `draft` 0.2.0 | 9/9 aprovados funcionalmente como candidatos |
| matriz por SVG | `active` 0.15.0 | canônica preservada |
| registro de lacunas | `active` 0.24.0 | sem promoção automática |
| protótipo, aplicação e motor | não iniciados | — |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 5. Etapa transversal de Planos — UXA-100

A UXA-100 introduz uma etapa transversal candidata nas três jornadas:

```text
área do participante
→ Planos
→ plano atual + uso/capacidade
→ comparação geral + diferença incremental
→ manter / upgrade / downgrade / cancelar / solicitar proposta
→ revisão de contratação quando aplicável
→ pagamento simulado ou processo comercial governado
→ retorno ao contexto anterior
```

A entrada em Planos ocorre por dois caminhos legítimos:

1. **voluntário**, pela área de conta/administração, sem necessidade de atingir limite;
2. **contextual**, quando uma capacidade do plano é atingida, sempre preservando alternativas gratuitas ou operacionais aplicáveis.

Telas dedicadas candidatas:

- Pessoa: `uxa-100-person-plans-screen-mobile.svg`;
- Coletivo: `uxa-100-collective-plans-screen-desktop.svg`;
- Organização: `uxa-100-organization-plans-screen-desktop.svg`.

A UXA-100-A2 aprovou funcionalmente os nove ativos como candidatos. Eles ainda não possuem IDs canônicos de superfície ou transição.

## 6. Cobertura canônica preservada

| Indicador | Resultado vigente antes de eventual promoção da UXA-100 |
|---|---:|
| SVGs canônicos existentes | **109** |
| associações individuais canônicas | **109** |
| perfis de rastreabilidade | **28** |
| com validação funcional vigente no conjunto canônico | **109** |
| pendentes de validação específica no conjunto canônico | **0** |
| IDs com referência visual | **30 de 40** |
| responsabilidades sem SVG dedicado | **9** |
| fronteira sem tela por definição | 1 |
| SVGs candidatos de Planos funcionalmente aprovados | **9 de 9** |

Os 9 SVGs da UXA-100 permanecem **fora da contagem canônica** até promoção governada.

## 7. Continuidades anteriores preservadas

`TRN-203`, `TRN-204`, `TRN-210` e `TRN-211` permanecem integralmente validadas pela UXA-098. `TRN-007` permanece integralmente validada pela UXA-097. Oito handoffs permanecem integralmente validados no trecho governado de Coletivos: `TRN-105`, `106`, `107`, `108`, `109`, `110`, `111` e `112`.

## 8. Separações obrigatórias

- Planos como etapa de jornada não equivale a checkout implementado;
- tela funcionalmente aprovada como candidata não equivale a superfície canônica registrada;
- pagar um plano não altera relevância orgânica, confiança, legitimidade ou evolução;
- limite comercial não apaga direitos essenciais ou alternativas gratuitas legítimas;
- validar `COM-005` não valida automaticamente `TRN-305`;
- estados residuais publicitários não alteram catálogo, busca ou ordenação orgânicos;
- repetir a mesma intenção não duplica efeito lógico;
- validação documental não equivale a implementação técnica.

## 9. Próxima decisão da UXA-100

A validação funcional candidata foi concluída pela UXA-100-A2. O próximo ato possível é decidir, separadamente, **fragmentação e promoção canônica**: quantas superfícies devem existir, quais IDs devem ser criados e quais transições precisam ser registradas. Nenhuma dessas ações é automática.
