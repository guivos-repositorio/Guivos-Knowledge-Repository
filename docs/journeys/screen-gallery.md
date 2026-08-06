---
id: GKR-JOURNEY-SCREEN-GALLERY-001
title: Galeria Visual Integrada de Telas
status: draft
version: 0.1.0
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

Esta galeria reúne, em uma única página de inspeção, todos os arquivos SVG atualmente existentes em `docs/assets/wireframes/`.

Ela foi criada para facilitar a verificação humana de assertividade, coerência visual, cobertura por participante e continuidade entre telas.

A galeria é um instrumento observacional. Ela não:

- substitui os artefatos canônicos de origem;
- altera maturidades ou estados registrados;
- valida transições de entrada ou saída;
- promove jornadas incompletas;
- transforma responsabilidades sem interface em telas existentes;
- autoriza protótipo, aplicação ou Engenharia de Produto.

## 2. Resultado da auditoria

| Família | SVGs existentes | Com validação funcional registrada | Pendentes de validação específica |
|---|---:|---:|---:|
| Fundação pública e experiência recorrente | 2 | 2 | 0 |
| Início protegido, compreensão e expressão guiada | 17 | 17 | 0 |
| Oportunidades orgânicas | 7 | 7 | 0 |
| Organização | 2 | 2 | 0 |
| Coletivo — referência inicial | 1 | 1 | 0 |
| Coletivos — cobertura móvel | 22 | 22 | 0 |
| Opportunity Boost | 46 | 36 | 10 |
| **Total** | **97** | **87** | **10** |

Os 97 SVGs são arquivos visuais distintos. Essa contagem não equivale a 97 superfícies granulares, porque uma responsabilidade pode possuir vários estados, dispositivos ou variantes.

## 3. Cobertura perante o registro granular

| Condição | IDs granulares |
|---|---:|
| com ao menos uma referência visual direta ou agrupada | 25 |
| sem SVG dedicado | 14 |
| fronteira documental intencionalmente sem tela | 1 |
| **Total do registro de superfícies** | **40** |

A cobertura visual direta ou agrupada alcança 25 dos 40 IDs registrados. Isso não significa que as 25 continuidades estejam validadas ponta a ponta.

## 4. Regra de rastreabilidade

Cada visual apresenta:

- nome exato do arquivo;
- ID granular relacionado;
- pacote de materialização;
- pacote de validação, quando existente;
- canal inferido exclusivamente pelo sufixo do arquivo;
- estado de validação preservado.

Quando vários SVGs pertencem à mesma responsabilidade, todos apontam para o mesmo ID ou conjunto controlado de IDs. Essa associação facilita a inspeção, mas não substitui o detalhamento obrigatório do registro de superfícies.

## 5. Galeria

