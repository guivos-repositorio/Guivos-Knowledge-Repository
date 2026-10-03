---
id: ADR-CC-003
title: Pontos de Aplicação dos Guardrails da Captura de Contexto
status: proposed
version: 0.1.0
owner: Guivos
last_updated: 2026-07-19
normative: true
related:
  - PAS-001-CC-UIC-GUARDRAILS-ACCESS-001
  - PAS-001-CC-UIC-NFR-SECURITY-001
---

# ADR-CC-003 — Pontos de Aplicação dos Guardrails

## Status

`Proposed 0.1.0`.

## Contexto

Guardrails apenas documentados não evitam violações. Regras críticas podem ser perdidas se forem aplicadas somente na interface, no consumidor, na Intelligence ou em uma validação tardia.

## Decisão

Distribuir os guardrails por pontos explícitos:

- entrada/edge;
- command handler;
- agregado de domínio;
- política de conteúdo;
- publicação de evento;
- consumidor;
- busca;
- projeção e cache;
- administração;
- observabilidade.

Guardrails de autoridade, finalidade, isolamento, revogação e natureza da informação deverão possuir defesa em profundidade e falha fechada.

## Regras

1. interface nunca é único ponto de proteção;
2. domínio protege invariantes funcionais;
3. política protege finalidade, sensibilidade e acesso;
4. consumidor decide admissibilidade própria;
5. busca autoriza antes da recuperação;
6. observabilidade impede conteúdo proibido;
7. administração não substitui autoridade humana;
8. falha de política nega operação material;
9. cada guardrail possui código, teste e evidência;
10. duplicação de controle deve ser coerente, não contraditória.

## Consequências positivas

- controles verificáveis;
- menor dependência de um componente;
- falhas localizadas e observáveis;
- testes diretamente vinculados a riscos;
- possibilidade de suspensão seletiva.

## Consequências negativas

- maior complexidade de política;
- risco de decisões divergentes entre camadas;
- necessidade de versionamento e testes de consistência;
- custos adicionais de observabilidade.

## Alternativas rejeitadas

### Guardrails somente no frontend

Rejeitada por ser contornável e não cobrir integrações.

### Guardrails somente no domínio

Rejeitada porque busca, logs, mídia e administração possuem riscos fora do agregado.

### Guardrails somente em um serviço central

Rejeitada porque indisponibilidade ou configuração errada criaria ponto único de falha e não substituiria invariantes locais.

## Evidências requeridas

- matriz `GR-001` a `GR-030`;
- testes por ponto de aplicação;
- teste de consistência das decisões;
- exercício de falha do componente de política;
- relatório de negações e violações;
- prova de falha fechada em C0/C1.

## Decisões posteriores

Motor de políticas, formato de regras, sidecar, biblioteca ou serviço de autorização serão avaliados após o readiness.