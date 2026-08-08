---
id: GEM-F3S-M0-M6-CASH-WORKING-CAPITAL-STRUCTURE-001
title: Estrutura de Caixa e Capital de Giro M0–M6 — F3-S
status: active
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-08-08
parent: GEM-010
depends_on:
  - GEM-F1F2-F3-READINESS-RECONCILIATION-001
  - GEM-F1-M0-M6-COST-BASELINE-001
  - GEM-F1C-M0-M6-EVIDENCE-QUOTE-PACK-001
  - GEM-F2-M0-M6-CAPACITY-HEADCOUNT-BASELINE-001
  - GEM-F2B-M0-M6-PEOPLE-DELIVERY-COST-001
  - GEM-F2C-M0-M6-ASSIGNMENT-DEDICATION-001
  - GEM-010-CASH-WORKING-CAPITAL-AND-FUNDING-001
  - GEM-010-OPERATING-DRIVER-MODEL-001
  - GTM-003
  - GTM-006
related:
  - GEM-POST-P9-FINANCIAL-RECONCILIATION-001
  - GEM-010-COST-AND-CAPACITY-MODEL-001
  - GTM-004
normative: true
---

# Estrutura de Caixa e Capital de Giro M0–M6 — F3-S

## 1. Finalidade

Estabelecer a camada **estrutural** do F3 para o horizonte `M0–M6`, governando eventos de caixa, calendário, estados, buckets, pontes de competência e liquidação, contas a receber/pagar e regras de reconciliação sem preencher valores monetários ainda não sustentados.

F3-S executa exclusivamente o `F3_structural_readiness = PASS — conditional` definido em `GEM-F1F2-F3-READINESS-RECONCILIATION-001`.

F3-S **não altera** o estado:

```text
F3_monetary_readiness = FAIL
```

Consequentemente, esta autoridade **não calcula** burn, consumo líquido de caixa, capital de giro necessário, runway, necessidade de capital, rodada necessária, break-even ou suficiência de qualquer aporte.

## 2. Princípio central

```text
competência ≠ faturamento ≠ contas a receber ≠ recebimento ≠ caixa livre
obrigação ≠ contas a pagar ≠ pagamento
recebimento ≠ receita econômica
pagamento ≠ custo reconhecido
saldo bancário ≠ caixa livre
reserva protegida ≠ caixa disponível
pass-through ≠ receita própria
TBD ≠ zero
```

A estrutura existe para tornar essas diferenças auditáveis antes de existir um forecast financeiro completo.

## 3. Perímetro

### 3.1 Temporal

| Período | Estado de referência |
|---|---|
| M0–M3 | preparação controlada de Belo Horizonte |
| M4–M6 | lançamento inicial de Belo Horizonte |

A publicação desta estrutura não define uma data-calendário para `M0`.

### 3.2 Territorial

F3-S cobre somente o perímetro econômico `M0–M6` já governado em F1/F2.

Ficam fora:

- São Paulo após M6;
- Portugal/Lisboa;
- expansão nacional posterior;
- qualquer segundo país;
- custos ou recebimentos cuja operação territorial ainda não esteja autorizada.

## 4. Estado de maturidade

| Camada | Estado após F3-S |
|---|---|
| contrato de evento de caixa | PASS |
| calendário estrutural M0–M6 | PASS |
| buckets de caixa | PASS |
| estados de evidência | PASS |
| ponte receita→recebimento | PASS estrutural |
| ponte custo→pagamento | PASS estrutural |
| contas a receber/pagar | PASS estrutural |
| regras de reconciliação | PASS |
| saldo inicial em reais | TBD |
| amounts mensais completos | NOT CALCULABLE |
| capital de giro em reais | NOT CALCULABLE |
| burn | NOT CALCULABLE |
| runway | NOT CALCULABLE |
| necessidade de capital | NOT CALCULABLE |

## 5. Contrato canônico de evento de caixa

Todo evento estrutural elegível deverá poder ser expresso pelo contrato abaixo.

