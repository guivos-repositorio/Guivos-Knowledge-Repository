---
id: GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
title: Matriz de Rastreabilidade Visual por SVG
status: active
version: 0.11.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
parent: GKR-JOURNEY-SCREEN-GALLERY-001
depends_on:
  - UXA-083
  - UXA-084
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
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Matriz de Rastreabilidade Visual por SVG

## 1. Finalidade

Esta matriz atribui individualmente um perfil de rastreabilidade a cada um dos **107 SVGs**. Perfis documentais não substituem análise semântica exclusiva de cada estado e não validam automaticamente transições ou jornadas.

## 2. Estado do instrumento

A UXA-094 preserva as 107 associações e 27 perfis. `R26` e `R27` passam a refletir as versões reformuladas/validadas de `PER-106` e `PER-107`, e `TRN-110` passa a integralmente validada.

## 3. Perfis de rastreabilidade

| Perfil | Superfície(s) | Entrada | Saída | Retorno ou interrupção | Lacuna | Validação |
|---|---|---|---|---|---|---|
| R01 | PER-001 | entrada pública | TRN-001 | permanecer/retornar | continuidade pública → protegida | UXA-021 |
| R02 | PER-002/003/005 | TRN-001 | TRN-002 a 005 | voltar/trocar/editar/recusar | integração inicial | UXA-035 |
| R03 | PER-004 | TRN-003 | TRN-004 | trocar/editar/descartar | expressão → inventário | UXA-069 |
| R04 | PER-006/007 | TRN-005/006 | TRN-007 | revisar/recusar/retornar | compreensão → Hoje | UXA-037 |
| R05 | PER-008 | TRN-007 | continuidade recorrente | retorno não examinado | experiência recorrente | UXA-010 |
| R06 | PER-201 | TRN-203/304 | TRN-204/210 | voltar/alternar | publicação/mapa/lista/detalhe | UXA-025/027/031/033 |
| R07 | PER-202 | TRN-210/306 | TRN-211 | retornar ao mapa | mapa/lista/detalhe | UXA-029 |
| R08 | PER-203 | TRN-204/211 | TRN-205 | retornar | efeito externo | UXA-012 |
| R09 | ORG-001 | entrada institucional | TRN-201 | cancelar/retornar | matriz institucional | UXA-017 |
| R10 | ORG-002/003 | TRN-201 | TRN-202/203 | editar/retirar/pausar | publicação → descoberta | UXA-013 |
| R11 | COL-001 | busca ou entrada responsável | TRN-103 | retornar/sair | presença pública → gestão | UXA-018/063 |
| R12 | PER-101/102 | exploração | TRN-101/102 | limpar/voltar/refazer | descoberta → perfil | UXA-061 |
| R13 | PER-103/COL-001 | TRN-102 | TRN-103 | retornar | solicitação | UXA-063 |
| R14 | PER-104 | TRN-103 | TRN-104 | cancelar/retornar | handoff | UXA-065 |
| R15 | PER-105 | TRN-104/106/109 | TRN-105/107/108 | cancelar/responder/aguardar | outras continuidades separadas | UXA-067; aprovado UXA-092 |
| R16 | COM-001 | anunciante | TRN-301 | editar/cancelar | regras econômicas | UXA-041 |
| R17 | COM-001 | anunciante | TRN-301 | editar/cancelar | estados residuais | UXA-052 |
| R18 | COM-002 | TRN-302/303 | TRN-304/306 | ignorar/retornar | orgânico ↔ patrocinado | UXA-043 |
| R19 | COM-003 | entrega elegível | TRN-303 | retornar | continuidade patrocinada | UXA-045 |
| R20 | COM-004 | TRN-301 | TRN-302/305 | pausar/revisar/encerrar | estados residuais | UXA-047 |
| R21 | COM-004 | campanha | retorno à gestão | reconciliar/revisar | atribuição | UXA-049 |
| R22 | COM-004 | TRN-301 | TRN-302/305 | pausar/revisar/encerrar | estados residuais | UXA-054 |
| R23 | COM-005 | TRN-305 | não examinada | conforme estado | 10 estados UXA-055 | pendente |
| R24 | COL-002 | representação válida | TRN-112 | permanecer/retornar | fechada | UXA-087; TRN-112 UXA-090 |
| R25 | COL-003 | TRN-105/107/112 | TRN-106/108/109 | voltar/aguardar/interromper | handoffs fechados nos gates | UXA-089/090/092 |
| R26 | PER-106 | TRN-108 ou acesso recorrente | **TRN-110** | trocar categoria/voltar | P0B separado | **UXA-092; gatilho revalidado UXA-094** |
| R27 | PER-107 | **TRN-110** ou atualização autorizada | PER-105/PER-106; TRN-111 futuro | retornar/ajustar preferência | PER-108/TRN-111; P0B/P1 | **UXA-094; TRN-110 integralmente validada** |

## 4. Associação individual dos 107 SVGs

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
| `uxa-086-collective-responsible-overview-desktop.svg` | R24 |
| `uxa-088-collective-request-management-queue-desktop.svg` | R25 |
| `uxa-088-collective-request-management-detail-desktop.svg` | R25 |
| `uxa-088-collective-request-management-protected-detail-desktop.svg` | R25 |
| `uxa-088-collective-request-management-additional-information-desktop.svg` | R25 |
| `uxa-088-collective-request-management-approve-confirmation-desktop.svg` | R25 |
| `uxa-088-collective-request-management-refuse-confirmation-desktop.svg` | R25 |
| `uxa-088-collective-request-management-insufficient-authority-desktop.svg` | R25 |
| `uxa-091-my-collectives-mobile.svg` | R26 |
| `uxa-093-collective-updates-center-mobile.svg` | R27 |
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

- SVGs registrados: **107**;
- associações individuais: **107**;
- perfis documentais: **27**;
- com validação funcional vigente: **97**;
- pendentes de validação específica: **10**, exclusivamente UXA-055;
- arquivos visuais novos na UXA-094: **0**;
- arquivos existentes reformulados pela UXA-094: **2**.

## 6. Próxima transição possível

**UXA-095 — Materialização/Reformulação Controlada do Início do Participante (`GKR-SURF-PER-108`) e Refinamento de `GKR-TRN-111`**, mediante autorização separada.

A UXA-095 não é iniciada por esta matriz.
