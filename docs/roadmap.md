---
id: ROADMAP-12.61.0
title: Roadmap Arquitetural — Gestão de Solicitações Materializada
status: active
version: 12.61.0
owner: Guivos
last_updated: 2026-08-07
supersedes_partial:
  - ROADMAP-12.60.0
related:
  - GKR-STATE-001
  - GPA-007
  - UXA-000
  - UXA-055
  - UXA-056
  - UXA-059
  - UXA-070
  - UXA-071
  - UXA-072
  - UXA-073
  - UXA-074
  - UXA-075
  - UXA-076
  - UXA-077
  - UXA-078
  - UXA-079
  - UXA-080
  - UXA-081
  - UXA-082
  - UXA-083
  - UXA-084
  - UXA-085
  - UXA-086
  - UXA-087
  - UXA-088
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - M7.75
---

# Roadmap Arquitetural — Gestão de Solicitações Materializada

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | gestão de solicitações do responsável materializada; validação pendente | UXA-088; M7.75 |
| Registros granulares | 40 superfícies e 37 transições | UXA-080; UXA-088 |
| Galeria visual | `active` 0.8.0; 105 SVGs | UXA-088 |
| página de Coletivos | `active` 0.6.0 | UXA-088 |
| matriz por SVG | 105 arquivos / 25 perfis; `active` 0.6.0 | UXA-088 |
| validações funcionais registradas | 88 | pacotes anteriores |
| pendentes de validação específica | 17 | UXA-055; UXA-088 |
| Jornadas principais | Pessoa, Coletivo e Organização em `draft` | Jornadas Integradas |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Sequência das Jornadas Integradas

```text
UXA-070 a UXA-075 — estruturação e promoção seletiva das Jornadas Integradas
→ UXA-076 a UXA-080 — registros granulares
→ UXA-081 a UXA-085 — galeria e matriz governadas
→ UXA-086 — COL-002 materializada
→ UXA-087 — COL-002 reformulada e validada
→ UXA-088 — COL-003 materializada em sete estados desktop
```

Nenhuma etapa inicia automaticamente a seguinte.

## 4. Resultado da UXA-088

| Dimensão | Resultado |
|---|---|
| superfície materializada | GKR-SURF-COL-003 — gestão de solicitações |
| canal | computador protegido |
| SVGs adicionados | 7 |
| SVGs totais | 105 |
| novo perfil | R25 |
| perfis totais | 25 |
| validações funcionais | 88 |
| pendentes | 17 |
| TRN-105 a TRN-109 | nova evidência do lado responsável; continuam parciais |
| GKR-TRN-112 | ambos endpoints materializados; continua parcial |
| GKR-SURF-PER-106 | ausente |
| jornadas promovidas | 0 |
| Engenharia iniciada | não |

## 5. Estados da materialização

- fila operacional;
- detalhe comum;
- análise protegida;
- pedido de informação adicional;
- confirmação de aprovação;
- confirmação de recusa;
- autoridade insuficiente.

Expiração e cancelamento pela Pessoa permanecem eventos, não decisões equivalentes do responsável.

## 6. Trilha governada

```text
COL-002 validada
→ COL-003 materializada
→ validar funcionalmente COL-003 em pacote próprio
→ somente depois avaliar continuidade bilateral e avanço para PER-106
```

Materialização e validação continuam atos distintos.

## 7. Prioridade de Coletivos

```text
COL-002 — validada
→ COL-003 — materializada; validação pendente
→ PER-106 — Meus Coletivos, ausente
→ PER-107 — Central de Atualizações, ausente
→ PER-108 — Início do Participante, reformulação pendente
```

## 8. Dívidas preservadas

- sete estados da UXA-088 sem validação;
- dez estados da UXA-055 sem validação;
- handoffs bilaterais de solicitação sem validação integrada;
- compreensão inicial → Tela Hoje;
- publicação → descoberta;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados.

## 9. Limites

A UXA-088 não materializa `PER-106`, `PER-107`, `PER-108` ou `COL-004` a `COL-008`, não promove jornadas e não inicia protótipo, teste com pessoas ou Engenharia.

## 10. Próxima iniciativa possível

> **UXA-089 — Validação Funcional da Gestão de Solicitações do Responsável do Coletivo**

A UXA-089 depende de autorização separada e não é iniciada por este pacote.
