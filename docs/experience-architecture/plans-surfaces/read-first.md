---
id: GKR-UX-PLANS-READ-FIRST-001
title: Planos — Superfícies e Fluxos — Leia Primeiro
status: active
version: 0.7.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: false
depends_on:
  - GKR-PLANS-INDEX-001
  - GEM-004-A1
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GEM-004-BUSINESS-VARIABLE-PRICING-AUTHORITY-001
---

# Planos — Superfícies e Fluxos — Leia Primeiro

## 1. Finalidade

Esta coleção organiza a experiência de **compreensão, comparação, composição e contratação de planos** para Pessoa, Coletivo, Organização e Guivos Business.

Ela existe para orientar Design, IA, Produto e Engenharia sem transformar documentos comerciais em prescrição visual.

## 2. O que esta coleção deve tornar explícito

Toda superfície de planos deve permitir compreender, conforme o contexto:

- quais planos existem;
- qual é a finalidade de cada plano;
- quais capacidades estão incluídas;
- quais limites diferenciam os planos;
- o que muda ao subir ou reduzir de plano;
- preço mensal e preço anual, quando numericamente definidos;
- quando o preço depende de dimensionamento;
- quais componentes são assinatura, adicionais, volume ou recurso operacional separado;
- qual ação apenas compara e qual ação inicia contratação;
- como permanecer no plano atual ou sair da comparação sem efeito comercial.

## 3. Domínios separados

```text
PESSOA
→ Free · Plus · Pro

COLETIVO
→ Livre · Mobiliza · Impacta · Rede

ORGANIZAÇÃO
→ Conecta · Eleva · Transforma

GUIVOS BUSINESS
→ Start · Growth · Scale · Enterprise
```

As quatro taxonomias não devem ser misturadas.

```text
ORGANIZAÇÃO
≠ GUIVOS BUSINESS
```

## 4. Periodicidade

A decisão corrente é:

```text
PLANOS PAGOS
→ CONTRATAÇÃO MENSAL OU ANUAL
```

Quando o valor de uma periodicidade ainda não estiver numericamente congelado, a superfície deve indicar **dimensionado** ou **sob consulta**, sem calcular desconto, preço ou economia por inferência.

## 5. Fontes

- `plans/person.md` — Pessoa;
- `plans/collectives.md` — Coletivos;
- `plans/organizations.md` — Organizações;
- `plans/business.md` — Guivos Business;
- `GEM-004-A1` — baseline econômica normativa;
- `PER-301` — comparação autenticada da Pessoa.

## 6. Regra de consumo

```text
VERDADE ECONÔMICA / FUNCIONAL
→ DOCUMENTO DE PLANO E AUTORIDADE ECONÔMICA

SIGNIFICADO, ESTADOS E CONTINUIDADE DA SUPERFÍCIE
→ ESTA COLEÇÃO

COMPOSIÇÃO VISUAL
→ DESIGN
```

## 7. Liberdade de Design

A coleção não impõe grid, card, tabela, cores, tipografia, ordem visual rígida, motion ou componente específico. O Design deve preservar significado, legibilidade, acessibilidade e autonomia de decisão.

## 8. Proibição de invenção comercial

Design, IA e Engenharia não podem inventar ou substituir a autoridade vigente de:

- preço;
- desconto;
- faixa populacional;
- preço por pessoa;
- pacote;
- entitlement;
- promoção;
- trial;
- imposto;
- SLA;
- regra de proration;
- meio de pagamento;
- recomendação automática de plano.

## 9. Guivos Business

Business possui configurador Self-service próprio. Ele deve exigir uma **oferta Business obrigatória** antes de concluir a composição. Sem Programas de Incentivo, Journey custeado ou ambas, não existe contratação Business ativa. Depois da oferta, a experiência enquadra tier, população/escala, acessos, capacidades, periodicidade e serviços aplicáveis.

