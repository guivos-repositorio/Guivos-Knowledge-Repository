---
id: GEM-F1F2-F3-READINESS-RECONCILIATION-001
title: Reconciliação de Prontidão F1/F2 para F3
status: active
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-08-08
parent: GEM-010
depends_on:
  - GEM-POST-P9-FINANCIAL-RECONCILIATION-001
  - GEM-F1-M0-M6-COST-BASELINE-001
  - GEM-F1B-M0-M6-COST-CALIBRATION-001
  - GEM-F1C-M0-M6-EVIDENCE-QUOTE-PACK-001
  - GEM-F2-M0-M6-CAPACITY-HEADCOUNT-BASELINE-001
  - GEM-F2B-M0-M6-PEOPLE-DELIVERY-COST-001
  - GEM-F2C-M0-M6-ASSIGNMENT-DEDICATION-001
  - GEM-010-CASH-WORKING-CAPITAL-AND-FUNDING-001
  - GTM-003
  - GTM-006
related:
  - GEM-010-COST-AND-CAPACITY-MODEL-001
  - GEM-010-OPERATING-DRIVER-MODEL-001
  - GTM-004
normative: true
---

# Reconciliação de Prontidão F1/F2 para F3

## 1. Finalidade

Determinar, após a integração de F1, F1-B, F1-C, F2, F2-B e F2-C, se o Guivos Economic Model possui evidência suficiente para iniciar o **F3 — caixa e capital de giro** e, em caso positivo, qual parte de F3 pode ser governada sem produzir falsa precisão financeira.

Esta autoridade separa explicitamente:

```text
prontidão estrutural de F3
≠ prontidão monetária de F3
≠ burn calculável
≠ runway calculável
≠ necessidade de capital calculável
```

A reconciliação **não executa F3**, não cria valores mensais, não escolhe fornecedores, não contrata pessoas, não reativa Product Engineering e não autoriza captação.

## 2. Base reconciliada

### 2.1 F1/F1-B/F1-C

O bloco de custos possui 18 pools governados para M0–M6.

Após F1-C:

- 12/18 pools possuem ao menos uma taxa, fórmula ou benchmark numérico rastreável;
- 6/18 pools continuam sem calibração numérica útil;
- 0/18 pools estão completamente fechados para todos os meses M0–M6;
- nenhum subtotal parcial pode ser promovido a “custo mínimo da Guivos”.

Pools ainda sem calibração útil:

- F1-C01 — produto/desenvolvimento/QA;
- F1-C02 — infraestrutura/hospedagem;
- F1-C03 — IA/processamento/dados;
- F1-C10 — onboarding/ecossistema;
- F1-C11 — mídia paga/performance;
- F1-C18 — integrações/reconciliação.

### 2.2 F2/F2-B/F2-C

O bloco de capacidade já governa:

- 18 capacidades funcionais;
- três role-equivalents dedicados de referência — Growth/GTM, comercial institucional/Business e ecossistema/parcerias;
- owner scopes;
- modos de entrega admissíveis;
- benchmarks de mercado para papéis selecionados;
- regras contra dupla contagem de capacidade;
- bandas candidatas de dedicação;
- cobertura compartilhada, fracionária e condicional.

Ainda permanecem pendentes para custo monetário de pessoas:

- resource assignment por mês;
- delivery mode efetivamente escolhido por assignment;
- fração mensal exata;
- quantidade efetiva de pessoas/prestadores;
- remuneração, fee ou cotação;
- benefícios, variável, impostos e componentes acessórios;
- competência mensal.

Logo, F1-C05 continua `partially_parameterized_by_F2B_F2C`, não fechado.

## 3. Pergunta de decisão

A pergunta correta não é “F3 pode ou não pode começar?” como um único estado binário.

F3 possui duas maturidades distintas:

1. **estrutura de caixa** — contratos de fluxo, estados, buckets, calendário e rastreabilidade;
2. **cálculo monetário** — amounts mensais reconciliados, consumo líquido, capital de giro, runway e necessidade de capital.

F1/F2 já possuem maturidade suficiente para a primeira camada, mas não para a segunda.

## 4. Gates de prontidão

