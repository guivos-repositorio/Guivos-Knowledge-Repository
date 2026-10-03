---
id: GEM-F1-M0-M6-COST-BASELINE-001
title: Baseline de Custos M0–M6 — F1
status: active
version: 0.5.0
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
  - GEM-F1C-M0-M6-EVIDENCE-QUOTE-PACK-001
  - GEM-F2-M0-M6-CAPACITY-HEADCOUNT-BASELINE-001
  - GEM-F2B-M0-M6-PEOPLE-DELIVERY-COST-001
  - GEM-F2C-M0-M6-ASSIGNMENT-DEDICATION-001
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

F1-B pode registrar uma **taxa unitária benchmark** ou fórmula variável enquanto `amount_brl` permanece `TBD`. F1-C pode ampliar evidência pública e estruturar pacotes de cotação sem promover benchmark a orçamento. F2-B pode registrar benchmarks salariais e sensibilidades de pessoas enquanto regime, dedicação e amount real permanecem `TBD`. O valor mensal somente nasce quando quantidade, aplicabilidade e período estiverem suficientemente governados.

## 6. Catálogo mestre de pools M0–M6

| ID | Categoria | Pool de custo | Comportamento inicial | Driver principal | Estado numérico |
|---|---|---|---|---|---|
| F1-C01 | C-02 | produto, desenvolvimento, QA e entrega técnica | fixo/step | escopo implementável e releases autorizados | blocked_by_engineering |
| F1-C02 | C-02 | infraestrutura, hospedagem, armazenamento e observabilidade | semivariável/step | ambientes, tráfego, armazenamento e disponibilidade | blocked_by_engineering |
| F1-C03 | C-01/C-02 | IA, processamento, mensageria e serviços de dados | variável/step | uso elegível e volume processado | blocked_by_engineering |
| F1-C04 | C-04 | segurança, privacidade e controles técnicos | fixo/step | superfície, risco e requisitos aprovados | parcialmente calibrado; endpoint benchmark + quote required para controles especializados |
| F1-C05 | C-02 | equipe e serviços profissionais | fixo/step | capacidade e papéis requeridos | partially_parameterized_by_F2B_F2C; amount TBD |
| F1-C06 | C-02/C-04 | jurídico, contábil, fiscal, administrativo e compliance | fixo/event | obrigações, contratos e gates de lançamento | parcialmente calibrado; jurídico/privacy/compliance quote required |
| F1-C07 | C-02 | marca, conteúdo e produção criativa | fixo/event | calendário de conteúdo e lançamento | parcialmente calibrado; ferramenta criativa benchmark + produção quote required |
| F1-C08 | C-03 | CRM, vendas e Customer Success | fixo/step | pipeline institucional e contas ativas | parcialmente calibrado por benchmark |
| F1-C09 | C-03/C-06 | prospecção, reuniões, deslocamentos e operação comercial local | variável/event | reuniões, pilotos e parceiros em BH | parcialmente calibrado; transporte coletivo BH benchmark |
| F1-C10 | C-03/C-06 | onboarding de Coletivos, Organizações, parceiros e ativação comunitária | variável/step | entidades ativadas e suporte de implantação | scope_definition_required |
| F1-C11 | C-03 | mídia paga e performance | variável | aquisição incremental validada | budget_decision_and_experiment_required |
| F1-C12 | C-03 | lançamento, eventos e presença de campo em BH | event | ações de lançamento autorizadas | parcialmente calibrado; ticketing condicional + quote required |
| F1-C13 | C-01 | meios de pagamento e cobrança | variável | volume financeiro elegível e transações | fórmula benchmark disponível; amount TBD |
| F1-C14 | C-05 | reembolsos, chargebacks, disputas e perdas operacionais | contingent/variable | transações e incidentes | tarifa parcial benchmark; incidência TBD |
| F1-C15 | C-04 | suporte, moderação, curadoria e prevenção de fraude | semivariável/step | usuários, entidades, casos e conteúdo | parcialmente calibrado; help desk benchmark + serviço especializado quote required |
| F1-C16 | C-02 | domínios, marca, propriedade intelectual e ativos institucionais | fixed/event | ativos efetivamente mantidos ou protegidos | INPI + domínio .br com tarifas públicas parciais; quantidade/honorários TBD |
| F1-C17 | C-02 | espaço físico, coworking, equipamentos e infraestrutura administrativa | fixed/event | decisão operacional explícita | benchmark BH disponível; necessidade TBD |
| F1-C18 | C-06 | integrações, coordenação e reconciliação entre produtos/parceiros | variable/step | integrações e relações efetivamente ativadas | scope_definition_required |

