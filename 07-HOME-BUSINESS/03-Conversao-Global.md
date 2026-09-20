---
id: GKR-UX-HOME-BUSINESS-CONVERSION-002
title: Autoridade de Conversão Global — Home Pública — Guivos Business — v2
status: active
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-08-16
parent: GKR-UX-HOME-BUSINESS-CONVERSION-001
depends_on:
  - GKR-UX-HOME-BUSINESS-NARRATIVE-001
  - GKR-UX-HOME-BUSINESS-AUTHORITY-001
  - GPA-004
  - GKR-STATE-001
  - ROADMAP-12.79.0
supersedes:
  - GKR-UX-HOME-BUSINESS-CONVERSION-001
normative: true
---

# Autoridade de Conversão Global — Home Pública — Guivos Business — v2

## 1. Finalidade

Este documento substitui a autoridade de conversão anterior da Home Pública do Guivos Business no ponto em que ela separava `Online / Assistida / Especializada` como formas distintas de contratação.

A decisão validada posteriormente é mais simples e mais adequada à escala global:

> **Toda contratação do Guivos Business deve ser concebida como contratação online. O que varia é a forma de implementação e condução da operação depois da contratação.**

A arquitetura comercial passa a separar somente:

```text
PLANO / CAPACIDADE
Start · Growth · Scale · Enterprise

≠

MODELO DE IMPLEMENTAÇÃO / OPERAÇÃO
Self-service · Com apoio do suporte · Gerenciado
```

A contratação permanece digital nos três modelos.

## 2. Princípio de escala global

A Home e o configurador comercial não devem pressupor vendedor obrigatório, contrato manual ou atendimento humano como etapa necessária para concluir a contratação.

Direção:

```text
CONFIGURAR
↓
COMPARAR
↓
CONHECER O VALOR
↓
CONTRATAR ONLINE
↓
PAGAR / FORMALIZAR
↓
IMPLEMENTAR DE ACORDO COM O MODELO INDICADO
```

A futura implementação deve poder variar, por mercado efetivamente suportado, idioma, país/região, moeda, entidade contratante, faturamento, tributação, meio de pagamento, disponibilidade de produtos, requisitos regulatórios, privacidade, suporte e nível de serviço.

Nenhum país, moeda, preço, meio de pagamento ou regra fiscal específica é congelado por esta autoridade.

## 3. Dimensão 1 — Plano / capacidade

Os planos permanecem:

```text
START
→ Comece a operar

GROWTH
→ Acompanhe e compreenda

SCALE
→ Interprete e integre

ENTERPRISE
→ Governe em alta complexidade e escala
```

Plano governa capacidade, escala, Intelligence, integração, governança e serviço conforme contratos futuros.

Plano não define mérito, qualidade humana, nível de evolução ou valor da empresa.

Regra:

> **Mais plano ≠ mais evolução. Mais plano significa mais capacidade operacional contratada.**

## 4. Dimensão 2 — Modelo de implementação / operação

### 4.1 Self-service

Aplicável quando a empresa consegue concluir a implementação e operar com os recursos padronizados disponíveis.

Fluxo:

```text
CONFIGURA
↓
CONHECE O VALOR
↓
CONTRATA ONLINE
↓
PAGA / FORMALIZA
↓
ACESSA
↓
CONFIGURA
↓
OPERA
```

Mensagem pública possível:

> **Sua empresa pode configurar e iniciar a operação diretamente pela plataforma.**

### 4.2 Com apoio do suporte

Aplicável quando a contratação pode ser concluída normalmente online, mas a continuidade da implementação necessita apoio do suporte Guivos.

O suporte entra **depois da contratação**.

Fluxo:

```text
CONFIGURA
↓
CONHECE O VALOR
↓
CONTRATA ONLINE
↓
PAGA / FORMALIZA
↓
CONTRATAÇÃO CONCLUÍDA
↓
SUPORTE GUIVOS
↓
APOIO NA IMPLEMENTAÇÃO
↓
OPERAÇÃO
```

Mensagem pública possível:

> **Após a contratação, o suporte Guivos acompanha a implementação da configuração contratada.**

Não utilizar como CTA pré-contratação a expressão `Configurar com apoio da Guivos` quando ela sugerir dependência comercial anterior ao pagamento.

### 4.3 Gerenciado

Aplicável quando a complexidade exige participação mais profunda da Guivos na implementação, governança ou condução da operação.

A contratação continua online.

Fluxo:

```text
CONFIGURAÇÃO DEFINIDA
↓
VALOR / CONDIÇÕES APLICÁVEIS
↓
CONTRATAÇÃO ONLINE
↓
PAGAMENTO / FORMALIZAÇÃO
↓
IMPLEMENTAÇÃO GUIVOS + EMPRESA
↓
GOVERNANÇA
↓
OPERAÇÃO GERENCIADA
```

A futura engenharia comercial deve assegurar que operações gerenciadas possam ser contratadas digitalmente mesmo quando exijam maior acompanhamento posterior.

## 5. Configurador comercial

O Movimento 09 da Home deve funcionar como configurador comercial, e não apenas como calculadora de preço.

Ele pode considerar, conforme disponibilidade real:

```text
NÚMERO DE PESSOAS
+
OFERTA CONTRATADA
+
CAPACIDADE / PLANO
+
TIPO DE OPERAÇÃO
+
INTELLIGENCE
+
INTEGRAÇÕES
+
GOVERNANÇA
+
SERVIÇO
+
MERCADO
```

E devolver:

```text
PLANO / CONFIGURAÇÃO
+
CAPACIDADES
+
VALOR OU ESTIMATIVA APLICÁVEL
+
MODELO DE IMPLEMENTAÇÃO / OPERAÇÃO
+
PRÓXIMO PASSO
```

O CTA final, quando a configuração estiver apta, deve levar à contratação online.

## 6. Princípio público de conversão

Formulação consolidada:

> **Configure. Compare. Contrate.**

Supporting copy de referência:

> **Encontre a configuração adequada para sua empresa, compare as capacidades disponíveis, conheça o valor e contrate online.**

Síntese operacional:

> **Self-service quando possível. Suporte quando necessário. Operação gerenciada quando a complexidade exigir.**

## 7. O que esta autoridade substitui

Fica substituída, para a Home Business e futuras implementações derivadas, a arquitetura anterior:

```text
FORMA DE CONTRATAÇÃO
Online · Assistida · Especializada

+

MODELO DE SERVIÇO
Self-service · Assisted · Managed
```

A arquitetura vigente passa a ser:

```text
CONTRATAÇÃO
→ ONLINE

MODELO DE IMPLEMENTAÇÃO / OPERAÇÃO
→ SELF-SERVICE
→ COM APOIO DO SUPORTE
→ GERENCIADO
```

## 8. Preservações

Esta autoridade não:

- define preços finais;
- congela limites quantitativos;
- define SLA;
- congela entitlements;
- define regras fiscais;
- define disponibilidade por país;
- altera `GPA-004`;
- cria nova família comercial;
- transforma suporte em etapa obrigatória de venda;
- autoriza Source Lock ou Design por si só.
