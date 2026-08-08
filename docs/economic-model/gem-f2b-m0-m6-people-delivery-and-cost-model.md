---
id: GEM-F2B-M0-M6-PEOPLE-DELIVERY-COST-001
title: Modelo de Entrega e Custo de Pessoas M0–M6 — F2-B
status: active
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-08-08
parent: GEM-010
depends_on:
  - GEM-F2-M0-M6-CAPACITY-HEADCOUNT-BASELINE-001
  - GEM-F1-M0-M6-COST-BASELINE-001
  - GEM-F1B-M0-M6-COST-CALIBRATION-001
  - GEM-010-COST-AND-CAPACITY-MODEL-001
  - GTM-001
  - GTM-002
related:
  - GEM-008-COST-ARCHITECTURE-001
  - GEM-008-CAPACITY-AND-SATURATION-MODEL-001
  - GEM-009-CAPACITY-AND-QUALITY-METRICS-001
normative: true
---

# Modelo de Entrega e Custo de Pessoas M0–M6 — F2-B

## 1. Finalidade

Converter a baseline de capacidade do F2 em um **modelo governado de entrega e custo de pessoas para M0–M6**, sem transformar capacidade em contratação real e sem promover benchmark salarial a orçamento.

F2-B responde a cinco perguntas:

1. quais modos de entrega são economicamente admissíveis para cada tipo de cobertura;
2. como um role-equivalent deve ser convertido em custo somente quando houver owner, dedicação e regime definidos;
3. quais benchmarks externos podem servir de referência para os três RE dedicados já sustentados pelo GTM;
4. quais componentes trabalhistas conhecidos precisam aparecer em um cenário CLT sem que se invente um custo total;
5. quais lacunas ainda impedem calcular o custo mensal completo de `F1-C05`.

F2-B **não aprova contratação, salário, proposta de remuneração, regime trabalhista, pró-labore, comissão, benefícios, fornecedor, orçamento, burn, runway, necessidade de capital ou Product Engineering**.

## 2. Regra central: benchmark não é custo Guivos

O modelo separa explicitamente:

```text
capacidade necessária
→ papel / role-equivalent
→ modo de entrega candidato
→ benchmark de mercado ou cotação
→ quantidade/dedicação governada
→ componentes acessórios aplicáveis
→ custo candidato do papel
→ custo contratado ou realizado somente com evidência própria
```

Portanto:

- benchmark salarial não significa salário aprovado;
- salário de mercado não equivale a custo total do empregador;
- remuneração CLT não equivale a preço PJ/contractor;
- preço de prestador não pode ser derivado automaticamente de salário CLT;
- founder coverage não equivale a custo zero;
- uma pessoa cobrindo dois papéis não elimina o custo econômico nem prova capacidade sustentável;
- cobertura fracionária externa não deve ser duplicada em `F1-C05` quando o mesmo gasto já estiver governado em outro pool;
- comissão, bônus ou variável comercial permanecem fora do baseline até política própria.

## 3. Estados de calibração de pessoas

| Estado | Significado |
|---|---|
| `salary_benchmark_available` | existe benchmark salarial rastreável e comparável |
| `proxy_salary_benchmark` | existe benchmark de função adjacente, com comparabilidade limitada |
| `quote_required` | custo depende de proposta de prestador/serviço |
| `allocation_required` | existe custo-base, mas falta percentual de dedicação/rateio |
| `regime_required` | falta escolher o modo jurídico/econômico de entrega |
| `founder_compensation_TBD` | cobertura por fundador é possível, mas remuneração econômica/caixa não está definida |
| `blocked_by_product_engineering` | implementação não pode ser dimensionada antes da autoridade técnica |
| `TBD` | evidência insuficiente |

## 4. Modos de entrega e regra de custo

