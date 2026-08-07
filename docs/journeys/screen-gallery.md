---
id: GKR-JOURNEY-SCREEN-GALLERY-001
title: Galeria Visual Integrada de Telas
status: active
version: 0.18.0
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

Esta seção reúne os **109 SVGs canônicos** para inspeção humana de assertividade, sequência, coerência e cobertura e passa a apontar também para um **apêndice candidato UXA-100 com 9 SVGs de Planos, comparação e cobrança**.

Os 9 ativos candidatos não integram a contagem canônica até validação funcional e promoção governada.

## 2. Estado do instrumento

A galeria permanece `active` como instrumento de inspeção. Esse status não significa que as jornadas estejam automaticamente aprovadas.

Ressalvas vigentes:

- 109 SVGs canônicos compartilham 28 perfis de rastreabilidade;
- 9 responsabilidades continuam sem SVG dedicado no conjunto canônico;
- uma fronteira permanece corretamente sem tela;
- **109 SVGs canônicos possuem validação funcional vigente**;
- **0 aguardam validação funcional específica** no conjunto canônico;
- a UXA-100 adiciona **9 SVGs candidatos ainda não validados funcionalmente**;
- validar os dez estados de `COM-005` não promove automaticamente `TRN-305`;
- `TRN-205`, `TRN-304` e `TRN-306` permanecem parciais;
- oito transições do trecho governado de Coletivos permanecem integralmente validadas: `105`, `106`, `107`, `108`, `109`, `110`, `111`, `112`.

## 3. Instrumentos de inspeção

- [Matriz de Rastreabilidade Visual por SVG](screen-gallery-traceability-matrix.md)
- [Catálogo Integrado de Telas](screen-catalog.md)
- [Planos, Comparação e Cobrança — Galeria Candidata](screen-gallery-plans-billing.md)
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
|  | **Total canônico** | **109** | **109 validados; 0 pendentes** |

## 5. Apêndice candidato UXA-100 — Planos

A [galeria candidata de Planos](screen-gallery-plans-billing.md) reúne 9 SVGs:

| Participante | Tela dedicada de Planos | Fluxo | Comparação incremental | Total |
|---|---:|---:|---:|---:|
| Pessoa | 1 | 1 | 1 | 3 |
| Coletivo | 1 | 1 | 1 | 3 |
| Organização | 1 | 1 | 1 | 3 |
| **Total candidato** | **3** | **3** | **3** | **9** |

Esses ativos:

- estão associados à UXA-100;
- foram inseridos como referências nas três jornadas `draft`;
- não possuem IDs canônicos de superfície/transição;
- não alteram a matriz canônica de 109 SVGs;
- não representam checkout, cobrança ou oferta comercial implementados.

## 6. Cobertura canônica confirmada

| Indicador | Resultado |
|---|---:|
| SVGs canônicos existentes e referenciados | **109** |
| associações individuais canônicas | **109** |
| perfis de rastreabilidade | **28** |
| com validação funcional vigente | **109** |
| pendentes de validação específica | **0** |
| IDs com referência visual | **30 de 40** |
| responsabilidades sem SVG dedicado | **9** |
| fronteira documental sem tela | 1 |
| SVGs candidatos UXA-100 | **9** |

## 7. Responsabilidades sem SVG dedicado

- `GKR-SURF-COL-004` a `GKR-SURF-COL-008`;
- `GKR-SURF-ORG-004` a `GKR-SURF-ORG-007`.

`GKR-SURF-BND-001` permanece intencionalmente sem tela Guivos.

As novas telas de Planos não reduzem essa lacuna canônica porque ainda não foram promovidas a IDs de superfície.

## 8. Fronteiras de validação

A validação dos 109 SVGs canônicos não implica que todas as 37 transições estejam integralmente validadas. Permanecem continuidades parciais, entre elas `TRN-305`, `TRN-205`, `TRN-304` e `TRN-306`.

A existência dos 9 SVGs candidatos da UXA-100 também não implica validação funcional, superfície registrada ou transição integrada.

O status `active` aprova somente os instrumentos documentais de inspeção. Não inicia protótipo ou Engenharia de Produto.

## 9. Próxima decisão

A UXA-100 passa a ter telas de Planos e integração candidata às três jornadas. O próximo ato governado é validar funcionalmente os 9 ativos candidatos e somente depois decidir sua promoção ao conjunto canônico.