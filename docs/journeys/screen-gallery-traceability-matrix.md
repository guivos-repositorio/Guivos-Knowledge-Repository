---
id: GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
title: Matriz de Rastreabilidade Visual por SVG
status: active
version: 0.3.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
parent: GKR-JOURNEY-SCREEN-GALLERY-001
depends_on:
  - UXA-083
  - UXA-084
  - UXA-085
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - UXA-081
  - UXA-082
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Matriz de Rastreabilidade Visual por SVG

## 1. Finalidade

Esta matriz atribui individualmente um perfil de rastreabilidade a cada um dos 97 SVGs. Cada perfil declara superfície, entrada, saída, retorno ou interrupção, lacuna e validação, sem inventar precisão quando vários estados compartilham a mesma responsabilidade.

## 2. Veredito da UXA-084

**Aprovada com ressalvas no escopo documental de rastreabilidade.**

As 97 associações individuais foram confirmadas. A utilização de 23 perfis é aceita para inspeção e cobertura, mas não substitui análise semântica exclusiva de cada estado visual nem valida transições ou jornadas.

A UXA-085 promove esta matriz somente como instrumento documental vigente, preservando o conteúdo e todas as ressalvas do parecer.

## 3. Perfis de rastreabilidade

| Perfil | Superfície(s) | Entrada | Saída | Retorno ou interrupção | Lacuna | Validação |
|---|---|---|---|---|---|---|
| R01 | GKR-SURF-PER-001 | entrada pública | GKR-TRN-001 | permanecer ou retornar à Home | continuidade pública → protegida parcial | UXA-021 |
| R02 | GKR-SURF-PER-002; GKR-SURF-PER-003; GKR-SURF-PER-005 | GKR-TRN-001 | GKR-TRN-002 a GKR-TRN-005 | voltar, trocar modalidade, editar ou recusar | integração entre início protegido, expressão e compreensão | UXA-035 |
| R03 | GKR-SURF-PER-004 | GKR-TRN-003 | GKR-TRN-004 | trocar modalidade, editar, descartar ou interromper | expressão → inventário ainda parcial | UXA-069 |
| R04 | GKR-SURF-PER-006; GKR-SURF-PER-007 | GKR-TRN-005; GKR-TRN-006 | GKR-TRN-007 | revisar, recusar persistência ou retornar | compreensão → Tela Hoje não examinada | UXA-037 |
| R05 | GKR-SURF-PER-008 | GKR-TRN-007 | saída recorrente não consolidada | retorno recorrente não examinado | compreensão → Tela Hoje | UXA-010 |
| R06 | GKR-SURF-PER-201 | GKR-TRN-203; GKR-TRN-304 | GKR-TRN-204; GKR-TRN-210 | voltar ao contexto anterior ou alternar visualização | publicação → descoberta; mapa ↔ lista ↔ detalhe | UXA-025; UXA-027; UXA-031; UXA-033 |
| R07 | GKR-SURF-PER-202 | GKR-TRN-210; GKR-TRN-306 | GKR-TRN-211 | retornar ao mapa mantendo consulta compatível | sincronização mapa ↔ lista ↔ detalhe | UXA-029 |
| R08 | GKR-SURF-PER-203 | GKR-TRN-204; GKR-TRN-211 | GKR-TRN-205 | retornar ao mapa ou à lista | efeito externo não validado | UXA-012 |
| R09 | GKR-SURF-ORG-001 | entrada institucional protegida | GKR-TRN-201 | cancelar ação e retornar à visão geral | matriz institucional completa | UXA-017 |
| R10 | GKR-SURF-ORG-002; GKR-SURF-ORG-003 | GKR-TRN-201 | GKR-TRN-202; GKR-TRN-203 | editar, retirar, pausar ou encerrar conforme estado | publicação → descoberta não examinada | UXA-013 |
| R11 | GKR-SURF-COL-001 | GKR-TRN-102 ou entrada protegida do responsável | GKR-TRN-103; continuidade interna não materializada | retornar à busca ou sair do contexto protegido | Visão Geral do Responsável ausente | UXA-018; UXA-063 |
| R12 | GKR-SURF-PER-101; GKR-SURF-PER-102 | origem de exploração | GKR-TRN-101; GKR-TRN-102 | limpar filtros, voltar ou refazer busca | continuidade entre descoberta e perfil | UXA-061 |
| R13 | GKR-SURF-PER-103; GKR-SURF-COL-001 | GKR-TRN-102 | GKR-TRN-103 | retornar aos resultados | handoff para solicitação | UXA-063 |
| R14 | GKR-SURF-PER-104 | GKR-TRN-103 | GKR-TRN-104 | cancelar e retornar ao perfil | destino operacional do responsável ausente | UXA-065 |
| R15 | GKR-SURF-PER-105; GKR-SURF-COL-003 | GKR-TRN-104; GKR-TRN-106; GKR-TRN-109 | GKR-TRN-105; GKR-TRN-107 a GKR-TRN-109 | cancelar, responder, aguardar ou voltar à exploração | origem operacional e continuidade pós-decisão ausentes | UXA-067 na perspectiva da Pessoa |
| R16 | GKR-SURF-COM-001 | entrada protegida do anunciante | GKR-TRN-301 | editar, cancelar, pausar ou encerrar conforme estado | regras econômicas e estados residuais | UXA-041 |
| R17 | GKR-SURF-COM-001 | entrada protegida do anunciante | GKR-TRN-301 | editar, cancelar, pausar ou encerrar conforme estado | regras econômicas e estados residuais | UXA-052 |
| R18 | GKR-SURF-COM-002 | GKR-TRN-302; GKR-TRN-303 | GKR-TRN-304; GKR-TRN-306 | ignorar ou retornar ao contexto orgânico | integração orgânico ↔ patrocinado | UXA-043 |
| R19 | GKR-SURF-COM-003 | entrega comercial elegível | GKR-TRN-303 | retornar ao mapa ou lista orgânicos | continuidade transversal patrocinada | UXA-045 |
| R20 | GKR-SURF-COM-004 | GKR-TRN-301 | GKR-TRN-302; GKR-TRN-305 | pausar, revisar, encerrar ou contestar conforme estado | estados residuais e regras econômicas | UXA-047 |
| R21 | GKR-SURF-COM-004 | campanha ativa ou encerrada | retorno à gestão de campanha | reconciliar, revisar atribuição ou sair | atribuição e continuidade operacional | UXA-049 |
| R22 | GKR-SURF-COM-004 | GKR-TRN-301 | GKR-TRN-302; GKR-TRN-305 | pausar, revisar, encerrar ou contestar conforme estado | estados residuais e regras econômicas | UXA-054 |
| R23 | GKR-SURF-COM-005 | GKR-TRN-305 | não examinada | depende do estado; desfazer, contestar ou continuar não validados | dez estados residuais da UXA-055 | pendente de validação específica |

