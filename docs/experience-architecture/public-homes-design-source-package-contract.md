---
id: GKR-UX-HOMES-DESIGN-SOURCE-PACKAGE-001
title: Homes Públicas — Contrato Canônico do Pacote-Fonte para Design e IA
status: active
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-09-19
normative: true
maturity: source_package_reconciled_pre_v6_snapshot
depends_on:
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
related:
  - GKR-UX-HOMES-DESIGN-DELIVERY-V5-SNAPSHOT-001
  - GKR-STATE-001
---

# Homes Públicas — Contrato Canônico do Pacote-Fonte para Design e IA

## 1. Finalidade

Esta autoridade define o que a Guivos entrega à designer e como sistemas de IA podem consumir a mesma base documental para apoiar criação, análise ou exploração.

A entrega governada pelo GKR é documental.

~~~text
GKR
→ VERDADE / SIGNIFICADO / FUNÇÃO / LIMITES / EVIDÊNCIA / CONTEXTO
→ DOCUMENTOS MESTRES + FONTES + SOURCE LOCKS + GUARDRAILS

DESIGNER
→ CRIA MANUALMENTE
→ DEFINE EXPRESSÃO VISUAL
→ CONSTRÓI O FIGMA
→ PRESERVA TOTAL LIBERDADE CRIATIVA DENTRO DOS BOUNDARIES

SISTEMAS DE IA
→ PODEM CONSUMIR O MESMO PACOTE
→ APOIO OPCIONAL
→ NÃO SÃO ETAPA OBRIGATÓRIA
→ NÃO CRIAM AUTORIDADE VISUAL
~~~

Esta autoridade substitui qualquer interpretação operacional segundo a qual Figma Make, um protótipo gerado por IA ou qualquer ferramenta generativa seria etapa obrigatória antes do trabalho da designer.

## 2. Regra de primazia

~~~text
DOCUMENTAÇÃO GKR → FONTE DE VERDADE
DESIGN MANUAL → FORMA PRIMÁRIA DE MATERIALIZAÇÃO VISUAL
IA → CONSUMIDOR OPCIONAL DA DOCUMENTAÇÃO
OUTPUT DE IA → NÃO CANÔNICO / NÃO APROVADO POR PADRÃO
~~~

A designer não precisa reproduzir, consultar ou partir de qualquer material visual gerado por IA.

## 3. Liberdade criativa protegida

Não são canonicalizados pelo GKR antes do Design:

- identidade visual da Home;
- tipografia;
- paleta;
- fotografia, vídeo, ilustração e imagem gerada;
- iconografia;
- direção de arte;
- composição, grid, ritmo e densidade;
- motion e microinterações;
- aparência de componentes;
- atmosfera e linguagem gráfica;
- forma visual de agrupar movimentos narrativos;
- copy e tom não congelados.

~~~text
DESIGN FREEDOM
≠ PRODUCT REDEFINITION
≠ FACTUAL INVENTION
≠ CLAIM SEM EVIDÊNCIA
≠ ALTERAÇÃO DE AUTORIDADE
~~~

A ausência de identidade visual canônica prévia não é lacuna. É decisão deliberada para preservar autoria, originalidade e capacidade criativa da designer.

## 4. O que o pacote deve fornecer

Antes da entrega à designer, cada Home deve permitir responder sem reconstrução histórica:

1. o que esta Home é;
2. para quem ela existe;
3. qual pergunta-mãe governa sua abertura;
4. qual tese e progressão narrativa devem sobreviver;
5. quais movimentos são função de significado e não layout obrigatório;
6. quais participantes, produtos e capacidades não podem ser confundidos;
7. quais CTAs, boundaries e transições possuem função específica;
8. quais claims exigem evidência real;
9. o que pode ser placeholder;
10. quais decisões permanecem abertas ao Design;
11. o que é proibido inferir;
12. como mobile, acessibilidade, fallback e reduced motion preservam significado;
13. quais documentos são fonte inicial e quais são aprofundamento;
14. qual checkpoint/versionamento governa o pacote.

Se uma dessas respostas depender de reconstrução por múltiplos documentos históricos, o pacote não está pronto.

## 5. As oito classes obrigatórias

Todo 00-LEIA-PRIMEIRO / SOURCE LOCK deve separar explicitamente:

1. CANONICAL;
2. DESIGN_CREATIVE;
3. CONTENT_CANDIDATE;
4. DESIGN_HYPOTHESIS;
5. PROTOTYPE_PLACEHOLDER;
6. REAL_DATA_REQUIRED;
7. OPEN_QUESTION;
8. PROHIBITED_INFERENCE.

A classificação existe para ampliar liberdade com segurança, não para transformar Design em preenchimento mecânico.

## 6. Consumo pela designer

Ordem recomendada de leitura:

