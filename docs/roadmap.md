---
id: ROADMAP-12.74.1
title: Roadmap Arquitetural — Patch de Taxonomia Global de Planos
status: active
version: 12.74.1
owner: Guivos
last_updated: 2026-08-08
supersedes_partial:
  - ROADMAP-12.74.0
related:
  - GKR-STATE-001
  - GPA-004
  - GPA-007
  - GEM-004-A1
  - UXA-000
  - UXA-099
  - UXA-100
  - UXA-101
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.88
---

# Roadmap Arquitetural — Patch de Taxonomia Global de Planos

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual e só se torna vigente na `main` após integração governada.

A versão 12.74.1 é **patch documental** sobre o estado pós-UXA-101. Ela não cria UXA, não cria marco, não inicia V5 e não inicia Engenharia de Produto.

## 2. Estado proposto

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | saída consciente para fronteira externa validada | UXA-101; **M7.88** |
| Patch | taxonomia global de planos e separação Organização/Business | GEM-004-A1; GPA-004; UXA-100 |
| Registros granulares | **53 superfícies/estados/fronteiras e 54 transições** | UXA-100/101 |
| Galeria visual | `active` 0.21.0; **118 SVGs** | UXA-101 |
| matriz por SVG | **118 arquivos / 31 perfis**; `active` 0.17.0 | UXA-101 |
| validações funcionais vigentes de SVG | **118** | UXA-100-A2/101 |
| pendentes de validação específica | **0** | UXA-100-A2/101 |
| V4 | **encerrada até BND-001** | UXA-101 |
| Jornadas principais | Pessoa, Coletivo e Organização em `draft` | Jornadas Integradas |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Taxonomia global governada

| Contexto | Planos |
|---|---|
| Pessoa | **Free · Plus · Pro** |
| Coletivo | **Livre · Mobiliza · Impacta · Rede** |
| Organização | **Conecta · Eleva · Transforma** |
| Guivos Business | **Start · Growth · Scale · Enterprise** |

Plano representa profundidade de serviço, capacidade ou complexidade atendida; não representa valor, mérito, prestígio ou nível de evolução.

**Organização Transforma ≠ Guivos Business Enterprise.** Organização é participante institucional; Guivos Business é produto especializado. Não há correspondência automática 1:1.

Preços/capacidades de participantes permanecem preservados conforme GEM-004-A1. Preços, entitlements e packaging próprios do Guivos Business permanecem indefinidos.

## 4. Sequência governada recente

```text
UXA-097 — compreensão inicial → primeira Hoje
→ UXA-098 — publicação → descoberta → Mapa/Lista → Detalhe
→ UXA-099 — dez estados residuais Opportunity Boost
→ UXA-100/A1/A2/A3 — Planos materializados, validados e promovidos
→ UXA-101 — Detalhe → revisão consciente → BND-001
→ patch 2.27.1 / roadmap 12.74.1 — taxonomia de Planos sincronizada
```

O patch não se torna `UXA-102` e não altera a fila de validação.

## 5. Efeito do patch taxonômico

| Dimensão | Resultado |
|---|---|
| novos SVGs | **0** |
| SVGs sincronizados | **6 dos 9 ativos UXA-100** |
| SVGs de Pessoa alterados | **0** |
| novas superfícies | **0** |
| novas fronteiras | **0** |
| novas transições | **0** |
| `TRN-416` | **permanece parcial** |
| `TRN-426` | **permanece parcial** |
| `BND-002` | mesma identidade; semântica genérica de contratação/dimensionamento assistido |
| SVGs totais | **118** |
| associações | **118** |
| perfis | **31** |
| superfícies/estados/fronteiras | **53** |
| transições | **54** |
| jornadas promovidas | 0 |
| Engenharia iniciada | não |

## 6. Resultado da UXA-101 preservado

```text
PER-203 — Detalhe
→ revisão de saída na própria PER-203
→ confirmação afirmativa
→ TRN-205
→ BND-001
→ autoridade externa
```

`TRN-205` permanece validada até `BND-001`; o processo posterior continua sob autoridade externa.

## 7. BND-002 corrigido

`BND-002` é a **fronteira de contratação/dimensionamento assistido** quando uma configuração deixa de ser autonomamente contratável e exige proposta, dimensionamento, contrato, configuração ou análise específica.

Não significa Enterprise, Scale, Rede ou Transforma e não é checkout.

`TRN-416/426` continuam parciais porque o processo posterior à fronteira não foi materializado/validado como conjunto.

## 8. Fila global preservada

```text
V1 — compreensão inicial → Tela Hoje — ENCERRADA pela UXA-097
→ V2 — publicação → descoberta/mapa/lista/detalhe — ENCERRADA pela UXA-098
→ V3 — dez estados residuais UXA-055 — ENCERRADA pela UXA-099
→ Planos — identidade/promoção canônica — ENCERRADA pela UXA-100-A3
→ V4 — efeito externo de oportunidades — ENCERRADA pela UXA-101 até BND-001
→ V5 — erros, retornos e interrupções — PENDENTE / NÃO INICIADA
```

## 9. Dívidas preservadas

- estados P0B adicionais de Meus Coletivos, Central e Início do Participante;
- áreas P1 de comunicação especializada;
- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` parciais;
- `TRN-304`, `TRN-305` e `TRN-306` parciais;
- cobrança real e gateway de Planos;
- processo assistido posterior a `BND-002`;
- entradas contextuais de Planos sem origem canônica adequada;
- operação interna restante do Coletivo;
- relação Organização–Coletivo ainda não materializada;
- processo/resultados externos posteriores a `BND-001`;
- definição comercial própria de Guivos Business: preços, entitlements, packaging, limites e unit economics.

## 10. Próxima iniciativa possível

**UXA-102/V5 permanece não iniciada** e dependente de autorização humana separada. A definição comercial de Guivos Business, o realinhamento posterior da PR #203 e qualquer Engenharia de Produto continuam frentes independentes.
