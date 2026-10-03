---
id: GEM-004-BUSINESS-VARIABLE-PRICING-AUTHORITY-001
title: Guivos Business — Autoridade de Pricing Variável para Configurador
status: active
version: 1.0.0
owner: Guivos Economic Model
last_updated: 2026-10-03
normative: true
maturity: adjudicated_economic_authority
depends_on:
  - GEM-004-A1
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GKR-PLANS-BUSINESS-001
  - GKR-UX-PLANS-BUSINESS-CONFIGURATOR-001
related:
  - GEM-010-A1
  - GEM-005-INCENTIVE-LAYER-ARCHITECTURE-001
---

# Guivos Business — Autoridade de Pricing Variável para Configurador

## 1. Finalidade

Este documento estabelece a tabela econômica vigente para tornar numericamente calculável a composição Self-service do Guivos Business.

A composição permanece:

```text
ASSINATURA RECORRENTE / CONTRATUAL
=
PLANO-BASE
+ COMPONENTE DE POPULAÇÃO / ESCALA
+ COMPONENTE DE OFERTA
+ ACESSOS JOURNEY CUSTEADOS
+ CAPACIDADES ADICIONAIS
+ SERVIÇOS ADICIONAIS

RECURSO OPERACIONAL SEPARADO
=
ORÇAMENTO PRÉ-PAGO DE INCENTIVO
```

Os valores abaixo foram **adjudicados como autoridade econômica interna do configurador**. Eles não constituem, por si, oferta pública, autorização de cobrança, condição fiscal ou liberação de implementação.

## 2. Princípios econômicos

1. o plano-base remunera a camada de capacidade do produto;
2. população/escala remunera volume elegível crescente com preço marginal decrescente;
3. oferta remunera a ativação funcional de Incentivos, Journey custeado ou ambos;
4. Journey custeado é precificado por acesso efetivamente financiado;
5. add-ons só são cobrados quando a capacidade não estiver incluída no entitlement do plano;
6. serviços adicionais remuneram participação humana/operacional acima do Self-service;
7. orçamento de incentivo é recurso operacional do cliente e não se mistura à assinatura;
8. o anual usa, como regra adjudicada, aproximadamente 10 mensalidades para componentes tabelados;
9. Scale e Enterprise podem substituir partes da tabela por condições dimensionadas quando a configuração ultrapassar o Self-service elegível.

## 3. Plano-base

| Plano | Mensal | Anual | Regra |
|---|---:|---:|---|
| **Start** | R$ 299,00 | R$ 2.990,00 | baseline vigente |
| **Growth** | R$ 799,00 | R$ 7.990,00 | baseline vigente |
| **Scale** | a partir de R$ 1.990,00 | dimensionado | referência mínima vigente |
| **Enterprise** | sob consulta | sob consulta | dimensionamento obrigatório |

A tabela variável não altera os preços-base já registrados.

## 4. Componente de população / escala

### 4.1 Base precificável

A base precificável adjudicada é a **população elegível para a configuração contratada**, não necessariamente toda a folha da empresa.

A cobrança é progressiva por faixa.

| Faixa da população elegível | Mensal por pessoa na faixa | Anual por pessoa na faixa |
|---|---:|---:|
| 1–50 | incluído | incluído |
| 51–250 | R$ 1,49 | R$ 14,90 |
| 251–1.000 | R$ 0,99 | R$ 9,90 |
| 1.001–5.000 | R$ 0,69 | R$ 6,90 |
| 5.001–20.000 | R$ 0,49 | R$ 4,90 |
| acima de 20.000 | dimensionado | dimensionado |

Regra:

```text
POPULATION_COMPONENT
=
SOMA DAS PESSOAS EM CADA FAIXA × TARIFA DA FAIXA
```

A cobrança progressiva evita salto artificial ao mudar de faixa.

## 5. Componente de oferta

| Oferta Business | Mensal | Anual | Observação |
|---|---:|---:|---|
| **Programas de Incentivo** | R$ 199,00 | R$ 1.990,00 | habilita operação de programas; orçamento de recompensa continua separado |
| **Journey custeado** | R$ 99,00 | R$ 990,00 | habilita gestão empresarial dos acessos; licenças são cobradas separadamente |
| **Incentivos + Journey** | R$ 249,00 | R$ 2.490,00 | composição conjunta; substitui a soma das duas taxas de oferta |

A seleção de oferta não muda por si só o plano-base. O plano continua determinado pela maior capacidade necessária da configuração.

## 6. Acessos Journey custeados

### 6.1 Journey Plus custeado

| Acessos custeados | Mensal por acesso | Anual por acesso |
|---|---:|---:|
| 1–99 | R$ 19,90 | R$ 199,00 |
| 100–499 | R$ 17,90 | R$ 179,00 |
| 500–1.999 | R$ 15,90 | R$ 159,00 |
| 2.000+ | R$ 13,90 | R$ 139,00 |

### 6.2 Journey Pro custeado

