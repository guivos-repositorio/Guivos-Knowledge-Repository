---
id: ROADMAP-12.63.0
title: Roadmap Arquitetural — Handoffs de Solicitação Validados
status: active
version: 12.63.0
owner: Guivos
last_updated: 2026-08-07
supersedes_partial:
  - ROADMAP-12.62.0
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
  - UXA-090
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - M7.77
---

# Roadmap Arquitetural — Handoffs de Solicitação Validados

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | cinco handoffs de solicitação validados ponta a ponta; continuidade pós-aprovação parcial | UXA-090; M7.77 |
| Registros granulares | 40 superfícies e 37 transições | UXA-080; UXA-090 |
| Galeria visual | `active` 0.9.0; 105 SVGs | UXA-089 |
| página de Coletivos | `active` 0.7.0 | UXA-089 |
| matriz por SVG | 105 arquivos / 25 perfis; `active` 0.7.0 | UXA-089 |
| validações funcionais de SVG | 95 | UXA-089 e pacotes anteriores |
| pendentes de validação específica | 10 | UXA-055 |
| handoffs integralmente validados | 5 | UXA-090 |
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
→ UXA-090 — cinco handoffs elegíveis validados ponta a ponta
```

Nenhuma etapa inicia automaticamente a seguinte.

## 4. Resultado da UXA-090

| Dimensão | Resultado |
|---|---|
| GKR-TRN-105 | integralmente validada |
| GKR-TRN-106 | integralmente validada |
| GKR-TRN-107 | integralmente validada |
| GKR-TRN-109 | integralmente validada |
| GKR-TRN-112 | integralmente validada |
| GKR-TRN-108 | parcial |
| PER-106 | ausente |
| SVGs adicionados | 0 |
| transições adicionadas | 0 |
| jornadas promovidas | 0 |
| Engenharia iniciada | não |

## 5. Contrato integrado consolidado

Os cinco handoffs validados preservam:

- identidade lógica estável da solicitação;
- um único estado canônico vigente;
- autoridade revalidada antes de efeito;
- dados mínimos e finalidade declarada;
- resolução de concorrência entre cancelamento, expiração, resposta e decisão;
- estado obsoleto incapaz de sobrescrever evento mais recente;
- efeito lógico único diante de repetição ou reenvio;
- retorno e interrupção sem decisão implícita.

A validação é documental e funcional. Não especifica API, lock, fila, persistência ou implementação técnica.

## 6. Continuidade de aprovação

`GKR-TRN-108` permanece fora do fechamento integrado porque:

1. `GKR-SURF-PER-106 — Meus Coletivos` ainda não está materializada;
2. o resultado `aprovada` já é observável na família `PER-105` antes da futura entrada no ambiente do participante.

A futura materialização de `PER-106` deverá refinar explicitamente essa passagem, sem pular o resultado compreensível da solicitação.

## 7. Trilha governada

```text
COL-002 validada
→ TRN-112 integralmente validada
→ COL-003 validada
↔ TRN-105/106/107/109 integralmente validadas com PER-105
→ TRN-108 parcial
→ materializar PER-106 e refinar continuidade pós-aprovação
```

## 8. Prioridade de Coletivos

```text
COL-002 — validada
→ COL-003 — validada
→ TRN-105/106/107/109/112 — integralmente validadas
→ TRN-108 + PER-106 — continuidade parcial / superfície ausente
→ PER-107 — Central de Atualizações, ausente
→ PER-108 — Início do Participante, reformulação pendente
```

## 9. Dívidas preservadas

- `PER-106` e continuidade pós-aprovação;
- dez estados da UXA-055 sem validação;
- compreensão inicial → Tela Hoje;
- publicação → descoberta;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados;
- operação interna restante do Coletivo.

## 10. Limites

A UXA-090 não materializa `PER-106`, `PER-107`, `PER-108` ou `COL-004` a `COL-008`, não promove jornadas, não cria novo SVG ou transição e não inicia protótipo, teste com pessoas ou Engenharia.

## 11. Próxima iniciativa possível

> **UXA-091 — Materialização Controlada de Meus Coletivos (`GKR-SURF-PER-106`) e Refinamento da Continuidade Pós-Aprovação**

A UXA-091 depende de autorização separada e não é iniciada por este pacote.
