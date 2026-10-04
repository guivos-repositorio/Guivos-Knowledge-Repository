---
id: GKR-UX-PLANS-BUSINESS-CONFIGURATOR-001
title: Planos — Guivos Business — Configurador, Capacidades e Pricing — Documento Mestre
status: active
version: 0.8.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: false
depends_on:
  - GKR-PLANS-BUSINESS-001
  - GPA-004-FUNCTIONAL-PORTFOLIO-001
  - GEM-004-A1
  - GEM-004-BUSINESS-VARIABLE-PRICING-AUTHORITY-001
---

# Planos — Guivos Business — Configurador, Capacidades e Pricing — Documento Mestre

## 1. Finalidade

Definir a experiência pela qual uma empresa pode **compreender, configurar, estimar quando houver autoridade de preço e contratar online** o Guivos Business.

O configurador é uma experiência de composição. Ele não é um quinto plano.

## 2. Tiers de capacidade resultantes

| Plano | Mensal | Anual | Direção |
|---|---:|---:|---|
| **Start** | R$ 299,00 | R$ 2.990,00 | operar |
| **Growth** | R$ 799,00 | R$ 7.990,00 | acompanhar e compreender |
| **Scale** | a partir de R$ 1.990,00 | dimensionado | interpretar e integrar em escala |
| **Enterprise** | sob consulta | sob consulta | governar alta complexidade e escala |

Todos admitem seleção Mensal ou Anual. Quando o valor não estiver numericamente congelado, a calculadora não deve inventá-lo.

### 2.1 Como o tier é determinado

```text
OFERTA ESCOLHIDA
+
ESCALA
+
CAPACIDADES
+
INTEGRAÇÕES
+
GOVERNANÇA / SEGURANÇA
↓
TIER COMPATÍVEL

DEPOIS
→ MODELO DE IMPLEMENTAÇÃO / OPERAÇÃO
→ SELF-SERVICE / SUPORTE / GERENCIADO
```

A empresa não precisa escolher Start, Growth, Scale ou Enterprise antes de informar sua necessidade. O configurador deve **enquadrar e explicar** o tier compatível.


## 3. Dados de preenchimento

A composição deve conseguir receber, conforme aplicável:

### Empresa e escala

- população total da empresa;
- população elegível para a configuração;
- quantidade prevista de participantes;
- quantidade de acessos Journey custeados;
- quantidade de unidades/filiais, quando relevante.

### Oferta

- Programas de Incentivo;
- Guivos Journey custeado;
- ambas.

### Capacidades

A superfície deve listar **todas as capacidades governadas**, cada uma com decisão explícita **Incluir / Não incluir**:

- Intelligence avançado;
- Exportações automatizadas / Power BI;
- API Business;
- SSO / SAML;
- Governança / auditoria avançadas;
- Integração dedicada;
- Integrações dedicadas adicionais.

Para cada capacidade selecionada, a interface deve mostrar se ela já está incluída no tier resultante, gera add-on, exige reenquadramento ou exige dimensionamento.

### Governança / segurança

- requisitos de governança;
- auditoria;
- autenticação corporativa;
- segurança e controle aplicáveis.

### Modelo de implementação / operação — etapa posterior

Somente depois do tier resultante:

- Self-service;
- apoio do suporte;
- gerenciado.

### Periodicidade

- mensal;
- anual.

### Recursos operacionais

- orçamento pré-pago de incentivo, quando aplicável.

## 4. Modelo de composição

```text
CONFIGURAÇÃO VÁLIDA
=
OFERTA BUSINESS OBRIGATÓRIA
+ TIER DE CAPACIDADE

VALOR RECORRENTE DE PLATAFORMA
=
TIER DE CAPACIDADE
+ COMPONENTE DE POPULAÇÃO / ESCALA
+ ACESSOS JOURNEY CUSTEADOS, SE APLICÁVEL
+ CAPACIDADES ADICIONAIS

DEPOIS

VALOR CONTRATUAL FINAL
=
VALOR RECORRENTE DE PLATAFORMA
+ SERVIÇOS PAGOS ADICIONAIS, SE CONTRATADOS

RECURSO OPERACIONAL SEPARADO
=
ORÇAMENTO PRÉ-PAGO DE INCENTIVO
```

O orçamento de incentivo deve ser exibido separadamente e nunca mascarado como assinatura.

## 5. Regra da calculadora

A calculadora deve trabalhar com uma tabela econômica versionada e não com números hardcoded pela interface.

