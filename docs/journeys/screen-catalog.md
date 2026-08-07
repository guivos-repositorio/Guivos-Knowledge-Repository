---
id: GKR-JOURNEY-SCREEN-CATALOG-001
title: Catálogo Integrado de Telas
status: active
version: 0.12.0
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
≠ transição validada
≠ jornada integrada validada
```

Uma superfície pode possuir validação funcional própria sem que sua continuidade para o próximo destino esteja validada. A inspeção visual ocorre na [Galeria Visual Integrada](screen-gallery.md) e a associação individual está na [Matriz de Rastreabilidade por SVG](screen-gallery-traceability-matrix.md).

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
| Pessoa em Coletivos | revisão e solicitação | 5 | 5 validados | parcial | destino operacional do responsável |
| Pessoa em Coletivos | Solicitação Pendente | 8 | 8 validados na perspectiva da Pessoa | ausente após decisão | gestão do responsável e Meus Coletivos |
| Coletivo | referência inicial | 1 | validado | parcial | continuidade com gestão |
| Coletivo | Visão Geral do Responsável | 1 | validado por UXA-087 | GKR-TRN-112 parcial | gestão completa de solicitações |
| Organização | visão geral e cadastro | 2 | 2 validados | publicação–descoberta não examinada | matriz institucional completa |
| camada comercial | Opportunity Boost | 46 | 36 validados; 10 pendentes | parcial | estados residuais da UXA-055 |
| fronteira documental | destino externo | 0 | não aplicável | não examinada | efeito externo |
| **Total** |  | **98** | **88 validados; 10 pendentes** |  |  |

## 3. Instrumentos granulares vigentes

| Registro | Quantidade | Estado |
|---|---:|---|
| superfícies, estados, responsabilidades ou fronteiras | 40 | `active` 0.5.0 |
| transições documentais | 37 | `active` 0.4.0 |
| referências de endpoint | 74 | resolvidas |
| endpoints em texto livre | 0 | aprovado |
| detalhamento do Coletivo | 8 entradas | `active` 0.4.0 |
| demais detalhamentos obrigatórios | 3 arquivos | `active` 0.2.0 |

O status `active` aprova os instrumentos, não os objetos registrados.

## 4. Cobertura visual

| Condição | Quantidade |
|---|---:|
| IDs com referência visual direta ou agrupada | 26 |
| responsabilidades sem SVG dedicado | 13 |
| fronteira intencionalmente sem tela | 1 |
| **Total** | **40** |

## 5. Efeito da UXA-087

A UXA-087 reformula o arquivo `uxa-086-collective-responsible-overview-desktop.svg` sem criar um novo ativo e valida funcionalmente `GKR-SURF-COL-002`.

O incremento:

- mantém o inventário visual em 98 SVGs;
- mantém 24 perfis de rastreabilidade;
- aumenta validações funcionais de 87 para 88;
- reduz pendentes de 11 para 10;
- mantém 26 IDs com referência visual;
- mantém 13 responsabilidades sem SVG dedicado;
- não materializa `GKR-SURF-COL-003`;
- não valida `GKR-TRN-112` ponta a ponta.

## 6. Prioridade de Coletivos

```text
Visão Geral do Responsável — validada
→ gestão completa de solicitações — ausente
→ Meus Coletivos — ausente
→ Central de Atualizações — ausente
→ Início do Participante — reformulação pendente
```

## 7. Separações obrigatórias

- `GKR-SURF-PER-102` representa exclusivamente busca de Coletivos;
- `GKR-SURF-PER-201`, `202` e `203` representam mapa, lista e detalhe de oportunidades;
- `GKR-SURF-ORG-003` representa o estado institucional de oportunidade;
- `GKR-SURF-COL-002` é a visão geral validada do responsável e não substitui a gestão completa de solicitações;
- `GKR-SURF-COM-005` permanece ligado aos dez SVGs não validados da UXA-055;
- `GKR-SURF-BND-001` é fronteira documental, não tela.

## 8. Estado vigente

- catálogo: `active` 0.12.0;
- galeria: `active` 0.7.0;
- página de Coletivos: `active` 0.5.0;
- demais páginas visuais: `active` 0.3.0;
- matriz por SVG: `active` 0.5.0;
- jornadas da Pessoa, Coletivo e Organização: `draft`;
- protótipo e Engenharia de Produto: não iniciados.

A validação da UXA-087 não autoriza UXA-088 automaticamente.
