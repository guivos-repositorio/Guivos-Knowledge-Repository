---
id: ROADMAP-12.71.0
title: Roadmap Arquitetural — Publicação → Descoberta, Mapa, Lista e Detalhe Validados
status: active
version: 12.71.0
owner: Guivos
last_updated: 2026-08-07
supersedes_partial:
  - ROADMAP-12.70.0
related:
  - GKR-STATE-001
  - GPA-007
  - UXA-000
  - UXA-055
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
  - UXA-094
  - UXA-095
  - UXA-096
  - UXA-097
  - UXA-098
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.85
---

# Roadmap Arquitetural — Publicação → Descoberta, Mapa, Lista e Detalhe Validados

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado proposto

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | publicação, descoberta e Mapa/Lista/Detalhe validados | UXA-098; M7.85 |
| Registros granulares | 40 superfícies e 37 transições | UXA-098 |
| Galeria visual | `active` 0.16.0; 109 SVGs | sem alteração na UXA-098 |
| matriz por SVG | 109 arquivos / 28 perfis; `active` 0.14.0 | sem alteração na UXA-098 |
| validações funcionais vigentes de SVG | **99** | pacotes anteriores preservados |
| pendentes de validação específica | **10, exclusivamente UXA-055** | UXA-055 |
| V2 | **TRN-203/204/210/211 integralmente validadas** | UXA-098 |
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
→ UXA-098 — publicação, descoberta, Mapa, Lista e Detalhe validados como continuidade integrada
```

Nenhuma etapa inicia automaticamente a seguinte.

## 4. Resultado da UXA-098

| Dimensão | Resultado |
|---|---|
| ORG-003 | permanece validado; sem alteração visual |
| PER-201 / PER-202 / PER-203 | permanecem validados; sem alteração visual |
| SVGs novos | **0** |
| SVGs reformulados | **0** |
| GKR-TRN-203 | não examinada → **integralmente validada** |
| GKR-TRN-204 | parcial → **integralmente validada** |
| GKR-TRN-210 | parcial → **integralmente validada** |
| GKR-TRN-211 | parcial → **integralmente validada** |
| SVGs totais | **109** |
| associações | **109** |
| perfis | **28** |
| validações vigentes | **99** |
| pendentes | **10, exclusivamente UXA-055** |
| jornadas promovidas | 0 |
| Engenharia iniciada | não |

## 5. Contrato V2 validado

```text
ORG-003 — oportunidade aprovada e ativa
→ TRN-203 — candidata à descoberta, sem exposição garantida
→ PER-201 — Mapa
↔ TRN-210 — mesma consulta territorial
→ PER-202 — Lista

PER-201 → TRN-204 → PER-203
PER-202 → TRN-211 → PER-203
```

A identidade lógica e o estado canônico permanecem únicos. Pausa, expiração, indisponibilidade ou mudança material prevalecem sobre tela obsoleta. Mapa e Lista não criam autorização nova. Abrir o Detalhe não equivale a interesse ou evolução.

## 6. Fronteiras preservadas

- `TRN-205`: efeito externo posterior continua parcial;
- `TRN-304` e `TRN-306`: integração patrocinada com Mapa/Lista continua parcial;
- pagamento amplia distribuição publicitária identificada, não relevância funcional;
- publicação não garante impressão, posição, recomendação ou alcance.

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

## 8. Fila de validação

```text
V1 — compreensão inicial → Tela Hoje — ENCERRADA pela UXA-097
→ V2 — publicação → descoberta/mapa/lista/detalhe — ENCERRADA pela UXA-098
→ V3 — dez estados residuais UXA-055 — próxima prioridade
→ V4 — efeito externo de oportunidades
→ V5 — erros, retornos e interrupções
```

## 9. Dívidas preservadas

- estados P0B de Meus Coletivos, Central e Início do Participante;
- áreas P1 de comunicação especializada;
- dez estados residuais da UXA-055;
- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` ainda parciais;
- `TRN-205` efeito externo de oportunidades;
- `TRN-304` e `TRN-306` integração patrocinada;
- erros, retornos e interrupções em outras jornadas;
- operação interna restante do Coletivo;
- relação Organização–Coletivo ainda não materializada como conjunto.

## 10. Limites

A UXA-098 não altera SVGs, não cria IDs, não define algoritmo, não garante distribuição, não valida UXA-055 residual, não executa efeito externo, não promove jornadas e não inicia protótipo, teste com pessoas ou Engenharia de Produto.

## 11. Próxima iniciativa possível

A próxima prioridade registrada é **V3 — dez estados residuais UXA-055**. Uma eventual UXA-099 dependerá de autorização separada e **não foi iniciada**.