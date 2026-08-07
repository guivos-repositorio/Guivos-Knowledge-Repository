---
id: GKR-JOURNEY-SCREEN-CATALOG-001
title: Catálogo Integrado de Telas
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

## 2. Inventário agregado por família

| Participante ou camada | Família | SVGs | Validação funcional vigente | Continuidade integrada | Lacuna associada |
|---|---|---:|---|---|---|
| Pessoa | Home pública | 1 | validado | entrada protegida parcial | continuidade entre pacotes |
| Pessoa | início protegido | 4 | 4 validados | parcial | reconciliação ponta a ponta |
| Pessoa | expressão guiada | 8 | 8 validados | parcial | integração com inventário |
| Pessoa | compreensão inicial | 5 | 5 validados | Tela Hoje não examinada | continuidade recorrente |
| Pessoa | Tela Hoje | 1 | validado | entrada recorrente não examinada | compreensão → Tela Hoje |
| Pessoa | oportunidades orgânicas | 7 | 7 validados | parcial | publicação/sincronização/fronteira |
| Pessoa em Coletivos | descoberta e busca | 5 | 5 validados | parcial | continuidade entre famílias |
| Pessoa em Coletivos | Perfil Público | 4 | 4 validados | parcial | handoff para solicitação |
| Pessoa em Coletivos | revisão e solicitação | 5 | 5 validados | parcial | handoff bilateral |
| Pessoa em Coletivos | Solicitação Pendente | 8 | 8 validados | TRN-105/106/107/108/109 validadas nos gates aplicáveis | outras continuidades separadas |
| Pessoa em Coletivos | Meus Coletivos | 1 | **validado na versão corrente por UXA-092/094** | TRN-108 e TRN-110 integralmente validadas | P0B separado |
| Pessoa em Coletivos | Central de Atualizações | 1 | **validado por UXA-094** | TRN-110 integralmente validada; TRN-111 ausente | PER-108; P0B/P1 separados |
| Coletivo | referência inicial | 1 | validado | parcial | continuidade com gestão |
| Coletivo | Visão Geral do Responsável | 1 | validado | TRN-112 integralmente validada | gestão especializada |
| Coletivo | gestão de solicitações | 7 | 7 validados | handoffs aplicáveis integralmente validados | operação interna posterior |
| Organização | visão geral e cadastro | 2 | 2 validados | publicação–descoberta não examinada | matriz institucional completa |
| camada comercial | Opportunity Boost | 46 | 36 validados; 10 pendentes | parcial | estados residuais UXA-055 |
| fronteira documental | destino externo | 0 | não aplicável | não examinada | efeito externo |
| **Total** |  | **107** | **97 validados; 10 pendentes** |  |  |

## 3. Instrumentos granulares vigentes

| Registro | Quantidade | Estado proposto pela UXA-094 |
|---|---:|---|
| superfícies/estados/responsabilidades/fronteiras | 40 | `active` 0.11.0 |
| transições documentais | 37 | `active` 0.11.0 |
| detalhamento da Pessoa | 19 entradas | `active` 0.6.0 |
| catálogo | 107 SVGs | `active` 0.18.0 |

## 4. Cobertura visual

| Condição | Quantidade |
|---|---:|
| IDs com referência visual direta ou agrupada | 29 |
| responsabilidades sem SVG dedicado | 10 |
| fronteira intencionalmente sem tela | 1 |
| **Total** | **40** |

## 5. Efeito da UXA-094

- cria 0 SVG e reforma 2 existentes;
- mantém 107 SVGs, 27 perfis, 40 IDs e 37 transições;
- eleva validações vigentes de 96 para **97**;
- reduz pendências de 11 para **10**, exclusivamente UXA-055;
- revalida `PER-106` no gatilho corrente;
- valida `PER-107`;
- promove `TRN-110` a integralmente validada;
- mantém `TRN-111` ausente.

## 6. Prioridade de Coletivos

```text
Visão Geral do Responsável — validada
→ gestão de solicitações — validada
→ handoffs de solicitação — integralmente validados
→ Meus Coletivos — validado
→ TRN-110 — integralmente validada
→ Central de Atualizações — validada
→ Início do Participante — reformulação/materialização pendente
```

## 7. Separações obrigatórias

- `PER-106` organiza participações/estados e não substitui a Central;
- `PER-107` é triagem de atualizações e não substitui canais especializados ou `PER-108`;
- abrir a Central não altera vínculo ou leitura;
- leitura não conclui ação substantiva;
- `PER-108` permanece fora da forma vigente;
- `COM-005` permanece ligado aos dez SVGs não validados da UXA-055;
- `BND-001` é fronteira documental, não tela.

## 8. Estado do catálogo

- catálogo: `active` 0.18.0;
- galeria: `active` 0.13.0;
- página de Coletivos: `active` 0.11.0;
- matriz por SVG: `active` 0.11.0;
- jornadas da Pessoa, Coletivo e Organização: `draft`;
- protótipo e Engenharia de Produto: não iniciados.

A validação da UXA-094 não autoriza UXA-095 automaticamente.
