---
id: GKR-CHANGELOG-UXA-086-001
title: Changelog — UXA-086 Materialização da Visão Geral do Responsável
status: active
version: 1.0.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-07
depends_on:
  - UXA-086
  - GKR-STATE-001
related:
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
  - ROADMAP-12.59.0
  - M7.73
normative: false
---

# Changelog — UXA-086 Materialização da Visão Geral do Responsável

## 1. Baseline

Base do incremento:

```text
main
6b3e93f1ee6b7ab052e784bc5f4d6557182cc6e0
```

A baseline corresponde à UXA-085 integrada.

## 2. Mudança arquitetural

A UXA-086 materializa exclusivamente `GKR-SURF-COL-002 — Visão Geral do Responsável` por meio de:

- documento de autoridade da UXA-086;
- um wireframe desktop de baixa fidelidade;
- contexto explícito de papel e autoridade;
- síntese de momento operacional;
- atenção principal justificada;
- sínteses de solicitações e vínculos, comunicação, proteção, governança e relações;
- ponto de entrada documental para a futura gestão completa de solicitações.

## 3. Efeito quantitativo

| Indicador | Antes | Após UXA-086 |
|---|---:|---:|
| SVGs | 97 | 98 |
| associações individuais | 97 | 98 |
| perfis de rastreabilidade | 23 | 24 |
| validações funcionais registradas | 87 | 87 |
| pendentes de validação específica | 10 | 11 |
| IDs granulares com referência visual | 25 | 26 |
| responsabilidades sem SVG dedicado | 14 | 13 |
| superfícies registradas | 40 | 40 |
| transições registradas | 37 | 37 |

## 4. Reclassificação observacional

`GKR-TRN-112` passa de `ausente` para `parcial` porque:

- sua origem `GKR-SURF-COL-002` agora possui materialização;
- seu destino `GKR-SURF-COL-003` continua sem superfície operacional própria;
- a transição não foi funcionalmente validada.

Nenhuma nova transição é criada.

## 5. Estado sincronizado proposto

- `GKR-STATE-001` → 2.12.0;
- `ROADMAP` → 12.59.0;
- marco → M7.73;
- `UXA-000` → 0.79.0;
- Jornadas Integradas → 0.14.0;
- Galeria Visual Integrada → 0.6.0;
- página de Coletivos → 0.4.0;
- Matriz por SVG → 0.4.0;
- Catálogo Integrado → 0.11.0;
- Lacunas → 0.11.0;
- Registro de Superfícies → 0.4.0;
- Registro de Transições → 0.4.0;
- detalhamento do Coletivo → 0.3.0;
- Jornada Integrada do Coletivo → `draft` 0.4.0.

## 6. Preservações

A UXA-086 não:

- valida funcionalmente a nova referência;
- materializa `GKR-SURF-COL-003`;
- valida `GKR-TRN-112`;
- fecha automaticamente a lacuna de `GKR-SURF-COL-002`;
- materializa Meus Coletivos, Central de Atualizações ou Início do Participante;
- altera os dez estados residuais da UXA-055;
- promove a jornada do Coletivo;
- cria protótipo ou teste com pessoas;
- inicia Engenharia de Produto;
- altera Resultados Empresariais.

## 7. Próximo ato possível

**UXA-087 — Validação Funcional da Visão Geral do Responsável do Coletivo**, mediante autorização separada.

Este changelog registra o incremento; não autoriza a UXA-087 nem qualquer materialização posterior.
