---
id: GKR-JOURNEY-SCREEN-CATALOG-001
title: Catálogo Integrado de Telas
status: active
version: 0.17.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - UXA-005
  - UXA-070
  - UXA-074
  - UXA-075
  - UXA-076
  - UXA-077
  - UXA-078
  - UXA-079
  - UXA-080
  - UXA-081
  - UXA-082
  - UXA-083
  - UXA-084
  - UXA-085
  - UXA-086
  - UXA-087
  - UXA-088
  - UXA-089
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
  - GKR-JOURNEY-SCREEN-GALLERY-001
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

Uma superfície pode possuir materialização própria sem validação; uma versão visual reformulada também exige novo exame antes de ser tratada como validada.

## 2. Inventário agregado por família

| Participante ou camada | Família | SVGs | Validação funcional vigente | Continuidade integrada | Lacuna associada |
|---|---|---:|---|---|---|
| Pessoa | Home pública | 1 | validado | entrada protegida parcial | continuidade entre pacotes |
| Pessoa | início protegido | 4 | 4 validados | parcial | reconciliação ponta a ponta |
| Pessoa | expressão guiada | 8 | 8 validados | parcial | integração com inventário |
| Pessoa | compreensão inicial | 5 | 5 validados | Tela Hoje não examinada | continuidade recorrente |
| Pessoa | Tela Hoje | 1 | validado | entrada recorrente não examinada | compreensão → Tela Hoje |
| Pessoa | oportunidades orgânicas | 7 | 7 validados | publicação e efeito externo parciais | publicação, sincronização e fronteira |
| Pessoa em Coletivos | descoberta e busca | 5 | 5 validados | parcial | continuidade entre famílias |
| Pessoa em Coletivos | Perfil Público | 4 | 4 validados | parcial | handoff para solicitação |
| Pessoa em Coletivos | revisão e solicitação | 5 | 5 validados | parcial | handoff bilateral |
| Pessoa em Coletivos | Solicitação Pendente | 8 | 8 validados na versão corrente | handoffs 105/106/107/109 e TRN-108 validados | continuidades posteriores distintas |
| Pessoa em Coletivos | Meus Coletivos | 1 | validado por UXA-092 | TRN-108 validada; TRN-110 parcial | P0B adicional separado |
| Pessoa em Coletivos | Central de Atualizações | 1 | pendente após UXA-093 | TRN-110 parcial; TRN-111 ausente | validação funcional; PER-108 ausente; P0B separado |
| Coletivo | referência inicial | 1 | validado | parcial | continuidade com gestão |
| Coletivo | Visão Geral do Responsável | 1 | validado por UXA-087 | TRN-112 integralmente validada | gestão especializada |
| Coletivo | gestão de solicitações | 7 | 7 validados por UXA-089 | TRN-105/106/107/108/109/112 integralmente validadas no escopo aplicável | continuidade posterior em PER-107 |
| Organização | visão geral e cadastro | 2 | 2 validados | publicação–descoberta não examinada | matriz institucional completa |
| camada comercial | Opportunity Boost | 46 | 36 validados; 10 pendentes | parcial | estados residuais da UXA-055 |
| fronteira documental | destino externo | 0 | não aplicável | não examinada | efeito externo |
| **Total** |  | **107** | **96 validados; 11 pendentes** |  |  |

## 3. Instrumentos granulares vigentes

| Registro | Quantidade | Estado proposto pela UXA-093 |
|---|---:|---|
| superfícies, estados, responsabilidades ou fronteiras | 40 | `active` 0.10.0 |
| transições documentais | 37 | `active` 0.10.0 |
| referências de endpoint | 74 | resolvidas |
| endpoints em texto livre | 0 | aprovado |
| detalhamento da Pessoa | 19 entradas | `active` 0.5.0 |
| detalhamento do Coletivo | 8 entradas | `active` 0.6.0 |
| demais detalhamentos obrigatórios | 2 arquivos | `active` 0.2.0 |

## 4. Cobertura visual

| Condição | Quantidade |
|---|---:|
| IDs com referência visual direta ou agrupada | 29 |
| responsabilidades sem SVG dedicado | 10 |
| fronteira intencionalmente sem tela | 1 |
| **Total** | **40** |

## 5. Efeito da UXA-093

A UXA-093:

- cria 1 SVG móvel para `GKR-SURF-PER-107`;
- não altera SVG previamente validado;
- mantém 40 IDs e 37 transições;
- eleva SVGs de 106 para 107 e perfis de 26 para 27;
- mantém validações funcionais vigentes em 96;
- eleva pendências específicas de 10 para 11: dez UXA-055 + PER-107;
- eleva IDs com referência visual de 28 para 29 e reduz responsabilidades sem SVG de 11 para 10;
- materializa `PER-107` sem validação;
- mantém `GKR-TRN-110` parcial e `GKR-TRN-111` ausente.

## 6. Prioridade de Coletivos

```text
Visão Geral do Responsável — validada
→ gestão de solicitações — validada
→ seis handoffs do fluxo de solicitação — integralmente validados
→ estado aprovado PER-105 — validado
→ Meus Coletivos — validado
→ Central de Atualizações — materializada; validação pendente
→ Início do Participante — reformulação pendente
```

## 7. Separações obrigatórias

- `GKR-SURF-COL-002` continua sendo orientação e entrada de gestão;
- `GKR-SURF-COL-003` é exclusivamente a operação de solicitações;
- `GKR-SURF-COL-004` permanece responsável por participantes e vínculos no lado do responsável;
- `GKR-SURF-PER-105` continua representando a solicitação e seus resultados;
- `GKR-SURF-PER-106` organiza participações e estados relacionados da Pessoa e não substitui `PER-107` ou `PER-108`;
- `GKR-SURF-PER-107` é central de triagem de atualizações e não substitui canais especializados ou `PER-108`;
- `GKR-SURF-COM-005` permanece ligado aos dez SVGs não validados da UXA-055;
- `GKR-SURF-BND-001` é fronteira documental, não tela.

## 8. Estado do catálogo

- catálogo: `active` 0.17.0;
- galeria: `active` 0.12.0;
- página de Coletivos: `active` 0.10.0;
- demais páginas visuais: `active` 0.3.0;
- matriz por SVG: `active` 0.10.0;
- jornadas da Pessoa, Coletivo e Organização: `draft`;
- protótipo e Engenharia de Produto: não iniciados.

A materialização da UXA-093 não autoriza UXA-094 automaticamente.