---
id: GEM-004
title: Modelo Gratuito e Pago
status: active
version: 0.3.0
owner: Guivos Economic Model
last_updated: 2026-08-08
parent: GEM-000
depends_on:
  - GEM-003
  - GEM-003-DEPENDENCY-VALIDATION-CHECKPOINT-001
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
related:
  - GEM-004-UNIVERSAL-FREE-VALUE-BASELINE-001
  - GEM-004-PLAN-ARCHETYPE-CATALOG-001
  - GEM-004-PAYWALL-POLICY-001
  - GEM-004-PLAN-CONTRACT-001
  - GEM-004-A1
  - GEM-004-A2
  - GEM-010-A1
  - GEM-COMMERCIAL-BASELINE-001
  - M6.3
  - M7.39
---

# GEM-004 — Modelo Gratuito e Pago

## 1. Objetivo

Definir como o Ecossistema Guivos distribui capacidades entre acesso gratuito, acesso pago e acesso financiado por terceiros, preservando valor universal, autonomia, segurança, transparência e sustentabilidade.

A versão 0.3.0 reconcilia a baseline comercial com a autoridade conceitual vigente de planos, separando definitivamente os planos de Organização dos tiers do Produto Especializado Guivos Business.

## 2. Pergunta arquitetural

> Qual valor mínimo toda pessoa, Coletivo ou Organização deverá conseguir acessar gratuitamente e quais ampliações poderão ser oferecidas de forma paga sem enfraquecer artificialmente o gratuito, explorar vulnerabilidade ou comprometer autonomia, segurança e propósito?

## 3. Sequência de referência

```text
valor universal gratuito
→ participação e benefício reais
→ necessidade adicional identificada
→ ampliação paga compreensível
→ preço e limite transparentes
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

Conjunto organizado de capacidades, limites, direitos, condições, preços e responsabilidades atribuído a um ator elegível.

### Arquétipo de plano

Estrutura conceitual que sustenta planos comerciais sem substituí-los.

### Plano comercial candidato

Composição documentada de nome, público, benefícios, limites e preço aprovada para validação, mas não para cobrança ou oferta pública.

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
10. preço candidato não autoriza cobrança;
11. catálogo público e correspondência personalizada são objetos diferentes;
12. assinatura, transação, comissão, taxa de pagamento e tributo são objetos diferentes;
13. compra de plano não aumenta relevância, ranking, impacto ou evidência;
14. publicações existentes não perderão visibilidade para pressionar upgrade;
15. capacidade sem limite padrão permanece sujeita a contrato, uso justo e disponibilidade operacional.

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

## 7. Arquétipos preservados

1. AM-01 — Participante Universal;
2. AM-02 — Participante Ampliado;
3. AM-03 — Participante Assistido;
4. AM-04 — Acesso Financiado por Organização;
5. AM-05 — Acesso Patrocinado ou Social;
6. AM-06 — Acesso de Parceiros e Profissionais;
7. AM-07 — Acesso Organizacional.

## 8. Taxonomia comercial vigente para validação

### Pessoas

- Guivos Free;
- Guivos Plus;
- Guivos Pro.

### Coletivos

- Coletivo Livre;
- Coletivo Mobiliza;
- Coletivo Impacta;
- Coletivo Rede.

### Organizações

- Organização Conecta;
- Organização Eleva;
- Organização Transforma.

### Guivos Business

Guivos Business é Produto Especializado e não um tipo de participante nem uma família de planos de Organização. Sua taxonomia própria é:

- Start;
- Growth;
- Scale;
- Enterprise.

Não existe correspondência automática 1:1 entre `Conecta / Eleva / Transforma` e `Start / Growth / Scale / Enterprise`.

> **Organização Transforma ≠ Guivos Business Enterprise.**

### Acesso transversal

- Guivos Patrocinado ou financiado.

Nomes, preços, benefícios e limites de Pessoa, Coletivo e Organização são governados pela autoridade conceitual vigente e pelos artefatos econômicos derivados aplicáveis. A taxonomia de Guivos Business não autoriza preços ou entitlements de Business onde eles ainda não tenham autoridade específica.

## 9. Requisitos mínimos de admissibilidade

Uma diferenciação somente poderá avançar quando:

- o gratuito continuar útil;
- a capacidade paga possuir valor adicional identificável;
- direitos e segurança permanecerem protegidos;
- pagador, beneficiário e financiador estiverem claros;
- limites e transições forem compreensíveis;
- cancelamento e downgrade forem possíveis;
- dados e acessos de terceiros estiverem limitados;
- riscos operacionais e de exclusão forem reconhecidos;
- hipóteses e evidências estiverem registradas;
- o catálogo público não for ocultado para pressionar pagamento;
- o limite estiver associado a custo, risco, capacidade ou diferenciação legítima;
- compromisso já assumido permanecer protegido no downgrade ou cancelamento.

## 10. Baseline comercial vigente

A baseline candidata está distribuída em:

- autoridade conceitual de taxonomia de planos — nomes, fronteiras e precedência semântica;
- GEM-004-A1 — planos, benefícios, limites e preços aplicáveis;
- GEM-004-A2 — oferta, upgrade, downgrade e cancelamento;
- GEM-010-A1 — premissas de preço, custos e validação;
- GEM-COMMERCIAL-BASELINE-001 — parecer de reabertura localizada.

O conjunto é documentalmente definido e empiricamente não validado. Em caso de conflito de nomenclatura, prevalece `GEM-004-PLAN-TAXONOMY-AUTHORITY-001`.

## 11. Limites desta versão

A versão 0.3.0 não aprova:

- oferta pública;
- cobrança;
- SKU técnico;
- limites de infraestrutura;
- comissão transacional;
- gateway ou adquirente;
- tributos finais;
- reembolso;
- metas de conversão;
- unit economics calibrados;
- contratos;
- implementação de entitlement;
- produção;
- preços ou entitlements próprios de Guivos Business sem autoridade específica.

## 12. Critérios de conclusão documental

- valor universal definido;
- capacidades essenciais protegidas;
- ampliações pagas catalogadas;
- arquétipos preservados;
- planos comerciais candidatos para Pessoas, Coletivos e Organizações consolidados;
- Guivos Business preservado como Produto Especializado separado;
- preços e limites candidatos registrados onde houver autoridade aplicável;
- acesso financiado estruturado;
- regras de cotas documentadas;
- separação entre assinatura e transação estabelecida;
- política de oferta e paywall definida;
- upgrade, downgrade e cancelamento publicados;
- premissas financeiras e gates de validação registrados;
- pendências empíricas, operacionais e especializadas explícitas.
