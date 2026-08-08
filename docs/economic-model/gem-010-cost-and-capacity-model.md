---
id: GEM-010-COST-AND-CAPACITY-MODEL-001
title: Modelo de Custos e Capacidade
status: draft
version: 0.5.0
owner: Guivos Economic Model
last_updated: 2026-08-08
parent: GEM-010
depends_on:
  - GEM-008-COST-ARCHITECTURE-001
  - GEM-POST-P9-FINANCIAL-RECONCILIATION-001
related:
  - GEM-F1-M0-M6-COST-BASELINE-001
  - GEM-F1B-M0-M6-COST-CALIBRATION-001
  - GEM-F2-M0-M6-CAPACITY-HEADCOUNT-BASELINE-001
  - GEM-F2B-M0-M6-PEOPLE-DELIVERY-COST-001
  - GEM-F2C-M0-M6-ASSIGNMENT-DEDICATION-001
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

Capacidade funcional, role-equivalent, headcount, assignment, dedicação, contratação e custo são dimensões distintas. Uma obrigação de cobertura não comprova vínculo, gasto ou disponibilidade operacional.

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

A aplicação governada deste modelo possui cinco camadas complementares:

1. [Baseline de Custos M0–M6 — F1](gem-f1-m0-m6-cost-baseline.md): pools, drivers, ativação e evidência;
2. [Calibração Numérica M0–M6 — F1-B](gem-f1b-m0-m6-cost-calibration.md): benchmarks públicos rastreáveis sem promoção a orçamento;
3. [Baseline de Capacidade, Papéis e Headcount M0–M6 — F2](gem-f2-m0-m6-capacity-and-headcount-baseline.md): cobertura funcional, role-equivalents e gates de capacidade;
4. [Modelo de Entrega e Custo de Pessoas M0–M6 — F2-B](gem-f2b-m0-m6-people-delivery-and-cost-model.md): modos de entrega, benchmarks de remuneração e regras para converter capacidade em custo somente após regime, dedicação e evidência;
5. [Matriz de Assignment e Dedicação M0–M6 — F2-C](gem-f2c-m0-m6-assignment-and-dedication-model.md): owner scopes, sobreposições, bandas candidatas de dedicação e guardrails contra dupla contagem de capacidade.

F2 estabelece como piso funcional de referência os três role-equivalents dedicados explicitamente suportados pelo GTM — Growth/GTM, comercial institucional/B2B e ecossistema/parcerias — além de coberturas compartilhadas, especialistas fracionários e capacidades condicionais.

Esse piso **não equivale a três empregados** e não define HC total, vínculo ou custo.

## Relação F2/F2-B/F2-C → F1-C05

O pool `F1-C05 — equipe e serviços profissionais` está **parcialmente parametrizado em capacidade, benchmarks e assignment**, mas permanece sem amount mensal completo.

F2-B define:

- modos de entrega admissíveis para founder/internal, CLT, shared internal, contractor/PJ, especialista fracionário e partner-enabled;
- benchmark 2026 para Growth/GTM em Belo Horizonte;
- benchmark comercial B2B nacional;
- proxy explicitamente limitado para ecossistema/parcerias;
- benchmark auxiliar de CRM/CX para eventual reforço dedicado de suporte/CS;
- componentes trabalhistas oficiais mínimos que não constituem, isoladamente, custo CLT completo;
- regras de rateio e prevenção de dupla contagem.

F2-C define:

- owner scopes para as 18 capacidades;
- owner primário de R01, R02 e R03;
- regra contra contabilizar a mesma capacidade física como dois RE dedicados integrais;
- piso central candidato de 65% por RE dedicado;
- teto candidato de carga planejada de 85%, preservando 15% de folga;
- teto suave candidato de 20% para uma capacidade secundária isolada;
- envelope de até 0.60 RE-equivalent de carga secundária agregada dentro dos três RE, sem convertê-lo em headcount.

Ainda são necessários para converter F1-C05 em custo completo:

- resource assignment real/candidato por período;
- delivery mode escolhido por assignment;
- fração mensal exata dentro das bandas ou exceção documentada;
- quantidade efetiva de pessoas/prestadores;
- remuneração, fee ou cotação;
- encargos, benefícios, variável e impostos aplicáveis;
- competência mensal.

Benchmark salarial não é orçamento, salário aprovado ou custo total do empregador. Banda de dedicação não é folha, headcount ou disponibilidade comprovada. Até que essas lacunas sejam resolvidas, não existe burn completo de pessoas.

## Gates de capacidade

A passagem para lançamento não poderá ocorrer apenas pelo calendário. Coberturas essenciais deverão possuir owner identificável e capacidade suficiente para não operar em estado `constrained`, `saturated`, `degraded` ou `unavailable`.

F2-C acrescenta um gate preventivo de planejamento: soma de alocações acima de 0.85 para o mesmo recurso consome a folga e exige revisão; soma acima de 1.00 é overallocated e invalida o plano. Esses valores são candidatos de planejamento, não thresholds operacionais comprovados.

Sinais como backlog crescente, tempo de resposta degradado, ausência de owner, falhas de moderação, sobrecarga de segurança ou concentração crítica deverão acionar revisão de capacidade antes de aumento de volume.

## Limites desta versão

Esta versão não aprova:

- valores completos de custo;
- orçamento;
- HC interno total;
- assignment nominal de pessoas;
- salários, propostas de remuneração ou regimes de contratação;
- pró-labore, comissão, bônus ou benefícios;
- fornecedor, vendor, tier ou região tecnológica;
- Product Engineering;
- rateios definitivos;
- burn;
- runway;
- necessidade de capital;
- contratação ou implementação.