| Acessos custeados | Mensal por acesso | Anual por acesso |
|---|---:|---:|
| 1–99 | R$ 39,90 | R$ 399,00 |
| 100–499 | R$ 35,90 | R$ 359,00 |
| 500–1.999 | R$ 31,90 | R$ 319,00 |
| 2.000+ | R$ 27,90 | R$ 279,00 |

A faixa é determinada pela quantidade total de acessos custeados daquela modalidade no contrato.

```text
JOURNEY_ACCESS_COMPONENT
=
ACESSOS PLUS × RATE_PLUS
+
ACESSOS PRO × RATE_PRO
```

O acesso financiado pela empresa não transfere à empresa autoridade indevida sobre o contexto individual da Pessoa.

## 7. Capacidades adicionais

Cobrar somente quando a capacidade não estiver incluída no entitlement do plano contratado.

| Capacidade adicional | Mensal | Anual | Unidade |
|---|---:|---:|---|
| **Intelligence avançado** | R$ 299,00 | R$ 2.990,00 | por contrato |
| **Exportações automatizadas / conector Power BI** | R$ 249,00 | R$ 2.490,00 | por contrato |
| **API Business** | R$ 399,00 | R$ 3.990,00 | por contrato |
| **SSO / SAML** | R$ 299,00 | R$ 2.990,00 | por contrato |
| **Governança e trilha de auditoria avançadas** | R$ 249,00 | R$ 2.490,00 | por contrato |
| **Integração dedicada adicional** | R$ 490,00 | R$ 4.900,00 | por integração |

Regras:

- nenhuma capacidade é cobrada duas vezes;
- se o plano já incluir a capacidade, seu preço adicional é R$ 0,00;
- integração customizada com projeto específico pode exigir setup separado e dimensionamento.

## 8. Serviços adicionais

Self-service permanece a operação padrão sem taxa adicional de serviço.

| Modelo / serviço adicional | Mensal | Anual | Regra |
|---|---:|---:|---|
| **Self-service** | R$ 0,00 | R$ 0,00 | operação autônoma |
| **Suporte ampliado** | R$ 299,00 | R$ 2.990,00 | acompanhamento acima do suporte padrão do plano |
| **Operação gerenciada** | R$ 990,00 | R$ 9.900,00 | participação operacional recorrente da Guivos |
| **Gestão dedicada / SLA ampliado** | R$ 1.990,00 | R$ 19.900,00 | atendimento dedicado e governança ampliada |
| **Projeto de implantação customizada** | sob consulta | sob consulta | cobrança não recorrente ou contratual própria |

Serviço adicional não define automaticamente o plano-base.

## 9. Orçamento pré-pago de incentivo

O orçamento de incentivo é informado pela empresa e exibido em linha separada.

```text
INCENTIVE_BUDGET
→ PREPAID
→ CUSTOMER-FUNDED
→ SEPARATE FROM SUBSCRIPTION
```

Tabela adjudicada:

| Item | Valor |
|---|---:|
| Orçamento de incentivo | definido pela empresa |
| Impacto na assinatura recorrente | R$ 0,00 |
| Incorporação automática à receita de assinatura | não |
| Uso | somente conforme regras do programa e saldo disponível |

Nenhum markup, taxa de resgate, spread, expiração econômica ou valor mínimo de recarga é criado por esta tabela. Esses elementos exigem autoridade própria se vierem a existir.

## 10. Regra anual

Para componentes tabelados neste documento:

```text
ANUAL
≈ 10 × COMPONENTE MENSAL
```

Isso preserva a lógica comercial já usada nos planos Start/Growth e nos planos de Pessoa.

A regra não se aplica automaticamente a itens “dimensionados” ou “sob consulta”.

## 11. Fórmula calculável adjudicada

```text
RECURRING_TOTAL
=
BASE(plan, periodicity)
+
PROGRESSIVE_POPULATION(population, periodicity)
+
OFFER_RATE(offer, periodicity)
+
JOURNEY_PLUS_RATE(volume, periodicity) × plus_accesses
+
JOURNEY_PRO_RATE(volume, periodicity) × pro_accesses
+
SUM(ADDONS_NOT_INCLUDED_IN_PLAN)
+
SERVICE_RATE(service_model, periodicity)
```

Separadamente:

```text
CONTRACT_CHECKOUT_TOTAL
=
RECURRING_TOTAL
+
INCENTIVE_BUDGET_PREPAID
+
ONE_TIME_ITEMS, IF ANY
```

O checkout deve distinguir claramente recorrência, pré-pagamento operacional e itens únicos.

## 12. Exemplos de teste da calculadora

### Exemplo A — operação inicial

```text
START
POPULAÇÃO ELEGÍVEL = 120
OFERTA = INCENTIVOS
JOURNEY = 0
ADD-ONS = 0
SERVIÇO = SELF-SERVICE
```

Cálculo mensal:

- plano-base: R$ 299,00;
- primeiros 50 elegíveis: incluídos;
- 70 × R$ 1,49 = R$ 104,30;
- oferta Incentivos: R$ 199,00;
- total recorrente adjudicado: **R$ 602,30/mês**;
- orçamento de incentivo: separado.