??? abstract "Fundação pública e experiência recorrente — 2 SVGs"

    | Arquivo e visual | Rastreabilidade |
    |---|---|
    | `uxa-022-public-home-desktop.svg`<br>[![uxa-022-public-home-desktop.svg](../assets/wireframes/uxa-022-public-home-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-022-public-home-desktop.svg) | `GKR-SURF-PER-001`<br>Origem: `UXA-022`<br>Validação: `UXA-021`<br>Canal: computador<br>Estado: **validado** |
    | `uxa-006-hoje-mobile.svg`<br>[![uxa-006-hoje-mobile.svg](../assets/wireframes/uxa-006-hoje-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-006-hoje-mobile.svg) | `GKR-SURF-PER-008`<br>Origem: `UXA-006`<br>Validação: `UXA-010`<br>Canal: móvel<br>Estado: **validado** |

??? abstract "Início protegido — 4 SVGs"

    | Arquivo e visual | Rastreabilidade |
    |---|---|
    | `uxa-034-protected-entry-access-mobile.svg`<br>[![uxa-034-protected-entry-access-mobile.svg](../assets/wireframes/uxa-034-protected-entry-access-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-034-protected-entry-access-mobile.svg) | `GKR-SURF-PER-002; GKR-SURF-PER-003; GKR-SURF-PER-005`<br>Origem: `UXA-034`<br>Validação: `UXA-035`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-034-protected-entry-explanation-mobile.svg`<br>[![uxa-034-protected-entry-explanation-mobile.svg](../assets/wireframes/uxa-034-protected-entry-explanation-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-034-protected-entry-explanation-mobile.svg) | `GKR-SURF-PER-002; GKR-SURF-PER-003; GKR-SURF-PER-005`<br>Origem: `UXA-034`<br>Validação: `UXA-035`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-034-protected-entry-review-mobile.svg`<br>[![uxa-034-protected-entry-review-mobile.svg](../assets/wireframes/uxa-034-protected-entry-review-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-034-protected-entry-review-mobile.svg) | `GKR-SURF-PER-002; GKR-SURF-PER-003; GKR-SURF-PER-005`<br>Origem: `UXA-034`<br>Validação: `UXA-035`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-034-protected-entry-sharing-mobile.svg`<br>[![uxa-034-protected-entry-sharing-mobile.svg](../assets/wireframes/uxa-034-protected-entry-sharing-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-034-protected-entry-sharing-mobile.svg) | `GKR-SURF-PER-002; GKR-SURF-PER-003; GKR-SURF-PER-005`<br>Origem: `UXA-034`<br>Validação: `UXA-035`<br>Canal: móvel<br>Estado: **validado** |

??? abstract "Compreensão inicial — 5 SVGs"

    | Arquivo e visual | Rastreabilidade |
    |---|---|
    | `uxa-036-initial-understanding-decision-mobile.svg`<br>[![uxa-036-initial-understanding-decision-mobile.svg](../assets/wireframes/uxa-036-initial-understanding-decision-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-036-initial-understanding-decision-mobile.svg) | `GKR-SURF-PER-006; GKR-SURF-PER-007`<br>Origem: `UXA-036`<br>Validação: `UXA-037`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-036-initial-understanding-processing-mobile.svg`<br>[![uxa-036-initial-understanding-processing-mobile.svg](../assets/wireframes/uxa-036-initial-understanding-processing-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-036-initial-understanding-processing-mobile.svg) | `GKR-SURF-PER-006; GKR-SURF-PER-007`<br>Origem: `UXA-036`<br>Validação: `UXA-037`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-036-initial-understanding-review-mobile.svg`<br>[![uxa-036-initial-understanding-review-mobile.svg](../assets/wireframes/uxa-036-initial-understanding-review-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-036-initial-understanding-review-mobile.svg) | `GKR-SURF-PER-006; GKR-SURF-PER-007`<br>Origem: `UXA-036`<br>Validação: `UXA-037`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-036-initial-understanding-source-mobile.svg`<br>[![uxa-036-initial-understanding-source-mobile.svg](../assets/wireframes/uxa-036-initial-understanding-source-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-036-initial-understanding-source-mobile.svg) | `GKR-SURF-PER-006; GKR-SURF-PER-007`<br>Origem: `UXA-036`<br>Validação: `UXA-037`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-036-initial-understanding-summary-mobile.svg`<br>[![uxa-036-initial-understanding-summary-mobile.svg](../assets/wireframes/uxa-036-initial-understanding-summary-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-036-initial-understanding-summary-mobile.svg) | `GKR-SURF-PER-006; GKR-SURF-PER-007`<br>Origem: `UXA-036`<br>Validação: `UXA-037`<br>Canal: móvel<br>Estado: **validado** |

??? abstract "Expressão guiada do momento atual — 8 SVGs"

    | Arquivo e visual | Rastreabilidade |
    |---|---|
    | `uxa-068-guided-current-moment-confirmation-mobile.svg`<br>[![uxa-068-guided-current-moment-confirmation-mobile.svg](../assets/wireframes/uxa-068-guided-current-moment-confirmation-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-068-guided-current-moment-confirmation-mobile.svg) | `GKR-SURF-PER-004`<br>Origem: `UXA-068`<br>Validação: `UXA-069`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-068-guided-current-moment-intro-mobile.svg`<br>[![uxa-068-guided-current-moment-intro-mobile.svg](../assets/wireframes/uxa-068-guided-current-moment-intro-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-068-guided-current-moment-intro-mobile.svg) | `GKR-SURF-PER-004`<br>Origem: `UXA-068`<br>Validação: `UXA-069`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-068-guided-current-moment-review-mobile.svg`<br>[![uxa-068-guided-current-moment-review-mobile.svg](../assets/wireframes/uxa-068-guided-current-moment-review-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-068-guided-current-moment-review-mobile.svg) | `GKR-SURF-PER-004`<br>Origem: `UXA-068`<br>Validação: `UXA-069`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-068-guided-current-moment-text-mobile.svg`<br>[![uxa-068-guided-current-moment-text-mobile.svg](../assets/wireframes/uxa-068-guided-current-moment-text-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-068-guided-current-moment-text-mobile.svg) | `GKR-SURF-PER-004`<br>Origem: `UXA-068`<br>Validação: `UXA-069`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-068-guided-current-moment-voice-mobile.svg`<br>[![uxa-068-guided-current-moment-voice-mobile.svg](../assets/wireframes/uxa-068-guided-current-moment-voice-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-068-guided-current-moment-voice-mobile.svg) | `GKR-SURF-PER-004`<br>Origem: `UXA-068`<br>Validação: `UXA-069`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-068-guided-current-moment-voice-paused-mobile.svg`<br>[![uxa-068-guided-current-moment-voice-paused-mobile.svg](../assets/wireframes/uxa-068-guided-current-moment-voice-paused-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-068-guided-current-moment-voice-paused-mobile.svg) | `GKR-SURF-PER-004`<br>Origem: `UXA-068`<br>Validação: `UXA-069`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-068-guided-current-moment-voice-recording-mobile.svg`<br>[![uxa-068-guided-current-moment-voice-recording-mobile.svg](../assets/wireframes/uxa-068-guided-current-moment-voice-recording-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-068-guided-current-moment-voice-recording-mobile.svg) | `GKR-SURF-PER-004`<br>Origem: `UXA-068`<br>Validação: `UXA-069`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-068-guided-current-moment-voice-review-mobile.svg`<br>[![uxa-068-guided-current-moment-voice-review-mobile.svg](../assets/wireframes/uxa-068-guided-current-moment-voice-review-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-068-guided-current-moment-voice-review-mobile.svg) | `GKR-SURF-PER-004`<br>Origem: `UXA-068`<br>Validação: `UXA-069`<br>Canal: móvel<br>Estado: **validado** |

??? abstract "Oportunidades orgânicas — 7 SVGs"

    | Arquivo e visual | Rastreabilidade |
    |---|---|
    | `uxa-024-opportunity-map-mobile.svg`<br>[![uxa-024-opportunity-map-mobile.svg](../assets/wireframes/uxa-024-opportunity-map-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-024-opportunity-map-mobile.svg) | `GKR-SURF-PER-201`<br>Origem: `UXA-024`<br>Validação: `UXA-025`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-026-opportunity-map-location-disabled-mobile.svg`<br>[![uxa-026-opportunity-map-location-disabled-mobile.svg](../assets/wireframes/uxa-026-opportunity-map-location-disabled-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-026-opportunity-map-location-disabled-mobile.svg) | `GKR-SURF-PER-201`<br>Origem: `UXA-026`<br>Validação: `UXA-027`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-028-opportunity-map-list-mobile.svg`<br>[![uxa-028-opportunity-map-list-mobile.svg](../assets/wireframes/uxa-028-opportunity-map-list-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-028-opportunity-map-list-mobile.svg) | `GKR-SURF-PER-202`<br>Origem: `UXA-028`<br>Validação: `UXA-029`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-030-opportunity-map-no-results-mobile.svg`<br>[![uxa-030-opportunity-map-no-results-mobile.svg](../assets/wireframes/uxa-030-opportunity-map-no-results-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-030-opportunity-map-no-results-mobile.svg) | `GKR-SURF-PER-201`<br>Origem: `UXA-030`<br>Validação: `UXA-031`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-032-opportunity-map-desktop.svg`<br>[![uxa-032-opportunity-map-desktop.svg](../assets/wireframes/uxa-032-opportunity-map-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-032-opportunity-map-desktop.svg) | `GKR-SURF-PER-201`<br>Origem: `UXA-032`<br>Validação: `UXA-033`<br>Canal: computador<br>Estado: **validado** |
    | `uxa-032-opportunity-map-no-results-desktop.svg`<br>[![uxa-032-opportunity-map-no-results-desktop.svg](../assets/wireframes/uxa-032-opportunity-map-no-results-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-032-opportunity-map-no-results-desktop.svg) | `GKR-SURF-PER-201`<br>Origem: `UXA-032`<br>Validação: `UXA-033`<br>Canal: computador<br>Estado: **validado** |
    | `uxa-007-opportunity-detail-mobile.svg`<br>[![uxa-007-opportunity-detail-mobile.svg](../assets/wireframes/uxa-007-opportunity-detail-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-007-opportunity-detail-mobile.svg) | `GKR-SURF-PER-203`<br>Origem: `UXA-007`<br>Validação: `UXA-012`<br>Canal: móvel<br>Estado: **validado** |

??? abstract "Organização — 2 SVGs"

    | Arquivo e visual | Rastreabilidade |
    |---|---|
    | `uxa-015-organization-overview-desktop.svg`<br>[![uxa-015-organization-overview-desktop.svg](../assets/wireframes/uxa-015-organization-overview-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-015-organization-overview-desktop.svg) | `GKR-SURF-ORG-001`<br>Origem: `UXA-015`<br>Validação: `UXA-017`<br>Canal: computador<br>Estado: **validado** |
    | `uxa-008-organization-opportunity-registration-desktop.svg`<br>[![uxa-008-organization-opportunity-registration-desktop.svg](../assets/wireframes/uxa-008-organization-opportunity-registration-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-008-organization-opportunity-registration-desktop.svg) | `GKR-SURF-ORG-002; GKR-SURF-ORG-003`<br>Origem: `UXA-008`<br>Validação: `UXA-013`<br>Canal: computador<br>Estado: **validado** |

??? abstract "Coletivo — referência inicial — 1 SVG"

    | Arquivo e visual | Rastreabilidade |
    |---|---|
    | `uxa-016-collective-home-mobile.svg`<br>[![uxa-016-collective-home-mobile.svg](../assets/wireframes/uxa-016-collective-home-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-016-collective-home-mobile.svg) | `GKR-SURF-COL-001`<br>Origem: `UXA-016`<br>Validação: `UXA-018`<br>Canal: móvel<br>Estado: **validado** |

??? abstract "Coletivos — descoberta e busca — 5 SVGs"

    | Arquivo e visual | Rastreabilidade |
    |---|---|
    | `uxa-060-collective-explore-empty-mobile.svg`<br>[![uxa-060-collective-explore-empty-mobile.svg](../assets/wireframes/uxa-060-collective-explore-empty-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-060-collective-explore-empty-mobile.svg) | `GKR-SURF-PER-101; GKR-SURF-PER-102`<br>Origem: `UXA-060`<br>Validação: `UXA-061`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-060-collective-explore-mobile.svg`<br>[![uxa-060-collective-explore-mobile.svg](../assets/wireframes/uxa-060-collective-explore-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-060-collective-explore-mobile.svg) | `GKR-SURF-PER-101; GKR-SURF-PER-102`<br>Origem: `UXA-060`<br>Validação: `UXA-061`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-060-collective-explore-results-mobile.svg`<br>[![uxa-060-collective-explore-results-mobile.svg](../assets/wireframes/uxa-060-collective-explore-results-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-060-collective-explore-results-mobile.svg) | `GKR-SURF-PER-101; GKR-SURF-PER-102`<br>Origem: `UXA-060`<br>Validação: `UXA-061`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-060-collective-explore-search-mobile.svg`<br>[![uxa-060-collective-explore-search-mobile.svg](../assets/wireframes/uxa-060-collective-explore-search-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-060-collective-explore-search-mobile.svg) | `GKR-SURF-PER-101; GKR-SURF-PER-102`<br>Origem: `UXA-060`<br>Validação: `UXA-061`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-060-collective-explore-with-filters-mobile.svg`<br>[![uxa-060-collective-explore-with-filters-mobile.svg](../assets/wireframes/uxa-060-collective-explore-with-filters-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-060-collective-explore-with-filters-mobile.svg) | `GKR-SURF-PER-101; GKR-SURF-PER-102`<br>Origem: `UXA-060`<br>Validação: `UXA-061`<br>Canal: móvel<br>Estado: **validado** |

??? abstract "Coletivos — Perfil Público — 4 SVGs"

    | Arquivo e visual | Rastreabilidade |
    |---|---|
    | `uxa-062-collective-public-profile-about-mobile.svg`<br>[![uxa-062-collective-public-profile-about-mobile.svg](../assets/wireframes/uxa-062-collective-public-profile-about-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-062-collective-public-profile-about-mobile.svg) | `GKR-SURF-PER-103; GKR-SURF-COL-001`<br>Origem: `UXA-062`<br>Validação: `UXA-063`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-062-collective-public-profile-activities-mobile.svg`<br>[![uxa-062-collective-public-profile-activities-mobile.svg](../assets/wireframes/uxa-062-collective-public-profile-activities-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-062-collective-public-profile-activities-mobile.svg) | `GKR-SURF-PER-103; GKR-SURF-COL-001`<br>Origem: `UXA-062`<br>Validação: `UXA-063`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-062-collective-public-profile-mobile.svg`<br>[![uxa-062-collective-public-profile-mobile.svg](../assets/wireframes/uxa-062-collective-public-profile-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-062-collective-public-profile-mobile.svg) | `GKR-SURF-PER-103; GKR-SURF-COL-001`<br>Origem: `UXA-062`<br>Validação: `UXA-063`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-062-collective-public-profile-rules-mobile.svg`<br>[![uxa-062-collective-public-profile-rules-mobile.svg](../assets/wireframes/uxa-062-collective-public-profile-rules-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-062-collective-public-profile-rules-mobile.svg) | `GKR-SURF-PER-103; GKR-SURF-COL-001`<br>Origem: `UXA-062`<br>Validação: `UXA-063`<br>Canal: móvel<br>Estado: **validado** |

??? abstract "Coletivos — revisão e solicitação — 5 SVGs"

    | Arquivo e visual | Rastreabilidade |
    |---|---|
    | `uxa-064-collective-participation-request-confirmation-mobile.svg`<br>[![uxa-064-collective-participation-request-confirmation-mobile.svg](../assets/wireframes/uxa-064-collective-participation-request-confirmation-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-064-collective-participation-request-confirmation-mobile.svg) | `GKR-SURF-PER-104`<br>Origem: `UXA-064`<br>Validação: `UXA-065`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-064-collective-participation-request-eligibility-mobile.svg`<br>[![uxa-064-collective-participation-request-eligibility-mobile.svg](../assets/wireframes/uxa-064-collective-participation-request-eligibility-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-064-collective-participation-request-eligibility-mobile.svg) | `GKR-SURF-PER-104`<br>Origem: `UXA-064`<br>Validação: `UXA-065`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-064-collective-participation-request-review-mobile.svg`<br>[![uxa-064-collective-participation-request-review-mobile.svg](../assets/wireframes/uxa-064-collective-participation-request-review-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-064-collective-participation-request-review-mobile.svg) | `GKR-SURF-PER-104`<br>Origem: `UXA-064`<br>Validação: `UXA-065`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-064-collective-participation-request-rules-mobile.svg`<br>[![uxa-064-collective-participation-request-rules-mobile.svg](../assets/wireframes/uxa-064-collective-participation-request-rules-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-064-collective-participation-request-rules-mobile.svg) | `GKR-SURF-PER-104`<br>Origem: `UXA-064`<br>Validação: `UXA-065`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-064-collective-participation-request-summary-mobile.svg`<br>[![uxa-064-collective-participation-request-summary-mobile.svg](../assets/wireframes/uxa-064-collective-participation-request-summary-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-064-collective-participation-request-summary-mobile.svg) | `GKR-SURF-PER-104`<br>Origem: `UXA-064`<br>Validação: `UXA-065`<br>Canal: móvel<br>Estado: **validado** |

??? abstract "Coletivos — Solicitação Pendente — 8 SVGs"

    | Arquivo e visual | Rastreabilidade |
    |---|---|
    | `uxa-066-collective-pending-request-approved-mobile.svg`<br>[![uxa-066-collective-pending-request-approved-mobile.svg](../assets/wireframes/uxa-066-collective-pending-request-approved-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-066-collective-pending-request-approved-mobile.svg) | `GKR-SURF-PER-105; GKR-SURF-COL-003`<br>Origem: `UXA-066`<br>Validação: `UXA-067`<br>Canal: móvel<br>Estado: **validado na perspectiva da Pessoa** |
    | `uxa-066-collective-pending-request-cancelled-mobile.svg`<br>[![uxa-066-collective-pending-request-cancelled-mobile.svg](../assets/wireframes/uxa-066-collective-pending-request-cancelled-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-066-collective-pending-request-cancelled-mobile.svg) | `GKR-SURF-PER-105; GKR-SURF-COL-003`<br>Origem: `UXA-066`<br>Validação: `UXA-067`<br>Canal: móvel<br>Estado: **validado na perspectiva da Pessoa** |
    | `uxa-066-collective-pending-request-expired-mobile.svg`<br>[![uxa-066-collective-pending-request-expired-mobile.svg](../assets/wireframes/uxa-066-collective-pending-request-expired-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-066-collective-pending-request-expired-mobile.svg) | `GKR-SURF-PER-105; GKR-SURF-COL-003`<br>Origem: `UXA-066`<br>Validação: `UXA-067`<br>Canal: móvel<br>Estado: **validado na perspectiva da Pessoa** |
    | `uxa-066-collective-pending-request-extra-info-mobile.svg`<br>[![uxa-066-collective-pending-request-extra-info-mobile.svg](../assets/wireframes/uxa-066-collective-pending-request-extra-info-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-066-collective-pending-request-extra-info-mobile.svg) | `GKR-SURF-PER-105; GKR-SURF-COL-003`<br>Origem: `UXA-066`<br>Validação: `UXA-067`<br>Canal: móvel<br>Estado: **validado na perspectiva da Pessoa** |
    | `uxa-066-collective-pending-request-pending-mobile.svg`<br>[![uxa-066-collective-pending-request-pending-mobile.svg](../assets/wireframes/uxa-066-collective-pending-request-pending-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-066-collective-pending-request-pending-mobile.svg) | `GKR-SURF-PER-105; GKR-SURF-COL-003`<br>Origem: `UXA-066`<br>Validação: `UXA-067`<br>Canal: móvel<br>Estado: **validado na perspectiva da Pessoa** |
    | `uxa-066-collective-pending-request-rejected-mobile.svg`<br>[![uxa-066-collective-pending-request-rejected-mobile.svg](../assets/wireframes/uxa-066-collective-pending-request-rejected-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-066-collective-pending-request-rejected-mobile.svg) | `GKR-SURF-PER-105; GKR-SURF-COL-003`<br>Origem: `UXA-066`<br>Validação: `UXA-067`<br>Canal: móvel<br>Estado: **validado na perspectiva da Pessoa** |
    | `uxa-066-collective-pending-request-response-mobile.svg`<br>[![uxa-066-collective-pending-request-response-mobile.svg](../assets/wireframes/uxa-066-collective-pending-request-response-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-066-collective-pending-request-response-mobile.svg) | `GKR-SURF-PER-105; GKR-SURF-COL-003`<br>Origem: `UXA-066`<br>Validação: `UXA-067`<br>Canal: móvel<br>Estado: **validado na perspectiva da Pessoa** |
    | `uxa-066-collective-pending-request-withdrawn-mobile.svg`<br>[![uxa-066-collective-pending-request-withdrawn-mobile.svg](../assets/wireframes/uxa-066-collective-pending-request-withdrawn-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-066-collective-pending-request-withdrawn-mobile.svg) | `GKR-SURF-PER-105; GKR-SURF-COL-003`<br>Origem: `UXA-066`<br>Validação: `UXA-067`<br>Canal: móvel<br>Estado: **validado na perspectiva da Pessoa** |

??? abstract "Opportunity Boost — fluxo do anunciante — 5 SVGs"

    | Arquivo e visual | Rastreabilidade |
    |---|---|
    | `uxa-040-opportunity-boost-advertiser-campaign-review-desktop.svg`<br>[![uxa-040-opportunity-boost-advertiser-campaign-review-desktop.svg](../assets/wireframes/uxa-040-opportunity-boost-advertiser-campaign-review-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-040-opportunity-boost-advertiser-campaign-review-desktop.svg) | `GKR-SURF-COM-001`<br>Origem: `UXA-040`<br>Validação: `UXA-041`<br>Canal: computador<br>Estado: **validado** |
    | `uxa-040-opportunity-boost-advertiser-campaign-setup-desktop.svg`<br>[![uxa-040-opportunity-boost-advertiser-campaign-setup-desktop.svg](../assets/wireframes/uxa-040-opportunity-boost-advertiser-campaign-setup-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-040-opportunity-boost-advertiser-campaign-setup-desktop.svg) | `GKR-SURF-COM-001`<br>Origem: `UXA-040`<br>Validação: `UXA-041`<br>Canal: computador<br>Estado: **validado** |
    | `uxa-040-opportunity-boost-advertiser-campaign-targeting-desktop.svg`<br>[![uxa-040-opportunity-boost-advertiser-campaign-targeting-desktop.svg](../assets/wireframes/uxa-040-opportunity-boost-advertiser-campaign-targeting-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-040-opportunity-boost-advertiser-campaign-targeting-desktop.svg) | `GKR-SURF-COM-001`<br>Origem: `UXA-040`<br>Validação: `UXA-041`<br>Canal: computador<br>Estado: **validado** |
    | `uxa-040-opportunity-boost-advertiser-confirmation-desktop.svg`<br>[![uxa-040-opportunity-boost-advertiser-confirmation-desktop.svg](../assets/wireframes/uxa-040-opportunity-boost-advertiser-confirmation-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-040-opportunity-boost-advertiser-confirmation-desktop.svg) | `GKR-SURF-COM-001`<br>Origem: `UXA-040`<br>Validação: `UXA-041`<br>Canal: computador<br>Estado: **validado** |
    | `uxa-040-opportunity-boost-advertiser-opportunity-selection-desktop.svg`<br>[![uxa-040-opportunity-boost-advertiser-opportunity-selection-desktop.svg](../assets/wireframes/uxa-040-opportunity-boost-advertiser-opportunity-selection-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-040-opportunity-boost-advertiser-opportunity-selection-desktop.svg) | `GKR-SURF-COM-001`<br>Origem: `UXA-040`<br>Validação: `UXA-041`<br>Canal: computador<br>Estado: **validado** |

??? abstract "Opportunity Boost — cartão patrocinado e explicação — 6 SVGs"

    | Arquivo e visual | Rastreabilidade |
    |---|---|
    | `uxa-042-opportunity-boost-explanation-mobile.svg`<br>[![uxa-042-opportunity-boost-explanation-mobile.svg](../assets/wireframes/uxa-042-opportunity-boost-explanation-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-042-opportunity-boost-explanation-mobile.svg) | `GKR-SURF-COM-002`<br>Origem: `UXA-042`<br>Validação: `UXA-043`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-042-opportunity-boost-explanation-desktop.svg`<br>[![uxa-042-opportunity-boost-explanation-desktop.svg](../assets/wireframes/uxa-042-opportunity-boost-explanation-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-042-opportunity-boost-explanation-desktop.svg) | `GKR-SURF-COM-002`<br>Origem: `UXA-042`<br>Validação: `UXA-043`<br>Canal: computador<br>Estado: **validado** |
    | `uxa-042-opportunity-boost-sponsored-card-desktop.svg`<br>[![uxa-042-opportunity-boost-sponsored-card-desktop.svg](../assets/wireframes/uxa-042-opportunity-boost-sponsored-card-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-042-opportunity-boost-sponsored-card-desktop.svg) | `GKR-SURF-COM-002`<br>Origem: `UXA-042`<br>Validação: `UXA-043`<br>Canal: computador<br>Estado: **validado** |
    | `uxa-042-opportunity-boost-sponsored-card-hidden-mobile.svg`<br>[![uxa-042-opportunity-boost-sponsored-card-hidden-mobile.svg](../assets/wireframes/uxa-042-opportunity-boost-sponsored-card-hidden-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-042-opportunity-boost-sponsored-card-hidden-mobile.svg) | `GKR-SURF-COM-002`<br>Origem: `UXA-042`<br>Validação: `UXA-043`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-042-opportunity-boost-sponsored-card-mobile.svg`<br>[![uxa-042-opportunity-boost-sponsored-card-mobile.svg](../assets/wireframes/uxa-042-opportunity-boost-sponsored-card-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-042-opportunity-boost-sponsored-card-mobile.svg) | `GKR-SURF-COM-002`<br>Origem: `UXA-042`<br>Validação: `UXA-043`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-042-opportunity-boost-sponsored-card-report-mobile.svg`<br>[![uxa-042-opportunity-boost-sponsored-card-report-mobile.svg](../assets/wireframes/uxa-042-opportunity-boost-sponsored-card-report-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-042-opportunity-boost-sponsored-card-report-mobile.svg) | `GKR-SURF-COM-002`<br>Origem: `UXA-042`<br>Validação: `UXA-043`<br>Canal: móvel<br>Estado: **validado** |

??? abstract "Opportunity Boost — estados patrocinados de lista e mapa — 4 SVGs"

    | Arquivo e visual | Rastreabilidade |
    |---|---|
    | `uxa-044-opportunity-boost-sponsored-list-desktop.svg`<br>[![uxa-044-opportunity-boost-sponsored-list-desktop.svg](../assets/wireframes/uxa-044-opportunity-boost-sponsored-list-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-044-opportunity-boost-sponsored-list-desktop.svg) | `GKR-SURF-COM-003`<br>Origem: `UXA-044`<br>Validação: `UXA-045`<br>Canal: computador<br>Estado: **validado** |
    | `uxa-044-opportunity-boost-sponsored-list-mobile.svg`<br>[![uxa-044-opportunity-boost-sponsored-list-mobile.svg](../assets/wireframes/uxa-044-opportunity-boost-sponsored-list-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-044-opportunity-boost-sponsored-list-mobile.svg) | `GKR-SURF-COM-003`<br>Origem: `UXA-044`<br>Validação: `UXA-045`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-044-opportunity-boost-sponsored-map-desktop.svg`<br>[![uxa-044-opportunity-boost-sponsored-map-desktop.svg](../assets/wireframes/uxa-044-opportunity-boost-sponsored-map-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-044-opportunity-boost-sponsored-map-desktop.svg) | `GKR-SURF-COM-003`<br>Origem: `UXA-044`<br>Validação: `UXA-045`<br>Canal: computador<br>Estado: **validado** |
    | `uxa-044-opportunity-boost-sponsored-map-mobile.svg`<br>[![uxa-044-opportunity-boost-sponsored-map-mobile.svg](../assets/wireframes/uxa-044-opportunity-boost-sponsored-map-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-044-opportunity-boost-sponsored-map-mobile.svg) | `GKR-SURF-COM-003`<br>Origem: `UXA-044`<br>Validação: `UXA-045`<br>Canal: móvel<br>Estado: **validado** |

??? abstract "Opportunity Boost — gestão da campanha ativa — computador — 6 SVGs"

    | Arquivo e visual | Rastreabilidade |
    |---|---|
    | `uxa-046-opportunity-boost-active-campaign-dashboard-desktop.svg`<br>[![uxa-046-opportunity-boost-active-campaign-dashboard-desktop.svg](../assets/wireframes/uxa-046-opportunity-boost-active-campaign-dashboard-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-046-opportunity-boost-active-campaign-dashboard-desktop.svg) | `GKR-SURF-COM-004`<br>Origem: `UXA-046`<br>Validação: `UXA-047`<br>Canal: computador<br>Estado: **validado** |
    | `uxa-046-opportunity-boost-active-campaign-ended-desktop.svg`<br>[![uxa-046-opportunity-boost-active-campaign-ended-desktop.svg](../assets/wireframes/uxa-046-opportunity-boost-active-campaign-ended-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-046-opportunity-boost-active-campaign-ended-desktop.svg) | `GKR-SURF-COM-004`<br>Origem: `UXA-046`<br>Validação: `UXA-047`<br>Canal: computador<br>Estado: **validado** |
    | `uxa-046-opportunity-boost-active-campaign-ending-desktop.svg`<br>[![uxa-046-opportunity-boost-active-campaign-ending-desktop.svg](../assets/wireframes/uxa-046-opportunity-boost-active-campaign-ending-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-046-opportunity-boost-active-campaign-ending-desktop.svg) | `GKR-SURF-COM-004`<br>Origem: `UXA-046`<br>Validação: `UXA-047`<br>Canal: computador<br>Estado: **validado** |
    | `uxa-046-opportunity-boost-active-campaign-paused-desktop.svg`<br>[![uxa-046-opportunity-boost-active-campaign-paused-desktop.svg](../assets/wireframes/uxa-046-opportunity-boost-active-campaign-paused-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-046-opportunity-boost-active-campaign-paused-desktop.svg) | `GKR-SURF-COM-004`<br>Origem: `UXA-046`<br>Validação: `UXA-047`<br>Canal: computador<br>Estado: **validado** |
    | `uxa-046-opportunity-boost-active-campaign-resumed-desktop.svg`<br>[![uxa-046-opportunity-boost-active-campaign-resumed-desktop.svg](../assets/wireframes/uxa-046-opportunity-boost-active-campaign-resumed-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-046-opportunity-boost-active-campaign-resumed-desktop.svg) | `GKR-SURF-COM-004`<br>Origem: `UXA-046`<br>Validação: `UXA-047`<br>Canal: computador<br>Estado: **validado** |
    | `uxa-046-opportunity-boost-active-campaign-settings-desktop.svg`<br>[![uxa-046-opportunity-boost-active-campaign-settings-desktop.svg](../assets/wireframes/uxa-046-opportunity-boost-active-campaign-settings-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-046-opportunity-boost-active-campaign-settings-desktop.svg) | `GKR-SURF-COM-004`<br>Origem: `UXA-046`<br>Validação: `UXA-047`<br>Canal: computador<br>Estado: **validado** |

??? abstract "Opportunity Boost — relatório agregado — 4 SVGs"

    | Arquivo e visual | Rastreabilidade |
    |---|---|
    | `uxa-048-opportunity-boost-aggregated-report-comparison-desktop.svg`<br>[![uxa-048-opportunity-boost-aggregated-report-comparison-desktop.svg](../assets/wireframes/uxa-048-opportunity-boost-aggregated-report-comparison-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-048-opportunity-boost-aggregated-report-comparison-desktop.svg) | `GKR-SURF-COM-004`<br>Origem: `UXA-048`<br>Validação: `UXA-049`<br>Canal: computador<br>Estado: **validado** |
    | `uxa-048-opportunity-boost-aggregated-report-dashboard-desktop.svg`<br>[![uxa-048-opportunity-boost-aggregated-report-dashboard-desktop.svg](../assets/wireframes/uxa-048-opportunity-boost-aggregated-report-dashboard-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-048-opportunity-boost-aggregated-report-dashboard-desktop.svg) | `GKR-SURF-COM-004`<br>Origem: `UXA-048`<br>Validação: `UXA-049`<br>Canal: computador<br>Estado: **validado** |
    | `uxa-048-opportunity-boost-aggregated-report-export-desktop.svg`<br>[![uxa-048-opportunity-boost-aggregated-report-export-desktop.svg](../assets/wireframes/uxa-048-opportunity-boost-aggregated-report-export-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-048-opportunity-boost-aggregated-report-export-desktop.svg) | `GKR-SURF-COM-004`<br>Origem: `UXA-048`<br>Validação: `UXA-049`<br>Canal: computador<br>Estado: **validado** |
    | `uxa-048-opportunity-boost-aggregated-report-period-desktop.svg`<br>[![uxa-048-opportunity-boost-aggregated-report-period-desktop.svg](../assets/wireframes/uxa-048-opportunity-boost-aggregated-report-period-desktop.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-048-opportunity-boost-aggregated-report-period-desktop.svg) | `GKR-SURF-COM-004`<br>Origem: `UXA-048`<br>Validação: `UXA-049`<br>Canal: computador<br>Estado: **validado** |

??? abstract "Opportunity Boost — configuração móvel do anunciante — 5 SVGs"

    | Arquivo e visual | Rastreabilidade |
    |---|---|
    | `uxa-051-opportunity-boost-advertiser-mobile-budget.svg`<br>[![uxa-051-opportunity-boost-advertiser-mobile-budget.svg](../assets/wireframes/uxa-051-opportunity-boost-advertiser-mobile-budget.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-051-opportunity-boost-advertiser-mobile-budget.svg) | `GKR-SURF-COM-001`<br>Origem: `UXA-051`<br>Validação: `UXA-052`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-051-opportunity-boost-advertiser-mobile-confirmation.svg`<br>[![uxa-051-opportunity-boost-advertiser-mobile-confirmation.svg](../assets/wireframes/uxa-051-opportunity-boost-advertiser-mobile-confirmation.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-051-opportunity-boost-advertiser-mobile-confirmation.svg) | `GKR-SURF-COM-001`<br>Origem: `UXA-051`<br>Validação: `UXA-052`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-051-opportunity-boost-advertiser-mobile-review.svg`<br>[![uxa-051-opportunity-boost-advertiser-mobile-review.svg](../assets/wireframes/uxa-051-opportunity-boost-advertiser-mobile-review.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-051-opportunity-boost-advertiser-mobile-review.svg) | `GKR-SURF-COM-001`<br>Origem: `UXA-051`<br>Validação: `UXA-052`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-051-opportunity-boost-advertiser-mobile-selection.svg`<br>[![uxa-051-opportunity-boost-advertiser-mobile-selection.svg](../assets/wireframes/uxa-051-opportunity-boost-advertiser-mobile-selection.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-051-opportunity-boost-advertiser-mobile-selection.svg) | `GKR-SURF-COM-001`<br>Origem: `UXA-051`<br>Validação: `UXA-052`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-051-opportunity-boost-advertiser-mobile-targeting.svg`<br>[![uxa-051-opportunity-boost-advertiser-mobile-targeting.svg](../assets/wireframes/uxa-051-opportunity-boost-advertiser-mobile-targeting.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-051-opportunity-boost-advertiser-mobile-targeting.svg) | `GKR-SURF-COM-001`<br>Origem: `UXA-051`<br>Validação: `UXA-052`<br>Canal: móvel<br>Estado: **validado** |

??? abstract "Opportunity Boost — gestão móvel da campanha ativa — 6 SVGs"

    | Arquivo e visual | Rastreabilidade |
    |---|---|
    | `uxa-053-opportunity-boost-active-campaign-mobile-dashboard.svg`<br>[![uxa-053-opportunity-boost-active-campaign-mobile-dashboard.svg](../assets/wireframes/uxa-053-opportunity-boost-active-campaign-mobile-dashboard.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-053-opportunity-boost-active-campaign-mobile-dashboard.svg) | `GKR-SURF-COM-004`<br>Origem: `UXA-053`<br>Validação: `UXA-054`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-053-opportunity-boost-active-campaign-mobile-ended.svg`<br>[![uxa-053-opportunity-boost-active-campaign-mobile-ended.svg](../assets/wireframes/uxa-053-opportunity-boost-active-campaign-mobile-ended.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-053-opportunity-boost-active-campaign-mobile-ended.svg) | `GKR-SURF-COM-004`<br>Origem: `UXA-053`<br>Validação: `UXA-054`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-053-opportunity-boost-active-campaign-mobile-ending.svg`<br>[![uxa-053-opportunity-boost-active-campaign-mobile-ending.svg](../assets/wireframes/uxa-053-opportunity-boost-active-campaign-mobile-ending.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-053-opportunity-boost-active-campaign-mobile-ending.svg) | `GKR-SURF-COM-004`<br>Origem: `UXA-053`<br>Validação: `UXA-054`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-053-opportunity-boost-active-campaign-mobile-paused.svg`<br>[![uxa-053-opportunity-boost-active-campaign-mobile-paused.svg](../assets/wireframes/uxa-053-opportunity-boost-active-campaign-mobile-paused.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-053-opportunity-boost-active-campaign-mobile-paused.svg) | `GKR-SURF-COM-004`<br>Origem: `UXA-053`<br>Validação: `UXA-054`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-053-opportunity-boost-active-campaign-mobile-resumed.svg`<br>[![uxa-053-opportunity-boost-active-campaign-mobile-resumed.svg](../assets/wireframes/uxa-053-opportunity-boost-active-campaign-mobile-resumed.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-053-opportunity-boost-active-campaign-mobile-resumed.svg) | `GKR-SURF-COM-004`<br>Origem: `UXA-053`<br>Validação: `UXA-054`<br>Canal: móvel<br>Estado: **validado** |
    | `uxa-053-opportunity-boost-active-campaign-mobile-settings.svg`<br>[![uxa-053-opportunity-boost-active-campaign-mobile-settings.svg](../assets/wireframes/uxa-053-opportunity-boost-active-campaign-mobile-settings.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-053-opportunity-boost-active-campaign-mobile-settings.svg) | `GKR-SURF-COM-004`<br>Origem: `UXA-053`<br>Validação: `UXA-054`<br>Canal: móvel<br>Estado: **validado** |

??? abstract "Opportunity Boost — estados residuais — 10 SVGs pendentes"

    | Arquivo e visual | Rastreabilidade |
    |---|---|
    | `uxa-055-opportunity-boost-density-limit-mobile.svg`<br>[![uxa-055-opportunity-boost-density-limit-mobile.svg](../assets/wireframes/uxa-055-opportunity-boost-density-limit-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-055-opportunity-boost-density-limit-mobile.svg) | `GKR-SURF-COM-005`<br>Origem: `UXA-055`<br>Validação: **ausente**<br>Canal: móvel<br>Estado: **materializado; validação funcional específica pendente** |
    | `uxa-055-opportunity-boost-hidden-preference-mobile.svg`<br>[![uxa-055-opportunity-boost-hidden-preference-mobile.svg](../assets/wireframes/uxa-055-opportunity-boost-hidden-preference-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-055-opportunity-boost-hidden-preference-mobile.svg) | `GKR-SURF-COM-005`<br>Origem: `UXA-055`<br>Validação: **ausente**<br>Canal: móvel<br>Estado: **materializado; validação funcional específica pendente** |
    | `uxa-055-opportunity-boost-inventory-unavailable-mobile.svg`<br>[![uxa-055-opportunity-boost-inventory-unavailable-mobile.svg](../assets/wireframes/uxa-055-opportunity-boost-inventory-unavailable-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-055-opportunity-boost-inventory-unavailable-mobile.svg) | `GKR-SURF-COM-005`<br>Origem: `UXA-055`<br>Validação: **ausente**<br>Canal: móvel<br>Estado: **materializado; validação funcional específica pendente** |
    | `uxa-055-opportunity-boost-map-density-mobile.svg`<br>[![uxa-055-opportunity-boost-map-density-mobile.svg](../assets/wireframes/uxa-055-opportunity-boost-map-density-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-055-opportunity-boost-map-density-mobile.svg) | `GKR-SURF-COM-005`<br>Origem: `UXA-055`<br>Validação: **ausente**<br>Canal: móvel<br>Estado: **materializado; validação funcional específica pendente** |
    | `uxa-055-opportunity-boost-preference-settings-mobile.svg`<br>[![uxa-055-opportunity-boost-preference-settings-mobile.svg](../assets/wireframes/uxa-055-opportunity-boost-preference-settings-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-055-opportunity-boost-preference-settings-mobile.svg) | `GKR-SURF-COM-005`<br>Origem: `UXA-055`<br>Validação: **ausente**<br>Canal: móvel<br>Estado: **materializado; validação funcional específica pendente** |
    | `uxa-055-opportunity-boost-report-review-mobile.svg`<br>[![uxa-055-opportunity-boost-report-review-mobile.svg](../assets/wireframes/uxa-055-opportunity-boost-report-review-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-055-opportunity-boost-report-review-mobile.svg) | `GKR-SURF-COM-005`<br>Origem: `UXA-055`<br>Validação: **ausente**<br>Canal: móvel<br>Estado: **materializado; validação funcional específica pendente** |
    | `uxa-055-opportunity-boost-report-submitted-mobile.svg`<br>[![uxa-055-opportunity-boost-report-submitted-mobile.svg](../assets/wireframes/uxa-055-opportunity-boost-report-submitted-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-055-opportunity-boost-report-submitted-mobile.svg) | `GKR-SURF-COM-005`<br>Origem: `UXA-055`<br>Validação: **ausente**<br>Canal: móvel<br>Estado: **materializado; validação funcional específica pendente** |
    | `uxa-055-opportunity-boost-reporting-mobile.svg`<br>[![uxa-055-opportunity-boost-reporting-mobile.svg](../assets/wireframes/uxa-055-opportunity-boost-reporting-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-055-opportunity-boost-reporting-mobile.svg) | `GKR-SURF-COM-005`<br>Origem: `UXA-055`<br>Validação: **ausente**<br>Canal: móvel<br>Estado: **materializado; validação funcional específica pendente** |
    | `uxa-055-opportunity-boost-technical-error-mobile.svg`<br>[![uxa-055-opportunity-boost-technical-error-mobile.svg](../assets/wireframes/uxa-055-opportunity-boost-technical-error-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-055-opportunity-boost-technical-error-mobile.svg) | `GKR-SURF-COM-005`<br>Origem: `UXA-055`<br>Validação: **ausente**<br>Canal: móvel<br>Estado: **materializado; validação funcional específica pendente** |
    | `uxa-055-opportunity-boost-user-control-mobile.svg`<br>[![uxa-055-opportunity-boost-user-control-mobile.svg](../assets/wireframes/uxa-055-opportunity-boost-user-control-mobile.svg){ width="280" loading="lazy" }](../assets/wireframes/uxa-055-opportunity-boost-user-control-mobile.svg) | `GKR-SURF-COM-005`<br>Origem: `UXA-055`<br>Validação: **ausente**<br>Canal: móvel<br>Estado: **materializado; validação funcional específica pendente** |

## 6. Auditoria de cobertura

### 6.1 IDs sem SVG dedicado

| ID | Responsabilidade | Estado visual observado |
|---|---|---|
| GKR-SURF-PER-106 | Meus Coletivos | ausente |
| GKR-SURF-PER-107 | Central de Atualizações | ausente |
| GKR-SURF-PER-108 | Início do Participante | reformulação pendente; referência anterior não promovida |
| GKR-SURF-COL-002 | Visão Geral do Responsável | não iniciado |
| GKR-SURF-COL-003 | gestão de solicitações | sem SVG dedicado da origem operacional; apenas efeitos na perspectiva da Pessoa |
| GKR-SURF-COL-004 | participantes e vínculos | sem SVG dedicado |
| GKR-SURF-COL-005 | comunicação oficial | sem SVG dedicado |
| GKR-SURF-COL-006 | atividades, consultas e decisões | sem SVG integrado |
| GKR-SURF-COL-007 | proteção e moderação | sem SVG dedicado |
| GKR-SURF-COL-008 | relações institucionais | sem SVG dedicado |
| GKR-SURF-ORG-004 | proposta de relação com Coletivo | sem SVG dedicado |
| GKR-SURF-ORG-005 | avaliação e negociação bilateral | sem SVG dedicado |
| GKR-SURF-ORG-006 | relação ativa e revisão | sem SVG dedicado |
| GKR-SURF-ORG-007 | resultados e evidências institucionais | sem SVG dedicado |
| GKR-SURF-BND-001 | fronteira externa identificada | intencionalmente sem tela Guivos |

### 6.2 Achados

#### A01 — catálogo desatualizado após UXA-080

O Catálogo Integrado de Telas ainda indicava os registros granulares como `draft`. A UXA-081 sincroniza essa informação com o estado `active` promovido pela UXA-080.

#### A02 — ausência de ponto único de inspeção

Os 97 SVGs estavam distribuídos nos pacotes de origem, sem uma página única para comparação visual e verificação de assertividade.

#### A03 — concentração de múltiplos SVGs em poucos IDs

Os 97 arquivos concentram-se em 25 dos 40 IDs granulares. Variações de dispositivo e estado não devem ser confundidas com cobertura de novas responsabilidades.

#### A04 — dez estados residuais continuam pendentes

Os dez SVGs da UXA-055 são exibidos para inspeção, porém permanecem materializados sem validação funcional específica.

#### A05 — continuidade integrada continua incompleta

A presença lado a lado das telas evidencia que ainda não estão validadas como conjunto:

- a passagem da compreensão inicial para a Tela Hoje;
- a operação bilateral das solicitações de Coletivos;
- a continuidade após aprovação para Meus Coletivos;
- a sequência Meus Coletivos → Central de Atualizações → Início do Participante;
- a relação Organização–Coletivo;
- a publicação institucional até descoberta, lista, mapa e detalhe;
- os efeitos após a fronteira externa;
- a matriz integrada de erros, retornos e interrupções.

## 7. Estado da galeria

A galeria permanece `draft` até revisão funcional e visual específica. Sua inclusão na navegação não aprova assertividade visual, continuidade ou prontidão de produto.

## 8. Próxima transição possível

**UXA-082 — Validação Funcional e Visual da Galeria Integrada e Priorização Governada das Lacunas.**

A UXA-082 não é iniciada por este pacote e dependerá de autorização separada.