```yaml
cash_event_id: string
period: M0 | M1 | M2 | M3 | M4 | M5 | M6
event_type: inflow | outflow | transfer | reserve | release | reversal
source_authority: string
economic_family: string
economic_object: string
participant_or_counterparty_scope: string_or_TBD
product_scope: Journey | Mall | Travel | Business | Media | Intelligence | Ads | corporate | multi_product | TBD
territory: BH | Brazil_preparation | TBD
recognition_state: candidate | benchmark | quoted | contracted | actual | not_applicable
activation_state: required | conditional | inactive_by_baseline | not_applicable
accrual_period: M0..M6_or_TBD
billing_date: date_or_TBD
due_date: date_or_TBD
expected_cash_date: date_or_TBD
actual_cash_date: date_or_TBD
amount_brl: number_or_TBD
gross_net_state: gross | net | not_applicable | TBD
cash_bucket: free_cash | restricted_cash | protected_reserve | pass_through | TBD_classification
payment_or_receipt_method: string_or_TBD
terms: string_or_TBD
tax_state: defined | partial | TBD | not_applicable
fee_state: defined | partial | TBD | not_applicable
repass_state: defined | partial | TBD | not_applicable
reversal_state: none | possible | actual | TBD
reconciliation_key: string
source_document: string_or_TBD
owner_scope: string_or_TBD
notes: string
```

### 5.1 Regras obrigatórias

1. `amount_brl: TBD` deverá permanecer visível quando o valor não for sustentado;
2. nenhuma data futura será inventada para completar o calendário;
3. `expected_cash_date` não equivale a recebimento realizado;
4. `contracted` exige obrigação/documento identificável;
5. `actual` exige evidência de liquidação ou competência reconciliada conforme o objeto;
6. valores de terceiros deverão preservar `pass_through` quando aplicável;
7. recursos restritos ou reservas não serão classificados como `free_cash` por conveniência;
8. um mesmo evento econômico não poderá gerar dois eventos de caixa próprios sem relação explícita de split, taxa, repasse ou reversão.

## 6. Identidade e chaves de reconciliação

O `cash_event_id` deverá ser único.

A `reconciliation_key` deverá permitir conectar, conforme aplicável:

```text
driver
→ evento econômico
→ documento/origem
→ competência
→ cobrança/obrigação
→ recebível/pagável
→ liquidação
→ taxa/tributo/repasse
→ bucket de caixa
→ reversão ou encerramento
```

Uma chave de reconciliação não substitui documento-fonte.

Quando um único evento bruto gerar componentes econômicos distintos, cada componente deverá ser identificável, por exemplo:

```text
recebimento bruto
├─ receita própria potencial
├─ taxa de pagamento
├─ tributo
├─ repasse/pass-through
└─ valor líquido elegível para classificação de caixa
```

## 7. Buckets de caixa

### 7.1 `free_cash`

Recurso monetário sem restrição identificada que, após reconciliação de obrigações, taxas, tributos, repasses e reservas aplicáveis, pode ser elegível para uso operacional.

`free_cash` não significa automaticamente excedente distribuível ou orçamento disponível.

### 7.2 `restricted_cash`

Recurso recebido com destinação, condição, contrato, programa ou restrição identificável.

Exemplos conceituais incluem recursos vinculados a uma entrega, campanha, subsídio ou obrigação específica, quando juridicamente/economicamente aplicável.

### 7.3 `protected_reserve`

Valor separado por regra de governança para proteção, contingência, obrigação futura, risco ou continuidade.

F3-S cria o bucket, mas **não define percentual ou valor mínimo de reserva**.

### 7.4 `pass_through`

Valor recebido ou movimentado pela Guivos que economicamente pertence a terceiro ou deverá ser repassado conforme relação governada.

`pass_through` não integra receita própria nem caixa livre.

### 7.5 `TBD_classification`

Estado transitório obrigatório quando a natureza econômica do saldo ainda não estiver sustentada.

Não poderá ser promovido silenciosamente a `free_cash`.

## 8. Estados de evidência

F3-S reutiliza e especializa os estados econômicos vigentes.

