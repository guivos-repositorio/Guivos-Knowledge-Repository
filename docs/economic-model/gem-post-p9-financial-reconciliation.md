---
id: GEM-POST-P9-FINANCIAL-RECONCILIATION-001
title: Reconciliação Econômico-Financeira Pós-P9
status: active
version: 1.0.0
owner: Guivos Economic Model
last_updated: 2026-08-08
parent: GEM-010
depends_on:
  - GEM-010
  - GTM-003
  - GTM-004
  - GTM-006
related:
  - GEM-008-COST-ARCHITECTURE-001
  - GEM-009-COST-AND-UNIT-ECONOMICS-001
  - GEM-010-A1
  - GEM-010-A2
  - GEM-CLOSURE-REVIEW-001
normative: true
---

# Reconciliação Econômico-Financeira Pós-P9

## 1. Finalidade

Reconciliar a baseline quantitativa de Go-to-Market consolidada em 2026-08-08 com a arquitetura do Guivos Economic Model sem promover hipóteses a orçamento, forecast, necessidade de capital, margem, runway ou valuation aprovado.

Este documento é um overlay de reconciliação. Ele não substitui `GTM-003`, `GTM-004`, `GTM-006` nem os contratos do `GEM-010`; define como seus estados devem ser lidos conjuntamente após o P9.

## 2. Parecer executivo

> **PARTIAL PASS — revenue and growth planning inputs are reconciled; full financial calibration remains blocked by missing cost, capacity, working-capital and empirical parameters.**

A auditoria pós-P9 confirmou que:

1. lançamento, crescimento, pagantes e receita possuem baseline candidata M0–M60 no GTM;
2. preços candidatos de Pessoas, Coletivos e Organizações estão rastreados no GEM;
3. Guivos Business possui envelope agregado de receita para planejamento, mas não preço governado por tier;
4. Opportunity Boost possui parâmetros candidatos próprios, porém permanece excluído da projeção de receita até validação;
5. custos, headcount, tributos, taxas de pagamento, CAC, churn observado, margem, capital de giro, caixa e capacidade ainda não possuem parâmetros suficientes para um forecast financeiro completo;
6. o aporte ilustrativo de R$ 2 milhões do `GTM-004` não foi derivado de um cálculo de runway ou necessidade acumulada de capital;
7. a faixa de valuation de R$ 10–15 milhões e as sensibilidades futuras permanecem âncoras negociais/analíticas, não saídas calculadas do modelo financeiro.

## 3. Baseline quantitativa reconciliada

Os valores abaixo podem ser consumidos pelo GEM somente como `candidate_gtm_input`.

| Checkpoint | Pessoas cadastradas | Pessoas pagantes | ARR conhecido de planos | Business ARR-alvo | Run-rate combinado mínimo |
|---|---:|---:|---:|---:|---:|
| M12 | 20.000 | 1.000 | R$ 695.910 | R$ 400.000 | R$ 1.095.910 |
| M24 | 100.000 | 6.000 | R$ 3.661.764 | R$ 1.800.000 | R$ 5.461.764 |
| M36 | 300.000 | 21.000 | R$ 12.109.296 | R$ 6.000.000 | R$ 18.109.296 |
| M48 | 600.000 | 45.000 | R$ 25.445.100 | R$ 14.000.000 | R$ 39.445.100 |
| M60 | 1.000.000 | 80.000 | R$ 44.284.560 | R$ 25.000.000 | R$ 69.284.560 |

A meta gerencial anual base atualmente publicada no `GTM-003` é:

| Ano | Meta gerencial anual base |
|---|---:|
| Ano 1 | R$ 547.955 |
| Ano 2 | R$ 3.278.837 |
| Ano 3 | R$ 11.785.530 |
| Ano 4 | R$ 28.777.198 |
| Ano 5 | R$ 54.364.830 |

Esses números são metas e sensibilidades de planejamento. Não equivalem a receita realizada, budget aprovado, guidance externo ou demonstração contábil.

## 4. Estado dos parâmetros após a reconciliação

