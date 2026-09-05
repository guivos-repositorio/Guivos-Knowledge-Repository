---
id: GKR-JOURNEY-SCREEN-GALLERY-OPPORTUNITIES-ORGANIZATION-001
title: Organização e Oportunidades
status: superseded
version: 0.6.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-05
parent: GKR-JOURNEY-SCREEN-GALLERY-001
related:
  - UXA-081
  - UXA-082
  - UXA-083
  - UXA-084
  - UXA-085
  - UXA-098
  - UXA-101
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-UX-ORGCOL-UX-STATE-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-ORGCOL-POST313-RECON-001
normative: false
maturity: historical_provenance_only
---

# Organização e Oportunidades

> **F-016-A — desmaterialização física.** Os SVGs desta frente foram removidos do corpus vigente. Qualquer nome `.svg` remanescente neste documento é **proveniência histórica**, não arquivo disponível, não autoridade visual e não autorização de Design. O contrato funcional permanece governado pelo texto e pelas autoridades funcionais relacionadas.


[← Pessoa](screen-gallery-person.md) · [Índice](screen-gallery.md) · [Matriz por SVG](screen-gallery-traceability-matrix.md) · [Próxima: Coletivos →](screen-gallery-collectives.md)

## 1. Ordem funcional de inspeção

```text
contexto institucional da Organização
→ atores, autoridades e jobs já definidos
→ Arquitetura da Informação autenticada definida pre-surface-map
→ mapa final de superfícies ainda não canônico
→ wireframe principal autenticado ainda a definir
→ cadastro e ativação institucional de oportunidade
→ mapa de oportunidades
↔ lista sincronizada
→ detalhe
→ revisão consciente de saída no próprio detalhe
→ fronteira externa identificada
```

A UXA-098 valida `GKR-TRN-203`, `204`, `210` e `211`. A UXA-101 valida `GKR-TRN-205` até `GKR-SURF-BND-001`, preservando o destino externo fora da autoridade da Guivos.

A reconciliação pós-PR #313/#314 separa a UX principal autenticada da Organização do fluxo especializado de oportunidades:

```text
UXA-015/017 + antiga materialização de ORG-001
→ REMOVIDOS DO CORPUS CORRENTE / PROVENIÊNCIA PRESERVADA NO HISTÓRICO GIT

UXA-008/013 — CADASTRO DE OPORTUNIDADE
→ MATURIDADE PRÓPRIA PRESERVADA
```

`GKR-UX-ORGCOL-AUTH-JOBS-001` e `GKR-UX-ORGCOL-AUTH-IA-001` já definem a base funcional e a Arquitetura da Informação autenticada. Isso **não** define mapa final de superfícies, wireframe, UI, protótipo ou implementação.

## 2. Organização

**Cobertura física:** 1 SVG · IDs associados: `GKR-SURF-ORG-001`, `GKR-SURF-ORG-002`, `GKR-SURF-ORG-003`.

- `GKR-SURF-ORG-001`: contrato funcional/IA preservado; `UXA-015/017` foram removidos do corpus corrente; a materialização visual pertence exclusivamente a Design;
- `GKR-SURF-ORG-002/003`: fluxo especializado de cadastro/ativação preserva autoridade `UXA-008/013`, com continuidade de publicação em `UXA-098`.


### `uxa-008-organization-opportunity-registration-desktop.svg`


O cadastro de oportunidade permanece um fluxo especializado independente e não define a arquitetura completa da Organização.

## 3. Mapa de Oportunidades

**Cobertura:** 5 SVGs · ID: `GKR-SURF-PER-201` · validações locais: `UXA-025`, `UXA-027`, `UXA-031`, `UXA-033`; integração: `UXA-098`

### `uxa-024-opportunity-map-mobile.svg`


### `uxa-026-opportunity-map-location-disabled-mobile.svg`


### `uxa-030-opportunity-map-no-results-mobile.svg`


### `uxa-032-opportunity-map-desktop.svg`


### `uxa-032-opportunity-map-no-results-desktop.svg`


## 4. Lista de Oportunidades

**Cobertura:** 1 SVG · ID: `GKR-SURF-PER-202` · validação local: `UXA-029`; integração com Mapa e Detalhe: `UXA-098`

### `uxa-028-opportunity-map-list-mobile.svg`


## 5. Detalhe e revisão consciente de saída

**Cobertura:** 1 SVG · ID: `GKR-SURF-PER-203` · validação original: `UXA-012`; entradas integradas: `UXA-098`; reformulação/revalidação de saída: `UXA-101`

### `uxa-007-opportunity-detail-mobile.svg`


O mesmo SVG mostra dois estados da mesma responsabilidade `PER-203`: o Detalhe e a revisão acionada por `Ver como participar`. A revisão identifica que a próxima etapa é externa, quem responde por ela, o tratamento de dados/contexto, os limites da Guivos e as opções de continuar ou voltar.

Nenhum SVG é criado para `BND-001`.

## 6. Limite

A continuidade orgânica `publicação → descoberta → Mapa/Lista → Detalhe → fronteira externa` está documentalmente validada nos limites de autoridade definidos pelas UXA-098 e UXA-101.

Isso **não** valida inscrição, reserva, compra, contratação, disponibilidade, autenticação ou qualquer outro processo executado pelo terceiro depois de `BND-001`. Integrações patrocinadas `TRN-304/306` permanecem parciais.

Também não valida a UX principal autenticada da Organização. Atores, autoridades, jobs e a Arquitetura da Informação autenticada já estão definidos; o próximo trabalho documental limita-se a contratos funcionais, fluxos/estados críticos e handoff; a materialização visual pertence exclusivamente a Design.

O status `active` registra o instrumento de inspeção e não inicia protótipo ou Engenharia de Produto.

[← Pessoa](screen-gallery-person.md) · [Índice](screen-gallery.md) · [Matriz por SVG](screen-gallery-traceability-matrix.md) · [Próxima: Coletivos →](screen-gallery-collectives.md)