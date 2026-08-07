---
id: GKR-CHANGELOG-UXA-092-001
title: Changelog — UXA-092
status: active
version: 0.1.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-07
depends_on:
  - UXA-092
  - GKR-STATE-001
related:
  - UXA-091
  - UXA-090
  - GKR-SURF-PER-105
  - GKR-SURF-PER-106
  - GKR-TRN-108
  - GKR-TRN-110
  - M7.79
normative: false
---

# Changelog — UXA-092

## Resumo

A UXA-092 valida funcionalmente `GKR-SURF-PER-106 — Meus Coletivos`, revalida o estado aprovado corrente de `GKR-SURF-PER-105` e valida integralmente `GKR-TRN-108` após reformulação controlada de dois SVGs existentes.

## Diagnóstico

A materialização UXA-091 exigia ajuste porque:

- solicitações e convites apareciam sob linguagem que os tratava como vínculos;
- referências a não lidos/comunicados antecipavam responsabilidade de `PER-107`;
- `Salvar decisão` no resultado aprovado podia sugerir que a Pessoa precisava confirmar uma aprovação já registrada.

## Reformulação

- `uxa-066-collective-pending-request-approved-mobile.svg`: aprovação explicitamente registrada antes da navegação; `Salvar decisão` substituído por `Agora não`;
- `uxa-091-my-collectives-mobile.svg`: separação entre participações e estados relacionados; remoção de semântica própria de Central de Atualizações.

Nenhum SVG, ID, superfície ou transição novo foi criado.

## Resultado

- `PER-105` aprovado: validado na versão corrente;
- `PER-106`: validado;
- `TRN-108`: `integralmente validada`;
- `TRN-110`: permanece `parcial` por `PER-107` ausente;
- Jornadas da Pessoa e do Coletivo: permanecem `draft`.

## Cobertura proposta

- GKR-STATE 2.18.0;
- M7.79;
- ROADMAP 12.65.0;
- UXA-000 0.85.0;
- 106 SVGs;
- 106 associações;
- 26 perfis;
- 96 validações funcionais vigentes;
- 10 pendências, exclusivamente UXA-055;
- 28/40 IDs com referência visual;
- 11 responsabilidades sem SVG dedicado;
- 40 superfícies;
- 37 transições;
- 6 handoffs integralmente validados no fluxo de solicitação.

## Limites

A UXA-092 não materializa `PER-107`, `PER-108` ou estados P0B adicionais de `PER-106`, não valida `TRN-110`, não promove jornadas e não inicia protótipo, teste, Engenharia de Produto ou UXA-093.