| Estado | Uso em F3-S |
|---|---|
| `candidate` | evento/fluxo admissível, ainda sem obrigação executável |
| `benchmark` | taxa ou referência externa documentada; não é obrigação |
| `quoted` | proposta identificável; ainda não contratada |
| `contracted` | obrigação ou direito contratual documentado |
| `actual` | fato realizado/reconciliado |
| `not_applicable` | comprovadamente não aplicável ao período/objeto |

Nenhum estado autoriza converter informação faltante em zero.

## 9. Ponte estrutural de entradas

A cadeia mínima para entradas é:

```text
driver elegível
→ evento econômico admissível
→ estado de reconhecimento
→ competência/faturamento quando aplicável
→ conta a receber quando aplicável
→ recebimento esperado
→ recebimento realizado
→ taxas/tributos/repasses
→ classificação em bucket
→ reconciliação
```

### 9.1 Famílias admitidas sem antecipar execução

F3-S pode reservar estrutura para fontes já reconhecidas conceitualmente no GEM/GTM, entre elas:

- assinaturas de Pessoa;
- assinaturas de Coletivo;
- assinaturas de Organização;
- contratos agregados de Guivos Business;
- demais famílias de receita somente quando possuírem autoridade vigente compatível.

Regras:

- preço candidato não cria recebível;
- meta de pagantes não cria faturamento;
- envelope de Guivos Business não cria contrato individual;
- Opportunity Boost permanece fora da baseline de receita até validação e autorização específica;
- qualquer nova família deverá preservar owner, base de cobrança e evento econômico governados.

## 10. Ponte estrutural de saídas

A cadeia mínima para saídas é:

```text
pool/driver de custo
→ necessidade/obrigação potencial
→ estado de evidência
→ competência
→ conta a pagar quando aplicável
→ pagamento esperado
→ pagamento realizado
→ classificação de caixa
→ reconciliação
```

Os 18 pools F1 poderão originar eventos estruturais, mas somente quando o estado de ativação e a evidência permitirem.

F3-S não promove nenhum dos 18 pools a custo mensal fechado.

## 11. Contas a receber — estado estrutural

Todo recebível deverá poder percorrer estados explícitos:

```text
not_created
→ candidate_receivable
→ billed_or_documented
→ open
→ partially_received | received
→ reversed | cancelled | disputed | written_off
→ reconciled
```

Regras:

- `candidate_receivable` não compõe caixa;
- `billed_or_documented` não significa recebido;
- recebimento parcial deverá preservar saldo aberto;
- cancelamento, reembolso ou disputa deverá ser conectável ao evento original;
- baixa/perda futura exige política/evidência própria, não podendo ser presumida em F3-S.

## 12. Contas a pagar — estado estrutural

Toda obrigação poderá percorrer:

```text
not_created
→ candidate_obligation
→ quoted
→ contracted_or_incurred
→ open
→ partially_paid | paid
→ reversed | cancelled | disputed
→ reconciled
```

Regras:

- benchmark não cria conta a pagar;
- quote não cria obrigação;
- contrato poderá criar obrigação futura conforme termos;
- pagamento parcial deverá preservar saldo;
- competência e caixa deverão permanecer distinguíveis.

## 13. Calendário estrutural M0–M6

F3-S não cria calendário de valores. Cria um calendário de **camadas mínimas a serem reconciliadas**.

| Camada mensal | M0 | M1 | M2 | M3 | M4 | M5 | M6 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| saldo inicial por bucket | TBD | roll-forward | roll-forward | roll-forward | roll-forward | roll-forward | roll-forward |
| eventos de entrada elegíveis | registrar | registrar | registrar | registrar | registrar | registrar | registrar |
| eventos de saída elegíveis | registrar | registrar | registrar | registrar | registrar | registrar | registrar |
| contas a receber | reconciliar | reconciliar | reconciliar | reconciliar | reconciliar | reconciliar | reconciliar |
| contas a pagar | reconciliar | reconciliar | reconciliar | reconciliar | reconciliar | reconciliar | reconciliar |
| taxas/tributos/repasses | TBD/registrar | TBD/registrar | TBD/registrar | TBD/registrar | TBD/registrar | TBD/registrar | TBD/registrar |
| reservas/restrições | TBD/registrar | TBD/registrar | TBD/registrar | TBD/registrar | TBD/registrar | TBD/registrar | TBD/registrar |
| reversões/disputas | registrar se ocorrer | registrar se ocorrer | registrar se ocorrer | registrar se ocorrer | registrar se ocorrer | registrar se ocorrer | registrar se ocorrer |
| fechamento estrutural | requerido | requerido | requerido | requerido | requerido | requerido | requerido |

