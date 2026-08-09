---
id: GKR-JOURNEY-SCREEN-CATALOG-001
title: Catálogo Integrado de Telas
status: active
version: 0.29.0
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

A D5-C1 adiciona três responsabilidades granulares da Pessoa sem criar SVG: `PER-010 — Meus Objetivos`, `PER-011 — Meus Próximos Passos` e `PER-012 — Minha Evolução`. Os 118 ativos visuais permanecem inalterados; os seis handoffs `TRN-008..013` permanecem contratados até materialização e validação próprias.

## 2. Inventário agregado canônico por família

| Participante ou camada | Família | SVGs | Validação funcional vigente | Continuidade integrada | Lacuna associada |
|---|---|---:|---|---|---|
| Pessoa | Home pública | 1 | validado | entrada protegida parcial | continuidade entre pacotes |
| Pessoa | início protegido | 4 | 4 validados | parcial | reconciliação ponta a ponta |
| Pessoa | expressão guiada | 8 | 8 validados | parcial | integração com inventário |
| Pessoa | compreensão inicial | 5 | 5 validados | **TRN-007 integralmente validada** | handoffs anteriores ainda parciais |
| Pessoa | Tela Hoje | 2 | 2 validados | primeira entrada validada; `TRN-008/010/012` contratadas | estados alternativos e handoffs especializados ainda sem materialização ponta a ponta |
| Pessoa | Meus Objetivos | **0** | sem SVG | `TRN-008/009` contratadas | materialização e validação próprias |
| Pessoa | Meus Próximos Passos | **0** | sem SVG | `TRN-010/011` contratadas | materialização e validação próprias |
| Pessoa | Minha Evolução | **0** | sem SVG | `TRN-012/013` contratadas | materialização e validação próprias; separar domínio/dimensão/aspecto |
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

| Registro | Quantidade | Estado vigente após D5-C1 |
|---|---:|---|
| superfícies/estados/responsabilidades/fronteiras | **57** | `active` 0.20.0 |
| transições documentais | **66** | `active` 0.21.0 |
| catálogo canônico | **118 SVGs** | `active` 0.29.0 |
| matriz de rastreabilidade | **118 SVGs / 31 perfis** | sem novos perfis porque PER-010..012 não possuem SVG |
| galeria visual | **118 SVGs** | quantidade preservada |

## 4. Cobertura visual canônica

| Condição | Quantidade |
|---|---:|
| IDs com referência visual direta ou agrupada | **42** |
| responsabilidades sem SVG dedicado | **13** |
| fronteiras intencionalmente sem tela | **2** |
| **Total** | **57** |

## 5. Efeito acumulado da D5-C1 no catálogo

- SVGs canônicos: **118 → 118**;
- associações: **118 → 118**;
- perfis: **31 → 31**;
- validações funcionais vigentes de SVG: **118 → 118**;
- pendências específicas de SVG existente: **0 → 0**;
- IDs granulares: **54 → 57**;
- transições: **60 → 66**;
- `PER-010`, `PER-011` e `PER-012`: novas responsabilidades sem SVG dedicado;
- `TRN-008..013`: contratadas;
- `PER-009`: permanece responsabilidade sem SVG dedicado;
- `TRN-406/407`: permanecem contratadas;
- `TRN-417/418` e `TRN-427/428`: permanecem integralmente validadas no limite de navegação administrativa.

A D5-C1 não altera nenhum dos 118 ativos já materializados por D5-A, D5-B ou pelas UXAs anteriores.

## 6. Separações obrigatórias

- primeira Tela Hoje e Tela Hoje recorrente são variantes do mesmo `PER-008`;
- Hoje sintetiza direção, movimento e continuidade, mas não substitui `PER-010`, `PER-011` ou `PER-012`;
- `PER-010` governa Objetivos, não score de direção ou produtividade;
- `PER-011` governa movimentos contextuais, não uma lista coercitiva de tarefas;
- `PER-012` governa trajetórias de evolução, não roda da vida, ranking ou nota humana;
- em Minha Evolução, Domínio de Evolução ≠ dimensão estrutural do Contexto Vivo ≠ aspecto descritivo da mudança;
- a D5-C1 não cria handoff direto entre `PER-010`, `PER-011` e `PER-012`;
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

- catálogo: `active` 0.29.0;
- galeria principal: 118 SVGs;
- matriz por SVG: 118 associações / 31 perfis;
- novas responsabilidades D5-C1: 3, todas sem SVG e `contratadas`;
- novos handoffs D5-C1: 6, todos `contratados`;
- jornadas da Pessoa, Coletivo e Organização: `draft`;
- protótipo e Engenharia de Produto: não iniciados.

A reconciliação documental não autoriza materialização visual de `PER-010..012`, implementação, cobrança real, UXA-102/V5, D6, D7 ou próxima frente.