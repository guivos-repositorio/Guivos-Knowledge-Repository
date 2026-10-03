---
id: GEM-F1F2-F3-READINESS-RECONCILIATION-001
title: Reconciliação de Prontidão F1/F2 para F3
status: active
version: 0.2.0
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
  - GEM-F3S-M0-M6-CASH-WORKING-CAPITAL-STRUCTURE-001
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

A reconciliação não cria valores mensais, não escolhe fornecedores, não contrata pessoas, não reativa Product Engineering e não autoriza captação.

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

F3 possui duas maturidades distintas:

1. **estrutura de caixa** — contratos de fluxo, estados, buckets, calendário e rastreabilidade;
2. **cálculo monetário** — amounts mensais reconciliados, consumo líquido, capital de giro, runway e necessidade de capital.

F1/F2 possuem maturidade suficiente para a primeira camada, mas não para a segunda.

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
8. modelo conceitual de caixa capaz de distinguir recebimentos, pagamentos, recursos livres e restritos.

Resultado original:

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

Resultado vigente:

`FAIL — material monetary inputs missing`.

## 5. Consumo do gate estrutural por F3-S

A autorização posterior permitiu a execução de `GEM-F3S-M0-M6-CASH-WORKING-CAPITAL-STRUCTURE-001`.

F3-S materializa a camada estrutural aprovada por esta reconciliação e governa:

- contrato canônico de evento de caixa;
- calendário estrutural M0–M6;
- pontes de receita→recebimento;
- pontes de custo→pagamento;
- estados de contas a receber e pagar;
- buckets de caixa;
- estados de evidência;
- taxas, tributos e repasses como componentes rastreáveis;
- regras de reconciliação;
- exceções e fechamento mensal estrutural;
- preservação explícita de `TBD`.

Assim, o gate estrutural deixa de ser apenas autorização potencial e passa a possuir implementação documental específica.

```text
F3 structural architecture = instantiated by F3-S
F3 monetary readiness = FAIL
```

Isso **não** promove nenhum output monetário.

## 6. Bloqueadores monetários reconciliados

| Bloqueador | Origem | Impacto em F3 estrutural | Impacto em F3 monetário |
|---|---|---|---|
| C01/C02/C03 sem custo executável | Product Engineering pausado | schema suporta TBD | bloqueia amount completo |
| C05 people cost incompleto | F2-B/F2-C | owner/driver suportado | bloqueia outflow de pessoas |
| C10 onboarding sem driver | F1-C | schema suporta TBD | bloqueia custo mensal completo |
| C11 mídia sem orçamento/experimento | F1-C | gate condicional suportado | bloqueia cenário com mídia |
| C18 integrações sem escopo | F1-C | schema suporta TBD | bloqueia custo de integrações |
| quotes Q04/Q06/Q07/Q12/Q15 pendentes | F1-C | `quote_required` suportado | bloqueia amounts materiais quando ativados |
| saldo inicial livre | cash model | bucket/campo existe | bloqueia runway |
| timing de recebimento | receita/contratos | campo existe | bloqueia curva de caixa |
| tributos/taxas/repasses | fiscal/pagamentos | componentes separados | bloqueia caixa líquido |
| reservas/restrições | governança de recursos | buckets existem | bloqueia caixa livre real |
| perdas/reversões | operação/pagamentos | lifecycle existe | bloqueia estresse/caixa líquido |

## 7. Materialidade e regra de promoção

A existência de 12/18 pools com alguma evidência numérica **não representa 66,7% de prontidão financeira**.

Cobertura por contagem de pools não mede materialidade econômica.

Um único item material sem amount — por exemplo people cost, infraestrutura ou tributo — pode inviabilizar o fechamento de um mês inteiro.

A promoção para `F3_monetary_readiness: PASS` exige avaliação de **materialidade por período**, não percentual arbitrário de pools calibrados.

## 8. Relação com o aporte ilustrativo de R$ 2 milhões

Permanece válido:

```text
R$ 2 milhões ilustrativos no GTM-004
≠ caixa inicial confirmado
≠ necessidade de capital
≠ runway
≠ orçamento aprovado
```

F3-S não usa esse valor para concluir suficiência de capital.

## 9. Estado formal após F3-S

| Gate | Resultado |
|---|---|
| F1 scope/cost architecture | PASS |
| F1 numeric evidence coverage | PARTIAL — 12/18 pools with some evidence |
| F1 complete monthly amounts | FAIL — 0/18 fully closed |
| F2 functional capacity | PASS/PARTIAL |
| F2 assignment architecture | PASS/PARTIAL |
| F2 monetary people cost | FAIL — material inputs pending |
| cash conceptual architecture | PASS |
| F3 structural readiness | PASS — gate consumed by F3-S |
| F3 structural architecture | PASS — instantiated by F3-S |
| F3 monetary readiness | FAIL |
| burn calculable | NO |
| working capital calculable | NO |
| runway calculable | NO |
| capital requirement calculable | NO |

## 10. Parecer pós-F3-S

**Parecer:**

`STRUCTURAL PASS / MONETARY FAIL — the F3 structural gate has been consumed by the F3-S authority, which now governs M0–M6 cash-event structure, lifecycle, buckets, calendar and reconciliation. Material monetary inputs remain insufficient; burn, working capital amount, runway and capital requirement remain not calculable.`

Em termos operacionais:

```text
F3-S estrutural = executado documentalmente
F3 monetário = bloqueado
F4 = não autorizado por esta reconciliação
F5 = não autorizado
F6 = não autorizado
```

## 11. Próximo ato governado

Após eventual integração de F3-S, o próximo incremento econômico recomendado poderá ser:

**F3-M readiness/input closure**

Escopo admissível somente mediante autorização separada:

- inventariar saldo inicial por bucket;
- fechar timing/amount de recebimentos sustentáveis;
- fechar timing/amount de pagamentos materiais;
- reconciliar people cost monetário;
- definir tributos aplicáveis;
- definir taxas/repasses por arquitetura real;
- governar reservas/restrições;
- tratar perdas/reversões e desembolsos não recorrentes;
- reavaliar `F3_monetary_readiness` por materialidade.

F3-M não significa automaticamente calcular runway ou necessidade de capital. F4, F5 e F6 permanecem dependentes de gates posteriores.