~~~text
00-COMUM
↓
00-LEIA-PRIMEIRO / SOURCE LOCK DA HOME
↓
DOCUMENTO MESTRE DA HOME
↓
FONTES ESPECÍFICAS DA HOME
↓
APROFUNDAMENTO, SOMENTE QUANDO NECESSÁRIO
~~~

O pacote não deve obrigar a designer a conhecer o histórico completo do GKR, comparar versões superseded, adivinhar o que é copy final, dado real ou placeholder, usar ferramenta específica ou seguir template visual pré-imposto.

## 7. Consumo por sistemas de IA

IA deve consumir a mesma verdade entregue à designer.

- uma Home por contexto quando possível;
- fontes comuns + Source Lock + fontes específicas;
- não carregar indiscriminadamente documentos históricos;
- não criar fatos para preencher lacunas;
- não promover hipótese a regra;
- não converter referência visual em autoridade;
- identificar claramente suposições;
- tratar OPEN_QUESTION como aberta;
- tratar REAL_DATA_REQUIRED como bloqueio de factualidade;
- preservar PROHIBITED_INFERENCE;
- retornar proposta como material de apoio, nunca como decisão.

Prompts são conveniência de consumo. Prompt não é especificação de Design.

## 8. Materiais Figma existentes

Materiais existentes no Figma podem ser consultados pela designer quando forem úteis para componentes, ativos, tokens, padrões técnicos, aprendizado do sistema anterior ou consistência operacional.

~~~text
FIGMA EXISTENTE → REFERÊNCIA OPCIONAL
FIGMA EXISTENTE ≠ AUTORIDADE SEMÂNTICA
FIGMA EXISTENTE ≠ BASELINE VISUAL OBRIGATÓRIA
FIGMA EXISTENTE ≠ RESTRIÇÃO À CRIATIVIDADE
~~~

A designer pode preservar, adaptar, evoluir ou substituir soluções visuais anteriores, desde que respeite as verdades e boundaries do GKR.

## 9. Regras para conteúdo e evidência

Nenhum sistema humano ou de IA pode inventar como fato pessoas, organizações, coletivos, parceiros, métricas, resultados, cases, depoimentos, preços, disponibilidade, cobertura, performance, tecnologia operacional, números de usuários, relações comerciais, impacto ou causalidade.

Quando a composição precisa de volume visual sem dado real, usar PROTOTYPE_PLACEHOLDER de forma identificável.

## 10. Critério de completude do pacote

~~~text
MASTER DOCUMENTS → 8 / 8 CURRENT
PER-HOME SOURCE LOCKS → 8 / 8 COMPLETE
COMMON CONTRACTS → CURRENT / NON-CONTRADICTORY
EIGHT CLASS MATRIX → 8 / 8 HOMES COMPLETE
REAL DATA BOUNDARIES → EXPLICIT
OPEN QUESTIONS → EXPLICIT
PROHIBITED INFERENCES → EXPLICIT
MOBILE / RESPONSIVE PRINCIPLES → EXPLICIT
ACCESSIBILITY / FALLBACK → EXPLICIT
AI CONSUMPTION → OPTIONAL / SAFE / SAME SOURCE OF TRUTH
TOOL MANDATE → NONE
VISUAL IDENTITY PRE-LOCK → NONE
HISTORICAL/SUPERSEDED CONFLICT IN INITIAL PACKAGE → NONE
CHECKPOINT / VERSION / SOURCE INVENTORY → REPRODUCIBLE
~~~

## 11. Modelo operacional correto

~~~text
GKR COMPLETES SOURCE PACKAGE
↓
HUMAN VALIDATION OF COMPLETENESS
↓
PACKAGE / SNAPSHOT EMISSION
↓
DESIGNER RECEIVES DOCUMENTATION
↓
DESIGNER CREATES MANUALLY
   ↘ OPTIONAL AI SUPPORT
↓
HUMAN DESIGN REVIEW
↓
DESIGNER REFINES / FINALIZES
~~~

O GKR não produz o arquivo Figma da designer.

## 12. Relação com o Design Production Release

GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001 continua significando que a frente externa de Design pode consumir o pacote governado. Não significa obrigação de Figma Make, execução automática por IA, criação de protótipo pelo GKR, direção visual aprovada, Figma final aprovado, implementação ou Product Engineering.

## 13. Estado

~~~text
SOURCE PACKAGE CONTRACT → DEFINED / ACTIVE / NORMATIVE
DESIGNER MANUAL CREATION → PRIMARY MATERIALIZATION MODE
AI SUPPORT → OPTIONAL / DOCUMENT-CONSUMER ONLY
FIGMA MAKE MANDATORY FLOW → NOT APPLICABLE
VISUAL IDENTITY PRE-LOCK → NOT REQUIRED
V5 SNAPSHOT → HISTORICAL FROZEN DELIVERY
NEXT GOVERNED FRONT → RECONCILE CURRENT AUTHORITIES / AUDIT 8/8 HOME SOURCE PACKAGES / PREPARE V6 CANDIDATE
~~~
