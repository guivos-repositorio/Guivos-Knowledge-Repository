---
id: GKR-CHANGELOG-UXA-089-001
title: Registro da UXA-089 — Validação da Gestão de Solicitações do Responsável
status: active
version: 1.0.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-07
depends_on:
  - GKR-STATE-001
related:
  - UXA-089
  - GKR-SURF-COL-003
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - M7.76
normative: false
---

# Registro da UXA-089 — Validação da Gestão de Solicitações do Responsável

## 1. Baseline

A UXA-089 foi preparada sobre a `main` no commit `654c044ed998e3e434de88d8c492c91f49887421`, após o fechamento operacional da UXA-088.

Este registro descreve o pacote proposto. O estado somente se torna vigente na `main` após decisão governada de integração.

## 2. Escopo executado na branch

Foi validada funcionalmente `GKR-SURF-COL-003 — gestão de solicitações` em seus sete estados desktop.

Seis SVGs existentes foram reformulados e um foi aprovado sem alteração. Nenhum novo SVG, ID granular ou transição foi criado.

## 3. Reformulações aplicadas

1. distinção entre estimativa e prazo de resposta na fila;
2. critérios de decisão vinculados a condições previamente apresentadas à Pessoa;
3. retirada de acessibilidade da elegibilidade, preservando-a como acomodação;
4. autoridade de aprovação verificada por escopo, não por checkbox;
5. autoridade de recusa verificada por escopo, com fundamento previamente apresentado;
6. autoridade insuficiente permite consultar o escopo concedido, sem sugerir autoalteração de permissão.

## 4. Mudança de cobertura proposta

| Indicador | Antes | Após UXA-089 |
|---|---:|---:|
| SVGs | 105 | 105 |
| associações individuais | 105 | 105 |
| perfis de rastreabilidade | 25 | 25 |
| validações funcionais registradas | 88 | 95 |
| pendentes de validação específica | 17 | 10 |
| IDs com referência visual | 27 de 40 | 27 de 40 |
| responsabilidades sem SVG dedicado | 12 | 12 |
| superfícies registradas | 40 | 40 |
| transições registradas | 37 | 37 |

Os dez pendentes remanescentes correspondem exclusivamente aos estados residuais da UXA-055.

## 5. Efeito sobre transições

`GKR-TRN-105`, `106`, `107`, `109` e `112` passam a possuir endpoints validados como superfícies, mas permanecem `parcial` porque ainda não foram examinadas ponta a ponta.

`GKR-TRN-108` permanece `parcial` adicionalmente porque `GKR-SURF-PER-106` continua ausente.

## 6. Baseline documental proposta

- GKR-STATE-001: **2.15.0**;
- marco: **M7.76**;
- ROADMAP: **12.62.0**;
- UXA-000: **0.82.0**;
- Jornadas Integradas: **0.17.0**;
- Galeria Visual: **0.9.0**;
- página de Coletivos: **0.7.0**;
- Matriz por SVG: **0.7.0**;
- Catálogo: **0.14.0**;
- Lacunas: **0.14.0**;
- Registro de Superfícies: **0.7.0**;
- Registro de Transições: **0.6.0**;
- detalhamento do Coletivo: **0.6.0**.

## 7. Limites preservados

A UXA-089 não:

- valida os handoffs bilaterais como conjunto;
- materializa `PER-106`, `PER-107` ou `PER-108`;
- materializa `COL-004` a `COL-008`;
- promove a Jornada do Coletivo;
- altera Resultados Empresariais;
- inicia protótipo, teste com pessoas ou Engenharia de Produto;
- inicia UXA-090.

## 8. Próximo ato possível

Após eventual integração e autorização separada:

> **UXA-090 — Validação Integrada dos Handoffs Bilaterais de Solicitação em Coletivos.**

A UXA-090 não é iniciada por este registro.
