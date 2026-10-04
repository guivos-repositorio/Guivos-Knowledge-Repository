---
id: GKR-UX-PLANS-ORCHESTRATION-001
title: Planos — Superfícies e Fluxos — Documento Mestre de Orquestração UX/UI
status: active
version: 0.6.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: false
depends_on:
  - GKR-UX-PLANS-READ-FIRST-001
  - GKR-PLANS-INDEX-001
  - GEM-004-A1
  - GEM-004-BUSINESS-VARIABLE-PRICING-AUTHORITY-001
---

# Planos — Superfícies e Fluxos — Documento Mestre de Orquestração UX/UI

## 1. Objetivo

Orquestrar a experiência de planos sem misturar quatro contextos econômicos distintos.

## 2. Arquitetura de alto nível

```text
ENTRADA EM PLANOS
↓
IDENTIFICAR CONTEXTO
├─ Pessoa
├─ Coletivo
├─ Organização
└─ Guivos Business
↓
COMPREENDER PLANOS E DIFERENÇAS
↓
ESCOLHER PERIODICIDADE
├─ Mensal
└─ Anual
↓
DECISÃO
├─ permanecer / voltar
├─ revisar mudança de plano
└─ no Business: configurar composição
```

## 3. Regra de comparação

A comparação deve mostrar diferenças relevantes em capacidades e limites. “Vantagem” significa **capacidade adicional, maior limite, maior profundidade ou menor custo relativo quando uma economia anual estiver documentalmente comprovada**.

A superfície não deve usar superioridade moral, pressão, medo de perda ou garantia de resultado.

## 4. Informação mínima por plano

Cada plano deve possuir nome, finalidade, preço mensal, preço anual, capacidades incluídas, limites principais, diferenças em relação ao tier anterior quando aplicável, condições sujeitas a dimensionamento, ação de continuidade e opção de não prosseguir.

## 5. Mensal e anual

A periodicidade deve ser uma escolha explícita para todo plano pago.

Quando ambas as cifras forem conhecidas, a superfície pode apresentar a comparação entre elas. Economia percentual ou absoluta só pode ser exibida se derivada diretamente dos valores vigentes.

Quando uma cifra não estiver congelada:

```text
ANUAL OU MENSAL
→ DISPONÍVEL
→ VALOR DIMENSIONADO / SOB CONSULTA
```

## 6. Estado atual

Quando houver contexto autenticado e fonte confiável, a superfície pode identificar o plano atual. A ausência de informação não autoriza inferência.

## 7. Continuidade sem efeito comercial

Comparar, alternar periodicidade, abrir detalhes ou selecionar temporariamente um plano para leitura não equivale a contratar.

## 8. Business

Guivos Business acrescenta uma etapa de composição:

```text
OFERTA BUSINESS OBRIGATÓRIA
→ DEFINE O OBJETO DA CONTRATAÇÃO
→ TAXA DE ATIVAÇÃO = R$ 0,00

TIER DE CAPACIDADE
+ POPULAÇÃO / ESCALA
+ ACESSOS JOURNEY CUSTEADOS, SE APLICÁVEL
+ CAPACIDADES ADICIONAIS NÃO INCLUÍDAS NO TIER
+ SERVIÇOS ADICIONAIS
= VALOR RECORRENTE CONTRATUAL

ORÇAMENTO DE INCENTIVO
= RECURSO OPERACIONAL SEPARADO
```


### 8.1 Ordem funcional recomendada do configurador

A experiência Business deve permitir, sem prescrever layout:

```text
1. ESCOLHER OFERTA BUSINESS OBRIGATÓRIA
2. ESCOLHER PERIODICIDADE
3. INFORMAR POPULAÇÃO ELEGÍVEL
4. INFORMAR ACESSOS JOURNEY, SE APLICÁVEL
5. IDENTIFICAR CAPACIDADES NECESSÁRIAS
6. ENQUADRAR TIER COMPATÍVEL
7. ZERAR ADD-ONS JÁ INCLUÍDOS NO TIER
8. ESCOLHER SERVIÇO ADICIONAL, SE NECESSÁRIO
9. INFORMAR ORÇAMENTO DE INCENTIVO SEPARADO
10. REVISAR COMPOSIÇÃO
11. EXIBIR TOTAL RECORRENTE + ITENS SEPARADOS / DIMENSIONADOS
```

A ordem pode ser reorganizada visualmente, mas a semântica de cálculo e a proteção contra dupla cobrança devem permanecer.

### 8.2 Informação mínima do resultado Business

O resumo da composição deve distinguir:

