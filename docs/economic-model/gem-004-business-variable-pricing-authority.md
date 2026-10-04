---
id: GEM-004-BUSINESS-VARIABLE-PRICING-AUTHORITY-001
title: Guivos Business — Autoridade de Pricing Variável para Configurador
status: active
version: 2.1.0
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

Este documento estabelece a tabela econômica vigente para tornar numericamente calculável a composição do Guivos Business, separando valor recorrente de plataforma, serviços pagos adicionais e recursos operacionais separados.

A composição permanece:

```text
CONTRATAÇÃO BUSINESS VÁLIDA
=
OFERTA BUSINESS OBRIGATÓRIA
+ TIER DE CAPACIDADE

ASSINATURA RECORRENTE / CONTRATUAL
=
PLANO / TIER DE CAPACIDADE
+ COMPONENTE DE POPULAÇÃO / ESCALA
+ ACESSOS JOURNEY CUSTEADOS, SE APLICÁVEL
+ CAPACIDADES ADICIONAIS
+ SERVIÇOS ADICIONAIS

RECURSO OPERACIONAL SEPARADO
=
ORÇAMENTO PRÉ-PAGO DE INCENTIVO
```

Os valores abaixo foram **adjudicados como autoridade econômica interna do configurador**. Eles não constituem, por si, oferta pública, autorização de cobrança, condição fiscal ou liberação de implementação.

## 2. Princípios econômicos

1. a **oferta Business contratada** é o objeto econômico primário da contratação;
2. não existe contratação Business ativa sem pelo menos uma oferta: Programas de Incentivo, Journey custeado ou ambas;
3. o plano/tier remunera a camada de capacidade da plataforma necessária para operar a oferta selecionada;
4. a seleção da oferta **não gera taxa recorrente adicional de ativação**;
5. população/escala remunera volume elegível crescente com preço marginal decrescente;
6. Journey custeado é precificado por acesso efetivamente financiado;
7. add-ons só são cobrados quando a capacidade não estiver incluída no entitlement do plano;
8. serviços pagos adicionais remuneram participação humana/operacional contratada depois do tier e não determinam o tier por si só;
9. orçamento de incentivo é recurso operacional do cliente e não se mistura à assinatura;
10. o anual usa, como regra adjudicada, aproximadamente 10 mensalidades para componentes tabelados;
11. Scale e Enterprise podem substituir partes da tabela por condições dimensionadas quando a configuração exigir dimensionamento conforme os entitlements vigentes; o modelo de implementação/operação não determina esse enquadramento por si só.

## 3. Plano-base

| Plano | Mensal | Anual | Regra |
|---|---:|---:|---|
| **Start** | R$ 299,00 | R$ 2.990,00 | baseline vigente |
| **Growth** | R$ 799,00 | R$ 7.990,00 | baseline vigente |
| **Scale** | a partir de R$ 1.990,00 | dimensionado | referência mínima vigente |
| **Enterprise** | sob consulta | sob consulta | dimensionamento obrigatório |

Os valores do tier continuam sendo a remuneração da capacidade da plataforma, mas **o tier não é contratável isoladamente**. Uma contratação Business válida exige pelo menos uma oferta Business selecionada.

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

## 5. Oferta Business obrigatória — sem taxa de ativação

A oferta é o objeto econômico primário da contratação Business. Pelo menos uma oferta deve estar selecionada para que exista uma contratação Business válida.

| Oferta Business | Taxa mensal de ativação | Taxa anual de ativação | Regra |
|---|---:|---:|---|
| **Programas de Incentivo** | **R$ 0,00** | **R$ 0,00** | operado dentro do tier contratado; orçamento de incentivo continua separado |
| **Journey custeado** | **R$ 0,00** | **R$ 0,00** | operado dentro do tier contratado; acessos financiados são cobrados separadamente |
| **Incentivos + Journey** | **R$ 0,00** | **R$ 0,00** | combinação permitida sem taxa adicional de habilitação |

```text
SEM OFERTA BUSINESS
→ SEM CONTRATAÇÃO BUSINESS ATIVA

OFERTA SELECIONADA
→ DETERMINA O OBJETO DA CONTRATAÇÃO
→ NÃO ADICIONA TAXA DE ATIVAÇÃO

TIER
→ REMUNERA CAPACIDADE DA PLATAFORMA
→ NÃO É OFERTA AUTÔNOMA
```

A seleção da oferta pode influenciar o tier necessário conforme capacidades, escala e requisitos, mas não adiciona uma segunda assinatura pela simples habilitação da oferta.

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

## 8. Modelo de implementação/operação e serviços pagos adicionais

O modelo de implementação/operação é definido somente depois do tier resultante. `Self-service` é uma modalidade operacional com autonomia e **não é um serviço adicional tarifado**.

| Serviço pago adicional | Mensal | Anual | Regra |
|---|---:|---:|---|
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
VALID_CONFIGURATION
=
REQUIRED_BUSINESS_OFFER(offer)