| Modo | Pode cobrir RE dedicado? | Regra econômica F2-B | Estado mínimo antes de entrar em burn candidato |
|---|---|---|---|
| `founder_or_internal` | sim | custo de caixa e custo econômico devem ser explicitados; nunca presumir R$ 0 | remuneração/pro-labore/compensação ou decisão documentada + período |
| `dedicated_internal_CLT` | sim | salário benchmark + componentes legais/benefícios aplicáveis | regime, salário candidato, enquadramento tributário/trabalhista e data |
| `shared_internal` | não como RE integral sem dedicação demonstrada | custo da pessoa × fração de dedicação governada | custo-base + allocation factor + capacidade remanescente |
| `contractor_PJ` | sim | preço contratado/cotado; benchmark salarial é apenas referência de mercado | cotação/proposta + impostos/escopo + dedicação + vigência |
| `external_specialist_fractional` | geralmente não | fee por hora/mês/evento; evitar dupla contagem com outros pools | cotação/contrato + unidade + volume |
| `partner_enabled` | não automaticamente | contrapartida econômica deve estar no relacionamento/parceria aplicável | acordo, valor/contrapartida e owner |
| `TBD` | não | sem custo calculável | decisão posterior |

F2-B não define qual desses modos será usado pela Guivos. O objetivo é tornar a decisão mensurável quando ela ocorrer.

## 5. Fontes públicas de benchmark recuperadas em 2026-08-08

### 5.1 Robert Half — Guia Salarial 2026

A Robert Half informa que suas projeções salariais são baseadas em remuneração real de profissionais conectados a empregadores no Brasil. Os percentis representam níveis crescentes de experiência e valor da pessoa na função.

Fontes utilizadas:

- Head of Growth (P/M), Belo Horizonte: `https://www.roberthalf.com/br/pt/vagas-detalhes/head-of-growth-pm/belo-horizonte`
- Executivo(a) de Contas (P/M), Brasil: `https://www.roberthalf.com/br/pt/vagas-detalhes/executivoa-de-contas-pm`
- Gerente Regional de Vendas (P/M), Brasil: `https://www.roberthalf.com/br/pt/vagas-detalhes/gerente-regional-de-vendas-pm`
- CRM/CX (P/M), Brasil: `https://www.roberthalf.com/br/pt/vagas-detalhes/crmcx-pm`

### 5.2 Fontes oficiais para componentes trabalhistas

- Receita Federal — contribuição patronal previdenciária: `https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/tributos/contribuicoes-previdenciarias-pj`
- Ministério do Trabalho e Emprego — FGTS: `https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/inspecao-do-trabalho/areas-de-atuacao/fgts-fundo-de-garantia-do-tempo-de-servico`
- Receita Federal — GILRAT: `https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/declaracoes-e-demonstrativos/revisao-de-declaracao-malha/pj-parametro-50.006`

Essas fontes não determinam o regime tributário, CNAE, FAP, benefícios, convenção coletiva ou demais componentes aplicáveis à Guivos.

## 6. Benchmarks dos três RE dedicados

Os três RE abaixo já existem no F2. F2-B adiciona somente **referências salariais de mercado**, sem afirmar que as descrições de cargo são equivalentes em todos os aspectos.

| RE | Papel F2 | Benchmark externo | P25 | P50 | P75 | Comparabilidade |
|---|---|---|---:|---:|---:|---|
| F2-R01 | liderança Growth/GTM | Head of Growth (P/M), Belo Horizonte | R$ 13.800 | R$ 19.950 | R$ 24.500 | alta para referência de mercado; escopo Guivos ainda precisa de descrição final |
| F2-R02 | comercial institucional + Guivos Business | Executivo(a) de Contas (P/M), Brasil | R$ 7.350 | R$ 10.600 | R$ 13.250 | média; benchmark comercial B2B, sem equivalência automática de senioridade |
| F2-R03 | ecossistema + Parcerias Estratégicas | Gerente Regional de Vendas (P/M), Brasil | R$ 11.750 | R$ 16.750 | R$ 21.100 | baixa/média; usado apenas como proxy relacional/comercial por ausência de benchmark específico de partnerships |

### Regras de leitura

1. os valores são **salário-base de referência de mercado**, não custo total;
2. não incluem bônus, comissão, benefícios, encargos, equipamentos, recrutamento ou despesas de trabalho;
3. R02 e R03 exigem validação de descrição/senioridade antes de qualquer decisão remuneratória;
4. R03 permanece `proxy_salary_benchmark`, não `salary_benchmark_available` pleno;
5. os benchmarks não autorizam que os três RE sejam executados por três pessoas diferentes.

