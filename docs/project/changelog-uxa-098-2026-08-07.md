---
id: GKR-CHANGELOG-UXA-098-001
title: Changelog — UXA-098 — Publicação → Descoberta, Mapa, Lista e Detalhe
status: active
version: 0.1.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-07
depends_on:
  - UXA-098
related:
  - GKR-STATE-001
  - ROADMAP-12.71.0
  - M7.85
normative: false
---

# Changelog — UXA-098

## Estado proposto

- GKR-STATE: **2.24.0**;
- marco: **M7.85**;
- ROADMAP: **12.71.0**;
- UXA-000: **0.91.0**;
- Jornadas Integradas: **0.26.0**;
- Jornada da Pessoa: **draft 0.11.0**;
- Jornada da Organização: **draft 0.4.0**;
- Transition Registry: **0.15.0**;
- Lacunas: **0.23.0**.

## Mudança principal

A UXA-098 valida como conjunto a continuidade de oportunidade entre cadastro/ativação institucional e descoberta pela Pessoa:

- `TRN-203`: não examinada → **integralmente validada**;
- `TRN-204`: parcial → **integralmente validada**;
- `TRN-210`: parcial → **integralmente validada**;
- `TRN-211`: parcial → **integralmente validada**.

## Contratos consolidados

- ativação cria elegibilidade à descoberta, não exposição garantida;
- Mapa e Lista são representações da mesma consulta;
- Mapa e Lista conduzem ao mesmo Detalhe canônico;
- estado vigente prevalece sobre cartão ou detalhe obsoleto;
- abertura do Detalhe não cria interesse, inscrição ou evolução;
- repetição/sincronização é idempotente;
- patrocínio não altera relevância funcional;
- efeito externo posterior permanece em `TRN-205`.

## Cobertura preservada

- 109 SVGs;
- 109 associações;
- 28 perfis;
- 99 validações funcionais vigentes;
- 10 pendências, exclusivamente UXA-055;
- 30/40 IDs com referência visual;
- 9 responsabilidades sem SVG dedicado;
- 40 superfícies;
- 37 transições.

Nenhum SVG foi criado ou alterado.

## Limites

A UXA-098 não valida `TRN-205`, `TRN-304`, `TRN-306`, os dez estados residuais UXA-055, não promove jornadas e não inicia protótipo, teste, W0-01 ou Engenharia de Produto.

A próxima prioridade registrada após eventual integração é `V3 — dez estados residuais UXA-055`. A UXA-099 não foi iniciada.