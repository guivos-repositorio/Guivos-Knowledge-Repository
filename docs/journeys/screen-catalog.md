---
id: GKR-JOURNEY-SCREEN-CATALOG-001
title: Catálogo Integrado de Telas
status: active
version: 0.25.0
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
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-GALLERY-PLANS-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Catálogo Integrado de Telas

## 1. Regra de leitura

```text
SVG existente
≠ superfície granular adicional por padrão
≠ transição integralmente validada automaticamente
≠ jornada integrada validada
≠ implementação técnica
```

A UXA-100-A3 promove os nove SVGs de Planos após a validação funcional da UXA-100-A2. A promoção segue fragmentação mínima: comparação e estados transitórios não recebem tela própria apenas por existirem no board.

## 2. Inventário agregado canônico por família

| Participante ou camada | Família | SVGs | Validação funcional vigente | Continuidade integrada | Lacuna associada |
|---|---|---:|---|---|---|
| Pessoa | Home pública | 1 | validado | entrada protegida parcial | continuidade entre pacotes |
| Pessoa | início protegido | 4 | 4 validados | parcial | reconciliação ponta a ponta |
| Pessoa | expressão guiada | 8 | 8 validados | parcial | integração com inventário |
| Pessoa | compreensão inicial | 5 | 5 validados | **TRN-007 integralmente validada** | handoffs anteriores ainda parciais |
| Pessoa | Tela Hoje | 2 | 2 validados | primeira entrada validada; recorrência separada | estados alternativos de Hoje |
| Pessoa | oportunidades orgânicas | 7 | 7 validados | publicação/descoberta e Mapa/Lista/Detalhe integrados | efeito externo separado |
| Pessoa | Planos, comparação e cobrança | **3** | **3 validados** | TRN-401 a 405 localmente validadas | gateway/proration e entradas externas específicas |
| Pessoa em Coletivos | descoberta e busca | 5 | 5 validados | parcial | continuidade entre famílias |
| Pessoa em Coletivos | Perfil Público | 4 | 4 validados | parcial | handoff para solicitação |
| Pessoa em Coletivos | revisão e solicitação | 5 | 5 validados | parcial | handoff bilateral |
| Pessoa em Coletivos | Solicitação Pendente | 8 | 8 validados | TRN-105/106/107/108/109 nos gates aplicáveis | outras continuidades separadas |
| Pessoa em Coletivos | Meus Coletivos | 1 | validado | TRN-108 e TRN-110 integralmente validadas | P0B separado |
| Pessoa em Coletivos | Central de Atualizações | 1 | validado | TRN-110 e TRN-111 integralmente validadas | P0B/P1 separados |
| Pessoa em Coletivos | Início do Participante | 1 | validado | TRN-111 integralmente validada | P0B e áreas internas separadas |
| Coletivo | referência inicial | 1 | validado | parcial | continuidade com gestão |
| Coletivo | Visão Geral do Responsável | 1 | validado | TRN-112 integralmente validada | gestão especializada |
| Coletivo | gestão de solicitações | 7 | 7 validados | handoffs aplicáveis integralmente validados | operação interna posterior |
| Coletivo | Planos, comparação e cobrança | **3** | **3 validados** | TRN-411 a 415 locais; TRN-416 parcial | processo Enterprise e cobrança real |
| Organização | visão geral e cadastro | 2 | 2 validados | publicação–descoberta integralmente validada em TRN-203 | matriz institucional completa |
| Organização | Planos, comparação e cobrança | **3** | **3 validados** | TRN-421 a 425 locais; TRN-426 parcial | processo Scale e cobrança real |
| camada comercial | Opportunity Boost | 46 | **46 validados** | parcial | TRN-304/305/306 e integrações específicas |
| fronteira documental | destinos externos/comerciais | 0 | não aplicável | não examinada/parcial | BND-001 efeito externo; BND-002 processo Enterprise/Scale |
| **Total canônico** |  | **118** | **118 validados; 0 pendentes** |  |  |

## 3. Frente UXA-100 promovida

A UXA-100-A3 promove os nove ativos da frente:

