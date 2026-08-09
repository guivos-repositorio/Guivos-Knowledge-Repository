---
id: GKR-JOURNEY-SCREEN-GALLERY-001
title: Galeria Visual Integrada de Telas
status: active
version: 0.23.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-09
related:
  - UXA-005
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
  - UXA-100-A4
  - UXA-101
  - GKR-UX-D5-C1-001
  - GKR-UX-D5-C2-001
  - GKR-JOURNEY-SCREEN-GALLERY-PLANS-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Galeria Visual Integrada de Telas

## 1. Finalidade

Esta seção reúne os **121 SVGs canônicos** para inspeção humana de assertividade, sequência, coerência e cobertura.

A D5-C2 adiciona três estados-base low-fidelity para responsabilidades já contratadas pela D5-C1: `PER-010 — Meus Objetivos`, `PER-011 — Meus Próximos Passos` e `PER-012 — Minha Evolução`. Esses três SVGs são materializações pendentes de validação funcional; os 118 ativos anteriores preservam suas validações vigentes.

## 2. Estado do instrumento

A galeria permanece `active` como instrumento de inspeção. Esse status não significa que as jornadas estejam automaticamente aprovadas.

Ressalvas vigentes:

- **121 SVGs canônicos** compartilham **34 perfis de rastreabilidade**;
- **10 responsabilidades** continuam sem SVG dedicado;
- **duas fronteiras** permanecem corretamente sem tela;
- **118 SVGs possuem validação funcional documental vigente**;
- **3 aguardam validação funcional específica** — `PER-010`, `PER-011`, `PER-012`;
- `TRN-008..013` permanecem contratadas apesar da materialização visual de seus destinos/origens;
- `TRN-406/407` estão contratadas porque `PER-009` ainda não foi materializada;
- `TRN-417/418` e `TRN-427/428` estão integralmente validadas no limite documental de navegação administrativa;
- `TRN-205` está validada até `BND-001` pela UXA-101, sem validar o processo externo posterior;
- `TRN-304`, `TRN-305`, `TRN-306`, `TRN-416` e `TRN-426` permanecem parciais;
- as 15 transições comerciais internas de Planos permanecem localmente validadas;
- oito transições do trecho governado de Coletivos permanecem integralmente validadas: `105`, `106`, `107`, `108`, `109`, `110`, `111`, `112`.

## 3. Instrumentos de inspeção

- [Matriz de Rastreabilidade Visual por SVG](screen-gallery-traceability-matrix.md)
- [Catálogo Integrado de Telas](screen-catalog.md)
- [Planos, Comparação e Cobrança — Galeria Canônica](screen-gallery-plans-billing.md)
- [Registro Granular de Superfícies e Estados](surface-registry.md)
- [Registro Granular de Transições](transition-registry.md)
- [Lacunas e Continuidades Ausentes](gaps.md)

## 4. Rota canônica de inspeção

| Ordem | Página | SVGs | Continuidade examinada |
|---:|---|---:|---|
| 1 | [Pessoa — Fundação, Entrada, Compreensão e Recorrência](screen-gallery-person.md) | **23** | Home → início protegido → expressão → compreensão → primeira Hoje → recorrência → Objetivos/Próximos Passos/Evolução |
| 2 | [Organização e Oportunidades](screen-gallery-opportunities-organization.md) | 9 | publicação → mapa/lista → detalhe → revisão de saída → fronteira |
| 3 | [Coletivos](screen-gallery-collectives.md) | 34 | descoberta → solicitação → gestão → Meus Coletivos → Central → Início |
| 4 | [Opportunity Boost — Configuração e Exposição](screen-gallery-opportunity-boost-exposure.md) | 20 | configuração → exposição → retorno orgânico |
| 5 | [Opportunity Boost — Operação, Relatórios e Resíduos](screen-gallery-opportunity-boost-operations.md) | 26 | gestão → relatório → estados residuais |
| 6 | [Planos, Comparação e Cobrança](screen-gallery-plans-billing.md) | **9** | origem administrativa → plano atual → comparação → contratação/ciclo → resultado/recuperação → retorno |
|  | **Total canônico** | **121** | **118 validados; 3 pendentes** |

## 5. Cobertura canônica confirmada

| Indicador | Resultado |
|---|---:|
| SVGs canônicos existentes e referenciados | **121** |
| associações individuais canônicas | **121** |
| perfis de rastreabilidade | **34** |
| com validação funcional vigente | **118** |
| pendentes de validação específica | **3** |
| superfícies/estados/fronteiras | **57** |
| transições documentais | **66** |
| IDs com referência visual | **45 de 57** |
| responsabilidades sem SVG dedicado | **10** |
| fronteiras documentais sem tela | **2** |

## 6. Responsabilidades sem SVG dedicado

Após D5-C2, permanecem sem SVG dedicado:

- `GKR-SURF-PER-009`;
- `GKR-SURF-COL-004` a `GKR-SURF-COL-008`;
- `GKR-SURF-ORG-004` a `GKR-SURF-ORG-007`.

`GKR-SURF-BND-001` e `GKR-SURF-BND-002` permanecem intencionalmente sem tela Guivos. O estado de revisão de saída pertence a `PER-203` e não altera essa regra.

## 7. Fronteiras de validação

A existência de 121 SVGs não implica 121 validações nem que todas as 66 transições estejam integralmente validadas. Em particular:

- `PER-010`, `PER-011` e `PER-012` estão materializados e **pendentes de validação funcional**;
- `TRN-008..013` permanecem contratadas;
- `TRN-406/407` permanecem contratadas;
- `TRN-417/418` e `TRN-427/428` são integrais apenas para navegação administrativa e retorno sem efeito comercial;
- `TRN-205` é integral somente **até a fronteira de autoridade Guivos**;
- `TRN-401` a `405`, `411` a `415` e `421` a `425` são localmente validadas;
- `TRN-304`, `305`, `306`, `416` e `426` permanecem parciais;
- cobrança real, gateway, proration e processo após `BND-002` permanecem fora do escopo.

O status `active` aprova somente os instrumentos documentais de inspeção. Não inicia protótipo ou Engenharia de Produto.

## 8. Estado após D5-C2

D5-C2 adiciona três SVGs sem criar nova responsabilidade granular: `PER-010..012` já existiam desde D5-C1. Os três ativos entram na galeria como materializados e pendentes de validação, e `TRN-008..013` permanecem contratadas.

V4 continua encerrada pela UXA-101 no limite controlável pela Guivos. Pessoa, Coletivo e Organização continuam `draft`; V5/UXA-102, D6 e D7 não foram iniciadas e nenhuma implementação técnica é iniciada automaticamente.
