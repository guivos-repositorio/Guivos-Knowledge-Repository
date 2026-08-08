---
id: GKR-JOURNEY-SCREEN-CATALOG-001
title: Catálogo Integrado de Telas
status: active
version: 0.28.0
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
  - UXA-100-A4
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

A UXA-100-A4 reformula quatro SVGs canônicos in-place para explicitar origem/retorno de Planos em Coletivo e Organização. A contagem visual permanece 118. `PER-009` é responsabilidade sem SVG dedicado.

## 2. Inventário agregado canônico por família

| Participante ou camada | Família | SVGs | Validação funcional vigente | Continuidade integrada | Lacuna associada |
|---|---|---:|---|---|---|
| Pessoa | Home pública | 1 | validado | entrada protegida parcial | continuidade entre pacotes |
| Pessoa | início protegido | 4 | 4 validados | parcial | reconciliação ponta a ponta |
| Pessoa | expressão guiada | 8 | 8 validados | parcial | integração com inventário |
| Pessoa | compreensão inicial | 5 | 5 validados | **TRN-007 integralmente validada** | handoffs anteriores ainda parciais |
| Pessoa | Tela Hoje | 2 | 2 validados | primeira entrada validada; recorrência separada | estados alternativos de Hoje |
| Pessoa | oportunidades orgânicas | 7 | **7 validados; Detalhe revalidado pela UXA-101** | publicação/descoberta, Mapa/Lista/Detalhe e saída até BND-001 integrados | processo externo posterior separado |
| Pessoa | Conta/Configurações | **0** | sem SVG | TRN-406/407 contratadas | materialização própria de PER-009 somente se necessária |
| Pessoa | Planos, comparação e cobrança | **3** | **3 validados** | TRN-401 a 405 locais; origem voluntária contratada | gateway/proration e materialização de PER-009 |
| Pessoa em Coletivos | descoberta e busca | 5 | 5 validados | parcial | continuidade entre famílias |
| Pessoa em Coletivos | Perfil Público | 4 | 4 validados | parcial | handoff para solicitação |
| Pessoa em Coletivos | revisão e solicitação | 5 | 5 validados | parcial | handoff bilateral |
| Pessoa em Coletivos | Solicitação Pendente | 8 | 8 validados | TRN-105/106/107/108/109 nos gates aplicáveis | outras continuidades separadas |
| Pessoa em Coletivos | Meus Coletivos | 1 | validado | TRN-108 e TRN-110 integralmente validadas | P0B separado |
| Pessoa em Coletivos | Central de Atualizações | 1 | validado | TRN-110 e TRN-111 integralmente validadas | P0B/P1 separados |
| Pessoa em Coletivos | Início do Participante | 1 | validado | TRN-111 integralmente validada | P0B e áreas internas separadas |
| Coletivo | referência inicial | 1 | validado | parcial | continuidade com gestão |
| Coletivo | Visão Geral do Responsável | 1 | validado; navegação reformulada A4 | TRN-112 e TRN-417/418 integrais | gestão especializada |
| Coletivo | gestão de solicitações | 7 | 7 validados | handoffs aplicáveis integralmente validados | operação interna posterior |
| Coletivo | Planos, comparação e cobrança | **3** | **3 validados** | TRN-417/418 integrais; TRN-411 a 415 locais; TRN-416 parcial | contratação/dimensionamento assistido e cobrança real |
| Organização | visão geral e cadastro | 2 | 2 validados; ORG-001 reformulada A4 | TRN-427/428 integrais; publicação–descoberta integral em TRN-203 | matriz institucional completa |
| Organização | Planos, comparação e cobrança | **3** | **3 validados** | TRN-427/428 integrais; TRN-421 a 425 locais; TRN-426 parcial | contratação/dimensionamento assistido e cobrança real |
| camada comercial | Opportunity Boost | 46 | **46 validados** | parcial | TRN-304/305/306 e integrações específicas |
| fronteira documental | destinos externos/comerciais | 0 | não aplicável | BND-001 examinada; BND-002 parcial | processo externo posterior; contratação/dimensionamento assistido |
| **Total canônico** |  | **118** | **118 validados; 0 pendentes** |  |  |

## 3. Instrumentos granulares vigentes

| Registro | Quantidade | Estado vigente após UXA-100-A4 |
|---|---:|---|
| superfícies/estados/responsabilidades/fronteiras | **54** | `active` 0.19.0 |
| transições documentais | **60** | `active` 0.20.0 |
| catálogo canônico | **118 SVGs** | `active` 0.28.0 |
| matriz de rastreabilidade | **118 SVGs / 31 perfis** | instrumento sincronizado à UXA-100-A4 |
| galeria visual | **118 SVGs** | `active` 0.22.0 |

## 4. Cobertura visual canônica

| Condição | Quantidade |
|---|---:|
| IDs com referência visual direta ou agrupada | **42** |
| responsabilidades sem SVG dedicado | **10** |
| fronteiras intencionalmente sem tela | **2** |
| **Total** | **54** |

## 5. Efeito da UXA-100-A4 no catálogo

- SVGs canônicos: **118 → 118**;
- associações: **118 → 118**;
- perfis: **31 → 31**;
- validações funcionais vigentes: **118 → 118**;
- pendências específicas de SVG: **0 → 0**;
- IDs: **53 → 54**;
- transições: **54 → 60**;
- `PER-009`: nova responsabilidade sem SVG dedicado;
- `uxa-086-collective-responsible-overview-desktop.svg`: navegação reformulada in-place;
- `uxa-015-organization-overview-desktop.svg`: rótulo `Guivos Business` corrigido para `Organização` e navegação de Planos adicionada;
- telas de Planos de Coletivo/Organização: retorno à origem administrativa explicitado;
- `TRN-406/407`: contratadas;
- `TRN-417/418` e `TRN-427/428`: integralmente validadas no limite de navegação administrativa.

## 6. Separações obrigatórias

- primeira Tela Hoje e Tela Hoje recorrente são variantes do mesmo `PER-008`;
- revisão de saída é estado do mesmo `PER-203`, não nova tela canônica;
- `BND-001` representa a transferência de autoridade, não o processo do terceiro;
- `PER-009` é responsabilidade de Conta suficiente para handoff e não uma arquitetura completa de Conta;
- `PER-106` organiza participações e não substitui a Central;
- `PER-107` é triagem de atualizações;
- `PER-108` sintetiza contexto interno e não replica canais especializados;
- comparação incremental de Planos não é tela adicional;
- processamento financeiro transitório não é tela própria;
- navegar para Planos não inicia cobrança;
- `BND-002` representa contratação/dimensionamento assistido quando aplicável e não é plano Enterprise ou Scale;
- Coletivo usa `Livre · Mobiliza · Impacta · Rede`;
- Organização usa `Conecta · Eleva · Transforma`;
- Guivos Business usa `Start · Growth · Scale · Enterprise` como Produto Especializado separado;
- `TRN-304`, `TRN-305`, `TRN-306`, `TRN-416` e `TRN-426` permanecem continuidades separadas.

## 7. Estado do catálogo

- catálogo: `active` 0.28.0;
- galeria principal: `active` 0.22.0; 118 SVGs;
- matriz por SVG: 118 associações / 31 perfis;
- jornadas da Pessoa, Coletivo e Organização: `draft`;
- protótipo e Engenharia de Produto: não iniciados.

A reconciliação documental não autoriza implementação, cobrança real, UXA-102/V5 ou próxima frente.