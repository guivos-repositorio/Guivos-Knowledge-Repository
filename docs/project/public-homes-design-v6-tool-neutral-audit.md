---
id: GKR-UX-HOMES-DESIGN-V6-AUDIT-001
title: Homes Públicas — Auditoria de Remediação Tool-Neutral para Design v6
status: active
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-09-19
normative: false
maturity: candidate_audit_pre_validation
depends_on:
  - GKR-UX-HOMES-DESIGN-CONSUMPTION-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
related:
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-HOME-OC-MASTER-001
  - GKR-UX-HOME-MALL-MASTER-001
  - GKR-UX-HOME-TRAVEL-MASTER-001
  - GKR-UX-HOME-MEDIA-MASTER-001
  - GKR-UX-HOME-ADS-MASTER-001
  - GKR-UX-HOME-BUSINESS-MASTER-001
  - GKR-UX-HOME-INTELLIGENCE-MASTER-001
---

# Homes Públicas — Auditoria de Remediação Tool-Neutral para Design v6

## 1. Objetivo

Registrar a remediação que remove o fluxo governado de materialização Figma/IA e restabelece o modelo aprovado:

```text
GKR
→ FONTE DE VERDADE DOCUMENTAL

DESIGNER
→ AUTORIA CRIATIVA E MATERIALIZAÇÃO VISUAL EXTERNA

IA
→ APOIO OPCIONAL

FIGMA
→ FERRAMENTA EXTERNA DA DESIGNER
→ NÃO GOVERNADA / NÃO EDITADA PELO GKR
```

## 2. Escopo auditado

Autoridades comuns:

- `GKR-UX-HOMES-DESIGN-CONSUMPTION-001`;
- `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001`;
- `GKR-UX-HOMES-DESIGN-HANDOFF-001`;
- `GKR-UX-HOMES-GENINPUT-001`;
- `GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001`;
- `GKR-UX-HOMES-DESIGN-DELIVERY-001`;
- `GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001`.

Masters:

1. Pessoa;
2. Organizações e Coletivos;
3. Mall;
4. Travel;
5. Media;
6. Ads;
7. Business;
8. Intelligence.

## 3. Findings remediados

### R-01 — Figma Make como gate obrigatório

Removido. IA passa a ser opcional.

### R-02 — GKR governando Figma definitivo

Removido. O artefato visual é externo ao GKR.

### R-03 — identidade visual pré-canônica

Confirmado como **não requerida**. Identidade, tipografia, paleta, imagens, composição, grid, motion, componentes, atmosfera e linguagem visual permanecem Design-owned.

### R-04 — Business com direção visual obrigatória

Remediado. Dashboard, KPIs, gráficos e demais recursos passam a exemplos admissíveis, não requisitos.

### R-05 — Travel com prescrição de força visual

Remediado. Importância passa a ser narrativa; intensidade e solução visual são da designer.

### R-06 — Media com prescrição de escala/densidade/tipografia

Remediado. O Master preserva hierarquia editorial e significado, deixando a forma visual para Design.

### R-07 — Ads com estética “visualmente tecnológica”

Remediado. Não há estética tecnológica obrigatória.

### R-08 — Business Source Lock marcado como futuro

Remediado. `GKR-UX-HOME-BUSINESS-SOURCELOCK-001 v1.0.0` é reconhecido como vigente.

### R-09 — Intelligence Home Source Lock marcado como inexistente

Remediado. `GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001 v1.0.0` e Handoff específico v1.0.0 são reconhecidos como vigentes.

### R-10 — Pessoa/O-C com estados de auditoria/materialização superados

Remediado para separar Design da Home pública de gates próprios da experiência autenticada.

## 4. Revisão 8/8

```text
PESSOA
→ REVIEWED / TOOL-NEUTRAL

ORGANIZAÇÕES E COLETIVOS
→ REVIEWED / TOOL-NEUTRAL

MALL
→ REVIEWED / TOOL-NEUTRAL

TRAVEL
→ REVIEWED / TOOL-NEUTRAL

MEDIA
→ REVIEWED / TOOL-NEUTRAL

ADS
→ REVIEWED / TOOL-NEUTRAL

BUSINESS
→ REVIEWED / TOOL-NEUTRAL

INTELLIGENCE
→ REVIEWED / TOOL-NEUTRAL
```

## 5. Boundary

Esta auditoria não materializa o pacote v6 e não declara validação final antes dos gates automáticos e independentes.

```text
CANONICAL REMEDIATION
→ CANDIDATE

SEMANTIC / MECHANICAL
→ PENDING

INDEPENDENT REVIEW
→ PENDING

MERGE
→ NOT AUTHORIZED

V6 SNAPSHOT
→ NOT EMITTED

FIGMA WRITE
→ OUT OF PROCESS
```

## 6. Critério de fechamento

A frente só pode ser fechada depois de:

1. Semantic = SUCCESS;
2. Mechanical = SUCCESS;
3. revisão independente sem finding material aberto;
4. zero threads materiais abertos;
5. merge humano autorizado;
6. geração pós-merge dos oito `00-LEIA-PRIMEIRO`;
7. materialização e validação do snapshot v6.
