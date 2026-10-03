---
id: GEM-010-CASH-WORKING-CAPITAL-AND-FUNDING-001
title: Caixa, Capital de Giro e Necessidade de Capital
status: draft
version: 0.4.0
owner: Guivos Economic Model
last_updated: 2026-08-08
parent: GEM-010
related:
  - GEM-POST-P9-FINANCIAL-RECONCILIATION-001
  - GEM-F1F2-F3-READINESS-RECONCILIATION-001
  - GEM-F3S-M0-M6-CASH-WORKING-CAPITAL-STRUCTURE-001
  - GEM-F1-M0-M6-COST-BASELINE-001
  - GEM-F1C-M0-M6-EVIDENCE-QUOTE-PACK-001
  - GEM-F2C-M0-M6-ASSIGNMENT-DEDICATION-001
  - GTM-004
---

# Caixa, Capital de Giro e Necessidade de Capital

## Pontes

O modelo deverá separar faturamento, reconhecimento gerencial, recebimento, pagamento, repasse, saldo livre, saldo vinculado e reserva protegida.

A camada estrutural M0–M6 é governada por `GEM-F3S-M0-M6-CASH-WORKING-CAPITAL-STRUCTURE-001`.

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

## Prontidão F1/F2 para F3

A autoridade `GEM-F1F2-F3-READINESS-RECONCILIATION-001` separa dois gates que não podem ser tratados como equivalentes:

```text
F3_structural_readiness = PASS — conditional
F3_monetary_readiness = FAIL
```

F3-S executa apenas a primeira camada.

## Camada F3-S — estrutura M0–M6

`GEM-F3S-M0-M6-CASH-WORKING-CAPITAL-STRUCTURE-001` passa a governar estruturalmente:

- contrato canônico de evento de caixa;
- calendário estrutural M0–M6;
- pontes competência/faturamento/recebimento;
- pontes obrigação/conta a pagar/pagamento;
- contas a receber e contas a pagar por estados;
- buckets `free_cash`, `restricted_cash`, `protected_reserve`, `pass_through` e `TBD_classification`;
- estados de evidência;
- chaves de reconciliação;
- taxas, tributos e repasses como componentes rastreáveis;
- reversões, cancelamentos e disputas vinculados ao evento original;
- fechamento mensal estrutural com exceções explícitas;
- campos `TBD` para saldo inicial, prazos, amounts, reservas e demais inputs ainda não sustentados.

F3-S formaliza:

```text
competência ≠ faturamento ≠ contas a receber ≠ recebimento ≠ caixa livre
obrigação ≠ contas a pagar ≠ pagamento
saldo bancário ≠ caixa livre
pass-through ≠ receita própria
TBD ≠ zero
```

Estruturar esses contratos **não significa que existe caixa, custo, recebimento ou pagamento calculado**.

## Camada monetária

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

A existência de benchmarks parciais em F1/F2 ou do schema F3-S não permite preencher `TBD` como zero nem somar um suposto custo mínimo.

## Gate de promoção monetária

O modelo somente poderá calcular outputs monetários completos quando, por período material, existirem evidências suficientes para:

1. saldo inicial por bucket;
2. recebimentos e respectivos timings;
3. pagamentos materiais e timings;
4. people cost;
5. tributos aplicáveis;
6. taxas e repasses;
7. perdas, reversões e disputas;
8. reservas/restrições;
9. desembolsos não recorrentes;
10. ausência de `TBD` material que torne o fechamento enganoso.

A avaliação deverá ser por materialidade, não por percentual simples de linhas preenchidas.

## Próximo incremento permitido

Após eventual integração de F3-S, o próximo incremento econômico poderá ser uma **F3-M readiness/input closure**, destinada a verificar e preencher, somente com evidência adequada, os inputs materiais necessários para futura promoção monetária.

F3-M não está automaticamente autorizada por F3-S. F4, F5 e F6 permanecem bloqueados até seus gates próprios.
