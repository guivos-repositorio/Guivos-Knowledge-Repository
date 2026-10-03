---
id: GKR-UX-PLANS-READ-FIRST-001
title: Planos — Superfícies e Fluxos — Leia Primeiro
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: false
depends_on:
  - GKR-PLANS-INDEX-001
  - GEM-004-A1
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
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

Design, IA e Engenharia não podem inventar:

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

Business possui configurador Self-service próprio. Ele deve permitir selecionar oferta, população/escala, acessos, capacidades, periodicidade e serviços aplicáveis e então **calcular somente o que estiver amparado por uma tabela econômica vigente**.

Enquanto preço por população, acesso ou produto não estiver adjudicado, o configurador pode estruturar a composição, mas não fabricar valor numérico.

## 10. Estado

```text
PLANS SURFACES COLLECTION
→ DOCUMENTED

VISUAL BASELINE
→ NOT IMPOSED

VARIABLE BUSINESS PRICING
→ STRUCTURE DEFINED
→ NUMERIC RATES REQUIRE ECONOMIC AUTHORITY

PRODUCT ENGINEERING
→ NOT RELEASED BY THIS COLLECTION
```