## 7. Envelope de salário-equivalente dos três RE — teste analítico

Somente para testar ordem de grandeza, F2-B calcula um cenário artificial no qual os três RE são **separadamente remunerados em dedicação integral** pelos benchmarks acima.

| Cenário de benchmark | R01 | R02 | R03 proxy | Soma mensal de salário-equivalente |
|---|---:|---:|---:|---:|
| P25 | R$ 13.800 | R$ 7.350 | R$ 11.750 | **R$ 32.900** |
| P50 | R$ 19.950 | R$ 10.600 | R$ 16.750 | **R$ 47.300** |
| P75 | R$ 24.500 | R$ 13.250 | R$ 21.100 | **R$ 58.850** |

Este envelope é classificado como:

```yaml
artifact: three_RE_separate_role_salary_equivalent_stress_test
value_state: benchmark
planning_use: sensitivity_only
budget_authority: false
hiring_authority: false
headcount_assertion: false
burn_eligible: false
```

Ele **não** significa que a Guivos precisa pagar R$ 32,9 mil, R$ 47,3 mil ou R$ 58,85 mil por mês. O valor real poderá ser menor, maior ou estruturalmente diferente conforme founder coverage, sobreposição sustentável, regime, dedicação, senioridade, variável, terceirização e momento de ativação.

## 8. Camada CLT — componentes legais conhecidos e limite do cálculo

Para uma empresa/equiparado em regime no qual as regras gerais sejam aplicáveis, as fontes oficiais indicam, entre outros componentes:

- contribuição previdenciária patronal geral de **20%** sobre remunerações, sujeita a enquadramento e exceções legais/tributárias;
- depósito de **FGTS de 8%** do salário do empregado, em regra;
- **GILRAT de 1%, 2% ou 3%**, conforme atividade preponderante, antes de ajustes e adicionais aplicáveis.

A soma aritmética desses três componentes corresponde a uma sobreposição parcial de **29% a 31%** sobre a base salarial quando todos forem aplicáveis.

Essa faixa **não é um fator de custo CLT completo** e não poderá ser usada como multiplicador oficial da Guivos, pois ainda faltam, conforme o caso:

- enquadramento tributário e previdenciário;
- CNAE e atividade preponderante;
- FAP e terceiros;
- 13º salário e respectivos reflexos;
- férias e adicional constitucional;
- benefícios e política de trabalho;
- convenção/acordo coletivo;
- horas extras/adicionais;
- recrutamento, equipamento e onboarding;
- provisões e custos de desligamento;
- tratamento contábil e competência.

### Sensibilidade parcial — não custo total

Se a sobreposição parcial de 29%–31% fosse aplicada **apenas matematicamente** ao teste de três RE separados, sem considerar os itens acima, teríamos:

| Benchmark salarial | +29% parcial | +31% parcial |
|---|---:|---:|
| P25 — R$ 32.900 | R$ 42.441 | R$ 43.099 |
| P50 — R$ 47.300 | R$ 61.017 | R$ 61.963 |
| P75 — R$ 58.850 | R$ 75.916,50 | R$ 77.093,50 |

Estado obrigatório desse quadro:

`illustrative_partial_statutory_overlay — NOT full employer cost — NOT budget — NOT burn`.

## 9. Cobertura por fundador ou liderança existente

Quando um RE for coberto por fundador ou pessoa já existente:

```text
capacidade coberta
≠ novo headcount
≠ custo de caixa necessariamente novo
≠ custo econômico zero
```

F2-B exige registrar:

```yaml
role_id: F2-Rxx
coverage_person_or_scope: identified_or_TBD
cash_compensation_brl: amount_or_TBD
economic_opportunity_cost: documented_or_TBD
allocation_fraction: 0..1_or_TBD
capacity_conflict_check: pass | conditional | fail | TBD
period: M0..M6
```

