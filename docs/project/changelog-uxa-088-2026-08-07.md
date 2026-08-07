---
id: GKR-CHANGELOG-UXA-088-001
title: Registro da UXA-088 — Materialização da Gestão de Solicitações do Responsável
status: active
version: 1.0.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-07
depends_on:
  - GKR-STATE-001
related:
  - UXA-088
  - GKR-SURF-COL-003
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - M7.75
normative: false
---

# Registro da UXA-088 — Materialização da Gestão de Solicitações do Responsável

## 1. Baseline

A UXA-088 foi preparada sobre a `main` no commit `8d9885ad2dfddd57164ebfb56ad0dd2b9eca6693`, após o fechamento operacional da UXA-087.

Este registro descreve o pacote proposto. O estado somente se torna vigente na `main` após decisão governada de integração.

## 2. Escopo executado na branch

Foi materializada exclusivamente `GKR-SURF-COL-003 — gestão de solicitações` em sete SVGs desktop:

1. fila operacional;
2. detalhe comum;
3. análise protegida;
4. pedido de informação adicional;
5. confirmação de aprovação;
6. confirmação de recusa;
7. autoridade insuficiente.

Nenhum novo ID granular ou transição foi criado.

## 3. Mudança de cobertura proposta

| Indicador | Antes | Após UXA-088 |
|---|---:|---:|
| SVGs | 98 | 105 |
| associações individuais | 98 | 105 |
| perfis de rastreabilidade | 24 | 25 |
| validações funcionais registradas | 88 | 88 |
| pendentes de validação específica | 10 | 17 |
| IDs com referência visual | 26 de 40 | 27 de 40 |
| responsabilidades sem SVG dedicado | 13 | 12 |
| superfícies registradas | 40 | 40 |
| transições registradas | 37 | 37 |

Os 17 pendentes propostos correspondem aos dez estados da UXA-055 e aos sete novos estados da UXA-088.

## 4. Efeito sobre transições

A UXA-088 adiciona evidência do lado responsável a `GKR-TRN-105` a `GKR-TRN-109` e materializa o destino de `GKR-TRN-112`.

Essas transições permanecem `parcial` porque:

- os sete novos estados ainda não foram funcionalmente validados;
- os handoffs bilaterais ainda não foram examinados ponta a ponta;
- `GKR-SURF-PER-106` continua ausente após aprovação.

## 5. Baseline documental proposta

- GKR-STATE-001: **2.14.0**;
- marco: **M7.75**;
- ROADMAP: **12.61.0**;
- UXA-000: **0.81.0**;
- Jornadas Integradas: **0.16.0**;
- Galeria Visual: **0.8.0**;
- página de Coletivos: **0.6.0**;
- Matriz por SVG: **0.6.0**;
- Catálogo: **0.13.0**;
- Lacunas: **0.13.0**;
- Registro de Superfícies: **0.6.0**;
- Registro de Transições: **0.5.0**;
- detalhamento do Coletivo: **0.5.0**.

## 6. Limites preservados

A UXA-088 não:

- valida funcionalmente os sete novos SVGs;
- valida `TRN-105` a `TRN-109` ou `TRN-112` ponta a ponta;
- materializa `PER-106`, `PER-107` ou `PER-108`;
- materializa `COL-004` a `COL-008`;
- promove a Jornada do Coletivo;
- altera Resultados Empresariais;
- inicia protótipo, teste com pessoas ou Engenharia de Produto;
- inicia UXA-089.

## 7. Próximo ato possível

Após eventual integração e autorização separada:

> **UXA-089 — Validação Funcional da Gestão de Solicitações do Responsável do Coletivo.**

A UXA-089 não é iniciada por este registro.
