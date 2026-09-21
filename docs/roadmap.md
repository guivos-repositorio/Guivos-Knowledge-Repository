---
id: ROADMAP-13.48.7
title: Roadmap Arquitetural — Frentes Correntes e Próximos Gates da Guivos
status: active
version: 13.48.15
owner: Guivos
last_updated: 2026-09-21
normative: true
related:
  - GKR-STATE-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-BUSINESS-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
  - GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001
  - GKR-UX-ORGCOL-AUTH-HIFI-AUTH-001
  - GKR-UX-PER002-PROTOTYPE-REVALIDATION-001
  - GPA-004
  - GPA-006
  - GIA-000
  - GIA-COG-001
  - ADR-008
  - RP-002-PMF-001
  - GOG-001
  - GKR-BRAND-SIGNATURE-001
  - GTM-007
  - M7.88
---

# Roadmap Arquitetural — Frentes Correntes e Próximos Gates da Guivos

## 1. Função

Este roadmap traduz `GKR-STATE-001 v3.50.8` em **frentes governadas de avanço**.

Ele não é cronologia do projeto, inventário de versões antigas, registro de PRs, histórico de auditoria ou autorização automática para executar a próxima coisa tecnicamente possível.

```text
ROADMAP
→ ORIENTA O PRÓXIMO MOVIMENTO LEGÍTIMO

ROADMAP
≠ FILA AUTOMÁTICA
≠ REGISTRO HISTÓRICO
≠ AUTORIZAÇÃO DE IMPLEMENTAÇÃO
```

A auditoria integral anterior está concluída. Lotes, findings resolvidos, SHAs, baselines e checkpoints usados para chegar ao estado corrente pertencem ao documento próprio de auditoria e ao Git; não orientam a execução futura por si só.

## 2. Estado base corrente

| Frente | Estado vigente |
|---|---|
| Estado global | `GKR-STATE-001 v3.50.8 / CURRENT` |
| Era | `GE-2 — KNOWLEDGE` |
| Marco funcional | `M7.88` |
| Última UXA numerada | `UXA-101` |
| Homes públicas | `8 / 8 READY FOR EXTERNAL DESIGN` |
| Manifesto de Design | `GKR-UX-HOMES-DESIGN-DELIVERY-001 v7.0.31` |
| Read-First das Homes | `8 / 8 CURRENT / NON-NORMATIVE` |
| Design das Homes | `DESIGNER-FIRST / AI OPTIONAL / TOOL-NEUTRAL` |
| Journey | vistas e registries correntes ativos |
| Business | `Start · Growth · Scale · Enterprise` / contratação online / Self-service quando elegível |
| O/C low-fidelity autenticado | `DELIVERY v0.1.0 + VALIDATION v1.0.0 / PASS` |
| O/C high-fidelity | `AUTHORIZED / NOT_STARTED` |
| O/C protótipo interativo | `NOT_AUTHORIZED` |
| PER-002 | referência interativa pós-review validada |
| UXA-102 / V5 | `NOT_STARTED` |
| Cognitive Reference Architecture | `GIA-COG-001 v0.1.1 / ACTIVE / NORMATIVE` |
| `GIA-COG-002..008` | `RESERVED / NOT MATERIALIZED` |
| Product Engineering | `PAUSED / NOT RELEASED` |
| PMF | `NOT VALIDATED` |
| Próxima execução automática | `NONE` |

## 3. Regras permanentes de execução

Toda frente deve responder:

1. existe necessidade estratégica ou funcional real?
2. qual autoridade corrente governa a decisão?
3. quais dependências precisam estar atuais?
4. a frente exige documentação, Design, implementação ou realidade operacional?
5. qual gate impede promoção indevida de maturidade?
6. o avanço cria nova verdade ou apenas elimina fragmentação?
7. todo conhecimento material validado será preservado?

