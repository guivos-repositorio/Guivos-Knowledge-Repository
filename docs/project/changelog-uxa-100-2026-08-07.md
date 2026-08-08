---
id: GKR-CHANGELOG-UXA-100-001
title: Changelog — UXA-100 Planos, Cobrança e Pagamentos
status: active
version: 0.1.1
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-07
depends_on:
  - UXA-100
  - UXA-100-A1
  - UXA-100-A2
  - UXA-100-A3
related:
  - GKR-STATE-001
  - ROADMAP-12.73.0
  - M7.87
normative: false
---

# Changelog — UXA-100 Planos, Cobrança e Pagamentos

## 1. Escopo

Registra a frente transversal de Planos para Pessoa, Coletivo e Organização no branch da PR #200.

## 2. Evolução governada

### UXA-100 / A1

- programa funcional criado;
- três telas dedicadas de Planos;
- três boards de fluxo;
- três comparações incrementais;
- Planos inserido nas três jornadas `draft`;
- comparação geral, incremental e delta direto atual → alvo documentados.

### UXA-100-A2

- 9/9 SVGs auditados funcionalmente;
- 6 reformulados controladamente;
- 3 comparações incrementais aprovadas sem reforma;
- Free preserva catálogo público;
- revisão de contratação, falha, downgrade e cancelamento alinhados ao GEM-004.

### UXA-100-A3

- 9 SVGs promovidos ao conjunto canônico;
- 4 superfícies por participante promovidas;
- `BND-002` criado como fronteira Enterprise/Scale;
- 17 transições registradas;
- 15 transições internas classificadas como localmente validadas;
- `TRN-416` e `TRN-426` permanecem parciais;
- comparação incremental permanece estado de `*-301`;
- processamento financeiro permanece transitório;
- sucesso e falha pertencem a `*-304` como estados de resultado/recuperação.

### Realinhamento após integração da UXA-099

- PR #199 integrada à `main` no commit `87bd767eeabcab81ad7b67e24b7f46a01fd52a39`;
- a árvore do merge da UXA-099 é idêntica à árvore do antigo head da UXA-099, permitindo alinhamento sem alteração temática da UXA-100;
- branch da UXA-100 alinhada à nova `main` pelo commit `843fb54684730d79dc370834640b1e7bc111ce8d`;
- PR #200 retargetada para `main`;
- o diff após o realinhamento permanece restrito ao escopo da UXA-100;
- nenhum merge da PR #200 foi realizado.

## 3. Estado proposto

| Indicador | Resultado |
|---|---:|
| GKR-STATE | **2.26.0** |
| Marco | **M7.87** |
| Roadmap | **12.73.0** |
| UXA-000 | **0.93.0** |
| SVGs canônicos | **118** |
| associações | **118** |
| perfis | **31** |
| validações funcionais | **118** |
| pendências específicas | **0** |
| superfícies/estados/fronteiras | **53** |
| transições | **54** |
| IDs com referência visual | **42** |
| responsabilidades sem SVG dedicado | **9** |
| fronteiras sem tela | **2** |

## 4. Limites

- preços continuam candidatos;
- não há oferta pública;
- não há gateway, cobrança real ou entitlement implementado;
- não há pró-rata, grace period ou política fiscal final;
- processo posterior a `BND-002` não está materializado;
- Pessoa, Coletivo e Organização permanecem `draft`;
- Engenharia de Produto permanece pausada antes de W0-01;
- PR #199 já está integrada e compõe a baseline vigente da `main`;
- PR #200 está alinhada e retargetada para `main`, mas continua fora da `main` e seu merge exige decisão humana separada;
- **UXA-101 não foi iniciada**.
