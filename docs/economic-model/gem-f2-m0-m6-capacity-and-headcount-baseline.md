---
id: GEM-F2-M0-M6-CAPACITY-HEADCOUNT-BASELINE-001
title: Baseline de Capacidade, Papéis e Headcount M0–M6 — F2
status: active
version: 0.2.0
owner: Guivos Economic Model
last_updated: 2026-08-08
parent: GEM-010
depends_on:
  - GEM-F1-M0-M6-COST-BASELINE-001
  - GEM-F1B-M0-M6-COST-CALIBRATION-001
  - GEM-008-CAPACITY-AND-SATURATION-MODEL-001
  - GEM-008-GROWTH-AND-CAPACITY-GATES-001
  - GEM-009-CAPACITY-AND-QUALITY-METRICS-001
  - GEM-010-OPERATING-DRIVER-MODEL-001
  - GTM-001
  - GTM-002
related:
  - GEM-F2B-M0-M6-PEOPLE-DELIVERY-COST-001
  - GEM-010-COST-AND-CAPACITY-MODEL-001
  - GEM-008-COST-ARCHITECTURE-001
normative: true
---

# Baseline de Capacidade, Papéis e Headcount M0–M6 — F2

## 1. Finalidade

Definir a primeira baseline governada de **capacidade humana e cobertura funcional** para `M0–M6`, conectando o desenho de lançamento de Belo Horizonte aos gates de capacidade do GKR e ao pool `F1-C05 — equipe e serviços profissionais`.

F2 responde a quatro perguntas:

1. quais capacidades precisam estar cobertas antes e durante o lançamento;
2. quais funções exigem dedicação identificável;
3. quais coberturas podem ser compartilhadas, fracionárias ou externas;
4. quais capacidades continuam bloqueadas por decisões posteriores.

F2 **não aprova contratação, vínculo trabalhista, salário, fornecedor, orçamento, organograma definitivo, Product Engineering, burn, runway ou necessidade de capital**.

## 2. Regra central: capacidade não é headcount

O GKR separa explicitamente:

- **capacidade funcional** — responsabilidade que precisa ser efetivamente coberta;
- **papel** — conjunto coerente de responsabilidades;
- **role-equivalent (RE)** — unidade de planejamento para uma função com dedicação identificável;
- **headcount (HC)** — número de pessoas físicas vinculadas à organização;
- **contratação** — decisão jurídica/econômica sobre quem executará o papel;
- **custo de pessoas** — resultado posterior de regime, quantidade, remuneração, encargos e serviços contratados.

Consequências:

- `1 RE` não significa automaticamente `1 empregado`;
- uma pessoa pode cobrir mais de um papel somente quando a capacidade e a qualidade permanecerem sustentáveis;
- uma função compartilhada pode ser executada por pessoa interna, fundador, prestador, parceiro ou serviço externo, conforme governança posterior;
- cobertura externa/fracionária não deve ser somada mecanicamente ao HC interno;
- ausência de contratação não elimina a obrigação de cobertura funcional.

## 3. Estados de cobertura

| Estado | Significado |
|---|---|
| `dedicated_role_equivalent` | a função requer uma unidade de dedicação identificável no planejamento |
| `shared_must_cover` | capacidade obrigatória, mas pode ser compartilhada entre papéis/recursos |
| `fractional_specialist` | cobertura especializada pode ser fracionária/externa |
| `conditional_on_launch` | torna-se obrigatória quando o gate/atividade correspondente é ativado |
| `conditional_on_volume` | reforço depende de demanda, backlog, contratos ou risco observados |
| `blocked_by_product_engineering` | capacidade de implementação depende de reativação formal de Product Engineering |
| `not_required_in_baseline` | não é requerida no perímetro M0–M6 vigente |
| `TBD` | cobertura ainda não suficientemente governada |

## 4. Modos de entrega possíveis

Os modos abaixo são **alternativas de cobertura**, não decisões de contratação:

- `founder_or_internal`;
- `dedicated_internal`;
- `shared_internal`;
- `contractor`;
- `external_specialist`;
- `partner_enabled`;
- `TBD`.

Nenhum modo possui custo aprovado nesta autoridade. A modelagem econômica detalhada desses modos é governada por [F2-B — Modelo de Entrega e Custo de Pessoas M0–M6](gem-f2b-m0-m6-people-delivery-and-cost-model.md).

## 5. Base explícita do GTM para M0–M6