```text
ATUALIZAR AUTORIDADE VIGENTE
→ PREFERÍVEL A CRIAR NOVO ADENDO

ABSORVER CONTEÚDO VÁLIDO
→ ANTES DE REMOVER ARTEFATO

CURRENT MAIN
→ FONTE PRIMÁRIA DA VERDADE

GIT
→ HISTÓRICO / PROVENIÊNCIA

SNAPSHOT
→ SOMENTE QUANDO HOUVER NECESSIDADE REAL DE FREEZE / TRANSPORTE

CANDIDATE
→ NÃO CRIADO POR PADRÃO

DOCUMENTAÇÃO
≠ IMPLEMENTAÇÃO

AUTORIZAÇÃO
≠ EXECUÇÃO AUTOMÁTICA
```

## 4. Frente corrente — Experiência e Journey current-only

Objetivo:

> permitir que humanos, Design e IA opcional consumam somente autoridades correntes sem reconstruir o histórico do GKR.

Estado:

```text
CURRENT MAIN
→ PRIMARY SOURCE OF TRUTH

CURRENT MANIFEST
→ CURRENT DESIGN SOURCE SET

HOME MASTERS
→ 8 / 8 CURRENT

READ-FIRST
→ 8 / 8 CURRENT

JOURNEY
→ CURRENT VIEWS + CURRENT REGISTRIES

HISTORICAL PRODUCERS
→ REMOVE FROM CURRENT CORPUS ONLY AFTER ABSORPTION IS PROVEN
```

Próximos atos permitidos nesta frente:

- continuar auditoria de documentos correntes;
- remover apenas artefatos cuja função esteja comprovadamente absorvida;
- corrigir dependências, versões, links, IDs, navegação e nomenclatura;
- preservar validações que ainda exerçam autoridade funcional;
- manter Design e IA consumindo o conjunto corrente;
- executar revisão independente do conjunto antes de qualquer gate humano de integração.

Esta frente **não** cria snapshot, Figma, protótipo, implementação ou Product Engineering por inferência.

## 5. Homes públicas — execução externa de Design

As oito Homes estão liberadas para produção externa de Design pela designer.

```text
DESIGNER
→ CREATIVE AUTHOR
→ MANUAL WORK = FIRST-CLASS

AI
→ OPTIONAL / DESIGNER-CONTROLLED

UNIVERSAL DESIGN AUTHORITIES
→ 4 / 4

OPTIONAL AI AUTHORITY
→ 1 / 1 WHEN AI IS USED

READ-FIRST
→ 8 / 8

SNAPSHOT PRECONDITION
→ NONE

GKR-CREATED FIGMA
→ NONE
```

O GKR governa significado, função, narrativa, papéis, autoridade, limites e evidências. Tipografia, paleta, fotografia, ilustração, grid, composição, componentes, motion, atmosfera e direção visual pertencem à designer, salvo regra ou texto explicitamente congelado.

Journey é carregada adicionalmente somente quando a solução atravessar da Home pública para experiência autenticada.

Design das Homes não libera publicação, implementação ou Product Engineering.

## 6. Organização e Coletivo autenticados

A cadeia principal está documentalmente fechada até a autorização high-fidelity:

```text
JOBS / AUTORIDADE
→ INFORMATION ARCHITECTURE
→ SURFACE MAP
→ STATE MAP
→ PRIORITY FLOWS
→ NAVIGATION MATERIALIZATION
→ LOW-FIDELITY DELIVERY
→ LOW-FIDELITY VALIDATION / PASS
→ HIGH-FIDELITY ELIGIBILITY / PASS
→ HIGH-FIDELITY AUTHORIZATION / GRANTED
```

Estado corrente:

```text
O/C HIGH-FIDELITY DESIGN
→ AUTHORIZED
→ NOT_STARTED

INTERACTIVE PROTOTYPE
→ NOT_AUTHORIZED

PRODUCT ENGINEERING
→ NOT RELEASED
```

A execução high-fidelity não é automática. Capacidades especializadas ainda abertas permanecem registradas em `GKR-JOURNEY-GAPS-001` e nos Surface Registries; não reabrem a cadeia principal já fechada.

## 7. Pessoa — PER-002 e continuidade

`PER-002` possui referência interativa pós-review validada. Isso não cria execução automática posterior.

