---
id: GEM-F1-M0-M6-COST-BASELINE-001
title: Baseline de Custos M0–M6 — F1
status: active
version: 0.2.0
owner: Guivos Economic Model
last_updated: 2026-08-08
parent: GEM-010
depends_on:
  - GEM-POST-P9-FINANCIAL-RECONCILIATION-001
  - GEM-008-COST-ARCHITECTURE-001
  - GEM-010-COST-AND-CAPACITY-MODEL-001
  - GTM-001
  - GTM-002
  - GTM-003
  - GTM-006
related:
  - GEM-F1B-M0-M6-COST-CALIBRATION-001
  - GEM-009-COST-AND-UNIT-ECONOMICS-001
  - GEA-REF-GRAPH-001
normative: true
---

# Baseline de Custos M0–M6 — F1

## 1. Finalidade

Estabelecer a primeira baseline governada de custos para o horizonte de lançamento `M0–M6`, com granularidade mensal, categorias, comportamento, drivers, estado de ativação e maturidade de evidência suficientes para posterior calibração numérica.

Esta autoridade **não aprova orçamento, contratação, headcount, fornecedor, tecnologia, captação, burn, runway ou necessidade de capital**.

A ausência de valor validado deverá permanecer `TBD`. `TBD` **não equivale a zero**.

## 2. Perímetro temporal e territorial

| Período | Estado de GTM | Território econômico desta baseline |
|---|---|---|
| M0–M3 | preparação controlada | Belo Horizonte / preparação Brasil |
| M4–M6 | lançamento inicial | Belo Horizonte / operação inicial Brasil |

Ficam fora desta baseline:

- São Paulo, cuja expansão começa após M6 na sequência vigente;
- Portugal/Lisboa, que permanece candidato condicionado e não operação ativa;
- expansão nacional posterior a M12;
- custos de escala internacional;
- custos de implementação de tecnologias, vendors, tiers ou regiões ainda não aprovados.

## 3. Drivers de referência M0–M6

Os volumes do GTM são usados somente como **drivers candidatos de dimensionamento**, nunca como prova de custo ou autorização de gasto.

### M0–M3 — preparação

- 50–100 participantes-piloto;
- 10–20 Coletivos/Organizações;
- 5–10 Parcerias Estratégicas;
- 1–3 pilotos Guivos Business;
- sem pressão de mídia paga ampla antes de validação de ativação.

### M4–M6 — lançamento de Belo Horizonte

Baseline-alvo em M6:

- 5.000 Pessoas;
- 100 Coletivos;
- 30 Organizações;
- 2 contratos Guivos Business;
- 10 Parcerias Estratégicas.

Estes números são metas candidatas de GTM e não realizados.

## 4. Estados de valor e evidência

Cada linha de custo deverá usar um dos estados abaixo.

| Estado | Significado | Pode entrar em burn calculado? |
|---|---|---|
| `TBD` | custo material identificado, valor ainda não sustentado | não |
| `benchmark` | estimativa externa documentada, datada e comparável | sim, apenas em cenário candidato |
| `quoted` | proposta/cotação identificável e ainda não contratada | sim, apenas em cenário candidato |
| `contracted` | obrigação contratual vigente e documentada | sim |
| `actual` | desembolso ou competência observada e reconciliada | sim |
| `not_applicable` | custo comprovadamente não aplicável ao período/perímetro | não |

Regras:

1. valor `0` somente poderá existir com evidência explícita de ausência de desembolso/obrigação;
2. linha `TBD` material impede tratar o somatório mensal como burn completo;
3. benchmark deverá registrar fonte, data, moeda, impostos, unidade e hipótese de uso;
4. cotação deverá registrar fornecedor, validade, escopo e impostos quando disponíveis;
5. valor contratado ou realizado deverá preservar documento-fonte e competência;
6. custo compartilhado deverá continuar visível mesmo antes de rateio;
7. custo não caixa, oportunidade e externalidade não será silenciosamente convertido em desembolso.

## 5. Contrato mínimo de linha de custo

```yaml
cost_id: string
cost_name: string
category: C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08
period: M0 | M1 | M2 | M3 | M4 | M5 | M6
activation_state: required | conditional | inactive_by_baseline | not_applicable
behavior: fixed | variable | semivariable | step | event | TBD
allocation_scope: direct | shared | corporate | TBD
recurrence: recurring | non_recurring | contingent | TBD
cash_nature: cash | non_cash | mixed | TBD
driver: string | TBD
unit: string | TBD
amount_brl: number | TBD
value_state: TBD | benchmark | quoted | contracted | actual | not_applicable
confidence: low | medium | high | not_assessed
source: string | TBD
owner_scope: string | TBD
activation_gate: string | none
notes: string
```