```text
REQUIRE_BUSINESS_OFFER(oferta)
+
BASE(periodicidade, tier)
+
POPULATION_RATE(periodicidade, faixa_autorizada) × base_precificável
+
JOURNEY_ACCESS_RATE(periodicidade) × acessos
+
ADDONS(periodicidade)
=
VALOR RECORRENTE DE PLATAFORMA CALCULÁVEL

DEPOIS
+
SERVICE_RATE(periodicidade, modelo_operacional), SE HOUVER SERVIÇO ADICIONAL CONTRATADO
=
VALOR CONTRATUAL FINAL
```

Cada termo só pode produzir número quando houver autoridade econômica correspondente.

## 6. Preço por população

O modelo usa as faixas e tarifas populacionais adjudicadas em `GEM-004-BUSINESS-VARIABLE-PRICING-AUTHORITY-001`.

A calculadora deve aplicar cobrança progressiva por faixa e exibir separadamente cada parcela. Acima de 20.000 elegíveis ou quando Scale/Enterprise exigir dimensionamento, deve exibir o componente como dimensionado em vez de inventar valor.

## 7. Produtos e ofertas

O configurador deve exigir pelo menos uma oferta Business. Programas de Incentivo, Journey custeado e a combinação de ambos possuem taxa de ativação igual a R$ 0,00; o impacto econômico decorre do tier, da escala, dos acessos Journey e dos demais componentes aplicáveis.

As taxas de Programas de Incentivo, Journey custeado e composição conjunta são governadas pela autoridade econômica vigente. Itens futuros não formalizados continuam sem cifra.


## 7.1 Tabela de referência para consumo da superfície

A interface deve consumir a autoridade econômica, não duplicar lógica hardcoded. Para legibilidade funcional, os principais valores vigentes são:

### População / escala

| Faixa | Mensal por pessoa | Anual por pessoa |
|---|---:|---:|
| 1–50 | incluído | incluído |
| 51–250 | R$ 1,49 | R$ 14,90 |
| 251–1.000 | R$ 0,99 | R$ 9,90 |
| 1.001–5.000 | R$ 0,69 | R$ 6,90 |
| 5.001–20.000 | R$ 0,49 | R$ 4,90 |
| 20.000+ | dimensionado | dimensionado |

### Ofertas

| Oferta | Mensal | Anual |
|---|---:|---:|
| Incentivos | R$ 0,00 | R$ 0,00 |
| Journey custeado | R$ 0,00 | R$ 0,00 |
| Incentivos + Journey | R$ 0,00 | R$ 0,00 |

### Modelo de implementação/operação e serviços pagos

O modelo é escolhido depois do tier resultante:

- Self-service;
- apoio do suporte;
- gerenciado.

`Self-service` não é um serviço adicional tarifado.

| Serviço pago adicional | Mensal | Anual |
|---|---:|---:|
| Suporte ampliado | R$ 299,00 | R$ 2.990,00 |
| Operação gerenciada | R$ 990,00 | R$ 9.900,00 |
| Gestão dedicada / SLA ampliado | R$ 1.990,00 | R$ 19.900,00 |
| Implantação customizada | sob consulta | sob consulta |

Os preços por acesso Journey e add-ons devem igualmente vir da autoridade econômica vigente.

## 7.2 Matriz calculável de capacidade por tier

A superfície deve consumir a seguinte matriz comercial:

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

A inclusão de uma capacidade no tier não significa que ela seja gratuita universalmente; significa que seu preço já está absorvido pelo tier de capacidade resultante.


### Regra de cálculo

```text
IF CAPABILITY INCLUDED IN PLAN
→ CAPABILITY_CHARGE = 0

ELSE IF CAPABILITY HAS AUTHORIZED ADDON PRICE
→ CAPABILITY_CHARGE = AUTHORIZED PRICE

ELSE
→ REQUIRE DIMENSIONING / HIGHER PLAN
```

A interface deve exibir a capacidade incluída com valor adicional zero, e não ocultá-la como se ela não tivesse valor econômico.


## 7.3 Progressão de capacidade por tier

| Dimensão | **Start** | **Growth** | **Scale** | **Enterprise** |
|---|---|---|---|---|
| **Direção** | Operar | Acompanhar e compreender | Interpretar e integrar | Governar alta complexidade e escala |
| **Intelligence avançado** | adicional | incluído | incluído | incluído |
| **Governança / auditoria avançadas** | adicional | incluído | incluído | incluído |
| **Exportações / Power BI** | adicional | adicional | incluído | incluído |
| **API Business** | adicional | adicional | incluído | incluído |
| **SSO / SAML** | adicional | adicional | incluído | incluído |
| **1 integração dedicada** | adicional | adicional | 1 incluída | conforme contrato |

