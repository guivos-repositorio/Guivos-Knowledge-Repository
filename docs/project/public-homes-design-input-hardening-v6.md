---
id: GKR-HOMES-DESIGN-INPUT-HARDENING-V6-001
title: Homes Públicas — Auditoria e Hardening do Pacote de Entrada para Design v6
status: active
version: 0.2.0
owner: Guivos
last_updated: 2026-09-19
normative: false
maturity: remediation_applied_pre_validation
depends_on:
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V5-SNAPSHOT-001
---

# Homes Públicas — Auditoria e Hardening do Pacote de Entrada para Design v6

## 1. Finalidade

Esta frente existe para deixar os arquivos das oito Homes públicas suficientemente completos, claros e autossuficientes para uso por:

- designer humana, com criação manual e liberdade criativa total dentro das fronteiras semânticas;
- sistemas de IA usados opcionalmente como ferramenta de apoio;
- revisão humana posterior;
- handoff contratual sem necessidade de reconstruir contexto por interpretação informal.

A frente não cria Figma, wireframe, UI, protótipo ou baseline visual.

```text
GKR
→ VERDADE / SIGNIFICADO / FUNÇÃO / LIMITES / EVIDÊNCIA / CONTEXTO

DESIGNER
→ EXPRESSÃO VISUAL / CRIATIVA / MATERIALIZAÇÃO

AI
→ FERRAMENTA OPCIONAL DE APOIO
→ CONSUME O MESMO PACOTE GOVERNADO
→ NÃO SUBSTITUI A DESIGNER NEM A AUTORIDADE HUMANA
```

## 2. Decisão humana que governa esta revisão

O fluxo anterior ficou excessivamente centrado em `Figma Make → revisão → Figma final`.

A direção vigente é:

```text
PACOTE DOCUMENTAL COMPLETO
↓
LEITURA / COMPREENSÃO DA DESIGNER
↓
CRIAÇÃO MANUAL LIVRE
↓
IA OPCIONAL, SE A DESIGNER JULGAR ÚTIL
↓
REVISÃO HUMANA
↓
REFINAMENTO E ENTREGA FINAL PELA DESIGNER
```

Nenhuma ferramenta específica é etapa obrigatória.

## 3. Snapshot v5

`delivery/design-handoff-v5` permanece histórico, congelado e imutável.

```text
V5
→ FROZEN
→ NÃO REESCREVER

V6
→ SOMENTE APÓS HARDENING, REVISÃO E VALIDAÇÃO
```

## 4. Findings materiais comprovados

### DH-001 — fluxo operacional excessivamente tool-centric

Documentos comuns tratam `Figma Make / generative exploration` como etapa padrão/esperada.

Decisão:

- remover obrigatoriedade de ferramenta;
- tornar IA opcional;
- tornar criação manual da designer o caminho principal;
- preservar que qualquer saída de IA é não canônica até revisão humana.

### DH-002 — assimetria entre os oito Masters

Pessoa e O/C possuem nível de completude muito superior aos Masters especializados.

Masters especializados precisam alcançar consistência mínima de consumo sem obrigar a designer a reconstruir regras espalhadas.

### DH-003 — responsividade e acessibilidade não estão uniformemente consolidadas

Situação observada nos Masters:

```text
PESSOA
→ EXPLÍCITO

O/C
→ EXPLÍCITO

MALL
→ INSUFICIENTE NO MASTER

TRAVEL
→ INSUFICIENTE NO MASTER

MEDIA
→ EXPLÍCITO

ADS
→ EXPLÍCITO

BUSINESS
→ INSUFICIENTE NO MASTER

INTELLIGENCE
→ INSUFICIENTE NO MASTER
```

Fontes auxiliares não eliminam a necessidade de síntese no Master de consumo.

### DH-004 — autonomia, privacidade e autoridade não estão uniformemente consolidadas

Travel e Media exigem reforço direto no Master. Business e Intelligence possuem material rico em fontes auxiliares, mas devem consolidar o mínimo necessário para consumo direto.

### DH-005 — Header / navegação / acesso não estão uniformemente consolidados

Business e Intelligence não possuem contrato de navegação pública suficientemente explícito no Master.