### Exemplo B — operação com Journey custeado

```text
GROWTH
POPULAÇÃO ELEGÍVEL = 300
OFERTA = JOURNEY
JOURNEY PLUS = 100 ACESSOS
SERVIÇO = SELF-SERVICE
```

Cálculo mensal:

- plano-base: R$ 799,00;
- faixa 51–250: 200 × R$ 1,49 = R$ 298,00;
- faixa 251–300: 50 × R$ 0,99 = R$ 49,50;
- oferta Journey: R$ 99,00;
- 100 acessos Plus × R$ 17,90 = R$ 1.790,00;
- total recorrente adjudicado: **R$ 3.035,50/mês**.

### Exemplo C — composição ampliada

```text
SCALE
POPULAÇÃO ELEGÍVEL = 1.500
OFERTA = INCENTIVOS + JOURNEY
JOURNEY PRO = 250 ACESSOS
ADD-ONS = API + SSO
SERVIÇO = OPERAÇÃO GERENCIADA
```

O configurador pode calcular as parcelas tabeladas, mas o preço-base final de Scale continua sujeito ao dimensionamento aplicável. Portanto, o resultado deve ser exibido como **subtotal conhecido + componente Scale dimensionado**, e não como total final definitivo.

## 13. Proteções contra dupla cobrança

```text
PLAN ENTITLEMENT INCLUDED
→ ADD-ON PRICE = ZERO

POPULATION ELIGIBLE
≠ JOURNEY FUNDED ACCESS

OFFER ENABLEMENT
≠ JOURNEY LICENSE

INCENTIVE PROGRAM FEE
≠ INCENTIVE BUDGET

SERVICE LEVEL
≠ PLAN CAPABILITY
```

A mesma unidade econômica não pode ser faturada duas vezes sob rótulos diferentes.

### 14.1 Inclusões mínimas por plano

A regra de entitlement para as capacidades adicionais desta autoridade é:

| Capacidade | Start | Growth | Scale | Enterprise |
|---|---|---|---|---|
| Intelligence avançado | adicional | **incluído** | **incluído** | **incluído** |
| Exportações automatizadas / Power BI | adicional | adicional | **incluído** | **incluído** |
| API Business | adicional | adicional | **incluído** | **incluído** |
| SSO / SAML | adicional | adicional | **incluído** | **incluído** |
| Governança e trilha de auditoria avançadas | adicional | **incluído** | **incluído** | **incluído** |
| 1 integração dedicada | adicional | adicional | **incluída** | **incluída conforme contrato** |
| Integrações dedicadas adicionais | adicional | adicional | R$ 490/mês por integração adicional | dimensionado conforme contrato |

Regras obrigatórias:

```text
CAPACIDADE INCLUÍDA NO TIER
→ ADD-ON = R$ 0,00

CAPACIDADE NÃO INCLUÍDA
→ PODE SER ADD-ON, SE TECNICAMENTE/COMERCIALMENTE ELEGÍVEL

ENTITLEMENT DE PLANO
≠ SERVIÇO OPERACIONAL

ENTERPRISE
→ CAPACIDADES DIMENSIONADAS NO CONTRATO
→ NÃO AUTORIZA DUPLA COBRANÇA
```

### 14.2 Serviços

Serviços de implementação/operação permanecem separados dos entitlements acima.

- Start, Growth, Scale e Enterprise podem operar em Self-service quando elegíveis;
- suporte ampliado, operação gerenciada e gestão dedicada/SLA ampliado só geram cobrança adicional quando **não estiverem expressamente incorporados ao contrato**;
- Enterprise não transforma automaticamente gestão dedicada em item separado: o contrato deve declarar se está incluída ou adicional.

## 15. Estado adjudicado

```text
BUSINESS VARIABLE PRICING TABLE
→ ADJUDICATED
→ ACTIVE / NORMATIVE
→ ECONOMIC AUTHORITY

FULL NUMERIC CONFIGURATOR
→ ECONOMICALLY SPECIFIABLE
→ IMPLEMENTATION NOT RELEASED

PUBLIC OFFER
→ NOT AUTHORIZED

CHARGING
→ NOT AUTHORIZED
```

## 16. Próximo gate

Esta autoridade econômica está congelada para consumo documental. Próximos atos exigem gates próprios para:

- implementação do configurador;
- checkout/cobrança;
- tributação;
- contrato/termos;
- oferta pública;
- validação de disposição a pagar e unit economics.


## 14. Entitlements por tier e proteção contra dupla cobrança

```text
BUSINESS VARIABLE PRICING TABLE
→ MATERIALIZED AS CANDIDATE
→ NOT ADJUDICATED
→ NOT NORMATIVE

FULL NUMERIC CONFIGURATOR
→ ECONOMICALLY SPECIFIABLE
→ NOT YET RELEASED

PUBLIC OFFER
→ NOT AUTHORIZED

CHARGING
→ NOT AUTHORIZED
```

