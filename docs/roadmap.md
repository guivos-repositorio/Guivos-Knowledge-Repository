---
id: ROADMAP-12.70.0
title: Roadmap Arquitetural — Compreensão Inicial → Tela Hoje Validada
status: active
version: 12.70.0
owner: Guivos
last_updated: 2026-08-07
supersedes_partial:
  - ROADMAP-12.69.0
related:
  - GKR-STATE-001
  - GPA-007
  - UXA-000
  - UXA-055
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
  - UXA-094
  - UXA-095
  - UXA-096
  - UXA-097
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.84
---

# Roadmap Arquitetural — Compreensão Inicial → Tela Hoje Validada

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado proposto

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | primeira Tela Hoje e TRN-007 validadas | UXA-097; M7.84 |
| Registros granulares | 40 superfícies e 37 transições | UXA-097 |
| Galeria visual | `active` 0.16.0; 109 SVGs | UXA-097 |
| página da Pessoa | `active` 0.4.0; 20 SVGs | UXA-097 |
| página de Coletivos | `active` 0.13.0 | UXA-096 |
| matriz por SVG | 109 arquivos / 28 perfis; `active` 0.14.0 | UXA-097 |
| validações funcionais vigentes de SVG | **99** | UXA-097 e pacotes anteriores |
| pendentes de validação específica | **10, exclusivamente UXA-055** | UXA-055 |
| handoffs integralmente validados em Coletivos | **8** | UXA-090; UXA-092; UXA-094; UXA-096 |
| TRN-007 pessoal | **integralmente validada** | UXA-097 |
| Jornadas principais | Pessoa, Coletivo e Organização em `draft` | Jornadas Integradas |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Sequência governada recente

```text
UXA-090 — cinco handoffs de solicitação validados
→ UXA-091 — PER-106 materializada
→ UXA-092 — PER-106 e TRN-108 validadas
→ UXA-093 — PER-107 materializada
→ UXA-094 — PER-107 e TRN-110 validadas
→ UXA-095 — PER-108 materializada e TRN-111 parcial
→ UXA-096 — PER-107/PER-108 validadas e TRN-111 validada ponta a ponta
→ UXA-097 — primeira PER-008 materializada e validada; PER-007 revalidada; TRN-007 validada ponta a ponta
```

Nenhuma etapa inicia automaticamente a seguinte.

## 4. Resultado da UXA-097

| Dimensão | Resultado |
|---|---|
| GKR-SURF-PER-007 | permanece **validado**; decisão corrente revalidada |
| GKR-SURF-PER-008 | primeira variante **validada**; recorrente preservada |
| SVGs novos | **1** |
| SVGs reformulados | **1 existente** |
| GKR-TRN-007 | não examinada → **integralmente validada** |
| SVGs totais | **109** |
| associações | **109** |
| perfis | **28** |
| validações vigentes | **99** |
| pendentes | **10, exclusivamente UXA-055** |
| jornadas promovidas | 0 |
| Engenharia iniciada | não |

## 5. Contrato validado de PER-007 → PER-008

```text
PER-007 — compreensão inicial revisável
→ escolhas compatíveis confirmadas explicitamente
→ condição escolhida torna-se efetiva sem ampliação implícita
→ TRN-007
→ primeira PER-008 consulta o estado canônico vigente
→ nenhuma mudança ou avanço anterior é presumido
```

Sem personalização, Hoje continua acessível sem indicações pessoais. Retirada, exclusão ou alteração posterior prevalecem sobre estado visual obsoleto. Repetição não duplica efeito lógico.

## 6. Trilha governada de Coletivos preservada

```text
COL-002 — validada
→ TRN-112 — integralmente validada
→ COL-003 — validada
↔ TRN-105/106/107/109 — integralmente validadas
→ TRN-108 — integralmente validada
→ PER-106 — validado
→ TRN-110 — integralmente validada
→ PER-107 — validado
→ TRN-111 — integralmente validada
→ PER-108 — validado
```

## 7. Fila de validação

```text
V1 — compreensão inicial → Tela Hoje — ENCERRADA pela UXA-097
→ V2 — publicação → descoberta/mapa/lista/detalhe — próxima prioridade
→ V3 — dez estados residuais UXA-055
→ V4 — efeito externo de oportunidades
→ V5 — erros, retornos e interrupções
```

## 8. Dívidas preservadas

- estados P0B de Meus Coletivos, Central e Início do Participante;
- áreas P1 de comunicação especializada;
- dez estados residuais da UXA-055;
- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` ainda parciais;
- publicação → descoberta/mapa/lista/detalhe;
- efeito externo de oportunidades;
- erros, retornos e interrupções em outras jornadas;
- estados alternativos adicionais da Tela Hoje;
- operação interna restante do Coletivo;
- relação Organização–Coletivo ainda não materializada como conjunto.

## 9. Limites

A UXA-097 não cria novos IDs, não altera a Tela Hoje recorrente, não fecha handoffs pessoais anteriores, não valida UXA-055, não promove jornadas e não inicia protótipo, teste com pessoas ou Engenharia de Produto.

## 10. Próxima iniciativa possível

A próxima prioridade registrada é **V2 — publicação → descoberta/mapa/lista/detalhe**. Uma eventual UXA-098 dependerá de autorização separada e **não foi iniciada**.