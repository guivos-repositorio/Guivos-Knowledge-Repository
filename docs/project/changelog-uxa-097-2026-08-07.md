---
id: GKR-CHANGELOG-UXA-097-001
title: Changelog UXA-097 — Compreensão Inicial → Tela Hoje
status: active
version: 0.1.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-07
depends_on:
  - UXA-097
  - GKR-STATE-001
related:
  - UXA-006
  - UXA-010
  - UXA-036
  - UXA-037
  - GKR-TRN-007
  - M7.84
normative: false
---

# Changelog UXA-097 — Compreensão Inicial → Tela Hoje

## 1. Escopo

A UXA-097 executa a prioridade de validação `V1`, fechando a continuidade entre a compreensão inicial revisável e a primeira Tela Hoje.

## 2. Alterações funcionais

- criado `uxa-097-first-today-after-initial-understanding-mobile.svg` como variante inicial de `PER-008`;
- reformulado `uxa-036-initial-understanding-decision-mobile.svg` para explicitar a rota `Usar nesta sessão e ir para Hoje sem personalização`;
- variante corrente de decisão de `PER-007` revalidada;
- primeira variante de `PER-008` validada;
- `GKR-TRN-007` promovida de `não examinada` para `integralmente validada`;
- Tela Hoje recorrente preservada sem alteração.

## 3. Contrato fechado

A primeira entrada em Hoje:

- não presume avanço humano ou mudança anterior;
- não exige personalização;
- utiliza somente base confirmada, autorizada e vigente;
- omite blocos pessoais quando personalização não estiver autorizada;
- respeita retirada, exclusão e estado canônico mais recente;
- não duplica efeitos em retorno, recarga ou repetição.

## 4. Cobertura proposta

- GKR-STATE: **2.23.0**;
- marco: **M7.84**;
- ROADMAP: **12.70.0**;
- SVGs: **109**;
- associações: **109**;
- perfis: **28**;
- validações vigentes: **99**;
- pendências: **10**, exclusivamente UXA-055;
- superfícies: **40**;
- transições: **37**.

## 5. Limites

A UXA-097 não fecha `TRN-001/003/004/005`, não valida UXA-055, não promove a Jornada da Pessoa, não inicia protótipo, teste com pessoas ou Engenharia de Produto.

A próxima prioridade registrada é `V2 — publicação → descoberta/mapa/lista/detalhe`. A UXA-098 não foi iniciada.