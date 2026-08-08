---
id: GKR-CHANGELOG-UXA-101-001
title: Changelog — UXA-101 Saída Consciente para Fronteira Externa
status: active
version: 0.1.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-07
depends_on:
  - UXA-101
related:
  - GKR-STATE-001
  - ROADMAP-12.74.0
  - M7.88
normative: false
---

# Changelog — UXA-101 Saída Consciente para Fronteira Externa

## 1. Escopo

Registra o fechamento documental de V4 no lado controlado pela Guivos, entre `PER-203` e `BND-001`.

## 2. Alterações

- criado o contrato UXA-101;
- reformulado `uxa-007-opportunity-detail-mobile.svg` sem criar novo SVG;
- materializado no próprio `PER-203` o estado de revisão antes da saída;
- explicitados destino externo, responsável, dados/contexto e limites de autoridade;
- adicionados caminhos conscientes de continuar ou voltar;
- redirecionamento silencioso é bloqueado quando o destino não pode ser confirmado;
- `TRN-205` promovida de parcial para **integralmente validada até a fronteira de autoridade Guivos**;
- `BND-001` passa a examinado e permanece sem tela Guivos;
- Jornada da Pessoa, galerias, catálogo, matriz, superfícies, transições e lacunas foram sincronizados;
- nenhuma inscrição, reserva, compra, contratação ou resultado externo é presumido.

## 3. Estado proposto

| Indicador | Resultado |
|---|---:|
| GKR-STATE | **2.27.0** |
| Marco | **M7.88** |
| Roadmap | **12.74.0** |
| UXA-000 | **0.94.0** |
| Jornadas Integradas | **0.31.0** |
| Jornada da Pessoa | `draft` **0.15.0** |
| SVGs canônicos | **118** |
| associações | **118** |
| perfis | **31** |
| validações funcionais | **118** |
| pendências específicas | **0** |
| superfícies/estados/fronteiras | **53** |
| transições | **54** |
| registro de superfícies | **0.17.0** |
| registro de transições | **0.18.0** |

## 4. Limites

- V4 encerra somente o handoff controlável pela Guivos;
- `BND-001` não incorpora o site/app de terceiro ao ecossistema de telas Guivos;
- processo externo posterior não foi validado;
- `TRN-304`, `TRN-305`, `TRN-306`, `TRN-416` e `TRN-426` permanecem parciais;
- V5 não foi iniciada;
- UXA-102 não foi iniciada;
- Engenharia de Produto permanece pausada antes de W0-01;
- merge da PR da UXA-101 exige decisão humana separada.