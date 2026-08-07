---
id: GKR-JOURNEY-SCREEN-CATALOG-001
title: Catálogo Integrado de Telas
status: active
version: 0.15.0
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
≠ validação funcional
≠ transição validada
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
| Pessoa em Coletivos | Solicitação Pendente | 8 | 7 validados na versão corrente; aprovação pendente de revalidação | handoffs elegíveis validados; TRN-108 parcial | continuidade pós-aprovação |
| Pessoa em Coletivos | Meus Coletivos | 1 | pendente | TRN-108 e TRN-110 parciais | validação funcional e PER-107 ausente |
| Coletivo | referência inicial | 1 | validado | parcial | continuidade com gestão |
| Coletivo | Visão Geral do Responsável | 1 | validado por UXA-087 | TRN-112 integralmente validada | gestão especializada |
| Coletivo | gestão de solicitações | 7 | 7 validados por UXA-089 | TRN-105/106/107/109/112 integralmente validadas; TRN-108 parcial | continuidade de aprovação |
| Organização | visão geral e cadastro | 2 | 2 validados | publicação–descoberta não examinada | matriz institucional completa |
| camada comercial | Opportunity Boost | 46 | 36 validados; 10 pendentes | parcial | estados residuais da UXA-055 |
| fronteira documental | destino externo | 0 | não aplicável | não examinada | efeito externo |
| **Total** |  | **106** | **94 validados; 12 pendentes** |  |  |

## 3. Instrumentos granulares vigentes

| Registro | Quantidade | Estado proposto pela UXA-091 |
|---|---:|---|
| superfícies, estados, responsabilidades ou fronteiras | 40 | `active` 0.8.0 |
| transições documentais | 37 | `active` 0.8.0 |
| referências de endpoint | 74 | resolvidas |
| endpoints em texto livre | 0 | aprovado |
| detalhamento da Pessoa | 19 entradas | `active` 0.3.0 |
| detalhamento do Coletivo | 8 entradas | `active` 0.6.0 |
| demais detalhamentos obrigatórios | 2 arquivos | `active` 0.2.0 |

## 4. Cobertura visual

| Condição | Quantidade |
|---|---:|
| IDs com referência visual direta ou agrupada | 28 |
| responsabilidades sem SVG dedicado | 11 |
| fronteira intencionalmente sem tela | 1 |
| **Total** | **40** |

## 5. Efeito da UXA-091

A UXA-091:

- adiciona 1 SVG móvel de `GKR-SURF-PER-106`;
- reforma 1 SVG existente do resultado aprovado de `GKR-SURF-PER-105`;
- mantém 40 IDs e 37 transições;
- aumenta o inventário visual de 105 para 106 SVGs;
- aumenta perfis de rastreabilidade de 25 para 26;
- mantém 94 SVGs com validação vigente;
- registra 12 pendências específicas;
- aumenta IDs com referência visual de 27 para 28;
- reduz responsabilidades sem SVG dedicado de 12 para 11;
- mantém `GKR-TRN-108` parcial;
- altera `GKR-TRN-110` de ausente para parcial.

## 6. Prioridade de Coletivos

```text
Visão Geral do Responsável — validada
→ gestão de solicitações — validada
→ cinco handoffs elegíveis — integralmente validados
→ estado aprovado PER-105 — reformulado; revalidação pendente
→ Meus Coletivos — materializado; validação pendente
→ Central de Atualizações — ausente
→ Início do Participante — reformulação pendente
```

## 7. Separações obrigatórias

- `GKR-SURF-COL-002` continua sendo orientação e entrada de gestão;
- `GKR-SURF-COL-003` é exclusivamente a operação de solicitações;
- `GKR-SURF-COL-004` permanece responsável por participantes e vínculos no lado do responsável;
- `GKR-SURF-PER-105` continua representando a solicitação e seus resultados;
- `GKR-SURF-PER-106` é a central de vínculos da Pessoa e não substitui `PER-107` ou `PER-108`;
- `GKR-SURF-COM-005` permanece ligado aos dez SVGs não validados da UXA-055;
- `GKR-SURF-BND-001` é fronteira documental, não tela.

## 8. Estado do catálogo

- catálogo: `active` 0.15.0;
- galeria: `active` 0.10.0;
- página de Coletivos: `active` 0.8.0;
- demais páginas visuais: `active` 0.3.0;
- matriz por SVG: `active` 0.8.0;
- jornadas da Pessoa, Coletivo e Organização: `draft`;
- protótipo e Engenharia de Produto: não iniciados.

A materialização da UXA-091 não autoriza UXA-092 automaticamente.
