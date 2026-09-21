---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.53.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-21
related:
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-BUSINESS-001
  - PAS-001-DOMAIN-MODEL-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-UX-ORGCOL-AUTH-NAV-MAT-001
  - GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001
  - GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001
  - GKR-UX-ORGCOL-AUTH-HIFI-ELIGIBILITY-001
  - GKR-UX-ORGCOL-AUTH-HIFI-AUTH-001
normative: false
---

# Jornadas Integradas

## 1. Finalidade

Esta seção descreve a continuidade corrente entre Homes públicas e experiências de **Pessoa, Coletivo, Organização e Guivos Business**.

Pessoa, Coletivo e Organização são contextos de participante. Guivos Business é um **produto especializado B2B** com contexto próprio de experiência e não deve ser confundido com Organização, Ads ou uma camada genérica "Comercial".

Ela deve ser lida como topologia funcional atual, não como cronologia de construção.

## 2. Vistas correntes

- [Jornada da Pessoa](person.md)
- [Jornada do Coletivo](collective.md)
- [Jornada da Organização](organization.md)
- [Experiência Integrada do Guivos Business](business.md)
- [Catálogo Integrado de Telas](screen-catalog.md)
- [Registro Granular de Superfícies e Estados](surface-registry.md)
- [Registro Granular de Transições](transition-registry.md)
- [Handoffs entre participantes](handoffs.md)
- [Cenários integrados](scenarios.md)
- [Lacunas e Continuidades Ausentes](gaps.md)

## 3. Topologia corrente

```text
PESSOA
→ HOME PÚBLICA
→ ENTRADA PROTEGIDA
→ COMPREENSÃO / HOJE
→ OBJETIVOS / PRÓXIMOS PASSOS / EVOLUÇÃO
→ OPORTUNIDADES
→ EXPERIÊNCIAS / FRONTEIRAS EXTERNAS

COLETIVO
→ HOME PÚBLICA
→ DESCOBERTA / PARTICIPAÇÃO
→ EXPERIÊNCIA AUTENTICADA
→ RESPONSABILIDADE / SOLICITAÇÕES / CONTINUIDADE

ORGANIZAÇÃO
→ HOME PÚBLICA
→ EXPERIÊNCIA AUTENTICADA
→ CAPACIDADES / OPORTUNIDADES / RELAÇÕES / CONTINUIDADE

BUSINESS
→ HOME GUIVOS BUSINESS
→ OFERTAS / INTELLIGENCE / PLANOS
→ CONFIGURADOR
→ CONTRATAÇÃO ONLINE
→ SELF-SERVICE / SUPORTE / GERENCIADO
→ OPERAÇÃO
```

## 4. Domínios de Evolução

As jornadas de **Pessoa, Coletivo e Organização** reconhecem os nove domínios canônicos dentro de seus limites aplicáveis. Business não se torna participante nem recebe score ou domínio próprio por essa razão.

`Ainda estou descobrindo` é estado legítimo de exploração, não um décimo domínio.

Domínio não é score, diagnóstico, prioridade imposta ou prova automática de evolução.

## 5. Pessoa — responsabilidades correntes

```text
HOJE
├── MEUS OBJETIVOS
├── MEUS PRÓXIMOS PASSOS
└── MINHA EVOLUÇÃO
```

Essas responsabilidades preservam autonomia, contexto, privacidade e explicabilidade. Abrir ou retornar de uma superfície não cria progresso, prioridade, aceitação ou evolução automaticamente.

## 6. Oportunidades e fronteira externa

```text
ORGANIZAÇÃO PUBLICA
→ OPORTUNIDADE ELEGÍVEL
→ MAPA / LISTA
→ DETALHE
→ REVISÃO CONSCIENTE
→ FRONTEIRA EXTERNA
```

A Guivos governa a experiência até a transferência consciente de autoridade. O processo de terceiro permanece fora da autoridade da Guivos.

## 7. Planos

- Pessoa: `Free · Plus · Pro`;
- Coletivo: `Livre · Mobiliza · Impacta · Rede`;
- Organização: `Conecta · Eleva · Transforma`;
- Guivos Business: `Start · Growth · Scale · Enterprise`, como produto separado.

Abrir Planos não inicia cobrança nem altera consentimento, capacidade ou relevância.

## 8. Organização e Coletivo autenticados

```text
INFORMATION ARCHITECTURE
→ SURFACE MAP
→ STATE MAP
→ PRIORITY FLOWS
→ NAVIGATION MATERIALIZATION
→ LOW-FIDELITY DELIVERY
→ LOW-FIDELITY VALIDATION
→ HIGH-FIDELITY ELIGIBILITY
→ HIGH-FIDELITY AUTHORIZATION
```

O Design high-fidelity autenticado de Organização e Coletivo está **autorizado e ainda não iniciado**. Protótipo interativo e implementação permanecem gates separados e não autorizados por essa decisão.

## 9. Autoridades para prototipação

```text
SCREEN CATALOG
→ responsibilities

SURFACE REGISTRY
→ states / ownership / maturity

TRANSITION REGISTRY
→ allowed transitions / effects / limits

PERSON / COLLECTIVE / ORGANIZATION VIEWS
→ participant-specific continuity

BUSINESS VIEW
→ product-specific continuity
```

## 9.1 Separação Business × Ads / Opportunity Boost

```text
GUIVOS BUSINESS
→ PRODUTO ESPECIALIZADO B2B
→ START / GROWTH / SCALE / ENTERPRISE
→ CONTRATAÇÃO ONLINE / SELF-SERVICE QUANDO ELEGÍVEL

GUIVOS ADS / OPPORTUNITY BOOST
→ PRODUTO PUBLICITÁRIO DISTINTO
→ COM-* NO REGISTRY POR LEGADO DE IDENTIFICADOR

BND-*
→ FRONTEIRAS DOCUMENTAIS
→ NÃO SÃO BUSINESS
→ NÃO SÃO PARTICIPANTES
```

A expressão histórica `COM-*` não cria um quarto participante chamado "Comercial" e não representa Guivos Business.

## 10. Exclusões de consumo

```text
HISTORICAL UXA SEQUENCE
SNAPSHOT COUNTS
OLD SVG INVENTORY
CHECKPOINT NARRATIVES
CLOSED AUDITS
→ NOT REQUIRED FOR DESIGN / AI
```

## 11. Estado

```text
JOURNEY DOCUMENTATION
→ CURRENT

DESIGN / PROTOTYPING INPUT
→ CURRENT VIEWS + CURRENT REGISTRIES

HISTORICAL RECONSTRUCTION
→ NOT REQUIRED

O/C HIGH-FIDELITY DESIGN
→ AUTHORIZED / NOT_STARTED

INTERACTIVE PROTOTYPE
→ NOT_AUTHORIZED

IMPLEMENTATION
→ SEPARATE GATE
```