R$ 0 em caixa somente poderá ser registrado quando existir decisão/evidência explícita para o período. Mesmo nesse caso, custo de oportunidade e risco de concentração devem permanecer visíveis.

## 10. Shared internal — fórmula de rateio

Para uma cobertura compartilhada:

```text
custo alocado do papel
= custo-base mensal da pessoa/recurso
× fração de dedicação governada ao papel
```

A fração de dedicação não poderá ser inventada a partir do número de responsabilidades. Deve ser sustentada por planejamento de capacidade ou observação real.

Exemplo estrutural, sem valores:

```yaml
capacity: F2-R06 suporte_atendimento
delivery_mode: shared_internal
base_monthly_people_cost_brl: TBD
allocation_fraction: TBD
allocated_cost_brl: TBD
capacity_status: not_assessed
```

## 11. Contractor/PJ — sem conversão automática de salário

Para `contractor_PJ`, a linha mínima é:

```yaml
role_id: F2-Rxx
scope: defined
monthly_fee_brl: quoted_or_contracted_or_TBD
taxes_included: yes | no | unknown
availability_fraction: defined_or_TBD
term: defined_or_TBD
termination_terms: defined_or_TBD
variable_compensation: defined_or_none_or_TBD
source: quote_or_contract
```

Regras:

- não aplicar fator arbitrário sobre salário CLT para estimar PJ;
- não presumir ausência de risco trabalhista;
- não presumir que preço mensal represente dedicação integral;
- comissão/variável comercial deve ser separada do fee fixo;
- somente cotação ou contrato identificável pode promover o valor além de `TBD`.

## 12. Especialistas fracionários e prevenção de dupla contagem

F2-R10, F2-R11 e F2-R12 podem ser entregues por especialista externo/fracionário.

A contabilização deverá respeitar o objeto econômico:

- contabilidade/fiscal normalmente permanece em `F1-C06`;
- jurídico/privacidade/compliance permanece em `F1-C06` quando contratado como serviço especializado;
- segurança/risco especializado pode permanecer em `F1-C04` quando fizer parte de serviço/controle de segurança;
- somente mão de obra individualizada que pertença economicamente ao pool de equipe deverá compor `F1-C05`.

O mesmo gasto nunca poderá aparecer simultaneamente em `F1-C05` e outro pool.

## 13. Shared coverage com benchmark auxiliar

Para suporte/Customer Success, existe benchmark 2026 de `CRM/CX (P/M)` nacional:

| Benchmark auxiliar | P25 | P50 | P75 |
|---|---:|---:|---:|
| CRM/CX (P/M), Brasil | R$ 4.350 | R$ 6.450 | R$ 7.900 |

Uso permitido:

- referência para dimensionamento futuro de F2-R06/F2-R07;
- somente após decisão de que uma função dedicada é necessária;
- não multiplicar por usuários, contratos ou entidades sem driver observado;
- não afirmar que suporte/CS já exige um HC adicional em M0–M6.

Estado: `auxiliary_salary_benchmark — allocation/activation required`.

## 14. Matriz F2-B por capacidade

| Capacidade | Estado de entrega após F2-B | Estado de custo após F2-B |
|---|---|---|
| F2-R01 Growth/GTM | modos admissíveis definidos | benchmark salarial BH disponível; regime/dedicação/custo real TBD |
| F2-R02 Comercial/Business | modos admissíveis definidos | benchmark comercial nacional disponível; regime/dedicação/custo real TBD |
| F2-R03 Ecossistema/Parcerias | modos admissíveis definidos | proxy salarial disponível; benchmark específico e custo real TBD |
| F2-R04 Conteúdo/marketing | shared/contractor | allocation/quote required |
| F2-R05 Operação/onboarding | founder/shared/contractor/partner | allocation/quote required |
| F2-R06 Suporte/atendimento | shared/contractor | benchmark auxiliar disponível; ativação/dedicação TBD |
| F2-R07 CS/implantação | shared/conditional | benchmark auxiliar disponível; driver por contas TBD |
| F2-R08 Moderação/trust & safety | shared/specialist/contractor | TBD/quote required |
| F2-R09 Finanças/admin | founder/shared/specialist | allocation/quote required |
| F2-R10 Contabilidade/fiscal | fractional specialist | calibrado parcialmente em F1-B/F1-C06; evitar dupla contagem |
| F2-R11 Jurídico/privacidade/compliance | fractional specialist | quote required em F1-C06 |
| F2-R12 Segurança/risco | fractional/shared | quote required em F1-C04 ou F1-C05 conforme objeto |
| F2-R13 Governança executiva | founder/internal | compensation/allocation TBD |
| F2-R14 Produto/design/UX documental | founder/shared/contractor | allocation/quote required |
| F2-R15 Engenharia implementação | bloqueado | blocked_by_product_engineering |
| F2-R16 Dados/IA implementação | bloqueado | blocked_by_product_engineering |
| F2-R17 Eventos/campo BH | event/shared | quote/event cost belongs to relevant F1 pool |
| F2-R18 Vendors/integrações | shared/specialist | allocation/quote required |