A calibração pública inicial é governada por `GEM-F1B-M0-M6-COST-CALIBRATION-001`. A expansão de evidência e os pacotes de cotação são governados por `GEM-F1C-M0-M6-EVIDENCE-QUOTE-PACK-001`. A capacidade de pessoas é governada por `GEM-F2-M0-M6-CAPACITY-HEADCOUNT-BASELINE-001`, os modos econômicos por `GEM-F2B-M0-M6-PEOPLE-DELIVERY-COST-001` e assignment/dedicação por `GEM-F2C-M0-M6-ASSIGNMENT-DEDICATION-001`.

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
| F1-C05 Equipe/serviços profissionais | R | R | R | R | R | R | R |
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
- mantém F1-C01, F1-C02 e F1-C03 `blocked_by_engineering` até decisão técnica e evidência de custo compatíveis com os gates de Product Engineering.

## 9. Relação com F2/F2-B/F2-C — capacidade, entrega e custo de pessoas

F2 definiu a baseline de cobertura funcional M0–M6 sem transformar capacidade em contratação. F2-B adicionou modos de entrega e benchmarks rastreáveis sem transformar benchmark em remuneração aprovada. F2-C adicionou owner scopes, regras de sobreposição e bandas candidatas de dedicação sem nomear pessoas ou transformar allocation em HC.

O estado vigente é:

- 3 role-equivalents dedicados de referência: Growth/GTM, comercial institucional/B2B e ecossistema/parcerias;
- conteúdo/marketing, operação/onboarding, suporte, governança e demais capacidades essenciais possuem cobertura compartilhada ou condicional governada;
- contabilidade/fiscal, jurídico/privacidade/compliance e segurança/risco podem ser coberturas especialistas fracionárias;
- engenharia e dados/IA de implementação permanecem bloqueados por Product Engineering;
- benchmark salarial 2026 de Growth/GTM em BH e comercial B2B nacional estão disponíveis;
- ecossistema/parcerias possui apenas proxy salarial de comparabilidade limitada;
- suporte/CS possui benchmark auxiliar de CRM/CX, sem ativação automática de HC;
- owner scopes existem para as 18 capacidades e os três RE possuem guardrails candidatos de dedicação;
- HC interno total, resource assignment nominal, regime, fração mensal exata, remuneração/fee e custo monetário mensal continuam `TBD`.

Consequentemente, F1-C05 está **partially_parameterized_by_F2B_F2C**, mas não numericamente fechado.

O teste de salário-equivalente de três RE separados do F2-B é sensibilidade analítica e não poderá ser publicado como equipe, orçamento, burn ou necessidade de capital. O envelope de 0,60 RE-equivalent do F2-C é capacidade secundária de planejamento e não headcount.

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

Taxas unitárias e benchmarks salariais sem quantidade, dedicação e regime governados não compõem o subtotal mensal.

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

## 12. Resultado do F1 após F1-B, F1-C, F2, F2-B e F2-C

| Gate | Resultado |
|---|---|
| perímetro M0–M6 | PASS |
| separação M0–M3 / M4–M6 | PASS |
| categorias e pools materiais | PASS |
| comportamento e drivers iniciais | PASS |
| matriz mensal de ativação | PASS |
| fontes primárias de benchmark | PASS |
| pools com alguma calibração numérica | PARTIAL — 12/18 |
| pools numericamente fechados | 0/18 |
| pacotes de cotação material | PASS — F1-C |
| cotações/contratos/realizados suficientes | PENDING |
| capacidade e papéis de equipe | PARTIAL PASS — F2 |
| modos de entrega e benchmarks de pessoas | PARTIAL PASS — F2-B |
| assignment e dedicação | PARTIAL PASS — F2-C |
| HC interno/regime/resource assignment/remuneração | PENDING |
| custo monetário completo F1-C05 | NOT CALCULABLE |
| custo mensal completo | NOT CALCULABLE |
| burn mensal completo | NOT CALCULABLE |
| runway e necessidade de capital | NOT CALCULABLE |

**Parecer:** `PARTIAL PASS — F1/F1-B/F1-C/F2/F2-B/F2-C now govern cost scope, twelve pools with traceable numeric evidence, quote-ready external scopes, functional capacity, people-delivery economics and assignment guardrails; material scope, quantity, quotations, resource assignment and monetary gaps still prevent a complete cost and burn baseline.`

## 13. Próximo incremento permitido

Após integração do F1-C, o próximo ato recomendado é uma **reconciliação F1/F2 de prontidão para F3**, classificando os `TBD` remanescentes por materialidade e decidindo se F3 pode começar apenas como estrutura ou se deve aguardar mais evidência.

Essa reconciliação exige autorização própria e **não autoriza F3 automaticamente**. Burn, caixa, runway e necessidade de capital continuam bloqueados até que as lacunas materiais sejam suficientemente resolvidas.