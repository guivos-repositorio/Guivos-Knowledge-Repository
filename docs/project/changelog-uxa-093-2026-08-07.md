---
id: GKR-CHANGELOG-UXA-093-001
title: Changelog — UXA-093 — Central de Atualizações
status: active
version: 0.1.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-07
depends_on:
  - GKR-STATE-001
related:
  - UXA-093
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.80
normative: false
---

# Changelog — UXA-093

## 1. Incremento

A UXA-093 materializa `GKR-SURF-PER-107 — Central de Atualizações` como referência móvel P0A da Pessoa em Coletivos.

## 2. Ativo visual

Foi criado exatamente um novo SVG:

- `docs/assets/wireframes/uxa-093-collective-updates-center-mobile.svg`.

Nenhum SVG previamente existente foi reformulado.

## 3. Semântica materializada

A Central passa a representar triagem de mudanças com:

- origem;
- natureza;
- contexto;
- autoridade;
- estado de leitura;
- necessidade de ação;
- prazo legítimo quando houver.

A ordenação não deve ser dominada por engajamento, popularidade, volume de reações, compra de plano, publicidade ou interesse comercial não declarado. Estado `lido` não equivale a concordância, consentimento, presença ou ação concluída.

## 4. Maturidade

- `PER-107`: `ausente` → `materializado`;
- `TRN-110`: permanece `parcial`, agora com ambos os endpoints materializados;
- `TRN-111`: permanece `ausente` por `PER-108` não vigente;
- `PER-108`: reformulação pendente;
- `PER-105` e `PER-106`: sem alteração visual e com validações vigentes preservadas.

## 5. Cobertura proposta

| Indicador | Resultado |
|---|---:|
| SVGs | 107 |
| associações individuais | 107 |
| perfis de rastreabilidade | 27 |
| validações funcionais vigentes | 96 |
| pendentes de validação específica | 11 |
| IDs com referência visual | 29 de 40 |
| responsabilidades sem SVG dedicado | 10 |
| superfícies | 40 |
| transições | 37 |

Os 11 pendentes são os dez estados residuais da UXA-055 e o novo SVG de `PER-107`.

## 6. Limites

A UXA-093 não valida `PER-107` ou `TRN-110`, não materializa `PER-108`, estados P0B ou áreas P1, não cria novos IDs, não promove jornadas e não inicia protótipo, testes ou Engenharia de Produto.

## 7. Baseline proposta

- `GKR-STATE-001`: 2.19.0;
- marco: M7.80;
- `ROADMAP`: 12.66.0;
- `UXA-000`: 0.86.0.

## 8. Próxima frente

**UXA-094 — Validação Funcional da Central de Atualizações e Revalidação de `GKR-TRN-110`**.

A UXA-094 não foi iniciada.
