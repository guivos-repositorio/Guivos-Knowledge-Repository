---
id: GEM-004
title: Modelo Gratuito e Pago
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-000
depends_on:
  - GEM-003
  - GEM-003-DEPENDENCY-VALIDATION-CHECKPOINT-001
related:
  - GEM-004-UNIVERSAL-FREE-VALUE-BASELINE-001
  - GEM-004-PLAN-ARCHETYPE-CATALOG-001
  - GEM-004-PAYWALL-POLICY-001
  - GEM-004-PLAN-CONTRACT-001
  - M6.3
---

# GEM-004 — Modelo Gratuito e Pago

## 1. Objetivo

Definir como o Ecossistema Guivos distribui capacidades entre acesso gratuito, acesso pago e acesso financiado por terceiros, preservando valor universal, autonomia, segurança, transparência e sustentabilidade.

## 2. Pergunta arquitetural

> Qual valor mínimo toda pessoa deverá conseguir acessar gratuitamente e quais ampliações poderão ser oferecidas de forma paga sem enfraquecer artificialmente o gratuito, explorar vulnerabilidade ou comprometer autonomia, segurança e propósito?

## 3. Sequência de referência

```text
valor universal gratuito
→ participação e benefício reais
→ necessidade adicional identificada
→ ampliação paga compreensível
→ escolha livre
→ utilização
→ continuidade, alteração ou cancelamento
```

Não é admissível criar escassez artificial, frustração deliberada, urgência, medo ou dependência para induzir conversão.

## 4. Conceitos

### Valor universal gratuito

Conjunto mínimo de benefícios, capacidades, direitos e proteções que permite participação significativa sem pagamento.

### Valor essencial

Capacidade necessária para preservar propósito, autonomia, segurança, transparência, controle dos próprios dados e participação básica.

### Ampliação paga

Capacidade adicional que amplia profundidade, velocidade, conveniência, personalização, volume, colaboração, automação, suporte, inteligência ou integração.

### Plano

Conjunto organizado de capacidades, limites, direitos, condições e responsabilidades atribuído a um ator elegível.

### Arquétipo de plano

Estrutura conceitual para organizar planos futuros, sem estabelecer nome comercial, preço, SKU ou contrato definitivo.

### Entitlement

Direito efetivo de acessar ou utilizar determinada capacidade.

### Paywall

Regra que condiciona uma ampliação a pagamento, financiamento ou elegibilidade.

### Acesso financiado

Acesso cujo custo é assumido por organização, patrocinador, parceiro, programa social ou terceiro legítimo.

## 5. Princípios

1. o gratuito deverá entregar valor real;
2. o pago deverá ampliar valor, não devolver artificialmente valor retirado;
3. direitos básicos não poderão ser condicionados a pagamento;
4. escolha, recusa, downgrade e cancelamento deverão permanecer compreensíveis;
5. falha de pagamento deverá afetar primeiro ampliações pagas;
6. dados próprios e direitos deverão ser preservados nas transições;
7. organização ou patrocinador não receberá autoridade indevida;
8. capacidade paga deverá possuir hipótese de valor e validação;
9. diferenciação entre planos deverá ser compreensível;
10. preço e implementação permanecem fora desta versão.

## 6. Estados de capacidade

- `universal_free`;
- `free_limited`;
- `paid_extension`;
- `paid_specialized`;
- `organization_funded`;
- `sponsor_funded`;
- `partner_access`;
- `temporarily_unlocked`;
- `prohibited_paywall`;
- `not_assessed`.

## 7. Arquétipos iniciais

1. AM-01 — Participante Universal;
2. AM-02 — Participante Ampliado;
3. AM-03 — Participante Assistido;
4. AM-04 — Acesso Financiado por Organização;
5. AM-05 — Acesso Patrocinado ou Social;
6. AM-06 — Acesso de Parceiros e Profissionais;
7. AM-07 — Acesso Organizacional.

## 8. Requisitos mínimos de admissibilidade

Uma diferenciação somente poderá avançar quando:

- o gratuito continuar útil;
- a capacidade paga possuir valor adicional identificável;
- direitos e segurança permanecerem protegidos;
- pagador, beneficiário e financiador estiverem claros;
- limites e transições forem compreensíveis;
- cancelamento e downgrade forem possíveis;
- dados e acessos de terceiros estiverem limitados;
- riscos operacionais e de exclusão forem reconhecidos;
- hipóteses e evidências estiverem registradas.

## 9. Limites desta versão

O GEM-004 não define:

- nomes comerciais finais;
- preços, moedas ou descontos;
- limites quantitativos definitivos;
- períodos de cobrança;
- duração final de trials;
- contratos;
- gateway, adquirente ou sistema de pagamento;
- metas de conversão;
- unit economics;
- implementação de entitlement;
- oferta pública;
- produção.

## 10. Critérios de conclusão

- valor universal definido;
- capacidades essenciais protegidas;
- ampliações pagas catalogadas;
- sete arquétipos definidos;
- matriz de alocação publicada;
- elegibilidade e acesso financiado estruturados;
- ciclo de vida documentado;
- política de paywall definida;
- regras de upgrade, downgrade e cancelamento publicadas;
- contrato canônico disponível;
- nove cenários e quatorze gates documentados;
- pendências do GEM-005 explícitas.
