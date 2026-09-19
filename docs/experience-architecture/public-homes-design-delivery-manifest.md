---
id: GKR-UX-HOMES-DESIGN-DELIVERY-001
title: Homes Públicas — Manifesto Canônico de Entrega para Design
status: active
version: 6.0.0
owner: Experience Architecture
last_updated: 2026-09-19
normative: true
maturity: design_delivery_v6_candidate_human_first_ai_optional
depends_on:
  - GKR-STATE-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
related:
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V5-SNAPSHOT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
  - GKR-HOMES-DESIGN-INPUT-HARDENING-V6-001
---

# Homes Públicas — Manifesto Canônico de Entrega para Design

## 1. Finalidade

Este Manifesto define o **candidato v6** do pacote documental externo das oito Homes públicas.

O v6 existe para entregar à designer humana um conjunto completo, atual, isolável por Home e suficientemente claro para criação manual, preservando IA apenas como ferramenta opcional.

```text
V5
→ HISTÓRICO / FROZEN / REPRODUCIBLE

V6
→ CANDIDATE
→ HUMAN-FIRST
→ AI-OPTIONAL
→ NOT_EMITTED
```

O v6 não contém, cria ou exige arquivo Figma, wireframe, UI, protótipo ou identidade visual.

## 2. Princípio do v6

A designer recebe a mesma verdade documental que qualquer sistema de IA opcional.

```text
DESIGNER
→ CONSUME O PACOTE
→ CRIA MANUALMENTE

AI
→ OPTIONAL
→ CONSUME O MESMO PACOTE
→ NÃO RECEBE AUTORIDADE ADICIONAL

GKR
→ NÃO DEFINE IDENTIDADE VISUAL
```

Cada Home recebe um `LEIA-PRIMEIRO` orientado primeiro à compreensão humana. O prompt/Source Lock de IA, quando necessário, funciona como adaptador secundário e não como caminho obrigatório.

## 3. Composição canônica — 26 fontes únicas

### 3.1 Fontes comuns

1. `docs/experience-architecture/public-homes-design-handoff.md` — `GKR-UX-HOMES-DESIGN-HANDOFF-001 v1.6.0`;
2. `docs/experience-architecture/public-homes-generative-source-lock-and-prompt-template.md` — `GKR-UX-HOMES-GENINPUT-001 v2.1.0`;
3. `docs/experience-architecture/public-homes-design-production-readiness-and-figma-contract.md` — `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001 v1.1.0`;
4. `docs/experience-architecture/public-homes-design-delivery-operational-flow.md` — `GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001 v3.0.0`.

### 3.2 Pessoa

5. `docs/experience-architecture/public-home-master-document.md` — `GKR-UX-HOME-MASTER-001 v1.1.0`;
6. `docs/experience-architecture/public-home-person-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001 v1.0.0`.

### 3.3 Organizações e Coletivos

7. `docs/experience-architecture/public-home-organizations-collectives-master-document.md` — `GKR-UX-HOME-OC-MASTER-001 v1.1.0`;
8. `docs/experience-architecture/public-home-organizations-collectives-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-OC-MEDIA-SUPPLY-001 v1.0.0`.

### 3.4 Mall

9. `docs/experience-architecture/public-home-mall-master-document.md` — `GKR-UX-HOME-MALL-MASTER-001 v1.1.0`;
10. `docs/experience-architecture/public-home-mall-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-MALL-MEDIA-SUPPLY-001 v1.0.0`.

### 3.5 Travel

11. `docs/experience-architecture/public-home-travel-master-document.md` — `GKR-UX-HOME-TRAVEL-MASTER-001 v1.1.0`;
12. `docs/experience-architecture/public-home-travel-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001 v1.0.0`.

### 3.6 Media

13. `docs/experience-architecture/public-home-media-master-document.md` — `GKR-UX-HOME-MEDIA-MASTER-001 v1.1.0`;
14. `docs/product-architecture/media.md` — `GPA-005 v1.2.0`.

### 3.7 Ads

15. `docs/experience-architecture/public-home-ads-master-document.md` — `GKR-UX-HOME-ADS-MASTER-001 v1.1.0`;
16. `docs/product-architecture/ads.md` — `GPA-007 v1.3.0`.

### 3.8 Business

17. `docs/experience-architecture/public-home-business-source-lock.md` — `GKR-UX-HOME-BUSINESS-SOURCELOCK-001 v1.1.0`;
18. `docs/experience-architecture/public-home-business-master-document.md` — `GKR-UX-HOME-BUSINESS-MASTER-001 v1.1.0`;
19. `docs/experience-architecture/public-home-business-conversion-authority-v2.md` — `GKR-UX-HOME-BUSINESS-CONVERSION-002 v1.0.0`;
20. `docs/experience-architecture/public-home-business-authority-contracts.md` — `GKR-UX-HOME-BUSINESS-AUTHORITY-001 v1.0.0`;
21. `docs/product-architecture/business.md` — `GPA-004 v1.6.0`.

