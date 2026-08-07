---
id: GKR-UXA-093-PR-CHECKPOINT-001
title: Checkpoint Governado do PR — UXA-093
status: active
version: 0.1.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-07
depends_on:
  - GKR-STATE-001
  - UXA-093
related:
  - ROADMAP-12.66.0
  - M7.80
normative: false
---

# Checkpoint Governado — UXA-093

## 1. Baseline

- repositório: `guivos-repositorio/Guivos-Knowledge-Repository`;
- `main` utilizada como baseline: `0ef8fabaae3c63eec90beae0a512421652414d8e`;
- branch: `agent/uxa-093-collective-updates-center-materialization`;
- iniciativa: `UXA-093 — Materialização Controlada da Central de Atualizações`.

## 2. Escopo autorizado

- materializar exclusivamente `GKR-SURF-PER-107 — Central de Atualizações`;
- criar uma referência móvel P0A;
- atualizar a evidência de `GKR-TRN-110` sem promovê-la por inferência;
- manter `GKR-TRN-111` ausente enquanto `PER-108` não existir na forma vigente;
- sincronizar registros, galeria, matriz, catálogo, jornadas, baseline, roadmap, índice e changelog.

## 3. Limites

Este pacote não autoriza:

- validação funcional de `PER-107`;
- validação integral de `TRN-110`;
- materialização de `PER-108`;
- estados P0B da Central;
- áreas P1 de comunicação;
- novos IDs de superfície ou transição;
- promoção das Jornadas da Pessoa ou do Coletivo;
- protótipo, teste com pessoas ou Engenharia de Produto;
- início da UXA-094.

## 4. Estado proposto após eventual integração

- GKR-STATE 2.19.0;
- M7.80;
- ROADMAP 12.66.0;
- UXA-000 0.86.0;
- 107 SVGs;
- 107 associações;
- 27 perfis;
- 96 validações funcionais vigentes;
- 11 pendências específicas;
- 29 de 40 IDs com referência visual;
- 10 responsabilidades sem SVG dedicado;
- 40 superfícies;
- 37 transições;
- seis handoffs integralmente validados preservados.

## 5. Regra de integração

O PR deve permanecer em `DRAFT` após os gates Semantic e Mechanical. Retirar o rascunho e fazer merge requer autorização separada do usuário após apresentação dos resultados.

A UXA-094 não é iniciada por este checkpoint.
