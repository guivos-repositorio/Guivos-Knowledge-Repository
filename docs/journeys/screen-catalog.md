---
id: GKR-JOURNEY-SCREEN-CATALOG-001
title: Catálogo Integrado de Telas
status: active
version: 0.27.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-08
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
  - UXA-101
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

A UXA-101 reformula o SVG de Detalhe de Oportunidade para incluir a revisão consciente pré-saída no próprio `PER-203`. Não cria novo ID nem novo SVG; `BND-001` continua sem tela.

## 2. Inventário agregado canônico por família

| Participante ou camada | Família | SVGs | Validação funcional vigente | Continuidade integrada | Lacuna associada |
|---|---|---:|---|---|---|
| Pessoa | Home pública | 1 | validado | entrada protegida parcial | continuidade entre pacotes |
| Pessoa | início protegido | 4 | 4 validados | parcial | reconciliação ponta a ponta |
| Pessoa | expressão guiada | 8 | 8 validados | parcial | integração com inventário |
| Pessoa | compreensão inicial | 5 | 5 validados | **TRN-007 integralmente validada** | handoffs anteriores ainda parciais |
| Pessoa | Tela Hoje | 2 | 2 validados | primeira entrada validada; recorrência separada | estados alternativos de Hoje |
| Pessoa | oportunidades orgânicas | 7 | **7 validados; Detalhe revalidado pela UXA-101** | publicação/descoberta, Mapa/Lista/Detalhe e saída até BND-001 integrados | processo externo posterior separado |
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
| Coletivo | Planos, comparação e cobrança | **3** | **3 validados** | TRN-411 a 415 locais; TRN-416 parcial | contratação/dimensionamento assistido e cobrança real |
| Organização | visão geral e cadastro | 2 | 2 validados | publicação–descoberta integralmente validada em TRN-203 | matriz institucional completa |
| Organização | Planos, comparação e cobrança | **3** | **3 validados** | TRN-421 a 425 locais; TRN-426 parcial | contratação/dimensionamento assistido e cobrança real |
| camada comercial | Opportunity Boost | 46 | **46 validados** | parcial | TRN-304/305/306 e integrações específicas |
| fronteira documental | destinos externos/comerciais | 0 | não aplicável | BND-001 examinada; BND-002 parcial | processo externo posterior; contratação/dimensionamento assistido |
| **Total canônico** |  | **118** | **118 validados; 0 pendentes** |  |  |

## 3. Instrumentos granulares vigentes

| Registro | Quantidade | Estado vigente após UXA-101 |
|---|---:|---|
| superfícies/estados/responsabilidades/fronteiras | **53** | `active` 0.17.0 |
| transições documentais | **54** | `active` 0.18.0 |
| catálogo canônico | **118 SVGs** | `active` 0.27.0 |
| matriz de rastreabilidade | **118 SVGs / 31 perfis** | `active` 0.17.0 |
| galeria visual | **118 SVGs** | `active` 0.21.0 |

## 4. Cobertura visual canônica

| Condição | Quantidade |
|---|---:|
| IDs com referência visual direta ou agrupada | **42** |
| responsabilidades sem SVG dedicado | **9** |
| fronteiras intencionalmente sem tela | **2** |
| **Total** | **53** |

## 5. Efeito da UXA-101 no catálogo

- SVGs canônicos: **118 → 118**;
- associações: **118 → 118**;
- perfis: **31 → 31**;
- validações funcionais vigentes: **118 → 118**;
- pendências específicas: **0 → 0**;
- IDs: **53 → 53**;
- transições: **54 → 54**;
- `uxa-007-opportunity-detail-mobile.svg`: reformulado e revalidado;
- `TRN-205`: parcial → **integralmente validada até BND-001**;
- `BND-001`: examinada como fronteira externa sem tela.

## 6. Separações obrigatórias

- primeira Tela Hoje e Tela Hoje recorrente são variantes do mesmo `PER-008`;
- revisão de saída é estado do mesmo `PER-203`, não nova tela canônica;
- `BND-001` representa a transferência de autoridade, não o processo do terceiro;
- `PER-106` organiza participações e não substitui a Central;
- `PER-107` é triagem de atualizações;
- `PER-108` sintetiza contexto interno e não replica canais especializados;
- comparação incremental de Planos não é tela adicional;
- processamento financeiro transitório não é tela própria;
- `BND-002` representa contratação/dimensionamento assistido quando aplicável e não é plano Enterprise ou Scale;
- Coletivo usa `Livre · Mobiliza · Impacta · Rede`;
- Organização usa `Conecta · Eleva · Transforma`;
- Guivos Business usa `Start · Growth · Scale · Enterprise` como Produto Especializado separado;
- `TRN-304`, `TRN-305`, `TRN-306`, `TRN-416` e `TRN-426` permanecem continuidades separadas.

## 7. Estado do catálogo

- catálogo: `active` 0.27.0;
- galeria principal: `active` 0.21.0; 118 SVGs;
- matriz por SVG: `active` 0.17.0; 118 associações / 31 perfis;
- jornadas da Pessoa, Coletivo e Organização: `draft`;
- protótipo e Engenharia de Produto: não iniciados.

A promoção documental não autoriza implementação ou próxima UXA.
