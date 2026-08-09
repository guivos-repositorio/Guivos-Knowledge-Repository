---
id: GKR-JOURNEY-SCREEN-CATALOG-001
title: Catálogo Integrado de Telas
status: active
version: 0.31.0
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
  - GKR-UX-D5-C3-001
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

A D5-C1 contratou `PER-010 — Meus Objetivos`, `PER-011 — Meus Próximos Passos` e `PER-012 — Minha Evolução`. A D5-C2 criou um SVG low-fidelity para cada uma dessas responsabilidades sem criar novo ID granular e sem promover `TRN-008..013`. A D5-C3 reforma in-place e valida funcionalmente os três estados-base, mantendo as transições contratadas.

## 2. Inventário agregado canônico por família

| Participante ou camada | Família | SVGs | Validação funcional vigente | Continuidade integrada | Lacuna associada |
|---|---|---:|---|---|---|
| Pessoa | Home pública | 1 | validado | entrada protegida parcial | continuidade entre pacotes |
| Pessoa | início protegido | 4 | 4 validados | parcial | reconciliação ponta a ponta |
| Pessoa | expressão guiada | 8 | 8 validados | parcial | integração com inventário |
| Pessoa | compreensão inicial | 5 | 5 validados | **TRN-007 integralmente validada** | handoffs anteriores ainda parciais |
| Pessoa | Tela Hoje | 2 | 2 validados | primeira entrada validada; `TRN-008/010/012` contratadas | estados alternativos e handoffs especializados ainda não validados ponta a ponta |
| Pessoa | Meus Objetivos | **1** | **validado localmente pela D5-C3** | `TRN-008/009` contratadas | validação integrada do handoff |
| Pessoa | Meus Próximos Passos | **1** | **validado localmente pela D5-C3** | `TRN-010/011` contratadas | validação integrada do handoff |
| Pessoa | Minha Evolução | **1** | **validado localmente pela D5-C3** | `TRN-012/013` contratadas | estados sensíveis adicionais quando aplicáveis; validação integrada do handoff |
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
| **Total canônico** |  | **121** | **121 validados; 0 pendentes** |  |  |

## 3. Instrumentos granulares vigentes

| Registro | Quantidade | Estado vigente após D5-C3 |
|---|---:|---|
| superfícies/estados/responsabilidades/fronteiras | **57** | D5-C3 não cria novo ID |
| transições documentais | **66** | D5-C3 não promove `TRN-008..013` |
| catálogo canônico | **121 SVGs** | `active` 0.31.0 |
| matriz de rastreabilidade | **121 SVGs / 34 perfis** | R32–R34 validados localmente |
| galeria visual | **121 SVGs** | 121 validados / 0 pendentes |

## 4. Cobertura visual canônica

| Condição | Quantidade |
|---|---:|
| IDs com referência visual direta ou agrupada | **45** |
| responsabilidades sem SVG dedicado | **10** |
| fronteiras intencionalmente sem tela | **2** |
| **Total** | **57** |

## 5. Efeito acumulado D5-C2 → D5-C3 no catálogo

D5-C2 alterou o inventário físico:

- SVGs canônicos: **118 → 121**;
- associações: **118 → 121**;
- perfis: **31 → 34**;
- IDs com referência visual: **42 → 45**;
- responsabilidades sem SVG dedicado: **13 → 10**.

D5-C3 não altera essas contagens. Ela altera somente a maturidade visual:

- validações funcionais vigentes de SVG: **118 → 121**;
- pendências específicas de SVG: **3 → 0**;
- `PER-010`, `PER-011` e `PER-012`: passam de materializados/pendentes para **validados localmente**;
- `TRN-008..013`: permanecem contratadas;
- `PER-009`: permanece responsabilidade sem SVG dedicado;
- `TRN-406/407`: permanecem contratadas;
- `TRN-417/418` e `TRN-427/428`: permanecem integralmente validadas no limite de navegação administrativa.

## 6. Separações obrigatórias

- primeira Tela Hoje e Tela Hoje recorrente são variantes do mesmo `PER-008`;
- Hoje sintetiza direção, movimento e continuidade, mas não substitui `PER-010`, `PER-011` ou `PER-012`;
- `PER-010` governa Objetivos, não score de direção ou produtividade;
- `PER-011` governa movimentos contextuais, não uma lista coercitiva de tarefas;
- `PER-012` governa trajetórias de evolução, não roda da vida, ranking ou nota humana;
- em Minha Evolução, Domínio de Evolução ≠ dimensão estrutural do Contexto Vivo ≠ aspecto descritivo da mudança;
- validação local de `PER-010..012` ≠ validação integrada de `TRN-008..013`;
- presença de retorno visual para Hoje ≠ validação dos handoffs;
- D5-C1/C2/C3 não criam handoff direto entre `PER-010`, `PER-011` e `PER-012`;
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

- catálogo: `active` 0.31.0;
- galeria principal: **121 SVGs / 121 validados / 0 pendentes**;
- matriz por SVG: **121 associações / 34 perfis**;
- `PER-010..012`: validados localmente pela D5-C3;
- `TRN-008..013`: permanecem `contratadas`;
- jornadas da Pessoa, Coletivo e Organização: `draft`;
- protótipo e Engenharia de Produto: não iniciados.

A D5-C3 não autoriza implementação, cobrança real, UXA-102/V5, D6, D7 ou próxima frente.