```text
PER-002
→ CURRENT INTERACTIVE REFERENCE EXISTS
→ POST-REVIEW REVALIDATION = PASS

AUTHENTICATION
→ INTERNAL GATE / STATE
→ ≠ MATERIAL PROCESSING AUTHORIZATION

FIRST DISTINCT DOWNSTREAM SURFACE
→ PER-003 — ESCOLHA DE MODALIDADE

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```

Qualquer nova materialização, teste real, implementação ou avanço de `UXA-102/V5` depende de ato próprio.

## 8. Guivos Business

`GPA-004 v1.7.4` governa a arquitetura funcional do Guivos Business.

```text
BUSINESS
→ PRODUTO ESPECIALIZADO B2B
→ CONTEXTO PRÓPRIO DE EXPERIÊNCIA
→ ≠ ORGANIZAÇÃO
→ ≠ ADS / COM-*
→ ≠ BND-002

PLANOS
→ START
→ GROWTH
→ SCALE
→ ENTERPRISE

CONTRATAÇÃO
→ ONLINE

SELF-SERVICE
→ WHEN ELIGIBLE

SUPPORT / MANAGED
→ WHEN COMPLEXITY REQUIRES
```

Não existe equivalência Pontos ↔ BRL aprovada como regra econômica vigente.

Permanecem dependentes de formalização/implementação própria, conforme `GKR-JOURNEY-GAPS-001`:

- preços/faixas ainda não governados;
- implementação do configurador;
- cobrança, tributação e liquidação reais;
- critérios operacionais exatos de roteamento;
- integrações/API/exportações contratadas;
- publicação operacional da experiência Business.

## 9. Guivos Intelligence, dados e tecnologia

`GPA-006` governa o produto. `GIA-000`, `GAI-001`, `GAI-002` e `GIA-COG-001` governam princípios e arquiteturas subordinadas.

```text
GIA-COG-001
→ ACTIVE / NORMATIVE
→ CONCEPTUAL / REFERENCE

GIA-COG-002..008
→ RESERVED / NOT MATERIALIZED

NEO4J
→ REFERENCE_SELECTED
→ ≠ PRODUCTION

GRAPHRAG
→ CANDIDATE
→ ≠ IMPLEMENTATION

PHYSICAL ARCHITECTURE / REAL DATA / PRODUCTION
→ NOT AUTHORIZED BY DOCUMENTARY MATURITY
```

A Home Intelligence está pronta para Design externo; isso não comprova capacidade tecnológica operacional.

## 10. Mercado, Research e evidência

Continuam dependentes de realidade:

- aplicação da validação B2C;
- PMF;
- disposição a pagar;
- retenção/recorrência;
- uso e resultado real das ofertas;
- impacto real;
- causalidade quando alegada;
- performance real das Homes;
- performance GTM.

```text
MÉTODO DEFINIDO
≠ INSTRUMENTO APLICADO
≠ BASE VÁLIDA
≠ KPI CALCULADO
≠ DECISÃO DE MERCADO
≠ PMF
```

Simulações sintéticas e maturidade documental não constituem evidência humana ou de mercado.

## 11. Marca e filing

Autoridade institucional:

```text
Possibility, lived.
Possibilidade, vivida.
#PossibilityLived
```

Autoridade pessoal:

```text
Do possível ao vivido.
→ FUNDADOR
```

O filing continua dependente de **Human Filing Authorization** e demais atos próprios.

```text
FILE
≠ FILING_AUTHORIZED

CLEAR
≠ REGISTRO
```

Documentação não autoriza gasto, GRU ou protocolo.

## 12. Internacionalização

Planejamento territorial não equivale a mercado ativo.

Sequência de referência permanece condicionada a gates próprios:

```text
BRASIL
→ EXPANSÃO NACIONAL SELETIVA
→ PORTUGAL QUANDO GATES FOREM ATENDIDOS
→ NOVO PAÍS SOMENTE POR NOVA AUTORIZAÇÃO
```

Entidade, fiscalidade, pagamentos, suporte, compliance e operação internacional exigem realidade operacional própria.

## 13. Jurídico, privacidade e institucional

