---
id: GEM-010-CASH-WORKING-CAPITAL-AND-FUNDING-001
title: Caixa, Capital de Giro e Necessidade de Capital
status: draft
version: 0.3.0
owner: Guivos Economic Model
last_updated: 2026-08-08
parent: GEM-010
related:
  - GEM-POST-P9-FINANCIAL-RECONCILIATION-001
  - GEM-F1F2-F3-READINESS-RECONCILIATION-001
  - GEM-F1-M0-M6-COST-BASELINE-001
  - GEM-F1C-M0-M6-EVIDENCE-QUOTE-PACK-001
  - GEM-F2C-M0-M6-ASSIGNMENT-DEDICATION-001
  - GTM-004
---

# Caixa, Capital de Giro e Necessidade de Capital

## Pontes

O modelo deverá separar faturamento, reconhecimento gerencial, recebimento, pagamento, repasse, saldo livre, saldo vinculado e reserva protegida.

## Indicadores conceituais

- consumo líquido de caixa;
- runway por cenário;
- necessidade máxima acumulada de capital;
- capital de giro operacional;
- atraso de recebimentos e pagamentos;
- cobertura de obrigações e reservas.

`runway = caixa livre disponível / consumo líquido médio`, somente quando denominador, sazonalidade e restrições forem apropriados.

Necessidade de capital não autoriza captação. Recursos vinculados ou protegidos não compõem caixa livre.

## Estado pós-P9

A reconciliação de 2026-08-08 confirmou que estes indicadores **ainda não são calculáveis** com segurança. A baseline GTM fornece metas de receita, mas permanecem pendentes, entre outros:

- caixa livre inicial;
- curva mensal de recebimentos e pagamentos;
- custos estruturais e variáveis;
- headcount e custos por capacidade;
- tributos, taxas, perdas, reembolsos e repasses;
- desembolsos não recorrentes;
- reservas mínimas e recursos restritos;
- premissas de capital de giro e cenário de estresse.

O aporte de referência de **R$ 2 milhões** utilizado no `GTM-004` é exclusivamente um cenário ilustrativo de estruturação de rodada. Não é resultado deste modelo e não deverá ser apresentado como necessidade de capital calculada, runway aprovado ou orçamento disponível.

```text
R$ 2 milhões ilustrativos
≠ necessidade máxima acumulada de capital
≠ caixa livre disponível
≠ runway aprovado
```

O cálculo somente poderá ser promovido quando os parâmetros acima possuírem fonte, data-base, estado e revisão adequados.

## Prontidão F1/F2 para F3

A autoridade `GEM-F1F2-F3-READINESS-RECONCILIATION-001` separa dois gates que não podem ser tratados como equivalentes:

```text
F3_structural_readiness = PASS — conditional
F3_monetary_readiness = FAIL
```

### Camada estrutural

Após autorização própria, F3 poderá estruturar sem amounts completos:

- contrato de eventos de caixa;
- calendário M0–M6;
- pontes competência/faturamento/recebimento;
- pontes obrigação/conta a pagar/pagamento;
- buckets de `free_cash`, `restricted_cash`, `protected_reserve` e `pass_through`;
- estados de evidência;
- chaves de reconciliação;
- campos `TBD` para saldo inicial, tributos, taxas, repasses, reservas, prazos e amounts ainda não sustentados.

Estruturar esses contratos **não significa que existe caixa, custo, recebimento ou pagamento calculado**.

### Camada monetária

Permanece bloqueada enquanto existirem inputs materiais insuficientes em custos, people cost, timing, tributos, reservas, saldo inicial e demais drivers.

Enquanto `F3_monetary_readiness = FAIL`, continuam `NOT CALCULABLE`:

- burn mensal completo;
- burn acumulado;
- consumo líquido de caixa;
- capital de giro necessário;
- runway;
- necessidade máxima acumulada de capital;
- rodada necessária;
- margem de segurança financeira.

A existência de benchmarks parciais em F1/F2 não permite preencher `TBD` como zero nem somar um suposto custo mínimo.

## Próximo incremento permitido

Após integração da reconciliação de prontidão e mediante autorização separada, o próximo incremento permitido é **F3-S — Estrutura de Caixa e Capital de Giro M0–M6**.

F3-S é uma camada de schema, fluxo, calendário e reconciliação. Não autoriza cálculo monetário completo, captação, orçamento ou conclusão sobre suficiência do aporte ilustrativo de R$ 2 milhões.