### 4.1 F3 structural readiness

O gate `F3_structural_readiness` exige:

1. horizonte governado M0–M6;
2. famílias de receita e metas candidatas identificáveis;
3. pools de custo e drivers materialmente mapeados;
4. estados explícitos para valores ausentes;
5. separação benchmark × quoted × contracted × actual;
6. distinção entre capacidade e custo;
7. prevenção de dupla contagem;
8. modelo conceitual de caixa já capaz de distinguir recebimentos, pagamentos, recursos livres e restritos.

Resultado:

`PASS — conditional structural start allowed after separate authorization`.

### 4.2 F3 monetary readiness

O gate `F3_monetary_readiness` exige, para cada período relevante:

1. saldo inicial de caixa livre e demais buckets aplicáveis;
2. curva de faturamento e recebimentos por fonte;
3. prazos de recebimento e inadimplência/reversões quando aplicáveis;
4. custos materiais com amount ou estado de não aplicabilidade sustentado;
5. calendário de pagamentos;
6. people cost suficientemente parametrizado;
7. tributos e incidências aplicáveis;
8. taxas de pagamentos/repasses com volume/mix;
9. reembolsos, disputas e perdas com premissa/evidência;
10. desembolsos não recorrentes;
11. reservas mínimas e recursos restritos;
12. regras de capital de giro e cenário de estresse.

Resultado:

`FAIL — material monetary inputs missing`.

## 5. O que F3 poderá estruturar sem amount completo

Após autorização específica de F3, a camada estrutural poderá definir, sem preencher valores inexistentes:

### 5.1 Contrato mensal de evento de caixa

```yaml
cash_event_id: string
period: M0 | M1 | M2 | M3 | M4 | M5 | M6
event_type: inflow | outflow | transfer | reserve | release | reversal
source_authority: string
economic_object: string
recognition_state: candidate | benchmark | quoted | contracted | actual | not_applicable
accrual_period: M0..M6_or_TBD
billing_date: date_or_TBD
expected_cash_date: date_or_TBD
actual_cash_date: date_or_TBD
amount_brl: number_or_TBD
cash_bucket: free | restricted | protected_reserve | pass_through | TBD
counterparty_scope: string_or_TBD
payment_or_receipt_terms: string_or_TBD
tax_fee_repass_state: defined | partial | TBD
reconciliation_key: string
notes: string
```

### 5.2 Pontes permitidas

Receita:

```text
meta/driver candidato
→ evento econômico elegível
→ faturamento/competência
→ conta a receber
→ recebimento
→ taxas/tributos/repasses
→ caixa livre ou restrito
```

Custo:

```text
pool/driver
→ obrigação potencial
→ benchmark/quote/contrato
→ competência
→ conta a pagar
→ pagamento
→ classificação de caixa
```

Essas pontes podem existir com `TBD` preservado. O contrato estrutural não transforma `TBD` em zero.

### 5.3 Buckets de caixa

F3 estrutural poderá governar ao menos:

- `free_cash` — caixa livre elegível para operação;
- `restricted_cash` — recurso com destinação/restrição identificada;
- `protected_reserve` — reserva protegida por regra governada;
- `pass_through` — valor recebido mas economicamente devido a terceiro;
- `TBD_classification` — classificação ainda insuficiente.

Saldo vinculado, reserva protegida e pass-through não podem ser silenciosamente tratados como caixa livre.

## 6. O que permanece proibido no F3 estrutural

Enquanto `F3_monetary_readiness = FAIL`, F3 não poderá publicar como resultado válido:

- burn mensal completo;
- burn acumulado M0–M6;
- consumo líquido médio de caixa;
- capital de giro necessário;
- runway;
- necessidade máxima acumulada de capital;
- “rodada necessária”;
- caixa mínimo recomendado em reais;
- break-even;
- margem de segurança financeira;
- suficiência do aporte ilustrativo de R$ 2 milhões.

Qualquer simulação parcial deverá ser identificada como `incomplete_sensitivity`, nunca como forecast completo.

## 7. Bloqueadores monetários reconciliados

