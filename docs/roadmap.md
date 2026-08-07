---
id: ROADMAP-12.68.0
title: Roadmap Arquitetural — Início do Participante Materializado
status: active
version: 12.68.0
owner: Guivos
last_updated: 2026-08-07
supersedes_partial:
  - ROADMAP-12.67.0
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
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.82
---

# Roadmap Arquitetural — Início do Participante Materializado

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado proposto

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | Início do Participante materializado; TRN-111 parcial | UXA-095; M7.82 |
| Registros granulares | 40 superfícies e 37 transições | UXA-095 |
| Galeria visual | `active` 0.14.0; 108 SVGs | UXA-095 |
| página de Coletivos | `active` 0.12.0 | UXA-095 |
| matriz por SVG | 108 arquivos / 28 perfis; `active` 0.12.0 | UXA-095 |
| validações funcionais vigentes de SVG | **96** | UXA-095 e pacotes anteriores |
| pendentes de validação específica | **12** | UXA-055; UXA-095 |
| handoffs integralmente validados em Coletivos | **7** | UXA-090; UXA-092; UXA-094 |
| Jornadas principais | Pessoa, Coletivo e Organização em `draft` | Jornadas Integradas |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Sequência governada

```text
UXA-086 — COL-002 materializada
→ UXA-087 — COL-002 validada
→ UXA-088 — COL-003 materializada
→ UXA-089 — COL-003 validada
→ UXA-090 — cinco handoffs validados
→ UXA-091 — PER-106 materializada
→ UXA-092 — PER-106 e TRN-108 validadas
→ UXA-093 — PER-107 materializada
→ UXA-094 — PER-107 e TRN-110 validadas
→ UXA-095 — PER-108 materializada e TRN-111 tornada parcial
```

Nenhuma etapa inicia automaticamente a seguinte.

## 4. Resultado da UXA-095

| Dimensão | Resultado |
|---|---|
| GKR-SURF-PER-107 | contrato previamente validado; SVG corrente reformulado e pendente de revalidação |
| GKR-SURF-PER-108 | `materializado` por novo SVG móvel |
| SVGs novos | 1 |
| SVGs reformulados | 1 existente |
| GKR-TRN-110 | permanece `integralmente validada` |
| GKR-TRN-111 | `ausente` → `parcial` |
| SVGs totais | 108 |
| perfis | 28 |
| validações vigentes | 96 |
| pendentes | 12 = 10 UXA-055 + PER-107 corrente + PER-108 |
| jornadas promovidas | 0 |
| Engenharia iniciada | não |

## 5. Contrato de materialização de PER-108

O Início do Participante sintetiza propósito, vínculo, momento coletivo, ação compartilhada, consulta e autonomia. Ele preserva áreas próprias para comunicação, atividades, pessoas/papéis, decisões, recursos e proteção.

Pertencimento não implica disponibilidade; disponibilidade não implica função; função não implica autoridade; vínculo não confirma presença em atividade.

## 6. Continuidade representada

```text
PER-107 — Central de Atualizações
→ “Abrir início do Coletivo”
→ entrada neutra, sem alterar vínculo ou leitura
→ PER-108 — Início do Participante
```

A continuidade permanece parcial até validação integrada da origem reformulada, do destino novo e das regras de retorno/concorrência.

## 7. Trilha governada de Coletivos

```text
COL-002 — validada
→ TRN-112 — integralmente validada
→ COL-003 — validada
↔ TRN-105/106/107/109 — integralmente validadas
→ TRN-108 — integralmente validada
→ PER-106 — validado
→ TRN-110 — integralmente validada
→ PER-107 — contrato validado; SVG corrente pendente
→ TRN-111 — parcial
→ PER-108 — materializado; validação pendente
```

## 8. Dívidas preservadas

- validação funcional de PER-108, revalidação do PER-107 corrente e TRN-111 ponta a ponta;
- P0B de Meus Coletivos e Central;
- áreas P1 de comunicação especializada;
- dez estados residuais da UXA-055;
- compreensão inicial → Tela Hoje;
- publicação → descoberta;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados;
- operação interna restante do Coletivo.

## 9. Limites

A UXA-095 não valida `PER-108` ou `TRN-111`, não promove a nova versão visual de `PER-107` por inferência, não cria IDs, não promove jornadas e não inicia protótipo, teste com pessoas ou Engenharia.

## 10. Próxima iniciativa possível

> **UXA-096 — Validação Funcional do Início do Participante, Revalidação de PER-107 e Validação Integrada de GKR-TRN-111**

A UXA-096 depende de autorização separada e não é iniciada por este pacote.