Os preços variáveis do Business estão adjudicados em `GEM-004-BUSINESS-VARIABLE-PRICING-AUTHORITY-001`. A oferta obrigatória possui **taxa de ativação igual a R$ 0,00**; o tier remunera a capacidade da plataforma. O configurador calcula população/escala, acessos Journey, add-ons e serviços, consome a **matriz de inclusões por tier** e indica `dimensionado` ou `sob consulta` somente onde a autoridade assim determinar.

## 9.1 Composição econômica Business corrente

Toda superfície Business deve partir da seguinte verdade econômica:

```text
SEM OFERTA BUSINESS
→ SEM CONTRATAÇÃO BUSINESS ATIVA

OFERTA BUSINESS
→ OBRIGATÓRIA
→ TAXA DE ATIVAÇÃO = R$ 0,00

VALOR RECORRENTE
=
TIER DE CAPACIDADE
+ POPULAÇÃO / ESCALA
+ ACESSOS JOURNEY CUSTEADOS, SE APLICÁVEL
+ CAPACIDADES ADICIONAIS NÃO INCLUÍDAS NO TIER
+ SERVIÇOS ADICIONAIS
```

### Ordem semântica da contratação Business

```text
1. ESCOLHER O QUE QUER CONTRATAR
   → INCENTIVOS
   → JOURNEY
   → OU AMBOS

2. INFORMAR A CONFIGURAÇÃO
   → ESCALA
   → CAPACIDADES
   → INTEGRAÇÕES
   → GOVERNANÇA / SEGURANÇA

3. ENQUADRAR O TIER COMPATÍVEL
   → START
   → GROWTH
   → SCALE
   → ENTERPRISE

4. CALCULAR A COMPOSIÇÃO ECONÔMICA

5. DEPOIS DEFINIR MODELO DE IMPLEMENTAÇÃO / OPERAÇÃO
   → SELF-SERVICE
   → SUPORTE
   → GERENCIADO
```

O tier deve ser apresentado como **resultado explicável da configuração**, e não como uma escolha abstrata anterior à necessidade.

O modelo de implementação/operação é uma decisão posterior e **não participa do enquadramento do tier por si só**.

### Regra de seleção de capacidades

Nas superfícies de capacidades, **todas as capacidades governadas e contratáveis devem ser exibidas** e cada uma deve permitir decisão explícita da empresa:

```text
CAPACIDADE
→ INCLUIR
→ NÃO INCLUIR
```

A superfície deve mostrar, para cada capacidade:

- nome;
- finalidade;
- o que habilita na prática;
- opção **Incluir**;
- opção **Não incluir**;
- status no tier resultante;
- valor adicional mensal/anual, quando aplicável;
- indicação de valor adicional zero quando já incluída no tier;
- indicação `dimensionado` ou `sob consulta` quando não houver cifra autorizada.

```text
EMPRESA SELECIONA CAPACIDADE
↓
SISTEMA ENQUADRA TIER
↓
SE CAPACIDADE JÁ ESTÁ INCLUÍDA NO TIER
→ VALOR ADICIONAL ZERO

SE NÃO ESTÁ INCLUÍDA E POSSUI PREÇO AUTORIZADO
→ COBRAR COMO ADD-ON

SE EXIGE TIER SUPERIOR
→ REENQUADRAR E EXPLICAR

SE NÃO HÁ PREÇO AUTORIZADO
→ DIMENSIONAR / SOB CONSULTA
```

Nenhuma capacidade deve desaparecer da superfície apenas porque está incluída ou não no tier.

### Diferença de valor entre tiers