- oferta Business contratada e taxa de ativação `R$ 0,00`;
- tier de capacidade;
- população/escala e faixas aplicadas;
- Journey Plus/Pro custeado e quantidade;
- add-ons efetivamente cobrados, com valor mensal/anual aplicável;
- capacidades incluídas no tier, explicitadas com `R$ 0,00 adicional`;
- serviço adicional;
- subtotal/total recorrente;
- orçamento pré-pago de incentivo em linha separada;
- itens dimensionados ou sob consulta;
- periodicidade e condição anual/mensal.

```text
INCLUDED
≠ FREE UNIVERSALLY
≠ ADD-ON CHARGED

INCENTIVE BUDGET
≠ SUBSCRIPTION REVENUE
```

### 8.3 Matriz de capacidade por tier

Para cada capacidade contratável, a experiência deve mostrar simultaneamente:

```text
CAPACIDADE
+ STATUS NO TIER
+ VALOR ADICIONAL MENSAL
+ VALOR ADICIONAL ANUAL
```

Estados possíveis:

- **incluído** → `R$ 0,00 adicional`;
- **adicional** → usar preço mensal/anual vigente da capacidade;
- **dimensionado** → não gerar cifra por inferência;
- **incluído conforme contrato** → respeitar o dimensionamento contratual aplicável.

Essa matriz deve ser consumida como regra econômica, não como prescrição visual.

### 8.4 Quadro econômico mínimo da superfície

A experiência de composição Business deve ter acesso explícito aos componentes abaixo:

| Componente | Regra econômica corrente |
|---|---|
| **Oferta Business** | obrigatória; taxa de ativação = R$ 0,00 |
| **Start** | R$ 299/mês · R$ 2.990/ano |
| **Growth** | R$ 799/mês · R$ 7.990/ano |
| **Scale** | a partir de R$ 1.990/mês · anual dimensionado |
| **Enterprise** | sob consulta |
| **População** | progressiva por faixa; 1–50 incluídos |
| **Journey custeado** | cobrança por acesso Plus/Pro financiado |
| **Capacidade incluída no tier** | R$ 0,00 adicional |
| **Capacidade não incluída** | preço mensal/anual governado |
| **Self-service** | R$ 0,00 |
| **Orçamento de incentivo** | separado da assinatura |

Exemplo mínimo de leitura:

```text
EMPRESA ESCOLHE
→ PROGRAMAS DE INCENTIVO

CONFIGURA
→ 120 PESSOAS
→ SELF-SERVICE
→ SEM INTEGRAÇÃO ADICIONAL

ENQUADRAMENTO
→ START

COMPOSIÇÃO RECORRENTE
→ TIER START = R$ 299,00
→ 1–50 = R$ 0,00
→ 51–120 = 70 × R$ 1,49 = R$ 104,30
→ SELF-SERVICE = R$ 0,00
→ TOTAL = R$ 403,30/MÊS
```

A oferta não deve aparecer como parcela financeira artificial de R$ 0,00 no subtotal. Ela é o objeto contratado. O orçamento destinado às recompensas do programa não integra esse total recorrente.

### 8.5 Progressão funcional dos tiers

A experiência deve tornar legível **por que** uma configuração sobe de tier.

| Tier | Direção | O que muda na prática |
|---|---|---|
| **Start** | operar | núcleo necessário para executar a oferta contratada |
| **Growth** | acompanhar e compreender | adiciona profundidade de Intelligence e governança |
| **Scale** | interpretar e integrar | adiciona capacidades de integração, API, SSO, exportações e operação em escala |
| **Enterprise** | governar alta complexidade e escala | dimensiona segurança, governança, integrações, capacidade e condições contratuais específicas |

A interface deve explicar o motivo do enquadramento:

```text
TIER RESULTANTE
→ EXPLICÁVEL

SUBIR DE TIER
→ CONSEQUÊNCIA DE CAPACIDADE NECESSÁRIA
→ NÃO PRESSÃO COMERCIAL
→ NÃO MAXIMIZAÇÃO DE RECEITA
```

## 9. Estados transversais

Design pode representar, sem criar nova autoridade: carregamento, comparação disponível, preço conhecido, preço dimensionado, periodicidade mensal, periodicidade anual, configuração incompleta, configuração calculável, configuração que exige proposta, erro recuperável e retorno sem alteração.

## 10. Acessibilidade

Diferenças, preços, periodicidade e ações não podem depender apenas de cor, posição ou ícone. Tabelas e cards precisam preservar leitura linear e tecnologias assistivas.

## 11. Critérios de aceite

A experiência é aceitável quando as quatro taxonomias permanecem separadas; mensal/anual é explicitamente selecionável; diferenças funcionais são legíveis; valores consomem a autoridade econômica vigente; dimensionamento é distinguido de preço fixo; capacidades incluídas não são cobradas novamente; comparar não produz contratação; Business separa assinatura de orçamento de incentivo; Design mantém liberdade criativa; e Product Engineering não é liberado por este documento.