F1-B pode registrar uma **taxa unitária benchmark** ou fórmula variável enquanto `amount_brl` permanece `TBD`. O valor mensal somente nasce quando quantidade, aplicabilidade e período estiverem suficientemente governados.

## 6. Catálogo mestre de pools M0–M6

| ID | Categoria | Pool de custo | Comportamento inicial | Driver principal | Estado numérico |
|---|---|---|---|---|---|
| F1-C01 | C-02 | produto, desenvolvimento, QA e entrega técnica | fixo/step | escopo implementável e releases autorizados | TBD |
| F1-C02 | C-02 | infraestrutura, hospedagem, armazenamento e observabilidade | semivariável/step | ambientes, tráfego, armazenamento e disponibilidade | TBD |
| F1-C03 | C-01/C-02 | IA, processamento, mensageria e serviços de dados | variável/step | uso elegível e volume processado | TBD |
| F1-C04 | C-04 | segurança, privacidade e controles técnicos | fixo/step | superfície, risco e requisitos aprovados | TBD / quote required |
| F1-C05 | C-02 | equipe e serviços profissionais | fixo/step | capacidade e papéis requeridos | TBD — depende de F2 para dimensionamento |
| F1-C06 | C-02/C-04 | jurídico, contábil, fiscal, administrativo e compliance | fixo/event | obrigações, contratos e gates de lançamento | parcialmente calibrado por benchmark |
| F1-C07 | C-02 | marca, conteúdo e produção criativa | fixo/event | calendário de conteúdo e lançamento | TBD |
| F1-C08 | C-03 | CRM, vendas e Customer Success | fixo/step | pipeline institucional e contas ativas | parcialmente calibrado por benchmark |
| F1-C09 | C-03/C-06 | prospecção, reuniões, deslocamentos e operação comercial local | variável/event | reuniões, pilotos e parceiros em BH | TBD |
| F1-C10 | C-03/C-06 | onboarding de Coletivos, Organizações, parceiros e ativação comunitária | variável/step | entidades ativadas e suporte de implantação | TBD |
| F1-C11 | C-03 | mídia paga e performance | variável | aquisição incremental validada | TBD — condicionada a gate de ativação |
| F1-C12 | C-03 | lançamento, eventos e presença de campo em BH | event | ações de lançamento autorizadas | TBD / quote required |
| F1-C13 | C-01 | meios de pagamento e cobrança | variável | volume financeiro elegível e transações | fórmula benchmark disponível; amount TBD |
| F1-C14 | C-05 | reembolsos, chargebacks, disputas e perdas operacionais | contingent/variable | transações e incidentes | tarifa parcial benchmark; incidência TBD |
| F1-C15 | C-04 | suporte, moderação, curadoria e prevenção de fraude | semivariável/step | usuários, entidades, casos e conteúdo | TBD |
| F1-C16 | C-02 | domínios, marca, propriedade intelectual e ativos institucionais | fixed/event | ativos efetivamente mantidos ou protegidos | tarifas oficiais de INPI parciais; demais itens TBD |
| F1-C17 | C-02 | espaço físico, coworking, equipamentos e infraestrutura administrativa | fixed/event | decisão operacional explícita | benchmark BH disponível; necessidade TBD |
| F1-C18 | C-06 | integrações, coordenação e reconciliação entre produtos/parceiros | variable/step | integrações e relações efetivamente ativadas | TBD |

A calibração detalhada e suas fontes são governadas por `GEM-F1B-M0-M6-COST-CALIBRATION-001`.

### C-07 e C-08

Custos de oportunidade e externalidades sociais/ambientais continuam obrigatórios para decisão, mas não integram automaticamente o desembolso mensal. Quando materiais, deverão ser registrados em análise própria e ligados à linha econômica correspondente.

## 7. Matriz de ativação mensal

Legenda:

- `R` — requerido no escopo do mês, valor ainda sujeito ao estado de evidência;
- `C` — condicional a gate/decisão/atividade real;
- `I` — inativo pela baseline vigente do período;
- `D` — depende de frente posterior de dimensionamento, sem autorização antecipada.

