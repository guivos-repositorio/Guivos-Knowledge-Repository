---
id: GEM-M0-M6-CONSUMPTION-001
title: Planejamento Financeiro M0–M6
status: active
version: 1.0.0
owner: Guivos Economic Model
last_updated: 2026-08-11
depends_on:
  - GEM-F1-M0-M6-COST-BASELINE-001
  - GEM-F1B-M0-M6-COST-CALIBRATION-001
  - GEM-F1C-M0-M6-EVIDENCE-QUOTE-PACK-001
  - GEM-F2-M0-M6-CAPACITY-HEADCOUNT-BASELINE-001
  - GEM-F2B-M0-M6-PEOPLE-DELIVERY-COST-001
  - GEM-F2C-M0-M6-ASSIGNMENT-DEDICATION-001
  - GEM-F1F2-F3-READINESS-RECONCILIATION-001
  - GEM-F3S-M0-M6-CASH-WORKING-CAPITAL-STRUCTURE-001
normative: false
---

# Planejamento Financeiro M0–M6

## 1. Finalidade

Este documento consolida o planejamento financeiro do período M0–M6 em uma única leitura.

O horizonte cobre preparação e lançamento inicial da Guivos em Belo Horizonte.

Ele organiza custos, capacidade, evidências, caixa e prontidão financeira sem converter valores ausentes em falsa precisão.

---

## 2. Perímetro

```text
M0–M3
→ preparação controlada
→ Belo Horizonte / preparação Brasil

M4–M6
→ lançamento inicial
→ Belo Horizonte / operação inicial Brasil
```

São Paulo e Portugal não integram o perímetro econômico M0–M6 desta baseline.

---

## 3. Drivers candidatos

### M0–M3

- 50–100 participantes-piloto;
- 10–20 Coletivos/Organizações;
- 5–10 Parcerias Estratégicas;
- 1–3 pilotos Business.

### M6

Metas candidatas usadas como drivers de dimensionamento:

- 5.000 Pessoas;
- 100 Coletivos;
- 30 Organizações;
- 2 contratos Business;
- 10 Parcerias Estratégicas.

Esses números não são realizados e não autorizam gasto por si só.

---

## 4. Estados de valor

| Estado | Significado |
|---|---|
| `TBD` | custo material identificado, sem valor sustentado |
| `benchmark` | referência externa documentada |
| `quoted` | proposta ou cotação identificável |
| `contracted` | obrigação contratual vigente |
| `actual` | valor realizado e reconciliado |
| `not_applicable` | comprovadamente não aplicável |

> **TBD não é zero.**

Uma linha material em TBD impede tratar o somatório do mês como burn completo.

---

## 5. Dezoito pools de custo

A baseline M0–M6 governa 18 pools:

1. produto, desenvolvimento, QA e entrega técnica;
2. infraestrutura, hospedagem, armazenamento e observabilidade;
3. IA, processamento, mensageria e dados;
4. segurança, privacidade e controles técnicos;
5. equipe e serviços profissionais;
6. jurídico, contábil, fiscal, administrativo e compliance;
7. marca, conteúdo e produção criativa;
8. CRM, vendas e Customer Success;
9. prospecção, reuniões, deslocamentos e operação comercial local;
10. onboarding de Coletivos, Organizações e parceiros;
11. mídia paga e performance;
12. lançamento, eventos e presença de campo;
13. meios de pagamento e cobrança;
14. reembolsos, chargebacks, disputas e perdas;
15. suporte, moderação, curadoria e prevenção de fraude;
16. domínios, marca, propriedade intelectual e ativos institucionais;
17. espaço físico, equipamentos e infraestrutura administrativa;
18. integrações, coordenação e reconciliação entre produtos/parceiros.

---

## 6. Maturidade dos custos

No estado reconciliado:

- 12 de 18 pools possuem ao menos uma taxa, fórmula ou benchmark numérico rastreável;
- 6 de 18 ainda não possuem calibração numérica útil;
- 0 de 18 estão completamente fechados para todos os meses M0–M6.

Continuam sem calibração útil suficiente:

- produto/desenvolvimento/QA;
- infraestrutura/hospedagem;
- IA/processamento/dados;
- onboarding/ecossistema;
- mídia paga/performance;
- integrações/reconciliação.

Essa contagem não representa percentual de prontidão financeira. Materialidade econômica prevalece sobre quantidade de linhas.

---

## 7. Capacidade e pessoas

A arquitetura de capacidade governa 18 capacidades funcionais e papéis de referência para, entre outras frentes:

- Growth/GTM;
- comercial institucional/Business;
- ecossistema/parcerias;
- produto e tecnologia;
- operação;
- suporte;
- governança e funções corporativas.

Ainda não estão completamente fechados para custo monetário de pessoas:

- assignment por mês;
- modo de entrega efetivamente escolhido;
- dedicação mensal exata;
- quantidade efetiva de pessoas/prestadores;
- remuneração ou fee;
- impostos, benefícios e variável;
- competência mensal.

Capacidade e custo permanecem conceitos separados.

---

## 8. Regra contra dupla contagem

Uma mesma capacidade compartilhada não pode ser contabilizada como se representasse múltiplas pessoas dedicadas integralmente.

É necessário distinguir:

```text
capacidade necessária
→ papel equivalente
→ recurso real
→ modo de entrega
→ dedicação
→ custo
```

A existência de um papel arquitetural não significa contratação aprovada.

---

## 9. Ativação temporal

Alguns custos são requeridos desde a preparação; outros dependem de gates.

Exemplos:

- segurança, funções corporativas básicas, pessoas, prospecção e suporte possuem necessidade estrutural desde cedo;
- mídia paga ampla permanece condicionada a validação;
- pagamentos/cobrança dependem da ativação de fluxos financeiros;
- eventos dependem de decisão específica;
- tecnologia depende do escopo de implementação efetivamente autorizado.

A matriz detalhada mensal permanece nas fontes GEM-F1.

---

## 10. Evidências e cotações

Benchmark não deve ser promovido automaticamente para orçamento.

Uma cotação precisa preservar, quando aplicável:

- fornecedor;
- data;
- validade;
- escopo;
- moeda;
- impostos;
- unidade;
- condições;
- premissas.

Valor contratado e realizado exigem documento-fonte e competência.

---

## 11. Prontidão de caixa

A arquitetura distingue duas maturidades.

### Estrutura de caixa

**PASS.**

Já existe base documental suficiente para governar:

- eventos de caixa;
- calendário M0–M6;
- receita → recebimento;
- custo → pagamento;
- contas a receber;
- contas a pagar;
- buckets de caixa;
- estados de evidência;
- taxas, tributos e repasses;
- reconciliação;
- exceções;
- fechamento mensal estrutural.

### Prontidão monetária

**FAIL enquanto entradas materiais estiverem ausentes.**

Ainda faltam elementos como:

- saldo inicial de caixa livre;
- curva real de recebimentos;
- prazos de recebimento;
- custos materiais completos;
- people cost suficiente;
- tributos;
- taxas e repasses;
- perdas e reversões;
- desembolsos não recorrentes;
- reservas;
- regras de capital de giro.

---

## 12. Burn, runway e necessidade de capital

Enquanto a prontidão monetária estiver incompleta:

```text
burn completo = não calculável com autoridade suficiente
runway = não calculável com autoridade suficiente
necessidade de capital = não calculável com autoridade suficiente
```

Subtotais parciais não devem ser apresentados como “custo mínimo da Guivos”.

---

## 13. Relação com o cenário de investimento

O valor ilustrativo de R$ 2 milhões utilizado em material de GTM não equivale a:

- saldo inicial confirmado;
- necessidade de capital;
- funding aprovado;
- orçamento;
- runway suficiente.

Ele permanece cenário ilustrativo até decisão própria.

---

## 14. Capital de giro

A estrutura financeira precisa separar, quando aplicável:

- caixa livre;
- recursos restritos;
- recebimentos pendentes;
- obrigações a pagar;
- tributos;
- repasses;
- reservas;
- reembolsos/disputas;
- eventos extraordinários.

Saldo bancário bruto não deve ser confundido automaticamente com caixa livre utilizável.

---

## 15. Próximo avanço financeiro

O avanço para cálculo monetário confiável depende de substituir TBDs materiais por evidências governadas, especialmente em:

- tecnologia e infraestrutura;
- IA/dados;
- custo de pessoas;
- onboarding;
- mídia quando ativada;
- integrações;
- tributação e pagamentos;
- saldo inicial e calendário de caixa.

---

## 16. Síntese

> **A Guivos possui uma arquitetura financeira M0–M6 suficientemente estruturada para organizar custos, capacidade e caixa, mas ainda não possui base monetária completa para declarar burn, runway ou necessidade definitiva de capital. A regra vigente é preservar TBD onde ainda não existe evidência, em vez de preencher o modelo com falsa precisão.**