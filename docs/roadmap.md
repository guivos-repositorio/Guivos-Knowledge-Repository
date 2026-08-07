---
id: ROADMAP-12.62.0
title: Roadmap Arquitetural — Gestão de Solicitações Validada
status: active
version: 12.62.0
owner: Guivos
last_updated: 2026-08-07
supersedes_partial:
  - ROADMAP-12.61.0
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
  - UXA-089
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - M7.76
---

# Roadmap Arquitetural — Gestão de Solicitações Validada

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | gestão de solicitações do responsável reformulada e validada; handoffs pendentes | UXA-089; M7.76 |
| Registros granulares | 40 superfícies e 37 transições | UXA-080; UXA-089 |
| Galeria visual | `active` 0.9.0; 105 SVGs | UXA-089 |
| página de Coletivos | `active` 0.7.0 | UXA-089 |
| matriz por SVG | 105 arquivos / 25 perfis; `active` 0.7.0 | UXA-089 |
| validações funcionais registradas | 95 | UXA-089 e pacotes anteriores |
| pendentes de validação específica | 10 | UXA-055 |
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
→ UXA-089 — COL-003 reformulada e validada funcionalmente
```

Nenhuma etapa inicia automaticamente a seguinte.

## 4. Resultado da UXA-089

| Dimensão | Resultado |
|---|---|
| superfície validada | GKR-SURF-COL-003 — gestão de solicitações |
| canal | computador protegido |
| SVGs existentes na família | 7 |
| SVGs reformulados | 6 |
| SVGs totais | 105 |
| perfis totais | 25 |
| validações funcionais | 95 |
| pendentes | 10, exclusivamente UXA-055 |
| TRN-105, 106, 107, 109 e 112 | endpoints validados como superfícies; continuam parciais |
| GKR-TRN-108 | origem validada; PER-106 ausente; continua parcial |
| GKR-SURF-PER-106 | ausente |
| jornadas promovidas | 0 |
| Engenharia iniciada | não |

## 5. Reformulações funcionais consolidadas

- fila distingue estimativa de prazo de resposta;
- ordenação não cria prioridade substantiva automática;
- critérios de decisão precisam ter sido apresentados à Pessoa;
- pedido adicional não usa acessibilidade como barreira de entrada;
- acessibilidade permanece responsabilidade de acomodação;
- autoridade é verificada pelo escopo concedido;
- confirmação não cria nem amplia permissão;
- aprovação e recusa preservam fundamento e consequência;
- autoridade insuficiente não oferece autoelevação de permissão.

## 6. Trilha governada

```text
COL-002 validada
→ COL-003 materializada e validada
→ validar integralmente os handoffs bilaterais elegíveis
→ somente depois avaliar materialização de PER-106
```

`GKR-TRN-108` permanece fora do fechamento integrado enquanto `GKR-SURF-PER-106` estiver ausente.

## 7. Prioridade de Coletivos

```text
COL-002 — validada
→ COL-003 — validada no escopo da superfície
→ TRN-105/106/107/109/112 — validação integrada pendente
→ PER-106 — Meus Coletivos, ausente
→ PER-107 — Central de Atualizações, ausente
→ PER-108 — Início do Participante, reformulação pendente
```

## 8. Dívidas preservadas

- dez estados da UXA-055 sem validação;
- handoffs bilaterais de solicitação sem validação integrada;
- `TRN-108` bloqueada por `PER-106` ausente;
- compreensão inicial → Tela Hoje;
- publicação → descoberta;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados.

## 9. Limites

A UXA-089 não materializa `PER-106`, `PER-107`, `PER-108` ou `COL-004` a `COL-008`, não promove jornadas e não inicia protótipo, teste com pessoas ou Engenharia.

## 10. Próxima iniciativa possível

> **UXA-090 — Validação Integrada dos Handoffs Bilaterais de Solicitação em Coletivos**

A UXA-090 deverá examinar `GKR-TRN-105`, `106`, `107`, `109` e `112` como ligações entre superfícies já validadas. `GKR-TRN-108` continuará parcial enquanto `GKR-SURF-PER-106` permanecer ausente.

A UXA-090 depende de autorização separada e não é iniciada por este pacote.