`roll-forward` significa transportar saldos reconciliáveis conforme evidência. Não implica que o saldo inicial de M0 seja conhecido.

## 14. Fechamento mensal estrutural

Cada mês deverá responder, no mínimo:

1. quais eventos de caixa foram criados;
2. qual sua autoridade de origem;
3. quais permanecem `TBD` e por quê;
4. quais recebíveis e obrigações foram abertos;
5. quais liquidações ocorreram;
6. quais taxas, tributos ou repasses foram separados;
7. quais valores permanecem restritos, reservados ou pass-through;
8. quais reversões, disputas ou cancelamentos existem;
9. quais eventos não reconciliam com documento/origem;
10. quais saldos podem ou não ser transportados ao mês seguinte.

Resultado do mês:

- `structurally_reconciled`;
- `structurally_reconciled_with_TBDs`;
- `reconciliation_exception`;
- `reconciliation_blocked`.

Nenhum desses estados significa fechamento contábil, fiscal ou financeiro aprovado.

## 15. Exceções de reconciliação

Deverão permanecer visíveis, entre outras:

- recebimento sem evento econômico identificável;
- pagamento sem obrigação/pool identificável;
- divergência entre bruto e líquido sem taxa/tributo/repasse explicado;
- valor classificado como livre sem evidência suficiente;
- duplicidade de evento;
- recebível vencido sem estado atualizado;
- pagamento fora do período esperado;
- reversão sem vínculo com o evento original;
- recurso de terceiro misturado a receita própria;
- bucket `TBD_classification` não resolvido em fechamento material.

## 16. Relação com F1

F1/F1-B/F1-C governam o **que pode gerar custo e em qual estado de evidência**.

F3-S governa **quando e como esse objeto pode virar obrigação e movimento de caixa**.

Logo:

```text
benchmark F1
≠ obrigação F3
≠ conta a pagar
≠ pagamento
```

Pools com `blocked_by_engineering`, `scope_definition_required` ou `budget_decision_and_experiment_required` poderão existir no schema, mas não receberão amount ou obrigação fictícia.

## 17. Relação com F2

F2/F2-B/F2-C governam capacidade, owner scopes, delivery modes, benchmarks e dedication planning.

F3-S não converte role-equivalent em desembolso.

Para originar um evento monetário de pessoas ainda serão necessários, conforme aplicável:

- assignment identificável;
- delivery mode efetivo;
- período/fração;
- remuneração, fee ou cotação sustentada;
- tributos/benefícios/componentes aplicáveis;
- obrigação e termos de pagamento.

Enquanto isso, a estrutura registra o driver e mantém o amount como `TBD`.

## 18. Tributos, taxas e repasses

F3-S cria campos e eventos separados para tributos, taxas e repasses.

Regras:

1. taxa de pagamento não poderá ser escondida dentro de receita líquida sem trilha;
2. tributo não poderá ser presumido sem regime/base aplicável;
3. repasse a terceiro deverá preservar `pass_through` quando economicamente devido;
4. Stripe, Sympla ou qualquer benchmark não é fornecedor escolhido;
5. uma mesma transação não poderá receber duas taxas de processamento sobre o mesmo fato sem justificativa;
6. valores líquidos só poderão ser derivados quando bruto e deduções estiverem sustentados.

## 19. Reservas e recursos restritos

F3-S não define política quantitativa de reserva.

A estrutura exige apenas que qualquer futura reserva possua:

```yaml
reserve_id: string
purpose: string
rule_authority: string
activation_state: candidate | approved | actual
minimum_or_formula: TBD_or_defined
funding_source: string_or_TBD
release_condition: string_or_TBD
amount_brl: TBD_or_number
cash_bucket: protected_reserve
```

Sem regra de reserva governada, nenhum percentual arbitrário será aplicado ao caixa.