PLATFORM_RECURRING_VALUE
=
BASE(plan, periodicity)
+
PROGRESSIVE_POPULATION(population, periodicity)
+
JOURNEY_PLUS_RATE(volume, periodicity) × plus_accesses
+
JOURNEY_PRO_RATE(volume, periodicity) × pro_accesses
+
SUM(ADDONS_NOT_INCLUDED_IN_PLAN)

FINAL_CONTRACT_VALUE
=
PLATFORM_RECURRING_VALUE
+
SUM(PAID_ADDITIONAL_SERVICES, IF CONTRACTED)
```

Separadamente:

```text
CONTRACT_CHECKOUT_TOTAL
=
FINAL_CONTRACT_VALUE
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
MODELO DE IMPLEMENTAÇÃO / OPERAÇÃO = SELF-SERVICE
```

Cálculo mensal:

- plano-base: R$ 299,00;
- primeiros 50 elegíveis: incluídos;
- 70 × R$ 1,49 = R$ 104,30;
- Programas de Incentivo: oferta obrigatória selecionada, **R$ 0,00 de taxa de ativação**;
- total recorrente adjudicado: **R$ 403,30/mês**;
- orçamento de incentivo: separado.

### Exemplo B — operação com Journey custeado

```text
GROWTH
POPULAÇÃO ELEGÍVEL = 300
OFERTA = JOURNEY
JOURNEY PLUS = 100 ACESSOS
MODELO DE IMPLEMENTAÇÃO / OPERAÇÃO = SELF-SERVICE
```

Cálculo mensal:

- plano-base: R$ 799,00;
- faixa 51–250: 200 × R$ 1,49 = R$ 298,00;
- faixa 251–300: 50 × R$ 0,99 = R$ 49,50;
- Journey custeado: oferta obrigatória selecionada, **R$ 0,00 de taxa de ativação**;
- 100 acessos Plus × R$ 17,90 = R$ 1.790,00;
- total recorrente adjudicado: **R$ 2.936,50/mês**.

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

BUSINESS OFFER SELECTION
→ REQUIRED
→ ACTIVATION FEE = ZERO

TIER PRICE
≠ OFFER ACTIVATION FEE

JOURNEY ACCESS FEE
≠ OFFER ACTIVATION FEE

INCENTIVE PROGRAM FEE
≠ INCENTIVE BUDGET

SERVICE LEVEL
≠ PLAN CAPABILITY
```

A mesma unidade econômica não pode ser faturada duas vezes sob rótulos diferentes.

### Matriz de inclusões e contratação por tier

A matriz abaixo governa simultaneamente **o que já está incluído no plano** e **quanto custa contratar a capacidade quando ela não está incluída**.

| Capacidade | Start | Growth | Scale | Enterprise |
|---|---|---|---|---|
| **Intelligence avançado** | R$ 299/mês · R$ 2.990/ano | **incluído — R$ 0 adicional** | **incluído — R$ 0 adicional** | **incluído — R$ 0 adicional** |
| **Exportações automatizadas / Power BI** | R$ 249/mês · R$ 2.490/ano | R$ 249/mês · R$ 2.490/ano | **incluído — R$ 0 adicional** | **incluído — R$ 0 adicional** |
| **API Business** | R$ 399/mês · R$ 3.990/ano | R$ 399/mês · R$ 3.990/ano | **incluído — R$ 0 adicional** | **incluído — R$ 0 adicional** |
| **SSO / SAML** | R$ 299/mês · R$ 2.990/ano | R$ 299/mês · R$ 2.990/ano | **incluído — R$ 0 adicional** | **incluído — R$ 0 adicional** |
| **Governança / auditoria avançadas** | R$ 249/mês · R$ 2.490/ano | **incluído — R$ 0 adicional** | **incluído — R$ 0 adicional** | **incluído — R$ 0 adicional** |
| **1 integração dedicada** | R$ 490/mês · R$ 4.900/ano | R$ 490/mês · R$ 4.900/ano | **1 incluída — R$ 0 adicional** | **incluída conforme contrato** |
| **Integração dedicada adicional** | R$ 490/mês · R$ 4.900/ano por integração | R$ 490/mês · R$ 4.900/ano por integração | R$ 490/mês · R$ 4.900/ano por integração além da 1ª incluída | dimensionado conforme contrato |

Regras:

```text
INCLUÍDO NO TIER
→ R$ 0,00 ADICIONAL

NÃO INCLUÍDO + ELEGÍVEL COMO ADD-ON
→ APLICAR VALOR DA CAPACIDADE

INTEGRAÇÃO DEDICADA
→ R$ 490/MÊS
→ R$ 4.900/ANO
→ POR INTEGRAÇÃO COBRÁVEL

ENTERPRISE
→ PREVALECE DIMENSIONAMENTO CONTRATUAL
```

A inclusão de uma capacidade no tier não significa que ela seja gratuita universalmente; significa que seu preço já está absorvido pelo plano-base contratado.


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
