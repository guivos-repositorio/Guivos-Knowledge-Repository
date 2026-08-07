---
id: GKR-JOURNEY-SCREEN-CATALOG-001
title: Catálogo Integrado de Telas
status: active
version: 0.21.0
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
| Pessoa | compreensão inicial | 5 | 5 validados | **TRN-007 integralmente validada** | handoffs anteriores ainda parciais |
| Pessoa | Tela Hoje | **2** | **2 validados** | **primeira entrada validada; recorrência separada** | estados alternativos de Hoje |
| Pessoa | oportunidades orgânicas | 7 | 7 validados | parcial | publicação/sincronização/fronteira |
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
| Organização | visão geral e cadastro | 2 | 2 validados | publicação–descoberta não examinada | matriz institucional completa |
| camada comercial | Opportunity Boost | 46 | 36 validados; 10 pendentes | parcial | estados residuais UXA-055 |
| fronteira documental | destino externo | 0 | não aplicável | não examinada | efeito externo |
| **Total** |  | **109** | **99 validados; 10 pendentes** |  |  |

## 3. Instrumentos granulares vigentes

| Registro | Quantidade | Estado proposto pela UXA-097 |
|---|---:|---|
| superfícies/estados/responsabilidades/fronteiras | 40 | `active` 0.14.0 |
| transições documentais | 37 | `active` 0.14.0 |
| detalhamento da Pessoa | 19 entradas | `active` 0.9.0 |
| catálogo | 109 SVGs | `active` 0.21.0 |

## 4. Cobertura visual

| Condição | Quantidade |
|---|---:|
| IDs com referência visual direta ou agrupada | **30** |
| responsabilidades sem SVG dedicado | **9** |
| fronteira intencionalmente sem tela | 1 |
| **Total** | **40** |

## 5. Efeito da UXA-097

- cria 1 SVG e reforma 1 existente;
- preserva 28 perfis, 40 IDs e 37 transições;
- registra **99 validações vigentes e 10 pendências**, exclusivamente UXA-055;
- revalida a variante de decisão de `PER-007`;
- valida a primeira variante de `PER-008`;
- promove `TRN-007` a integralmente validada;
- não altera a Tela Hoje recorrente.

## 6. Continuidade pessoal examinada

```text
PER-007 — compreensão inicial revisável
→ escolhas explícitas
→ TRN-007 — integralmente validada
→ PER-008 — primeira Tela Hoje validada
→ experiência recorrente separada
```

A primeira entrada não presume avanço, urgência ou histórico. Sem personalização vigente, indicações pessoais são omitidas.

## 7. Prioridade de Coletivos preservada

```text
Visão Geral do Responsável — validada
→ gestão de solicitações — validada
→ handoffs de solicitação — integralmente validados
→ Meus Coletivos — validado
→ TRN-110 — integralmente validada
→ Central de Atualizações — validada
→ TRN-111 — integralmente validada
→ Início do Participante — validado
```

## 8. Separações obrigatórias

- primeira Tela Hoje e Tela Hoje recorrente são variantes do mesmo `PER-008`, não novos IDs;
- `PER-106` organiza participações e não substitui a Central;
- `PER-107` é triagem de atualizações;
- `PER-108` sintetiza o contexto interno e não replica canais especializados;
- evento histórico não concede acesso a `PER-108`;
- `COM-005` permanece ligado aos dez SVGs não validados da UXA-055;
- `BND-001` é fronteira documental, não tela.

## 9. Estado do catálogo

- catálogo: `active` 0.21.0;
- galeria: `active` 0.16.0;
- página da Pessoa: `active` 0.4.0;
- página de Coletivos: `active` 0.13.0;
- matriz por SVG: `active` 0.14.0;
- jornadas da Pessoa, Coletivo e Organização: `draft`;
- protótipo e Engenharia de Produto: não iniciados.

Com `V1` fechado, a próxima prioridade vigente é `V2 — publicação → descoberta/mapa/lista/detalhe`. **UXA-098 não foi iniciada.**