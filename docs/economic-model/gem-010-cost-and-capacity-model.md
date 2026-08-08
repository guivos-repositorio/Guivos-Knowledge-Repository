---
id: GEM-010-COST-AND-CAPACITY-MODEL-001
title: Modelo de Custos e Capacidade
status: draft
version: 0.2.0
owner: Guivos Economic Model
last_updated: 2026-08-08
parent: GEM-010
depends_on:
  - GEM-008-COST-ARCHITECTURE-001
  - GEM-POST-P9-FINANCIAL-RECONCILIATION-001
related:
  - GEM-F1-M0-M6-COST-BASELINE-001
  - GEM-009-COST-AND-UNIT-ECONOMICS-001
---

# Modelo de Custos e Capacidade

## Classificações

- fixo, variável, semivariável ou em degrau;
- direto, compartilhado ou corporativo;
- recorrente ou não recorrente;
- caixa ou não caixa;
- comprometido, discricionário, protegido ou contingente.

## Relação com capacidade

Custos em degrau deverão explicitar o gatilho de capacidade. Ganhos de escala não serão presumidos quando suporte, risco, qualidade ou infraestrutura crescem de forma diferente do volume.

## Rateio

Custos compartilhados exigem driver causal ou justificativa gerencial, versão e reconciliação. Rateio não altera o custo total consolidado nem transfere ownership funcional.

## Estados de evidência de valor

A calibração financeira deverá distinguir, no mínimo:

- `TBD` — linha identificada sem valor sustentado;
- `benchmark` — estimativa externa documentada e comparável;
- `quoted` — cotação identificável ainda não contratada;
- `contracted` — obrigação contratual vigente;
- `actual` — valor observado e reconciliado;
- `not_applicable` — item comprovadamente não aplicável ao perímetro.

`TBD` não equivale a zero. Valor zero exige evidência explícita de ausência de custo, obrigação ou desembolso aplicável.

## Baseline M0–M6

A primeira aplicação governada deste modelo é a [Baseline de Custos M0–M6 — F1](gem-f1-m0-m6-cost-baseline.md).

Ela estabelece:

- granularidade mensal de M0 a M6;
- separação entre preparação M0–M3 e lançamento M4–M6 em Belo Horizonte;
- pools de custo derivados da arquitetura GEM vigente;
- comportamento, drivers e estados de ativação;
- contrato de evidência para posterior preenchimento numérico;
- dependência explícita do F2 para dimensionamento de headcount e custo de equipe.

A ativação de uma linha não autoriza gasto nem comprova valor. Enquanto linhas materiais permanecerem `TBD`, burn, runway e necessidade de capital não poderão ser apresentados como completos.

## Limites desta versão

Esta versão não aprova:

- valores de custo;
- orçamento;
- headcount;
- salários ou regimes de contratação;
- fornecedor, vendor, tier ou região tecnológica;
- rateios definitivos;
- burn;
- runway;
- necessidade de capital;
- contratação ou implementação.
