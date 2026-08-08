---
id: GEM-F1B-M0-M6-COST-CALIBRATION-001
title: Calibração Numérica M0–M6 — F1-B
status: active
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-08-08
parent: GEM-F1-M0-M6-COST-BASELINE-001
depends_on:
  - GEM-F1-M0-M6-COST-BASELINE-001
  - GEM-010-COST-AND-CAPACITY-MODEL-001
  - GEM-POST-P9-FINANCIAL-RECONCILIATION-001
related:
  - GEM-009-COST-AND-UNIT-ECONOMICS-001
  - GTM-001
  - GTM-003
  - GTM-006
normative: true
---

# Calibração Numérica M0–M6 — F1-B

## 1. Finalidade

Executar a primeira calibração numérica da baseline de custos `M0–M6` usando somente evidência rastreável disponível em 2026-08-08.

F1-B diferencia explicitamente:

- **taxa unitária benchmark** — preço público observável ou tarifa oficial utilizável como referência;
- **quantidade do driver** — número de usuários, licenças, classes, transações, dias, assentos ou eventos;
- **amount_brl mensal** — valor mensal calculado após quantidade e aplicabilidade estarem governadas.

Uma taxa unitária benchmark **não transforma o respectivo pool em custo contratado, realizado ou orçamento aprovado**.

Quando a quantidade do driver, o fornecedor, o plano, o escopo ou o gate de ativação não estiverem definidos, `amount_brl` permanece `TBD`.

## 2. Método e critérios de aceitação

Foram aceitos somente:

1. preços públicos do próprio fornecedor;
2. tarifas governamentais oficiais;
3. páginas com preço e unidade identificáveis;
4. informações recuperadas em 2026-08-08;
5. valores compatíveis com Brasil/Belo Horizonte ou diretamente aplicáveis em BRL.

Não foram usados:

- médias genéricas sem fonte primária;
- estimativas criadas pelo GKR;
- fóruns, agregadores ou posts sem autoridade comercial;
- valores de tecnologia cuja contratação depende de Product Engineering;
- salários ou headcount antes do F2;
- valores promocionais como se fossem preço permanente;
- preço de um fornecedor como decisão de fornecedor.

## 3. Estados adicionais de calibração

| Estado F1-B | Significado |
|---|---|
| `unit_benchmark_available` | existe taxa unitária pública rastreável, mas não há quantidade/decisão suficiente para `amount_brl` |
| `formula_benchmark_available` | existe fórmula/tarifa variável pública, mas volume/mix ainda é `TBD` |
| `official_fee_available` | existe tarifa oficial governamental por evento/unidade |
| `quote_required` | escopo material existe, mas preço público não é suficiente; requer cotação |
| `blocked_by_F2` | custo depende de dimensionamento de equipe/headcount |
| `blocked_by_engineering` | custo depende de decisão técnica/implementação ainda não autorizada |
| `TBD` | não há evidência numérica suficiente nesta versão |

## 4. Ledger de fontes primárias

| Fonte | Tipo | Evidência pública observada | Recuperado em | Uso permitido |
|---|---|---|---|---|
| Contabilizei — preços de serviços contábeis | fornecedor | plano Básico a partir de R$ 139/mês; Padrão R$ 195/mês; preço varia por faturamento/complexidade | 2026-08-08 | benchmark de contabilidade; não seleção de fornecedor |
| Google Workspace — preços Brasil | fornecedor | Business Starter em BRL; referência pública observada de R$ 39,20/usuário/mês no compromisso anual e R$ 49/usuário/mês na modalidade flexível; promoções podem alterar a cobrança inicial | 2026-08-08 | benchmark de produtividade administrativa; quantidade de usuários permanece TBD |
| RD Station CRM — preços Brasil | fornecedor | Free R$ 0 com limite de 4 usuários; Basic R$ 73/usuário/mês no plano anual; implementação personalizada opcional R$ 849 | 2026-08-08 | benchmark de CRM; plano e usuários não aprovados |
| Stripe Brasil — preços padrão | fornecedor | cartões nacionais 3,99% + R$ 0,39 por transação; Pix 1,19%; boleto pago R$ 3,45; contestação recebida R$ 55 | 2026-08-08 | benchmark de meios de pagamento e disputas; mix/volume permanece TBD |
| Stripe Billing — preços Brasil | fornecedor | Billing 0,7% do volume processado pelo Billing | 2026-08-08 | benchmark de cobrança recorrente; arquitetura de cobrança não aprovada |
| INPI — Tabela de Retribuições | governo | pedido de marca por classe: código 389, R$ 880 / R$ 440 com desconto; código 394, R$ 1.720 / R$ 860 com desconto, vigentes desde 20/09/2025 | 2026-08-08 | tarifa oficial por classe; elegibilidade a desconto e número de classes permanecem TBD |
| WeWork — Belo Horizonte | fornecedor | passe diário a partir de R$ 214; associação de coworking a partir de R$ 1.003/mês em referência de compromisso anual; escritório privativo para 3 pessoas a partir de R$ 2.690/mês, sujeito a impostos/taxas e condições comerciais | 2026-08-08 | benchmark local de espaço; nenhuma contratação ou necessidade física presumida |