### DH-006 — classes de verdade e conteúdo não estão uniformemente consolidadas

Os oito Masters devem tornar reconhecíveis, mesmo quando sem usar os rótulos técnicos em todas as seções:

- verdade canônica;
- liberdade criativa;
- copy candidata;
- hipótese de Design;
- placeholder;
- dado real obrigatório;
- questão aberta;
- inferência proibida.

A matriz comum continua sendo a autoridade transversal; os Masters precisam absorver o mínimo necessário para evitar uso incorreto.

### DH-007 — status documental inconsistente com o claim de prontidão

Estado observado:

```text
PESSOA
→ active

O/C
→ active

MALL
→ draft

TRAVEL
→ draft

MEDIA
→ draft

ADS
→ draft

BUSINESS
→ active

INTELLIGENCE
→ draft / v0.1.1
```

Nenhuma Home deve ser tratada como "100% pronta para contrato de Design" enquanto seu Master ainda estiver draft sem adjudicação explícita.

### DH-008 — Business contém restrição visual excessiva

`GKR-UX-HOME-BUSINESS-MASTER-001` e o Source Lock usam:

```text
"DIREÇÃO VISUAL OBRIGATÓRIA"
"DIREÇÃO VISUAL CONGELADA"
```

e priorizam dashboard / KPIs / gráficos.

O requisito legítimo é semântico:

> O valor do Intelligence precisa se tornar tangível e compreensível.

Dashboard, gráfico, KPI, série temporal ou outra representação são hipóteses criativas possíveis, não obrigação visual.

### DH-009 — liberdade criativa precisa ficar inequívoca em todos os Masters

A ausência de identidade visual canônica não é gap.

Devem permanecer Design-owned:

- tipografia;
- paleta;
- imagens;
- fotografia;
- ilustração;
- iconografia;
- composição;
- grid;
- ritmo;
- motion;
- microinterações;
- linguagem gráfica;
- atmosfera;
- expressão de componentes;
- copy e tom não congelados.

### DH-010 — pacote v6 deve ser human-first e AI-compatible

Cada Home deverá ter um ponto de entrada que permita dois modos:

```text
MODO A — DESIGNER HUMANA
→ LEIA-PRIMEIRO
→ MASTER
→ FONTES ESPECÍFICAS NECESSÁRIAS
→ CRIAÇÃO

MODO B — IA OPCIONAL
→ MESMO LEIA-PRIMEIRO
→ MESMO MASTER
→ MESMAS FONTES AUTORIZADAS
→ PROMPT / SOURCE LOCK APENAS COMO ADAPTADOR
```

A IA não recebe uma verdade diferente da designer.

## 5. Matriz de completude obrigatória por Home

Antes da emissão do v6, cada Home precisa passar, no mínimo, por:

1. finalidade e papel;
2. público/participante;
3. pergunta-mãe ou princípio equivalente quando aplicável;
4. tese;
5. Hero e primeira motivação;
6. narrativa/movimentos;
7. Header/navegação/acessos;
8. CTAs e hierarquia de ação;
9. relação com Produtos/participantes;
10. conteúdo/editorial;
11. prova/evidência;
12. dados reais e claims;
13. patrocínio/publicidade/recomendação, quando aplicável;
14. autonomia;
15. privacidade/autoridade;
16. acessibilidade;
17. mobile/responsividade;
18. performance/robustez quando material;
19. liberdade criativa;
20. hipóteses permitidas;
21. placeholders;
22. questões abertas;
23. inferências proibidas;
24. critérios de aceite;
25. não escopo;
26. fontes de aprofundamento;
27. instrução de consumo humano;
28. instrução de consumo por IA opcional.

## 6. Resultado exigido

```text
8 / 8 MASTERS
→ COMPLETE FOR DESIGN INPUT

COMMON HANDOFF
→ HUMAN-FIRST

AI SUPPORT
→ OPTIONAL

TOOL REQUIREMENT
→ NONE

VISUAL IDENTITY CANONICALIZATION
→ NONE

MATERIAL DOCUMENT GAPS
→ 0

V6 SNAPSHOT
→ ONLY AFTER EXACT-HEAD VALIDATION
```

