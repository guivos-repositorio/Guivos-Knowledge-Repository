---
id: GKR-JOURNEY-SCREEN-CATALOG-001
title: Catálogo Integrado de Telas
status: active
version: 0.13.0
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

Uma superfície pode possuir materialização própria sem que a continuidade para o próximo destino esteja validada.

## 2. Inventário agregado por família

| Participante ou camada | Família | SVGs | Validação funcional | Continuidade integrada | Lacuna associada |
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
| Pessoa em Coletivos | Solicitação Pendente | 8 | 8 validados na perspectiva da Pessoa | parcial | continuidade após decisão |
| Coletivo | referência inicial | 1 | validado | parcial | continuidade com gestão |
| Coletivo | Visão Geral do Responsável | 1 | validado por UXA-087 | TRN-112 não validada como conjunto | gestão especializada |
| Coletivo | gestão de solicitações | 7 | pendentes de validação | TRN-105 a 109 e 112 parciais | validação bilateral e Meus Coletivos |
| Organização | visão geral e cadastro | 2 | 2 validados | publicação–descoberta não examinada | matriz institucional completa |
| camada comercial | Opportunity Boost | 46 | 36 validados; 10 pendentes | parcial | estados residuais da UXA-055 |
| fronteira documental | destino externo | 0 | não aplicável | não examinada | efeito externo |
| **Total** |  | **105** | **88 validados; 17 pendentes** |  |  |

## 3. Instrumentos granulares vigentes

| Registro | Quantidade | Estado proposto pela UXA-088 |
|---|---:|---|
| superfícies, estados, responsabilidades ou fronteiras | 40 | `active` 0.6.0 |
| transições documentais | 37 | `active` 0.5.0 |
| referências de endpoint | 74 | resolvidas |
| endpoints em texto livre | 0 | aprovado |
| detalhamento do Coletivo | 8 entradas | `active` 0.5.0 |
| demais detalhamentos obrigatórios | 3 arquivos | `active` 0.2.0 |

## 4. Cobertura visual

| Condição | Quantidade |
|---|---:|
| IDs com referência visual direta ou agrupada | 27 |
| responsabilidades sem SVG dedicado | 12 |
| fronteira intencionalmente sem tela | 1 |
| **Total** | **40** |

## 5. Efeito da UXA-088

A UXA-088 adiciona sete SVGs de `GKR-SURF-COL-003`:

- fila operacional;
- detalhe comum;
- análise protegida;
- pedido adicional;
- confirmação de aprovação;
- confirmação de recusa;
- autoridade insuficiente.

O incremento:

- aumenta o inventário visual de 98 para 105 SVGs;
- aumenta perfis de rastreabilidade de 24 para 25;
- mantém validações funcionais em 88;
- aumenta pendentes de 10 para 17;
- aumenta IDs com referência visual de 26 para 27;
- reduz responsabilidades sem SVG dedicado de 13 para 12;
- não cria ID granular ou transição nova;
- não valida `GKR-TRN-105` a `109` nem `GKR-TRN-112` ponta a ponta.

## 6. Prioridade de Coletivos

```text
Visão Geral do Responsável — validada
→ gestão de solicitações — materializada; validação pendente
→ Meus Coletivos — ausente
→ Central de Atualizações — ausente
→ Início do Participante — reformulação pendente
```

## 7. Separações obrigatórias

- `GKR-SURF-COL-002` continua sendo orientação e entrada de gestão;
- `GKR-SURF-COL-003` é exclusivamente a operação de solicitações, não gestão de participantes;
- `GKR-SURF-COL-004` permanece responsável por participantes e vínculos;
- `GKR-SURF-PER-105` continua representando o acompanhamento da Pessoa;
- `GKR-SURF-PER-106` permanece ausente;
- `GKR-SURF-COM-005` permanece ligado aos dez SVGs não validados da UXA-055;
- `GKR-SURF-BND-001` é fronteira documental, não tela.

## 8. Estado do catálogo

- catálogo: `active` 0.13.0;
- galeria: `active` 0.8.0;
- página de Coletivos: `active` 0.6.0;
- demais páginas visuais: `active` 0.3.0;
- matriz por SVG: `active` 0.6.0;
- jornadas da Pessoa, Coletivo e Organização: `draft`;
- protótipo e Engenharia de Produto: não iniciados.

A materialização da UXA-088 não autoriza UXA-089 automaticamente.