### URLs de origem

- Contabilizei: `https://www.contabilizei.com.br/contabilidade-online/servicos-de-contabilidade-precos/`
- Google Workspace: `https://workspace.google.com/intl/pt-BR/`
- RD Station CRM: `https://www.rdstation.com/planos/crm/`
- Stripe Payments: `https://stripe.com/br/pricing`
- Stripe Billing: `https://stripe.com/br/billing/pricing`
- INPI: `https://www.gov.br/inpi/pt-br/inpi-data/precificacao-dos-servicos/tabela-de-retribuicoes-inpi_portaria-mdic-no110_2025-e-portaria-inpi-no-10_2025.pdf`
- WeWork BH coworking: `https://www.wework.com/pt-BR/l/coworking-space/belo-horizonte`
- WeWork BH office: `https://www.wework.com/pt-BR/l/office-space/belo-horizonte`

## 5. Benchmarks por pool

### F1-C06 — jurídico, contábil, fiscal, administrativo e compliance

#### F1B-C06-ACC — contabilidade recorrente

```yaml
pool: F1-C06
subcost: contabilidade_recorrente
unit_rate_brl: 139..195
unit: empresa_mes
value_state: benchmark
calibration_state: unit_benchmark_available
source: Contabilizei
amount_brl: TBD
confidence_source: high
confidence_applicability: low
```

Interpretação:

- R$ 139/mês é preço inicial público do plano Básico;
- R$ 195/mês é referência pública do plano Padrão;
- o próprio fornecedor informa que preço e adequação variam conforme faturamento, regime, atividade e complexidade;
- jurídico especializado, fiscal específico, DPO/Encarregado, pareceres e compliance continuam `TBD`/`quote_required`.

#### F1B-C06-WORKSPACE — produtividade administrativa

```yaml
pool: F1-C06
subcost: produtividade_colaboracao
unit_rate_brl: 39.20..49.00
unit: usuario_mes
value_state: benchmark
calibration_state: unit_benchmark_available
source: Google Workspace Business Starter Brasil
amount_brl: TBD
confidence_source: high
confidence_applicability: medium
```

A faixa representa modalidades públicas observadas e não incorpora promoções temporárias. O número de usuários e a decisão de ferramenta permanecem `TBD`.

### F1-C08 — CRM, vendas e Customer Success

```yaml
pool: F1-C08
subcost: crm_vendas
unit_rate_brl:
  free: 0
  basic_annual: 73
unit: usuario_mes
optional_implementation_brl: 849
value_state: benchmark
calibration_state: unit_benchmark_available
source: RD Station CRM
amount_brl: TBD
confidence_source: high
confidence_applicability: medium
```

Regras:

- o valor R$ 0 é permitido aqui porque o fornecedor declara explicitamente plano Free sem cobrança, limitado a 4 usuários;
- F1-B não presume que o Free seja suficiente para a Guivos;
- o Basic é referência por usuário; quantidade depende da estrutura comercial e, indiretamente, do F2;
- implementação é opcional e não entra em nenhum mês sem decisão explícita.

### F1-C13 — meios de pagamento e cobrança

