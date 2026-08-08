---
id: GKR-JOURNEY-SCREEN-GALLERY-PLANS-001
title: Planos, Comparação e Cobrança — Galeria Candidata
status: draft
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - UXA-100
  - UXA-100-A1
  - UXA-100-A2
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
normative: false
---

# Planos, Comparação e Cobrança — Galeria Candidata

## 1. Finalidade

Esta galeria reúne as materializações candidatas da UXA-100 para **Pessoa, Coletivo e Organização**. Os ativos desta página não integram a contagem canônica da galeria principal e não criam IDs de superfície ou transição.

A UXA-100-A2 auditou funcionalmente os nove ativos: **6 foram reformulados controladamente e 3 permaneceram inalterados; 9/9 foram aprovados funcionalmente como candidatos**.

## 2. Pessoa

### 2.1 Tela dedicada de Planos — aprovada após reforma

![Pessoa — tela dedicada de Planos](../assets/wireframes/uxa-100-person-plans-screen-mobile.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-person-plans-screen-mobile.svg)

### 2.2 Fluxo de plano, cobrança e pagamento — aprovado após reforma

![Pessoa — fluxo de planos e pagamentos](../assets/wireframes/uxa-100-person-plans-payments-flow-board.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-person-plans-payments-flow-board.svg)

### 2.3 Comparação incremental — aprovada sem reforma

![Pessoa — comparação incremental](../assets/wireframes/uxa-100-person-plan-incremental-benefits-comparison.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-person-plan-incremental-benefits-comparison.svg)

## 3. Coletivo

### 3.1 Tela dedicada de Planos — aprovada após reforma

![Coletivo — tela dedicada de Planos](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

### 3.2 Fluxo de plano, cobrança e pagamento — aprovado após reforma

![Coletivo — fluxo de planos e pagamentos](../assets/wireframes/uxa-100-collective-plans-payments-flow-board.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-collective-plans-payments-flow-board.svg)

### 3.3 Comparação incremental — aprovada sem reforma

![Coletivo — comparação incremental](../assets/wireframes/uxa-100-collective-plan-incremental-benefits-comparison.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-collective-plan-incremental-benefits-comparison.svg)

## 4. Organização

### 4.1 Tela dedicada de Planos — aprovada após reforma

![Organização — tela dedicada de Planos](../assets/wireframes/uxa-100-organization-plans-screen-desktop.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-organization-plans-screen-desktop.svg)

### 4.2 Fluxo de plano, cobrança e pagamento — aprovado após reforma

![Organização — fluxo de planos e pagamentos](../assets/wireframes/uxa-100-organization-plans-payments-flow-board.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-organization-plans-payments-flow-board.svg)

### 4.3 Comparação incremental — aprovada sem reforma

![Organização — comparação incremental](../assets/wireframes/uxa-100-organization-plan-incremental-benefits-comparison.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-organization-plan-incremental-benefits-comparison.svg)

## 5. Leitura de jornada validada no escopo candidato

```text
participante
→ Planos
→ plano atual + uso/capacidade
→ matriz geral + delta incremental
→ manter / upgrade / downgrade / cancelar / solicitar proposta
→ revisão de contratação
→ pagamento simulado ou processo comercial governado
→ sucesso/falha
→ retorno ao contexto anterior
```

Também pode existir entrada contextual a partir de um limite legítimo, sem ocultar alternativas gratuitas ou operacionais aplicáveis.

## 6. Contagem candidata

| Participante | Tela Planos | Placa de fluxo | Comparação incremental | Total candidato | Funcionalmente aprovado |
|---|---:|---:|---:|---:|---:|
| Pessoa | 1 | 1 | 1 | 3 | 3 |
| Coletivo | 1 | 1 | 1 | 3 | 3 |
| Organização | 1 | 1 | 1 | 3 | 3 |
| **Total** | **3** | **3** | **3** | **9** | **9** |

Os 9 SVGs permanecem candidatos e **não elevam os 109 SVGs canônicos** enquanto não houver promoção governada.

## 7. Reformas da UXA-100-A2

Foram reformulados:

- tela de Planos da Pessoa;
- fluxo de planos/pagamentos da Pessoa;
- tela de Planos do Coletivo;
- fluxo de planos/pagamentos do Coletivo;
- tela de Planos da Organização;
- fluxo de planos/pagamentos da Organização.

Foram preservadas sem reforma as três comparações incrementais.

## 8. Proteções

- plano pago não compra relevância, confiança, legitimidade, impacto ou evolução;
- oportunidade pública não é escondida para vender plano;
- benefícios herdados não aparecem como novidades;
- Enterprise/Scale não simulam checkout autônomo definitivo;
- falha de pagamento não presume ativação;
- data de início e recorrência devem aparecer antes da confirmação;
- downgrade/cancelamento exibem consequências e tratam capacidades excedentes antes da efetivação;
- materialização documental e validação funcional não equivalem a implementação.