O GTM-002 já define a equipe de referência por estágio e declara que se trata de **desenho funcional, não autorização de contratação**.

Para M0–M6, a base explícita é:

1. liderança de Growth/GTM;
2. 1 função comercial institucional/B2B;
3. 1 função ecossistema/parcerias estratégicas;
4. suporte compartilhado de conteúdo/marketing e operação.

Portanto, o único piso quantitativo diretamente sustentado pelo GTM nesta etapa é:

> **3 role-equivalents dedicados de referência**, correspondentes às três primeiras funções acima, mais coberturas compartilhadas necessárias.

Esse piso é **capacidade funcional planejada**, não headcount contratado ou existente.

## 6. Baseline de capacidades M0–M6

| ID | Capacidade | M0–M3 | M4–M6 | Unidade de planejamento | Modo admissível | Origem/gate |
|---|---|---|---|---|---|---|
| F2-R01 | liderança Growth/GTM | dedicated_role_equivalent | dedicated_role_equivalent | 1 RE | founder_or_internal / dedicated_internal / contractor | GTM-002 |
| F2-R02 | comercial institucional + Guivos Business | dedicated_role_equivalent | dedicated_role_equivalent | 1 RE | dedicated_internal / contractor | GTM-002 |
| F2-R03 | ecossistema + Parcerias Estratégicas | dedicated_role_equivalent | dedicated_role_equivalent | 1 RE | dedicated_internal / contractor | GTM-002 |
| F2-R04 | conteúdo e marketing | shared_must_cover | shared_must_cover | shared | shared_internal / contractor | GTM-002; lançamento |
| F2-R05 | operação local, onboarding e ativação BH | shared_must_cover | shared_must_cover | shared | founder_or_internal / shared_internal / contractor / partner_enabled | GTM-001/002 |
| F2-R06 | suporte e atendimento | shared_must_cover | shared_must_cover | shared; reforço condicional | shared_internal / contractor | gates de capacidade e qualidade |
| F2-R07 | Customer Success / implantação institucional | conditional_on_contract | conditional_on_launch | shared; reforço por contas | R02/R05/shared/TBD | contratos Business/Organizações |
| F2-R08 | moderação, curadoria, trust & safety e fraude | shared_must_cover | shared_must_cover | shared; reforço por volume/risco | shared_internal / external_specialist / contractor | GEM-008/009 |
| F2-R09 | finanças, administração e controles | shared_must_cover | shared_must_cover | shared/fractional | founder_or_internal / shared_internal / external_specialist | C-02/governança |
| F2-R10 | contabilidade e fiscal | fractional_specialist | fractional_specialist | fractional | external_specialist | F1-C06 |
| F2-R11 | jurídico, privacidade e compliance | fractional_specialist | fractional_specialist | fractional | external_specialist | privacy/legal gates |
| F2-R12 | segurança e risco especializado | fractional_specialist | fractional_specialist | fractional | external_specialist / shared_internal | gates de segurança |
| F2-R13 | governança executiva e decisões de escopo | shared_must_cover | shared_must_cover | shared | founder_or_internal | governance gate |
| F2-R14 | produto/design/UX — coordenação documental | shared_must_cover | shared_must_cover | shared | founder_or_internal / shared_internal / contractor | documentação vigente |
| F2-R15 | engenharia/plataforma — implementação | blocked_by_product_engineering | blocked_by_product_engineering | TBD | TBD | Product Engineering pausado antes de W0-01 |
| F2-R16 | dados/IA/analytics — implementação | blocked_by_product_engineering | blocked_by_product_engineering | TBD | TBD | implementação depende de autoridade técnica |
| F2-R17 | eventos/presença de campo BH | conditional_on_launch | conditional_on_launch | event/shared | contractor / partner_enabled / shared_internal | F1-C12 / GTM local |
| F2-R18 | compras/vendors/integrações operacionais | conditional_on_activity | conditional_on_activity | shared | shared_internal / external_specialist | F1-C18 |

### Normalização dos estados condicionais

Nesta tabela:

- `conditional_on_contract` é uma especialização de `conditional_on_volume` acionada por contrato elegível;
- `conditional_on_activity` é uma especialização de `conditional_on_launch`/`conditional_on_volume` acionada pela atividade correspondente.

Essas especializações não autorizam contratação.

## 7. Piso de capacidade dedicada

### M0–M3

O piso governado é:

```text
3 RE dedicados de referência
+ conteúdo/marketing compartilhado
+ operação/onboarding compartilhados
+ suporte/qualidade compartilhados
+ coberturas especialistas fracionárias necessárias
+ governança compartilhada
```

### M4–M6

O piso permanece em **3 RE dedicados de referência**, porém a carga operacional aumenta por:

- lançamento para Pessoas;
- onboarding de Coletivos e Organizações;
- contratos Guivos Business;
- Parcerias Estratégicas ativas;
- suporte, atendimento, moderação e risco;
- conteúdo e aquisição;
- possível presença de campo.

Consequentemente, M4–M6 exige que as coberturas compartilhadas tenham capacidade demonstrável. O simples fato de manter 3 RE não comprova prontidão para lançamento.

## 8. Headcount governado nesta versão

F2 **não fixa um HC total** porque o GTM permite suporte compartilhado e os gates protetivos podem ser cobertos de diferentes formas.

O que pode ser afirmado é:

| Métrica | Estado F2 |
|---|---|
| funções dedicadas explicitamente sustentadas pelo GTM | 3 RE |
| HC interno contratado necessário | TBD |
| quantidade de prestadores | TBD |
| quantidade de especialistas fracionários | TBD |
| conteúdo/marketing | cobertura compartilhada obrigatória; HC TBD |
| operação/onboarding | cobertura compartilhada obrigatória; HC TBD |
| suporte/CS | capacidade obrigatória; dedicação cresce por volume/contratos |
| engenharia de implementação | bloqueada por Product Engineering |
| dados/IA de implementação | bloqueada por Product Engineering |

Portanto, **“3 RE” não deve ser publicado como “equipe de 3 pessoas”**.

## 9. Matriz mensal de cobertura

Legenda:

- `D` — RE dedicado de referência;
- `S` — cobertura compartilhada obrigatória;
- `F` — especialista fracionário/externo;
- `C` — condicional a atividade/volume;
- `B` — bloqueado por Product Engineering.

| Capacidade | M0 | M1 | M2 | M3 | M4 | M5 | M6 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Growth/GTM | D | D | D | D | D | D | D |
| Comercial institucional/B2B | D | D | D | D | D | D | D |
| Ecossistema/Parcerias | D | D | D | D | D | D | D |
| Conteúdo/marketing | S | S | S | S | S | S | S |
| Operação/onboarding BH | S | S | S | S | S | S | S |
| Suporte/atendimento | S | S | S | S | S | S | S |
| CS/implantação institucional | C | C | C | C | S | S | S |
| Moderação/curadoria/fraude | S | S | S | S | S | S | S |
| Finanças/admin | S | S | S | S | S | S | S |
| Contabilidade/fiscal | F | F | F | F | F | F | F |
| Jurídico/privacidade/compliance | F | F | F | F | F | F | F |
| Segurança/risco especializado | F | F | F | F | F | F | F |
| Governança executiva | S | S | S | S | S | S | S |
| Produto/design/UX documental | S | S | S | S | S | S | S |
| Engenharia de implementação | B | B | B | B | B | B | B |
| Dados/IA de implementação | B | B | B | B | B | B | B |
| Eventos/campo BH | C | C | C | C | C | C | C |
| Vendors/integrações operacionais | C | C | C | C | C | C | C |

A matriz define **obrigação de cobertura**, não número de indivíduos.

## 10. Drivers de reforço de capacidade

Coberturas compartilhadas deverão ser reforçadas antes de saturação quando sinais materiais ocorrerem.

### Comercial e ecossistema

- pipeline qualificado sem follow-up dentro da cadência;
- backlog de discovery/propostas;
- perda de oportunidades por falta de owner;
- concentração crítica em uma única pessoa;
- incompatibilidade entre volume comercial e onboarding.

### Operação, onboarding e CS

- entidades aguardando ativação;
- contratos sem capacidade de implantação;
- backlog fora do prazo;
- reaberturas e retrabalho recorrentes;
- deterioração de satisfação ou sucesso inicial.

### Suporte, moderação e trust & safety

- aumento recorrente de filas/tempo de resposta;
- incidentes/reclamações não tratados;
- moderação insuficiente;
- contestação/fraude sem owner;
- sobrecarga humana ou redução de controles protetivos.

### Especialistas

- obrigação legal/regulatória nova;
- mudança de tratamento de dados;
- contrato ou campanha que altere risco;
- incidente material;
- entrada em atividade que exija revisão especializada.

