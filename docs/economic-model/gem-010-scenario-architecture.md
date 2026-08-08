---
id: GEM-010-SCENARIO-ARCHITECTURE-001
title: Arquitetura de Cenários
status: draft
version: 0.2.0
owner: Guivos Economic Model
last_updated: 2026-08-08
parent: GEM-010
related:
  - GEM-POST-P9-FINANCIAL-RECONCILIATION-001
  - GTM-003
---

# Arquitetura de Cenários

## Cenários mínimos

| Cenário | Função |
|---|---|
| conservador | testar menor adoção, conversão e eficiência, com maior pressão de custo e caixa |
| base | representar o conjunto mais defensável de premissas disponíveis |
| expansivo | testar crescimento superior condicionado a capacidade e financiamento |
| estresse | testar choques combinados, concentração, atraso de receita e aumento de custos |

## Contrato de comparabilidade

Todos deverão compartilhar data-base, horizonte, granularidade, moedas, perímetro de consolidação, política de arredondamento e definições métricas. Diferenças deverão estar concentradas em premissas identificadas.

## Horizontes

- curto prazo: liquidez, capacidade e execução;
- médio prazo: eficiência, retenção, margem e capital;
- longo prazo: sustentabilidade e resiliência, com incerteza ampliada.

Probabilidades não serão atribuídas sem método e evidência. O cenário base não será escolhido por conveniência narrativa.

## Reconciliação pós-P9

Os multiplicadores `70% / 100% / 130%` registrados no `GTM-003` representam **sensibilidades de faturamento** para gestão de risco. Eles não substituem os quatro cenários deste contrato.

Um cenário financeiro completo deverá variar drivers correlacionados de forma coerente, incluindo quando parametrizados:

- aquisição, conversão, retenção e churn;
- preço, mix e descontos;
- custos variáveis e custos em degrau;
- capacidade e headcount;
- CAC e canais;
- tributos, pagamentos, reembolsos e inadimplência;
- capital de giro e timing de caixa;
- reservas, funding e expansão territorial.

Reduzir receita para 70% não autoriza reduzir custos na mesma proporção. Elevar receita para 130% não presume que capacidade, margem ou caixa acompanhem linearmente. O cenário de estresse deverá preservar rupturas mensais relevantes em vez de diluí-las em médias anuais.