```text
POLÍTICA PUBLICADA
≠ CONFORMIDADE OPERACIONAL COMPROVADA

CONCEITO INSTITUCIONAL
≠ ENTIDADE CONSTITUÍDA

DOCUMENTAÇÃO DE PRIVACIDADE
≠ CONTROLE TÉCNICO IMPLEMENTADO
```

Nenhuma maturidade documental promove execução jurídica, constituição institucional ou compliance operacional por inferência.

## 14. Preservações transversais

```text
ORGANIZAÇÃO ≠ GUIVOS BUSINESS ≠ GUIVOS ADS
EMPRESA CONTRATANTE ≠ NOVO PARTICIPANTE ESTRUTURAL
OFERTA ≠ PLANO ≠ ESCALA ≠ ORÇAMENTO ≠ IMPLEMENTAÇÃO
CONTRATAÇÃO ONLINE ≠ MODELO DE OPERAÇÃO
CUSTEIO DA JOURNEY ≠ PROPRIEDADE DA JOURNEY
PONTOS ≠ EVOLUÇÃO ≠ RELEVÂNCIA ≠ PRIORIDADE
VALOR DE IMPACTO LIBERADO ≠ IMPACTO REALIZADO ≠ IMPACTO COMPROVADO
INTELLIGENCE BUSINESS ≠ INGESTÃO OBRIGATÓRIA DE KPIs INTERNOS
INTELLIGENCE APOIANDO BUSINESS ≠ MÓDULO BUSINESS
ENTITLEMENT ≠ AUTORIDADE
MAIOR PLANO ≠ MENOR PRIVACIDADE
GRAPH / KNOWLEDGE / ANALYTICS / AI ≠ IDENTIDADE DO PRODUTO
NEO4J = REFERENCE_SELECTED ≠ PRODUCTION
GRAPHRAG = CANDIDATE ≠ IMPLEMENTATION
GUIVOS.AI ≠ GUIVOS INTELLIGENCE
PERCEBER ANTES ≠ PREVER O FUTURO
ACTIVE / NORMATIVE REFERENCE ARCHITECTURE ≠ IMPLEMENTATION AUTHORIZATION
GUIVOS ≠ FUNDADOR
HOME DOCUMENTADA ≠ HOME IMPLEMENTADA
SOURCE LOCK ≠ AUTORIZAÇÃO AUTOMÁTICA DE DESIGN
DESIGN AUTHORIZATION ≠ DESIGN DELIVERY ≠ VALIDATION
PROTOTYPE ≠ IMPLEMENTED PRODUCT
DISPLAYED ≠ UNDERSTOOD
CLICKED ≠ UNDERSTOOD
ACEITE CONTRATUAL ≠ CONSENTIMENTO LGPD
PLANEJAMENTO GTM ≠ EXECUÇÃO GTM
```

## 15. Regra do próximo movimento

Não existe próxima execução automática.

```text
NEXT AUTOMATIC EXECUTION
→ NONE

CURRENT DOCUMENTARY FRONT
→ EXPERIENCE / JOURNEY CURRENT-ONLY CONSOLIDATION

PUBLIC HOME DESIGN
→ RELEASED FOR EXTERNAL DESIGNER

O/C HIGH-FIDELITY EXECUTION
→ AUTHORIZED / NOT_STARTED
→ SEPARATE EXECUTION ACT

O/C INTERACTIVE PROTOTYPE
→ NOT_AUTHORIZED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED

REAL MARKET EVIDENCE
→ NOT YET PROVEN

SNAPSHOT
→ NOT REQUIRED BY DEFAULT
```

Qualquer avanço deve partir da autoridade temática vigente e do gate específico aplicável.

## 16. Limite de proveniência histórica

A auditoria integral anterior permanece disponível em `GKR-FULL-CORPUS-AUDIT-001` e no Git.

```text
AUDIT LOTS / FINDINGS / PRs / SHAs / HISTORICAL BASELINES
→ PROVENANCE

CURRENT ROADMAP
→ CURRENT FRONTS + CURRENT GATES

HISTORY
→ MUST NOT RE-ENTER EXECUTION BY INFERENCE
```

O Roadmap corrente não exige reconstrução do processo que levou ao estado atual.