| Dimensão | Estado pós-P9 | Leitura autorizada |
|---|---|---|
| Pessoas, Coletivos e Organizações por checkpoint | `candidate_parameterized` | baseline GTM candidata |
| preços de planos governados | `candidate_parameterized` | hipótese aprovada para teste, não disposição a pagar comprovada |
| receita conhecida por preços governados | `candidate_parameterized` | cálculo matemático sobre mix/meta candidata |
| Guivos Business | `partial_parameterization` | quantidade de contratos e envelope agregado; preço/mix por tier pendentes |
| Opportunity Boost | `candidate_parameterized_excluded_from_forecast` | parâmetros candidatos; nenhuma receita incluída no GTM-003 |
| Mall, Travel, Media, Intelligence, Ads além de Boost e outras famílias | `parameter_pending` | excluídas da baseline numérica enquanto não governadas/calibradas |
| custos estruturais e diretos | `parameter_pending` | categorias definidas; valores ausentes |
| headcount e custo por função | `parameter_pending` | não há plano financeiro calibrado |
| infraestrutura, processamento e capacidade | `parameter_pending` | drivers definidos; curva de custo ausente |
| tributos, gateway, chargeback e repasses | `specialist_and_parameter_pending` | não podem ser presumidos |
| CAC e payback | `evidence_pending` | fórmulas definidas; dados ausentes |
| retenção e churn | `evidence_pending` | metas não substituem coortes observadas |
| margem de contribuição | `not_calculable_yet` | depende de custos, tributos, taxas e perdas |
| EBITDA/lucro | `not_calculable_yet` | não inferir a partir de receita |
| capital de giro | `not_calculable_yet` | prazos de recebimento/pagamento e obrigações pendentes |
| runway | `not_calculable_yet` | caixa livre inicial e burn por cenário ausentes |
| necessidade acumulada de capital | `not_calculable_yet` | não existe valor calculado vigente |
| valuation pré-receita | `candidate_negotiation_anchor` | R$ 10–15 mi; referência central R$ 12 mi |
| aporte de R$ 2 mi | `illustrative_financing_scenario` | não é necessidade de capital demonstrada |

## 5. Regra de consumo GTM → GEM

```text
meta GTM candidata
→ driver financeiro candidato
→ custos e capacidade rastreáveis
→ reconhecimento e recebimento
→ margem e caixa
→ cenário reconciliado
→ stress e sensibilidade
→ necessidade de capital
→ decisão humana
```

Nenhuma etapa poderá ser pulada para transformar receita-meta diretamente em lucro, caixa, runway, funding ou valuation.

## 6. Cenários: correção de interpretação

Os multiplicadores de `70% / 100% / 130%` do `GTM-003` são **sensibilidades de faturamento**. Eles não constituem, isoladamente, os cenários financeiros completos do `GEM-010`.

Um cenário financeiro completo deverá variar de forma coerente, quando houver parâmetros:

- aquisição, ativação, conversão, retenção e churn;
- mix de planos e contratos;
- descontos, inadimplência, cancelamentos e reembolsos;
- custos variáveis e custos em degrau;
- headcount e capacidade;
- CAC e canais;
- tributos e pagamentos;
- prazos de recebimento e pagamento;
- reservas e recursos restritos;
- investimentos e desembolsos não recorrentes;
- expansão territorial;
- eventos de estresse.

O cenário conservador não será obtido apenas reduzindo receita; custos, capacidade e caixa podem reagir de forma não linear.

## 7. Capital, caixa e runway

O `GTM-004` utiliza R$ 2 milhões como cenário ilustrativo de rodada e distribuição de recursos. Pós-P9, a interpretação obrigatória é:

```text
R$ 2 milhões ilustrativos
≠ necessidade de capital calculada
≠ runway aprovado
≠ orçamento autorizado
≠ captação aprovada
```

Para que uma necessidade de capital seja calculável, deverão existir pelo menos:

1. saldo inicial de caixa livre e recursos restritos;
2. curva mensal de receita e recebimento;
3. OPEX e custos variáveis mensais;
4. headcount e contratações por gate;
5. CAPEX/desembolsos não recorrentes quando aplicáveis;
6. tributos, taxas, repasses, inadimplência e reembolsos;
7. capital de giro e prazos médios;
8. reservas e cobertura mínima;
9. cenário de estresse;
10. horizonte de runway e margem de segurança aprovados.

Até isso ocorrer, qualquer valor de rodada é apenas hipótese de estruturação financeira.

## 8. Valuation: limite pós-P9

A faixa pré-receita de R$ 10–15 milhões permanece preservada como `candidate_negotiation_anchor`, com referência central de R$ 12 milhões.

As sensibilidades futuras baseadas no run-rate M60 também permanecem somente matemáticas. Múltiplo de receita não substitui avaliação de:

- crescimento e qualidade da receita;
- margem bruta e contribuição;
- retenção e churn;
- concentração;
- previsibilidade comercial;
- eficiência de capital;
- CAC e payback;
- risco regulatório e operacional;
- capacidade de internacionalização;
- condições de mercado e termos da rodada.

Valuation futuro não deverá ser promovido a meta corporativa apenas porque o run-rate candidato foi atingido.

## 9. Internacionalização

Portugal/Lisboa permanece uma expansão condicionada a gates. O GTM possui janela territorial, mas o GEM ainda não possui orçamento calibrado para internacionalização.

