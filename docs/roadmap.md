---
id: ROADMAP-12.64.0
title: Roadmap Arquitetural — Meus Coletivos Materializada
status: active
version: 12.64.0
owner: Guivos
last_updated: 2026-08-07
supersedes_partial:
  - ROADMAP-12.63.0
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
  - UXA-091
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - M7.78
---

# Roadmap Arquitetural — Meus Coletivos Materializada

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | Meus Coletivos materializada; continuidade pós-aprovação refinada e ainda não revalidada | UXA-091; M7.78 |
| Registros granulares | 40 superfícies e 37 transições | UXA-080; UXA-091 |
| Galeria visual | `active` 0.10.0; 106 SVGs | UXA-091 |
| página de Coletivos | `active` 0.8.0 | UXA-091 |
| matriz por SVG | 106 arquivos / 26 perfis; `active` 0.8.0 | UXA-091 |
| validações funcionais vigentes de SVG | 94 | UXA-091 e pacotes anteriores |
| pendentes de validação específica | 12 | UXA-055; UXA-091 |
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
→ UXA-088 — COL-003 materializada
→ UXA-089 — COL-003 reformulada e validada
→ UXA-090 — cinco handoffs elegíveis validados ponta a ponta
→ UXA-091 — PER-106 materializada e continuidade pós-aprovação refinada
```

Nenhuma etapa inicia automaticamente a seguinte.

## 4. Resultado da UXA-091

| Dimensão | Resultado |
|---|---|
| GKR-SURF-PER-106 | materializado; validação pendente |
| SVG novo | `uxa-091-my-collectives-mobile.svg` |
| estado aprovado de PER-105 | reformulado; revalidação pendente |
| GKR-TRN-108 | parcial; destino agora materializado |
| GKR-TRN-110 | parcial; origem materializada e PER-107 ausente |
| GKR-SURF-PER-107 | ausente |
| GKR-SURF-PER-108 | reformulação pendente |
| SVGs totais | 106 |
| perfis totais | 26 |
| validações vigentes | 94 |
| pendentes | 12 |
| jornadas promovidas | 0 |
| Engenharia iniciada | não |

## 5. Contrato de Meus Coletivos

`PER-106` deverá organizar vínculos sem misturar estados:

- Participando;
- Acompanhando;
- Solicitações;
- Convites;
- Participações pausadas;
- histórico quando necessário.

A superfície não cria ranking, pontuação de engajamento, sequência obrigatória, função automática, autoridade automática, presença obrigatória ou notificação automática.

## 6. Continuidade de aprovação refinada

```text
COL-003 — aprovação confirmada
→ resultado aprovado em PER-105
→ ação consciente “Ver em Meus Coletivos”
→ PER-106 — vínculo confirmado visível
```

Essa passagem agora possui materialização suficiente para ser examinada, mas continua `parcial` porque as versões correntes de `PER-105` aprovado e `PER-106` ainda não foram validadas funcionalmente em conjunto.

## 7. Trilha governada

```text
COL-002 validada
→ TRN-112 integralmente validada
→ COL-003 validada
↔ TRN-105/106/107/109 integralmente validadas com PER-105
→ UXA-091 materializa PER-106 e refina TRN-108
→ validar PER-106 + estado aprovado corrente + TRN-108
→ somente depois avaliar materialização de PER-107
```

## 8. Prioridade de Coletivos

```text
COL-002 — validada
→ COL-003 — validada
→ TRN-105/106/107/109/112 — integralmente validadas
→ PER-105 aprovado — reformulado; revalidação pendente
→ TRN-108 — parcial
→ PER-106 — materializado; validação pendente
→ TRN-110 — parcial
→ PER-107 — ausente
→ PER-108 — reformulação pendente
```

## 9. Dívidas preservadas

- validação funcional de `PER-106` e revalidação de `TRN-108`;
- `PER-107` e `PER-108` ainda não materializadas na forma vigente;
- dez estados da UXA-055 sem validação;
- compreensão inicial → Tela Hoje;
- publicação → descoberta;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados;
- operação interna restante do Coletivo.

## 10. Limites

A UXA-091 não valida `PER-106`, não fecha `TRN-108`, não materializa `PER-107`, `PER-108` ou `COL-004` a `COL-008`, não cria novo ID ou transição, não promove jornadas e não inicia protótipo, teste com pessoas ou Engenharia.

## 11. Próxima iniciativa possível

> **UXA-092 — Validação Funcional de Meus Coletivos e Revalidação da Continuidade Pós-Aprovação**

A UXA-092 depende de autorização separada e não é iniciada por este pacote.