| Dimensão | **Start** | **Growth** | **Scale** | **Enterprise** |
|---|---|---|---|---|
| **Direção** | Operar | Acompanhar e compreender | Interpretar e integrar | Governar alta complexidade e escala |
| **Operacionalização** | núcleo para colocar a oferta em operação | adiciona Intelligence e governança ampliadas | adiciona integração, API, SSO, exportações e maior escala | dimensiona capacidades, segurança, governança, integrações e contrato |
| **Intelligence avançado** | adicional | incluído | incluído | incluído |
| **Governança avançada** | adicional | incluído | incluído | incluído |
| **Power BI / exportações** | adicional | adicional | incluído | incluído |
| **API Business** | adicional | adicional | incluído | incluído |
| **SSO / SAML** | adicional | adicional | incluído | incluído |
| **1 integração dedicada** | adicional | adicional | 1 incluída | conforme contrato |

### Tiers de capacidade

| Tier | Mensal | Anual |
|---|---:|---:|
| **Start** | R$ 299,00 | R$ 2.990,00 |
| **Growth** | R$ 799,00 | R$ 7.990,00 |
| **Scale** | a partir de R$ 1.990,00 | dimensionado |
| **Enterprise** | sob consulta | sob consulta |

### População elegível

| Faixa | Mensal por pessoa | Anual por pessoa |
|---|---:|---:|
| **1–50** | incluído | incluído |
| **51–250** | R$ 1,49 | R$ 14,90 |
| **251–1.000** | R$ 0,99 | R$ 9,90 |
| **1.001–5.000** | R$ 0,69 | R$ 6,90 |
| **5.001–20.000** | R$ 0,49 | R$ 4,90 |
| **20.000+** | dimensionado | dimensionado |

### Oferta Business

| Oferta | Taxa mensal de ativação | Taxa anual de ativação |
|---|---:|---:|
| **Programas de Incentivo** | **R$ 0,00** | **R$ 0,00** |
| **Journey custeado** | **R$ 0,00** | **R$ 0,00** |
| **Incentivos + Journey** | **R$ 0,00** | **R$ 0,00** |

Journey custeado continua possuindo cobrança por acesso financiado. O orçamento de incentivo continua separado da assinatura.

### Matriz de inclusões por tier

| Capacidade | Start | Growth | Scale | Enterprise |
|---|---|---|---|---|
| **Intelligence avançado** | R$ 299/mês · R$ 2.990/ano | incluído | incluído | incluído |
| **Exportações automatizadas / Power BI** | R$ 249/mês · R$ 2.490/ano | R$ 249/mês · R$ 2.490/ano | incluído | incluído |
| **API Business** | R$ 399/mês · R$ 3.990/ano | R$ 399/mês · R$ 3.990/ano | incluído | incluído |
| **SSO / SAML** | R$ 299/mês · R$ 2.990/ano | R$ 299/mês · R$ 2.990/ano | incluído | incluído |
| **Governança / auditoria avançadas** | R$ 249/mês · R$ 2.490/ano | incluído | incluído | incluído |
| **1 integração dedicada** | R$ 490/mês · R$ 4.900/ano | R$ 490/mês · R$ 4.900/ano | 1 incluída | incluída conforme contrato |
| **Integração dedicada adicional** | R$ 490/mês · R$ 4.900/ano por integração | mesmo valor | mesmo valor além da 1ª incluída | dimensionado |

## 10. Estado

```text
PLANS SURFACES COLLECTION
→ DOCUMENTED

VISUAL BASELINE
→ NOT IMPOSED

VARIABLE BUSINESS PRICING
→ ADJUDICATED / NORMATIVE
→ OFFER-FIRST MODEL
→ BUSINESS OFFER REQUIRED
→ OFFER ACTIVATION FEE = R$ 0,00
→ NUMERIC RATES AVAILABLE FOR CONFIGURATOR

BUSINESS TIER ENTITLEMENTS
→ ADJUDICATED
→ MATRIX EXPLICIT
→ ADD-ON PRICES EXPLICIT
→ DOUBLE CHARGING PROHIBITED

PRODUCT ENGINEERING
→ NOT RELEASED BY THIS COLLECTION
```