## 7. Limites

Esta frente não autoriza:

- execução de Figma;
- criação de wireframe;
- escolha de identidade visual;
- aprovação de direção artística;
- Product Engineering;
- publicação;
- GTM;
- implementação;
- criação de dados, parceiros, cases ou métricas não sustentados.

---

## 8. Estado de remediação aplicado

Os findings DH-001..DH-010 receberam remediação documental no candidato atual.

```text
DH-001 TOOL-CENTRIC FLOW
→ REMEDIATED

DH-002 MASTER ASYMMETRY
→ REMEDIATED

DH-003 RESPONSIVE / ACCESSIBILITY
→ REMEDIATED

DH-004 AUTONOMY / PRIVACY
→ REMEDIATED

DH-005 HEADER / NAVIGATION
→ REMEDIATED

DH-006 INFORMATION CLASSES
→ REMEDIATED

DH-007 MASTER STATUS
→ REMEDIATED
→ 8 / 8 ACTIVE

DH-008 BUSINESS VISUAL OVERCONSTRAINT
→ REMEDIATED
→ DASHBOARD / KPI / GRAPH = DESIGN_HYPOTHESIS

DH-009 CREATIVE FREEDOM
→ REMEDIATED / EXPLICIT 8 OF 8

DH-010 HUMAN-FIRST / AI-COMPATIBLE
→ REMEDIATED
```

## 9. Prova de completude dos Masters

Matriz aplicada a todas as oito Homes:

```text
ROLE / PURPOSE
QUESTION OR OPENING PRINCIPLE
THESIS
NAVIGATION
CTA
NARRATIVE
PROOF / EVIDENCE
AUTONOMY
PRIVACY / AUTHORITY
ACCESSIBILITY
MOBILE / RESPONSIVENESS
CREATIVE FREEDOM
REAL DATA BOUNDARY
OPEN QUESTIONS
OPTIONAL AI CONSUMPTION
```

Resultado:

```text
PESSOA
→ PASS

ORGANIZAÇÕES E COLETIVOS
→ PASS

MALL
→ PASS

TRAVEL
→ PASS

MEDIA
→ PASS

ADS
→ PASS

BUSINESS
→ PASS

INTELLIGENCE
→ PASS

TOTAL
→ 8 / 8 PASS
```

Todos os oito Masters estão:

```text
status = active
maturity = design_input_ready_human_first_ai_optional
```

## 10. Prova do Manifesto v6

As 26 fontes declaradas em `GKR-UX-HOMES-DESIGN-DELIVERY-001 v6.0.0` foram verificadas no candidato.

```text
FILES FOUND
→ 26 / 26

ID MATCH
→ 26 / 26

VERSION MATCH
→ 26 / 26
```

O snapshot v5 permanece inalterado.

## 11. Guias human-first

`GKR-HOMES-DESIGN-INPUT-V6-GUIDES-001 v1.0.0` define integralmente os oito blueprints de `LEIA-PRIMEIRO`.

```text
GUIDE BLUEPRINTS
→ 8 / 8 COMPLETE

PRIMARY CONSUMER
→ HUMAN DESIGNER

AI APPENDIX
→ OPTIONAL

POST-MERGE SHAs
→ DELIBERATELY PENDING
→ MUST BE FILLED ONLY AT SNAPSHOT EMISSION
```

## 12. Estado pré-validação

```text
CONTENT HARDENING
→ APPLIED

8 / 8 MASTERS
→ DESIGN-INPUT-READY CANDIDATE

26 / 26 MANIFEST SOURCES
→ ID / VERSION / PATH VERIFIED

8 / 8 GUIDE BLUEPRINTS
→ COMPLETE

COMMON AUTHORITIES
→ HUMAN-FIRST / AI-OPTIONAL / TOOL-AGNOSTIC

V6 SNAPSHOT
→ NOT_EMITTED

SEMANTIC VALIDATION
→ PENDING

MECHANICAL VALIDATION
→ PENDING

INDEPENDENT REVIEW
→ PENDING

MAIN
→ UNCHANGED

PRODUCT ENGINEERING
→ NOT RELEASED
```
