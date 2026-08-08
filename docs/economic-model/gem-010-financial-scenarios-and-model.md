---
id: GEM-010
title: Cenários e Modelo Financeiro
status: active
version: 0.3.0
owner: Guivos Economic Model
last_updated: 2026-08-08
parent: GEM-000
depends_on:
  - GEM-009
  - GEM-009-DEPENDENCY-VALIDATION-CHECKPOINT-001
related:
  - GEM-004-A1
  - GEM-004-A2
  - GEM-009
  - GEM-010-A1
  - GEM-010-A2
  - GEM-COMMERCIAL-BASELINE-001
  - GEM-POST-P9-FINANCIAL-RECONCILIATION-001
  - GTM-003
  - GTM-004
  - GTM-006
  - M6.9
  - M7.39
---

# GEM-010 — Cenários e Modelo Financeiro

## 1. Objetivo

Definir a arquitetura pela qual premissas rastreáveis poderão ser transformadas em cenários comparáveis de atividade, receita, custos, margem, caixa, capital, capacidade e sustentabilidade, sem inventar valores nem tratar projeções como fatos.

A versão 0.3.0 reconcilia a arquitetura financeira com a baseline quantitativa pós-P9 do Go-to-Market. Preços, metas de pagantes, envelopes de receita e checkpoints M0–M60 podem agora ser consumidos como entradas candidatas rastreáveis, sem promovê-los a budget, forecast, margem, caixa, necessidade de capital ou valuation aprovado.

## 2. Princípio central

```text
pergunta decisória
→ data-base e horizonte
→ premissas classificadas
→ drivers e dependências
→ cenário coerente
→ demonstrações reconciliadas
→ sensibilidade e riscos
→ gates e decisão humana
```

## 3. Camadas do modelo

1. premissas e evidências;
2. drivers de usuários, parceiros, transações e capacidade;
3. planos, preços, cotas e mix de contratação;
4. receitas, custos e margens;
5. caixa, capital de giro, runway e necessidade de capital;
6. unit economics por produto, segmento e coorte;
7. sensibilidades, break-even e eventos de estresse;
8. consolidação entre produtos, reservas, subsídios e reinvestimento;
9. governança, versionamento e gates.

## 4. Estados

`conceptual`, `candidate_parameterized`, `partial_parameterization`, `parameter_pending`, `evidence_pending`, `calibrated`, `reviewed`, `approved_for_planning`, `superseded` ou `retired`.

Após a reconciliação pós-P9:

- preços governados de Pessoas, Coletivos e Organizações: `candidate_parameterized`;
- metas e receita de planejamento do `GTM-003`: `candidate_parameterized` como entrada GTM, não forecast aprovado;
- Guivos Business: `partial_parameterization`, pois contratos e envelope agregado existem, mas preço/mix por tier permanecem pendentes;
- Opportunity Boost: `candidate_parameterized`, excluído do forecast de receita vigente;
- custos, capacidade financeira, tributos, margem, caixa, runway e necessidade de capital: `parameter_pending` ou `evidence_pending` conforme a dimensão.

## 5. Separações canônicas

- cenário não é previsão garantida;
- projeção não é fato, meta ou compromisso;
- meta GTM não é automaticamente premissa financeira aprovada;
- preço candidato não é disposição a pagar;
- preço publicado não é receita realizada;
- assinatura não é transação;
- GMV não é receita;
- receita não é caixa;
- aporte e dívida não são receita;
- aporte ilustrativo não é necessidade de capital calculada;
- margem não é lucro nem caixa livre;
- break-even contábil não é liquidez suficiente;
- runway não é autorização para consumir reservas protegidas;
- transferência interna não é receita consolidada;
- crescimento modelado não comprova capacidade;
- premissa otimista não é cenário base;
- sensibilidade de faturamento não é cenário financeiro completo;
- valuation não é resultado automático do modelo.

## 6. Autoridade de parâmetros comerciais

O GEM-010-A1 governa:

- preços mensais e anuais candidatos;
- faixas de sensibilidade;
- premissas de moeda e cobrança;
- drivers de custo;
- perguntas e métricas de validação;
- unit economics mínimos;
- gates de teste;
- critérios de parada.