## 20. Saldo inicial M0

O saldo inicial de `M0` permanece `TBD` até evidência adequada.

O futuro registro deverá separar:

- free cash inicial;
- restricted cash inicial;
- reservas protegidas existentes;
- pass-through pendente;
- obrigações já incorridas antes de M0, se aplicáveis;
- recebíveis anteriores, se aplicáveis.

Nenhum aporte ilustrativo do GTM poderá ser tratado como saldo inicial real.

## 21. Capital de giro — tratamento estrutural

F3-S governa a existência do **gap temporal** entre competência, recebimento e pagamento.

Capital de giro monetário continua não calculável.

A estrutura deverá permitir posteriormente responder:

```text
quando o direito econômico nasce?
quando é faturado?
quando é recebido?
quando a obrigação nasce?
quando vence?
quando é paga?
qual parcela do saldo é livre, restrita, reservada ou de terceiro?
```

Somente após amounts, prazos e materialidade suficientemente sustentados essas relações poderão gerar necessidade de capital de giro em reais.

## 22. Gate de promoção para F3 monetário

`F3_monetary_readiness` não poderá passar para `PASS` apenas porque o schema está completo.

A promoção exige, por período material:

1. saldo inicial reconciliável por bucket;
2. recebimentos com amount e timing sustentados;
3. pagamentos materiais com amount e timing sustentados;
4. people cost monetariamente parametrizado;
5. tributos aplicáveis definidos;
6. taxas/repasses reconciliáveis;
7. perdas/reversões com premissa ou evidência adequada;
8. reservas/restrições governadas;
9. desembolsos não recorrentes materiais identificados;
10. ausência de `TBD` material que torne o fechamento enganoso.

A avaliação será por materialidade, não por percentual simples de linhas preenchidas.

## 23. Outputs proibidos nesta camada

F3-S não poderá publicar como resultado válido:

- “burn da Guivos”;
- “caixa necessário para M0–M6”;
- “capital de giro necessário”;
- “runway de X meses”;
- “rodada necessária de R$ X”;
- “R$ 2 milhões são suficientes/insuficientes”;
- “caixa mínimo recomendado”;
- forecast aprovado;
- orçamento aprovado;
- break-even monetário;
- valuation recalculado por caixa.

## 24. Resultado F3-S

| Gate | Resultado |
|---|---|
| contrato canônico de evento de caixa | PASS |
| buckets de caixa | PASS |
| ponte entradas | PASS estrutural |
| ponte saídas | PASS estrutural |
| AR state machine | PASS |
| AP state machine | PASS |
| calendário M0–M6 | PASS estrutural |
| fechamento/reconciliação mensal | PASS estrutural |
| tratamento de taxas/tributos/repasses | PASS estrutural / amounts TBD |
| reservas/restrições | PASS estrutural / política quantitativa TBD |
| saldo inicial M0 | TBD |
| amounts mensais completos | FAIL / NOT CALCULABLE |
| capital de giro monetário | NOT CALCULABLE |
| burn | NOT CALCULABLE |
| runway | NOT CALCULABLE |
| necessidade de capital | NOT CALCULABLE |

**Parecer:** `PASS — F3-S establishes the M0–M6 cash and working-capital schema, event lifecycle, buckets, monthly structural calendar and reconciliation rules while preserving all unsupported monetary inputs as TBD. F3 monetary readiness remains FAIL and no burn, runway, working-capital amount or capital requirement is calculated.`

## 25. Próximo incremento econômico permitido

Após eventual integração de F3-S, o próximo passo econômico **não deverá ser promovido automaticamente para cálculo de runway**.

Antes de qualquer F3 monetário, deverá existir uma revisão de preenchimento dos inputs materiais de caixa, incluindo pelo menos:

- saldo inicial;
- timing e amount de recebimentos elegíveis;
- timing e amount de pagamentos materiais;
- people cost;
- tributos;
- taxas/repasses;
- reservas/restrições;
- perdas/reversões;
- desembolsos não recorrentes.

A próxima frente poderá ser uma **F3-M readiness/input closure**, se autorizada separadamente. F4, F5 e F6 permanecem não autorizados por F3-S.
