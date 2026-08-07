---
id: GKR-UXA-095-PR-CHECKPOINT-001
title: Checkpoint Pré-PR — UXA-095
status: active
version: 0.1.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-07
related:
  - UXA-095
  - GKR-STATE-001
  - M7.82
normative: false
---

# Checkpoint Pré-PR — UXA-095

## 1. Baseline e branch

- repositório: `guivos-repositorio/Guivos-Knowledge-Repository`;
- base autorizada: `main` em `a85c96ac7efc39705ab9220f2a431eefb6c08b1a`;
- branch: `agent/uxa-095-participant-home-materialization-trn111-refinement`;
- iniciativa: UXA-095 — Materialização Controlada do Início do Participante e Refinamento de TRN-111.

## 2. Escopo visual

- 1 SVG novo: `uxa-095-collective-participant-home-mobile.svg`;
- 1 SVG existente reformulado: `uxa-093-collective-updates-center-mobile.svg`;
- 0 IDs de superfície novos;
- 0 IDs de transição novos;
- nenhuma remoção de SVG existente.

## 3. Efeito de maturidade proposto

- `PER-107`: contrato previamente validado; SVG corrente reformulado e pendente de revalidação;
- `PER-108`: `materializado`, validação funcional pendente;
- `TRN-110`: permanece `integralmente validada`;
- `TRN-111`: `ausente` → `parcial`;
- sete handoffs integralmente validados no trecho anterior permanecem preservados;
- Jornadas da Pessoa e do Coletivo permanecem `draft`;
- Engenharia de Produto permanece pausada antes de W0-01.

## 4. Baseline proposta após eventual integração

- GKR-STATE: 2.21.0;
- marco: M7.82;
- ROADMAP: 12.68.0;
- UXA-000: 0.88.0;
- Jornadas Integradas: 0.23.0;
- Jornada da Pessoa: draft 0.8.0;
- Jornada do Coletivo: draft 0.11.0;
- Galeria: 0.14.0;
- página Coletivos: 0.12.0;
- Matriz: 0.12.0;
- Catálogo: 0.19.0;
- Lacunas: 0.20.0;
- Surface Registry: 0.12.0;
- Transition Registry: 0.12.0;
- detalhamento da Pessoa: 0.7.0.

## 5. Cobertura proposta

- SVGs: 108;
- associações individuais: 108;
- perfis documentais: 28;
- validações funcionais vigentes: 96;
- pendentes: 12 = 10 UXA-055 + PER-107 corrente + PER-108;
- IDs com referência visual: 30/40;
- responsabilidades sem SVG dedicado: 9;
- superfícies: 40;
- transições: 37;
- fronteira sem tela: 1.

## 6. Gates obrigatórios

Antes de qualquer decisão de integração, o PR deverá permanecer em rascunho e obter:

1. GKR Semantic State Validation em `SUCCESS` no head exato;
2. GKR Mechanical Validation em `SUCCESS` no mesmo head;
3. zero threads de revisão pendentes;
4. confirmação de que `main` não se moveu da baseline esperada;
5. confirmação de que o head do PR não mudou durante a decisão.

## 7. Limite de autorização

Este checkpoint não autoriza retirar o PR do modo rascunho nem realizar merge. A integração exige autorização separada do usuário.

A UXA-096 não foi iniciada.