## 15. Relação com F1-C05

Após F2-B, `F1-C05 — equipe e serviços profissionais` evolui para:

> `partially_calibrated_by_F2B — delivery modes defined; salary benchmarks available for R01/R02, proxy for R03 and auxiliary CRM/CX benchmark; actual HC, overlap, regime, compensation, allocations, benefits and quotes remain TBD`.

Isso permite dizer que o custo de pessoas deixou de ser uma caixa conceitual vazia, mas **ainda não permite calcular o amount mensal completo**.

Para fechar F1-C05 ainda são necessários:

1. owner/cobertura real de cada RE e capacidade compartilhada;
2. sobreposição autorizada e sustentável entre papéis;
3. modo de entrega escolhido por papel;
4. quantidade real de pessoas/prestadores;
5. dedicação por papel e período;
6. remuneração/fee/cotação;
7. variável, comissão e benefícios quando aplicáveis;
8. enquadramento trabalhista/tributário para eventual CLT;
9. data de ativação e encerramento;
10. prevenção de dupla contagem com F1-C04/F1-C06/F1-C07/F1-C08/F1-C12/F1-C18.

## 16. Gate de custo de pessoas por mês

Um mês somente pode receber custo completo de pessoas quando:

```text
todos os RE/coberturas materiais do mês
→ owner identificado
→ modo de entrega definido
→ dedicação/quantidade definida
→ valor sustentado
→ custos acessórios aplicáveis classificados
→ dupla contagem eliminada
→ subtotal reconciliado
```

Se qualquer cobertura material permanecer `TBD`, o mês continua com `people_cost_incomplete`.

## 17. Resultado F2-B

| Gate | Resultado |
|---|---|
| modos de entrega formalizados | PASS |
| regras de founder/shared/CLT/PJ/fractional | PASS |
| benchmarks R01/R02 | PASS |
| proxy R03 | PARTIAL — proxy, não benchmark específico |
| benchmark auxiliar suporte/CS | PASS |
| componentes legais CLT mínimos identificados | PASS — parcial, não custo total |
| prevenção de dupla contagem | PASS |
| HC real | PENDING |
| regime por papel | PENDING |
| compensação/fee real | PENDING |
| allocation fractions | PENDING |
| benefícios/variável/comissão | PENDING |
| custo mensal completo F1-C05 | NOT CALCULABLE |
| burn completo M0–M6 | NOT CALCULABLE |
| runway/necessidade de capital | NOT CALCULABLE |

**Parecer:** `PARTIAL PASS — F2-B establishes delivery-mode economics and traceable people-cost benchmarks without converting role-equivalents into hires or market salary into Guivos budget; material allocation, regime and compensation decisions remain pending.`

## 18. Próximo incremento permitido

Após integração do F2-B, o programa deverá decidir separadamente entre:

1. **F2-C — assignment e dedicação M0–M6**, definindo quem cobre o quê, sobreposições e frações de capacidade sem contratar; ou
2. **F1-C — evidências/cotações dos pools materiais ainda pendentes**.

F3 — caixa, capital de giro e necessidade de capital continua bloqueado até que F1 e F2 possuam cobertura monetária material suficiente.
