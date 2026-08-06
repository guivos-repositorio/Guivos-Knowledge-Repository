---
id: GKR-JOURNEY-SCREEN-GALLERY-001
title: Galeria Visual Integrada de Telas
status: draft
version: 0.1.1
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
related:
  - UXA-005
  - UXA-070
  - UXA-075
  - UXA-080
  - UXA-081
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Galeria Visual Integrada de Telas

## 1. Finalidade

Esta seção reúne os 97 SVGs existentes em `docs/assets/wireframes/` para inspeção humana de assertividade, coerência e cobertura.

Os arquivos permanecem em seus caminhos canônicos e são incorporados por referência. A galeria não modifica SVGs, valida transições, fecha lacunas, promove jornadas ou autoriza implementação.

## 2. Abrir as galerias

| Grupo | SVGs | Estado |
|---|---:|---|
| [Pessoa — Fundação, Entrada e Compreensão](screen-gallery-person.md) | 19 | validados nos pacotes de origem |
| [Oportunidades e Organização](screen-gallery-opportunities-organization.md) | 9 | validados nos pacotes de origem |
| [Coletivos](screen-gallery-collectives.md) | 23 | validados nas perspectivas cobertas |
| [Opportunity Boost — Configuração e Exposição](screen-gallery-opportunity-boost-exposure.md) | 20 | validados nos pacotes de origem |
| [Opportunity Boost — Operação, Relatórios e Resíduos](screen-gallery-opportunity-boost-operations.md) | 26 | 16 validados e 10 pendentes |
| **Total** | **97** | **87 validados e 10 pendentes** |

A divisão em páginas evita sobrecarga de renderização e mantém um único ponto de entrada para a inspeção.

## 3. Auditoria

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 97 |
| com validação funcional registrada | 87 |
| pendentes de validação específica | 10 |
| IDs com referência visual direta ou agrupada | 25 de 40 |
| responsabilidades sem SVG dedicado | 14 |
| fronteira documental sem tela por definição | 1 |

A quantidade de SVGs não equivale à quantidade de superfícies: estados alternativos e dispositivos podem compartilhar a mesma responsabilidade granular.

## 4. Responsabilidades sem SVG dedicado

- `GKR-SURF-PER-106` — Meus Coletivos;
- `GKR-SURF-PER-107` — Central de Atualizações;
- `GKR-SURF-PER-108` — Início do Participante;
- `GKR-SURF-COL-002` — Visão Geral do Responsável;
- `GKR-SURF-COL-003` — gestão de solicitações na origem operacional;
- `GKR-SURF-COL-004` a `GKR-SURF-COL-008` — operação interna e institucional do Coletivo;
- `GKR-SURF-ORG-004` a `GKR-SURF-ORG-007` — relação com Coletivos e resultados institucionais.

`GKR-SURF-BND-001` permanece intencionalmente sem tela Guivos.

## 5. Achados preservados

- os dez SVGs da UXA-055 permanecem sem validação funcional específica;
- compreensão inicial e Tela Hoje existem separadamente, mas sua continuidade não foi validada;
- a operação bilateral das solicitações de Coletivos permanece incompleta;
- Meus Coletivos, Central de Atualizações, Início do Participante e Visão Geral do Responsável permanecem ausentes ou pendentes;
- a relação Organização–Coletivo permanece sem materialização visual;
- publicação, mapa, lista, detalhe e fronteira externa não formam jornada integrada validada;
- erros, retornos e interrupções permanecem dispersos.

## 6. Estado

A galeria e suas páginas permanecem `draft` até revisão funcional e visual específica. Sua presença na navegação não aprova assertividade visual ou prontidão de produto.

## 7. Próxima transição possível

**UXA-082 — Validação Funcional e Visual da Galeria Integrada e Priorização Governada das Lacunas.**

A UXA-082 não é iniciada por este pacote e exige autorização separada.