| Bloqueador | Origem | Impacto em F3 estrutural | Impacto em F3 monetário |
|---|---|---|---|
| C01/C02/C03 sem custo executável | Product Engineering pausado | não bloqueia schema | bloqueia amount completo |
| C05 people cost incompleto | F2-B/F2-C | não bloqueia owner/driver | bloqueia outflow de pessoas |
| C10 onboarding sem driver | F1-C | pode manter TBD | bloqueia custo mensal completo |
| C11 mídia sem orçamento/experimento | F1-C | pode manter gate condicional | bloqueia cenário com mídia |
| C18 integrações sem escopo | F1-C | pode manter TBD | bloqueia custo de integrações |
| quotes Q04/Q06/Q07/Q12/Q15 pendentes | F1-C | pode registrar quote_required | bloqueia amounts materiais quando ativados |
| saldo inicial livre | cash model | campo pode existir | bloqueia runway |
| timing de recebimento | receita/contratos | campo pode existir | bloqueia curva de caixa |
| tributos/taxas/repasses | fiscal/pagamentos | schema pode existir | bloqueia caixa líquido |
| reservas/restrições | governança de recursos | buckets podem existir | bloqueia caixa livre real |
| perdas/reversões | operação/pagamentos | estado pode existir | bloqueia estresse/caixa líquido |

## 8. Materialidade e regra de promoção

A existência de 12/18 pools com alguma evidência numérica **não representa 66,7% de prontidão financeira**.

Cobertura por contagem de pools não mede materialidade econômica.

Um único item material sem amount — por exemplo people cost, infraestrutura ou tributo — pode inviabilizar o fechamento de um mês inteiro.

Portanto, a promoção para `F3_monetary_readiness: PASS` exige avaliação de **materialidade por período**, não um percentual arbitrário de pools calibrados.

## 9. Relação com o aporte ilustrativo de R$ 2 milhões

Permanece válido:

```text
R$ 2 milhões ilustrativos no GTM-004
≠ caixa inicial confirmado
≠ necessidade de capital
≠ runway
≠ orçamento aprovado
```

F3 estrutural poderá representar uma entrada hipotética apenas em cenário explicitamente identificado como ilustrativo, sem usá-la para concluir suficiência de capital.

## 10. Estado formal de prontidão

| Gate | Resultado |
|---|---|
| F1 scope/cost architecture | PASS |
| F1 numeric evidence coverage | PARTIAL — 12/18 pools with some evidence |
| F1 complete monthly amounts | FAIL — 0/18 fully closed |
| F2 functional capacity | PASS/PARTIAL |
| F2 assignment architecture | PASS/PARTIAL |
| F2 monetary people cost | FAIL — material inputs pending |
| cash conceptual architecture | PASS |
| F3 structural readiness | PASS — conditional |
| F3 monetary readiness | FAIL |
| burn calculable | NO |
| working capital calculable | NO |
| runway calculable | NO |
| capital requirement calculable | NO |

## 11. Parecer

**Parecer:**

`CONDITIONAL GO — F1/F2 provide sufficient semantic and structural maturity to start F3 as a schema-and-flow layer after separate authorization, preserving all missing monetary inputs as TBD. F3 monetary calculation remains blocked until material cost, people, timing, tax, reserve and opening-cash inputs are sufficiently evidenced.`

Em termos operacionais:

```text
F3 estrutural = permitido após autorização separada
F3 monetário = bloqueado
F4 = não autorizado por esta reconciliação
F5 = não autorizado
F6 = não autorizado
```

## 12. Próximo ato governado

Após eventual integração desta reconciliação, o próximo incremento recomendado é:

**F3-S — Estrutura de Caixa e Capital de Giro M0–M6**

Escopo permitido do F3-S:

- contrato de eventos de caixa;
- calendário M0–M6;
- pontes competência/faturamento/recebimento e obrigação/pagamento;
- buckets de caixa;
- estados de evidência;
- regras de reconciliação;
- placeholders explícitos para tributos, taxas, repasses, reservas e saldo inicial;
- nenhuma promoção de `TBD` a zero;
- nenhum cálculo de burn, runway ou necessidade de capital.

F3-S exige autorização própria e esta reconciliação não o inicia automaticamente.