| Pool | M0 | M1 | M2 | M3 | M4 | M5 | M6 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| F1-C01 Produto/desenvolvimento/QA | C | C | C | C | C | C | C |
| F1-C02 Infraestrutura/hospedagem | C | C | C | C | C | C | C |
| F1-C03 IA/processamento/dados | C | C | C | C | C | C | C |
| F1-C04 Segurança/privacidade | R | R | R | R | R | R | R |
| F1-C05 Equipe/serviços profissionais | D | D | D | D | D | D | D |
| F1-C06 Jurídico/contábil/fiscal/admin | R | R | R | R | R | R | R |
| F1-C07 Marca/conteúdo/criativo | C | C | C | C | R | R | R |
| F1-C08 CRM/vendas/Customer Success | C | C | C | C | R | R | R |
| F1-C09 Prospecção/reuniões/deslocamentos BH | R | R | R | R | R | R | R |
| F1-C10 Onboarding/ecossistema | R | R | R | R | R | R | R |
| F1-C11 Mídia paga/performance | I | I | I | I | C | C | C |
| F1-C12 Eventos/presença de campo BH | C | C | C | C | C | C | C |
| F1-C13 Pagamentos/cobrança | I | I | C | C | C | C | C |
| F1-C14 Reembolsos/chargebacks/disputas | I | I | C | C | C | C | C |
| F1-C15 Suporte/moderação/curadoria/fraude | R | R | R | R | R | R | R |
| F1-C16 Domínios/marca/IP | C | C | C | C | C | C | C |
| F1-C17 Espaço/equipamentos físicos | C | C | C | C | C | C | C |
| F1-C18 Integrações/coordenação/reconciliação | C | C | C | C | C | C | C |

`R`, `C`, `I` e `D` não representam valor monetário. Em especial, `I` não autoriza registrar R$ 0 sem evidência do período.

## 8. Restrições tecnológicas

A arquitetura vigente mantém tecnologias de grafo e inteligência como referências arquiteturais, sem fornecedor, tier, contrato, região, custo ou implementação aprovados.

Consequentemente, esta baseline:

- não presume contratação de Neo4j, GraphRAG, GDS, Power BI ou serviço equivalente;
- não usa preço de vendor como fato interno;
- não transforma arquitetura de referência em OPEX ou CAPEX;
- mantém F1-C01, F1-C02 e F1-C03 `TBD` até decisão técnica e evidência de custo compatíveis com os gates de Product Engineering.

## 9. Relação com F2 — capacidade e headcount

F1-C05 existe para impedir que custo de pessoas desapareça da baseline. Porém, **F1 não dimensiona quadro, cargos, salários, regime de contratação ou datas de admissão**.

Esses parâmetros pertencem ao F2. Até lá:

- o custo de equipe permanece material e `TBD`;
- nenhum número de headcount será inferido a partir das metas de usuários;
- nenhum burn total poderá ser declarado completo sem resolver essa dependência.

## 10. Regra de fechamento mensal

Para cada mês deverá ser possível separar:

```text
subtotal com valores sustentados
+ linhas materiais TBD
= baseline mensal incompleta
```

Somente quando todas as linhas materiais do perímetro estiverem em `benchmark`, `quoted`, `contracted`, `actual` ou `not_applicable` devidamente evidenciado poderá existir:

```text
custo mensal candidato completo
→ burn candidato
→ ponte para caixa e runway
```

Taxas unitárias sem quantidade governada não compõem o subtotal mensal.

## 11. Gates para calibração numérica do F1

Cada pool somente poderá receber valor quando houver, no mínimo:

1. escopo e período definidos;
2. driver e unidade identificados;
3. comportamento de custo classificado;
4. fonte rastreável;
5. moeda, impostos e recorrência declarados quando aplicáveis;
6. estado de evidência atribuído;
7. owner funcional ou owner de validação definido;
8. distinção entre custo direto, compartilhado e corporativo;
9. ausência de dupla contagem entre produtos e áreas;
10. tratamento explícito de incerteza.

## 12. Resultado do F1 após F1-B

| Gate | Resultado |
|---|---|
| perímetro M0–M6 | PASS |
| separação M0–M3 / M4–M6 | PASS |
| categorias e pools materiais | PASS |
| comportamento e drivers iniciais | PASS |
| matriz mensal de ativação | PASS |
| fontes primárias de benchmark | PASS |
| pools com alguma calibração numérica | PARTIAL — 6/18 |
| pools numericamente fechados | 0/18 |
| cotações/contratos/realizados suficientes | PENDING |
| headcount e custo de equipe | BLOCKED BY F2 |
| custo mensal completo | NOT CALCULABLE |
| burn mensal completo | NOT CALCULABLE |
| runway e necessidade de capital | NOT CALCULABLE |

**Parecer:** `PARTIAL PASS — F1 structural baseline is active and F1-B added traceable unit benchmarks to six pools; material TBDs still prevent a complete M0–M6 cost baseline.`

## 13. Próximos incrementos permitidos

F1-B foi executado sem promover nenhum benchmark a orçamento, contrato ou realizado.

Os próximos atos são independentes e exigem autorização própria:

1. **F1-C — evidência e cotações faltantes**, para ampliar a cobertura externa de custos materiais;
2. **F2 — capacidade e headcount**, para dimensionar papéis, quantidade, regime e custo de pessoas M0–M6.

Burn, caixa, runway e necessidade de capital permanecem bloqueados até que as lacunas materiais de F1 e F2 estejam suficientemente resolvidas.