## 4. Associação individual dos 97 SVGs

| SVG | Perfil |
|---|---|
| `uxa-022-public-home-desktop.svg` | R01 |
| `uxa-034-protected-entry-access-mobile.svg` | R02 |
| `uxa-034-protected-entry-explanation-mobile.svg` | R02 |
| `uxa-034-protected-entry-sharing-mobile.svg` | R02 |
| `uxa-034-protected-entry-review-mobile.svg` | R02 |
| `uxa-068-guided-current-moment-orientation-mobile.svg` | R03 |
| `uxa-068-guided-current-moment-text-draft-mobile.svg` | R03 |
| `uxa-068-guided-current-moment-voice-preparation-mobile.svg` | R03 |
| `uxa-068-guided-current-moment-voice-recording-mobile.svg` | R03 |
| `uxa-068-guided-current-moment-voice-transcription-review-mobile.svg` | R03 |
| `uxa-068-guided-current-moment-focus-separation-mobile.svg` | R03 |
| `uxa-068-guided-current-moment-adaptive-clarification-mobile.svg` | R03 |
| `uxa-068-guided-current-moment-structured-summary-mobile.svg` | R03 |
| `uxa-036-initial-understanding-processing-mobile.svg` | R04 |
| `uxa-036-initial-understanding-presentation-mobile.svg` | R04 |
| `uxa-036-initial-understanding-review-mobile.svg` | R04 |
| `uxa-036-initial-understanding-decision-mobile.svg` | R04 |
| `uxa-036-initial-understanding-insufficient-basis-mobile.svg` | R04 |
| `uxa-006-hoje-mobile.svg` | R05 |
| `uxa-024-opportunity-map-mobile.svg` | R06 |
| `uxa-026-opportunity-map-location-disabled-mobile.svg` | R06 |
| `uxa-030-opportunity-map-no-results-mobile.svg` | R06 |
| `uxa-032-opportunity-map-desktop.svg` | R06 |
| `uxa-032-opportunity-map-no-results-desktop.svg` | R06 |
| `uxa-028-opportunity-map-list-mobile.svg` | R07 |
| `uxa-007-opportunity-detail-mobile.svg` | R08 |
| `uxa-015-organization-overview-desktop.svg` | R09 |
| `uxa-008-organization-opportunity-registration-desktop.svg` | R10 |
| `uxa-016-collective-home-mobile.svg` | R11 |
| `uxa-060-collective-discovery-origin-mobile.svg` | R12 |
| `uxa-060-collective-explore-mobile.svg` | R12 |
| `uxa-060-collective-search-filters-mobile.svg` | R12 |
| `uxa-060-collective-search-results-mobile.svg` | R12 |
| `uxa-060-collective-search-no-results-mobile.svg` | R12 |
| `uxa-062-collective-public-profile-open-entry-mobile.svg` | R13 |
| `uxa-062-collective-public-profile-approval-entry-mobile.svg` | R13 |
| `uxa-062-collective-public-profile-closed-entry-mobile.svg` | R13 |
| `uxa-062-collective-public-profile-protected-mobile.svg` | R13 |
| `uxa-064-collective-participation-open-entry-review-mobile.svg` | R14 |
| `uxa-064-collective-participation-open-entry-confirmed-mobile.svg` | R14 |
| `uxa-064-collective-participation-approval-request-review-mobile.svg` | R14 |
| `uxa-064-collective-participation-approval-request-receipt-mobile.svg` | R14 |
| `uxa-064-collective-participation-protected-invite-review-mobile.svg` | R14 |
| `uxa-066-collective-pending-request-awaiting-decision-mobile.svg` | R15 |
| `uxa-066-collective-pending-request-protected-analysis-mobile.svg` | R15 |
| `uxa-066-collective-pending-request-additional-information-required-mobile.svg` | R15 |
| `uxa-066-collective-pending-request-additional-information-review-mobile.svg` | R15 |
| `uxa-066-collective-pending-request-approved-mobile.svg` | R15 |
| `uxa-066-collective-pending-request-refused-mobile.svg` | R15 |
| `uxa-066-collective-pending-request-cancelled-mobile.svg` | R15 |
| `uxa-066-collective-pending-request-expired-mobile.svg` | R15 |
| `uxa-040-opportunity-boost-eligibility-desktop.svg` | R16 |
| `uxa-040-opportunity-boost-objective-audience-desktop.svg` | R16 |
| `uxa-040-opportunity-boost-budget-schedule-desktop.svg` | R16 |
| `uxa-040-opportunity-boost-preview-confirmation-desktop.svg` | R16 |
| `uxa-040-opportunity-boost-submission-desktop.svg` | R16 |
| `uxa-051-opportunity-boost-eligibility-mobile.svg` | R17 |
| `uxa-051-opportunity-boost-objective-audience-mobile.svg` | R17 |
| `uxa-051-opportunity-boost-budget-schedule-mobile.svg` | R17 |
| `uxa-051-opportunity-boost-preview-confirmation-mobile.svg` | R17 |
| `uxa-051-opportunity-boost-submission-mobile.svg` | R17 |
| `uxa-042-sponsored-card-mobile.svg` | R18 |
| `uxa-042-sponsored-explanation-mobile.svg` | R18 |
| `uxa-042-sponsored-card-desktop.svg` | R18 |
| `uxa-042-sponsored-explanation-desktop.svg` | R18 |
| `uxa-042-social-financed-card-mobile.svg` | R18 |
| `uxa-042-social-financed-explanation-mobile.svg` | R18 |
| `uxa-044-sponsored-list-mobile.svg` | R19 |
| `uxa-044-sponsored-map-mobile.svg` | R19 |
| `uxa-044-sponsored-list-desktop.svg` | R19 |
| `uxa-044-sponsored-map-desktop.svg` | R19 |
| `uxa-046-campaign-scheduled-desktop.svg` | R20 |
| `uxa-046-campaign-active-desktop.svg` | R20 |
| `uxa-046-campaign-paused-desktop.svg` | R20 |
| `uxa-046-campaign-limited-desktop.svg` | R20 |
| `uxa-046-campaign-material-change-desktop.svg` | R20 |
| `uxa-046-campaign-closure-desktop.svg` | R20 |
| `uxa-048-aggregated-report-overview-desktop.svg` | R21 |
| `uxa-048-aggregated-report-attribution-desktop.svg` | R21 |
| `uxa-048-aggregated-report-overview-mobile.svg` | R21 |
| `uxa-048-aggregated-report-reconciliation-mobile.svg` | R21 |
| `uxa-053-campaign-scheduled-mobile.svg` | R22 |
| `uxa-053-campaign-active-mobile.svg` | R22 |
| `uxa-053-campaign-paused-mobile.svg` | R22 |
| `uxa-053-campaign-limited-mobile.svg` | R22 |
| `uxa-053-campaign-material-change-mobile.svg` | R22 |
| `uxa-053-campaign-closure-mobile.svg` | R22 |
| `uxa-055-sponsored-technical-error-mobile.svg` | R23 |
| `uxa-055-sponsored-inventory-unavailable-mobile.svg` | R23 |
| `uxa-055-low-organic-supply-mobile.svg` | R23 |
| `uxa-055-show-less-type-mobile.svg` | R23 |
| `uxa-055-hide-campaign-mobile.svg` | R23 |
| `uxa-055-report-content-mobile.svg` | R23 |
| `uxa-055-disable-sponsored-opportunities-mobile.svg` | R23 |
| `uxa-055-review-reverse-preferences-mobile.svg` | R23 |
| `uxa-055-contest-data-use-mobile.svg` | R23 |
| `uxa-055-advertiser-update-failure-mobile.svg` | R23 |

## 5. Totais e limites

- SVGs registrados: **97**;
- associações individuais: **97**;
- perfis documentais: **23**;
- com validação de origem registrada: **87**;
- pendentes de validação específica: **10**;
- arquivos visuais alterados pelas UXA-083, UXA-084 e UXA-085: **0**.

A associação a um perfil não valida automaticamente uma transição ou jornada. A matriz está `active` 0.3.0 após a promoção controlada da UXA-085, mantendo as ressalvas do parecer da UXA-084.

## 6. Próxima transição possível

**UXA-086 — Materialização Controlada da Visão Geral do Responsável do Coletivo**, mediante autorização separada.

A UXA-086 não é iniciada pela promoção desta matriz.
