---
id: GKR-JOURNEY-SCREEN-GALLERY-001
title: Galeria Visual Integrada de Telas
status: active
version: 0.20.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
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

Esta seção reúne os **118 SVGs canônicos** para inspeção humana de assertividade, sequência, coerência e cobertura.

A UXA-100-A3 incorpora os nove ativos de Planos funcionalmente aprovados pela UXA-100-A2. A promoção cria identidade canônica para as famílias de Planos, mas não converte cada estado do board em tela independente nem comprova implementação de cobrança.

## 2. Estado do instrumento

A galeria permanece `active` como instrumento de inspeção. Esse status não significa que as jornadas estejam automaticamente aprovadas.

Ressalvas vigentes:

- **118 SVGs canônicos** compartilham **31 perfis de rastreabilidade**;
- 9 responsabilidades continuam sem SVG dedicado;
- **duas fronteiras** permanecem corretamente sem tela;
- **118 SVGs possuem validação funcional documental vigente**;
- **0 aguardam validação funcional específica**;
- a UXA-100-A3 adiciona 12 superfícies de Planos e `BND-002`, sem criar novos SVGs além dos 9 já materializados;
- as 15 transições internas de Planos são localmente validadas e `TRN-416/426` permanecem parciais;
- validar os dez estados de `COM-005` não promove automaticamente `TRN-305`;
- `TRN-205`, `TRN-304` e `TRN-306` permanecem parciais;
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
| 1 | [Pessoa — Fundação, Entrada, Compreensão e Recorrência](screen-gallery-person.md) | **20** | Home → início protegido → expressão → compreensão → primeira Hoje → recorrência |
| 2 | [Organização e Oportunidades](screen-gallery-opportunities-organization.md) | 9 | publicação → mapa → lista → detalhe → fronteira |
| 3 | [Coletivos](screen-gallery-collectives.md) | 34 | descoberta → solicitação → gestão → Meus Coletivos → Central → Início |
| 4 | [Opportunity Boost — Configuração e Exposição](screen-gallery-opportunity-boost-exposure.md) | 20 | configuração → exposição → retorno orgânico |
| 5 | [Opportunity Boost — Operação, Relatórios e Resíduos](screen-gallery-opportunity-boost-operations.md) | 26 | gestão → relatório → estados residuais |
| 6 | [Planos, Comparação e Cobrança](screen-gallery-plans-billing.md) | **9** | plano atual → comparação → contratação/ciclo → resultado/recuperação |
|  | **Total canônico** | **118** | **118 validados; 0 pendentes** |

## 5. Planos — UXA-100

A galeria de Planos reúne:

| Participante | Tela dedicada de Planos | Fluxo | Comparação incremental | Total | Perfil |
|---|---:|---:|---:|---:|---|
| Pessoa | 1 | 1 | 1 | 3 | R29 |
| Coletivo | 1 | 1 | 1 | 3 | R30 |
| Organização | 1 | 1 | 1 | 3 | R31 |
| **Total** | **3** | **3** | **3** | **9** | **3 perfis** |

Esses ativos:

- estão associados à UXA-100/A1/A2/A3;
- permanecem referências nas três jornadas `draft`;
- foram funcionalmente aprovados pela UXA-100-A2;
- foram promovidos pela UXA-100-A3;
- cobrem `PER/COL/ORG-301` a `304`;
- não representam checkout, gateway ou cobrança implementados.

## 6. Cobertura canônica confirmada

| Indicador | Resultado |
|---|---:|
| SVGs canônicos existentes e referenciados | **118** |
| associações individuais canônicas | **118** |
| perfis de rastreabilidade | **31** |
| com validação funcional vigente | **118** |
| pendentes de validação específica | **0** |
| superfícies/estados/fronteiras | **53** |
| transições documentais | **54** |
| IDs com referência visual | **42 de 53** |
| responsabilidades sem SVG dedicado | **9** |
| fronteiras documentais sem tela | **2** |

## 7. Responsabilidades sem SVG dedicado

- `GKR-SURF-COL-004` a `GKR-SURF-COL-008`;
- `GKR-SURF-ORG-004` a `GKR-SURF-ORG-007`.

`GKR-SURF-BND-001` e `GKR-SURF-BND-002` permanecem intencionalmente sem tela Guivos.

As superfícies de Planos possuem referência visual direta ou agrupada e, portanto, não aumentam a lista de responsabilidades sem SVG dedicado.

## 8. Fronteiras de validação

A validação dos 118 SVGs não implica que todas as 54 transições estejam integralmente validadas. Na frente de Planos:

- `TRN-401` a `405`, `411` a `415` e `421` a `425` são **localmente validadas**;
- `TRN-416` e `TRN-426` são **parciais**;
- cobrança real, gateway, proration e processo após `BND-002` permanecem fora do escopo.

Também permanecem parciais `TRN-205`, `TRN-304`, `TRN-305` e `TRN-306`.

O status `active` aprova somente os instrumentos documentais de inspeção. Não inicia protótipo ou Engenharia de Produto.

## 9. Estado após UXA-100-A3

A fragmentação e promoção canônica de Planos está documentada. Pessoa, Coletivo e Organização continuam `draft`; nenhuma próxima UXA, integração à `main` ou implementação técnica é iniciada automaticamente.