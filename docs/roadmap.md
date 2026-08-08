---
id: ROADMAP-12.73.0
title: Roadmap Arquitetural — Planos Fragmentados e Promovidos Canonicamente
status: active
version: 12.73.0
owner: Guivos
last_updated: 2026-08-07
supersedes_partial:
  - ROADMAP-12.72.0
related:
  - GKR-STATE-001
  - GPA-007
  - UXA-000
  - UXA-099
  - UXA-100
  - UXA-100-A1
  - UXA-100-A2
  - UXA-100-A3
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.87
---

# Roadmap Arquitetural — Planos Fragmentados e Promovidos Canonicamente

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual e só se torna vigente na `main` após integração governada.

## 2. Estado proposto

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | Planos fragmentados e promovidos canonicamente | UXA-100-A3; M7.87 |
| Registros granulares | **53 superfícies/estados/fronteiras e 54 transições** | UXA-100-A3 |
| Galeria visual | `active` 0.20.0; **118 SVGs** | UXA-100-A3 |
| matriz por SVG | **118 arquivos / 31 perfis**; `active` 0.16.0 | UXA-100-A3 |
| validações funcionais vigentes de SVG | **118** | UXA-100-A2/A3 |
| pendentes de validação específica | **0** | UXA-100-A2/A3 |
| Planos | **canonicamente registrados** | UXA-100-A3 |
| Jornadas principais | Pessoa, Coletivo e Organização em `draft` | Jornadas Integradas |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Sequência governada recente

```text
UXA-090 — cinco handoffs de solicitação validados
→ UXA-091 — PER-106 materializada
→ UXA-092 — PER-106 e TRN-108 validados
→ UXA-093 — PER-107 materializada
→ UXA-094 — PER-107 e TRN-110 validadas
→ UXA-095 — PER-108 materializada e TRN-111 parcial
→ UXA-096 — PER-107/PER-108 validadas e TRN-111 validada ponta a ponta
→ UXA-097 — primeira PER-008 materializada e validada; TRN-007 integral
→ UXA-098 — publicação, descoberta, Mapa, Lista e Detalhe validados
→ UXA-099 — dez estados residuais Opportunity Boost validados
→ UXA-100/A1 — Planos materializados nas três jornadas
→ UXA-100-A2 — 9/9 SVGs aprovados após seis reformas
→ UXA-100-A3 — fragmentação mínima e promoção canônica
```

Nenhuma etapa inicia automaticamente a seguinte.

## 4. Resultado da UXA-100-A3

| Dimensão | Resultado |
|---|---|
| SVGs de Planos examinados | **9** |
| SVGs promovidos | **9** |
| novas superfícies de Planos | **12** |
| nova fronteira | **BND-002** |
| novas transições | **17** |
| transições internas locais | **15** |
| handoffs Enterprise/Scale parciais | **2 — TRN-416/426** |
| SVGs totais | **118** |
| associações | **118** |
| perfis | **31** |
| validações vigentes | **118** |
| pendentes | **0** |
| superfícies/estados/fronteiras | **53** |
| transições | **54** |
| jornadas promovidas | 0 |
| Engenharia iniciada | não |

## 5. Contrato canônico de Planos

```text
*-301 Planos e comparação
├── upgrade → *-302 revisão → *-304 resultado/recuperação → *-301
├── downgrade/cancelamento → *-303 revisão de ciclo → *-304 → *-301
└── Enterprise/Scale → BND-002
```

- comparação incremental permanece em `*-301`;
- processamento financeiro permanece transitório;
- sucesso e falha pertencem a `*-304` com consequências distintas;
- Enterprise/Scale não recebem checkout fictício;
- assinatura não compra relevância, confiança, impacto, legitimidade ou evolução.

## 6. Fronteiras preservadas

- `TRN-205`: efeito externo posterior continua parcial;
- `TRN-304`, `TRN-305` e `TRN-306`: integrações patrocinadas continuam parciais;
- `TRN-416`/`426`: processo comercial após `BND-002` continua parcial;
- gateway, cobrança real, proration, grace period e regras fiscais finais permanecem fora do escopo;
- nenhuma implementação é criada pela promoção documental.

## 7. Trilha governada de Coletivos preservada

```text
COL-002
→ TRN-112
→ COL-003
↔ TRN-105/106/107/109
→ TRN-108
→ PER-106
→ TRN-110
→ PER-107
→ TRN-111
→ PER-108
```

As oito transições indicadas permanecem integralmente validadas.

## 8. Fila global

```text
V1 — compreensão inicial → Tela Hoje — ENCERRADA pela UXA-097
→ V2 — publicação → descoberta/mapa/lista/detalhe — ENCERRADA pela UXA-098
→ V3 — dez estados residuais UXA-055 — ENCERRADA pela UXA-099
→ Planos — identidade/promoção canônica — ENCERRADA pela UXA-100-A3
→ V4 — efeito externo de oportunidades — prioridade global preservada
→ V5 — erros, retornos e interrupções
```

A execução autorizada de Planos não cancelou nem executou V4/V5.

## 9. Dívidas preservadas

- estados P0B adicionais de Meus Coletivos, Central e Início do Participante;
- áreas P1 de comunicação especializada;
- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` parciais;
- `TRN-205`, `TRN-304`, `TRN-305` e `TRN-306` parciais;
- cobrança real e gateway de Planos;
- processo Enterprise/Scale após `BND-002`;
- entradas contextuais de Planos a partir de superfícies ainda não registradas;
- operação interna restante do Coletivo;
- relação Organização–Coletivo ainda não materializada.

## 10. Limites

A UXA-100-A3 não valida preço em mercado, não cria checkout/gateway/cobrança, não define política fiscal ou pró-rata, não implementa entitlement, não materializa processo comercial pós-`BND-002`, não promove jornadas e não inicia protótipo, teste com pessoas ou Engenharia de Produto.

## 11. Próxima iniciativa possível

A identidade canônica de Planos está encerrada. A próxima iniciativa só poderá começar mediante decisão humana separada; **UXA-101 não foi iniciada**. A fila global ainda registra V4 como prioridade pendente.