F2 não fixa thresholds numéricos sem dados observados. O primeiro ciclo real deverá instrumentar utilização, folga operacional, backlog saudável, tempo de resposta e sinais de saturação.

## 11. Gate de prontidão M4

A passagem de preparação para lançamento não depende apenas do calendário. Antes de M4, devem estar cobertos e com owner identificável:

1. Growth/GTM;
2. comercial institucional/B2B;
3. ecossistema/parcerias;
4. conteúdo/marketing;
5. operação/onboarding;
6. suporte/atendimento;
7. moderação/curadoria/trust & safety;
8. finanças/admin;
9. jurídico/privacidade/compliance aplicável;
10. segurança/risco aplicável;
11. governança executiva.

Se uma cobertura essencial estiver `unavailable`, `constrained`, `saturated` ou sem owner, o gate de crescimento deverá ser condicionado, limitado, pausado ou bloqueado conforme a autoridade GEM-008.

## 12. Relação com F1-C05 — custo de equipe

Após F2 e F2-B, o estado de `F1-C05` é:

> `partially_calibrated_by_F2B — 3 dedicated role-equivalents of reference plus mandatory shared/fractional/conditional coverage; delivery modes and salary benchmarks are governed, while actual HC, assignment, overlap, regime, compensation, allocation and complete amount remain TBD`.

F2-B adiciona:

- modos econômicos de entrega;
- benchmarks rastreáveis de Growth/GTM e comercial B2B;
- proxy limitado para ecossistema/parcerias;
- benchmark auxiliar de CRM/CX para eventual reforço de suporte/CS;
- componentes trabalhistas oficiais mínimos e guardrails contra multiplicador CLT incompleto;
- prevenção de dupla contagem com outros pools.

Ainda faltam para converter F1-C05 em custo mensal completo:

- decisão de quem cobre cada papel;
- sobreposição admissível entre papéis;
- vínculo/regime de execução por papel;
- quantidade efetiva de pessoas/prestadores;
- dedicação/rateio por período;
- remuneração ou preço do serviço aplicável;
- encargos, benefícios, impostos e custos acessórios quando aplicáveis;
- datas de início/fim;
- capacidade real observada.

## 13. O que F2 não autoriza

F2 e F2-B não autorizam:

- contratar 3 pessoas;
- contratar 18 pessoas;
- afirmar que a Guivos possui atualmente qualquer uma dessas funções contratadas;
- definir salários ou propostas de remuneração;
- escolher CLT, PJ, contractor ou outsourcing;
- transformar benchmark em orçamento;
- criar vagas;
- iniciar Product Engineering;
- contratar Neo4j, cloud, IA ou stack;
- operar um produto ainda não implementado;
- calcular burn completo;
- calcular runway ou capital necessário.

## 14. Resultado F2 após F2-B

| Gate | Resultado |
|---|---|
| capacidades M0–M6 inventariadas | PASS |
| base explícita do GTM preservada | PASS |
| piso de RE dedicados | PASS — 3 RE de referência |
| coberturas compartilhadas/protetivas | PASS |
| separação capacidade × HC × contratação | PASS |
| matriz mensal de cobertura | PASS |
| drivers de reforço/saturação | PASS |
| modos de entrega econômicos | PASS — F2-B |
| benchmarks de remuneração | PARTIAL PASS — R01/R02 + proxy R03 + auxiliar CRM/CX |
| HC interno total | PENDING |
| assignment/sobreposição/dedicação | PENDING |
| regime por papel | PENDING |
| remuneração/fee real por papel | PENDING |
| engenharia de implementação | BLOCKED BY PRODUCT ENGINEERING |
| custo mensal completo F1-C05 | NOT CALCULABLE |
| burn/runway/capital | NOT CALCULABLE |

**Parecer:** `PARTIAL PASS — M0–M6 functional capacity, delivery-mode economics and traceable people benchmarks are governed; exact assignment, headcount, overlap, regimes, allocations, compensation and complete monetary people cost remain pending.`

## 15. Próximo incremento econômico permitido

Após F2-B, o próximo incremento econômico-financeiro deverá escolher explicitamente entre:

1. **F2-C — assignment e dedicação M0–M6**, definindo quem cobre o quê, sobreposições e frações de capacidade sem contratar; ou
2. **F1-C — completar evidências/cotações materiais ainda faltantes**.

Somente depois de F1 e F2 terem cobertura monetária material suficiente deverá o programa avançar para **F3 — caixa, capital de giro e necessidade de capital**.