A superfície deve explicar a progressão como mudança de capacidade, e não apenas como diferença de preço.

## 7.4 Regra universal de incluir / não incluir

A superfície de capacidades não deve presumir que a empresa deseja determinada capacidade apenas porque ela está disponível ou incluída em um tier.

Cada capacidade deve possuir:

```text
INCLUIR
OU
NÃO INCLUIR
```

| Escolha | Condição | Efeito |
|---|---|---|
| Não incluir | qualquer tier | capacidade não compõe a configuração |
| Incluir | já incluída no tier | valor adicional zero |
| Incluir | não incluída + preço autorizado | add-on |
| Incluir | exige tier superior | reenquadrar e explicar |
| Incluir | exige dimensionamento | marcar como dimensionado / sob consulta |

Essa regra vale inclusive para capacidades que um tier superior oferece sem valor adicional. **Disponibilidade não equivale a seleção automática.**

## 8. Resultado

Quando todos os componentes necessários possuírem preço vigente, o resultado deve mostrar primeiro a oferta Business escolhida e a configuração informada; depois, o tier resultante e a justificativa do enquadramento; em seguida, população/escala, acessos Journey e capacidades adicionais que formam o **valor recorrente de plataforma**; somente depois, modelo de implementação/operação e eventual serviço pago adicional que compõe o **valor contratual final**. O orçamento de incentivo permanece em linha separada.

## 9. Configuração parcialmente calculável

Uma composição pode ser parcialmente calculável.

```text
SCALE / ENTERPRISE
→ BASE OU COMPONENTE PODE EXIGIR DIMENSIONAMENTO

POPULAÇÃO ATÉ 20.000
→ TAXAS TABELADAS DISPONÍVEIS

JOURNEY CUSTEADO
→ TAXAS PLUS / PRO TABELADAS DISPONÍVEIS

ITEM SOB CONSULTA
→ NÃO INVENTAR VALOR

TOTAL
→ CALCULAR SOMENTE PARCELAS NUMÉRICAS VIGENTES
```

A interface pode mostrar a parcela conhecida e indicar claramente o que falta para o total.

## 10. Enquadramento de plano

O tier compatível deve ser determinado depois da seleção da oferta e pela maior capacidade exigida pela configuração e pelos entitlements vigentes. Sem oferta Business selecionada, a configuração não é contratável.

A calculadora não pode elevar plano com base apenas em maximização de receita.

## 11. Self-service

Self-service é uma modalidade posterior de implementação/operação na qual a empresa segue com autonomia quando elegível. Suporte e Gerenciado são modalidades alternativas de implementação/operação. Nenhuma delas determina automaticamente Start, Growth, Scale ou Enterprise.

## 12. Estados

- composição vazia;
- composição em preenchimento;
- composição válida;
- preço total calculável;
- preço parcialmente calculável;
- item sob consulta;
- plano incompatível com capacidade solicitada;
- revisão antes de contratação;
- erro recuperável.

## 13. Autonomia e transparência

A superfície deve explicar **por que** um componente altera o valor. Não deve esconder taxa variável dentro de um total opaco.

## 14. Critérios de aceite

O configurador é aceitável quando Start/Growth/Scale/Enterprise permanecem intactos; Mensal/Anual é selecionável; população e ofertas podem compor a contratação; valores variáveis consomem a autoridade econômica vigente; orçamento de incentivo fica separado; total não é inventado; Self-service não vira plano; Organização não é confundida com Business; Design mantém liberdade criativa; e Product Engineering não é liberado por este Master.

## 15. Autoridade econômica corrente

A tabela econômica corrente é `GEM-004-BUSINESS-VARIABLE-PRICING-AUTHORITY-001`, que governa faixas populacionais, ofertas, acessos Journey, add-ons, serviços e regra anual dos componentes tabelados. O configurador deve também consumir a matriz de inclusões por tier para impedir dupla cobrança.

```text
ECONOMIC AUTHORITY
→ ADJUDICATED / NORMATIVE

FULL NUMERIC CONFIGURATOR
→ ECONOMICALLY SPECIFIABLE

IMPLEMENTATION
→ NOT RELEASED

PUBLIC OFFER / CHARGING
→ NOT AUTHORIZED
```