| Participante | Tela dedicada de Planos | Board de fluxo | Comparação incremental | Total canônico | Perfil |
|---|---:|---:|---:|---:|---|
| Pessoa | 1 | 1 | 1 | 3 | R29 |
| Coletivo | 1 | 1 | 1 | 3 | R30 |
| Organização | 1 | 1 | 1 | 3 | R31 |
| **Total UXA-100** | **3** | **3** | **3** | **9** | **3 perfis** |

Referência de inspeção: [Planos, Comparação e Cobrança — Galeria Canônica](screen-gallery-plans-billing.md).

Fragmentação promovida:

- Pessoa: `PER-301` a `PER-304`;
- Coletivo: `COL-301` a `COL-304`;
- Organização: `ORG-301` a `ORG-304`;
- fronteira comercial compartilhada: `BND-002`.

Comparação incremental pertence a `*-301`; processamento não recebe superfície própria; resultado confirmado e falha pertencem a `*-304` como estados diferentes da mesma responsabilidade.

## 4. Instrumentos granulares vigentes

| Registro | Quantidade | Estado vigente |
|---|---:|---|
| superfícies/estados/responsabilidades/fronteiras | **53** | `active` 0.16.0 |
| transições documentais | **54** | `active` 0.17.0 |
| detalhamento da Pessoa | 23 entradas | `active` 0.10.0 |
| detalhamento do Coletivo | 12 entradas | `active` 0.7.0 |
| detalhamento da Organização | 11 entradas | `active` 0.3.0 |
| catálogo canônico | **118 SVGs** | `active` 0.25.0 |
| matriz de rastreabilidade | **118 SVGs / 31 perfis** | `active` 0.16.0 |

## 5. Cobertura visual canônica

| Condição | Quantidade |
|---|---:|
| IDs com referência visual direta ou agrupada | **42** |
| responsabilidades sem SVG dedicado | **9** |
| fronteiras intencionalmente sem tela | **2** |
| **Total** | **53** |

## 6. Efeito da UXA-100-A3 no catálogo

- SVGs canônicos: **109 → 118**;
- associações: **109 → 118**;
- perfis: **28 → 31**;
- validações funcionais vigentes: **109 → 118**;
- pendências específicas: **0 → 0**;
- IDs: **40 → 53**;
- transições: **37 → 54**;
- IDs com referência visual: **30 → 42**;
- fronteiras sem tela: **1 → 2**;
- Pessoa, Coletivo e Organização permanecem `draft`;
- nenhuma implementação de cobrança é criada.

## 7. Separações obrigatórias

- primeira Tela Hoje e Tela Hoje recorrente são variantes do mesmo `PER-008`, não novos IDs;
- `PER-106` organiza participações e não substitui a Central;
- `PER-107` é triagem de atualizações;
- `PER-108` sintetiza o contexto interno e não replica canais especializados;
- `PER/COL/ORG-301` concentram plano atual e comparação; comparação incremental não é uma tela adicional;
- `PER/COL/ORG-302` são revisão de contratação; processamento financeiro transitório não é tela própria;
- `PER/COL/ORG-303` governam downgrade/cancelamento e suas consequências;
- `PER/COL/ORG-304` governam resultado/recuperação e preservam a diferença entre sucesso e falha;
- `BND-002` é fronteira de proposta Enterprise/Scale, não checkout;
- plano pago não compra relevância, legitimidade, confiança, impacto ou evolução;
- `COM-005` continua validado pela UXA-099 sem promover automaticamente `TRN-305`;
- `TRN-205`, `TRN-304`, `TRN-305` e `TRN-306` permanecem continuidades separadas.

## 8. Estado do catálogo

- catálogo: `active` 0.25.0;
- galeria principal: **118 SVGs canônicos**;
- galeria de Planos: `active` 0.3.0; 9 SVGs canônicos;
- matriz por SVG: `active` 0.16.0; 118 associações / 31 perfis;
- jornadas da Pessoa, Coletivo e Organização: `draft`, com Planos canonicamente registrado;
- protótipo e Engenharia de Produto: não iniciados.

A promoção documental não autoriza merge, implementação ou próxima UXA.