```yaml
pool: F1-C13
subcost: pagamentos_e_cobranca
benchmark_formula:
  card_national: "3.99% * volume_cartao + R$0.39 * transacoes_cartao"
  pix: "1.19% * volume_pix"
  boleto: "R$3.45 * boletos_pagos"
  billing_if_adopted: "0.70% * volume_billing"
value_state: benchmark
calibration_state: formula_benchmark_available
source: Stripe Brasil
amount_brl: TBD
confidence_source: high
confidence_applicability: low
```

A Guivos não está vinculada à Stripe por esta baseline. As tarifas servem apenas para demonstrar uma ordem de grandeza unitária rastreável. O mix de pagamento, volume, recorrência, impostos e arquitetura de cobrança continuam pendentes.

### F1-C14 — reembolsos, chargebacks, disputas e perdas operacionais

```yaml
pool: F1-C14
subcost: contestacao_cartao
unit_rate_brl: 55
unit: contestacao_recebida
value_state: benchmark
calibration_state: formula_benchmark_available
source: Stripe Brasil
amount_brl: TBD
confidence_source: high
confidence_applicability: low
```

O benchmark não permite projetar quantidade de disputas. A incidência permanece `TBD`; perdas, fraude e reembolsos não podem ser inferidos a partir desta tarifa.

### F1-C16 — domínios, marca, propriedade intelectual e ativos institucionais

```yaml
pool: F1-C16
subcost: pedido_registro_marca_inpi
unit_rate_brl:
  code_389_general: 880
  code_389_discounted: 440
  code_394_general: 1720
  code_394_discounted: 860
unit: classe_por_pedido
value_state: benchmark
official_fee: true
calibration_state: official_fee_available
source: INPI
amount_brl: TBD
confidence_source: high
confidence_applicability: medium
```

Regras:

- código 389 corresponde à especificação pré-aprovada;
- código 394 corresponde ao livre preenchimento;
- o desconto depende do enquadramento jurídico elegível;
- quantidade de classes, pedidos e eventos M0–M6 precisa vir da estratégia de propriedade intelectual, não desta calibração;
- honorários de procurador/escritório permanecem `TBD`.

### F1-C17 — espaço físico, coworking, equipamentos e infraestrutura administrativa

```yaml
pool: F1-C17
subcost: espaco_fisico_bh
unit_rate_brl:
  day_pass: 214
  coworking_membership_reference: 1003
  private_office_3p_reference: 2690
unit:
  day_pass: pessoa_dia
  coworking_membership_reference: pessoa_mes
  private_office_3p_reference: escritorio_mes
value_state: benchmark
calibration_state: unit_benchmark_available
source: WeWork Belo Horizonte
amount_brl: TBD
confidence_source: high
confidence_applicability: low
```

Os preços de espaço físico permanecem apenas como benchmark local. A fonte informa condições promocionais/contratuais e, para escritórios, incidência possível de impostos e taxas. Nenhuma estrutura física foi autorizada ou presumida.

## 6. Matriz de calibração dos 18 pools

