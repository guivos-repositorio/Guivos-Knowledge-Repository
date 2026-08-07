---
id: GKR-JOURNEY-SCREEN-CATALOG-001
title: Catálogo Integrado de Telas
status: active
version: 0.10.0
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

A inspeção visual ocorre na [Galeria Visual Integrada](screen-gallery.md). A associação individual dos arquivos está na [Matriz de Rastreabilidade por SVG](screen-gallery-traceability-matrix.md).

## 2. Inventário agregado por família

| Participante ou camada | Família | SVGs | Validação local | Continuidade integrada | Lacuna associada |
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
| Coletivo | referência inicial | 1 | validado | não examinada | Visão Geral do Responsável |
| Organização | visão geral e cadastro | 2 | 2 validados | publicação–descoberta não examinada | matriz institucional completa |
| camada comercial | Opportunity Boost | 46 | 36 validados; 10 pendentes | parcial | estados residuais da UXA-055 |
| fronteira documental | destino externo | 0 | não aplicável | não examinada | efeito externo |
| **Total** |  | **97** | **87 validados; 10 pendentes** |  |  |

## 3. Instrumentos granulares vigentes

| Registro | Quantidade | Estado |
|---|---:|---|
| superfícies, estados, responsabilidades ou fronteiras | 40 | `active` 0.3.0 |
| transições documentais | 37 | `active` 0.3.0 |
| referências de endpoint | 74 | resolvidas |
| endpoints em texto livre | 0 | aprovado |
| detalhamentos obrigatórios | 4 | `active` 0.2.0 |

O status `active` aprova os instrumentos, não os objetos registrados.

## 4. Cobertura visual

| Condição | Quantidade |
|---|---:|
| IDs com referência visual direta ou agrupada | 25 |
| responsabilidades sem SVG dedicado | 14 |
| fronteira intencionalmente sem tela | 1 |
| **Total** | **40** |

## 5. Resultado da UXA-084 e promoção da UXA-085

A galeria reformulada foi **aprovada com ressalvas no escopo documental de inspeção** pela UXA-084 e promovida como instrumento documental pela UXA-085.

Foram preservados:

1. ordem funcional da Pessoa compatível com os registros;
2. Home pública e Tela Hoje separadas;
3. rota contínua entre as cinco páginas;
4. 97 associações individuais a 23 perfis;
5. estados parciais, ausentes e não examinados;
6. dez estados da UXA-055 sem validação específica.

A promoção não modifica cobertura, validação ou maturidade dos objetos catalogados.

## 6. Prioridade de materialização preservada

```text
Visão Geral do Responsável
→ gestão completa de solicitações
→ Meus Coletivos
→ Central de Atualizações
→ Início do Participante
```

Nenhuma dessas superfícies foi iniciada.

## 7. Separações obrigatórias

- `GKR-SURF-PER-102` representa exclusivamente busca de Coletivos;
- `GKR-SURF-PER-201`, `202` e `203` representam mapa, lista e detalhe de oportunidades;
- `GKR-SURF-ORG-003` representa o estado institucional de oportunidade;
- `GKR-SURF-COM-005` permanece ligado aos dez SVGs não validados da UXA-055;
- `GKR-SURF-BND-001` é fronteira documental, não tela.

## 8. Estado vigente

- catálogo: `active` 0.10.0;
- galeria: `active` 0.5.0, promovida com ressalvas preservadas;
- cinco páginas visuais: `active` 0.3.0;
- matriz por SVG: `active` 0.3.0;
- jornadas da Pessoa, Coletivo e Organização: `draft`;
- protótipo e Engenharia de Produto: não iniciados.

O status dos instrumentos visuais não promove superfícies, transições ou jornadas.
