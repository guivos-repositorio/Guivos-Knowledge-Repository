---
id: CANONICAL-CONSOLIDATION-MATRIX-UIC-01-W0-01-CHARTER-ADDENDUM
title: Matriz de Consolidação Canônica — Addendum W0-01 Charter
status: active
version: 1.38.0
owner: Guivos
last_updated: 2026-07-20
supersedes_partial:
  - CANONICAL-CONSOLIDATION-MATRIX-UIC-01-WAVE-0-PLANNING-ADDENDUM
related:
  - PAS-001-CC-UIC-001-OVERLAY-0.7.0
  - PAS-001-CC-W0-01-CHARTER-001
  - M5.18
---

# Matriz de Consolidação Canônica — Addendum W0-01 Charter

## 1. Regra de precedência

Este addendum prevalece somente sobre:

- estado corrente da UIC-01;
- charter e readiness do W0-01;
- blockers de autorização;
- marco vigente;
- ponto de retomada.

Não substitui autoridades funcionais, técnicas ou de planejamento anteriores.

## 2. Fontes novas

| ID | Autoridade |
|---|---|
| PAS-001-CC-W0-01-CHARTER-001 | escopo, autorização, pacotes e limites |
| PAS-001-CC-W0-01-OWNERS-001 | owners, RACI, segregação e bloqueios |
| PAS-001-CC-W0-01-REPO-001 | repositório, branches, PRs e versões |
| PAS-001-CC-W0-01-PIPELINE-001 | checks, logs, artefatos e exceções |
| PAS-001-CC-W0-01-SYNTHETIC-DATA-001 | dados e mídia sintéticos |
| PAS-001-CC-W0-01-EVIDENCE-001 | EV-017/018 e armazenamento |
| PAS-001-CC-W0-01-DECISIONS-001 | sequência de ADRs bloqueantes |
| PAS-001-CC-W0-01-READINESS-001 | gates e estado verificável |

## 3. Consolidação de estado

| Questão | Estado efetivo |
|---|---|
| readiness arquitetural | 100% |
| planejamento da Onda 0 | concluído |
| charter do W0-01 | definido |
| execução do W0-01 | não iniciada |
| owners técnicos | pendentes e bloqueantes |
| repositório de implementação | proposto, não criado |
| stack | não escolhida |
| EV-017/018 | planejadas, não produzidas |
| produção | não autorizada |

## 4. Decisões reconciliadas

- separar GKR e repositório de implementação;
- propor repositório privado `Guivos-Capture-Context`;
- iniciar com monólito modular sem topologia definitiva;
- bloquear execução até owners nominais;
- impedir dados reais e uso da VAL-002 como fixtures;
- exigir PR, checks e evidência;
- decidir ADR-TCC-001/006 antes do W0-02;
- manter W0-02 dependente de decisão separada.

## 5. Não conflito

O pacote não altera:

- autoridade humana;
- contratos de domínio;
- lifecycle;
- schemas propostos;
- storage, indexação e guardrails;
- NFR, SLO e threat model;
- plano W0-01 a W0-08;
- UIC-02 a UIC-09;
- programa VAL.

## 6. Blockers normativos

Os seguintes blockers não podem ser ocultados por linguagem de prontidão:

- owners Architecture, Engineering, Security/Privacy, Quality/Evidence e Platform/DevOps ausentes;
- decisão de execução ausente;
- repositório não criado;
- ADRs não aceitos;
- controles não configurados;
- evidências não produzidas.

## 7. Marco

`M5.18 — Capture Context W0-01 Execution Charter Defined`.

## 8. Próxima decisão permitida

Atribuição nominal dos owners e autorização limitada da execução do W0-01. Qualquer outra expansão exige ciclo próprio.