Antes de incluir Portugal em forecast financeiro aprovado deverão existir, no mínimo:

- custos jurídicos, fiscais e contábeis aplicáveis;
- pagamentos e moeda;
- suporte e operação local/remota;
- aquisição e desenvolvimento de oferta local;
- infraestrutura e dados;
- viagens, fornecedores e serviços especializados quando aplicáveis;
- contingência e capacidade de absorção de falhas;
- tratamento de receitas e despesas por moeda e território.

Nenhum segundo país é financeiramente autorizado por esta reconciliação.

## 10. Opportunity Boost e novas receitas

`GEM-010-A2` permanece válido como baseline candidata de preço, orçamento e mensuração do Opportunity Boost.

Enquanto não houver validação e autorização específica:

- nenhuma receita de Boost entra no run-rate do `GTM-003`;
- orçamento de campanha não é integralmente receita líquida;
- CPM/CPC candidato não prova demanda, margem ou capacidade;
- créditos promocionais ou patrocinados não são receita automática;
- custos de entrega, antifraude, moderação, suporte, pagamentos e tributos permanecem visíveis.

A mesma regra vale para famílias ainda não precificadas/calibradas do ecossistema.

## 11. Gates para transformar a baseline em modelo financeiro aprovado

### F1 — baseline de custos

Definir valores rastreáveis para custos estruturais, diretos, aquisição, qualidade, risco e coordenação, com comportamento fixo/variável/degrau.

### F2 — capacidade e plano operacional

Vincular volume a infraestrutura, processamento, suporte, vendas, Customer Success, moderação, segurança e headcount por gate.

### F3 — caixa e capital de giro

Modelar recebimentos, pagamentos, tributos, taxas, repasses, reservas, recursos restritos e desembolsos não recorrentes em granularidade mensal.

### F4 — unit economics

Calcular margem de contribuição, custo de servir, CAC, payback e LTV somente após evidência suficiente, por segmento/coorte/canal.

### F5 — cenários completos

Construir conservador, base, expansivo e estresse com drivers coerentes de receita, custo, capacidade e caixa, em vez de apenas multiplicadores de faturamento.

### F6 — capital e valuation

Somente após F1–F5 calcular necessidade de capital, runway, margem de segurança e estrutura de rodada; reavaliar valuation com evidência operacional e mercado.

## 12. Prioridade de preenchimento

A próxima evolução financeira deve priorizar **curto prazo e lançamento**, não preencher cinco anos com falsa precisão.

Ordem recomendada:

```text
M0–M6 detalhado mensalmente
→ M7–M12 detalhado mensalmente
→ M13–M24 por trimestre com gates
→ M25–M60 por horizonte e sensibilidade
```

A granularidade futura deverá aumentar somente quando a evidência justificar.

## 13. Não conformidades e classificação

| ID | Achado | Classe | Tratamento |
|---|---|---|---|
| FIN-P9-01 | GTM quantitativo atualizado após arquitetura GEM-010 original | Major documental | reconciliado por este overlay e atualização do GEM-010 |
| FIN-P9-02 | R$ 2 mi pode ser confundido com necessidade de capital calculada | Major semântico | guardrail explícito no GTM-004 e GEM cash/funding |
| FIN-P9-03 | 70/100/130 pode ser confundido com cenário financeiro completo | Major semântico | separado de cenários GEM completos |
| FIN-P9-04 | custos, margem, runway e capital permanecem sem parâmetros | Observation material | permanece bloqueante para forecast aprovado; não inventar valores |
| FIN-P9-05 | Opportunity Boost possui preço candidato sem receita na baseline | Conforme | manter exclusão até evidência e autorização |
| FIN-P9-06 | Business possui envelope sem preço por tier | Conforme com pendência | preservar como envelope agregado e criar autoridade própria antes de precificação externa |

Não permanecem conflitos que autorizem tratar valores ausentes como zero ou assumir capital necessário a partir do aporte ilustrativo.

## 14. Estado formal

```text
Audit target: post-P9 financial coherence
Revenue/growth baseline reconciliation: PASS
Cost calibration: PENDING
Capacity calibration: PENDING
Unit economics calibration: PENDING
Cash/runway calculation: PENDING
Capital requirement calculation: PENDING
Valuation appraisal: NOT PERFORMED
Approved budget/forecast: NO
Operational authorization: NO
```

A arquitetura está apta a receber parâmetros futuros sem perder rastreabilidade. O próximo avanço quantitativo depende de evidência, estimativas documentadas ou decisões competentes; ausência de dado continuará explícita como pendência, nunca preenchida por suposição silenciosa.