### 3.9 Intelligence

22. `docs/experience-architecture/public-home-intelligence-design-handoff.md` — `GKR-UX-HOME-INTELLIGENCE-HANDOFF-001 v1.0.0`;
23. `docs/experience-architecture/public-home-intelligence-source-lock.md` — `GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001 v1.0.0`;
24. `docs/experience-architecture/public-home-intelligence-master-document.md` — `GKR-UX-HOME-INTELLIGENCE-MASTER-001 v1.0.0`;
25. `docs/product-architecture/intelligence-product-source-lock.md` — `GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001 v1.0.0`;
26. `docs/product-architecture/intelligence.md` — `GPA-006 v2.0.0`.

## 4. Oito guias `LEIA-PRIMEIRO`

A futura emissão v6 deve gerar oito guias, um por Home.

Cada guia precisa atender primeiro à designer humana e conter:

1. finalidade da Home;
2. ordem curta de leitura;
3. Documento Mestre;
4. fontes específicas;
5. decisões que precisam sobreviver;
6. liberdade criativa;
7. conteúdo/dados reais necessários;
8. placeholders permitidos;
9. questões abertas;
10. inferências proibidas;
11. critérios de aceite;
12. checkpoint e SHAs.

Somente depois disso o guia pode incluir um apêndice opcional para IA contendo Source Lock e prompt.

```text
LEIA-PRIMEIRO
→ HUMAN-FIRST

AI APPENDIX
→ OPTIONAL

PROMPT
→ ADAPTER
→ NOT AUTHORITY
```

## 5. Estrutura externa

O candidato de estrutura é:

`GUIVOS-HOMES-DESIGN-HANDOFF-v6/`

com:

- `00-COMUM`;
- `01-HOME-PESSOA`;
- `02-HOME-ORGANIZACOES-E-COLETIVOS`;
- `03-HOME-MALL`;
- `04-HOME-TRAVEL`;
- `05-HOME-MEDIA`;
- `06-HOME-ADS`;
- `07-HOME-BUSINESS`;
- `08-HOME-INTELLIGENCE`.

Contagem planejada continua:

```text
26 FONTES CANÔNICAS
+
8 LEIA-PRIMEIRO
=
34 ARQUIVOS EXTERNOS
```

### 5.1 Formato e transporte

- Markdown é fonte primária;
- PDF é auxílio opcional de leitura humana;
- ZIP é embalagem opcional;
- Git snapshot é referência reproduzível da emissão;
- nenhum formato derivado substitui a autoridade do GKR;
- o pacote não contém arquivo visual criado pela frente documental.

## 6. Regra de isolamento

Trabalhar uma Home por vez.

```text
00-COMUM
+
LEIA-PRIMEIRO DA HOME
+
DOCUMENTO MESTRE
+
FONTES ESPECÍFICAS NECESSÁRIAS
```

Não carregar documentos específicos de múltiplas Homes por conveniência.

## 7. Regra para IA opcional

Quando a designer utilizar IA:

- usar o mesmo pacote;
- não ampliar silenciosamente as fontes;
- classificar qualquer saída como hipótese/candidato;
- preservar placeholders;
- não inventar dados;
- não promover output automático a decisão do GKR.

A designer pode trabalhar integralmente sem IA.

## 8. Mudança de fonte após emissão

```text
NON-MATERIAL CHANGE
→ REVIEW IMPACT

MATERIAL CHANGE TO MEANING / INVARIANT / SOURCE PACKAGE
→ AFFECTED HOME PACKAGE INVALIDATED FOR NEW WORK
→ REISSUE / REVALIDATE
```

Melhoria puramente criativa da designer não exige reemissão do GKR.

## 9. Gate de emissão v6

A emissão v6 somente pode ocorrer depois de:

1. oito Masters aprovados para Design input;
2. autoridades comuns reconciliadas;
3. 26/26 fontes existentes;
4. ID × versão × path confirmados;
5. zero referência operacional obrigatória a ferramenta específica;
6. oito guias human-first preparados;
7. Semantic Validation = SUCCESS;
8. Mechanical Validation = SUCCESS;
9. revisão independente sem finding material aberto;
10. ato humano explícito para emissão/materialização do snapshot v6.

## 10. Estado

```text
V5
→ FROZEN / HISTORICAL / UNCHANGED

V6 MANIFEST
→ CANDIDATE
→ 26 CANONICAL SOURCES PLANNED
→ 8 HUMAN-FIRST GUIDES PLANNED
→ NOT_EMITTED

DESIGN PRODUCTION RELEASE
→ GRANTED / GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001 v1.1.0

DESIGNER-LED CREATION
→ PRIMARY PATH

AI
→ OPTIONAL

VISUAL IDENTITY
→ DESIGN-OWNED

PRODUCT ENGINEERING
→ NOT RELEASED
```