| Pool | Estado numérico após F1-B | Motivo |
|---|---|---|
| F1-C01 produto/desenvolvimento/QA | `blocked_by_engineering` | escopo implementável e execução continuam sem reativação de Product Engineering |
| F1-C02 infraestrutura/hospedagem | `blocked_by_engineering` | vendor, arquitetura executável, regiões e carga não aprovados |
| F1-C03 IA/processamento/dados | `blocked_by_engineering` | consumo e tecnologia operacional não aprovados |
| F1-C04 segurança/privacidade | `quote_required` | controles são obrigatórios, mas escopo operacional e fornecedores não estão definidos |
| F1-C05 equipe/serviços profissionais | `blocked_by_F2` | headcount, funções, salários e regime pertencem ao F2 |
| F1-C06 jurídico/contábil/fiscal/admin | `unit_benchmark_available` parcial | contabilidade e produtividade têm benchmark; jurídico/compliance material continua TBD |
| F1-C07 marca/conteúdo/criativo | `quote_required` | produção e calendário não especificados para cotação |
| F1-C08 CRM/vendas/CS | `unit_benchmark_available` parcial | CRM possui preço público; usuários/tier/CS continuam TBD |
| F1-C09 prospecção/deslocamentos BH | `TBD` | quantidade e política de deslocamento não definidas |
| F1-C10 onboarding/ecossistema | `TBD` | desenho operacional e esforço por entidade não evidenciados |
| F1-C11 mídia paga/performance | `TBD` | orçamento é decisão de aquisição, não preço de mercado automático |
| F1-C12 lançamento/eventos/campo BH | `quote_required` | formato, capacidade, local e produção não definidos |
| F1-C13 pagamentos/cobrança | `formula_benchmark_available` | tarifas públicas existem; volume/mix/arquitetura não |
| F1-C14 reembolsos/disputas/perdas | `formula_benchmark_available` parcial | tarifa de disputa existe; incidência e perdas permanecem TBD |
| F1-C15 suporte/moderação/curadoria/fraude | `TBD` | modelo de serviço e carga não definidos |
| F1-C16 domínios/marca/IP | `official_fee_available` parcial | INPI calibrado; domínios e honorários continuam TBD |
| F1-C17 espaço/equipamentos físicos | `unit_benchmark_available` | benchmark BH existe; necessidade e configuração continuam TBD |
| F1-C18 integrações/coordenação/reconciliação | `TBD` | integrações executadas ainda não definidas |

## 7. Cobertura obtida

Dos 18 pools F1:

- 6 possuem ao menos uma taxa/fórmula numérica externa utilizável (`F1-C06`, `F1-C08`, `F1-C13`, `F1-C14`, `F1-C16`, `F1-C17`);
- 12 permanecem sem calibração numérica suficiente no nível de pool completo;
- nenhum dos 18 pode ser declarado completamente fechado para burn M0–M6 nesta versão;
- a existência de 6 pools parcialmente calibrados **não autoriza somar um “custo mínimo da Guivos”**, pois isso excluiria custos materiais ainda `TBD`.

## 8. O que F1-B não pode calcular

Permanecem não calculáveis:

- custo mensal completo M0, M1, M2, M3, M4, M5 ou M6;
- burn mensal;
- burn acumulado M0–M6;
- capital de giro;
- runway;
- necessidade de capital;
- rodada necessária;
- break-even;
- margem operacional;
- CAC real;
- payback;
- valuation derivado de execução financeira.

## 9. Lacunas que exigem evidência própria

### Antes de fechar F1 numericamente

1. decisão sobre quais custos tecnológicos serão efetivamente ativados;
2. cotações de jurídico, privacidade/compliance e segurança quando aplicáveis;
3. escopo de conteúdo, lançamento, mídia e eventos;
4. política de deslocamento e reuniões em BH;
5. desenho de onboarding e suporte;
6. decisão sobre presença física;
7. decisão sobre stack administrativo/CRM/pagamentos;
8. número de classes e ações de PI no horizonte M0–M6;
9. F2 para headcount e custo de equipe.

## 10. Parecer F1-B

| Gate | Resultado |
|---|---|
| fontes primárias rastreáveis | PASS |
| benchmarks em BRL/Brasil | PASS |
| separação taxa unitária × quantidade × amount_brl | PASS |
| fornecedores tratados como benchmark, não decisão | PASS |
| 6/18 pools com calibração parcial | PASS |
| 18/18 pools numericamente fechados | FAIL — evidence missing |
| custo mensal M0–M6 completo | NOT CALCULABLE |
| burn/runway/capital | NOT CALCULABLE |

**Parecer:** `PARTIAL PASS — traceable public unit benchmarks established for six cost pools; complete M0–M6 numeric baseline remains blocked by material TBDs, F2 and engineering/operational decisions.`

## 11. Próximo ato governado

F1-B não autoriza o F2 automaticamente.

Com esta calibração, existem duas rotas válidas e separadas:

1. **F1-C — evidência/cotações faltantes**, caso se deseje aprofundar custos externos antes de dimensionar equipe;
2. **F2 — capacidade e headcount**, caso haja autorização humana para dimensionar papéis, quantidade, regime e custo de pessoas necessários a M0–M6.

Burn e runway somente devem ser produzidos depois que ambos os blocos materiais estiverem suficientemente resolvidos.
