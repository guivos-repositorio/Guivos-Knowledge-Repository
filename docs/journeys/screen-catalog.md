---
id: GKR-JOURNEY-SCREEN-CATALOG-001
title: Catálogo Integrado de Telas
status: active
version: 0.19.0
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
| Pessoa em Coletivos | Solicitação Pendente | 8 | 8 validados | TRN-105/106/107/108/109 nos gates aplicáveis | outras continuidades separadas |
| Pessoa em Coletivos | Meus Coletivos | 1 | validado | TRN-108 e TRN-110 integralmente validadas | P0B separado |
| Pessoa em Coletivos | Central de Atualizações | 1 | **SVG corrente reformulado; revalidação pendente** | TRN-110 integral; TRN-111 parcial | PER-108/UXA-096; P0B/P1 separados |
| Pessoa em Coletivos | **Início do Participante** | **1** | **pendente** | **TRN-111 parcial** | validação funcional/integrada |
| Coletivo | referência inicial | 1 | validado | parcial | continuidade com gestão |
| Coletivo | Visão Geral do Responsável | 1 | validado | TRN-112 integralmente validada | gestão especializada |
| Coletivo | gestão de solicitações | 7 | 7 validados | handoffs aplicáveis integralmente validados | operação interna posterior |
| Organização | visão geral e cadastro | 2 | 2 validados | publicação–descoberta não examinada | matriz institucional completa |
| camada comercial | Opportunity Boost | 46 | 36 validados; 10 pendentes | parcial | estados residuais UXA-055 |
| fronteira documental | destino externo | 0 | não aplicável | não examinada | efeito externo |
| **Total** |  | **108** | **96 validados; 12 pendentes** |  |  |

## 3. Instrumentos granulares vigentes

| Registro | Quantidade | Estado proposto pela UXA-095 |
|---|---:|---|
| superfícies/estados/responsabilidades/fronteiras | 40 | `active` 0.12.0 |
| transições documentais | 37 | `active` 0.12.0 |
| detalhamento da Pessoa | 19 entradas | `active` 0.7.0 |
| catálogo | 108 SVGs | `active` 0.19.0 |

## 4. Cobertura visual

| Condição | Quantidade |
|---|---:|
| IDs com referência visual direta ou agrupada | **30** |
| responsabilidades sem SVG dedicado | **9** |
| fronteira intencionalmente sem tela | 1 |
| **Total** | **40** |

## 5. Efeito da UXA-095

- cria 1 SVG e reforma 1 existente;
- passa para 108 SVGs e 28 perfis;
- mantém 40 IDs e 37 transições;
- registra 96 validações vigentes e 12 pendências;
- materializa `PER-108`;
- torna `TRN-111` parcial;
- não valida o SVG corrente reformulado de `PER-107` nem o novo `PER-108`.

## 6. Prioridade de Coletivos

```text
Visão Geral do Responsável — validada
→ gestão de solicitações — validada
→ handoffs de solicitação — integralmente validados
→ Meus Coletivos — validado
→ TRN-110 — integralmente validada
→ Central de Atualizações — contrato validado; SVG corrente pendente
→ TRN-111 — parcial
→ Início do Participante — materializado; validação pendente
```

## 7. Separações obrigatórias

- `PER-106` organiza participações e não substitui a Central;
- `PER-107` é triagem de atualizações;
- `PER-108` sintetiza o contexto interno e não replica canais especializados;
- abrir `PER-108` não altera vínculo, leitura, papel, presença ou autoridade;
- `COM-005` permanece ligado aos dez SVGs não validados da UXA-055;
- `BND-001` é fronteira documental, não tela.

## 8. Estado do catálogo

- catálogo: `active` 0.19.0;
- galeria: `active` 0.14.0;
- página de Coletivos: `active` 0.12.0;
- matriz por SVG: `active` 0.12.0;
- jornadas da Pessoa, Coletivo e Organização: `draft`;
- protótipo e Engenharia de Produto: não iniciados.

A materialização da UXA-095 não autoriza UXA-096 automaticamente.
