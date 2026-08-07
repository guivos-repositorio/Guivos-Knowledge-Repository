---
id: GKR-JOURNEY-SCREEN-CATALOG-001
title: Catálogo Integrado de Telas
status: active
version: 0.23.0
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
≠ superfície granular adicional
≠ validação funcional automática
≠ transição validada automaticamente
≠ jornada integrada validada
```

## 2. Inventário agregado canônico por família

| Participante ou camada | Família | SVGs | Validação funcional vigente | Continuidade integrada | Lacuna associada |
|---|---|---:|---|---|---|
| Pessoa | Home pública | 1 | validado | entrada protegida parcial | continuidade entre pacotes |
| Pessoa | início protegido | 4 | 4 validados | parcial | reconciliação ponta a ponta |
| Pessoa | expressão guiada | 8 | 8 validados | parcial | integração com inventário |
| Pessoa | compreensão inicial | 5 | 5 validados | **TRN-007 integralmente validada** | handoffs anteriores ainda parciais |
| Pessoa | Tela Hoje | **2** | **2 validados** | **primeira entrada validada; recorrência separada** | estados alternativos de Hoje |
| Pessoa | oportunidades orgânicas | 7 | 7 validados | publicação/descoberta e Mapa/Lista/Detalhe integrados | efeito externo separado |
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
| Organização | visão geral e cadastro | 2 | 2 validados | publicação–descoberta integralmente validada em TRN-203 | matriz institucional completa |
| camada comercial | Opportunity Boost | 46 | **46 validados** | parcial | TRN-304/305/306 e integrações específicas |
| fronteira documental | destino externo | 0 | não aplicável | não examinada | efeito externo |
| **Total canônico** |  | **109** | **109 validados; 0 pendentes** |  |  |

## 3. Conjunto candidato UXA-100 — Planos, comparação e cobrança

A UXA-100 adiciona um conjunto visual candidato, ainda fora da contagem canônica:

| Participante | Tela dedicada de Planos | Placa de fluxo | Comparação incremental | Total candidato |
|---|---:|---:|---:|---:|
| Pessoa | 1 | 1 | 1 | 3 |
| Coletivo | 1 | 1 | 1 | 3 |
| Organização | 1 | 1 | 1 | 3 |
| **Total candidato UXA-100** | **3** | **3** | **3** | **9** |

Referência de inspeção: [Planos, Comparação e Cobrança — Galeria Candidata](screen-gallery-plans-billing.md).

As telas dedicadas são:

- `uxa-100-person-plans-screen-mobile.svg`;
- `uxa-100-collective-plans-screen-desktop.svg`;
- `uxa-100-organization-plans-screen-desktop.svg`.

Materialização candidata não cria IDs de superfície/transição, não eleva a contagem canônica e não representa checkout implementado.

## 4. Instrumentos granulares vigentes

| Registro | Quantidade | Estado vigente/candidato |
|---|---:|---|
| superfícies/estados/responsabilidades/fronteiras | 40 | `active` 0.15.0; sem IDs de Planos |
| transições documentais | 37 | `active` 0.16.0; sem transições de Planos |
| detalhamento da Pessoa | 19 entradas | `active` 0.9.0 |
| catálogo canônico | 109 SVGs | `active` 0.23.0 |
| conjunto candidato UXA-100 | 9 SVGs | `draft`; fora da contagem canônica |

## 5. Cobertura visual canônica

| Condição | Quantidade |
|---|---:|
| IDs com referência visual direta ou agrupada | **30** |
| responsabilidades sem SVG dedicado | **9** |
| fronteira intencionalmente sem tela | 1 |
| **Total** | **40** |

## 6. Efeito da UXA-100 no catálogo

- preserva **109 SVGs canônicos**, 109 associações, 28 perfis, 40 IDs e 37 transições;
- adiciona **9 SVGs candidatos** de Planos/cobrança fora da contagem canônica;
- desses 9, três são telas dedicadas de Planos, três são placas de fluxo e três comparações incrementais;
- inclui a etapa Planos nas jornadas draft de Pessoa, Coletivo e Organização;
- não promove nenhuma superfície ou transição;
- não altera validações funcionais vigentes do conjunto canônico.

## 7. Separações obrigatórias

- primeira Tela Hoje e Tela Hoje recorrente são variantes do mesmo `PER-008`, não novos IDs;
- `PER-106` organiza participações e não substitui a Central;
- `PER-107` é triagem de atualizações;
- `PER-108` sintetiza o contexto interno e não replica canais especializados;
- Planos materializado na UXA-100 ainda não possui ID canônico;
- plano pago não compra relevância, legitimidade, confiança, impacto ou evolução;
- `COM-005` está validado pela UXA-099, mas sua validação não promove automaticamente `TRN-305`;
- `BND-001` é fronteira documental, não tela;
- `TRN-205`, `TRN-304`, `TRN-305` e `TRN-306` permanecem continuidades separadas.

## 8. Estado do catálogo

- catálogo: `active` 0.23.0;
- galeria principal canônica: 109 SVGs;
- galeria candidata de Planos: `draft` 0.1.0; 9 SVGs candidatos;
- matriz por SVG canônica: `active` 0.15.0;
- jornadas da Pessoa, Coletivo e Organização: `draft`, agora com Planos candidato;
- protótipo e Engenharia de Produto: não iniciados.

O próximo ato governado da UXA-100 é validar funcionalmente os nove SVGs candidatos antes de qualquer promoção ao registro de superfícies, transições ou contagem canônica.