O `GTM-003` governa a baseline candidata de pagantes, mix, receita e crescimento. O `GTM-006` organiza os horizontes M0–M60. O `GTM-004` governa referências candidatas de investimento e valuation. A leitura conjunta desses documentos é disciplinada por `GEM-POST-P9-FINANCIAL-RECONCILIATION-001`.

## 7. Ponte quantitativa pós-P9

O GEM pode consumir os checkpoints de `GTM-003` como `candidate_gtm_input` para construção futura de cenários.

| Checkpoint | ARR conhecido de planos | Business ARR-alvo | Run-rate combinado mínimo |
|---|---:|---:|---:|
| M12 | R$ 695.910 | R$ 400.000 | R$ 1.095.910 |
| M24 | R$ 3.661.764 | R$ 1.800.000 | R$ 5.461.764 |
| M36 | R$ 12.109.296 | R$ 6.000.000 | R$ 18.109.296 |
| M48 | R$ 25.445.100 | R$ 14.000.000 | R$ 39.445.100 |
| M60 | R$ 44.284.560 | R$ 25.000.000 | R$ 69.284.560 |

Esses valores não resolvem custos, margem, recebimento, caixa ou capital. Fontes não precificadas ou não validadas continuam excluídas, inclusive Opportunity Boost e outras famílias que ainda não possuem autoridade suficiente para forecast.

## 8. Cenários após P9

Os multiplicadores conservador/base/aceleração do `GTM-003` devem ser lidos como **sensibilidades de faturamento**, não como cenários financeiros completos.

Os cenários completos do GEM permanecem:

- conservador;
- base;
- expansivo;
- estresse.

Quando parametrizados, deverão reconciliar simultaneamente receita, custos, capacidade, capital de giro, caixa, reservas e financiamento. Não é permitido reduzir ou ampliar apenas a receita e assumir comportamento proporcional de custos e caixa.

## 9. Capital, runway e valuation

O cenário de aporte de R$ 2 milhões do `GTM-004` permanece ilustrativo. O GEM ainda não calcula necessidade de capital, porque faltam parâmetros materiais de custo, headcount, tributos, pagamentos, recebimentos, capital de giro, reservas e desembolsos.

Portanto:

```text
aporte ilustrativo de R$ 2 mi
≠ capital necessário calculado
≠ runway aprovado
≠ budget aprovado
```

A faixa de valuation pré-receita de R$ 10–15 milhões, com referência central de R$ 12 milhões, permanece âncora negocial candidata. As sensibilidades futuras por múltiplo de run-rate não constituem appraisal nem valuation aprovado.

## 10. Gates de calibração financeira

A promoção para `approved_for_planning` exige, no mínimo:

1. baseline rastreável de custos e comportamento fixo/variável/degrau;
2. plano de capacidade e headcount por gate;
3. tributos, taxas de pagamento, perdas, repasses e políticas de recebimento/pagamento;
4. curva mensal de caixa e capital de giro no curto prazo;
5. CAC, retenção, churn, margem e custo de servir com evidência suficiente;
6. cenários completos de conservador, base, expansivo e estresse;
7. cálculo de runway e necessidade acumulada de capital;
8. revisão financeira, contábil, fiscal e jurídica quando aplicável;
9. aprovação humana competente e versão congelada da data-base.

A ausência de um parâmetro continuará `TBD`/pendente; não será substituída por zero silencioso.

## 11. Prioridade de detalhamento

A calibração deverá aumentar precisão do horizonte mais próximo antes de preencher cinco anos com falsa exatidão:

```text
M0–M6 mensal
→ M7–M12 mensal
→ M13–M24 trimestral com gates
→ M25–M60 por horizonte e sensibilidade
```

Essa orientação não altera os checkpoints estratégicos do GTM.

## 12. Limites

Esta versão não aprova:

- previsão oficial de receita;
- orçamento;
- captação;
- dívida;
- investimento;
- política contábil;
- metas externas;
- margem;
- valuation;
- tributos;
- comissão;
- oferta pública;
- operação;
- implementação técnica.

## 13. Estado

`partial_parameterization — post-P9 GTM revenue and growth inputs reconciled; costs, capacity, unit economics, cash, runway, capital requirement, specialist reviews and planning approvals pending`.
